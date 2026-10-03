# Life Sciences Research Benchmark

Evaluate how models answer biological questions, design experiments, reason about competing explanations, and assess papers from fixed evidence.

**Current comparison:** 12 models, 30 questions, one answer per question. The project owner has carefully reviewed all 30 questions and reference answers. The existing scoring round will be completed before a separate, stricter rescore begins. See [current evaluation and review status](docs/CURRENT_EVALUATION.md) for the 20/30/50 category weights, reviewer provenance and requested rubric changes. The public pilot described below is an earlier, separate configuration.

The primary outcome is whether an answer helps a researcher make a sound decision and advance the work. Scientific accuracy, decision value, actionability, verifiability and clear communication determine the user-service score. Keywords, logic, protocol detail and historical follow-up hits are reported as supporting diagnostics; long answers and author imitation do not establish usefulness.

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
