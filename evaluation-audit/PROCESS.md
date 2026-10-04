# Scoring process

## Common inputs and sequence

1. Freeze the [30 questions and packets](../benchmark-30/QUESTIONS.md), the reference version and the item-applicable rubric. There are ten questions in each category.
2. Retain one selected final answer per model/question. All 360 selected answers are reused in both rounds. Eight missing first-round responses were recovered once with owner authorization; no valid refusal was retried and no best-of selection was used.
3. Read each complete final answer against the question, packet and relevant reference. Record evidence, scientific judgments, limitations and candidate-record hashes. References are aids; documented corrections are retained. Model/company identity is not a scoring criterion, although the referee was not blinded.
4. Finish and archive round one before the strict rescore. Keep scientific-quality judgments and historical matching separate.
5. Personally reread the saved answers for round two. Apply the frozen applicability matrix to the primary proposed route. Save each check, deduction, exact quotation or documented absence, and non-duplication link. Preserve correction history.
6. Recompute category means and model totals only after all items are available. Verify score arithmetic, coverage, evidence anchors and hashes. No paid model judges or answer regeneration were used for the second round.

## Round one

[Original rubric](../benchmark-30/v1/RUBRIC.md). Each service dimension is rated 0-4: scientific accuracy 35%, decision value 25%, actionability 20%, verifiability 15%, communication 5%.

`Q1 = sum(weight * rating / 4)`. A zero scientific-accuracy rating caps Q1 at 20. The saved `service` ratings, `errors`, `rationale`, reference guardrails and historical `followup_match_evidence` show how the referee reached each judgment. These dimension ratings are not the strict round-two point checklist. `overall_benchmark_score: null` is an unused original placeholder; item scores are reproducible from Q1 and the matching components, not missing reviews.

## Round two

[Final rubric](../benchmark-30/v2/RUBRIC.md) and [item applicability](../benchmark-30/v2/applicability.json). `Q2 = max(0, 100 - distinct applicable deductions)`. C and M cost ten points when unmet. Other applicable checks cost five; G1 and G2 permit distinct errors/omissions up to twenty each. A false central premise invalidating the main recommendation caps Q2 at twenty.

Each review records `met`, `unmet` or a justified `not_applicable`. Equivalent scientific content qualifies; keywords alone do not. `covered_by` marks the same defect already charged elsewhere and contributes zero additional deduction. Multiple missing quantities within a single procedural check are not separate unlimited penalties. Proposed calibration is allowed where unknown conditions cannot responsibly be supplied; invented precision earns no credit.

## Shared research and category formulas

For research questions, `item = 60 * Hit@1 + 0.40 * Q`. All five historical components must jointly qualify: biological question, mechanism, intervention, readout and predicted outcome, without a critical control/inference failure. Missing matching review is unavailable, not a miss. A valid alternative direction can earn quality credit while missing the historical target. The owner requested this weighting for both rounds after some answers were inspected.

For essays and experimental designs, `item = Q`. Final total is `0.20 * mean(10 essays) + 0.30 * mean(10 designs) + 0.50 * mean(10 research items)`. Never prorate missing questions.

## Exceptions and separate metrics

Valid refusals/wholly off-topic answers receive zero task performance. Empty refusals have no assessable explanation score; partial answers are graded as returned. Missing or transport-uncertain responses are not scored as zero.

Visible scientific explanation has four 0-4 dimensions: factual correctness, evidence grounding, causal validity and alternatives/limits. Their equally weighted mean is scaled to 100 and is not added again to task scores. It is not hidden-reasoning accuracy. Cost and latency refer to saved original generation records, with unconfirmed bills flagged; they are not new rescoring expense.

## Reproducibility limits

The verification script reproduces arithmetic and validates published records, not the scientific truth of a judgment. The single unblinded referee, retrospective target selection, post-hoc rubric and exposed source/reference material limit interpretation. Written experimental plans do not demonstrate actual laboratory performance or raw-data pipeline execution. Review amendments include original snapshots so later corrections can be audited without rewriting round one.
