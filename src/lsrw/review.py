import random
import uuid
from pathlib import Path

from .grading import validate_key, validate_rating, concept_diagnostics
from .runner import verify_run, response_slots
from .storage import digest, read_json, write_new


def prepare_review(run, keys_path, output, reviewers, seed=419):
    """Output belongs in a private directory; each rater receives only their queue."""
    if len(reviewers) != 2 or len(set(reviewers)) != 2:
        raise ValueError("Provide two different reviewer pseudonyms")
    manifest, items, _ = verify_run(run)
    if not manifest.get("sampling_policy"):
        raise ValueError("Historical review queues require their original software version")
    keys = read_json(keys_path)
    output = Path(output)
    output.mkdir(parents=True, exist_ok=False)
    assignments, mapping = {r:[] for r in reviewers}, {}
    for item, response_id in [(i,s) for i in items for s,_ in response_slots(i)]:
        if item["response_type"] != "open":
            continue
        record = read_json(Path(run) / "responses" / (response_id+".json"))
        if record["status"] != "completed":
            continue
        key = keys[item["id"]]
        validate_key(item, key)
        opaque = uuid.uuid4().hex
        mapping[opaque] = response_id
        for reviewer in reviewers:
            assignments[reviewer].append({"blind_id": opaque, "question": item, "answer": record["response"]["text"],
                                         "rubric": key, "concept_screening":concept_diagnostics(record["response"]["text"], key), "asset_root": str((Path(run)/"dataset").resolve())})
    rng = random.Random(seed)
    for index, reviewer in enumerate(reviewers):
        rng.shuffle(assignments[reviewer])
        folder = output / f"rater-{index+1}"
        write_new(folder / "queue.json", {"reviewer": reviewer, "items": assignments[reviewer]})
    write_new(output / "coordinator-only.json", {"run": str(Path(run).resolve()), "mapping": mapping, "reviewers": reviewers,
                "keys_sha256": digest(keys), "queues": {f"rater-{i+1}/queue.json":digest(read_json(output/f"rater-{i+1}/queue.json")) for i in range(2)}})
    return output


def save_rating(queue_path, blind_id, rating):
    queue_path = Path(queue_path)
    queue = read_json(queue_path)
    item = next((i for i in queue["items"] if i["blind_id"] == blind_id), None)
    if item is None or rating["reviewer"] != queue["reviewer"]:
        raise ValueError("Rating is not assigned to this reviewer")
    validate_rating(rating, item["question"]["ability"])
    write_new(queue_path.parent / "ratings" / f"{blind_id}.json", rating)


def collect_reviews(review_root, run, keys):
    review_root = Path(review_root)
    coordinator = read_json(review_root / "coordinator-only.json")
    if Path(coordinator["run"]).resolve() != Path(run).resolve() or coordinator["keys_sha256"] != digest(keys):
        raise ValueError("Reviews belong to a different run or rubric version")
    collected = {}
    for relative, expected in coordinator["queues"].items():
        queue_path = review_root / relative
        queue = read_json(queue_path)
        if digest(queue) != expected:
            raise ValueError("Review queue changed after assignment")
        for item in queue["items"]:
            path = queue_path.parent / "ratings" / (item["blind_id"] + ".json")
            if path.exists():
                rating = read_json(path)
                if rating["reviewer"] != queue["reviewer"]:
                    raise ValueError("Reviewer identity mismatch")
                collected.setdefault(coordinator["mapping"][item["blind_id"]], []).append(rating)
    return collected
