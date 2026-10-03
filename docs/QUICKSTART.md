# Installation and first evaluation

The Workbench evaluates models on the same questions. It also provides a candidate-review page organized around original discoveries; see the [discovery and review guide](DISCOVERY.md). The seven implemented analysis checks use synthetic data and validate author-side workflows, not a model's programming ability.

## 1. Separate public and private files

The current Windows checkout uses this layout:

```text
D:\life sciences research workbench\
  life-sciences-research-workbench\          # Public code and public questions
  life-sciences-research-workbench-private\  # Do not upload to GitHub
    draft-keys-v0.3.json                          # Draft answers and rubrics
    heldout\                                # Future held-out questions
    runs\                                   # Model responses
    reviews\                                # Ratings and reviewer identities
    reports\                                # Reports before publication
```

Use the same sibling-directory layout when working elsewhere. The supplied configurations resolve output paths relative to their own directory. Keep private material outside the public checkout and GitHub upload area.

## 2. Create a Python environment

The current D-drive checkout already has an editable installation in `.venv`, based on Python 3.12.9 with access to its system packages. Inspect AI and Streamlit are installed and their integration tests pass. The following commands create a fresh environment on a machine with Python 3.11 or newer. The Windows CLI enables UTF-8 automatically; use `python -X utf8` when running tests directly.

```powershell
Set-Location 'D:\life sciences research workbench\life-sciences-research-workbench'
$env:PIP_CACHE_DIR = 'D:\life sciences research workbench\pip-cache'
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -e .
```

The core installation is sufficient for free mock evaluations. Install the optional provider and review interfaces with:

```powershell
.\.venv\Scripts\python.exe -m pip install -e '.[runtime,review]'
```

You do not need to change PowerShell's execution policy or activate the environment. Call programs under `.venv\Scripts` directly. On macOS/Linux, use `.venv/bin` and choose appropriate output paths.

## 3. Validate the pilot

```powershell
.\.venv\Scripts\lsrw.exe validate
```

Expect 20 questions and `valid: true`. This checks structure, tags and asset hashes, not expert approval of scientific content.

```powershell
.\.venv\Scripts\lsrw.exe validate --formal
```

Formal validation currently fails by design: the 240-question bank is incomplete and the pilot remains a draft.

## 4. Run a free mock evaluation

Check `output_root` in `configs/mock.json`. The default points to the private sibling directory. A dry run sends no model requests and creates no run records.

```powershell
.\.venv\Scripts\lsrw.exe run --config configs/mock.json --dry-run
.\.venv\Scripts\lsrw.exe run --config configs/mock.json
```

Save the absolute run directory printed at the end. The mock is a local testing adapter; its score says nothing about an actual model provider.

## 5. Generate a report

Replace `RUN_DIRECTORY` with that absolute path and `KEY_FILE` with your private draft-answer file.

```powershell
.\.venv\Scripts\lsrw.exe score --run 'RUN_DIRECTORY' --keys 'KEY_FILE'
.\.venv\Scripts\lsrw.exe report --run 'RUN_DIRECTORY' --output '../life-sciences-research-workbench-private/reports/preview-1'
```

Open the generated `REPORT.html` in a browser. The output also includes `report.json` and `scores.csv`. Open responses remain pending and the overall score remains empty; missing ratings are not converted to zeros.

Results are versioned. If rescoring produces another artifact, select it with `--scores 'ABSOLUTE_SCORE_FILE'` and use a new report directory.

## 6. Obtain two independent expert ratings

```powershell
.\.venv\Scripts\lsrw.exe review --prepare --run 'RUN_DIRECTORY' --keys 'KEY_FILE' --output '../life-sciences-research-workbench-private/reviews/round-1' --reviewers expert-a expert-b
.\.venv\Scripts\lsrw.exe review --queue '../life-sciences-research-workbench-private/reviews/round-1/rater-1/queue.json'
```

The interface listens on `127.0.0.1` only. The second expert uses the `rater-2` queue. Choose 0–4 for every dimension using the task-specific weights and provide an evidence-linked rationale. Reasoning adds five explicit historical-match judgments for each independent sample. Scores have no preselected default; submitted records are preserved.

```powershell
.\.venv\Scripts\lsrw.exe score --run 'RUN_DIRECTORY' --keys 'KEY_FILE' --reviews '../life-sciences-research-workbench-private/reviews/round-1'
```

The report marks unresolved disagreements as `needs_adjudication`. See the [authoring and scoring guide](AUTHORING.md) for the third expert's procedure.

## 7. Configure a real provider

Copy `configs/api.template.json` into the private directory and configure:

| Field | Required decision |
|---|---|
| `model` | An exact Inspect provider/model identifier; record the version, not just the product name |
| `dataset`, `output_root` | Absolute paths for questions and outputs |
| `track` | `text`, `image` or `all`; compare models on the same questions |
| `supports_images` | Whether the model supports images; do not replace them with answer-bearing descriptions |
| `generation` | Provider-supported sampling or reasoning settings; omit uncertain options |
| `max_output_tokens` | Per-question output limit, accounting for response length and reasoning billing |
| `input_token_ceiling` | Input reservation including image and message overhead |
| `budget_usd` | Maximum Workbench reservation for the run |
| Both `*_usd_per_million` fields | Current input and output prices per million tokens in USD |
| `pricing_date`, `pricing_source` | Date and source of the price check |

Provide credentials through the provider's environment variables, never in questions or configuration files. No paid model evaluation has yet run through the Workbench. DeepSeek Harness used the existing signed-in account for authoring and review; those activities are recorded separately.

Run `--dry-run` first to check request counts, retry limits and estimated cost. Then run without that flag. Reservations depend on configured prices and ceilings; also set provider-side billing limits. Reasoning budgets across providers are not assumed equivalent.

Keep `formal` set to `false` until the complete bank, expert review, calibration and locking are finished.

## Next steps

Read the four bioinformatics text questions in `data/public/items.jsonl` and their private rubrics to assess difficulty and research context. Ask two reviewers and an adjudicator per domain to trial the drafts. Stabilize the scoring guidance before expanding against the coverage plan.
