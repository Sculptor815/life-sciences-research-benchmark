# Kimi K3 / inf-r02

Original final answer, shared by both scoring rounds.

# Recommended next biological question

**For one preselected, functionally important surface protein \(X\), does a reproducible RNA\(_X\)-high/surface-protein\(_X\)-low cell state represent a biologically real state that predicts later surface expression and function, rather than technical discordance?**

The most informative version is:

> **Are RNA-high/surface-low cells licensed precursor cells that subsequently acquire surface protein and its associated function, or are they a stable post-transcriptionally regulated state, a trafficking/turnover state, or an assay artifact?**

This is the most valuable next question because the supplied evidence establishes same-cell joint measurement, but not whether discordant measurements identify real cell states. A validated discordant state would provide a biological foundation for any later integrated representation. Without that validation, improving an integration algorithm could merely combine different forms of noise.

No RNA–protein disagreement, specific protein, cell type, stimulation, or functional result is reported in the packet. The choice of \(X\), the discordant direction, and the relevant functional assay are therefore **proposed prerequisites**, not reported findings.

---

# 1. Evidence-to-inference-to-conclusion chain

## Supplied evidence

- **E1, packet sentence 1:** “Oligonucleotide-tagged antibodies allow selected surface-protein measurements and transcript measurements to be linked to the same single cells.”
- **E2, packet sentence 2:** “The two measurements can provide complementary information and have different noise and detection properties.”
- **E3, packet sentence 3:** “The supplied result establishes joint measurement, but does not specify an optimal integrated representation or establish that all apparent RNA-protein disagreements define real cell states.”
- **E4, packet sentence 4:** “No later integration algorithm or benchmark result is supplied.”

## Inference

E1 supports same-cell comparison of RNA and surface protein. It does not establish that the two assays have equal sensitivity, quantitative scales, specificity, or temporal meaning.

E2 implies that an apparent disagreement can arise from either biology or measurement. RNA-high/surface-low could reflect delayed translation or trafficking, but also antibody failure; RNA-low/surface-high could reflect persistent protein after transcription declines, but also RNA dropout.

E3 and E4 rule out concluding that an unsupervised integrated cluster or discordant quadrant is already a validated biological state.

## Conclusion

Before developing or benchmarking a general integration representation, the next study should establish whether one recurrent discordant state is:

1. reproducible across independent biological units;
2. confirmed by orthogonal same-cell measurements;
3. temporally ordered or mechanistically interpretable; and
4. associated with a protein-relevant functional consequence.

---

# 2. Primary hypothesis and competing mechanisms

The protocol below is written for an **RNA-high/surface-low** candidate state because it offers a directly testable temporal prediction: RNA may precede surface expression. This direction is hypothetical, not reported. If the selected data instead nominate RNA-low/surface-high, the design should be mirrored rather than treating both directions as unrestricted primary hypotheses.

## Mechanism A: Transient expression precursor

RNA is produced first, followed by translation, intracellular protein and surface appearance.

**Distinct predictions**

- After a synchronizing biological stimulus, RNA increases before total and surface protein.
- RNA-high/surface-low cells are enriched at intermediate times.
- Cells in that state subsequently become surface-positive and acquire the target-associated function.
- A short translation-inhibition window prevents the predicted surface increase.
- Transcription inhibition begun only after RNA has accumulated should not immediately prevent the first wave of surface appearance, although it should prevent later RNA replenishment.

## Mechanism B: Stable post-transcriptional repression or unproductive RNA

Transcript persists, but little protein is synthesized or the measured RNA isoform does not generate the relevant protein.

**Distinct predictions**

- The RNA-high/surface-low state persists without a reproducible transition to surface-positive.
- Total and intracellular protein are also low, distinguishing this mechanism from intracellular retention.
- Translation-focused measurements show low production of the relevant protein, if technically feasible.
- A target-specific UTR, translation-regulator or isoform manipulation changes protein without a proportional change in total RNA.
- RNA and protein may both be technically real, but the RNA does not predict the tested surface function.

## Mechanism C: Intracellular retention or defective trafficking

