from collections import defaultdict
from pathlib import Path
from statistics import mean

from .dataset import load_dataset
from .grading import resolve_ratings, validate_key
from .storage import digest, file_hash, read_json, write_new
from .taxonomy import DIMENSIONS, DOMAINS


def calibration(records):
    """Records are actual independent human scores, never model-generated ratings."""
    if not records:
        raise ValueError("Calibration records required")
    differences, exact, within_one, totals = [], [], [], []
    for record in records:
        pair = record["ratings"]
        resolve_ratings(pair, record["ability"])
        a, b = pair
        for dim in DIMENSIONS[record["ability"]]:
            diff = abs(a["scores"][dim]-b["scores"][dim])
            differences.append({"dimension":dim,"difference":diff})
            exact.append(diff==0)
            within_one.append(diff<=1)
        totals.append(abs(sum(a["scores"].values())-sum(b["scores"].values()))*5)
    dims = sorted({d["dimension"] for d in differences})
    return {"pairs":len(records), "dimension_exact_agreement":mean(exact), "dimension_within_one_agreement":mean(within_one),
            "total_mean_absolute_difference_percentage_points":mean(totals),
            "dimensions":{d:{"exact_agreement":mean(x["difference"]==0 for x in differences if x["dimension"]==d), "n":sum(x["dimension"]==d for x in differences)} for d in dims},
            "records_sha256":digest(records)}


def lock_dataset(dataset, keys_path, approvals_path, calibration_path, output):
    items = load_dataset(dataset, formal=True)
    keys = read_json(keys_path)
    approvals = read_json(approvals_path)
    training = read_json(calibration_path)
    roster = approvals["domain_roster"]
    for domain in DOMAINS:
        entry = roster[domain]
        if len(entry["reviewers"]) < 2 or len(set(entry["reviewers"])) != len(entry["reviewers"]) or entry["adjudicator"] in entry["reviewers"] or not entry["adjudicator"]:
            raise ValueError("Each domain needs two reviewers and a separate adjudicator")
    checks = ("source_checked", "independent_trial_answer", "rubric_checked", "material_rights_checked")
    for item in items:
        validate_key(item, keys[item["id"]])
        entry = approvals["items"][item["id"]]
        if len(entry) != 2 or len({x["reviewer"] for x in entry}) != 2:
            raise ValueError("Every item requires two independent approvals")
        for approval in entry:
            if approval["reviewer"] not in roster[item["domain"]]["reviewers"] or not all(approval.get(k) is True for k in checks) or not approval.get("date"):
                raise ValueError("Incomplete expert approval")
    public_ids = {i["id"] for i in items if i["split"]=="public"}
    if set(training["completed_public_ids"]) != public_ids or len(public_ids) != 64:
        raise ValueError("Calibration must cover all 64 public items")
    expected_open = {i["id"] for i in items if i["split"]=="public" and i["ability"]!="knowledge"}
    if {r["item_id"] for r in training["records"]} != expected_open:
        raise ValueError("Calibration needs actual paired ratings for all public open items")
    stats = calibration(training["records"])
    if not training.get("accepted_by") or not training.get("acceptance_rationale") or training.get("unresolved_systematic_disagreement") is not False:
        raise ValueError("A human coordinator must resolve systematic differences and document calibration acceptance")
    result = {"dataset_sha256":digest(items), "keys_sha256":file_hash(keys_path), "approvals_sha256":file_hash(approvals_path),
              "calibration_sha256":file_hash(calibration_path), "calibration_summary":stats,
              "approved_ids":sorted(i["id"] for i in items), "domain_roster":roster, "lock_version":"1.0"}
    write_new(output, result)
    return result
