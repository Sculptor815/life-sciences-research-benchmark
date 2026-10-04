# GPT-5.6 Terra / inf-r02

Original final answer, shared by both scoring rounds.

# Proposed next biological question

**Within a defined biological cell population, do apparent disagreements between a surface-protein measurement and its cognate transcript represent reproducible biology—particularly temporal RNA-to-protein lag, post-transcriptional regulation, or surface trafficking—or are they primarily consequences of the distinct measurement and detection properties of the RNA and oligonucleotide-tagged-antibody assays?**

This is the most valuable next question because the packet establishes that the two modalities can be measured in the same cells, but explicitly does **not** establish that apparent RNA–protein disagreements are real cell states. Before optimizing a joint representation or assigning biological meaning to discordant cells, the field needs evidence that a given discordance is reproducible, assay-robust, and mechanistically interpretable.

---

# Evidence → inference → conclusion chain

## Reported evidence from the supplied packet

| Evidence location | Reported evidence |
|---|---|
| E1 | “Oligonucleotide-tagged antibodies allow selected surface-protein measurements and transcript measurements to be linked to the same single cells.” |
| E2 | “The two measurements can provide complementary information and have different noise and detection properties.” |
| E3 | “The supplied result establishes joint measurement, but does not specify an optimal integrated representation or establish that all apparent RNA-protein disagreements define real cell states.” |
| E4 | “No later integration algorithm or benchmark result is supplied.” |

## Inferences justified by that evidence

1. **Within-cell comparison is feasible** (from E1), so it is possible to ask whether RNA and surface-protein signals disagree in individual cells.
2. **A raw disagreement is not self-validating** (from E2). RNA and antibody-tag counts can differ because of their distinct detection, sampling, and noise properties.
3. **Biological interpretation remains unresolved** (from E3). The packet does not justify treating every RNA-high/protein-low or RNA-low/protein-high cell as a discrete cell state.
4. **No particular integration algorithm should be assumed to solve this problem** (from E3–E4). The primary analysis should therefore use assay-aware, interpretable comparisons rather than rely on an unspecified “optimal” joint embedding.

## Strongest current conclusion

The packet supports joint single-cell RNA and selected surface-protein measurement, but **does not yet support the claim that RNA–protein discordance defines biology rather than measurement behavior**. The appropriate next study is a controlled validation-and-mechanism experiment.

---

# Competing mechanisms and discriminating predictions

The experiment should not treat “discordance” as one mechanism. At least four explanations are plausible and may coexist.

| Mechanism | Interpretation | Distinct prediction |
|---|---|---|
| **M1. Technical/detection discordance** | RNA and antibody-tag measurements differ because of assay sensitivity, capture, sequencing depth, antibody background, epitope accessibility, ambient material, batch, or analytical thresholding. | Discordance is unstable across independent samples, antibody clones, technical runs, or sequencing depth; it is enriched near detection limits; it tracks quality-control variables or batch rather than biology. |
| **M2. RNA-to-protein kinetic lag** | Transcript abundance changes before surface protein changes because RNA production/decay and protein synthesis/turnover occur on different timescales. | During stimulus onset, RNA-high/surface-protein-low cells appear before protein induction. During washout or transcriptional decline, RNA-low/surface-protein-high cells appear. At the same RNA level, protein depends on prior stimulation history. |
| **M3. Persistent post-transcriptional regulation** | Translation efficiency, protein degradation, or other regulation changes protein abundance without a proportional RNA change. | Discordance persists at matched time points and in independent biological replicates, including under approximately steady conditions. An intervention that changes translation or protein turnover changes protein more than RNA. |
| **M4. Surface-specific regulation or epitope effects** | The antibody reports surface-accessible antigen, not necessarily total cellular protein. Internalization, trafficking, cleavage, shedding, or epitope masking can alter surface signal without proportionate RNA or total-protein change. | Surface signal changes while total protein is stable or changes differently. A second antibody clone or non-antibody total-protein assay may disagree with the original surface assay if epitope accessibility is responsible. |