Protein is made but is not efficiently delivered to the surface.

**Distinct predictions**

- Surface signal is low while total or intracellular protein is high.
- Orthogonal imaging shows intracellular localization.
- A calibrated trafficking perturbation changes localization or surface abundance without requiring a new RNA increase.
- RNA-high/surface-low cells can become surface-positive rapidly under conditions that permit trafficking.

## Mechanism D: Rapid internalization, degradation or shedding

Protein reaches the surface but has a short surface residence time.

**Distinct predictions**

- Surface signal is low despite evidence of production.
- Intracellular, degraded or shed target material is detectable where the biology permits.
- Pulse-labeling shows rapid loss from the surface.
- Perturbing internalization, degradation or shedding raises surface abundance without a corresponding immediate RNA increase.

## Mechanism E: Technical discordance

The apparent state results from RNA false positives, antibody false negatives, ambient molecules, doublets, batch effects, epitope inaccessibility or thresholding.

**Distinct predictions**

- The state does not reproduce across independent biological units.
- It tracks assay batch, ambient signal, sequencing/capture quality or antibody lot rather than biology.
- An alternative RNA assay or non-overlapping antibody clone fails to confirm the same cells.
- Positive and negative controls do not behave as expected.
- The state shows no reproducible temporal trajectory or protein-relevant function.

## Reverse-direction alternative

For **RNA-low/surface-high**, a leading biological alternative is persistence of previously synthesized surface protein after transcription falls. The discriminating prediction is RNA decline before protein decline, with protein loss governed by turnover. RNA dropout must first be excluded by calibrated RNA controls and orthogonal RNA measurement.

---

# 3. Proposed research plan

Everything in this section is a proposal; none of it should be described as an author-reported method or completed result.

## Phase 0: Lock the biological question and analysis rules

### 0.1 Select one target pair

Choose:

- one biological system;
- one surface protein \(X\);
- its corresponding transcript;
- one discordant direction; and
- one functional endpoint directly tied to \(X\), such as ligand binding, signaling, adhesion, transport or another function established for that protein in the chosen system.

The packet does not supply the system, target or function, so these are unreported parameters.

Selection should favor a target for which:

- a validated oligo-tagged antibody and an independent antibody or detection method are available;
- positive and negative biological controls can be obtained;
- the surface protein has a measurable function;
- a biologically relevant stimulus or perturbation can alter its expression; and
- independent biological samples are available.

### 0.2 Prespecify hypotheses

Primary null hypothesis:

> The candidate RNA-high/surface-low state is not reproducibly enriched beyond calibrated technical background and does not predict subsequent surface expression or function.

Primary biological alternative:

> The candidate state is reproducible, orthogonally confirmed and predicts later surface expression and target-associated function.

Secondary alternatives distinguish precursor, stable repression, retention and turnover.

### 0.3 Define estimands before seeing confirmatory data

Recommended primary estimands are:

1. the biological-unit-level proportion of cells in the candidate state;
2. the change in that proportion over time after a defined stimulus;
3. the probability or donor-level estimated rate of transition from the candidate state to surface-positive; and
4. the difference in the target-relevant functional endpoint between validated candidate and comparator cells.

A biologically meaningful effect size, \(\delta\), should be chosen from pilot data and the functional assay before confirmatory analysis. The packet provides no basis for a universal numerical cutoff.

### 0.4 Audit trail

Before data collection, record:

- hypothesis and primary endpoint;
- target, antibody clone/lot and oligo tag;
- RNA target and assay version;
- sample eligibility criteria;
- allocation and blinding procedures;
- preprocessing code and software versions;
- state-definition thresholds or probability model;
- sample-size assumptions;
- stop rules; and
- planned sensitivity analyses.

Raw files, sample identifiers, code and every threshold change should be versioned. Confirmatory endpoints should not be changed after unblinding.

---

## Phase 1: Prerequisites and independent units

### 1.1 Required materials and information

The study requires:

- raw RNA and antibody-tag counts with cell-barcode linkage;
- batch, donor/sample and processing metadata;
- antibody clone, concentration, lot and staining conditions;
- RNA target and library/assay details;
- viability and quality-control measurements;
- access to biological material for orthogonal and longitudinal studies; and
- a functional assay for the selected protein.

