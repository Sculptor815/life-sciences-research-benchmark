import csv
import html
import io
from pathlib import Path
from statistics import mean

from .grading import objective_score, resolve_ratings, validate_key
from .review import collect_reviews
from .runner import verify_run, response_slots
from .statistics import cell_means, family_interval, macro, paired_comparison
from .storage import digest, file_hash, read_json, write_new
from .taxonomy import ABILITIES, DOMAINS, CELL_COUNTS


def score_run(run, keys_path, review_root=None, adjudications_path=None, output=None):
    run = Path(run)
    manifest, items, completion = verify_run(run)
    if not manifest.get("sampling_policy"):
        raise ValueError("Historical runs require their original scoring version; current scoring uses the three-task sampling protocol")
    keys = read_json(keys_path)
    if manifest["keys_sha256"] and file_hash(keys_path) != manifest["keys_sha256"]:
        raise ValueError("Formal run rubric differs from locked version")
    ratings = collect_reviews(review_root, run, keys) if review_root else {}
    adjudications = read_json(adjudications_path) if adjudications_path else {}
    roster = read_json(run/"lock.json")["domain_roster"] if manifest["config"]["formal"] else None
    rows = []
    for item, response_id, sample in [(i,s,n) for i in items for s,n in response_slots(i)]:
        record = read_json(run / "responses" / (response_id+".json"))
        row = {k:item[k] for k in ("id", "family_id", "domain", "ability", "modality", "split")}
        row.update(id=response_id,item_id=item["id"],sample_number=sample)
        row.update(status=record["status"], score=None, elapsed_seconds=record["elapsed_seconds"],
                   cost_usd=record.get("usage_estimated_cost_usd"), empty=None, refusal=None)
        if record["status"] == "completed":
            key = keys[item["id"]]
            validate_key(item, key)
            answer = record["response"]["text"]
            row["empty"] = not answer.strip()
            if item["response_type"] != "open":
                row.update(objective_score(answer, key, item["response_type"]))
                row["status"] = "scored"
            elif len(ratings.get(response_id, [])) == 2:
                if roster:
                    eligible = roster[item["domain"]]
                    if any(r["reviewer"] not in eligible["reviewers"] for r in ratings[response_id]):
                        raise ValueError("Formal rating uses an unassigned domain reviewer")
                    if response_id in adjudications and adjudications[response_id]["reviewer"] != eligible["adjudicator"]:
                        raise ValueError("Formal adjudicator is not the registered domain adjudicator")
                row.update(resolve_ratings(ratings[response_id], item["ability"], adjudications.get(response_id)))
            else:
                row["status"] = "awaiting_review"
        rows.append(row)
    sample_rows = rows
    rows = []
    for item in items:
        group = [r for r in sample_rows if r["item_id"] == item["id"]]
        complete = all(r["status"] == "scored" for r in group)
        best = max(group, key=lambda r:r["score"] if r["score"] is not None else -1)
        row = {**best, "id":item["id"], "score":best["score"] if complete else None,
               "samples_expected":len(group), "samples_scored":sum(r["status"]=="scored" for r in group),
               "first_sample_score":group[0]["score"], "selected_response_id":best["id"] if complete else None,
               "historical_hit_at_5":int(any(r.get("historical_hit") for r in group)) if complete and item["ability"]=="research_reasoning" else None,
               "historical_hit_at_1":int(bool(group[0].get("historical_hit"))) if complete and item["ability"]=="research_reasoning" else None,
               "elapsed_seconds":sum(r["elapsed_seconds"] for r in group),
               "cost_usd":sum(r["cost_usd"] for r in group if r["cost_usd"] is not None) if any(r["cost_usd"] is not None for r in group) else None}
        if not complete:
            row["status"] = next(r["status"] for r in group if r["status"] != "scored")
        rows.append(row)
    artifact = {"run_id":manifest["run_id"], "manifest_sha256":digest(manifest), "dataset_sha256":manifest["dataset_sha256"],
                "rubric_sha256":file_hash(keys_path), "formal_requested":manifest["config"]["formal"],
                "mock":manifest["config"]["backend"]=="mock" or manifest["config"]["model"].split("/")[0]=="mockllm", "model":manifest["config"]["model"],
                "billing_uncertain":completion["billing_uncertain"], "reserved_usd":completion["reserved_usd"],
                "all_requests_completed":completion["completed"]==completion["total"],
                "sampling_policy":manifest.get("sampling_policy"), "rating_records":ratings, "adjudications":adjudications, "sample_rows":sample_rows, "rows":rows}
    # Scored artifacts contain private rater evidence; publish only derived reports after review.
    artifact["content_sha256"] = digest(artifact)
    path = Path(output) if output else run/"scores"/(artifact["content_sha256"][:16]+".json")
    if not path.exists():
        write_new(path, artifact)
    elif read_json(path) != artifact:
        raise ValueError("Score artifact already exists with different contents")
    return path


