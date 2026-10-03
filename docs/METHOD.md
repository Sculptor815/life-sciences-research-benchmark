# Evaluation method

Version 0.3 uses four domains and exactly three open-response tasks: **essay, experimental design, and research reasoning**. Disputed-paper appraisal is an essay task. The active pilot has no multiple-choice or numeric-only items.

## The primary outcome: helping the researcher

The benchmark asks whether the assistant helps a researcher make a better decision and carry out reliable work. Before authoring, specify the user's goal, current evidence, constraints, decision and observable success condition. A task should answer a real need: clarify a mechanism, choose a discriminating experiment, diagnose a failed assay, reproduce an analysis, assess a questionable claim, or decide what evidence to collect next.

The **primary reported score** is user service, rated independently on five 0–4 dimensions: scientific accuracy (35%), decision value (25%), actionability (20%), verifiability (15%) and communication (5%). A fatal factual premise receiving accuracy zero caps the primary total at 20/100; disagreement about that judgment requires adjudication. This is a proposed design requiring expert calibration, not a validated utility scale.

An excellent answer identifies the most consequential uncertainty, gives a feasible prioritized next action, explains how possible outcomes change the decision, and separates established facts from assumptions. It gives the essential recommendation first and detailed protocols where they support execution. If an indispensable input is unknown, it asks for or specifies that input; it does not fabricate precision. An honest, useful bounded answer can outperform a confident, exhaustive-looking answer.

Technical concept coverage, logic completeness, procedural depth and historical matching remain **diagnostic scores**, not substitutes for user benefit. A valid new direction can receive full service credit even when it differs from the author's later work. Best-of-five selection uses the primary service score, preserves every sample's technical scores, and reports historical hits separately. Two independent reviewers judge both score sets; a gap of at least 2 in either set or over 10 weighted percentage points in either total requires adjudication.

Validation should include blinded researchers attempting the next step from each answer, checking reproducibility, recording consequential errors and missing inputs, and measuring time and effort saved against an appropriate baseline. User satisfaction alone is insufficient if the advice is scientifically wrong. No such prospective user-outcome study has yet been completed.

## Answer depth

The 20-question public pilot contains 12 essays, four design questions and four reasoning questions; all four visual items are essays. Private reference answers themselves must contain at least 301, 901 and 1,201 English words respectively, excluding rubric annotations. Candidate limits are 1,500, 3,500 and 5,000 words. Length is an authoring completeness gate, not a score: shorter correct model answers can earn full credit if all substantive requirements are met.

Essays connect concepts, observations, alternative explanations and bounded conclusions. Design answers require an operational ordered protocol: identity/QC, independent units, allocation/blinding, preparation, intervention, sampling schedule, calibration, measurements, controls, analysis, troubleshooting and decision rules. Reasoning answers add a valid unresolved biological question, competing predictions and especially detailed positive, negative and ambiguous interpretations.

Each procedural detail must be labeled as source-reported, proposed or unknown. Unreported concentrations, coordinates, sequences, timings and power inputs require calibration or a missing-input statement, never invented historical precision. Draft keys are not laboratory-validated SOPs. Claiming greater completeness than published Methods requires a full Methods/supplement audit.

## Textbooks and exercises

Use demanding end-of-chapter problems from high-quality textbooks with verified adoption at leading US universities. Record edition, chapter, problem identifier, adoption evidence, learning objective and solution provenance. Prefer official author, publisher and university solutions over unattributed answer sites. Independently solve and verify the reasoning.

Select mechanism, evidence, control, quantitative-assumption and figure-interpretation problems. Write original variants with changed data and counterfactuals; do not redistribute copyrighted question/solution collections. Track public-solution exposure and semantic overlap. Publicly solved problems support calibration but do not establish resistance to memorization. Related variants stay in one source family.

## Bank and splits

The revised blueprint has 12 domain/task cells with 20 slots each: 240 target slots, 48 public and 192 held out. Each cell has 3/13 public/held-out text slots and 1/3 image slots; formal held-out tracks contain 156 text and 36 image items. This replaces the previous four-task 320-slot blueprint and does not imply completion. Split both case and source-paper families before authoring variants. Closely related publications, including both STAP papers, remain together.

## Concepts and logic scoring

Each private key lists concepts, aliases and criteria for correct contextual use, plus directed premise → inference → conclusion links with evidence locations. Reviewers mark missing, reversed or contradicted links. A term in an incorrect assertion earns no credit. The lexical diagnostic highlights matches but produces **no automatic score**; negation and keyword stuffing require contextual review.

