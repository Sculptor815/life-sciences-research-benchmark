# From original discoveries to candidate questions

For the revised 30-question answer review, open `research/OPEN-QUESTIONS-v0.3.html`. The older discovery collection remains an archive and has not all been upgraded to the new open-response/reference-length rules. Open `research/REVIEW.html` in the private directory to review the current candidates. It contains source papers, reading depth, original questions, experimental designs, inference limits, artifact hypotheses, candidate questions, draft reference answers and scoring points. Every case awaits human review. The page does not upload comments. It contains answers and must not be given to an evaluated model.

## Select and trace textbooks

Core textbooks require documented adoption in formal courses at leading US universities. Record the institution, course, semester, edition, required or recommended status, and official university URL. Historical syllabi prove use in that offering, not current adoption of the latest edition. Adoption is one selection criterion; domain coverage, primary evidence and teaching quality still require judgment.

Priority candidates include Alberts and Lodish for molecular biology; Stryer/Berg and Voet for biochemistry; Kandel, Purves and Bear for neuroscience; and Durbin and Jones/Pevzner for bioinformatics. Consult the private `textbook-adoption-*.json` records for the actual evidence. Pevsner's publisher-hosted chapter bibliography was retrieved separately; a lecture citation and adoption as a course textbook are different evidence. OpenStax and LibreTexts are supplementary and do not count toward core-textbook coverage.

Trace each chain through five steps: course adoption → edition/chapter → actual chapter references → primary research and subsequent validation → question evidence packet. Thematic relevance is not proof that a book cites a paper. Reading a complete chapter bibliography is not the same as retrieving all literature supporting its concepts. Preserve missing links rather than filling them with model guesses.

The 80-concept inventory is a search plan, separate from the 46 cases and 178 candidate questions. All 114 bibliography entries in the MIT-assigned Jones & Pevzner 2004 textbook have been extracted, with actual reference-number links in the alignment and HMM chapters. This does not mean all 114 primary sources were read. Another 365 entries from seven supplementary units do not count as core coverage. Most direct links between candidate papers and core textbooks still need checking. Complete main-text reading, selected-section reading, abstract reading and later author retrospectives are recorded separately.

## Review candidates

1. Filter by domain or search for a concept. Check the source and which sections or figures were actually read.
2. Read the question and fixed packet before the reference answer. The answer must follow from the supplied evidence or explicitly required background knowledge; the model should not need to browse for missing material.
3. Choose retain, revise or reject and explain why. Retaining a candidate requires checks of the source, question fairness, answer and material rights.
4. Export the review JSON. Browser storage supports continued editing; the exported file is the transferable record.

Reviewer names are self-attested, not authenticated accounts. Page comments and imported records do not automatically turn a candidate into a gold standard. Formal inclusion still requires two independent reviewers, item-specific 0–4 anchors, acceptable alternatives, blinded calibration and source-family separation.

Run these commands from the public project directory. Use new output paths to preserve earlier versions:

```powershell
.\.venv\Scripts\lsrw.exe research audit --corpus '../life-sciences-research-benchmark-private/research/corpus-v0.2.json'
.\.venv\Scripts\lsrw.exe research review --corpus '../life-sciences-research-benchmark-private/research/corpus-v0.2.json' --output '../life-sciences-research-benchmark-private/research/REVIEW-next.html'
.\.venv\Scripts\lsrw.exe research import-decisions --corpus '../life-sciences-research-benchmark-private/research/corpus-v0.2.json' --decisions 'EXPORTED-REVIEW.json' --output '../life-sciences-research-benchmark-private/candidate-reviews'
```

Import checks corpus and case hashes, rejecting stale versions, duplicate decisions and missing rationale. `research export` separates candidate prompts and packets from private answers only after checking the current task types and minimum reference-answer lengths; the older 178-candidate archive will require revision before export. These exports remain drafts, not a formal 240-question bank.

## Build questions from disputed literature

