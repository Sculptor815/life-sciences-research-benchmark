import json
import math
import re
from datetime import date

from .storage import number
from .taxonomy import DIMENSIONS, SOURCE_STATES, SUPPORT_STATES, WEIGHTS, REFERENCE_MIN_WORDS, FOLLOWUP_FIELDS
from . import service


def word_count(text):
    return len(re.findall(r"\b[A-Za-z0-9]+(?:['’-][A-Za-z0-9]+)*\b", text))


def weighted_score(scores, ability):
    return sum(scores[d]*w/4 for d,w in zip(DIMENSIONS[ability], WEIGHTS[ability]))


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
        if not key.get("user_goal") or set(key.get("service_criteria",{})) != set(service.DIMENSIONS):
            raise ValueError("A concrete user goal and all user-service criteria are required")
        answer = key.get("reference_answer")
        if not isinstance(answer, str) or word_count(answer) < REFERENCE_MIN_WORDS[item["ability"]]:
            raise ValueError("Reference answer is missing or shorter than the ability-specific minimum")
        concepts, chain = key.get("required_concepts"), key.get("logic_chain")
        if not isinstance(concepts, list) or not concepts or any(not isinstance(c,dict) or not c.get("id") or not c.get("aliases") or not c.get("criterion") for c in concepts):
            raise ValueError("Item-specific concepts, aliases and contextual criteria required")
        if not isinstance(chain, list) or not chain or any(not isinstance(e,dict) or not all(e.get(k) for k in ("id","premise","inference","conclusion","evidence_location")) for e in chain):
            raise ValueError("Directed evidence-to-inference-to-conclusion links required")
        if item["ability"] != "essay" and not key.get("protocol_steps"):
            raise ValueError("Design and reasoning keys require ordered protocol steps")
        if item["ability"] == "research_reasoning":
            target=key.get("followup_target", {})
            if not target.get("original_source") or not target.get("later_source") or not target.get("author_overlap") or set(target.get("match_criteria",{})) != set(FOLLOWUP_FIELDS):
                raise ValueError("Research reasoning requires a private chronological author-followup target")
            try:
                original=date.fromisoformat(target['original_source']['public_date'])
                cutoff=date.fromisoformat(target['cutoff_date'])
                later=date.fromisoformat(target['later_source']['public_date'])
                if not original <= cutoff < later:
                    raise ValueError()
            except (KeyError,TypeError,ValueError):
                raise ValueError("Original, cutoff and later-source dates must form a valid chronological sequence") from None
        dims = key.get("dimensions", {})
        if set(dims) != set(DIMENSIONS[item["ability"]]):
            raise ValueError("Rubric dimensions do not match ability")
        for dim in dims.values():
            if set(dim.get("anchors", {})) != set("01234") or not all(dim["anchors"].values()) or not dim.get("acceptable_alternatives") or not dim.get("critical_errors"):
                raise ValueError("Every dimension needs 0–4 anchors, alternatives and critical errors")
        if "source_state" in key and (key.get("source_state") not in SOURCE_STATES or key.get("support_state") not in SUPPORT_STATES):
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
    required = {"reviewer", "scores", "rationale", "source_correct", "conclusion_correct", "refusal", "followup_match", "user_service"}
    if set(rating) != required or not rating["reviewer"] or not rating["rationale"].strip():
        raise ValueError("Rating fields and a written rationale are required")
    if set(rating["scores"]) != set(DIMENSIONS[ability]) or any(type(v) is not int or not 0 <= v <= 4 for v in rating["scores"].values()):
        raise ValueError("Every dimension must have an integer score 0–4")
    if type(rating["refusal"]) is not bool:
        raise ValueError("Explicit refusal judgment required")
    service.score(rating['user_service'])
    if any(type(v) is not int for v in rating['user_service'].values()):
        raise ValueError("Independent user-service ratings must be integers")
    for field in ("source_correct", "conclusion_correct"):
        if rating[field] is not None and (ability != "essay" or type(rating[field]) is not bool):
            raise ValueError("Source subjudgments may be boolean for essays; otherwise use null")
    match=rating["followup_match"]
    if ability == "research_reasoning":
        if not isinstance(match,dict) or set(match)!=set(FOLLOWUP_FIELDS) or any(type(v) is not bool for v in match.values()):
            raise ValueError("All five explicit follow-up match judgments are required")
    elif match is not None:
        raise ValueError("Follow-up matching applies only to research reasoning")


def resolve_ratings(ratings, ability, adjudication=None):
    if len(ratings) != 2 or ratings[0]["reviewer"] == ratings[1]["reviewer"]:
        raise ValueError("Two different independent reviewers are required")
    for rating in ratings:
        validate_rating(rating, ability)
    left, right = ratings
    dimension_disagreement = any(abs(left["scores"][d]-right["scores"][d]) >= 2 for d in DIMENSIONS[ability])
    total_disagreement = abs(weighted_score(left["scores"], ability)-weighted_score(right["scores"], ability)) > 10
    service_disagreement = any(abs(left['user_service'][d]-right['user_service'][d]) >= 2 for d in service.DIMENSIONS) or abs(service.score(left['user_service'])-service.score(right['user_service'])) > 10
    if (left['user_service']['scientific_accuracy']==0) != (right['user_service']['scientific_accuracy']==0):
        service_disagreement = True
    # Contradictory categorical judgments also require explicit resolution.
    categories_disagree = any(left[f] != right[f] for f in ("source_correct", "conclusion_correct", "refusal", "followup_match"))
    needs = dimension_disagreement or total_disagreement or categories_disagree or service_disagreement
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
                  "user_service":{d:(left['user_service'][d]+right['user_service'][d])/2 for d in service.DIMENSIONS},
                  **{f:left[f] for f in ("source_correct", "conclusion_correct", "refusal", "followup_match")}}
    hit = (all(result["followup_match"].values()) and result["scores"]["logic_chain"] >= 3 and result["scores"]["task_detail"] >= 3 and result["scores"]["controls_uncertainty"] >= 2) if ability == "research_reasoning" else None
    return {"status": "scored", "score": service.score(result['user_service']),
            "user_service":result['user_service'], "task_quality_score":weighted_score(result["scores"], ability),
            "dimensions": result["scores"], "source_correct": result["source_correct"],
            "conclusion_correct": result["conclusion_correct"], "refusal": result["refusal"], "disagreement": needs,
            "followup_match":result["followup_match"], "historical_hit":hit}


def concept_diagnostics(answer, key):
    """Lexical screening helps reviewers locate evidence; it never assigns credit."""
    text=answer.casefold()
    return {"screening_only":True, "automatic_score":None, "concepts":[{
        "id":c["id"], "matched_aliases":[a for a in c["aliases"] if re.search(r"(?<!\w)"+re.escape(a.casefold())+r"(?!\w)",text)],
        "contextual_criterion":c["criterion"]} for c in key["required_concepts"]],
        "logic_chain_to_verify":key["logic_chain"],
        "warning":"Mention, negation and keyword stuffing are not evidence of correct use. Review direction, context and all required inference links."}
