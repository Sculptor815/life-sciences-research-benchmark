"""Audit a frozen raw-data reproduction submission against private numerical targets.

This checks evidence completeness and numeric agreement, not biological truth or
the honesty of a submitted execution log. A coordinator must independently run
the frozen code under network isolation before assigning agent capability credit.
"""
import math
from .storage import digest, file_hash, within


def check_reproduction(spec, submission, root):
    required=("paper_doi","figure_panels","raw_inputs","reference_build","software_lock","targets")
    if any(not spec.get(k) for k in required):
        raise ValueError("Reproduction specification needs paper, panels, raw inputs, reference, environment and frozen numerical targets")
    if submission.get("spec_sha256") != digest(spec):
        raise ValueError("Submission belongs to another frozen reproduction specification")
    inputs=spec["raw_inputs"]
    if any(x.get("level") != "raw" or not x.get("accession") or not x.get("license") for x in inputs):
        raise ValueError("Raw-data credit requires genuine raw inputs with accession and usage terms")
    for asset in inputs:
        if file_hash(within(root,asset["path"])) != asset["sha256"]:
            raise ValueError("Raw input checksum mismatch")
    for name in ("code", "environment", "execution_log", "figure", "derived_table"):
        artifact=submission.get("artifacts",{}).get(name,{})
        if not artifact.get("path") or file_hash(within(root,artifact["path"])) != artifact.get("sha256"):
            raise ValueError("Missing or modified reproduction artifact: "+name)
    metrics=submission.get("metrics",{})
    if set(metrics) != set(spec["targets"]):
        raise ValueError("All prespecified metrics must be reported; selective omission is prohibited")
    results={}
    for name,target in spec["targets"].items():
        actual=metrics[name]
        values=[actual,target.get("expected"),target.get("absolute_tolerance"),target.get("relative_tolerance")]
        if any(type(v) not in (int,float) or not math.isfinite(v) for v in values) or min(values[2:]) < 0:
            raise ValueError("Metrics and tolerances must be finite numbers with nonnegative tolerances")
        tolerance=max(values[2],abs(values[1])*values[3])
        results[name]={"actual":actual,"expected":values[1],"tolerance":tolerance,"within_tolerance":abs(actual-values[1])<=tolerance}
    return {"spec_sha256":digest(spec),"numerical_agreement":all(x["within_tolerance"] for x in results.values()),
            "metrics":results,"scope":spec.get("scope","unspecified"),
            "agent_capability_verified":False,
            "remaining_checks":["Independently execute the frozen submitted code from the supplied raw files", "Verify OS/network isolation and absence of reference-output access", "Review preprocessing, exclusions, experimental units and alternative explanations", "Check that plotted values actually come from the derived table; visual similarity alone is insufficient"]}
