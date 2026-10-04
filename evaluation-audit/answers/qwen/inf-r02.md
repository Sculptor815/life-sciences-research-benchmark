# Qwen3.8 Max (0902) / inf-r02

Original final answer, shared by both scoring rounds.

## Recommended next action

The most valuable next biological question is:

**For selected surface proteins measured in the same single cells as transcripts, which apparent RNA–protein discordances represent reproducible biological cell states, and which are better explained by modality-specific noise, detection limits, or staining/sequence-counting artifacts?**

The packet establishes that joint measurement is possible and that the two modalities are complementary but have different noise and detection properties. It does **not** establish that apparent RNA–protein disagreements are real cell states, nor does it specify an optimal integrated representation. Therefore, the highest-value next step is not to interpret discordant cells as new biology, but to build a calibrated, replicated, auditable test that separates reproducible biological discordance from technical discordance.

This answer is a proposal only. No additional results are assumed, and no missing author methods are reconstructed as if reported.

---

## 1. Evidence-to-inference-to-conclusion chain

### Evidence supplied

1. **E1.** Oligonucleotide-tagged antibodies allow selected surface-protein measurements and transcript measurements to be linked to the same single cells.  
2. **E2.** The two measurements can provide complementary information.  
3. **E3.** The two measurements have different noise and detection properties.  
4. **E4.** The supplied result establishes joint measurement.  
5. **E5.** The supplied result does not specify an optimal integrated representation.  
6. **E6.** The supplied result does not establish that all apparent RNA–protein disagreements define real cell states.  
7. **E7.** No later integration algorithm or benchmark result is supplied.

### Inferences

- From **E1**, the data structure contains paired RNA and surface-protein information per cell.  
- From **E2** and **E3**, RNA and surface-protein channels cannot be treated as interchangeable measurements of the same quantity. They may disagree because of biology, but also because of different sensitivities, backgrounds, dropouts, antibody-binding variation, barcode-counting variation, or normalization artifacts.  
- From **E4**, the key achieved result is feasibility of joint measurement, not interpretation of discordance.  
- From **E5** and **E7**, there is no supplied basis for declaring one integration or representation optimal.  
- From **E6**, apparent RNA–protein mismatch cannot automatically be treated as evidence of a distinct biological cell state.

### Conclusion

The strongest justified current conclusion is:

> Joint single-cell RNA and selected surface-protein measurement is feasible and potentially informative, but the biological reality of apparent RNA–protein discordant states is unresolved. The next study should test whether discordant patterns are reproducible beyond calibrated technical noise and independent of batch, detection limits, and quality-control artifacts.

---

## 2. Unresolved biological question

### Primary question

**Do apparent single-cell RNA–surface-protein discordances identify reproducible biological cell states, or are they mainly consequences of modality-specific measurement error?**

### Operational definition of terms

- **Surface-protein measurement:** an oligonucleotide-tagged antibody readout corresponding to a selected surface protein or epitope.  
- **Transcript measurement:** an RNA measurement, including, where available, the transcript corresponding to the surface protein.  
- **Discordance:** a cell or population in which RNA and surface-protein measurements for a target or set of targets are inconsistent more often than expected from calibrated measurement error. Examples include RNA-high/protein-low or RNA-low/protein-high patterns.  
- **Real cell state:** a reproducible multivariate pattern that is not explained by measured technical covariates and is stable or recurrent across independent biological units, calibrated thresholds, and reasonable representations.  
- **Technical discordance:** apparent RNA–protein mismatch caused by dropout, background binding, barcode noise, batch effects, staining artifacts, doublets, low-count uncertainty, or normalization choices.

### Why this is the most valuable question

The packet explicitly states that joint measurement is established but that it is not established whether apparent disagreements define real cell states. Therefore, biological interpretation of discordant cells is currently premature. The question is also consequential: if discordances are mostly technical, integrated analysis should down-weight or filter them; if some are biological, they may define regulatory, activation, differentiation, trafficking, or disease-relevant states invisible to either modality alone.

---

## 3. Competing mechanisms and discriminating predictions

The same observed RNA–protein discordance can arise through several non-mutually exclusive mechanisms.