The supplied packet does not report these methodological details, so none should be assumed from the original result.

### 1.2 Define independent biological units

Individual cells are not independent experimental units because cells from the same donor, animal or culture share biological and processing variation.

An independent unit should be one of:

- a separate donor;
- a separate animal;
- an independently initiated primary culture; or
- for a cell line, an independently thawed and separately maintained replicate culture.

Splitting one treated culture into wells does not create independent biological replication.

A practical starting design is:

- at least three independent units for assay calibration;
- at least six independent units for pilot variance estimation; and
- a confirmatory sample size calculated from the pilot’s unit-level variance, not from the number of cells.

These are proposed operational minima, not values supported by the packet. A conventional two-sided error rate and desired power may be prespecified, but adequacy must be based on the unit-level effect size and variance.

### 1.3 Allocation

- Randomize independent units to processing batches and, where treatment is between units, to treatment groups.
- When each unit can provide multiple aliquots, use a within-unit design for stimulation, time course or perturbation to control unit-level background.
- Balance relevant biological and processing covariates across batches.
- Randomize sample order during staining, library preparation, imaging and functional assays.

### 1.4 Blinding

Use coded identifiers so personnel performing:

- staining and library preparation;
- flow gating or imaging;
- functional scoring; and
- initial quality control

cannot see treatment, time point or expected state. Unblind only after quality-control acceptance and analysis-code lock. Complete blinding may not be feasible for personnel administering visibly different treatments; downstream measurement should still be blinded.

---

## Phase 2: Assay calibration

The purpose is to determine what each modality can and cannot detect before defining a biological state.

### 2.1 RNA calibration

Use, where feasible:

- known target-positive and target-negative cells;
- engineered target reduction or knockout as a specificity control;
- target-positive dilution series to estimate detection limits;
- sequencing or capture-depth sensitivity analyses;
- empty-droplet or background estimates when supported by the platform; and
- an orthogonal targeted RNA assay for a subset of cells or sorted populations.

Record raw counts, detection fraction, depth, background and unit-level variation. Do not interpret absence of RNA counts as absence of transcript until negative-control and detection-limit performance are established.

### 2.2 Surface-protein calibration

Perform an antibody titration and include:

- unstained controls;
- an irrelevant or isotype oligo-tagged control where appropriate;
- competition with excess unlabeled antibody of the same clone, where feasible;
- known target-positive and target-negative cells;
- engineered target reduction or knockout, where feasible;
- an alternative antibody clone or independent protein assay; and
- separate surface and permeabilized/total staining when localization matters.

An isotype control can estimate nonspecific background but does not by itself prove epitope specificity. Competition, genetic perturbation and orthogonal detection provide stronger specificity evidence.

### 2.3 Calibration acceptance criteria

Because the packet supplies no assay-specific numerical performance bounds, universal thresholds should not be invented. Before unblinded biological analysis, define acceptance criteria such as:

- positive controls separate from negative controls in the expected direction;
- target perturbation reduces the intended RNA or protein signal;
- staining is below saturation and within the validated antibody range;
- background is low enough to detect the prespecified effect;
- replicate measurements are sufficiently consistent to estimate donor-level proportions; and
- quality-control failures are not concentrated in one condition.

If these criteria are not met, stop and revise the assay rather than proceed to biological classification.

### 2.4 Define discordance probabilistically

RNA counts and antibody-tag counts are on different measurement scales and should not be compared as if equal numerical values imply equal abundance.

For each modality:

1. estimate background and positive-control distributions;
2. report continuous calibrated signal;
3. estimate a probability or confidence category for target positivity;
4. define the candidate state using prespecified criteria; and
5. retain threshold sensitivity analyses.

Do not use an unvalidated joint latent representation as the primary definition of the state.

---

## Phase 3: Reproducibility study

### 3.1 Discovery and replication structure

Use at least two non-overlapping sets of independent biological units:

- a discovery set to nominate the target pair and state; and
- an independent replication set to test the locked hypothesis.