def verify_scores(path):
    data = read_json(path)
    if digest({k:v for k,v in data.items() if k != "content_sha256"}) != data["content_sha256"]:
        raise ValueError("Scoring artifact was modified")
    return data


def summarize(scores):
    result = {k:scores[k] for k in ("run_id", "model", "dataset_sha256", "rubric_sha256", "content_sha256", "mock", "reserved_usd")}
    result["tracks"] = {}
    for modality in ("text", "image"):
        rows = [r for r in scores["rows"] if r["modality"] == modality]
        if not rows:
            continue
        cells = cell_means(rows)
        completed = sum(r["status"] in ("scored", "awaiting_review", "needs_adjudication") for r in rows)
        scored = [r for r in rows if r["score"] is not None]
        open_rows = rows
        reviewed = [r for r in open_rows if "disagreement" in r]
        paper = [r for r in rows if r["ability"] == "essay" and r.get("source_correct") is not None]
        expected = CELL_COUNTS["heldout",modality]*len(DOMAINS)*len(ABILITIES)
        eligible = bool(scores["formal_requested"] and not scores["mock"] and scores["all_requests_completed"] and len(rows)==expected and len(scored)==len(rows) and len(cells)==len(DOMAINS)*len(ABILITIES) and not scores["billing_uncertain"])
        by_domain = {d:mean(cells[d,a] for a in ABILITIES) if all((d,a) in cells for a in ABILITIES) else None for d in DOMAINS}
        by_ability = {a:mean(cells[d,a] for d in DOMAINS) if all((d,a) in cells for d in DOMAINS) else None for a in ABILITIES}
        known_refusals = [r for r in rows if r.get("refusal") is not None]
        result["tracks"][modality] = {
            "eligible_for_formal_leaderboard":eligible, "questions":len(rows), "completed":completed, "scored":len(scored),
            "completion_rate":completed/len(rows), "overall":macro(rows) if len(scored)==len(rows) else None,
            "observed_cells_mean":mean(cells.values()) if cells else None,
            "cells":{f"{d}/{a}":{"score":cells.get((d,a)), "n":sum(r["domain"]==d and r["ability"]==a for r in rows)} for d in DOMAINS for a in ABILITIES},
            "domains":by_domain, "abilities":by_ability,
            "ci95":family_interval(rows) if len(scored)==len(rows) else {"interval":None,"reason":"Incomplete scoring"},
            "expert_disagreement_rate":sum(r["disagreement"] for r in reviewed)/len(reviewed) if reviewed else None,
            "expert_pairs_reviewed":len(reviewed), "empty_answers":sum(r.get("empty") is True for r in rows),
            "refusal_rate_reviewed":sum(r["refusal"] for r in known_refusals)/len(known_refusals) if known_refusals else None,
            "refusal_judgments":len(known_refusals),
            "source_accuracy":mean(float(r["source_correct"]) for r in paper) if paper else None,
            "conclusion_accuracy":mean(float(r["conclusion_correct"]) for r in paper) if paper else None,
            "paper_judgments":len(paper), "elapsed_seconds":sum(r["elapsed_seconds"] for r in rows),
            "score_interpretation":"Primary score is user-service utility; technical quality and historical matching are separate diagnostics.",
            "research_reasoning": [{k:r.get(k) for k in ("id","first_sample_score","score","task_quality_score","historical_hit_at_1","historical_hit_at_5","samples_expected","samples_scored")} for r in rows if r["ability"]=="research_reasoning"],
            "usage_estimated_cost_usd":sum(r["cost_usd"] for r in rows if r["cost_usd"] is not None),
            "cost_records_available":sum(r["cost_usd"] is not None for r in rows),
        }
    return result


