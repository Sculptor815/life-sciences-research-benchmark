# GPT-6 Astra / inf-d01

Original final answer, shared by both scoring rounds.

## Recommendation

Develop a **small, batch-robust molecular program using patient-level paired changes**, and evaluate it once in the untouched second cohort. Start with separate analyses of each assay, then integrate reliable signals. Treat metabolomics as provisional until its treatment–batch separation is shown to be estimable.

The main threat is not the choice of integration algorithm: **most post-treatment metabolomics samples share a batch (M2)**. Integration and batch correction cannot recover a treatment effect that is indistinguishable from a technical effect.

No measurements or results are supplied, so this is a proposed analysis protocol—not evidence that a reproducible program already exists.

## Evidence → inference → conclusion

| Evidence location | Inference | Design conclusion |
|---|---|---|
| **M1:** 30 patients sampled before and after treatment | Observations within a patient are dependent; pairing can remove stable between-patient differences | Patients—not specimens, features or technical replicates—are the independent units. Analyze within-patient change and resample whole patients |
| **M2:** RNA and protein ran in different batches | Assays need separate technical models; different batches across modalities do not alone establish treatment confounding | Normalize and assess batch effects within each assay before integration |
| **M2:** Most post-treatment metabolomics samples share a batch | Treatment timing and metabolomics batch may be strongly or completely confounded | Check identifiability explicitly. Restrict, remeasure or exclude metabolomics from treatment-effect claims if necessary |
| **M3:** Some assays are missing | Effective sample sizes differ; complete-case selection or imputation may distort the program | Characterize missingness, report contributing patients and conduct missingness sensitivity analyses |
| **M4:** A second small cohort must remain untouched | It can provide independent evidence only if development does not use it | Seal it until the feature set, processing, scoring and validation decision rules are frozen |

**Important limit:** No untreated comparator, randomization, treatment details or sampling intervals are reported. A paired difference is therefore **treatment-associated**, not necessarily treatment-caused.

# Ordered operational protocol

## 1. Preparation and quality checks

Create an auditable manifest linking:

- Patient, specimen, time point and assay identifiers.
- Assay batch, run order and technical replicate identifiers.
- Collection timing, processing and storage information, where recorded.
- Treatment exposure and deviations, where recorded.
- Missing assays, failed measurements and reasons.
- Available tumor-content or cellular-composition measurements.

These fields are requested inputs, not reported characteristics of the study.

Check sample identity, duplicate records, feature identifiers, units, detection limits and assay-specific annotation confidence. Investigate anomalous samples without assuming that a large post-treatment change is an error.

### Calibrate quality rules

Numerical thresholds are unreported. Establish them from available blanks, reference materials, pooled quality-control samples, technical replicates and platform performance information. Relevant criteria include contamination, precision, detection reliability and run-order drift.

Prefer rules derived without viewing treatment-associated feature effects. Record exclusions and their reasons; compare exclusion rates across time points and batches.

### Assess design estimability before correction

Within each assay:

1. Cross-tabulate time point against batch.
2. Identify patients whose two measurements were processed together or separately.
3. Check whether a model containing patient, time point and batch can estimate a time-point effect.
4. Inspect how much treatment information comes from a small number of overlapping batches or patients.

A technically full-rank model may still give an unstable estimate when overlap is minimal. Report uncertainty and leverage, not simply “batch adjusted.”

---

## 2. Independent units and analysis populations

The maximum biological sample size is **30 patients**, not 60 specimens or the number of molecular measurements.

- Keep every patient’s time points, modalities and technical replicates together in resampling.
- Summarize technical replicates or model their measurement error; do not count them as independent patients.
- Report the number of usable pairs for every assay, feature and integrated score.
- Distinguish the eligible cohort, assay-specific paired subsets and fully observed multimodal subset.

Paired analysis removes stable patient differences. It does **not** remove batch effects when pre- and post-treatment specimens were processed differently.