If an existing paired dataset is used for discovery, the replication cohort must consist of different biological units, not merely different cells from the same units.

### 3.2 Measurements

For every unit, record:

- raw RNA and antibody-tag measurements;
- candidate-state proportion;
- RNA and protein positivity probabilities;
- cell viability and recovery;
- doublet/ambient-signal metrics;
- batch and processing order;
- biological condition; and
- relevant donor or culture covariates.

### 3.3 Primary analysis

Aggregate cell-level classifications to the biological-unit level. The primary comparison should use the unit-level proportion or rate, with uncertainty estimated across units. Cell-level models may be secondary but must account for clustering by unit and batch.

Proceed only if:

- the state exceeds calibrated background;
- the direction and magnitude replicate;
- the result is robust to prespecified threshold choices; and
- the effect is not explained by a measured technical confounder.

---

## Phase 4: Orthogonal same-cell validation

Validation should not use the same antibody signal to prove itself.

For matched aliquots from independent units, use a technically compatible combination such as:

- targeted RNA visualization plus surface immunostaining;
- an alternative, non-overlapping antibody clone;
- flow or imaging-based surface measurement;
- surface staining followed by permeabilized intracellular staining;
- targeted RNA measurement on sorted populations; and
- total-protein measurement where localization is ambiguous.

The primary orthogonal question is whether the same or prospectively enriched cells are:

- RNA-positive and surface-negative;
- RNA-positive and total-protein-negative; or
- RNA-positive and intracellular-protein-positive.

These patterns discriminate post-transcriptional repression from retention or turnover.

Perfect quantitative agreement is not required because assays have different scales, but direction and state enrichment should agree within prespecified limits.

---

## Phase 5: Longitudinal and fate experiment

### 5.1 Synchronization

Apply a predefined, biologically relevant stimulus expected to alter \(X\). Include:

- untreated baseline;
- vehicle or handling control;
- stimulated condition; and
- matched serial aliquots from the same independent unit.

The stimulus cannot be selected from the packet and must be justified for the chosen system.

### 5.2 Time points

Use an initial grid such as baseline, early RNA response, intermediate protein response and late response. A proposed starting grid could be 0, 2, 6, 12, 24 and 48 hours, but this is only a placeholder. The final grid should be set from a pilot so that it brackets the observed RNA and surface changes.

Measure at each time:

- paired RNA and surface signal;
- total and intracellular protein where feasible;
- viability;
- orthogonal RNA and protein in a subset;
- target-associated function; and
- shed or supernatant target if shedding is plausible.

### 5.3 Direct fate assessment

Single-cell transcript measurement may consume the cell, so population time courses do not prove that the same individual cells changed state.

If the candidate state can be prospectively enriched using validated live-cell markers without activating or blocking \(X\), sort or isolate it and follow surface expression and function. Maintain paired comparator populations. If prospective isolation is impossible, report only population-level transition evidence and avoid claiming direct single-cell fate.

Use separate aliquots for endpoint RNA/antibody measurement and live functional follow-up if the detection antibody itself could perturb the protein.

---

## Phase 6: Mechanism-discriminating perturbations

After the state is replicated and orthogonally confirmed, perturbations should be introduced in a short, calibrated window.

### 6.1 Transcription test

Start transcription inhibition after target RNA has accumulated.

- **Precursor prediction:** existing RNA can support an initial protein/surface rise.
- **Alternative:** if surface appearance requires ongoing transcription, the interpretation may involve a labile intermediate or nonspecific toxicity and should not be overinterpreted.

Include vehicle, viability and a genetic target-knockdown control where feasible.

### 6.2 Translation test

Start translation inhibition at the same post-RNA time.

- **Precursor prediction:** surface and total-protein increases are blocked.
- **Stable repression prediction:** little protein increase exists to block.
- **Retention prediction:** intracellular protein may already be present.

Global translation inhibitors can cause rapid toxicity; use the shortest calibrated exposure, viability controls and, where possible, an orthogonal target-specific manipulation.

### 6.3 Trafficking and turnover tests

Only after localization evidence is obtained, test a target-informed perturbation of:

