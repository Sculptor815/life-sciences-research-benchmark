# Life Sciences Research Benchmark

Evaluate how models answer biological questions, design experiments, reason about competing explanations, and assess papers from fixed evidence.

**Current comparison:** the strict second round is complete: **12 models, 30 questions each, 360 reviewed responses**. I carefully reviewed all 30 questions and original reference answers. The [complete second-round results](docs/second-round-20261004/SCORECARD.md) are the final scoring version for this run; the [first-round results](docs/first-round-20261003/SCORECARD.md) remain archived. All answers were reused without new candidate or judge API calls. The [open question set](benchmark-30/README.md) includes both reference versions and the [final rubric](benchmark-30/v2/RUBRIC.md). Revised references await my review. See [status and provenance](docs/CURRENT_EVALUATION.md).

## Second-round results

Scores use 20% essay, 30% experimental-design and 50% research-reasoning category means. Each research item combines 60% qualified historical-direction Hit@1 and 40% strict scientific quality. The rubric and direction weighting are post-hoc; scoring was performed by one unblinded Codex referee. A valid alternative research direction can receive quality credit without matching the selected historical continuation.

| Model | Essay | Design | Research | Total /100 | Direction hits /10 |
|---|---:|---:|---:|---:|---:|
| GPT-6 Astra | 72.50 | 60.00 | 54.40 | **59.70** | 5 |
| GPT-5.6 Sol | 70.00 | 59.00 | 57.40 | **60.40** | 6 |
| GPT-5.6 Terra | 71.50 | 45.00 | 24.20 | **39.90** | 1 |
| Claude Fable 5 | 50.00 | 12.50 | 13.00 | **20.25** | 1 |
| Claude Opus 4.6 | 53.00 | 25.00 | 15.00 | **25.60** | 1 |
| Claude Opus 4.8 | 60.00 | 34.50 | 22.20 | **33.45** | 2 |
| Gemini 3.1 Pro Preview | 52.00 | 17.00 | 6.00 | **18.50** | 0 |
| DeepSeek V4.1 Flash | 67.50 | 36.00 | 18.60 | **33.60** | 1 |
| Qwen3.8 Max (0902) | 64.50 | 34.00 | 27.60 | **36.90** | 2 |
| Kimi K3 | 67.50 | 52.50 | 31.80 | **45.15** | 2 |
| GLM 5.3 FlashX | 60.00 | 28.00 | 23.60 | **32.20** | 2 |
| Grok 4.7 | 66.50 | 50.00 | 23.00 | **39.80** | 1 |

[Full results and original cost/time metrics](docs/second-round-20261004/SCORECARD.md) | [Model metrics CSV](docs/second-round-20261004/model-summary.csv) | [All 360 item scores](docs/second-round-20261004/item-scores.csv)

Model order follows the frozen roster. All selected answer hashes, 7,560 checklist records and score calculations passed consistency checks; the first-round archive remains intact. Second-round API expense: **$0**. The new charts below summarize the complete second round. Earlier charts remain in the separately labeled first-round archive.

## Second-round visual summary

| Answer quality | Original API expense |
|---|---|
| ![Second-round answer quality](docs/second-round-20261004/answer-quality.png) | ![Original selected-answer expense](docs/second-round-20261004/api-expense.png) |
| Response time | Scientific explanation quality |
| ![Original request time](docs/second-round-20261004/response-time.png) | ![Second-round written explanation quality](docs/second-round-20261004/explanation-quality.png) |

![Second-round scores for all 360 answers](docs/second-round-20261004/reviewed-item-scores.png)

[Four-chart high-resolution overview](docs/second-round-20261004/four-metric-overview.png) | [Scalable overview](docs/second-round-20261004/four-metric-overview.svg) | [All figures as PDF](docs/second-round-20261004/second-round-figure-collection.pdf)

PNG exports are 300 DPI; SVG and PDF versions preserve vector detail. Provider colors match the first round. R marks an empty refusal; P marks a partial answer. Other zero scores are rubric outcomes. Expense is from original selected answers, with unresolved bills excluded; rescoring added $0 in candidate/judge API charges.

## Archived first-round results

The four charts compare the same 30 questions for every model. Essay, design and research category means carry 20/30/50 weights. Research items combine 60% qualified historical-direction hit and 40% scientific quality, under the documented post-hoc amendment. Provider colors are green for OpenAI, copper for Anthropic and slate blue for other providers; colors do not affect scoring.

| Answer quality | API expense |
|---|---|
| ![First-round answer quality](docs/first-round-20261003/common_score.png) | ![Confirmed run cost](docs/first-round-20261003/common_cost_confirmed_usd.png) |
| Response time | Scientific explanation quality |
| ![Mean response time](docs/first-round-20261003/common_mean_response_seconds.png) | ![Written explanation quality](docs/first-round-20261003/explanation_mean.png) |