| Competing mechanism | Description | Discriminating predictions |
|---|---|---|
| **M1. True biological discordance** | The cell state has genuine mismatch between transcript abundance and surface-protein abundance because of post-transcriptional regulation, translation control, protein stability, surface trafficking, internalization, or activation-dependent display. | Discordant pattern is reproducible across independent biological units; not confined to low-count or low-quality cells; not explained by batch or antibody lot; may be associated with independent markers or experimental condition; persists across calibrated thresholds and reasonable representations. |
| **M2. Technical measurement noise** | Discordance arises from RNA dropout, low transcript capture, antibody background, nonspecific binding, oligo-tag counting noise, sequencing-depth differences, or normalization artifacts. | Discordance concentrates near detection thresholds; correlates with low RNA counts, low protein counts, high background, total-count metrics, batch, or antibody lot; disappears after stricter QC or better calibration; appears in negative-control or unused-barcode channels; fails to replicate across biological units. |
| **M3. Transient kinetic transition** | Cells are moving between states; RNA changes before surface protein appears or protein persists after RNA declines. Discordance is real but may be continuous rather than discrete. | Discordant cells form a continuum or ordered gradient rather than isolated clusters; RNA and protein levels show consistent phase ordering; condition or time shifts the distribution; not necessarily stable as a discrete cluster; may be sensitive to timing of sampling. |
| **M4. Epitope/accessibility or antibody artifact** | The surface protein is present but the antibody epitope is masked, altered, internalized, shed, or otherwise inaccessible; or the antibody has clone/lot-specific off-target binding. | Discordance is antibody-clone, lot, staining-condition, or pre-treatment dependent; not reproduced by an independent surface-protein measurement if available; localized to one antibody target rather than a coordinated multivariate pattern. |
| **M5. Representation/integration artifact** | Discordance appears because one modality dominates an integrated embedding, or because normalization forces artificial separation. | Candidate discordant states appear only under one integration choice; disappear when modality weights, thresholds, or representations are changed; strongly associated with embedding parameters rather than biological replicates. |

### Key predictions that discriminate mechanisms

1. **Replicate consistency**  
   - Biological: reproducible across independent biological units.  
   - Technical: stochastic or batch-specific.

2. **Dependence on detection thresholds**  
   - Biological: robust to calibrated threshold variation.  
   - Technical: concentrated at or below detection limits.

3. **Association with QC metrics**  
   - Biological: weak association with total RNA, total antibody signal, background, doublet score, or viability metrics.  
   - Technical: strong association with poor QC or low-count cells.

4. **Negative-control behavior**  
   - Biological: absent from negative-control or unused-barcode channels.  
   - Technical: mirrored by negative controls, non-targeting reagents, or unused barcodes.

5. **Representation robustness**  
   - Biological: detectable under multiple reasonable representations.  
   - Integration artifact: appears only under one representation.

6. **Temporal or condition dependence**  
   - Kinetic: ordered RNA-before-protein or protein-after-RNA gradients.  
   - Stable biological state: discrete or recurrent pattern not necessarily tied to a temporal gradient.

---

## 4. Proposed research plan

This section is a **proposal**, not a report of performed experiments. Because the packet supplies no antibody panel, cell type, staining protocol, sequencing depth, normalization method, clustering method, replicate structure, or benchmark, all operational parameters below must be treated as assumptions to be preregistered or calibrated before biological inference.

### 4.0 Overall design logic

The plan has five linked goals:

1. **Calibrate** the RNA and surface-protein measurements separately.  
2. **Estimate** the rate of discordance expected from measurement error alone.  
3. **Identify** candidate discordant patterns without looking at biological condition labels.  
4. **Validate** candidate patterns across independent biological units and representations.  
5. **Discriminate** biological discordance from technical or kinetic alternatives.

---

## 5. Prerequisites and assumptions

### Required prerequisites

The plan assumes, but does not claim, the following:

1. The joint assay produces per-cell linked transcript measurements and oligonucleotide-tagged antibody measurements.  
2. Antibody-derived oligonucleotide barcodes can be distinguished from transcript-derived reads or counts.  
3. The selected surface-protein panel includes targets whose transcripts are measured, or at least targets whose biological relevance can be evaluated independently from the transcriptome.  
4. Sufficient cells can be obtained to detect candidate populations of interest.  
5. Independent biological replicates are available.  
6. Raw per-cell measurements, not only summary plots, can be preserved for audit.

