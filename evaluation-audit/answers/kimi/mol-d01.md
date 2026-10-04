# Kimi K3 / mol-d01

Original final answer, shared by both scoring rounds.

## Recommended conclusion and next action

The discriminating experiment is **matched rescue of validated K-null cells with wild-type K versus a catalytically inactive K construct**. Do **not** interpret the available kinase-dead construct until its expression, solubility/folding, localization, interactions, and residual catalytic activity have been measured.

The primary comparison should be:

1. **K-null + empty vector**: no rescue.
2. **K-null + wild-type K**: expected rescue.
3. **K-null + validated kinase-dead K**: determines whether catalytic activity is necessary.

If wild-type K restores ligand-induced phospho-S and growth, but equally expressed, properly folded, interaction-competent kinase-dead K does not, K catalytic activity is required. If kinase-dead K restores both despite having no detectable K catalytic activity, catalytic activity is dispensable and a noncatalytic—potentially scaffolding—function is sufficient.

---

# 1. Evidence-to-inference-to-conclusion chain

| Evidence | Supported inference | Not yet supported |
|---|---|---|
| **M1:** Pooled K knockout lowers ligand-induced phospho-S and slows growth | Loss of K is associated with reduced ligand-induced S phosphorylation and slower cell expansion | Whether the responsible K function is catalytic, structural, or both; whether effects are clonal, off-target, or adaptive |
| **M2:** Total S is unchanged | Assuming measured in the same conditions, the reduced signal is likely a lower phospho-S/total-S ratio rather than loss of S protein | Whether K directly phosphorylates S; total S must be remeasured in the new experiment |
| **M3:** One unvalidated kinase-dead construct exists | It is a candidate rescue reagent | That it is catalytically inactive, folded, stable, correctly localized, or capable of normal scaffolding |

### Conclusion from current evidence

M1 and M2 justify a mechanistic rescue study but do **not** distinguish catalytic from scaffolding functions. M3 cannot yet support a negative mechanistic inference.

### Operational hypotheses

- **H1—catalytic activity required:** Wild-type K rescues ligand-induced signaling and growth; catalytically null but structurally validated K does not.
- **H2—noncatalytic/scaffold function sufficient:** Catalytically null K rescues equivalently to wild-type K while retaining normal localization and relevant interactions.
- **H3—joint or quantitative requirement:** Kinase-dead K produces intermediate rescue or rescues only one endpoint.

“Scaffolding” should mean more than protein presence: kinase-dead K should preserve ligand-relevant K complexes, localization, or interactions. If no relevant partner or complex is known, an unbiased K-interaction analysis can support, but not prove, a scaffold mechanism.

---

# 2. Core study design

## 2.1 Cell groups

Use a full genotype-by-ligand design.

### Required groups

1. **Process-matched parental K-positive control**
2. **Validated K-null + empty rescue backbone**
3. **Validated K-null + wild-type K**
4. **Validated K-null + kinase-dead K**

Each group is tested with:

- Vehicle
- Ligand

A parental-plus-empty-vector group is useful if the rescue backbone or selection procedure could affect signaling or growth.

## 2.2 Genetic backgrounds

The original pooled knockout is useful preliminary evidence but should not be the sole mechanistic background because it may contain residual K, mixed edits, and clone-specific effects.

Preferred approach:

- Derive or generate **at least two independently derived K-null cell populations or clones**.
- Verify complete loss of K protein and characterize the relevant genomic alteration.
- Rescue each background independently with empty, wild-type, or kinase-dead constructs.

If resources permit only one K-null background initially, use at least three independently generated rescue populations per construct and subsequently confirm the key contrast in a second K-null background.

## 2.3 Construct requirements

Wild-type and kinase-dead rescue constructs should be identical except for the catalytic mutation:

- Same promoter or genomic targeting strategy
- Same tag, if any
- Same UTRs, selection marker, and backbone
- Sequence-verified coding region

Preferred expression is from the endogenous locus or another method giving approximately endogenous K abundance. If exogenous expression is used, calibrate it against parental K abundance and avoid high overexpression, which can exaggerate scaffolding or produce nonphysiological complexes.

