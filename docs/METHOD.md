# Evaluation method

## Scope and taxonomy

Version 1 targets four domains and four abilities. Every item has one primary domain/ability pair, topic and technique tags, a research context, an undergraduate/graduate difficulty label, and a case/source family. Disease names are contexts, not separate primary domains.

Bioinformatics emphasizes the validity of analysis choices and biological conclusions. Integration requires sample alignment, assay-specific QC, pairing, batch assessment and validation. Enrichment requires a defensible tested universe, gene-set version, null and multiplicity control. Pseudotime requires direction/topology assumptions and independent validation. GWAS separates association, causal variants and effector genes. Whole-genome sequencing includes callability, variant QC, ancestry, relatedness and compatible analysis pipelines. The first version does not measure software execution skill.

## Bank and split

Each of 16 cells has 16 text and 4 image items. Public/held-out counts per cell are 3/13 text and 1/3 image, respectively. Totals are 320 items: 64 public and 256 held out. Formal text and image tracks contain 208 and 48 items. The image sample size remains limited and uncertainty must be displayed.

Split by both case family and source-paper family before authoring variants. No family crosses the split. Global family identifiers should be retained across domain boundaries. Images use original synthetic or appropriately licensed materials, with hashes, provenance and processing records. The current visual pilot covers knowledge only; all four abilities need visual items before a formal release.

## Evidence conditions

Knowledge questions are closed book apart from their stimulus. Other questions use only supplied packets. All model requests contain an allowlisted system instruction, prompt, packet, options if relevant, answer-length requirement, and image bytes when applicable. Administrative metadata, keys, dimension anchors and expert records are not included.

Paper appraisal records source identity separately from conclusion support. Source states: real and matching, citation mismatch, known fabrication, insufficient to verify. Notice state is recorded separately. Conclusion states: supported, partially supported, unsupported, insufficient evidence. Some pilot cases use explicit teaching archives; matching within such an archive is not a claim that a real external article exists. Final questions need expert checks of packet sufficiency and provenance.

Unsuccessful retrieval alone does not establish fabrication. Retraction status and truth of individual claims are different judgments. Image anomalies require investigation before claims about cause or intent.

## Scoring

Knowledge uses exact labelled choices or numeric values with units and predeclared absolute/relative tolerance. The larger of the two tolerance bounds is used. Correct answers score 100, incorrect or malformed answers score 0. Format validity is recorded separately. Explicit JSON requirements are identical across models; there is no model-based answer extraction.

Open tasks use five dimensions scored 0–4:

| Ability | Dimensions |
|---|---|
| Experimental design | Hypothesis/measurement, controls, replication/statistics, confounds/feasibility, interpretation |
| Research reasoning | Question definition, competing hypotheses, discriminating predictions, information value, falsification/updating |
| Paper appraisal | Source verification, evidence localization, methods evaluation, inferential scope, uncertainty/validation |

Total percentage = sum of dimension scores × 5. Item-specific anchors and acceptable alternatives govern partial credit. Critical errors affect the relevant dimension; an omission is not repeatedly penalized across unrelated dimensions. Length, jargon and novelty alone earn no credit. Draft anchor answers are calibration aids pending expert revision, not certified gold standards.

Two experts score independently. Any dimension difference of at least 2, or total difference greater than 10 percentage points, requires a third reviewer. Exactly 10 points alone does not trigger adjudication. Disagreement on the paper subjudgments or refusal label also requires resolution. Otherwise, dimension scores are averaged. Adjudication replaces the final decision while preserving both originals. Formal review uses the locked domain roster.

Calibration reports exact and within-one dimension agreement and the mean absolute difference in total percentage scores. These are descriptive agreement summaries, not evidence of construct validity. A human coordinator must document acceptance and resolve systematic differences before locking a bank.

## Execution and costs

Each question starts with an independent context and no tools. One completed answer per question is retained. Network, rate-limit and timeout failures permit at most two additional attempts. API, context or unsupported-image errors remain operational outcomes; they do not count as scientific zeroes. Empty answers and irrelevant refusals are completed answers and receive no automatic retry.

The run configuration records exact model identifier, supported generation settings, code/dataset/template versions, pricing assumptions and limits. Responses retain the provider-reported model name, token counts when available, latency and stop reason. Provider-billed cost is recorded only when exposed; current Inspect adapter reports token-based estimates, not invoices. The reservation ledger retains an allocation for failed requests because failure does not guarantee no charge.

Input ceilings are estimates. The text preflight uses a conservative byte-based bound plus message overhead; image accounting is provider-dependent. This mechanism cannot enforce a provider's billing cap. Use provider-side limits, verify pricing, and choose ceilings that include all charged reasoning/image tokens. Unexpected or missing usage stops further paid requests. No fallback model is selected.

## Aggregation and uncertainty

Scores are aggregated separately by modality. Overall score is the unweighted mean of the 16 domain/ability cell means. Domain means weight the four abilities equally; ability means weight the four domains equally. Missing cells leave these totals unset. A partial report may show an explicitly labelled mean over observed cells; it is not a formal overall score.

Reports show requested and completed counts, scored counts, empty responses, expert-reviewed refusal rate and its denominator, expert disagreement and its denominator, paper source/conclusion subaccuracy, elapsed time and available cost estimates. Objective-question refusal status is not automatically classified in v0.1; their malformed/empty status is reported, and full refusal-rate auditing remains a coordinator task.

Confidence intervals use a fixed-seed case-family cluster bootstrap, stratified by the set of cells in which a family appears. Resample families within each stratum. A family receives the same weight wherever it appears, including across cells. This preserves the benchmark's cell composition while retaining dependence within cases. Each draw recomputes the equal-cell mean. Intervals are withheld if a cell or stratum has fewer than two scored families, scoring is incomplete, or too few valid draws remain. With three held-out visual items per cell, interval estimates are still fragile; the sample count must accompany them. The method does not capture question-author selection bias or expert uncertainty.

Paired model differences require identical question IDs, dataset hash and rubric hash. Each item's score difference is computed first, then aggregated and bootstrapped by family. Coordinators must additionally check generation and evidence conditions; a paired calculation alone does not establish fair equivalence. No automatic significance or superiority claim is produced.

## Versioning and governance

Completed run inputs and responses have a checksum inventory. Edits invalidate verification. Scoring produces content-addressed versions; reports are deterministic from a chosen score artifact. Local hashes detect accidental modification, not malicious rewriting of all records. Store a signed or externally archived manifest for a formal release.

Expert identities, held-out materials, answers, ratings and unpublished responses belong in a private directory outside the repository. A reviewed public release uses an explicit path allowlist. The current package contains development questions and code; it makes no claim of expert validation or real model performance.
