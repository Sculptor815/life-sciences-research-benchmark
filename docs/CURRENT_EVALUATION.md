# Current 30-question evaluation

The current comparison uses 12 models and 30 questions: ten essays, ten experimental designs and ten research-reasoning questions. Each question receives exactly one independently generated answer. Category means receive weights of 20%, 30% and 50%, respectively. Model browsing and tools are disabled. This configuration is separate from the older 20-question public pilot and its five-attempt research setting.

**Checkpoint, 3 October 2026, 17:32 UTC:** all **352 completed response records** have a first-round review and an immutable private archive. The 25 previously unsent requests each completed on their first submission; eight earlier transport-uncertain requests remain missing and were not resubmitted. No requests remain in flight or unsent. Seven models have all 30 reviewed answers; the full 12-model comparison remains incomplete. The [first-round scorecard](first-round-20261003/SCORECARD.md) compares all models on the same 27 available question IDs and separately identifies complete 30-question scores. It includes score, confirmed cost, time and written scientific-explanation charts.

The original 327-review archive is preserved, with an additive 352-review snapshot after the continuation. The [strict second-round rubric](STRICT_SCORING_V2.md), including its applicability table and [scoring workflow](assets/scoring-workflow-v2.svg), was frozen at the original 327-record checkpoint and remains unchanged. The 25 later responses were graded under the original first-round quality rubric before any second-round grading. No second-round reviews have been created. No private answers or individual reviews are published here.

## Human review and scoring provenance

All 30 questions and their reference answers have been carefully reviewed by the project owner, who confirmed completion on 3 October 2026. Question development combined literature-based drafting, AI assistance and human review. This statement applies to the current 30-question set; it does not certify the entire earlier discovery archive or imply two independent expert approvals.

Candidate-answer scores are assigned by Codex through individual reading. This is a single AI referee, not a human expert panel. The first round is unblinded and provisional. Human review of questions and references and AI scoring of candidate answers are separate activities.

## Two scoring rounds, kept separate

### Research scoring amendment, 3 October 2026

At the owner's explicit request, **both rounds, including round one**, use the following research-reasoning item score:

**Research score = 60 × qualified historical-direction Hit@1 + 0.40 × scientific quality.**

Scientific quality is scored from 0 to 100. Hit@1 is 1 only when the biological question, mechanism, intervention, readout and predicted outcome jointly match the sealed follow-up target without a critical control or inference failure; otherwise it is 0. Keyword overlap alone is insufficient. Component-level matches and exact evidence remain available in private review records. Missing matching review is unavailable, not a miss.

For example, a direction miss with scientific quality 100 receives 40; a qualified hit with quality 70 receives 88. A scientifically valuable alternative direction can therefore retain a high quality score while receiving a lower combined research score. This benchmark explicitly prioritizes the selected historical continuation; it does not establish that other research directions lack value or novelty.

The ten research scores are averaged before receiving the 50% category weight. Essay and experimental-design means retain their 20% and 30% weights. There is exactly one candidate answer per question. No answer regeneration or best-of-five selection is introduced.

This is an **owner-requested post-hoc weighting amendment**, made after some answers had been inspected. Existing scientific-quality scores, historical matching judgments, deduction evidence and candidate hashes are retained; only derived item/category/overall scores are recalculated. Earlier report snapshots are archived. The later stricter deduction policy remains a separate second-round change.

1. **Finish the existing round.** Read each available final answer against the frozen question, evidence and existing scientific-quality rubric. Apply the research-weight amendment above from this round. Save exact evidence for deductions and retain the original response hashes. Finish and archive this round before introducing the stricter deduction policy.
2. **Specify and freeze the stricter rubric.** Turn the owner's requirements below into an English, item-applicable checklist, with explicit deduction rules and a scoring flowchart. Freeze it before the second round begins.
3. **Regrade every saved answer.** Use the same candidate responses; do not ask models to regenerate answers. Save a separate second-round review for each answer. Keep both scoring versions, explain score changes and do not rewrite the first round.

The revised assessment is a **post-hoc rescore requested after inspection of some answers**. It must be labeled as such. No company or model receives a targeted adjustment. Model identity, reputation and desired ranking are not scoring criteria.

## Requested additions for the next rubric

The owner requirements below are now formalized in [strict-v2.0](STRICT_SCORING_V2.md). That document defines the complete applicability, evidence, calibration and non-duplication rules. Its new quality scale starts at 100 and deducts distinct failures, rather than subtracting again from first-round scores that already penalized some omissions. The two score versions remain separate.

| Requested criterion | Requested deduction |
|---|---:|
| For molecular biology, biochemistry and circuit experiments: verify what the relevant controls establish and design them before the experiment | 10 points when the requirement is unmet |
| Across all four domains: explicitly propose consulting prior papers' Methods or validated protocols for detailed conditions before execution | 10 points when absent |
| Each applicable, separately specified requirement for quantitative conditions, measurement, failure analysis or data-to-conclusion reasoning | 5 points when unmet |

The detailed checklist will cover executable conditions, amounts and units, timing, dose and parameter ranges, controls, pilot calibration, quantitative endpoints, tool assumptions, parameter sensitivity, failure diagnosis, iterative troubleshooting, and observations that would falsify the hypothesis. Bioinformatics conclusions must remain within what the data and tools identify.

Examples must be technique-specific: delivery titer and dose where a viral system is relevant; amplicon length and amplification conditions for PCR; substrate identity, enzyme activity, substrate amount, reaction volume, buffer, temperature and time for a digestion; and acquisition, background correction and intensity or positive-frequency definitions for fluorescence measurements. DNA restriction digestion and RNA-directed enzymatic assays must not be conflated.

Because candidates could not browse, the Methods criterion concerns an explicit plan to consult and verify relevant methods, not a false assertion that a search occurred. A planned lookup does not substitute for correct controls or an actionable design. Where a question explicitly requires calibration of unknown values, invented numerical precision must not earn credit; the revised rubric must reconcile that constraint with the request for executable detail.

Before rescoring, document which checks apply to each question, what earns full satisfaction, how partial or absent evidence is handled, and how deductions are bounded. Unrelated techniques are not required. Each deduction needs a criterion ID and answer evidence or a documented absence after a full read. The same omission must not be multiplied through synonymous checklist entries.

## Reporting and availability

Results remain incomplete while responses or reviews are missing. Missing API responses block a full benchmark score; valid refusals remain part of the evaluated record. Transport-uncertain requests are not blindly resubmitted. Confirmed charges, unresolved billing, elapsed response time and visible scientific-explanation quality are reported separately. No private chain of thought is evaluated.

Private answer keys, candidate response records and individual grading records are kept outside this public repository. No real raw-data pipeline execution or laboratory validation is established by these written answers.
