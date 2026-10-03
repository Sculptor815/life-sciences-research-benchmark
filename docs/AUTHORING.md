# Authoring, review and scoring

## Organization

The four primary domains are molecular biology, biochemistry, neuroscience and bioinformatics. Molecular and biochemical methods apply across diseases; cancer, inflammation and metabolic disease belong in research-context tags. Each question counts toward one primary domain and one ability. Record other connections in supporting tags to avoid double counting.

Bioinformatics questions should test research judgment: whether data suit a method, whether the experimental unit and statistical assumptions are appropriate, what level of inference the results support, and what independent validation is needed. Naming software alone is insufficient for a high open-response score. Actual tool operation requires a separate track with executable environments and data.

Assign at least two reviewers and one independent adjudicator per domain. Use reviewer codes and keep the identity mapping in the private directory. The software checks that codes differ; it cannot verify expertise or replace human review.

## Inspect the pilot first

Each line of `data/public/items.jsonl` contains one public question. The private `draft-keys-v0.3.json` stores answers, evidence locations, five-dimension rubrics, scoring anchors and acceptable alternatives by question ID. All 20 pilot questions were drafted with AI assistance and have not received human expert approval.

The draft rubrics provide 0–4 anchors and error guidance. Experts should check whether adjacent scores are distinguishable, reasonable alternative methods are accepted, and the same error is not penalized repeatedly without justification. These drafts are not validated measurement scales.

## Expand the question bank

Use `templates/item.json` for candidate-visible content. Use `templates/open-key.json` for private answers and open-response rubrics. Reference answers must not enter the question JSONL. `data/coverage-plan.csv` lists 240 target slots; it does not represent 240 completed questions.

For each question, record:

1. A unique ID, case family, source-paper family and version.
2. Primary domain, ability, topics, techniques, research context and difficulty.
3. An English prompt, fixed evidence packet, response format and length limit.
4. For images: the original asset, processing history, license, attribution and SHA-256.
5. In the separate answer file: justification, evidence locations, scoring criteria, partial credit, alternatives and critical errors.

An image question must require information from the image. Do not substitute an answer-bearing text description for the image. Label synthetic figures as teaching or simulated materials, not measured results. Similar rewrites of the same paper or experimental case remain in one family.

Paper-appraisal questions need enough fixed evidence to distinguish source identity from the support for a conclusion. Allow “insufficient material to verify” when identity cannot be established. A fictional-source label requires explicit evidence or a controlled synthetic identity. Date snapshots of retractions and corrections so historical information is not presented as a live status check.

## Review and lock

Two reviewers independently check sources, attempt each question, inspect the rubric and verify material rights. The private approval file uses the following format, with two independent records per question:

```json
{
  "domain_roster": {
    "molecular_biology": {"reviewers": ["mol-a", "mol-b"], "adjudicator": "mol-c"},
    "biochemistry": {"reviewers": ["bio-a", "bio-b"], "adjudicator": "bio-c"},
    "neuroscience": {"reviewers": ["neu-a", "neu-b"], "adjudicator": "neu-c"},
    "bioinformatics": {"reviewers": ["inf-a", "inf-b"], "adjudicator": "inf-c"}
  },
  "items": {
    "EXAMPLE-ID": [
      {"reviewer": "mol-a", "date": "YYYY-MM-DD", "source_checked": true, "independent_trial_answer": true, "rubric_checked": true, "material_rights_checked": true},
      {"reviewer": "mol-b", "date": "YYYY-MM-DD", "source_checked": true, "independent_trial_answer": true, "rubric_checked": true, "material_rights_checked": true}
    ]
  }
}
```

This is a format example, not an approval record. Change an item's `status` to `reviewed` only after actual review.

Train raters using all 48 final public questions and prepared responses. Preserve paired ratings for open responses; check calculations, units and all five reasoning samples too. The private calibration file must contain `completed_public_ids`, `records` (each with `item_id`, `ability` and `ratings`), `accepted_by`, `acceptance_rationale` and `unresolved_systematic_disagreement: false`. Set the last field only after systematic disagreements have actually been resolved.

```console
lsrw calibrate --records PRIVATE/pairs.json --output PRIVATE/calibration-summary.json
lsrw lock --dataset PRIVATE/full-bank/items.jsonl --keys PRIVATE/keys.json --approvals PRIVATE/approvals.json --calibration PRIVATE/calibration.json --output PRIVATE/bank-lock.json
```

The complete bank requires 240 questions with the specified 12-cell allocation and no source or case-family overlap between public and held-out splits. After locking, changes to questions or rubrics require review and a new version. Do not selectively rerun model responses already collected.

## Rating and adjudication

Each rater receives only their own queue. The interface hides model configuration and the other rater's scores. There is no account system: the coordinator must control file access, and separate local folders are not a security boundary. Record any loss of blinding when a response reveals its model identity.

Each response receives five primary user-service ratings and five technical diagnostic ratings, all on 0–4 scales, with a written rationale. Use the separate weights in METHOD.md. Keyword matches alone cannot establish correct contextual use or complete logic. Apply an error to the dimensions it actually affects and explain distinct consequences. Request adjudication for a gap of at least 2 in either set, a weighted-total gap greater than 10 percentage points in either total, disagreement about a fatal accuracy error, or any source/conclusion/refusal/historical-match disagreement. Exactly 10 points alone does not trigger adjudication; otherwise average paired dimension ratings. The primary score assesses usefulness, while technical and historical outcomes remain separate.

The third expert supplies a separate JSON file indexed by response ID (the question ID for sample one; append `--sample-2` through `--sample-5` for the other reasoning samples). For example, an experimental-design item uses:

```json
{
  "EXAMPLE-ID": {
    "reviewer": "mol-c",
    "scores": {"concept_coverage": 3, "logic_chain": 2, "task_detail": 3, "controls_uncertainty": 2, "conclusion_alignment": 3},
    "rationale": "Replace with the third expert's rationale based on the response, rubric and original disagreement.",
    "source_correct": null,
    "conclusion_correct": null,
    "refusal": false,
    "user_service": {"scientific_accuracy": 3, "decision_value": 3, "actionability": 3, "verifiability": 3, "communication": 3},
    "followup_match": null
  }
}
```

For evidence-appraisal essays, `source_correct` and `conclusion_correct` must each be `true` or `false`. They record the expert's assessment of whether the model's respective judgments were correct. The adjudicator must use the five dimensions for the item's ability and differ from both original raters.

```console
lsrw score --run RUN_DIRECTORY --keys PRIVATE/keys.json --reviews PRIVATE/reviews/round-1 --adjudications PRIVATE/adjudications.json
```

Original ratings are preserved. Revised rubrics require a new scoring round and version. Formal evaluations also check reviewer membership against the locked roster.

## Before publication

Write all public materials in English, including documentation, interface text, questions, rubrics, and contribution descriptions.

Check completeness, formal-ranking eligibility, question counts and confidence intervals. Mock responses, draft-question results and incomplete ratings do not support formal model rankings. Package only the release inventory. Held-out questions, credentials, answers, expert identities and unpublished responses remain private.

Research-reasoning ratings require `followup_match` booleans for `biological_question`, `mechanism`, `intervention`, `readout` and `predicted_outcome`; all other tasks use null. Formal design/reasoning keys require `protocol_readiness: reviewed_and_operational`. Formal reasoning also requires a certified earliest-public-disclosure chronology audit. These gates cannot be replaced by word counts or AI review.