PubPeer provides leads. Comment counts, author silence and failed replication do not individually establish misconduct. Record the original claim, specific concern, author response, journal notice, independent reanalysis and remaining unknowns separately. Verify retraction status against official notices. Retraction does not invalidate every related finding or establish personal intent.

Also examine selective reporting: the denominator of all attempts, preregistered endpoints, exclusion rules, full effect distributions, negative results and failed experiments. Authentic images can still form a misleading selected subset. Missing results are not necessarily negative. The collection includes an explicitly hypothetical complete-archive exercise; its invented numbers are not attributed to real authors.

## Authors may browse; evaluated models use fixed packets

Authors may consult publishers, PubMed, primary papers, notices and syllabi. Evaluated models receive only frozen questions, options and materials—not reference answers, editorial judgments, rubrics or review records. The question interface supports only `fixed_packet`, supplies an empty tool list and records attempted model tool calls as operational errors.

These checks cover client requests and responses, not a remote provider's internal retrieval. Stronger offline guarantees require auditable local inference and network isolation. OS-isolated evaluation of agent-generated code has not been run; a prompt instruction is not network isolation.

## Propose new questions and assess their quality

The private collection also contains 12 research proposals, three per domain, with competing hypotheses, discriminating experiments, informative negative outcomes, reference designs and preliminary AI ratings. A new proposal is not necessarily a world-first idea. An author's inclusion in a textbook does not make every paper by that author equally reliable.

`templates/question-quality-rubric.json` defines six dimensions with 0–4 anchors: importance, evidence grounding, bounded novelty, testability, discrimination between explanations, and feasibility under the stated constraints. This is a proposed project rubric, not a validated scale. A valuable question can yield an informative negative result; the reference design is only one acceptable approach. Two raters first assess proposals independently with author, institution, model identity and prior scores hidden to reduce prestige and verbosity bias.

The author/reviewer team records a current-literature check for real-world novelty. The evaluated model still uses only the frozen packet. Before that check is complete, novelty and total score remain `null`. The other five dimensions may produce a descriptive score out of 20, which must not support a formal ranking. Even with all six scores present, the tool only checks completeness and arithmetic; it does not approve scientific conclusions.

```powershell
.\.venv\Scripts\lsrw.exe question-quality --record 'PRIVATE-QUESTION-RATING.json' --output 'NEW-QUALITY-SUMMARY.json'
```

Provide each score and rationale using the template. Report question quality separately from agent task performance; one strong question does not establish overall agent ability. Prior work absent from the frozen packet can affect real-world novelty, but should not be treated as a model hallucination simply because the model could not see it.

## What the analysis checks actually execute

`scripts/check_analysis_pipelines.py` runs seven checks on synthetic data with a fixed seed: ORA enrichment, paired CCA, donor aggregation with exploratory differential expression, covariate-adjusted quantitative-trait association, Scanpy single-cell analysis, diffusion pseudotime and downstream VCF filtering. Reports record software versions, output hashes, acceptance criteria and limitations. The single-cell check removes a low-quality cell and verifies label alignment.

Run it in a scientific environment with `.[analysis]` installed:

```powershell
python -X utf8 scripts/check_analysis_pipelines.py --output 'NEW-PRIVATE-OUTPUT-DIRECTORY'
```

The current checks used an existing local scientific environment, recorded in the private `pipeline-checks/2026-10-03-v2/pipeline-report.json`. They are not full GATK, DESeq2 or MOFA runs, real-cohort validation, or evaluation of autonomously generated agent programs. Full WGS, external real-data validation, GWAS with more complex batch/relatedness structure, and isolated code execution remain separate work. A successful exit means only that the seven implemented checks passed.

## DeepSeek collaboration records

DeepSeek Harness used the installed program's official command interface and existing signed-in account to draft bioinformatics candidates, inventory concepts and review source code. Original output is preserved separately from scientific corrections and code-review adjudication. Another model's opinion is not automatically accepted. Detected errors included incorrect null-hypothesis interpretation, misattributed experiments and overgeneralized experimental-unit claims. AI review is not expert approval.