Because M3 is a single construct, a mutation-specific folding or interaction defect remains a major risk. If feasible, validate at least one independently constructed catalytic-null allele. The primary experiment can proceed with M3 only if it passes all quality gates.

---

# 3. Ordered operational protocol

## Stage 1 — Pre-register the experiment and calibrate unknown parameters

### 1.1 Define primary endpoints before unblinding

Use two co-primary endpoints:

1. **Ligand-induced signaling:** change in phospho-S normalized to total S, using a prespecified time point or area under the ligand-versus-vehicle time-course difference.
2. **Ligand-induced growth:** ligand-dependent change in exponential growth rate, measured by longitudinal viable-cell accumulation.

Choose one primary signaling endpoint after pilot calibration and lock it before the confirmatory experiment.

### 1.2 Calibrate ligand dose and sampling times

The active ligand concentration, response peak, and response duration are unreported. Therefore:

- Expose parental cells to a ligand dose series.
- Measure phospho-S and total S over multiple time points.
- Select a dose in the responsive, nonsaturated range.
- Include baseline, an early time, the approximate peak, and a later time.
- Repeat the time course in K-null and rescued cells because loss of K may shift kinetics as well as amplitude.

Do not assume that the parental peak time is appropriate for every genotype.

### 1.3 Calibrate the growth assay

The method and conditions underlying M1 are unspecified.

- Confirm that cells remain in exponential growth for the full observation interval.
- Calibrate starting density so confluence, nutrient depletion, or extensive death does not truncate the measurement.
- Measure viable-cell number or an equivalent calibrated biomass readout at multiple times, plus dead-cell fraction.
- Include ligand and vehicle conditions.
- Where possible, retain the original growth readout and add direct viable-cell counting as an orthogonal measurement.

A ligand-specific effect requires a genotype-by-ligand interaction. Equal slowing in ligand and vehicle would instead suggest a basal fitness defect.

### 1.4 Calibrate expression and rescue sensitivity

Generate a wild-type K expression or activity dilution series in K-null cells. Use it to determine:

- The relationship between K abundance and phospho-S rescue
- The relationship between K abundance and growth rescue
- The lowest wild-type K level that gives reproducible rescue
- An equivalence margin for comparing kinase-dead with wild-type rescue

This avoids declaring “no rescue” when the experiment could not detect rescue from a modest but biologically relevant amount of K.

---

## Stage 2 — Construct and cell-model quality control

### 2.1 Sequence and construct QC

For wild-type and kinase-dead constructs:

- Verify the intended mutation and absence of unintended coding changes.
- Confirm matching backbone and expression elements.
- Confirm that a rescue allele cannot be altered by any remaining genome-editing reagent, if relevant.

### 2.2 Verify K-null status

For each K-null background:

- Characterize the genomic alteration.
- Demonstrate absence of detectable full-length and truncated K protein using methods with defined limits of detection.
- Check whether residual K remains in a minor subpopulation.

If K protein is still detectable, reclone or derive a new K-null line. Residual K can interact with or be activated by a kinase-dead construct and confound the result.

### 2.3 Match K abundance and distribution

For each independent rescue line:

- Quantify K protein per cell relative to parental cells.
- Examine the distribution of expression, not only the population average.
- Compare soluble and insoluble K fractions.
- Confirm similar subcellular localization of wild-type and kinase-dead K.

The acceptance range should be based on the wild-type dose-response calibration: expression is adequately matched when wild-type variation across the same range does not materially alter rescue. Do not use an arbitrary abundance cutoff without that calibration.

### 2.4 Measure catalytic activity directly

The kinase-dead construct must be tested empirically.

Preferred measurements:

- Purified K activity, if a suitable preparation and substrate are available
- Otherwise, quantitative K immunoprecipitation followed by a validated catalytic assay

For immunoprecipitation assays:

- Normalize activity to recovered K abundance.
- Include K-null immunoprecipitates to estimate background.
- Include wild-type K dilutions to establish linearity and the lower detection limit.
- Measure activity under vehicle and ligand conditions if ligand activates K.

