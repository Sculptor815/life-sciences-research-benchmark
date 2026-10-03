# Implementation status — 2026-10-03

This is a development pilot. It is not a completed or expert-validated 320-question benchmark.

## Delivered

- Four-domain taxonomy and 16 domain/ability cells, including the added bioinformatics domain.
- A 320-slot coverage plan with separate public/held-out and text/image counts.
- Twenty independently authored draft cases: 16 text and 4 visual knowledge questions. All 16 cells have one text exemplar.
- Separate private draft keys: objective answers, per-item five-dimension rubrics, 0–4 anchors, alternative responses, critical-error guidance, and source/evidence references.
- Four original synthetic figures with reusable plotting source and material hashes.
- Standard-library validator, mock runner, immutable run inventories, deterministic objective scoring, blind review queues, third-rater resolution, and content-addressed score artifacts.
- An Inspect AI model adapter and an optional native Inspect public-pilot task. The main Workbench runner uses Inspect's model API and its own audit records; it does not yet export native `.eval` logs for that path.
- A local Streamlit review form, paired-rating calibration summaries and a formal-bank lock command.
- Separate modality reports in HTML/CSV/JSON, equal-cell aggregation, family-cluster bootstrap and same-item paired comparisons.
- English README/method documentation; Chinese installation, question-authoring and expert-review instructions.
- Explicit public release inventory, deterministic archive builder, and a proposed Windows/Linux CI workflow.

## Verification completed locally

- 51 automated checks pass on Python 3.12.9 / Windows, including the installed Inspect AI and Streamlit integration checks, candidate answer isolation, review version binding, malformed research records, source/case split isolation and forbidden model tool requests. Tests ran with Python UTF-8 mode; Streamlit's temporary test page required filesystem permission outside the sandbox. CI has not run on GitHub.
- Seven author-side synthetic workflow checks passed in the recorded scientific Python environment: ORA, paired CCA, donor aggregation/exploratory DE, covariate-adjusted quantitative-trait association, Scanpy clustering, diffusion pseudotime and miniature VCF QC. These are not agent capability scores, real-data validations, or full GATK/DESeq2/MOFA executions.
- A 20-item mock run completed; eight objective items were scored and twelve open items await human review. No expert ratings were fabricated. No paid model calls were made.
- Current public materials pass draft validation. Formal validation correctly rejects this pilot because counts and expert approvals are incomplete.
- Migration verified on 2026-10-03: both project directories were copied to `D:/life sciences research workbench` and all 1,772 copied files matched their source SHA-256 hashes before path updates. C-drive originals are retained. A D-drive virtual environment was created with `--system-site-packages` to reuse the existing Python build tools; offline editable installation and the installed CLI passed validation and dry-run checks. A new mock evaluation, scores, report and review queues were generated on D. Historical records retain their original bytes and paths. See the private `verification-migration.json` for the current verification record.

## Remaining gates

1. Validate at least one paid evaluation provider adapter with a configured budget before considering the API path production-ready. DeepSeek Harness was used for authoring and static review; that is separate from a Workbench evaluation-provider integration.
2. Recruit domain experts, independently trial the pilot and revise scientific content, adjacent scoring anchors, references and acceptable alternatives. Paper teaching archives need review for whether the available evidence makes each source judgment fair.
3. Build and review the final 320 questions. The 320-slot CSV is a blueprint; it is not a generated question bank. The pilot is not yet assigned to formal slots. Add image-based design, reasoning and appraisal cases.
4. Calibrate with the final 64 public items, resolve systematic disagreement and lock the 256 held-out items/rubrics.
5. Select exact model versions, provider-supported settings and budget; execute once per item; complete independent scoring and adjudication.
6. Review release materials, create a dedicated GitHub repository and publish code/public questions. Publish actual scores only after the preceding gates.

## Current limits

- No online identity system or authenticated expert portal. The local coordinator controls review-file separation and expert credentials.
- Hash inventories detect changes but are not signed audit trails. Formal releases should archive manifests externally.
- Refusal classification is human-reviewed for open answers. Objective answers expose format/empty status; a complete all-item refusal audit is not automated.
- Cost control is reservation-based and depends on configured pricing/ceilings. Provider-side budgets remain necessary.
- The current visual pilot and case count are too small for scientific claims about model rankings.
- Public code is prepared for `Sculptor815/life-sciences-research-workbench`. No formal scientific release, leaderboard, completed hidden question bank, or actual model score is claimed. Private research records and answers are excluded from the release inventory.
- Private discovery collection: 46 cases / 178 questions, including DNA damage response, pyroptosis, glycolysis/TCA discovery, neural circuits, analytical methods and four disputed-paper families. Only three original papers have a recorded complete main-text reading in this pass. Other source depths remain visible. Candidate selection does not count as formal expert approval.
- Textbook inventories distinguish official university adoption, publisher edition/TOC verification, actual chapter bibliography retrieval and paper-level reading. No claim of retrieving all references from all core textbooks is made. The 80-concept inventory is a coverage proposal, not 80 completed evidence dossiers.
- A separate question-generation rubric provides six dimensions and 30 behavioral anchors. Missing novelty evidence leaves the total unscored. The quality-summary command checks completeness and arithmetic; it does not authenticate reviewers or validate scientific merit. Twelve private proposed research directions have AI draft ratings, not expert scores.