- intracellular retention/export;
- internalization;
- degradation; or
- shedding.

The packet does not identify a target, so a specific drug should not be named in advance. Use vehicle, viability and genetic or orthogonal confirmation.

### 6.4 Regulatory test

If total protein is low despite persistent RNA, test a prespecified isoform, UTR or translation-regulator manipulation only if the selected system provides a rationale. A protein increase without a proportional RNA increase would support post-transcriptional regulation.

---

## Phase 7: Functional consequence

The functional endpoint must be chosen before confirmatory testing and must be directly related to the surface protein.

Compare:

- candidate-state cells;
- double-negative or RNA-low/surface-low comparators;
- surface-positive cells; and
- candidate cells after follow-up or perturbation.

Measure function under:

- baseline conditions;
- relevant stimulation;
- target blockade, if a validated perturbation exists; and
- rescue or genetic restoration where feasible.

A validated state that never affects a target-relevant function may still be real biologically, but it should not be described as functionally consequential.

---

# 4. Analysis plan

## 4.1 Ordered analysis

1. Freeze raw data and metadata.
2. Apply prespecified cell and sample quality control.
3. Evaluate calibration controls before biological samples are interpreted.
4. Normalize RNA and antibody-tag data separately.
5. Estimate modality-specific background and positivity probabilities.
6. Define the candidate state.
7. Aggregate results by independent biological unit.
8. Perform the locked replication analysis.
9. Conduct orthogonal, longitudinal and perturbation analyses.
10. Perform sensitivity analyses only after the primary result is recorded.

## 4.2 Statistical principles

- Treat biological units, not individual cells, as the primary replication unit.
- Report effect sizes and uncertainty intervals, not only dichotomous significance.
- Model time and perturbation effects at the unit-time level or include unit-level random effects in secondary models.
- Account for batch without removing the biological condition.
- Control multiplicity across exploratory proteins; the selected pair should have one primary endpoint.
- Conduct sensitivity analyses across normalization methods, state thresholds and quality-control exclusions.
- Do not claim direct cell fate from destructive serial measurements unless cells were prospectively followed.
- Do not claim an optimal integrated representation; the study validates one biological state, not a universal algorithm.

## 4.3 Missing data and failed runs

Prespecify whether samples are excluded before unblinding based on:

- control failure;
- insufficient recovery;
- failed barcode linkage;
- unacceptable background;
- extreme viability loss; or
- documented processing failure.

Exclusions should be recorded with reasons and analyzed for imbalance across conditions.

---

# 5. Stop rules

## Technical stop

Stop and rerun or redesign if:

- positive and negative controls fail their prespecified acceptance criteria;
- antibody titration does not produce a usable signal-to-background range;
- RNA controls show inadequate detection of known positive material;
- ambient signal or doublets prevent reliable classification;
- viability loss is excessive or disproportionate in one perturbation; or
- barcode or batch metadata are incomplete.

One blinded repeat may be allowed for a documented technical failure. Repeated unblinded attempts to obtain a desired result should not be allowed.

## Biological futility stop

Stop the biological-state claim if:

- the candidate state does not exceed calibrated background in the discovery cohort;
- it fails the independent replication criterion;
- orthogonal assays do not confirm the direction of discordance; or
- the confirmatory uncertainty interval excludes the prespecified biologically meaningful effect \(\delta\).

A true no-effect result should still be reported.

## Functional-question stop

If no target-relevant functional assay can be validated, do not claim functional consequence. Either develop the assay before the confirmatory experiment or restrict the conclusion to molecular state validation.

## Mechanistic stop

If a perturbation produces unacceptable nonspecific toxicity or cannot be interpreted, replace it with a genetic or orthogonal perturbation rather than treating the toxic condition as mechanism evidence.

---

# 6. Troubleshooting