## Important nonexclusive alternative: cell-population mixture

An apparent discordance can also result from comparing different cell types, activation stages, cell sizes, or cell-cycle states. This is biological heterogeneity, but it is not necessarily a special RNA–protein regulatory state. The primary comparison should therefore be made **within a pre-specified, biologically coherent cell population**, not across a mixed sample.

---

# Proposed research plan

## Overview and decision framework

The study should proceed in four ordered phases:

1. **Specify targets, biological context, and estimands.**
2. **Calibrate both modalities and demonstrate that candidate discordance exceeds assay behavior.**
3. **Establish reproducibility in independent biological units.**
4. **Use a balanced perturbation and time-course design to distinguish kinetic lag, persistent post-transcriptional regulation, and surface-specific regulation.**

A candidate discordance should not be called biological unless it meets pre-specified reproducibility and orthogonal-validation criteria.

---

## Phase 0 — Pre-study specification

### 0.1 Define the biological system

**Proposed requirement:** select one biologically defined population in which a surface antigen and its cognate transcript can both be detected sufficiently often for quantitative comparison.

Examples cannot be specified from the packet because it provides no organism, tissue, cell type, antigen panel, or perturbation context. The chosen system should be documented before data collection.

### 0.2 Define the primary target pairs

For each target, document:

- antibody identity and the antigen/epitope it recognizes;
- corresponding transcript identifier;
- whether the transcript could encode multiple protein isoforms;
- whether the antibody measures a surface-exposed epitope only;
- expected background and detection range from calibration;
- availability of an independent antibody clone, blocking reagent, or orthogonal protein assay.

**Critical assumption:** the detected transcript is meaningfully related to the protein species recognized by the antibody. This cannot be assumed when isoforms, cleavage products, or cross-reactive epitopes are possible.

### 0.3 Pre-specify the estimands

The main estimand should not be a joint embedding. It should be, for each target pair and within each defined cell population:

1. the association between transcript and surface-protein measurement;
2. the frequency and magnitude of cells with protein higher or lower than expected from their RNA level;
3. the reproducibility of that residual signal across independent biological units;
4. the change in that residual signal across time and perturbation conditions.

### 0.4 Define independent units

**Independent biological units are not individual cells.**

Use, as applicable:

- independent donors;
- independent animals;
- independent cultures initiated on different days;
- independent stimulation experiments.

Cells are nested observations within these units. Splitting one donor or one culture into many wells increases cell number and technical precision, but does not create independent biological replication.

### 0.5 Pre-registration and data lock

Before collecting the confirmatory dataset, record:

- target pairs;
- target cell population definition;
- exclusion criteria;
- quality-control criteria;
- planned perturbation and time points;
- primary and secondary analyses;
- criteria for classifying an outcome as supporting M1, M2, M3, or M4;
- handling of missing samples and failed runs.

The analysis team should receive coded condition and clone identities until assay QC and the primary analysis pipeline are frozen.

---

## Phase 1 — Analytical calibration

The objective is to establish what apparent discordance can be produced by the measurement system itself.

### 1.1 Antibody-tag calibration

For every antibody–oligonucleotide reagent:

1. **Perform an antibody concentration series** on the selected sample type.
   - Identify a working concentration with reproducible specific signal and acceptable background.
   - Avoid choosing concentration solely because it maximizes counts; excessively high staining can increase nonspecific signal or obscure dynamic range.

2. **Include reagent controls in every batch.**
   - no-antibody control;
   - antibody-omission control for the target;
   - nonbinding or irrelevant tagged-antibody control where available;
   - cell-free processing/library control to detect tag contamination;
   - viability and singlet assessment before single-cell capture.

3. **Validate antigen specificity where feasible.**
   - independent antibody clone recognizing a different epitope;
   - antigen-blocking or competition test;
   - comparison with an orthogonal surface-protein method such as conventional flow cytometry.

**Interpretation:** isotype or irrelevant-antibody controls assess background but do not prove target specificity. Concordance with a second clone or antigen competition is stronger evidence.