If no validated K substrate or direct activity assay exists, develop and calibrate one before making a catalytic-dead claim. A negative immunoprecipitation assay can be confounded by coprecipitating kinases, so purified protein is preferable when feasible.

Acceptance criterion: kinase-dead K activity should be indistinguishable from the K-null/background assay and below the amount of wild-type activity shown by titration to produce detectable rescue. Report the assay limit of detection.

### 2.5 Validate folding and scaffold-relevant properties

No single assay proves correct folding. Use several orthogonal comparisons of kinase-dead versus wild-type K:

- Soluble abundance and aggregate formation
- Thermal or protease sensitivity, if suitable assays are available
- Subcellular localization
- Native complex behavior
- Interactions with validated K-associated partners, if such partners are known

If no relevant partner is established, quantitative K immunoprecipitation followed by an unbiased interaction analysis can identify whether the mutation globally disrupts the K interactome. This is supportive, not definitive, evidence of scaffold preservation.

Acceptance criterion: kinase-dead K should be within prespecified equivalence limits of wild-type K for abundance, solubility, localization, and the interaction measures selected before unblinding. If it is misfolded, aggregated, mislocalized, or broadly interaction-defective, a failure to rescue cannot distinguish loss of catalysis from loss of structure.

---

## Stage 3 — Independent units, allocation, and blinding

### 3.1 Define the independent unit

The biological unit is an **independently generated rescue population or clone**, not an individual well.

Minimum feasible design:

- At least three independently generated rescue populations per construct per K-null background
- Technical replicates within each population may improve measurement precision but must not be counted as biological replicates

Final sample size should be calculated from pilot estimates of variance and the minimum rescue effect deemed biologically meaningful. A sample of three is a minimum for assessing reproducibility, not evidence of adequate power.

### 3.2 Allocation

- Maintain independent rescue populations separately.
- Within each independent unit, randomize cultures to ligand or vehicle.
- Randomize plate positions, processing order, and assay batches.
- Block by independent line, experimental day, and plate to prevent confounding.
- Rotate plate layouts between runs to reduce position effects.

### 3.3 Blinding

- Assign coded labels to genotype and treatment after allocation.
- Keep sample acquisition and primary quantification blinded.
- Lock the analysis plan before unblinding.
- Unblind only after sample-level quality control is complete.

If complete operator blinding is impossible during cell treatment, blinding should still be applied to sample labeling, image acquisition, quantification, and analysis.

---

## Stage 4 — Intervention and sampling

### 4.1 Acute signaling experiment

1. Plate equal numbers of viable cells from each independent unit.
2. Allow a standardized recovery period.
3. Apply ligand or vehicle using the randomized layout.
4. Collect samples at baseline and the calibrated time points.
5. Process all samples rapidly and uniformly using conditions validated to preserve phosphorylation.
6. Measure:
   - Phospho-S
   - Total S
   - K abundance
   - K catalytic activity in matched samples, where feasible
   - K localization or complex state in a prespecified subset

Use the same calibrated pre-stimulation conditions for every genotype. If those conditions themselves affect growth or basal signaling, record and model that effect rather than treating it as a constant.

### 4.2 Growth experiment

1. Plate equal viable-cell numbers at a density calibrated to remain in exponential growth.
2. Apply ligand or vehicle.
3. Measure viable-cell accumulation longitudinally across several doublings.
4. Measure dead-cell fraction or another viability endpoint at the same times.
5. Record confluence and any morphology that could distort biomass-based measurements.

Growth and signaling should be run as linked but separate experiments because acute signaling measurements require sampling before major differences in cell number develop.

---

# 4. Measurements and controls

## Required measurements

1. **Phospho-S and total S**
   - Report phospho-S/total-S.
   - Also report absolute phospho-S because M2 does not guarantee total S will remain unchanged in every new genotype.

2. **K abundance and localization**
   - Quantify per-cell expression and distribution.