---

## 3. Allocation and blinding

### Development cohort

Use the 30-patient cohort for development. A large permanent internal holdout would leave little information for either training or evaluation; prefer patient-grouped resampling, with inner resampling only where tuning is necessary.

All learned operations must occur inside the relevant training partition:

- Normalization parameters and imputation models.
- Feature filtering based on biological variability.
- Feature selection, signs and weights.
- Integration complexity and tuning choices.

Fixed assay acceptance rules can be applied consistently across partitions.

Where feasible, perform initial technical QC with treatment labels masked. The modeling team will subsequently need time-point and batch information to distinguish biological and technical associations.

### External cohort

Keep the second cohort sealed during development, including its expression distributions and treatment-response information. Do not use it to choose features, discover assay overlap, tune normalization or select the most favorable program.

Before release, freeze a versioned analysis package and prespecify eligibility and compatibility checks. Apply those checks only after development is locked.

### Proposed remeasurement

If remeasurement is possible, balance pre- and post-treatment aliquots across new batches, randomize run order and blind laboratory staff to time point where feasible. This is a proposed technical intervention, not a reported feature of the original study.

---

## 4. Intervention and sampling

Retrieve the actual treatment, exposure duration, sampling interval and relevant co-interventions. Do not invent a uniform regimen or sampling window.

Define the estimand as:

> The average within-patient change in a prespecified molecular-program score over the observed treatment interval, among patients represented by the analysis.

If intervals vary materially, prespecify how timing will be handled. With 30 patients, elaborate response-by-time or subgroup models are unlikely to be reliable.

Assess whether recorded differences in tissue processing, anatomical sampling or tumor content could explain the observed changes. A composition-driven program may be a real feature of sampled tumors, but it is not automatically a tumor-cell-intrinsic response.

An untreated or differently treated comparator, if available in a future study, would help distinguish treatment effects from time-related changes. Its absence here limits causal interpretation.

---

## 5. Measurements and preprocessing

Process RNA, protein and metabolite data separately using transformations and normalization appropriate to their actual measurement scales. The platforms are unspecified, so no particular preprocessing method can be asserted as the original or correct method.

Operational requirements:

- Use technical controls and residual diagnostics to choose transformations.
- Do not directly pool quantities with different units.
- Learn scaling parameters from development training data.
- Separate values below detection limits from whole-assay absence and technical failure.
- Preserve uncertain metabolite identities and ambiguous mappings.
- Avoid silently collapsing distinct transcripts, proteins or metabolites into a single gene-level measurement.

### Missingness

Tabulate missingness by patient, time point, batch and assay. Determine whether missing measurements reflect random processing failures, sample quality, detection limits or other recorded causes.

Use observed paired measurements for primary feature-level change estimates where possible. A model using unpaired observations may be a sensitivity analysis, but requires explicit missing-at-random and model assumptions.

For integration:

- Prefer an observed-data method or separate assay scores when feasible.
- Do not fill an entirely absent modality with zero.
- Fit any imputation procedure within training folds and propagate its uncertainty.
- Compare results with complete-pair and missingness-restricted analyses.
- Recognize that a missing-data-capable algorithm does not solve informative missingness.

If scores with different modality availability are needed, define and evaluate each version during development. Do not silently renormalize a three-assay score into a different two-assay score.

---

## 6. Controls and confounding checks

Use available technical controls to assess contamination, drift and measurement precision. Availability is unreported.

**Proposed bridging experiment:** Remeasure stored pre- and post-treatment aliquots together in balanced batches, including common reference materials. This can help separate assay batch effects from biological change. It cannot repair collection or storage differences already confounded with time point.

For metabolomics, distinguish:

1. **Adequate time-point overlap across batches:** estimate treatment-associated change with batch adjustment.
2. **Sparse overlap:** report fragile estimates and repeat analyses in the overlapping subset.
3. **No estimable separation:** do not attribute the metabolite shift to treatment. Obtain bridging measurements or omit metabolomics from the primary treatment-associated program.