### Unreported parameters that must be specified

The packet does not supply the following. They should be documented before analysis:

- Cell source, system, and biological condition.  
- Antibody clones, concentrations, staining conditions, and lot numbers.  
- Oligonucleotide barcode design and collision/error controls.  
- Transcript panel or whole-transcriptome measurement scope.  
- Sequencing depth or count acquisition parameters.  
- Cell-calling or cell-identification method.  
- Normalization and background-correction method.  
- Clustering or state-definition parameters.  
- Number of biological replicates and cells per replicate.  
- Thresholds for positive/negative calls and for declaring discordance.

If these cannot be specified or calibrated, the strongest conclusion remains limited to feasibility.

---

## 6. Ordered proposed protocol

### Step 1. Preregister the question and decision rules

Before examining biological condition labels or candidate cell states, record:

1. The list of surface-protein targets and corresponding transcripts, where applicable.  
2. Which targets are expected to be concordant, if any such prior expectation exists.  
3. The minimum candidate discordant-cell frequency to be treated as biologically interpretable.  
4. Calibration pass/fail criteria.  
5. Quality-control thresholds.  
6. Representation comparison criteria.  
7. Replication criteria.  
8. Stop rules.  
9. Analysis code version and random seeds.

This step prevents post hoc selection of discordant clusters as “biological.”

---

### Step 2. Perform calibration separately from biological discovery

Calibration should use pilot material or a portion of the data reserved from discovery inference.

#### 2.1 Estimate antibody-channel background

For each antibody or oligo-tagged reagent, estimate background using whichever of the following are available and appropriate:

- Cells not stained with that antibody.  
- Non-targeting oligonucleotide-tagged control reagent.  
- Unused antibody barcodes.  
- Cell-free or empty-well/droplet measurements, if applicable.  
- Known negative cell population, if available.

Do not assume any of these controls were used in the supplied result; they are proposed for future validation.

#### 2.2 Estimate RNA-channel detection limits

Estimate RNA detection behavior using:

- Low-expression genes.  
- Negative-control transcripts, if available.  
- Empty-well/droplet background, if applicable.  
- Positive and negative populations for transcripts expected to be well separated, if available.

The packet does not specify whether such controls exist. If absent, uncertainty must be stated explicitly.

#### 2.3 Titrate or validate antibody reagents

Where possible, choose antibody conditions that separate true signal from background. Record:

- Signal-to-background estimate for each surface-protein reagent.  
- Overlap between negative and positive distributions.  
- Evidence of nonspecific binding.  
- Evidence of barcode-specific background.

Markers that cannot be calibrated should be flagged as unreliable and excluded from biological interpretation or treated as exploratory only.

#### 2.4 Define per-target reliability metrics

For each surface-protein target, estimate:

- Protein-channel false-positive tendency.  
- Protein-channel false-negative tendency.  
- RNA-channel dropout or false-negative tendency, if corresponding transcript is measured.  
- Expected rate of apparent RNA–protein mismatch under a technical-noise model.

These metrics become the baseline for judging whether observed discordance exceeds technical expectation.

---

### Step 3. Define independent experimental units

A crucial design point is that **cells are not independent biological replicates**. Cells are nested within samples, donors, cultures, animals, production batches, or other biological units.

#### Independent unit

The independent unit for biological inference should be the biological source, for example:

- Donor.  
- Animal.  
- Independent culture.  
- Independent differentiation or treatment batch.  
- Independent clinical sample.

#### Nested structure

The data structure should be modeled as:

> cells within samples within batches/conditions.

This avoids pseudoreplication, where thousands of cells from one sample are treated as thousands of independent biological observations.

---

### Step 4. Determine sample size and cell-number targets

Because the packet supplies no rates or frequencies, exact numbers cannot be prescribed. Instead, set them during calibration.

A minimum logic is:

1. Choose a minimum biologically meaningful discordant-cell frequency, `f_min`.  
2. Choose the desired probability of observing at least one such cell in a sample.  
3. Calculate required cells per biological unit approximately as:

\[
N \geq \frac{\ln(1 - \text{desired probability})}{\ln(1 - f_{\min})}
\]