3. **K catalytic activity**
   - Demonstrate wild-type activity and kinase-dead background-level activity.

4. **Folding/scaffold quality**
   - Solubility, aggregation, localization, and relevant complex formation.

5. **Growth and viability**
   - Distinguish slower proliferation from increased death.

## Required controls

- Parental cells ± ligand
- K-null + empty backbone ± ligand
- K-null + wild-type K ± ligand
- K-null + kinase-dead K ± ligand
- Baseline unstimulated samples
- Assay-background controls
- K-null immunoprecipitate for the K activity assay
- Wild-type K dilution series for expression/activity sensitivity

---

# 5. Analysis plan

## 5.1 Signaling

For each independent unit, calculate the ligand-induced response from the phospho-S/total-S time course, preferably as:

\[
D_{\text{signaling}} = \text{ligand response AUC} - \text{matched vehicle response AUC}
\]

Analyze log-transformed ratios if that stabilizes variance.

Use a mixed-effects model with:

- Fixed effects: genotype, ligand, time, and their interactions
- Random effects: independent line/background, experimental batch, and plate where appropriate

The primary mechanistic contrast is:

\[
(\text{WT rescue} - \text{empty rescue})
\quad \text{versus} \quad
(\text{KD rescue} - \text{empty rescue})
\]

A normalized rescue index may aid interpretation:

\[
I_K =
\frac{D_{\text{rescue}} - D_{\text{empty}}}
{D_{\text{WT}} - D_{\text{empty}}}
\]

where 0 approximates no rescue and 1 approximates wild-type-level rescue. Do not use this index if wild-type rescue is close to zero because the ratio will be unstable.

## 5.2 Growth

Estimate the exponential growth rate from longitudinal viable-cell measurements. Model:

- Genotype
- Ligand
- Time
- Genotype-by-ligand interaction
- Random effects for line, plate, and batch

The key result is not simply whether a genotype grows, but whether ligand changes its growth rate relative to vehicle.

## 5.3 Decision rules

Use effect sizes and confidence intervals, with multiplicity control across prespecified contrasts.

- **Catalytic activity required:** wild-type rescue exceeds the prespecified meaningful threshold; kinase-dead rescue is below that threshold; kinase-dead activity is below the rescue-relevant detection limit; folding and interaction QC pass.
- **Catalytic activity dispensable/noncatalytic rescue sufficient:** kinase-dead rescue is equivalent to wild-type rescue within the calibrated equivalence margin, despite background-level catalytic activity.
- **Partial or dual role:** kinase-dead rescue is intermediate, or rescue differs between signaling and growth.

Equivalence margins must come from the wild-type dose-response and assay calibration, not from an arbitrary post hoc cutoff.

---

# 6. Discriminating outcomes

| Result, assuming all QC passes | Interpretation |
|---|---|
| WT rescues phospho-S and growth; kinase-dead K does not | K catalytic activity is required for both outputs. This does not prove that K directly phosphorylates S; it may activate another kinase. |
| WT and kinase-dead K rescue both endpoints equivalently; kinase-dead activity is background-level | K catalytic activity is dispensable. A noncatalytic K function is sufficient. If localization and relevant complexes are preserved, this supports a scaffold-like mechanism. |
| Kinase-dead K gives partial rescue of both endpoints | Catalytic activity contributes quantitatively, but a noncatalytic function also contributes, or residual pathway compensation exists. |
| Kinase-dead K rescues growth but not phospho-S | Catalytic activity is required for S phosphorylation but not for the growth effect; growth may depend on another K output or adaptation. |
| Kinase-dead K rescues phospho-S but not growth | S phosphorylation can be restored without restoring the growth phenotype; K catalytic activity may control a different growth-relevant substrate or process. |
| KO reduces growth equally in ligand and vehicle | K affects basal fitness, not specifically ligand-induced growth. |
| WT rescue fails | The mechanistic test is invalid. Possible causes include irreversible KO adaptation, off-target effects, failed reconstitution, or an inappropriate expression level. |
| Kinase-dead K has residual catalytic activity | No catalytic-versus-scaffold conclusion is justified. |
| Kinase-dead K is unstable, aggregated, mislocalized, or interaction-defective | Failure to rescue cannot be attributed specifically to loss of catalysis. Replace or re-engineer the construct. |
| Kinase-dead K rescues but does not preserve relevant complexes | A noncatalytic function is implicated, but it should not be called normal scaffolding without additional evidence. |