**360 question scores:** R marks a refusal; P marks a partial answer. Research cells already include the 60/40 direction/quality weighting.

![Reviewed question scores for all 12 models and 30 questions](docs/first-round-20261003/reviewed-item-scores.png)

[Four-chart high-resolution overview](docs/first-round-20261003/four-metric-overview.png) · [Scalable overview](docs/first-round-20261003/four-metric-overview.svg) · [Scalable heatmap](docs/first-round-20261003/reviewed-item-scores.svg) · [Metrics CSV](docs/first-round-20261003/model-summary.csv)

Confirmed run charges are **$35.6704**, with **16 unresolved bills** excluded. Means include provider/network waiting; they are not wall-clock completion times. Explanation scores concern visible scientific arguments, not hidden reasoning; Fable's mean uses 19 assessable answers out of 30. These are exploratory results from one unblinded Codex referee, not an independently validated leaderboard.

## Open questions, references and scoring

[Read all 30 questions](benchmark-30/QUESTIONS.md) and follow each question's links to its original and revised reference answers. The [reference revision log](benchmark-30/v2/REFERENCE-CHANGES.md) records scientific corrections and added execution detail. The [first rubric](benchmark-30/v1/RUBRIC.md) remains available alongside the [final strict rubric](benchmark-30/v2/RUBRIC.md). New reference revisions await owner review; the confirmed human review applies to the original versions.

![Strict scoring workflow](docs/assets/scoring-workflow-v2.svg)

The opened 30-question comparison is separate from the older pilot below. Its published answers and historical targets make it an exposed evaluation set, not a secret held-out test. Credentials and original provider response records are excluded from this release.

## Benchmark purpose

The purpose is to measure whether an answer helps a researcher make sound decisions and advance the work. The current strict rubric assesses scientific correctness, controls, executable procedures, quantitative analysis, failure diagnosis and verifiability. Research scores explicitly prioritize the selected historical continuation at 60%; that preference is not a claim that alternative research directions lack value. Long answers alone do not establish usefulness.

**Status: development benchmark, version 0.3.0.** The runnable public pilot has 20 open-response drafts. Private revised reference answers contain 421–636 words for essays, 949–1,082 for design, and 1,279–1,341 for reasoning. Ten additional disputed-paper essays have separate 500-plus-word private answers. The earlier private discovery-review collection contains 46 research/controversy cases and 178 candidate questions with draft reference answers, source-reading records and review tools. The older 178 candidates are an archived discovery collection; they have not all been upgraded to the current answer-depth contract. Candidates are not a formal question bank. No expert approvals or real model leaderboard are claimed.

Start with the [installation and walkthrough](docs/QUICKSTART.md). The [researcher needs](docs/USER_NEEDS.md) define what useful assistance should accomplish. Read the [evaluation method](docs/METHOD.md) before interpreting scores. Coordinators should also read the [authoring and review guide](docs/AUTHORING.md).

## What is evaluated

| Domain | Coverage |
|---|---|
| Molecular biology | Gene expression, KO/knockdown/rescue, WB and antibody specificity, immunofluorescence, protein purification and interactions |
| Biochemistry | Metabolism, enzyme kinetics, inhibition and allostery, flux, assay interference, macromolecule biosynthesis |
| Neuroscience | Circuit structure, activity measurements, optogenetics, behavioral experiments, motor/sensory/stress confounds |
| Bioinformatics | Multiomics integration, enrichment, pseudotime, GWAS, whole-genome sequencing |

Molecular and biochemical methods apply across disease areas. Each question has one primary domain and separate technique, topic and research-context tags. A cancer signaling experiment may be a molecular-biology question; a multiomics analysis of the same disease may be a bioinformatics question. Cross-disciplinary questions count once.

Each domain is evaluated in three open-response abilities: **essay, experimental design, and research reasoning**. The question track tests scientific judgment using supplied materials. Model browsing and tools are disabled in that track. A separate author-side script executes seven small synthetic analysis workflows; it does not score an agent's programming ability or establish real-data pipeline validity.

The [discovery-review guide](docs/DISCOVERY.md) explains textbook selection, frozen evidence packets, private answers, candidate review and pipeline limits. Core textbook selection requires documented adoption by leading US university courses, with edition, semester and required/recommended status distinguished. Open supplementary teaching resources do not substitute for this evidence.

## Pilot and full benchmark

| Set | Text | Image | Total |
|---|---:|---:|---:|
| Current draft pilot | 16 | 4 | 20 |
| Planned public set | 36 | 12 | 48 |
| Planned held-out set | 156 | 36 | 192 |
| Planned complete bank | 192 | 48 | 240 |

The full bank has 12 domain-by-ability cells. Each cell contains 16 text and 4 image questions, including 3 public text and 1 public image question. Formal scores use held-out questions only. Text and image scores are separate.

