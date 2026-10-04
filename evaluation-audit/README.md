# Open scoring audit

Both rounds are published here: **360 original answers, 360 first-round reviews, 360 second-round reviews and 7,560 second-round criterion decisions**. All scores and quoted evidence are the saved referee judgments; publication does not regrade an answer.

The owner explicitly authorized this release on 4 October 2026. It supersedes earlier statements that individual reviews would remain private. Frozen rubric snapshots retain that earlier release-policy text for provenance; the scientific criteria are unchanged.

## Browse by model

| Model | Answers and side-by-side scores |
|---|---|
| GPT-6 Astra | [30-question index](models/gpt-astra.md) |
| GPT-5.6 Sol | [30-question index](models/gpt-sol.md) |
| GPT-5.6 Terra | [30-question index](models/gpt-terra.md) |
| Claude Fable 5 | [30-question index](models/claude-fable.md) |
| Claude Opus 4.6 | [30-question index](models/claude-opus46.md) |
| Claude Opus 4.8 | [30-question index](models/claude-opus48.md) |
| Gemini 3.1 Pro Preview | [30-question index](models/gemini-pro.md) |
| DeepSeek V4.1 Flash | [30-question index](models/deepseek.md) |
| Qwen3.8 Max (0902) | [30-question index](models/qwen.md) |
| Kimi K3 | [30-question index](models/kimi.md) |
| GLM 5.3 FlashX | [30-question index](models/glm.md) |
| Grok 4.7 | [30-question index](models/grok.md) |

## Reproduce and inspect

- [Scoring process and limits](PROCESS.md)
- [First-round review JSON files](round-one/reviews)
- [First-round derived item scores](round-one/item-scores.csv)
- [First-round clarifications](round-one/clarifications)
- [Second-round review JSON files](round-two/reviews)
- [All second-round criterion decisions and exact evidence](round-two/checks.csv)
- [Review amendments and preserved prior versions](round-two/amendments)
- [Historical-direction matching audits](round-two/matching-audits)
- [Export provenance and redaction log](EXPORT-MANIFEST.json)
- [Public file checksums](SHA256SUMS.json)
- [Independent score verification script](verify_scores.py)

Run `python evaluation-audit/verify_scores.py` from a repository checkout. Python 3.10+ standard library only; no API, key or model call is required. The script verifies file hashes, answer hashes, quote anchors, all 720 scores and all 24 model totals against the published reports. It checks the saved decisions; it does not perform or automate scientific judging.

## What is and is not in this release

Final candidate text, reviewer explanations, deduction evidence and component-level matching are public. These are visible audit records, not hidden chain-of-thought. Raw provider envelopes, account/generation identifiers, credentials and local filesystem paths are excluded. The export manifest preserves original review hashes and identifies only the removed locator fields. Original private records remain unchanged.

Original candidate-record hashes refer to the preserved full provider records. Published answer-text hashes can be verified independently; the public final-answer projection cannot reconstruct the original provider-envelope hash.

Human review of original questions/references is distinct from scoring: the owner reviewed v1; revised references await owner review. Scores were assigned by one unblinded Codex referee and can be challenged using the evidence here. Historical matching and the stricter rubric are post-hoc.
