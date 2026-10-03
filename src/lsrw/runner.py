import datetime as dt
import importlib.metadata
import json
import platform
import time
import uuid
from pathlib import Path

from . import __version__
from .adapters import InspectAdapter, MockAdapter, RunError
from .dataset import load_dataset, verify_lock
from .prompts import visible_request
from .storage import digest, file_hash, number, read_json, within, write_new
from .taxonomy import SAMPLES


def response_slots(item):
    return [(item["id"] if n == 1 else item["id"]+f"--sample-{n}", n) for n in range(1, SAMPLES[item["ability"]]+1)]

REQUIRED = {"dataset", "output_root", "backend", "model", "track", "split", "formal", "supports_images", "max_output_tokens", "timeout_seconds", "generation", "budget_usd", "input_usd_per_million", "output_usd_per_million", "input_token_ceiling"}
OPTIONAL = {"mock_events", "lock", "keys", "dataset_version", "pricing_date", "pricing_source", "evidence_mode"}


def load_config(path):
    config = read_json(path)
    if REQUIRED - set(config) or set(config) - REQUIRED - OPTIONAL:
        raise ValueError("Invalid config fields; see configs/mock.json")
    if config["backend"] not in ("mock", "inspect") or config["track"] not in ("text", "image", "all") or config["split"] not in ("public", "heldout"):
        raise ValueError("Invalid backend, track or split")
    if config.get("evidence_mode", "fixed_packet") != "fixed_packet":
        raise ValueError("Question evaluation supports fixed_packet evidence only; browsing is prohibited")
    if not isinstance(config["model"], str) or not config["model"].strip():
        raise ValueError("Exact model identifier is required")
    for key in ("budget_usd", "input_usd_per_million", "output_usd_per_million"):
        if not number(config[key]):
            raise ValueError(f"Invalid {key}")
    for key in ("max_output_tokens", "input_token_ceiling", "timeout_seconds"):
        if type(config[key]) is not int or config[key] <= 0:
            raise ValueError(f"Invalid {key}")
    for key in ("formal", "supports_images"):
        if type(config[key]) is not bool:
            raise ValueError(f"{key} must be boolean")
    allowed_generation = {"temperature", "top_p", "seed", "reasoning_effort", "reasoning_tokens"}
    if not isinstance(config["generation"], dict) or set(config["generation"]) - allowed_generation:
        raise ValueError("Unsupported generation parameter; tool/retry overrides prohibited")
    if "seed" in config["generation"] and type(config["generation"]["seed"]) is not int:
        raise ValueError("A configured seed must be an integer")
    if config["backend"] == "inspect" and (config["budget_usd"] <= 0 or config["input_usd_per_million"] <= 0 or config["output_usd_per_million"] <= 0 or not config.get("pricing_date") or not config.get("pricing_source")):
        raise ValueError("Paid runs require a budget and dated input/output price estimates")
    if config["formal"] and (config["backend"] == "mock" or config["model"].split("/")[0] in ("mock", "mockllm") or config["split"] != "heldout" or not config.get("lock") or not config.get("keys")):
        raise ValueError("Formal runs need heldout items, a reviewed lock, and external keys")
    for key in ("dataset", "output_root", "lock", "keys"):
        if key in config:
            config[key] = str((Path(path).resolve().parent / config[key]).resolve())
    return config


def prepare(config):
    if config.get("evidence_mode", "fixed_packet") != "fixed_packet":
        raise ValueError("Question evaluation cannot enable browsing")
    items = load_dataset(config["dataset"], formal=config["formal"])
    if config["formal"]:
        verify_lock(items, config["lock"], config["keys"])
    selected = [i for i in items if i["split"] == config["split"] and (config["track"] == "all" or i["modality"] == config["track"])]
    if not selected:
        raise ValueError("No items match this configuration")
    root = Path(config["dataset"]).parent
    requests = [visible_request(i, root) for i in selected]
    ceiling = config["input_token_ceiling"]
    # UTF-8 byte count is a deliberately loose bound for text with byte-tokenizing models.
    for request in requests:
        if len((request["system"] + request["text"]).encode("utf-8")) + 512 > ceiling:
            raise ValueError("input_token_ceiling is too small for the text packet plus message overhead")
    reservation = (ceiling * config["input_usd_per_million"] + config["max_output_tokens"] * config["output_usd_per_million"]) / 1e6
    return selected, requests, reservation


def dry_run(config):
    items, _, reservation = prepare(config)
    requests = sum(SAMPLES[i["ability"]] for i in items)
    return {"questions": len(items), "initial_requests": requests, "maximum_attempts": requests*3,
            "independent_samples_by_ability":SAMPLES,
            "per_attempt_reserved_usd": reservation, "one_pass_estimate_usd": reservation*requests,
            "including_two_retries_estimate_usd": reservation*requests*3,
            "budget_usd": config["budget_usd"], "backend": config["backend"], "model": config["model"],
            "notice": "Estimates and maximum_attempts cover workbench-visible calls, not a guaranteed provider billing cap. Provider internal calls are not observable. Configure provider billing limits; image token ceilings must cover provider image accounting."}


