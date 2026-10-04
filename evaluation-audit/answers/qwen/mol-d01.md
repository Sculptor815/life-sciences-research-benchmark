# Qwen3.8 Max (0902) / mol-d01

Original final answer, shared by both scoring rounds.

## Recommended next action

Do **not** interpret the available unvalidated kinase-dead construct as evidence by itself. The decisive experiment is a **separation-of-function rescue test** in K-null cells, but it is interpretable only if the kinase-dead K protein is shown to be:

1. expressed at a comparable level to wild-type K,  
2. correctly folded/stable,  
3. catalytically inactive, and  
4. still competent for the relevant scaffolding interactions/localization.

The primary study should therefore be:

**K knockout cancer cells + empty vector vs. K knockout cells rescued with wild-type K vs. K knockout cells rescued with validated kinase-dead K**, followed by ligand stimulation and measurement of **phospho-S**, **total S**, and **growth**.  

Add orthogonal confirmation if feasible: acute catalytic inhibition, an endogenous catalytic-dead knock-in, or a degron-based scaffold-removal system.

---

# 1. Evidence-to-inference-to-conclusion chain

| Evidence | Inference supported | Inference not supported | Consequence for study design |
|---|---|---|---|
| **M1:** Pooled K knockout lowers phospho-S after ligand stimulation and slows growth. | K is required for normal ligand-induced S phosphorylation and for normal growth. | Whether K acts through catalytic activity, scaffolding, or both. KO removes the whole protein and therefore removes both possible functions. | Need separation-of-function mutants or acute catalytic inhibition. |
| **M2:** Total S is unchanged. | The phospho-S reduction is not explained by loss of S protein abundance. | Whether S is directly phosphorylated by K, whether S localization/complexing changes, or whether another kinase/adaptor is affected. | Measure phospho-S normalized to total S in all experimental arms; keep total S as a QC readout. |
| **M3:** One unvalidated kinase-dead construct is available; abundance and folding not measured. | A kinase-dead rescue could, in principle, distinguish catalytic from scaffolding functions. | Any causal conclusion from that construct until it is validated. If it is unstable, poorly expressed, misfolded, or binding-defective, failure to rescue cannot prove catalytic requirement. | Validate and expression-match the kinase-dead construct before functional interpretation; if it fails validation, use alternative alleles or endogenous knock-in. |

**Core logic:**  
A K knockout removes both catalytic and scaffolding functions. A validated kinase-dead mutant should remove catalysis while preserving scaffold. Therefore:

- If kinase-dead K fails to rescue while wild-type K rescues, and the kinase-dead protein is confirmed to be present, folded, catalytically inactive, and scaffold-competent, then **K catalytic activity is required**.
- If kinase-dead K rescues as well as wild-type K, and is confirmed catalytically inactive and scaffold-competent, then **catalytic activity is not required under those conditions**, supporting a scaffolding role.
- If kinase-dead K fails validation, the result is **inconclusive**.

---

# 2. Causal framework and discriminating perturbations

| Perturbation | Catalytic activity | Scaffold/protein presence | If catalytic activity is required | If scaffold is required but catalysis is not |
|---|---:|---:|---|---|
| K knockout/degron | Lost | Lost | Reduced phospho-S and growth | Reduced phospho-S and growth |
| Validated kinase-dead K in KO background | Lost | Present if properly folded and localized | Reduced phospho-S and growth | Rescue of phospho-S and growth |
| Acute selective catalytic inhibition | Lost or blocked | Present | Reduced phospho-S and growth | No effect, if inhibitor does not disrupt scaffold |
| Scaffold-defective but catalytically active K, if obtainable | Present | Lost or impaired | Rescue, if scaffold truly dispensable | Reduced phospho-S and growth |

The strongest study uses at least two complementary perturbations:

1. **Genetic rescue:** wild-type K versus kinase-dead K in K-null cells.  
2. **Acute catalytic inhibition:** selective inhibitor, analog-sensitive allele, or endogenous catalytic-dead knock-in.  

