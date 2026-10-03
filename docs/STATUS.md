# Implementation status — 2026-10-03

## Current comparison

The ongoing private evaluation uses 12 models and 30 questions, with one answer per question and category weights of 20/30/50. The project owner confirmed careful human review of all 30 questions and their reference answers. Codex is scoring candidate answers under the existing rubric first; a stricter second round will follow without replacing those results. [Current evaluation](CURRENT_EVALUATION.md) records the review provenance and requested additions. The implementation details below describe the earlier public pilot, whose settings are separate.

Version 0.3 is a development benchmark. No completed expert-validated bank, paid-model leaderboard, laboratory-validated protocol or full-paper raw-data reproduction is claimed.

## Current implementation

- Four domains and three open-response tasks: essay, experimental design and research reasoning. The active public pilot has 20 questions across 12 cells, including four visual essays. The revised blueprint has 240 unfilled target slots (48 public, 192 held out).
- Primary scoring evaluates service to the researcher: scientific accuracy, decision value, actionability, verifiability and communication. Concept/logic/protocol quality and historical matching remain separate diagnostics. This proposed rubric needs expert calibration and user-outcome validation.
- All 20 active reference answers were expanded and revised privately. Essay answers are 421–636 words, design 949–1,082 words, and reasoning 1,279–1,341 words. Validators enforce more than 300/900/1,200 words respectively and require concepts, directed logic links and protocol records.
- Four retrospective original-to-later research pairs, one per domain, with private target articles and author overlap. Each reasoning task schedules five independent samples without feedback. First-sample utility, best utility, technical scores and historical hit-at-1/hit-at-5 are preserved separately. Exact earliest-disclosure and complete source-method audits remain incomplete and block formal admission.
- Ten real disputed-paper essay drafts in nine families, each with a private 502–539 word answer and an explicit evidence-to-error chain. The public selection lists original papers, notices and audit focus. These are paraphrased candidate packets; original raw forensic data were not independently reanalyzed for all ten.
- A private 30-question readable answer book and a separate review page with exported human decisions. Twenty questions are runnable in the public pilot; the ten disputed-paper essays are separately reviewed candidates.
- Raw-data submission checks for input/artifact hashes, complete prespecified metrics and numerical tolerances. These checks do not execute submitted code or certify offline agent capability.
- English public documentation, UI and rubrics; explicit public-file release inventory. Private answers, future targets, raw harness logs and reviewer records remain outside GitHub.

## Verification

- 58 automated tests passed locally, including real installed Inspect/Streamlit integrations, answer isolation, five independent samples, per-sample seed records, no cross-answer merging of historical matches, user-service scoring, fatal-premise handling and reproduction-check rejection of processed or modified inputs.
- The current 20-question mock run completed 36 samples and produced a report plus two blinded 36-response review queues. Every scientific score remains pending; no human ratings or paid model evaluations were fabricated.
- Dataset draft validation and request/cost preflight passed. Formal validation remains blocked by incomplete bank coverage and expert approval.
- Seven earlier synthetic analysis checks passed in the recorded scientific environment. These do not certify raw biological-data reproduction.
- The earlier migration verified 1,772 copied files by SHA-256, retained the C-drive originals and established the D-drive runtime. Historical records retain their bytes. Use the original software version when rescoring historical runs.

## Remaining scientific and execution gates

1. Review all current scientific answers, their full sources and supplements, parameter provenance, alternative designs and item-specific anchors with independent domain experts. Long answers alone are not complete protocols.
2. Resolve exact protocol inputs and review readiness for design/reasoning questions; certify chronology using earliest public disclosures, including preprints and code.
3. Upgrade the earlier 46-case/178-question discovery archive. It remains readable, but its old task types and shorter answers do not satisfy the new contract; current export rejects unupgraded records. It is not included in the 30 revised answers.
4. Acquire and independently analyze licensed raw artifacts for the ten integrity cases, include author responses and matched reliable controls, and measure false accusations as well as detection.
5. Complete real raw-data paper-to-figure reproductions and an OS-isolated agent execution harness. Validate numerical targets and confirm that outputs actually derive from submitted code and original data.
6. Build the 240-slot bank, including visual design/reasoning, then calibrate and lock it. Assess usefulness with blinded researchers attempting to act on the answers, rather than relying only on reference matching.
7. Validate a paid evaluation-provider integration before production use. DeepSeek Harness assisted authoring; that is separate from running it as an evaluated Benchmark provider.