Check whether candidate scores track batch, run order, technical quality or missingness more strongly than time point. Such relationships are diagnostic warnings, not automatic proof that the signal is technical.

---

## 7. Analysis: separate effects, integrate, interpret, validate

### 7A. Estimate within-assay paired effects

For a suitably transformed feature, an illustrative model is:

\[
y_{itf}=\alpha_{if}+\beta_f\,\mathrm{Post}_{it}
+\gamma_{f,b(it)}+\epsilon_{itf}.
\]

Here, \(\alpha_{if}\) represents patient-specific baseline abundance, \(\beta_f\) the average post-treatment difference, and \(\gamma_{f,b(it)}\) an identifiable batch effect.

The likelihood and variance model must match the assay. Add only justified covariates supported by the sample size; post-treatment variables may be mediators rather than confounders.

Report effect sizes, uncertainty, contributing pairs and multiplicity-adjusted evidence. Calibrate the error-control policy before interpreting biological hits. Statistical significance without a credible effect magnitude or technical reliability is insufficient.

Do not apply a generic batch-removal procedure that can erase the time-point effect, or claim that adjustment resolves non-identifiability.

### 7B. Integrate into a parsimonious program

**Recommended primary approach: conservative late integration.** Analyze each modality first, then combine reliable information into a small signed program. This is easier to audit than a high-capacity joint model with 30 patients and incomplete assays.

Within each training partition:

1. Estimate and shrink standardized paired effects.
2. Identify features with stable direction, adequate measurement reliability and sufficient observed pairs.
3. Use molecular mappings to connect RNA, protein and metabolites, retaining mapping ambiguity.
4. Limit redundancy so that multiple measurements of one entity do not overwhelm the score.
5. Form assay-specific signed scores and combine them using fixed modality weights.

Calibrate feature count, shrinkage and weighting through internal resampling, constrained by technical reliability and stability. Do not optimize only for the largest apparent pre/post separation.

A sample-level score may take the form

\[
S_{it}=\sum_m a_m\sum_{f\in F_m}
w_{mf}\frac{x_{itmf}-\mu_{mf}}{s_{mf}},
\]

with feature sets, signs, weights, reference values, scaling and missingness rules frozen after development. The principal endpoint is the paired difference \(S_{i,\mathrm{post}}-S_{i,\mathrm{pre}}\).

If metabolomics is not identifiable, develop an RNA–protein program and label metabolomics as supplementary rather than forcing three-way integration.

**Role of integration:** establish a coherent, measurable program across molecular layers and assess shared versus assay-specific evidence. It does not establish causality or independently validate a finding.

RNA, protein and metabolite changes need not have identical directions. Interpret disagreement using pathway position, measurement uncertainty and possible timing differences; these explanations remain hypotheses.

### 7C. Test internal stability

Hold out whole patients during evaluation. Learn features, signs, scaling and weights on training patients, then calculate held-out paired score changes.

Assess:

- Stability of selected features and molecular groups.
- Direction and magnitude of held-out score changes.
- Dependence on individual patients.
- Sensitivity to complete-pair restrictions and missingness assumptions.
- Sensitivity to overlapping-batch subsets.
- Leave-one-modality-out performance.
- Batch-held-out performance where the design permits a meaningful comparison.

Do not report an ordinary paired test on the development-selected score as independent confirmation. Selection-aware inference would need to repeat the whole pipeline under an appropriate null scheme. Naive time-label shuffling is not valid when exchangeability is broken by batch structure.

### 7D. Use enrichment for interpretation

After estimating feature-level effects, perform enrichment using prespecified annotation resources, if available.