For reproducible validation, candidate cells should be observed in multiple independent biological units, not merely in one unit.

If the expected candidate population is too rare for the available cell number, the study should be described as underpowered rather than interpreted as negative evidence.

---

### Step 5. Allocation, blocking, and blinding

Where multiple conditions or groups exist:

#### Randomization and blocking

1. Process biological units from different conditions in a balanced order.  
2. Avoid processing all samples from one condition in one batch.  
3. Include a common reference sample in multiple batches if feasible.  
4. Record antibody lot, staining batch, library batch, and sequencing batch.

#### Blinding

1. Replace biological condition labels with coded identifiers before exploratory clustering or discordance calling.  
2. Define candidate discordant states while blinded to condition.  
3. Unblind only after candidate states, thresholds, and validation criteria are frozen.  
4. If QC requires partial unblinding, document exactly what was seen and how decisions were made.

Blinding is especially important because RNA–protein discordant clusters can be visually compelling and easy to overinterpret.

---

### Step 6. Controls

The following controls are proposed. The packet does not state that any were performed.

| Control | Purpose | Interpretation use |
|---|---|---|
| No-antibody or non-targeting oligo control | Estimate antibody-tag background | Set protein-channel background and false-positive expectations |
| Unused barcode control | Estimate barcode bleeding, index noise, or ambient tag signal | Detect artificial antibody-barcode signal |
| Single-modality control | Detect cross-contamination between RNA and antibody-tag measurements | Rule out modality cross-talk |
| Known negative/positive biological population, if available | Validate target-specific detection | Sanity check for concordant markers |
| Common reference sample | Monitor batch-to-batch technical variation | Normalize or flag batch artifacts |
| Technical replicate aliquot | Estimate technical repeatability | Separate technical from biological variance |
| Doublet/multiplet control, if available | Identify cells with mixed signals | Exclude artificial RNA–protein mismatches caused by cell doublets |
| Expected-concordant markers | Estimate baseline RNA–protein agreement | Calibrate expected technical discordance |

If no controls are available, the study can still describe candidate discordance, but the conclusion must remain highly tentative.

---

### Step 7. Measurements to collect

For each cell, preserve:

1. Transcript counts or expression values.  
2. Antibody oligo-tag counts for each selected surface protein.  
3. Cell identifier.  
4. Biological unit identifier.  
5. Batch identifier.  
6. Total RNA counts.  
7. Total antibody-tag counts.  
8. Fraction of antibody-tag signal attributed to each target.  
9. Background or negative-control estimates applicable to that cell’s batch.  
10. Quality-control metrics, if available.

For each sample, preserve:

1. Biological unit.  
2. Condition or group, kept blinded during discovery.  
3. Antibody panel and lot.  
4. Processing date.  
5. Sequencing or acquisition batch.  
6. Number of cells recovered.  
7. QC pass/fail rates.

All raw and processed files should be versioned.

---

## 8. Analysis plan

The analysis should be preregistered and auditable. It should not assume a single optimal integration method because none is supplied.

### 8.1 Quality control

Define and apply QC rules before biological interpretation.

Possible QC dimensions include:

- Minimum total RNA counts.  
- Maximum total RNA counts, to reduce doublet influence.  
- Minimum total antibody-tag counts.  
- Maximum antibody-tag background fraction.  
- Doublet/multiplet score, if available.  
- Viability or stress metrics, if available.  
- Excessive unused-barcode signal.  
- Extreme batch-specific outliers.

Cells failing QC should be excluded or analyzed separately. The fraction excluded and the reason should be reported.

Important: if discordant cells are disproportionately excluded by QC, that is evidence against treating them as robust biological states.

---

### 8.2 Modality-specific normalization and calibration

Normalize RNA and protein channels separately before integration.

For each modality:

1. Correct for sequencing or counting depth where appropriate.  
2. Estimate background from calibration controls.  
3. Convert raw counts to calibrated evidence of presence or abundance.  
4. Preserve uncertainty rather than forcing binary calls.

The packet states that the modalities have different noise properties, so treating them as directly comparable raw counts would be inappropriate.

---

### 8.3 Probabilistic RNA–protein discordance calls