### 1.2 RNA-measurement calibration

For the transcript component:

1. Process matched aliquots independently through the joint assay workflow.
2. Assess transcript detection reproducibility and sensitivity across runs.
3. If compatible with the chosen workflow, include external RNA controls; these assess library behavior but do not establish biological RNA abundance.
4. Confirm selected transcript changes in bulk or orthogonal assays, such as targeted RT-qPCR or RNA in situ hybridization, on matched aliquots.

### 1.3 Depth and detection-limit calibration

Because E2 states that RNA and protein have different detection properties, evaluate each modality separately.

For each target pair:

- determine the fraction of cells with detectable RNA and detectable protein;
- plot detection and count distributions against RNA-library size, antibody-tag library size, viability, and run;
- computationally downsample sequencing/tag depth to test whether “discordant” classifications are depth-sensitive;
- estimate the background distribution from blank and omission controls;
- avoid interpreting zero counts as true biological absence unless calibration supports that claim.

### 1.4 Acceptance and stop rules for calibration

Thresholds should be set from the pilot calibration, not adjusted after observing the primary result. Exact numerical thresholds cannot be justified from the packet because no assay performance data are supplied.

**Stop and repeat a batch if:**

- cell-free or omission controls show substantial target-tag contamination;
- target staining is indistinguishable from background under the pre-set calibration criterion;
- one modality has a systematic run-level failure;
- a condition has major loss of viable singlets relative to its matched control;
- library complexity or detection behavior differs so strongly by condition that condition and assay failure are confounded.

**Do not stop early because an apparent biological association is statistically strong.** Continue to the planned independent validation.

---

## Phase 2 — Baseline reproducibility study

### 2.1 Balanced sample allocation

For each biological unit:

1. obtain one sample or culture;
2. mix or homogenize the starting suspension before splitting;
3. randomly allocate matched aliquots to:
   - joint single-cell assay replicate A;
   - joint single-cell assay replicate B where material permits;
   - orthogonal protein validation;
   - orthogonal RNA validation;
   - reserve material.

Randomize processing order, reagent lots where possible, library preparation position, and sequencing allocation. Every batch should contain samples from multiple conditions and biological units.

### 2.2 Blinding

- Assign coded identifiers to biological unit, condition, and antibody clone.
- Keep the randomization key with a person not performing primary analysis.
- Freeze QC decisions before unblinding.
- Do not remove “outlier” biological units after learning whether they support the hypothesis unless an objective, pre-specified technical failure criterion was met.

### 2.3 Baseline analysis objective

The baseline phase asks:

> Is there a reproducible RNA–surface-protein residual signal within the selected cell population before invoking a mechanism?

A target should advance to mechanistic testing only if the pattern is observed in independent biological units and remains after calibration-based sensitivity analyses.

---

## Phase 3 — Mechanistic perturbation and time course

### 3.1 General design

Use a perturbation capable of changing the selected transcript in the chosen biological system. The packet provides no specific system or stimulus; therefore, the stimulus must be selected and validated before the main experiment.

For each independent biological unit:

1. divide a common starting sample into matched aliquots;
2. assign aliquots randomly to:
   - unstimulated/vehicle control;
   - stimulus onset time course;
   - stimulus washout or recovery time course;
   - mechanistic perturbation arms where feasible;
3. collect cells at pre-specified early, intermediate, and late times;
4. process all time points with balanced batches and identical QC procedures.

Because the assay is destructive, cells measured at different times are not the same individual cells. Results therefore describe population trajectories, not direct observation of single-cell state transitions.

### 3.2 Time-course predictions for kinetic lag

The time course should include both **onset** and **recovery/washout** if the biology permits.

