# Current 30-question evaluation

The current comparison uses 12 models and 30 questions: ten essays, ten experimental designs and ten research-reasoning questions. Each question receives exactly one independently generated answer. Category means receive weights of 20%, 30% and 50%, respectively. Model browsing and tools are disabled. This configuration is separate from the older 20-question public pilot and its five-attempt research setting.

## Human review and scoring provenance

All 30 questions and their reference answers have been carefully reviewed by the project owner, who confirmed completion on 3 October 2026. Question development combined literature-based drafting, AI assistance and human review. This statement applies to the current 30-question set; it does not certify the entire earlier discovery archive or imply two independent expert approvals.

Candidate-answer scores are assigned by Codex through individual reading. This is a single AI referee, not a human expert panel. The first round is unblinded and provisional. Human review of questions and references and AI scoring of candidate answers are separate activities.

## Two scoring rounds, kept separate

1. **Finish the existing round.** Read each available final answer against the frozen question, evidence and existing rubric. Save exact evidence for deductions and retain the original response hashes. Finish and archive this round before introducing the revised scoring policy.
2. **Specify and freeze the stricter rubric.** Turn the owner's requirements below into an English, item-applicable checklist, with explicit deduction rules and a scoring flowchart. Freeze it before the second round begins.
3. **Regrade every saved answer.** Use the same candidate responses; do not ask models to regenerate answers. Save a separate second-round review for each answer. Keep both scoring versions, explain score changes and do not rewrite the first round.

The revised assessment is a **post-hoc rescore requested after inspection of some answers**. It must be labeled as such. No company or model receives a targeted adjustment. Model identity, reputation and desired ranking are not scoring criteria.

## Requested additions for the next rubric

These requirements are recorded now; the revised rubric is **not yet active**. Its final applicability matrix and scoring flowchart will be published after the existing round is complete.

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