| Observation | Possible explanation | Proposed response |
|---|---|---|
| High antibody-tag background | Excess antibody, inadequate washing, nonspecific binding or ambient tags | Retitrate; improve washing; use competition and negative controls; estimate background before reclassification |
| Low surface signal in known positive cells | Epitope loss, antibody failure, fixation/processing effect or genuinely low surface abundance | Test alternative clone, fresh staining conditions and total/intracellular protein |
| Low RNA signal in known positive cells | Poor capture/depth, transcript instability or wrong isoform assay | Increase validated detection range if possible; use targeted orthogonal RNA assay; inspect isoform specificity |
| Discordance concentrated in one batch | Technical confounding | Rebalance units across batches; rerun independent units; do not batch-correct away the condition |
| State replicates but no surface transition occurs | Stable repression, unproductive RNA or missed time window | Add denser pilot-informed time points; measure total/intracellular protein and translation |
| Surface-low but total-protein-high | Intracellular retention or rapid internalization | Perform localization, pulse-label and turnover experiments |
| Inhibitor changes many unrelated readouts | Nonspecific toxicity | Shorten exposure, reduce dose within calibrated range, use genetic perturbation and viability controls |
| Sorted candidate cells rapidly change state | Sorting, temperature or handling alters biology | Minimize processing time; include handled controls; interpret as post-sort behavior rather than original fate |
| Orthogonal assays disagree with one another | Different epitopes, isoforms, localization or sensitivity | Resolve calibration first; do not average incompatible assays into a state call |

---

# 7. Interpretation of outcomes

## Positive outcome 1: transient licensed precursor

A strong positive package would show:

- replication across independent units;
- orthogonal RNA and surface confirmation;
- RNA increase before total/surface protein;
- enrichment of the candidate state at intermediate times;
- transition to surface-positive status;
- translation dependence; and
- later acquisition of target-relevant function.

**Strongest justified conclusion:** in the selected system and for the selected protein, the RNA-high/surface-low state is a reproducible transient precursor state that predicts surface expression and function.

This would not justify generalizing to all proteins, all cell types or all RNA–protein disagreements.

## Positive outcome 2: stable post-transcriptional state

If RNA and total protein measurements are valid but protein remains low, with no transition and a target-specific regulatory manipulation restores protein:

**Conclusion:** the state is biologically real but is a stable post-transcriptionally regulated or unproductive-RNA state, not a short-lived precursor.

## Positive outcome 3: trafficking or turnover state

If surface is low but intracellular, shed or newly produced protein is high, and a localization/turnover perturbation changes surface abundance without an immediate RNA change:

**Conclusion:** the discordance represents a real localization or surface-residence state rather than absence of protein production.

## Negative outcome due to technical discordance

If the state fails independent replication, tracks batch or ambient signal, and is not confirmed by an alternative RNA assay or antibody clone:

**Conclusion:** the apparent state is best explained by measurement or processing artifacts in this dataset. This would not prove that every RNA–protein disagreement is artifactual.

## Negative outcome with valid assays

If the state is technically detectable but is not enriched, does not transition and has no reproducible functional association:

**Conclusion:** under the tested conditions, there is no evidence that the candidate discordance defines a consequential biological state. This is a conditional absence of evidence, not proof that no state exists under all conditions.

## Ambiguous outcome

Ambiguity would arise if:

- the state replicates but orthogonal assays disagree;
- RNA and protein are both real but no mechanism separates;
- transition occurs at the population level without direct fate evidence;
- perturbations are toxic or nonspecific; or
- molecular state is validated but function remains unmeasurable.

**Conclusion:** report the reproducible molecular observation but withhold a precursor, regulatory or functional-state claim. The next step would then be assay-specific resolution or a target-specific perturbation, not a broad integration claim.

---

# Final recommendation and limits

**Next action:** select and lock one functionally interpretable RNA–surface-protein pair, calibrate each modality independently, replicate one discordant state across independent biological units, confirm it with orthogonal same-cell measurements, and test temporal and functional predictions using within-unit longitudinal and perturbation experiments.

The supplied packet justifies only the conclusion that RNA and selected surface proteins can be measured in the same cells. It does not justify calling a discordant cluster a cell state, choosing an integrated representation, or claiming causal or functional significance. The proposed study would convert a same-cell measurement disagreement into a testable biological hypothesis while preserving clear separation between reported evidence and proposed experiments.