- Prefer ranked effect evidence where appropriate rather than a convenient significance cutoff.
- Use the measured, reliably testable features as the background.
- Address multiplicity and redundant pathways.
- Report which features drive each result.
- Treat ambiguous metabolite annotations explicitly.
- Distinguish increased and decreased components where meaningful.

Enrichment asks whether changes concentrate in known biological sets. It does **not** validate the score, demonstrate pathway flux or prove pathway activation.

If pathway annotations were used to construct the program, enrichment against those same annotations is partly built into the design and is descriptive. Concordant RNA and protein enrichment is useful cross-layer evidence, but neither the measurements nor the pathway annotations are independent.

### 7E. Conduct external validation once

After freezing the development package, release the second cohort.

Its paired sampling, treatment comparability and assay compatibility are unreported. Apply the prespecified checks:

- If comparable pre/post samples exist, test the frozen paired score endpoint.
- If not, report exactly which association or transportability property can be assessed; do not call it validation of paired treatment-associated change.

Use frozen feature mappings and weights. Any new-batch calibration must follow a predetermined reference-control procedure, not outcome-guided correction.

The primary validation should estimate the paired score effect and uncertainty under a prespecified batch-aware model. Assess secondary feature directions and modality contributions without demanding that every feature individually reach significance.

**Role of external validation:** test whether the frozen program generalizes beyond development patients and development selection. A second small cohort may give wide uncertainty. It also cannot resolve shared systematic confounding present in both cohorts.

---

## 8. Acceptance and stopping criteria

Set numerical criteria before unsealing the external cohort. Since assay precision, intended use and minimum meaningful effect are unreported:

- Calibrate technical thresholds from controls and repeatability.
- Define a meaningful score change from analytical precision and the scientific objective.
- Select multiplicity and confidence criteria according to the acceptable false-program claim rate.
- Calibrate internal stability criteria using development resampling and technically justified null/reference analyses.
- If several programs reach validation, prespecify their hierarchy or multiplicity correction.

Use three gates:

1. **Analytical gate:** sufficient reliable pairs and identifiable treatment–batch effects. Otherwise restrict the claim or stop that modality.
2. **Development gate:** stable held-out patient behavior, credible assay contributions and no dependence on a single patient, batch or imputation choice. Otherwise nominate no program.
3. **External gate:** the frozen program meets its prespecified direction, effect-size and uncertainty criteria in eligible independent data.

If external uncertainty is too wide, conclude **inconclusive**, not reproduced or disproved. If the program is revised after validation, it becomes a new development candidate requiring another untouched evaluation.

---

## 9. Troubleshooting and alternatives

| Problem | Response and limitation |
|---|---|
| Metabolomics separates pre/post samples almost perfectly by batch | Inspect estimability; use overlap-restricted analysis or balanced remeasurement. Do not rely on visual separation or generic correction |
| Program disappears when one patient is removed | Check technical records and quantify influence; reject or simplify if instability persists. Do not exclude solely because the patient is inconvenient |
| Complete-case and missing-data analyses disagree | Investigate missingness mechanisms; report the affected population and sensitivity range |
| One modality dominates | Revisit scaling and redundancy within development; assess leave-one-modality-out results |
| RNA and protein disagree | Consider timing, regulation, coverage and noise as hypotheses; retain layer-specific effects rather than forcing concordance |
| Enrichment is strong but the score does not replicate | Retain pathway findings as exploratory interpretation, not evidence of reproducibility |
| External processing is incompatible | Report validation as infeasible or limited; do not quietly retune the program |

A regularized joint latent-factor model is an alternative if coverage and technical quality support it. Limit complexity through internal calibration and distinguish factors explaining patient heterogeneity from a reproducible mean treatment-associated shift. With these data, late integration is the more transparent primary choice.

**Final deliverable:** an auditable paired-effect analysis, a frozen score with explicit applicability limits, enrichment-based interpretation, and an independent validation result—or a clear statement that batch confounding, missingness or insufficient precision prevents a reproducible-program claim.