A scaffold-specific mutant is highly desirable but may require mapping K interaction surfaces first.

---

# 3. Assumptions and unreported parameters

The following are not specified in the evidence packet and must be calibrated, not assumed:

- ligand identity, concentration, and stimulation time;
- K kinase-dead mutation and construct architecture;
- expression level and stability of wild-type and kinase-dead K;
- relevant K scaffolding partners, including whether K binds S, receptor, or adaptor proteins;
- antibody or detection reagent specificity for K, phospho-S, and total S;
- availability and selectivity of a K catalytic inhibitor;
- growth assay duration, seeding density, and dynamic range.

For each unknown, the protocol below provides a calibration procedure.

---

# 4. Ordered operational protocol

## 4.1 Preparation and baseline quality checks

### 4.1.1 Cell model

1. Use the cancer cell line in which the M1/M2 phenotype was observed.
2. Authenticate the line and confirm absence of mycoplasma.
3. Maintain cells under standardized conditions and use low-passage stocks.
4. Create or obtain K knockout material:
   - If only pooled K knockout exists, derive at least two independent single-cell K knockout clones.
   - Use at least two independent guide RNAs or recombination events if new KO lines are generated.
5. Confirm K loss by quantitative immunoblot or targeted proteomics.
6. Confirm the baseline M1/M2 phenotype:
   - ligand-induced phospho-S is reduced in K knockout relative to parental;
   - total S is unchanged.

**Acceptance criterion:** K protein is undetectable or effectively absent, phospho-S induction is reduced, and total S remains unchanged.

### 4.1.2 Constructs

Use:

- empty vector;
- wild-type K;
- kinase-dead K;
- optionally, alternative kinase-dead alleles if the available one fails validation.

Construct design requirements:

- same promoter, vector backbone, selection marker, and tag strategy for wild-type and kinase-dead K;
- if tagged, place the tag at the same position in all constructs;
- test untagged and tagged versions if tagging might affect folding or interactions;
- sequence-verify all constructs across the K coding region, especially the kinase domain.

---

## 4.2 Calibration procedures for unknown parameters

### 4.2.1 Ligand concentration and stimulation time

Objective: choose ligand dose and time that robustly report K-dependent signaling without saturating the assay.

Procedure:

1. Stimulate parental cells and wild-type rescued K knockout cells with a serial dilution of ligand.
2. Collect samples across a time course after stimulation.
3. Measure phospho-S and total S.
4. Fit dose-response curves and time-response curves.
5. Select:
   - a ligand concentration giving a robust, reproducible induction with adequate dynamic range;
   - a time point corresponding to peak or early sustained phospho-S, depending on the biological question.

Do not fix final ligand dose or time before this calibration.

### 4.2.2 Growth assay dynamic range

Objective: ensure growth measurements are made during interpretable, non-saturated growth.

Procedure:

1. Seed cells at several densities.
2. Monitor cell number/viability over time.
3. Choose a seeding density and assay duration where cells remain in exponential growth and signal is linear with cell number.
4. Confirm that ligand, vehicle, and selection agents do not produce non-specific toxicity over the assay window.

### 4.2.3 Antibody/detection calibration

For phospho-S, total S, and K:

1. Validate phospho-S signal using K knockout cells and, if possible, phosphatase-treated samples.
2. Validate total S signal across a dilution series to establish linear detection range.
3. Validate K detection using knockout cells and purified K or calibrated lysate standards if available.
4. Pre-specify loading-control strategy: total protein stain, housekeeping protein, or targeted proteomics normalization.

### 4.2.4 Inhibitor calibration, if a selective inhibitor is available

If no selective inhibitor exists, do not use a weak or non-selective inhibitor as primary evidence. Instead, use genetic orthogonal approaches.

If an inhibitor is available:

1. Treat wild-type K rescue cells with a dose range.
2. Measure:
   - phospho-S induction;
   - K abundance;
   - K autophosphorylation or another cellular target-engagement readout if known;
   - relevant scaffold interactions.