| Time-course result | Interpretation |
|---|---|
| RNA increases first, followed by delayed surface-protein increase | Supports M2, provided assay controls are satisfactory. |
| RNA declines first after washout, while surface protein remains high temporarily | Stronger support for M2 or stable protein. |
| At matched RNA abundance, protein differs according to whether cells are on the induction versus recovery branch | Supports history-dependent kinetics. |
| RNA and surface protein change simultaneously within measurement resolution | Does not support a detectable lag for that target, but does not exclude a lag faster than sampled intervals. |
| No transcript response to the selected stimulus | The experiment cannot test lag for that perturbation; it is not evidence against M2 generally. |

### 3.3 Perturbations to distinguish M3 from M4

Where biologically and ethically appropriate, add carefully calibrated intervention arms:

1. **Transcription-modulating intervention**
   - Purpose: alter target RNA production.
   - Prediction under M2: RNA changes precede protein changes.
   - Limitation: global transcriptional interventions can cause stress and broad cell-state changes.

2. **Translation or protein-turnover intervention**
   - Purpose: determine whether protein can change disproportionately to RNA.
   - Prediction under M3: protein trajectory changes substantially while transcript behavior is relatively preserved.
   - Limitation: global translation/turnover inhibitors are highly pleiotropic; viability, stress responses, and non-target effects must be monitored.

3. **Surface-trafficking or internalization intervention**
   - Purpose: distinguish total protein from surface accessibility.
   - Prediction under M4: surface-antibody signal changes more than total protein or transcript.
   - Limitation: the relevant trafficking process and suitable intervention are not specified in the packet.

4. **Orthogonal total-protein measurement**
   - On matched aliquots, measure total antigen abundance by a validated non-surface-only method, if available.
   - Surface-only change with stable total protein favors M4 over general protein synthesis/degradation.

All perturbations require matched vehicle controls, viability assessment, and evidence that the intervention achieved its intended proximal effect. Without this verification, a null result is not mechanistically informative.

---

## Phase 4 — Analysis plan

### 4.1 Preserve assay-specific information

Do not assume that an integrated latent space is correct. The packet supplies no validated integration algorithm or benchmark.

Analyze RNA and antibody-tag data as distinct measurements first, then compare them.

### 4.2 Define discordance quantitatively

Within the pre-specified cell population, model surface-protein measurement as a function of:

- transcript measurement;
- RNA and protein/tag library sizes;
- batch;
- biological unit;
- time and perturbation;
- pre-specified quality variables.

Use a count-aware or detection-aware model appropriate to the observed data. Because the packet does not provide distributions, the exact model family should be chosen during calibration and locked before confirmatory analysis.

A simple complementary analysis should also be run:

- stratify cells into matched RNA bins;
- compare protein distributions within each RNA bin across condition, time, and biological unit;
- repeat after depth downsampling.

A cell is not intrinsically “discordant” merely because one raw count is high and the other is low. The relevant quantity is protein higher or lower than expected **given RNA, measurement depth, and calibrated background**.

### 4.3 Hierarchical inference

Use models that account for nesting:

- cells nested within library;
- libraries nested within biological unit;
- biological units as the principal replication level.

Report:

- biological-unit-level effect estimates;
- confidence intervals;
- between-unit variation;
- distributional plots for each unit;
- pre-specified multiple-testing correction across target pairs.

Do not treat thousands of cells from one donor or culture as thousands of independent biological experiments.

### 4.4 Criteria for a validated biological discordance

A candidate should be considered supported only if all of the following hold:

1. it is observed in independent biological units;
2. it persists after controlling for depth, batch, and calibrated background;
3. it is not driven solely by near-zero/detection-limit observations;
4. it is detectable with an independent protein reagent or orthogonal assay when available;
5. it shows a reproducible condition or time-course pattern consistent with a biological mechanism.

---

# Troubleshooting guide