For each target where both RNA and surface-protein measurements exist, classify each cell not as a hard binary pair but as a probability distribution over four states:

1. RNA present / protein present.  
2. RNA present / protein absent or low.  
3. RNA absent or low / protein present.  
4. RNA absent or low / protein absent or low.

The discordant probability for a cell-target pair is the summed probability of states 2 and 3.

This approach avoids overinterpreting cells near detection thresholds.

---

### 8.4 Compare multiple representations

Because the packet does not specify an optimal integrated representation, compare several predefined representations rather than selecting one informally.

Candidate representations include:

1. **RNA-only representation**  
   - Uses transcript measurements only.  
   - Tests whether candidate states are visible without protein information.

2. **Protein-only representation**  
   - Uses surface-protein measurements only.  
   - Tests whether candidate states are visible without RNA information.

3. **Calibrated joint representation**  
   - Combines RNA and protein features after separate normalization and weighting.  
   - Weights can be based on estimated reliability from calibration.

4. **Discordance-residual representation**  
   - Models expected protein level from RNA level, or expected joint distribution under technical noise.  
   - Represents cells by residuals or posterior probability of discordance.

5. **Consensus or late-integration representation**  
   - Builds separate neighborhoods or graphs for each modality, then combines them.  
   - Reduces risk that one modality dominates.

The goal is not to declare one method universally optimal. The goal is to identify candidate states that are robust to reasonable representation choices.

---

### 8.5 Candidate discordant-state discovery

Within each representation:

1. Identify cell groupings using a predefined, documented method.  
2. Annotate groups by RNA and protein profiles.  
3. Flag groups enriched for discordant posterior probability.  
4. Record group size, replicate composition, batch composition, and QC associations.  
5. Do not use condition labels at this stage if blinding is feasible.

Candidate states should be defined before unblinding.

---

### 8.6 Validation across independent biological units

A candidate discordant state should be evaluated at the level of independent biological units, not merely at the level of individual cells.

For each candidate state, compute:

1. Fraction of cells per biological unit assigned to the state.  
2. Detection rate across independent biological units.  
3. Consistency of marker pattern across units.  
4. Stability when the discovery set is split by biological unit.  
5. Stability across alternative representations.  
6. Sensitivity to QC thresholds.  
7. Sensitivity to RNA/protein positivity thresholds.

A candidate state that appears only in one biological unit should be considered unvalidated.

---

### 8.7 Statistical testing for excess discordance

The central statistical question is whether observed discordance exceeds the rate expected from calibrated measurement error.

A possible framework is:

1. Use calibration controls to estimate false-positive and false-negative rates for RNA and protein measurements.  
2. Define a technical-null model in which RNA and protein latent states are coupled except for measurement error.  
3. Compute expected discordance rates under that model.  
4. Compare observed discordance rates to expected rates.  
5. Adjust for multiple targets and multiple candidate states.  
6. Require that excess discordance remains after excluding low-quality cells.

The exact statistical model should be chosen and locked during calibration. It may be parametric or nonparametric. The packet does not supply enough information to prescribe a unique model.

---

### 8.8 Association with technical covariates

For each candidate discordant state, test association with:

- Total RNA count.  
- Total antibody-tag count.  
- Antibody background.  
- Unused-barcode signal.  
- Batch.  
- Antibody lot.  
- Sequencing or acquisition batch.  
- Doublet score.  
- Cell density or loading metrics, if available.

If the candidate state is strongly predicted by technical covariates, the most parsimonious explanation is technical artifact unless additional validation shows otherwise.

---

### 8.9 Discriminating biological, technical, and kinetic explanations

Use the following decision logic:

#### Evidence favoring biological discordance

- Candidate state is reproducible across independent biological units.  
- It exceeds calibrated technical-noise expectations.  
- It is not concentrated near detection thresholds.  
- It is not strongly associated with QC or batch.  
- It is robust to multiple representations.  
- It is absent from negative-control channels.  
- It is supported by multiple coordinated markers, if available.

#### Evidence favoring technical noise

- Candidate state disappears after stricter QC.  
- It is concentrated in low-count cells.  
- It appears in negative-control or unused-barcode channels.  
- It is batch-specific or antibody-lot-specific.  
- It fails to replicate across biological units.  
- It is highly sensitive to arbitrary threshold choices.

