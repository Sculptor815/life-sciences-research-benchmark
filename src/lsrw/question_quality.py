"""Summarize explicit question-quality ratings without inventing missing scores."""

DIMENSIONS=("importance","evidence_grounding","novelty","testability","discrimination","feasibility")


def summarize(record):
    if not isinstance(record,dict) or not isinstance(record.get("scores"),dict):
        raise ValueError("A record with six explicit score fields is required")
    scores=record["scores"]
    if set(scores)!=set(DIMENSIONS):
        raise ValueError("Use exactly the six question-quality dimensions")
    for value in scores.values():
        if value is not None and (type(value) is not int or not 0<=value<=4):
            raise ValueError("Scores must be integers 0..4 or null, not boolean")
    reasons=record.get("rationales_by_dimension",{})
    if not isinstance(reasons,dict) or any(not isinstance(reasons.get(d),str) or not reasons[d].strip() for d,v in scores.items() if v is not None):
        raise ValueError("Every supplied score requires its own rationale")
    literature=record.get("current_literature_review",{})
    if not isinstance(literature,dict):
        raise ValueError("Literature review must be an object")
    if scores["novelty"] is not None:
        if literature.get("status")!="completed_within_declared_scope" or not literature.get("search_log") or not literature.get("closest_prior_studies"):
            raise ValueError("Novelty needs a completed bounded search log and nearest-prior-work records")
    other=[scores[d] for d in DIMENSIONS if d!="novelty"]
    all_scored=all(v is not None for v in scores.values())
    return {"candidate_id":record.get("candidate_id"),"scores":scores,
            "partial_score":sum(other) if all(v is not None for v in other) else None,
            "partial_denominator":20,"partial_label":"Five-dimensional descriptive score; not a ranking",
            "total_score":sum(scores.values()) if all_scored else None,"total_denominator":24,
            "total_status":"all_dimensions_recorded_not_formal_approval" if all_scored else "pending",
            "formal_rank_eligible":False,"human_review":record.get("human_review","pending"),
            "notice":"Arithmetic and completeness only. This does not verify evidence, reviewer identity, novelty or scientific validity."}
