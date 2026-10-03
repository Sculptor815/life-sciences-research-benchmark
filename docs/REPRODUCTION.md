# Raw-data and figure reproduction

The goal is to help a researcher obtain a scientifically defensible result from original measurements, not merely execute software or imitate a plot. This track is separate from the three open-response question types. A written analysis plan cannot substitute for a completed raw-to-result run.

## Article eligibility

Before admitting a paper, verify its exact version, original claim, correction/retraction history and substantive post-publication concerns. Reputation is insufficient. Require accessible raw measurements, a complete sample map, an interpretable design, legally usable data, an author figure with traceable numerical quantities, and enough method/software provenance to reconstruct the result. Reject or explicitly defer cases with inaccessible controlled data, irreconcilable identities, unidentifiable complete confounding, missing essential measurements or unclear rights.

A processed count matrix, normalized expression table or source-data spreadsheet may support a downstream analysis task, but it must not be called raw sequencing or raw acquisition data. A paper with a documented correction can be useful when both the error and corrected result are auditable; correction is not itself evidence of fraud. Papers selected to test integrity concerns must be labeled separately from reference reproductions.

## Freeze the task before evaluation

Record the paper DOI/version, target figure panels, exact scientific claims, raw accessions, file sizes and hashes, sample sheet, reference genome/annotation/database versions, software lock, commands, random seeds and resource limits. Keep author outputs, answer keys and numerical target values outside the candidate environment. Authors may download and verify materials in advance; evaluated agents cannot browse.

Define each numerical comparison before seeing the candidate result. Depending on the claim, compare counts, effect sizes, uncertainty intervals, trajectory/event timing, rank or cluster stability, classifier performance or a specified statistical contrast. Tolerances must reflect rounding, deterministic versus stochastic variation, and scientific relevance. Do not choose a permissive tolerance after observing a discrepancy. Explain explicitly when a dataset slice cannot reproduce the original cohort-level conclusion.

## Deliverables and scientific checks

The submission must include executable code, a software/environment record, an execution log, derived numerical tables and regenerated figures. Plotting code must consume the submitted tables. Preserve failed runs, exclusions, QC reports and provenance rather than selecting only attractive outputs. Check sample identity, alignment between modalities, independent experimental units, batch/condition relationships, information leakage, multiplicity and the claimed inference.

For neural circuits, preserve animal/session/trial identity, acquisition timing, spike or voltage preprocessing, stimulus/behavior alignment and perturbation controls. Cells, frames and trials are nested measurements, not automatically independent animals. A reproduced activity correlation does not establish circuit necessity. For sequencing, retain raw-read QC, contamination assessment, reference mapping and quantification before downstream inference.

Run both a faithful reconstruction and justified sensitivity/correction analyses. An artifact can be exactly reproducible; execution success does not make the biological interpretation correct. Report what changed, which conclusion survives, which depends on processing, and what the user should investigate next.

## Implemented numerical audit

`lsrw reproduction-check --spec PRIVATE/spec.json --submission PRIVATE/submission.json --root PRIVATE/artifacts --output PRIVATE/new-check.json` checks:

- A frozen specification hash and genuine raw-input declarations with accession, rights and file hashes.
- Code, environment, execution-log, figure and derived-table artifacts and their hashes.
- Complete reporting of every prespecified numerical target, finite values and nonnegative tolerances.
- Absolute/relative agreement using the larger declared tolerance.

It deliberately returns `agent_capability_verified: false`. The checker does not execute the code, authenticate an execution log, inspect plot-to-table provenance, prove that a declared file is genuinely raw, or verify network isolation. Those require independent curator execution and source inspection. It cannot turn self-reported matching numbers into agent capability evidence.

## Candidate sources and remaining work

The [profDGE48 author repository](https://github.com/bartongroup/profDGE48) is a candidate for RNA-seq replication and replicate-number/effect-estimation tasks. [apeglmPaper](https://github.com/mikelove/apeglmPaper) supplies author analysis organization for effect-size estimation. Repository existence is not proof that every dependency, raw input or published panel has been reproduced.

The existing seven analysis checks are small synthetic author-side workflows. They remain useful software checks and do not establish real-data or agent performance. The current source-selection and access-attempt records are kept privately with raw-versus-derived distinctions. The latest ENA/DANDI metadata request failed in the sandbox; its escalated retry did not receive approval before cancellation. No genuine raw-data download or analysis was completed in that attempt. No full-paper raw-data reproduction is claimed by this release. A formal offline execution harness, independent run audit and expert assessment remain required.