def report(scores_path, output):
    scores = verify_scores(scores_path)
    summary = summarize(scores)
    output = Path(output)
    output.mkdir(parents=True, exist_ok=False)
    write_new(output/"report.json", summary)
    columns = ("id", "family_id", "domain", "ability", "modality", "status", "score", "task_quality_score", "historical_hit_at_1", "historical_hit_at_5", "elapsed_seconds", "cost_usd")
    with (output/"scores.csv").open("x", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=columns, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(scores["rows"])
    escape = html.escape
    blocks = []
    for track, data in summary["tracks"].items():
        rows = "".join(f"<tr><td>{escape(k)}</td><td>{v['n']}</td><td>{'Pending' if v['score'] is None else format(v['score'],'.1f')}</td></tr>" for k,v in data["cells"].items())
        status = "Eligible" if data["eligible_for_formal_leaderboard"] else "Development result — excluded from formal leaderboard"
        blocks.append(f"<section><h2>{track.title()} track</h2><p class='notice'>{status}</p><p>Answered {data['completed']}/{data['questions']}; scored {data['scored']}. Overall: {data['overall'] if data['overall'] is not None else 'Pending'}.</p><table><tr><th>Domain / ability</th><th>Questions</th><th>Score</th></tr>{rows}</table><details><summary>Uncertainty and run statistics</summary><pre>{escape(__import__('json').dumps(data, indent=2))}</pre></details></section>")
    page = "<!doctype html><html lang='en'><meta charset='utf-8'><meta name='viewport' content='width=device-width'><title>Life Sciences Research Workbench</title><style>body{font:16px system-ui;max-width:1100px;margin:40px auto;padding:0 24px;color:#173042;background:#f7f9fa}section{background:white;padding:24px;margin:24px 0;border:1px solid #d6e1e7;border-radius:12px}table{width:100%;border-collapse:collapse}td,th{padding:9px;border-bottom:1px solid #dfe6eb;text-align:left}.notice{color:#8b4f00}pre{white-space:pre-wrap;overflow-wrap:anywhere}h1{font-size:30px}</style><h1>Life Sciences Research Workbench</h1>"
    page += f"<p>Model: {escape(summary['model'])} · Run: {escape(summary['run_id'])}</p><p>Four domains · Three open-response abilities · Text and image tracks scored separately.</p>"
    page += "<p>Primary score: usefulness to the researcher, grounded in scientific accuracy. Technical answer quality and historical follow-up hits are separate diagnostics.</p>"
    if summary["mock"]:
        page += "<p class='notice'>Software demonstration using mock responses. These are not model capability results.</p>"
    page += "".join(blocks)+f"<footer>Dataset: {escape(summary['dataset_sha256'])}<br>Scoring: {escape(summary['content_sha256'])}</footer></html>"
    (output/"REPORT.html").write_text(page, encoding="utf-8")
    return output/"REPORT.html"


def compare(left_path, right_path):
    left, right = verify_scores(left_path), verify_scores(right_path)
    if left["dataset_sha256"] != right["dataset_sha256"] or left["rubric_sha256"] != right["rubric_sha256"]:
        raise ValueError("Compare only the same dataset and rubric versions")
    return {track:paired_comparison([r for r in left["rows"] if r["modality"]==track], [r for r in right["rows"] if r["modality"]==track]) for track in ("text", "image") if any(r["modality"]==track for r in left["rows"])}
