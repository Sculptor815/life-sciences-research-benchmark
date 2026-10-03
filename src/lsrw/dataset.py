import re
from collections import Counter, defaultdict
from pathlib import Path

from .storage import digest, file_hash, read_json, read_jsonl, within
from .taxonomy import ABILITIES, CELL_COUNTS, DOMAINS, TOPICS

FIELDS = {"id", "family_id", "source_family", "domain", "ability", "topics", "techniques", "context", "difficulty", "modality", "split", "language", "status", "prompt", "choices", "response_type", "word_limit", "materials", "packet", "version"}
MATERIAL_FIELDS = {"path", "sha256", "media_type", "license", "credit", "origin", "processing"}


def validate(items, root, formal=False):
    errors = [] if items else ["Dataset is empty"]
    ids, families, sources = set(), defaultdict(set), defaultdict(set)
    counts = Counter()
    coverage = defaultdict(set)
    for item in items:
        if not isinstance(item, dict):
            errors.append("Every item must be an object")
            continue
        name = str(item.get("id", "<missing>"))
        def fail(message):
            errors.append(f"{name}: {message}")
        if set(item) != FIELDS:
            fail(f"fields differ: missing={sorted(FIELDS-set(item))}; unknown={sorted(set(item)-FIELDS)}")
            continue
        string_fields = FIELDS - {"topics", "techniques", "choices", "materials", "word_limit"}
        if any(not isinstance(item[k], str) for k in string_fields) or not isinstance(item["choices"], dict) or any(not isinstance(item[k], list) for k in ("topics","techniques","materials")) or any(not isinstance(x,str) for k in ("topics","techniques") for x in item[k]):
            fail("invalid field types")
            continue
        if not re.fullmatch(r"[a-z0-9][a-z0-9_-]{2,79}", name) or name in ids:
            fail("invalid or duplicate ID")
        ids.add(name)
        if item["domain"] not in DOMAINS or item["ability"] not in ABILITIES:
            fail("unknown domain or ability")
        if (item["split"], item["modality"]) not in CELL_COUNTS:
            fail("invalid split/modality")
        if item["language"] != "en" or not item["prompt"].strip():
            fail("English language and a nonempty prompt required")
        if item["status"] not in ("draft", "reviewed") or (formal and item["status"] != "reviewed"):
            fail("formal items must have reviewed status")
        if item["difficulty"] not in ("undergraduate", "graduate"):
            fail("invalid difficulty")
        if type(item["word_limit"]) is not int or not 301 <= item["word_limit"] <= 12000:
            fail("word_limit must be an integer from 301 to 12000")
        if not item["family_id"] or not item["source_family"]:
            fail("case and source families are required")
        families[item["family_id"]].add(item["split"])
        sources[item["source_family"]].add(item["split"])
        counts[item["domain"], item["ability"], item["split"], item["modality"]] += 1
        if not isinstance(item["topics"], list) or not item["topics"]:
            fail("topic tags required")
        else:
            coverage[item["domain"]].update(item["topics"])
        if item["response_type"] != "open" or item["choices"]:
            fail("All current questions require open responses without answer choices")
        if not isinstance(item["packet"], str):
            fail("packet must be visible text, never hidden metadata")
        if not item["packet"].strip():
            fail("Every question requires a fixed evidence packet")
        if (item["modality"] == "image") != bool(item["materials"]):
            fail("images required only for image track")
        for asset in item["materials"]:
            if not isinstance(asset, dict) or set(asset) != MATERIAL_FIELDS or any(not isinstance(x, str) for x in asset.values()):
                fail("invalid material fields")
                continue
            try:
                path = within(root, asset["path"])
                if path.suffix.lower() not in (".png", ".jpg", ".jpeg") or asset["media_type"] not in ("image/png", "image/jpeg"):
                    fail("only PNG/JPEG assets supported")
                if file_hash(path) != asset["sha256"]:
                    fail("material hash mismatch")
                if not all(asset[k] for k in ("license", "credit", "origin", "processing")):
                    fail("material provenance incomplete")
            except (ValueError, OSError) as exc:
                fail(f"unreadable material: {type(exc).__name__}")
    for grouping, groups in (("case", families), ("source", sources)):
        errors.extend(f"{grouping} family crosses public/heldout: {key}" for key, splits in groups.items() if len(splits) > 1)
    if formal:
        for domain in DOMAINS:
            missing = set(TOPICS[domain]) - coverage[domain]
            if missing:
                errors.append(f"{domain}: missing topics {sorted(missing)}")
            for ability in ABILITIES:
                for (split, modality), expected in CELL_COUNTS.items():
                    actual = counts[domain, ability, split, modality]
                    if actual != expected:
                        errors.append(f"{domain}/{ability}/{split}/{modality}: {actual}, expected {expected}")
    return errors


def load_dataset(path, formal=False):
    path = Path(path).resolve()
    items = read_jsonl(path)
    errors = validate(items, path.parent, formal)
    if errors:
        raise ValueError("Dataset validation failed:\n" + "\n".join(errors))
    return items


def verify_lock(items, lock_path, key_path):
    lock = read_json(lock_path)
    if lock.get("dataset_sha256") != digest(items) or lock.get("keys_sha256") != file_hash(key_path):
        raise ValueError("Dataset or rubric differs from locked version")
    if lock.get("approved_ids") != sorted(x["id"] for x in items):
        raise ValueError("Lock approval inventory mismatch")
    return lock
