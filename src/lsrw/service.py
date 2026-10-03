"""Proposed user-service rubric; expert calibration remains required."""
DIMENSIONS = ("scientific_accuracy", "decision_value", "actionability", "verifiability", "communication")
WEIGHTS = (35, 25, 20, 15, 5)
CRITERIA = {
    "scientific_accuracy":"Distinguish observations, assumptions and proposals; state correct biological implications and uncertainty without inventing evidence.",
    "decision_value":"Resolve the user's stated decision, identify the highest-value uncertainty, prioritize a discriminating next step, and explain what would change the recommendation.",
    "actionability":"Provide an ordered feasible plan, prerequisites, controls, decision rules, and explicit blocking inputs; details must support execution rather than merely add length.",
    "verifiability":"Trace claims and results to supplied evidence, preserve data/protocol provenance, and specify independent checks; never present a proposed analysis as completed.",
    "communication":"Lead with the useful conclusion, separate essential actions from supporting detail, and make limits understandable without verbosity or false confidence."
}
ANCHORS = {
    "0":"Fundamentally wrong, unsupported or unusable for this criterion; a fatal false premise belongs in scientific accuracy, with the exact contradiction recorded.",
    "1":"Some relevant content, but the user still lacks the essential information or receives materially misleading guidance.",
    "2":"Partly useful and scientifically relevant, but substantial verification, redesign or clarification is still needed.",
    "3":"Reliably advances the stated decision, with a feasible next step and transparent limits; one noncritical issue remains.",
    "4":"Fully satisfies the stated criterion for this case: precise evidence, justified decisions, practical next steps and explicit conditions that would change the advice."
}


def score(scores):
    if not isinstance(scores,dict) or set(scores)!=set(DIMENSIONS) or any(type(v) is not int and type(v) is not float or not 0 <= v <= 4 for v in scores.values()):
        raise ValueError("Five user-service dimension scores from 0 to 4 are required")
    total=sum(scores[d]*w/4 for d,w in zip(DIMENSIONS,WEIGHTS))
    # A fundamentally wrong premise cannot be rescued by polished presentation.
    return min(total,20.0) if scores['scientific_accuracy']==0 else total