3. Choose a dose that suppresses catalytic readout without reducing K abundance or disrupting scaffold, unless the purpose is specifically to test conformational effects.
4. Include vehicle controls.

---

## 4.3 Validation of the kinase-dead construct before functional testing

This is the critical gate. Do not proceed to causal inference with an unvalidated kinase-dead protein.

### 4.3.1 Expression matching

1. Express wild-type K and kinase-dead K in K knockout cells.
2. Generate multiple independent stable lines or independently transduced populations for each construct.
3. Quantify K protein using calibrated immunoblot or targeted proteomics.
4. Match expression:
   - to endogenous K level in parental cells if possible;
   - at minimum, match wild-type and kinase-dead K to each other within a pre-specified interval derived from assay variability.

**Acceptance criterion:** wild-type and kinase-dead K are not significantly different in abundance, and neither is grossly overexpressed relative to endogenous K unless overexpression is explicitly being tested as a separate variable.

If kinase-dead K is unstable or low:

- test proteasome inhibition diagnostically to determine whether it is being degraded;
- try an alternative tag, promoter, or construct design;
- generate an endogenous kinase-dead knock-in instead;
- do not infer catalytic requirement from a low-abundance kinase-dead protein.

### 4.3.2 Folding and stability

Objective: show that the kinase-dead mutation does not grossly unfold or destabilize K.

Use one or more of:

- cellular thermal shift assay/CETSA;
- thermal shift assay on purified protein if purification is feasible;
- limited proteolysis sensitivity;
- solubility fractionation.

Calibration:

1. Establish wild-type K melting/protease-sensitivity profile.
2. Measure assay variability using repeated wild-type samples.
3. Pre-specify a stability acceptance band based on that variability.

**Acceptance criterion:** kinase-dead K has a folding/stability profile within the pre-specified acceptable range relative to wild-type K.

If kinase-dead K is markedly destabilized, failure to rescue cannot be attributed specifically to loss of catalytic activity.

### 4.3.3 Catalytic inactivity

Objective: demonstrate that kinase-dead K lacks detectable catalytic activity.

Use the most direct assay available:

- in vitro kinase assay with immunoprecipitated or purified K;
- phosphorylation of S if S is a candidate direct substrate;
- phosphorylation of a known K substrate if available;
- K autophosphorylation if a suitable site is known.

Calibration:

1. Establish linear product formation with wild-type K.
2. Include no-enzyme and no-ATP/no-substrate controls.
3. Define background using the no-enzyme control.
4. Pre-specify a maximum acceptable residual signal, for example based on blank variability.

**Acceptance criterion:** kinase-dead K activity is not distinguishable from blank/background and is strongly reduced relative to wild-type K.

If kinase-dead K retains measurable activity, it should be treated as a hypomorph, not a clean catalytic-null. Generate or obtain a more severe mutant if possible.

### 4.3.4 Scaffold competence

Objective: show that kinase-dead K still performs the relevant non-catalytic interactions.

Because the exact scaffold function may be unknown, use layered assessment:

1. **Known interactors:** if K is known to bind S, receptor, or adaptor proteins, measure those interactions.
2. **Discovery interactome:** if key partners are unknown, compare wild-type and kinase-dead K by co-immunoprecipitation followed by mass spectrometry or proximity labeling.
3. **Ligand-dependent assembly:** test whether K still enters the ligand-induced signaling complex.
4. **Localization:** compare wild-type and kinase-dead K by imaging or subcellular fractionation.

Calibration:

1. Optimize lysis stringency so true interactions are retained and negative controls are absent.
2. Use negative-control beads/IgG and, if possible, a known binding-disrupted positive control.
3. Define assay variability using replicate wild-type samples.
4. Pre-specify retention criteria for key interactors.

**Acceptance criterion:** kinase-dead K retains the relevant interactome/localization within pre-specified limits. Major loss of S, receptor, or adaptor binding makes the kinase-dead rescue uninterpretable for separating catalysis from scaffold.