The pilot covers all 12 cells and adds one visual essay per domain. It does not yet cover image-based design or reasoning. The revised 240-slot coverage plan contains targets, not completed or assigned questions.

## Install

Python 3.11 or newer is required. From the repository directory:

```console
python -m venv .venv
# Windows PowerShell:
.venv\Scripts\python.exe -m pip install -e ".[runtime,review]"
# macOS/Linux:
.venv/bin/python -m pip install -e ".[runtime,review]"
```

The core validator, mock runner and reports use Python's standard library. For an initial mock-only installation, use `pip install -e .` instead. Inspect AI is needed for API calls; Streamlit is needed for the review interface. Matplotlib and NumPy are only needed to redraw the already supplied synthetic figures.

## First run

The supplied mock configuration saves runs in the sibling `life-sciences-research-benchmark-private/runs` directory. Relative paths resolve from the configuration's directory, so the D-drive checkout and a new clone use the same layout. Change `output_root` to choose another private location.

```console
lsrw validate
lsrw run --config configs/mock.json --dry-run
lsrw run --config configs/mock.json
```

The 20 questions schedule 36 independent samples (five per reasoning question and one for other questions), with no cross-sample feedback. The last command prints the absolute run directory. Keep it for later commands. Each run contains a question/material snapshot, request hashes, responses, attempt records, versions and checksums. The mock deliberately returns weak answers and does not read answer keys.

Scoring requires an externally stored key file. The maintainer's draft keys are delivered separately in the private project directory. A public checkout alone can run questions but cannot supply expert gold standards.

```console
lsrw score --run "ABSOLUTE_RUN_DIRECTORY" --keys "PRIVATE_DIRECTORY/draft-keys-v0.3.json"
lsrw report --run "ABSOLUTE_RUN_DIRECTORY" --output "PRIVATE_DIRECTORY/reports/first-preview"
```

All questions are open responses and remain pending until two experts have reviewed them. Research reasoning uses five independent samples, each reviewed separately; reports distinguish best-answer quality from historical hit-at-5. A preview report can be generated immediately; missing expert scores remain visible and the run is excluded from formal ranking.

## Expert review

```console
lsrw review --prepare --run "ABSOLUTE_RUN_DIRECTORY" --keys "PRIVATE_DIRECTORY/draft-keys-v0.3.json" --output "PRIVATE_DIRECTORY/reviews/round-1" --reviewers reviewer-a reviewer-b
lsrw review --queue "PRIVATE_DIRECTORY/reviews/round-1/rater-1/queue.json"
```

Give each reviewer only their own queue and material access. The interface hides model configuration and the other reviewer's scores. Local files do not provide account-based access control; the coordinator is responsible for file separation. An answer may identify its model in its own text; document any resulting loss of blinding.

After both reviews, run `lsrw score` again with `--reviews`. Cases requiring a third reviewer remain pending until an adjudication file is supplied. See [the review guide](docs/AUTHORING.md) for the file format and commands.

## API evaluations

Copy `configs/api.template.json` into your private directory and set absolute dataset and output paths. Fill in an exact Inspect model identifier, supported generation settings, a budget, dated token prices, and an input-token ceiling. Keep provider credentials in environment variables. The template deliberately refuses to run while prices and budget are unset.

Run with `--dry-run` first to inspect request counts and reservation estimates. Use `lsrw run` for budget accounting. The optional `lsrw.inspect_tasks.public_pilot` task supports exploratory Inspect workflows, but direct `inspect eval` does not enforce Benchmark budget reservations or formal eligibility.

Prices and token ceilings are user-supplied estimates, not a provider-enforced spending limit. Configure a provider-side limit as well. Image and reasoning-token accounting require particular care. Requests stop when the next reservation would exceed the budget or reported usage exceeds the configured ceilings. A completed answer is never selectively retried. The five reasoning samples are scheduled in advance, including refusals and empty completions.

## Development and release

```console
python -m unittest discover -s tests -v
python scripts/package_release.py --manifest release-files.txt --output ../public-release.zip
```

The release script includes only explicitly listed public files, validates that dataset splits are public, and produces a SHA-256 inventory inside the archive. It excludes runs, reviewer identities and grading records. Never upload the private sibling directory.

See [implementation status](docs/STATUS.md) for completed checks and the remaining scientific review gates. The public repository contains only the explicit release inventory; private research corpora, draft answers and review records stay outside it.

Code: MIT. Original pilot questions and synthetic figures: CC BY 4.0, attributed to Life Sciences Research Benchmark contributors. External references retain their own licenses; linked papers and figures are not redistributed.

The [ten-paper audit selection](docs/DISPUTED_PAPERS.md) distinguishes fabrication findings from narrower reliability concerns. The [raw-data reproduction protocol](docs/REPRODUCTION.md) defines input, figure and numerical-evidence requirements. High-quality textbook exercises and official solutions may inform original questions; [authoring rules](docs/METHOD.md) address source tracking and memorization.