#### Evidence favoring kinetic transition

- Discordant cells form a continuous RNA-to-protein gradient.  
- The apparent direction is consistent with RNA changing before protein or protein persisting after RNA decreases.  
- The state is not discrete but shifts with condition or time.  
- It may be reproducible as a trajectory rather than as a fixed cluster.

#### Evidence favoring epitope or antibody artifact

- Discordance is localized to one antibody target.  
- It changes with antibody clone, lot, or staining condition.  
- It is not reproduced by an independent measurement of the same surface protein, if such measurement is available.  
- It lacks coordinated RNA or protein structure.

---

## 9. Stop rules

Stop rules are essential to prevent overinterpretation.

### Stop biological interpretation if:

1. Calibration fails to separate background from true signal for key targets.  
2. Discordant cells are overwhelmingly low-count or QC-failing cells.  
3. Candidate discordant states appear only in one biological unit.  
4. Candidate states are strongly associated with batch, antibody lot, or unused-barcode signal.  
5. Candidate states appear only under one arbitrary representation and vanish under minor parameter changes.  
6. Negative-control channels produce similar discordant patterns.  
7. Condition is completely confounded with batch.  
8. The number of cells is too low to detect the prespecified minimum candidate frequency with adequate probability.

In these cases, the correct conclusion is not necessarily “no biological discordance exists.” The correct conclusion is that the current evidence is insufficient.

### Proceed to biological interpretation only if:

1. Calibration passes.  
2. Candidate discordance exceeds technical expectation.  
3. Candidate state is detected in multiple independent biological units.  
4. Candidate state is not primarily explained by QC, batch, or detection threshold.  
5. Candidate state is robust to reasonable representation changes.  
6. Negative controls do not reproduce the candidate state.

---

## 10. Troubleshooting

| Problem | Likely issue | Proposed action |
|---|---|---|
| Many discordant cells near thresholds | Detection-limit artifact | Use probabilistic calls; increase counts or cells; widen uncertainty; avoid hard biological claims |
| Discordance only for one target | Antibody or epitope artifact | Revalidate antibody; test alternate clone or condition; exclude target if unresolved |
| Discordance associated with low RNA counts | RNA dropout | Improve RNA capture or sequencing depth; restrict analysis to cells above calibrated threshold |
| Discordance associated with high antibody background | Nonspecific binding or tag noise | Titrate antibody; improve blocking/washing if possible; use negative controls; exclude unreliable marker |
| Candidate state appears in one batch | Batch artifact | Rebalance design; include common reference; do not interpret biologically |
| Candidate state disappears when thresholds change | Instability | Treat as ambiguous; require orthogonal validation |
| Candidate state is rare | Underpowered | Increase biological units and cells; enrich population if possible; otherwise report as exploratory |
| RNA and protein measurements seem cross-contaminated | Modality cross-talk | Use single-modality controls; revise barcode demultiplexing; exclude affected targets |
| Doublets are suspected | Mixed-cell artifact | Apply doublet detection; reduce cell loading if possible; exclude suspected doublets |
| No negative controls are available | Calibration uncertainty | State uncertainty explicitly; avoid strong biological claims; seek orthogonal validation |

---

## 11. Conditional interpretation of outcomes

### 11.1 Positive outcome

A positive outcome would occur if:

- A discordant RNA–protein pattern is detected.  
- It exceeds the discordance expected from calibrated technical noise.  
- It is observed in multiple independent biological units.  
- It is not primarily associated with low counts, batch, antibody lot, or QC failure.  
- It is robust across reasonable representations.  
- Negative controls do not reproduce it.

#### Strongest justified conclusion from a positive outcome

> The data support the existence of at least one reproducible RNA–protein discordant cell state for the tested targets under the tested conditions.

This conclusion should still be limited:

- It does not prove that all discordant cells represent real states.  
- It does not by itself identify the molecular mechanism.  
- It does not prove causality.  
- It does not establish that the state is functionally important.  
- If no perturbation or orthogonal validation is performed, the conclusion remains associative.

If the candidate state is also condition-associated and survives batch-adjusted analysis, one may additionally conclude that it is associated with that condition, provided condition and batch are not confounded.

---