---

## 4.4 Independent experimental units, allocation, and blinding

### 4.4.1 Independent units

Do not treat technical wells as independent biological replicates.

Use as independent biological units:

- at least three independently derived K knockout clones or independently transduced knockout populations;
- at least three independently derived rescue lines or independent integration clones per construct, if feasible;
- separate cell thaws/passages or independent differentiation/transduction batches as experimental replicates.

If only one clone per genotype is available, the result is preliminary and should be confirmed with additional clones.

### 4.4.2 Randomization

1. Randomize plate layout across genotypes and treatments.
2. Balance groups across plate positions, incubator shelves, and processing batches.
3. Randomize order of lysis, sample loading, and imaging where feasible.

### 4.4.3 Blinding

1. Code cell lines and treatments so that operators and analysts are blinded to group identity.
2. Maintain the code until data acquisition and primary analysis pipeline are locked.
3. For image-based readouts, use automated segmentation/quantification rather than manual selection.

---

## 4.5 Interventions and sampling

## 4.5.1 Main rescue signaling experiment

Groups:

1. parental cells, vehicle;
2. parental cells, ligand;
3. K knockout + empty vector, vehicle;
4. K knockout + empty vector, ligand;
5. K knockout + wild-type K, vehicle;
6. K knockout + wild-type K, ligand;
7. K knockout + kinase-dead K, vehicle;
8. K knockout + kinase-dead K, ligand.

Optional groups:

- wild-type K rescue + ligand + selective K inhibitor;
- parental + ligand + selective K inhibitor;
- kinase-dead K rescue + ligand + inhibitor, to test additivity or off-target effects.

Procedure:

1. Seed cells at calibrated density.
2. Apply serum/starvation or resting conditions only if calibrated and kept constant.
3. Pre-treat with inhibitor or vehicle if applicable.
4. Stimulate with ligand at calibrated concentration.
5. Harvest at calibrated phospho-S peak time and, if useful, one later time point.
6. Lyse rapidly in phosphatase/protease inhibitors.
7. Randomize sample order during processing.

Measurements:

- phospho-S;
- total S;
- K abundance;
- loading control;
- optional K autophosphorylation/target-engagement marker.

Primary signaling readout:

**ligand-induced phospho-S normalized to total S**, compared across genotypes.

## 4.5.2 Growth phenotype experiment

Use the same validated rescue lines.

Procedure:

1. Seed equal numbers of viable cells based on calibrated counting.
2. Treat with vehicle or ligand at the concentration relevant to the growth phenotype.
3. Maintain conditions for the calibrated assay duration.
4. Measure growth using at least one primary method and one orthogonal method if possible.

Possible readouts:

- cell number by automated counting;
- DNA content;
- live-cell fluorescent cell tracking;
- ATP-based viability, interpreted carefully;
- clonogenic survival if appropriate;
- barcoded competition assay for subtle fitness differences.

Measurements should be taken at multiple time points to estimate growth rate, not only endpoint signal.

Primary growth readout:

**ligand-dependent growth rate or area-under-the-curve**, compared across genotypes.

## 4.5.3 Scaffold-complex sampling under functional conditions

In a subset of conditions, measure whether the kinase-dead protein remains in the ligand-induced complex.

Conditions:

- wild-type K + ligand;
- kinase-dead K + ligand;
- empty vector + ligand as negative control;
- optional inhibitor-treated wild-type K.

Measurements:

- co-immunoprecipitation or proximity assay for K with S/receptor/adaptor;
- input expression levels;
- ligand-dependent changes in complex formation.

---

## 4.6 Control set

Required controls:

| Control | Purpose |
|---|---|
| Parental cells | Reference state |
| K knockout + empty vector | Negative control for K function |
| Wild-type K rescue | Positive rescue control |
| Kinase-dead K rescue | Test construct |
| Vehicle vs ligand | Establish ligand dependence |
| Total S measurement | Ensure p-S changes are not due to S abundance |
| No-primary-antibody/isotype/beads-only | Co-IP/IP specificity |
| Wild-type K + inhibitor, if used | Orthogonal catalytic inhibition |
| Folding/stability reference samples | QC for kinase-dead folding |
| Kinase assay positive/negative controls | Confirm catalytic assay dynamic range |

If total S changes between groups, the p-S interpretation is confounded. Repeat or add orthogonal normalization.

---

# 5. Measurements

## 5.1 Signaling measurements

For each sample:

1. Quantify phospho-S.
2. Quantify total S from the same lysate.
3. Quantify K expression.
4. Normalize phospho-S to total S and loading.
5. Report absolute and normalized values.

If antibodies are limiting, use targeted mass spectrometry or validated epitope tags, but validate that the tag does not alter function.

## 5.2 Growth measurements

For each line and condition:

1. Estimate growth rate or cumulative population doubling.
2. Record viability/toxicity if available.
3. Check that differences are not explained by starting density errors.
4. If growth differences are small, use paired competition assays or longer calibrated time courses.

## 5.3 Scaffold measurements

For each relevant interaction:

1. Measure interactor abundance in IP or proximity assay.
2. Normalize to input K and total interactor.
3. Compare wild-type K versus kinase-dead K under ligand-stimulated conditions.
4. Report whether inhibitor treatment alters complex assembly.

---

# 6. Analysis plan

## 6.1 Analyze QC before functional outcomes

Before testing the main hypothesis, evaluate:

1. K knockout confirmation.
2. Reproducibility of reduced ligand-induced phospho-S and slowed growth.
3. Total S stability.
4. Wild-type rescue competence.
5. Kinase-dead expression matching.
6. Kinase-dead folding/stability.
7. Kinase-dead catalytic inactivity.
8. Kinase-dead scaffold retention.

If QC fails, do not proceed to causal interpretation.

## 6.2 Primary statistical contrasts

Use mixed-effects or blocked analysis appropriate for nested cell-line experiments.

Example structure:

- fixed effects: genotype, ligand, treatment, and interactions;
- random effects: experiment, clone, or independently derived line;
- technical wells nested within line.

Primary contrasts:

1. K knockout + wild-type K versus K knockout + empty vector.  
   Purpose: confirm rescue system works.

2. K knockout + wild-type K versus K knockout + kinase-dead K.  
   Purpose: test whether catalytic activity is required.

3. K knockout + kinase-dead K versus K knockout + empty vector.  
   Purpose: test whether kinase-dead K provides any scaffold-only rescue.

4. Wild-type K + inhibitor versus wild-type K + vehicle, if inhibitor used.  
   Purpose: orthogonal acute catalytic-inhibition test.

5. Ligand effect within each genotype.  
   Purpose: confirm ligand dependence.

Growth analysis should mirror signaling analysis using growth rate or area under the curve.

## 6.3 Decision rules

### Catalytic activity required

Conclude that K catalytic activity is required if all of the following are true:

- wild-type K rescues ligand-induced phospho-S and growth;
- kinase-dead K is expressed, folded, catalytically inactive, and scaffold-competent;
- kinase-dead K fails to rescue phospho-S and/or growth relative to wild-type K;
- kinase-dead K is statistically indistinguishable from empty vector or clearly inferior to wild-type K;
- an orthogonal catalytic inhibition approach, if available, produces a concordant reduction.

### Catalytic activity not required; scaffold sufficient

Conclude that catalytic activity is not required under the tested conditions if:

- wild-type K rescues;
- kinase-dead K is confirmed catalytically inactive and scaffold-competent;
- kinase-dead K rescues phospho-S and growth to a level not significantly below wild-type K;
- acute catalytic inhibition, if available, does not reproduce the knockout phenotype.

### Partial catalytic requirement

Conclude that catalytic activity contributes but is not the whole mechanism if:

- kinase-dead K partially rescues relative to empty vector but remains below wild-type K;
- or acute inhibition produces a partial phenotype;
- and QC supports kinase-dead protein integrity.

Possible interpretations:

- both catalytic and scaffold functions contribute;
- kinase-dead allele is hypomorphic;
- catalytic activity is required for full but not minimal signaling;
- compensatory pathways exist.

### Inconclusive

The study is inconclusive if:

- kinase-dead K is poorly expressed, degraded, misfolded, or binding-defective;
- wild-type K fails to rescue;
- total S changes substantially;
- inhibitor reduces K abundance or disrupts scaffold;
- only one clone supports the conclusion;
- kinase-dead K has residual catalytic activity that cannot be quantified.

---

# 7. Acceptance and stopping criteria

## 7.1 Go criteria for main inference

Proceed only if:

1. K knockout reproduces reduced ligand-induced phospho-S and reduced growth.
2. Total S remains unchanged across main groups.
3. Wild-type K rescues both signaling and growth.
4. Kinase-dead K passes expression, folding, catalytic, and scaffold QC.
5. Assay variability is low enough to detect the pre-specified minimum effect.

## 7.2 Stop or redirect criteria

Stop the kinase-dead rescue interpretation if:

- kinase-dead K abundance is materially lower than wild-type K and cannot be matched;
- kinase-dead K is unstable or misfolded;
- kinase-dead K loses key scaffold interactions;
- kinase-dead K retains catalytic activity;
- wild-type K rescue fails;
- ligand response is not reproducible.

Redirect to alternatives:

- endogenous catalytic-dead knock-in;
- alternative kinase-dead mutations;
- analog-sensitive K allele;
- acute K degron system;
- scaffold-defective catalytically active mutant after mapping interaction surfaces.

---

# 8. Troubleshooting

| Problem | Likely cause | Action |
|---|---|---|
| Kinase-dead K low abundance | Degradation, poor expression, tag effect | Calibrate expression; test proteasome inhibition diagnostically; change tag/promoter; generate endogenous knock-in |
| Kinase-dead K fails folding QC | Destabilizing mutation or tag | Test alternative kinase-dead residues, remove tag, use endogenous expression |
| Wild-type K fails to rescue | Overexpression toxicity, wrong isoform, clone artifact, pathway drift | Test another KO clone, reduce expression, verify construct sequence, recalibrate ligand |
| Phospho-S signal weak | Wrong ligand dose/time, assay insensitivity, phosphatase activity | Recalibrate ligand/time, improve lysis, enrich phosphopeptides, use more sensitive assay |
| Total S changes | Off-target effect, toxicity, altered S stability | Re-evaluate normalization, shorten assay, check viability, use orthogonal S measurement |
| Growth effect small/noisy | Assay duration too short, seeding error, saturation | Use calibrated exponential-phase growth assay, competition assay, more biological replicates |
| Inhibitor phenocopies KO but disrupts scaffold | Conformational/off-target effect | Do not use inhibitor alone; confirm with genetic catalytic-dead or analog-sensitive allele |
| Kinase-dead K rescues but in vitro activity assay says dead | Residual cellular activity, contaminating WT K, assay substrate mismatch, reversion | Re-sequence construct, verify KO has no endogenous K, test additional substrates/autophosphorylation |

---

# 9. Discriminating outcomes

| Outcome in validated system | Interpretation |
|---|---|
| Wild-type rescues; kinase-dead does not; kinase-dead is stable, scaffold-competent, catalytically inactive | Strong support that K catalytic activity is required |
| Wild-type rescues; kinase-dead rescues equally; kinase-dead is catalytically inactive and scaffold-competent | Catalytic activity not required; scaffold function likely sufficient under tested conditions |
| Kinase-dead partially rescues | Catalytic and non-catalytic functions may both contribute, or kinase-dead allele is partial loss-of-function |
| Kinase-dead fails but is unstable or binding-defective | Inconclusive; cannot separate catalytic from scaffold defect |
| Wild-type rescue fails | System invalid; cannot infer mechanism |
| Kinase-dead produces stronger phenotype than empty vector | Possible dominant-negative sequestration or toxic misfolding; not simple evidence for catalytic requirement |
| Selective inhibitor blocks signaling without altering K scaffold and phenocopies kinase-dead | Supports catalytic requirement |
| Selective inhibitor blocks signaling but also disrupts K complex/localization | Inhibitor evidence ambiguous; need genetic separation-of-function |

