import random
from collections import Counter, defaultdict
from statistics import mean

from .taxonomy import ABILITIES, DOMAINS


def cell_means(rows, weights=None):
    cells = defaultdict(list)
    for row in rows:
        if row.get("score") is None:
            continue
        weight = 1 if weights is None else weights.get(row["family_id"], 0)
        if weight:
            cells[row["domain"], row["ability"]].append((row["score"], weight))
    return {cell:sum(s*w for s,w in values)/sum(w for _,w in values) for cell,values in cells.items()}


def macro(rows, weights=None):
    cells = cell_means(rows, weights)
    return mean(cells.values()) if len(cells) == len(DOMAINS)*len(ABILITIES) else None


def family_interval(rows, draws=2000, seed=20261003):
    families = sorted({r["family_id"] for r in rows})
    by_cell = defaultdict(set)
    for row in rows:
        if row.get("score") is not None:
            by_cell[row["domain"], row["ability"]].add(row["family_id"])
    if macro(rows) is None or len(by_cell) != 16 or any(len(v)<2 for v in by_cell.values()):
        return {"interval": None, "valid_draws": 0, "reason": "Need scored observations and at least two case families in every cell."}
    membership = defaultdict(set)
    for row in rows:
        membership[row["family_id"]].add((row["domain"], row["ability"]))
    strata = defaultdict(list)
    for family in families:
        strata[tuple(sorted(membership[family]))].append(family)
    if any(len(group)<2 for group in strata.values()):
        return {"interval":None,"valid_draws":0,"reason":"Fewer than two independent families in a cell-membership stratum."}
    rng = random.Random(seed)
    estimates = []
    for _ in range(draws):
        weights = Counter()
        for group in strata.values():
            weights.update(rng.choices(group,k=len(group)))
        value = macro(rows, weights)
        if value is not None:
            estimates.append(value)
    if len(estimates) < draws*.8:
        return {"interval": None, "valid_draws": len(estimates), "reason": "Too many resamples omit a cell; more independent cases needed."}
    estimates.sort()
    return {"interval": [estimates[int(.025*(len(estimates)-1))], estimates[int(.975*(len(estimates)-1))]], "valid_draws":len(estimates),
            "method":"case-family cluster percentile bootstrap stratified by cell-membership pattern", "seed":seed}


def paired_comparison(left, right):
    a = {r["id"]:r for r in left}
    b = {r["id"]:r for r in right}
    if set(a) != set(b) or any(a[k].get("score") is None or b[k].get("score") is None for k in a):
        raise ValueError("Paired comparison requires the same fully scored question IDs")
    differences = []
    for key in sorted(a):
        if any(a[key][field] != b[key][field] for field in ("family_id", "domain", "ability", "modality")):
            raise ValueError("Paired item metadata differs")
        differences.append({**a[key], "score":a[key]["score"]-b[key]["score"]})
    return {"difference_left_minus_right":macro(differences), "ci95":family_interval(differences), "questions":len(differences)}
