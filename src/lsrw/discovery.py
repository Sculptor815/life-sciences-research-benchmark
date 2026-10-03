"""Private, source-traceable discovery corpus and human authoring review.

Research records are not executable items and never enter model requests.
Review decisions bind to content hashes; AI drafts do not count as approvals.
"""
import collections
import datetime as dt
import json
from pathlib import Path

from .storage import digest, read_json, write_new
from .taxonomy import ABILITIES, DOMAINS


def validate_corpus(corpus):
    errors = []
    if not isinstance(corpus, dict) or not isinstance(corpus.get("cases"), list):
        return ["Corpus requires a cases list"]
    ids, question_ids = set(), set()
    for case in corpus["cases"]:
        if not isinstance(case, dict):
            errors.append("Case must be an object")
            continue
        name = case.get("id", "<missing>")
        if not isinstance(name, str) or not name or name in ids:
            errors.append("Missing or duplicate case ID")
        else:
            ids.add(name)
        if case.get("domain") not in DOMAINS:
            errors.append(f"{name}: invalid domain")
        paper = case.get("paper", {})
        if not isinstance(paper, dict) or not paper.get("title") or not paper.get("url"):
            errors.append(f"{name}: paper title and URL required")
        if not case.get("original_question") or not case.get("experimental_design"):
            errors.append(f"{name}: original question and experiment required")
        questions = case.get("questions", [])
        if not isinstance(questions, list) or not questions:
            errors.append(f"{name}: candidate questions required")
            continue
        for q in questions:
            if not isinstance(q, dict) or q.get("ability") not in ABILITIES:
                errors.append(f"{name}: invalid question ability")
                continue
            question_id = q.get("id", str(name)+"-"+q["ability"])
            if not isinstance(question_id, str) or not question_id or question_id in question_ids:
                errors.append(f"{name}: missing or duplicate question ID; variants need unique IDs")
            else:
                question_ids.add(question_id)
            if not q.get("prompt") or not q.get("reference_answer"):
                errors.append(f"{name}: prompt and private reference answer required")
            if q["ability"] == "knowledge":
                if not isinstance(q.get("choices"), dict) or set(q["choices"]) != set("ABCD") or q.get("answer") not in ("A", "B", "C", "D"):
                    errors.append(f"{name}: knowledge question needs four choices and a key")
    return errors


def audit(corpus):
    errors = validate_corpus(corpus)
    if errors:
        return {"schema_version":"1.0", "corpus_sha256":digest(corpus), "valid":False,
                "errors":errors, "formal_ready":False}
    cases = corpus["cases"]
    counts = collections.Counter(c.get("domain") for c in cases)
    cells = collections.Counter((c.get("domain"), q.get("ability")) for c in cases for q in c.get("questions", []))
    depths = collections.Counter(str(c.get("paper", {}).get("read_depth", "unverified")) for c in cases)
    gaps = []
    for case in cases:
        reasons = []
        if case.get("paper", {}).get("read_depth") != "full_text":
            reasons.append("original full text not completely verified")
        if not case.get("textbook_reference_verified", False):
            reasons.append("textbook bibliography link not verified")
        if not case.get("notice_checked_at"):
            reasons.append("correction/retraction search not frozen")
        if any(not q.get("candidate_packet") for q in case.get("questions", [])):
            reasons.append("fixed evidence packet needs drafting")
        if any(q.get("ability") != "knowledge" and not q.get("dimensions") for q in case.get("questions", [])):
            reasons.append("item-specific 0-4 dimension anchors pending")
        reasons.append("independent human review and calibration required")
        gaps.append({"id":case.get("id"), "reasons":reasons})
    return {"schema_version":"1.0", "corpus_sha256":digest(corpus), "valid":not errors, "errors":errors,
            "cases":len(cases), "questions":sum(cells.values()), "domains":dict(counts),
            "cells":{f"{d}/{a}":cells[d,a] for d in DOMAINS for a in ABILITIES},
            "read_depth":dict(depths), "formal_ready":False, "readiness_gaps":gaps,
            "scope":"Discovery candidates for human review; not a completed benchmark or exhaustive bibliography"}