---

# 10. Alternatives and strengthening designs

## 10.1 Endogenous catalytic-dead knock-in

Generate the kinase-dead mutation at the endogenous K locus.

Advantages:

- native expression level;
- avoids overexpression artifacts;
- preserves endogenous regulation.

Limits:

- editing may be difficult;
- the mutation may still affect folding or interactions;
- chronic adaptation can occur.

## 10.2 Analog-sensitive K allele

Engineer K with a gatekeeper or analog-sensitive mutation that allows selective inhibition by a bulky ATP analog.

Advantages:

- acute catalytic inhibition;
- K protein remains present;
- useful for separating catalytic from scaffold roles.

Limits:

- the sensitizing mutation may alter kinase fitness or scaffold;
- inhibitor may change conformation;
- requires careful validation that scaffold remains intact.

## 10.3 Acute K degron

Fuse endogenous K to an inducible degron to remove the entire protein rapidly.

Advantages:

- acute loss avoids long-term compensation;
- compares protein removal against catalytic inhibition.

Limits:

- degron tag may alter K function;
- degradation may be incomplete;
- loss of protein removes both catalytic and scaffold functions, so it must be combined with catalytic-specific perturbations.

## 10.4 Scaffold-defective but catalytically active K

If K interaction surfaces can be mapped, generate K mutants that retain catalytic activity but lose binding to S, receptor, or key adaptors.

Advantages:

- directly tests whether scaffold is required.

Limits:

- interaction surface may be unknown;
- mutations may indirectly impair catalysis or folding;
- requires extensive validation.

---

# 11. Key limitations

1. **Knockout alone cannot distinguish catalytic from scaffold roles.**  
   It removes the whole protein.

2. **Kinase-dead mutants are not automatically scaffold-neutral.**  
   They may misfold, lose interactions, mislocalize, or become dominant-negative.

3. **Rescue depends on expression matching.**  
   Overexpressed kinase-dead K may force non-physiological interactions; underexpressed kinase-dead K may fail for non-catalytic reasons.

4. **Phospho-S may be indirect.**  
   K may control S phosphorylation through another kinase, localization change, or complex assembly. The study tests requirement, not necessarily direct phosphorylation.

5. **Growth phenotypes can be secondary.**  
   Growth changes may reflect toxicity, cell-cycle arrest, apoptosis, or metabolic stress. Include viability/proliferation readouts.

6. **One kinase-dead allele is insufficient for a strong claim.**  
   A second allele, endogenous knock-in, or acute catalytic inhibition is needed to rule out mutant-specific artifacts.

7. **Inhibitors can have scaffolding/conformational effects.**  
   A catalytic inhibitor may stabilize or disrupt protein complexes. Use scaffold QC after inhibitor treatment.

8. **Results may be cell-line specific.**  
   The conclusion applies to the tested cancer cell line and ligand condition unless replicated in additional models.

---

# Final minimal study design

The minimum interpretable experiment is:

1. Confirm K knockout lowers ligand-induced phospho-S and growth while total S remains unchanged.
2. Validate and expression-match wild-type and kinase-dead K in K knockout cells.
3. Confirm kinase-dead K is catalytically inactive and retains folding/scaffolding.
4. Compare ligand-induced phospho-S and growth among:
   - empty vector,
   - wild-type K rescue,
   - kinase-dead K rescue.
5. If possible, confirm with acute catalytic inhibition or endogenous catalytic-dead knock-in.
6. Interpret only if wild-type rescue works and kinase-dead QC passes.