def execute(config, adapter=None, sleep=time.sleep):
    items, requests, reservation = prepare(config)
    run_id = dt.datetime.now(dt.timezone.utc).strftime("%Y%m%dT%H%M%SZ") + "-" + uuid.uuid4().hex[:8]
    root = Path(config["output_root"]) / run_id
    root.mkdir(parents=True, exist_ok=False)
    snapshot = json.loads(json.dumps(items))
    for item in snapshot:
        for asset in item["materials"]:
            src = within(Path(config["dataset"]).parent, asset["path"])
            dest = within(root / "dataset", asset["path"])
            dest.parent.mkdir(parents=True, exist_ok=True)
            with dest.open("xb") as stream:
                stream.write(src.read_bytes())
    write_new(root / "items.json", snapshot)
    safe_config = {k:v for k,v in config.items() if k not in ("keys", "lock", "mock_events")}
    source_hashes = {p.name:file_hash(p) for p in sorted(Path(__file__).parent.glob("*.py"))}
    manifest = {"run_id": run_id, "code_version": __version__, "code_sha256":digest(source_hashes), "source_files_sha256":source_hashes, "python_version": platform.python_version(), "config": safe_config,
                "config_sha256": digest(safe_config), "dataset_sha256": digest(items), "dataset_file_sha256": file_hash(config["dataset"]),
                "lock_sha256": file_hash(config["lock"]) if config.get("lock") else None,
                "keys_sha256": file_hash(config["keys"]) if config.get("keys") else None,
                "created_utc": dt.datetime.now(dt.timezone.utc).isoformat(), "questions": len(items),
                "sampling_policy":{"samples_by_ability":SAMPLES,"feedback_between_samples":False,"selection":"best complete answer; never merge partial answers","transport_retries_per_sample":2},
                "evidence_policy": {"mode":"fixed_packet", "model_tools":[], "tool_choice":"none",
                                    "external_retrieval":False, "answer_keys_in_request":False,
                                    "enforcement_scope":"client request and tool response validation; remote provider internals are not observable"}}
    write_new(root / "manifest.json", manifest)
    if config.get("lock"):
        write_new(root / "lock.json", read_json(config["lock"]))
    try:
        adapter = adapter or (MockAdapter(config) if config["backend"] == "mock" else InspectAdapter(config))
    except Exception:
        # Provider exception text can contain credentials. Record state only.
        write_new(root / "aborted.json", {"status":"adapter_initialization_failed", "calls_started":0,
                  "recorded_utc":dt.datetime.now(dt.timezone.utc).isoformat()})
        raise ValueError(f"Adapter initialization failed; no model calls started. Record: {root}") from None
    charged = 0.0
    statuses = []
    billing_uncertain = False
    scheduled = [(item, request, response_id, sample) for item,request in zip(items,requests) for response_id,sample in response_slots(item)]
    for item, request, response_id, sample in scheduled:
        record = {"id": response_id, "item_id":item["id"], "sample_number":sample, "request_sha256": digest(request), "attempts": [], "response": None, "status": "not_started"}
        sample_config = {**config, "generation":dict(config["generation"])}
        if "seed" in sample_config["generation"]:
            sample_config["generation"]["seed"] += sample-1
        record["generation"] = sample_config["generation"]
        start = time.monotonic()
        if item["modality"] == "image" and not config["supports_images"]:
            record["status"] = "unsupported_image"
        elif billing_uncertain:
            record["status"] = "budget_accounting_uncertain"
        else:
            for attempt in range(3):
                if charged + reservation > config["budget_usd"] + 1e-12:
                    record["status"] = "budget_exhausted"
                    break
                charged += reservation  # Keep reservation for failed calls too.
                try:
                    output = adapter.generate(request, sample_config)
                    record["response"] = output
                    record["status"] = "completed"
                    record["attempts"].append({"number": attempt+1, "status": "completed", "reserved_usd": reservation})
                    usage = (output.get("input_tokens"), output.get("output_tokens"))
                    if all(number(v) for v in usage):
                        estimate = (usage[0]*config["input_usd_per_million"] + usage[1]*config["output_usd_per_million"]) / 1e6
                        record["usage_estimated_cost_usd"] = estimate
                        if usage[0] > config["input_token_ceiling"] or usage[1] > config["max_output_tokens"] or estimate > reservation + 1e-12:
                            billing_uncertain = True
                    else:
                        record["usage_estimated_cost_usd"] = None
                        billing_uncertain = config["backend"] != "mock"
                    break  # Any valid API completion, including empty/refusal, ends the item.
                except RunError as exc:
                    record["status"] = exc.status
                    record["attempts"].append({"number": attempt+1, "status": exc.status, "reserved_usd": reservation})
                    if not exc.retryable or attempt == 2:
                        break
                    sleep(2**attempt)
        record["elapsed_seconds"] = time.monotonic() - start
        write_new(root / "responses" / (response_id + ".json"), record)
        statuses.append(record["status"])
    files = {str(p.relative_to(root)).replace("\\", "/"): file_hash(p) for p in sorted(root.rglob("*")) if p.is_file()}
    write_new(root / "completion.json", {"files": files, "adapter_version": adapter.version, "reserved_usd": charged,
               "billing_uncertain": billing_uncertain, "completed": statuses.count("completed"), "total": len(scheduled), "questions":len(items),
               "finished_utc": dt.datetime.now(dt.timezone.utc).isoformat()})
    if hasattr(adapter, "close"):
        adapter.close()
    return root


def verify_run(root):
    root = Path(root)
    if not (root / "completion.json").exists():
        raise ValueError("Run is incomplete or aborted; it cannot be scored")
    completion = read_json(root / "completion.json")
    for relative, expected in completion["files"].items():
        if file_hash(within(root, relative)) != expected:
            raise ValueError("Run was modified after completion: " + relative)
    return read_json(root / "manifest.json"), read_json(root / "items.json"), completion