All dimensions have item-specific 0–4 anchors and these percentage weights:

| Task | Concepts | Logic chain | Task detail | Controls/uncertainty | Conclusion alignment |
|---|---:|---:|---:|---:|---:|
| Essay | 30 | 40 | 10 | 10 | 10 |
| Experimental design | 20 | 30 | 30 | 10 | 10 |
| Research reasoning | 15 | 30 | 30 | 10 | 15 |

Total = sum of dimension score / 4 × weight. Essay detail means precise evidence analysis; design/reasoning detail means operational protocol adequacy. Accept equivalent scientific terminology and valid alternative designs. Length, prestige, indiscriminate skepticism and fashionable techniques earn no credit. Explain distinct consequences before penalizing an error across multiple dimensions.

Two experts score independently. Any dimension gap ≥2, weighted-total gap >10 percentage points, or categorical disagreement requires a third reviewer. Exactly 10 points alone is not a trigger. Preserve both originals. Calibration measures agreement, not construct validity.

## Five independent reasoning attempts

Each reasoning question schedules five fresh-context samples with identical visible evidence and no previous answers, feedback or hints. Other tasks have one sample. With a configured seed, sample n uses base+n−1. Store duplicates, refusals and empty completions too. Each sample has at most two transport retries; retries are not extra scientific opportunities.

Freeze the original-paper packet before the earliest public disclosure of the later paper, including preprints. Private keys record both sources, dates, author overlap and the actual later experiments. Keep future-paper titles, findings, matching criteria and answers out of requests. These retrospective public-literature cases remain vulnerable to training-data memorization; hidden keys do not make them genuinely prospective.

A historical hit requires reviewer agreement that ONE answer matches all five aspects: biological question, mechanism, intervention/analysis strategy, readout and predicted outcome. That answer must also score ≥3/4 on logic and protocol detail and ≥2/4 on controls/uncertainty. A paper title, vague topic match or union of fragments across five answers cannot qualify. Equivalent methods may qualify with an explicit rationale.

Report first-sample quality, best complete-answer quality, hit-at-1 and hit-at-5 separately. All five must be scored before final aggregation. These are observed outcomes, not general pass-probability estimates. A strong alternative direction can earn quality credit without a historical hit. Later author behavior is a reference, not the only scientifically correct future direction.

## Disputed-paper and raw-data tracks

Disputed-paper essays require observation → measurement problem → affected comparison → claim limitation, benign alternatives and falsifying checks. Technical evidence should precede official notices. Distinguish fabrication findings, image concerns, contamination, non-replication, correction and retraction. PubPeer counts and author silence do not prove fraud. Missing results are not necessarily negative. Assess reporting denominators, exclusions and complete outcomes. See [the ten-paper selection](DISPUTED_PAPERS.md).

Raw-data bioinformatics and neural-data reproduction are separate artifact tasks. Require raw accessions/hashes, frozen environments, figure panels, preprocessing, derived tables and prespecified numerical tolerances. Processed matrices are not raw sequencing data; figure spreadsheets are not raw acquisition signals. See [the reproduction protocol](REPRODUCTION.md). The numerical checker verifies files and metric agreement; it does not execute submissions, authenticate logs, certify isolation or establish biological truth. Independent raw-to-output execution is required for agent credit.

## Execution and reporting

Authors may browse. Evaluated models receive only frozen materials and no retrieval tools. Client checks cannot inspect remote-provider internals; an offline code track requires OS-enforced network isolation and private-target separation.

The 20 questions schedule 36 samples and at most 108 visible calls with transport retries. Budget each call, retain failed-call reservations, and stop paid requests when usage is missing or exceeds ceilings. Provider limits remain necessary. The direct Inspect exploratory task does not implement Benchmark sampling/budget enforcement; use `lsrw run`.

Aggregate quality separately by modality as an equal mean over 12 cells. Incomplete scoring or missing cells leaves totals unset. Preserve every sample, not only winners. Family-cluster bootstrap and paired comparisons require sufficient independent families and matching dataset/rubric versions. Reports cannot remove selection bias, hindsight or expert uncertainty.

Run hashes detect changes but are not authenticated audit trails. Historical runs retain their original bytes and require their version's scoring software. Legacy discovery records remain inspectable, but current export is blocked until task types and answers are upgraded. Private answers, future-paper targets, reviewer identities and unpublished responses remain outside GitHub.