### 11.2 Negative outcome

A negative outcome would occur if:

- No discordant pattern exceeds calibrated technical expectations.  
- Apparent discordant cells are mostly low-quality or low-count cells.  
- Candidate states fail to replicate across biological units.  
- Discordance is explained by batch, background, or detection thresholds.

#### Strongest justified conclusion from a negative outcome

> Within the limits of the tested panel, cell number, and assay sensitivity, the observed RNA–protein disagreements do not provide sufficient evidence for reproducible biological cell states.

This does **not** prove that biological discordance is absent. It only means the current experiment cannot distinguish it from technical noise.

The appropriate next actions would be to improve calibration, increase independent biological units, increase cell number, reduce technical noise, or obtain orthogonal validation.

---

### 11.3 Ambiguous outcome

An ambiguous outcome is likely. Examples include:

- A candidate state replicates in some but not all biological units.  
- Discordance is reproducible but associated with a batch or antibody lot.  
- A state is visible in one representation but not another.  
- Discordant cells are rare and near detection thresholds.  
- The pattern resembles a biological transition but cannot be separated from dropout.  
- Condition is confounded with processing batch.

#### Strongest justified conclusion from an ambiguous outcome

> A candidate RNA–protein discordant pattern exists, but the available evidence cannot distinguish biological discordance from technical or kinetic artifacts.

In this case, the correct action is not to declare a new cell state. The correct action is to treat the pattern as a hypothesis requiring additional validation, such as independent biological cohorts, improved controls, orthogonal measurement, temporal sampling, or perturbation.

---

## 12. Strongest justified conclusion from the supplied packet alone

Using only the supplied packet, the strongest justified conclusion is:

> Oligonucleotide-tagged antibodies can link selected surface-protein and transcript measurements in the same single cells, and the two modalities may be complementary. However, because the modalities have different noise and detection properties, and because no integrated representation or validation of discordant states is supplied, one cannot conclude that apparent RNA–protein disagreements define real cell states.

No specific biological mechanism, cell type, marker, integration algorithm, or discordant population can be inferred from the packet.

---

## 13. Consequential uncertainties and what would change the recommendation

The most consequential uncertainties are:

1. **Calibration uncertainty**  
   If negative and positive signal distributions cannot be separated, discordance cannot be interpreted.  
   *What would change the plan:* better controls, antibody validation, or orthogonal protein measurement.

2. **Replication uncertainty**  
   If only one biological unit is available, no discordant state can be considered validated.  
   *What would change the plan:* independent biological replicates or independent cohorts.

3. **Representation uncertainty**  
   Because no optimal integration method is supplied, candidate states may be representation-dependent.  
   *What would change the plan:* a supplied benchmark, ground-truth labels, or validated integration method.

4. **Rare-state uncertainty**  
   If discordant states are rare, they may be indistinguishable from noise without very large cell numbers.  
   *What would change the plan:* enrichment, larger cell numbers, or targeted assay.

5. **Mechanism uncertainty**  
   Even validated discordance does not immediately reveal whether the cause is post-transcriptional regulation, protein trafficking, epitope masking, or another process.  
   *What would change the plan:* perturbation, time-course sampling, or orthogonal surface-protein measurement.

---

## 14. Alternatives and limits

### Alternative next questions

Depending on future data, alternative questions may become more valuable:

1. **Which integration representation best preserves known biology?**  
   This would require ground truth or benchmark data, which the packet does not supply.

2. **Which surface proteins add the most information beyond RNA?**  
   This is useful once measurement reliability is established.

3. **Which RNA–protein concordant markers are most robust for cell-type annotation?**  
   This may be more reliable if discordance proves too noisy.

4. **Do specific perturbations shift RNA–protein relationships?**  
   This would be powerful but requires perturbation experiments not described in the packet.

### Limits of the current proposal

- The packet does not identify a biological system.  
- It does not specify antibodies, targets, or transcripts.  
- It does not provide raw data, controls, or benchmark results.  
- It does not establish antibody specificity.  
- It does not establish sequencing depth or cell number.  
- It does not provide an optimal integration algorithm.  
- It does not prove that any discordant population is real.

Therefore, all procedural details above are proposed, not reported, and all biological conclusions are conditional on future validation.