---

# 7. Acceptance and stopping criteria

## Proceed only if all are met

1. K-null lines lack detectable K within the assay’s reported detection limit.
2. Parental cells show a reproducible, nonsaturated ligand-induced phospho-S response.
3. The K-null phenotype from M1 is reproduced in the validated background.
4. Wild-type K produces detectable rescue.
5. Wild-type and kinase-dead K are sequence-verified and expressed within the calibrated functional range.
6. Kinase-dead K has background-level activity in a direct assay.
7. Kinase-dead K passes solubility, localization, and relevant interaction QC.
8. Growth measurements remain within the calibrated exponential range.
9. At least the prespecified number of independent biological units is available.
10. Randomization, blinding, and batch balance were maintained.

## Stop or do not interpret mechanistically if

- Wild-type K fails to rescue.
- Kinase-dead K is unstable, misfolded, mislocalized, or broadly interaction-defective.
- Residual kinase-dead activity exceeds the level shown by wild-type titration to produce rescue.
- Expression cannot be matched or functionally calibrated.
- The parental ligand response disappears.
- Growth curves leave the calibrated range.
- One clone or batch dominates the result.

---

# 8. Troubleshooting

| Problem | Recommended response |
|---|---|
| Weak parental phospho-S response | Verify ligand activity and recalibrate dose, timing, and pre-stimulation conditions; check assay linearity. |
| High basal phospho-S | Adjust and standardize the pre-stimulation protocol; confirm that ligand still produces a dynamic response. |
| K expression mismatch | Use expression titration, alternative regulated expression, or select lines within the calibrated functional range. |
| Kinase-dead K unstable or aggregated | Do not interpret the negative result; validate an independently constructed catalytic-null allele. |
| WT rescues signaling but growth remains abnormal | Investigate expression, clone-specific adaptation, and whether growth depends on a different K output. |
| Growth differences accompanied by increased death | Analyze viable-cell accumulation and death separately; do not describe the phenotype solely as slowed proliferation. |
| Total S changes in a new genotype | Report absolute phospho-S and phospho-S/total-S; avoid attributing all change to phosphorylation. |
| Immunoprecipitated kinase-dead K appears active | Suspect residual activity or a coprecipitated kinase; normalize to K recovery and use purified K if possible. |
| Large clone-to-clone variability | Add independent K-null backgrounds and rescue populations; do not average away clonal effects without reporting them. |

---

# 9. Principal limits and alternatives

1. **A single kinase-dead allele is not sufficient by itself.** Mutation-induced misfolding can mimic loss of catalytic requirement. Structural and interaction QC is essential.
2. **Rescue with kinase-dead K can establish that catalytic activity is dispensable, but does not prove scaffolding is required.** Testing scaffold necessity requires a reciprocal catalytic-competent, scaffold-disruptive K variant. No validated scaffold-disruptive mutant or relevant interaction surface is supplied, so that arm cannot yet be specified.
3. **Long-term knockout and rescue allow adaptation.** A validated acute catalytic inhibitor, if one existed, would be an orthogonal test, but no such inhibitor is included in the evidence packet.
4. **Phospho-S is a pathway readout, not proof that S is a direct K substrate.** A direct K-to-S phosphorylation claim would require a separate direct-substrate experiment.
5. **Signaling and growth may be separable.** Concordant rescue does not prove that S phosphorylation causes the growth phenotype.
6. **Results may be cell-line and ligand-condition specific.** They should not be generalized beyond the tested cancer line without independent replication.

The pivotal gate is therefore **validation of M3 before phenotypic interpretation**. Only a matched, catalytically null, structurally competent rescue construct can discriminate catalytic necessity from a noncatalytic scaffold function.