| Problem | Likely implication | Corrective action |
|---|---|---|
| Discordance disappears after depth matching or downsampling analysis | Likely M1 contribution | Increase depth only if calibration shows undersampling; otherwise do not interpret as biology. |
| One antibody clone gives a pattern but another does not | Possible epitope/accessibility or specificity issue | Perform competition/blocking, assess total protein, and avoid concluding transcript–protein regulation. |
| Low RNA detection for the target | RNA zeros may be uninformative | Improve sample handling/library quality; use orthogonal RNA assay; do not call RNA-low biological absence. |
| Strong batch association | Batch confounding | Repeat with balanced allocation; batch correction alone is insufficient. |
| Stimulus causes cell death or global stress | Mechanistic interpretation compromised | Reduce exposure, change perturbation, or treat arm as noninterpretable. |
| No transcript response to stimulus | Lag test failed operationally | Verify stimulus activity with orthogonal RNA assay; choose another perturbation rather than concluding no lag. |
| Surface protein changes but total protein does not | Favors M4 | Test internalization/trafficking and epitope accessibility before invoking translation or degradation. |

---

# Interpretation of possible outcomes

## Outcome A: reproducible temporal RNA–protein offset

**Pattern:** independent biological units show transcript induction before surface-protein induction and/or transcript decline before surface-protein decline after washout. The effect is assay-robust and remains after depth/batch analyses.

**Justified conclusion:** for that target in that biological context, RNA–surface-protein discordance is consistent with a biologically meaningful kinetic lag.

**Limit:** this does not prove that every discordant cell is a stable state, and destructive time-course data do not directly track the same cells over time.

---

## Outcome B: reproducible discordance under steady conditions, altered mainly at protein level by post-transcriptional intervention

**Pattern:** the residual protein signal is consistent across biological units and persists without a simple induction/recovery lag; protein changes disproportionately to RNA after a validated intervention affecting translation or protein turnover.

**Justified conclusion:** the data support post-transcriptional or protein-stability regulation for that target.

**Limit:** a global intervention may have indirect effects. Target-specific causality would require additional targeted perturbation or rescue experiments.

---

## Outcome C: surface signal changes without matched total-protein change

**Pattern:** surface-antibody signal differs across conditions or time, but total protein remains stable or a second epitope behaves differently.

**Justified conclusion:** the discordance is more parsimoniously explained by surface trafficking, accessibility, cleavage, shedding, or epitope behavior than by transcript-to-total-protein regulation.

**Limit:** this remains a surface-antigen conclusion unless the trafficking mechanism itself is directly measured.

---

## Outcome D: discordance is not reproducible or is explained by assay properties

**Pattern:** the discordant category changes with depth, batch, clone, or threshold; it is concentrated at detection limits; it fails independent validation.

**Justified conclusion:** there is no adequate evidence that the apparent discrepancy defines a biological cell state in the tested system.

**What cannot be concluded:** RNA and protein are not generally concordant, nor that no biological discordance exists. Only the tested apparent signal failed validation.

---

## Outcome E: reproducible discordance but mechanism remains unresolved

**Pattern:** the signal is reproducible and orthogonally supported, but no clear time ordering, intervention effect, or surface-versus-total distinction emerges.

**Justified conclusion:** a real biological RNA–surface-protein discrepancy is supported for the tested target and context, but the available evidence does not distinguish kinetic lag, translation/protein turnover, and surface regulation.

**Next step:** add a more informative perturbation or a validated total-protein/trafficking assay rather than overinterpreting the joint single-cell measurements.

---

# Key limitations and unreported parameters

The packet does not report:

- biological source, organism, or cell type;
- antibody identities, antigen targets, or clone validation;
- transcript panel, sequencing depth, or library chemistry;
- sample size, donor structure, or technical replicate structure;
- stimulation conditions or perturbations;
- any integration method or benchmark;
- observed discordant targets or effect sizes.

Therefore, no numerical sample-size target, antibody concentration, sampling interval, or assay threshold can be justified from the packet alone. Those parameters must be established in Phase 1 and documented before confirmatory data collection.

# Final recommendation

Treat RNA–surface-protein disagreement as a **testable phenotype, not a discovered cell state**. The highest-value next study is a balanced, independently replicated, calibration-first time-course experiment that asks whether specific discordances are reproducible and whether their temporal and perturbational behavior supports technical noise, kinetic lag, post-transcriptional regulation, or surface-specific regulation.