def import_decisions(corpus, payload, output):
    """Append a new immutable batch; never change a case's scientific status."""
    if validate_corpus(corpus) or not isinstance(payload, dict):
        raise ValueError("Valid corpus and review object required")
    if payload.get("corpus_sha256") != digest(corpus):
        raise ValueError("Review belongs to another corpus version")
    if not isinstance(payload.get("reviewer"), str) or not payload["reviewer"].strip():
        raise ValueError("Human reviewer name or pseudonym required")
    cases = {c["id"]:c for c in corpus["cases"]}
    seen = set()
    decisions = payload.get("decisions")
    if not isinstance(decisions, list) or not decisions:
        raise ValueError("At least one explicit decision required")
    for decision in decisions:
        if not isinstance(decision, dict):
            raise ValueError("Each review decision must be an object")
        name = decision.get("case_id")
        if name not in cases or name in seen:
            raise ValueError("Unknown or duplicate case decision")
        seen.add(name)
        if decision.get("case_sha256") != digest(cases[name]):
            raise ValueError("Case changed since review")
        if decision.get("decision") not in ("retain", "revise", "reject") or not isinstance(decision.get("notes"), str) or not decision["notes"].strip():
            raise ValueError("Decision and rationale required")
        checks = decision.get("checks", {})
        if not isinstance(checks, dict) or set(checks) != {"source_read", "question_fair", "answer_checked", "rights_checked"} or any(type(v) is not bool for v in checks.values()):
            raise ValueError("Explicit source/question/answer/rights checks required")
        if decision["decision"] == "retain" and not all(checks.values()):
            raise ValueError("Retain requires all human checks")
    record = {"corpus_sha256":payload["corpus_sha256"], "reviewer":payload["reviewer"], "decisions":decisions,
              "review_type":"candidate_selection_not_formal_bank_approval", "identity_assurance":"self_attested_local_record_not_authenticated",
              "received_utc":dt.datetime.now(dt.timezone.utc).isoformat()}
    record["content_sha256"] = digest(record)
    write_new(Path(output)/(record["content_sha256"]+".json"), record)
    return record


def export_drafts(corpus, output):
    """Preview-only export. No automatic gold rubric, split choice or approval."""
    errors = validate_corpus(corpus)
    if errors:
        raise ValueError("Invalid research corpus: " + "; ".join(errors))
    output = Path(output)
    output.mkdir(parents=True, exist_ok=False)
    candidates, answers = [], {}
    for case in corpus["cases"]:
        for q in case["questions"]:
            name = q.get("id", case["id"]+"-"+q["ability"])
            candidates.append({"candidate_id":name,"case_id":case["id"],"source_doi":case["paper"].get("doi"),
                               "domain":case["domain"],"ability":q["ability"],"prompt":q["prompt"],
                               "choices":q.get("choices",{}),"fixed_packet_draft":q.get("candidate_packet", ""),
                               "status":"awaiting_human_review","split":"unassigned"})
            answers[name] = {"reference_answer":q["reference_answer"],"answer":q.get("answer"),
                             "scoring_points":q.get("scoring_points",[]),"evidence":case["paper"],
                             "rubric_status":"draft_not_calibrated"}
    write_new(output/"candidates.json", candidates)
    write_new(output/"reference-answers.json", answers)
    write_new(output/"audit.json", audit(corpus))
    return {"output":str(output.resolve()),"candidate_questions":len(candidates),"formal":False}


def render_review(corpus, output):
    errors = validate_corpus(corpus)
    if errors:
        raise ValueError("Invalid research corpus: " + "; ".join(errors))
    data = {"corpus":corpus,"sha256":digest(corpus),"case_hashes":{c["id"]:digest(c) for c in corpus["cases"]},"audit":audit(corpus)}
    # JSON inside script must not close its element, even for untrusted papers.
    embedded = json.dumps(data,ensure_ascii=False).replace("<", "\\u003c").replace("\u2028", "\\u2028").replace("\u2029", "\\u2029")
    page = Path(__file__).with_name("discovery_review.html").read_text(encoding="utf-8").replace("__CORPUS_JSON__", embedded)
    path = Path(output)
    path.parent.mkdir(parents=True,exist_ok=True)
    with path.open("x",encoding="utf-8") as stream:
        stream.write(page)
    return path.resolve()
