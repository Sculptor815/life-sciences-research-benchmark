import json
import math
import re

from .storage import number
from .taxonomy import DIMENSIONS, SOURCE_STATES, SUPPORT_STATES


def validate_key(item, key):
    if key.get("id") != item["id"] or not key.get("version") or not key.get("references"):
        raise ValueError("Key ID, version and references required")
    if item["response_type"] == "choice":
        if key.get("answer") not in item["choices"]:
            raise ValueError("Choice key missing or invalid")
    elif item["response_type"] == "numeric":
        if not number(key.get("absolute_tolerance")) or not number(key.get("relative_tolerance")) or not isinstance(key.get("units"), list) or not key["units"]:
            raise ValueError("Numeric units and nonnegative tolerances required")
        if not isinstance(key.get("value"), (int, float)) or not math.isfinite(key["value"]):
            raise ValueError("Numeric answer must be finite")
    else:
        dims = key.get("dimensions", {})
        if set(dims) != set(DIMENSIONS[item["ability"]]):
            raise ValueError("Rubric dimensions do not match ability")
        for dim in dims.values():
            if set(dim.get("anchors", {})) != set("01234") or not all(dim["anchors"].values()) or not dim.get("acceptable_alternatives") or not dim.get("critical_errors"):
                raise ValueError("Every dimension needs 0–4 anchors, alternatives and critical errors")
        if item["ability"] == "paper_appraisal" and (key.get("source_state") not in SOURCE_STATES or key.get("support_state") not in SUPPORT_STATES):
            raise ValueError("Paper source and support labels required")


def objective_score(text, key, response_type):
    text = text.strip()
    if text.startswith("```"):
        text = re.sub(r"^```(?:json)?\s*|\s*```$", "", text)
    try:
        value = json.loads(text)
        if not isinstance(value, dict):
            raise ValueError()
        if response_type == "choice":
            answer = value.get("answer")
            if answer not in ("A", "B", "C", "D"):
                raise ValueError()
            return {"score": 100.0 if answer == key["answer"] else 0.0, "format_valid": True}
        answer = value.get("value")
        if type(answer) not in (int, float) or not math.isfinite(answer) or not isinstance(value.get("unit"), str):
            raise ValueError()
        tolerance = max(key["absolute_tolerance"], abs(key["value"])*key["relative_tolerance"])
        good = abs(answer-key["value"]) <= tolerance and value["unit"].strip() in key["units"]
        return {"score": 100.0 if good else 0.0, "format_valid": True}
    except (ValueError, TypeError):
        return {"score": 0.0, "format_valid": False}


def validate_rating(rating, ability):
    required = {"reviewer", "scores", "rationale", "source_correct", "conclusion_correct", "refusal"}
    if set(rating) != required or not rating["reviewer"] or not rating["rationale"].strip():
        raise ValueError("Rating fields and a written rationale are required")
    if set(rating["scores"]) != set(DIMENSIONS[ability]) or any(type(v) is not int or not 0 <= v <= 4 for v in rating["scores"].values()):
        raise ValueError("Every dimension must have an integer score 0–4")
    if type(rating["refusal"]) is not bool:
        raise ValueError("Explicit refusal judgment required")
    for field in ("source_correct", "conclusion_correct"):
        if (ability == "paper_appraisal" and type(rating[field]) is not bool) or (ability != "paper_appraisal" and rating[field] is not None):
            raise ValueError("Paper subjudgments must be booleans; other tasks use null")


def resolve_ratings(ratings, ability, adjudication=None):
    if len(ratings) != 2 or ratings[0]["reviewer"] == ratings[1]["reviewer"]:
        raise ValueError("Two different independent reviewers are required")
    for rating in ratings:
        validate_rating(rating, ability)
    left, right = ratings
    dimension_disagreement = any(abs(left["scores"][d]-right["scores"][d]) >= 2 for d in DIMENSIONS[ability])
    total_disagreement = abs(sum(left["scores"].values())-sum(right["scores"].values()))*5 > 10
    # Contradictory categorical judgments also require explicit resolution.
    categories_disagree = any(left[f] != right[f] for f in ("source_correct", "conclusion_correct", "refusal"))
    needs = dimension_disagreement or total_disagreement or categories_disagree
    if needs:
        if adjudication is None:
            return {"status": "needs_adjudication", "disagreement": True}
        validate_rating(adjudication, ability)
        if adjudication["reviewer"] in {left["reviewer"], right["reviewer"]}:
            raise ValueError("Adjudicator must be a third reviewer")
        result = dict(adjudication)
    else:
        if adjudication is not None:
            raise ValueError("Unnecessary adjudication is not permitted")
        result = {"scores": {d:(left["scores"][d]+right["scores"][d])/2 for d in DIMENSIONS[ability]},
                  **{f:left[f] for f in ("source_correct", "conclusion_correct", "refusal")}}
    return {"status": "scored", "score": sum(result["scores"].values())*5,
            "dimensions": result["scores"], "source_correct": result["source_correct"],
            "conclusion_correct": result["conclusion_correct"], "refusal": result["refusal"], "disagreement": needs}
