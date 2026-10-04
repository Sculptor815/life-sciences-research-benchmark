# Qwen3.8 Max (0902) / inf-d01

Original final answer, shared by both scoring rounds.

## Recommended conclusion

Use the 30 paired pretreatment/post-treatment tumors as the **development cohort** and identify the treatment-associated program primarily from **within-patient paired changes**, not from raw cross-sectional omic values. Build a locked, multi-omic feature set or pathway-level score in the 30-patient cohort, then test it once in the untouched second cohort. Treat metabolomics with special caution: because most post-treatment metabolomics samples share one batch, metabolite changes are at high risk of being batch artifacts unless batch and treatment are demonstrably separable. If they are not separable, metabolomics should be excluded from primary discovery or used only as supportive/exploratory evidence.

The reproducible claim should be based on three distinct steps:

1. **Integration**: combine RNA, protein and metabolite measurements to find coordinated changes that are more stable than any single assay.
2. **Enrichment**: interpret the coordinated changes using predefined biological pathways or networks; enrichment explains the program but does not by itself prove reproducibility.
3. **External validation**: test the locked program in the independent cohort; this is the main evidence that the program is reproducible.

---

## Evidence-to-inference-to-conclusion chain

| Evidence | Inference | Consequence for analysis |
|---|---|---|
| **M1**: Thirty patients have pretreatment and post-treatment samples. | Each patient provides a natural paired contrast. Baseline biological differences between patients are largely controlled by using post minus pretreatment changes. | The primary biological unit is the **patient-specific paired change**. Paired tests or paired-effect models are preferred over unpaired comparisons. |
| **M2**: RNA and protein were run in different batches; most post-treatment metabolomics samples share a batch. | Batch effects can mimic treatment effects. For metabolomics, if post-treatment status and batch are nearly collinear, statistical adjustment cannot reliably separate treatment from batch. | Tabulate batch by timepoint for each omic. Adjust for batch only where estimable. Downgrade or exclude metabolomics if batch is confounded with treatment. |
| **M3**: Some assays are missing. | Missingness may reduce power and may bias results if missingness depends on treatment, sample quality or biological state. | Define feature- and sample-completeness rules. Use methods that tolerate missingness where appropriate, but do not impute systematically absent assays as if they were missing at random without checking. |
| **M4**: A second small cohort is available but must remain untouched during development. | The second cohort is the independent validation set. Using it during model building would invalidate reproducibility claims. | Freeze all preprocessing, feature selection, weights, thresholds and acceptance criteria before validation. Test the validation cohort once. |

---

## Roles of integration, enrichment and external validation

### Integration

Integration is the step that asks whether RNA, protein and metabolite changes form a **coordinated program** rather than isolated assay-specific changes. It is useful because individual omic features are often noisy, and reproducible biology is more likely to appear as concordant changes across layers.

Integration should not be used to erase known design problems. If a batch effect is confounded with treatment, integration cannot make the result causal or reproducible. Integration should be performed after per-omic quality control and batch assessment.

### Enrichment

Enrichment tests whether the treatment-associated features are concentrated in predefined biological sets, such as pathways, complexes, metabolic reactions or regulatory programs. It serves three purposes:

- reduces dependence on individual unstable features;
- provides biological interpretation;
- increases the chance of validating a reproducible signal when individual molecules differ across platforms.

Enrichment is not a substitute for external validation. A pathway can be enriched by chance or by batch-correlated features. Validation must therefore test either the program score, the directionality of core features, or the pathway-level signal in the independent cohort.

### External validation

External validation is the decisive reproducibility test. The second cohort must not be used to choose features, tune parameters, decide whether metabolomics are reliable, or refine the pathway definition. The validation question should be:

> Does the locked program show the same treatment-associated direction and magnitude in independent paired samples?

Because the validation cohort is small, validation should focus on aggregate evidence: a program score, a signed pathway score, or sign concordance among core features, rather than requiring every individual feature to replicate.

---

## Assumptions and unreported parameters requiring calibration

The following parameters are not specified in the evidence packet and should not be invented. Each requires a calibration or diagnostic procedure.

1. **Batch/timepoint balance**
   - Unknown: whether each omic batch contains both pretreatment and post-treatment samples.
   - Calibration: cross-tabulate batch by timepoint for RNA, protein and metabolites. If a batch contains only one timepoint, mark that omic as confounded for that comparison.

2. **Missingness mechanism**
   - Unknown: whether missing assays are random, due to low sample quality, below detection limit, or related to treatment.
   - Calibration: compare missingness rates by timepoint, sample quality metrics, patient characteristics and total signal. If missingness differs strongly by timepoint, treat affected features as high risk.

3. **Minimum number of paired observations per feature**
   - Unknown: how many complete pairs are needed for stable estimation.
   - Calibration: repeat feature selection using several minimum-pair thresholds. Use paired-label permutation to estimate null discoveries and bootstrap resampling to estimate selection stability. Choose a threshold where observed discoveries exceed the permutation null and selection stability improves.

4. **Number of features or components in the integrated program**
   - Unknown: how sparse the model should be.
   - Calibration: use nested cross-validation with patients as the resampling unit. Compare candidate sparsity levels and choose the simplest model whose performance is within one standard error of the best and clearly exceeds permuted-label controls.

5. **Stability-selection threshold**
   - Unknown: how often a feature must be selected before being retained.
   - Calibration: run the full pipeline on bootstrap resamples and on permuted paired labels. Retain features whose selection frequency exceeds the upper percentile of the permutation null, or control empirical false-discovery rate using the permutation distribution.

6. **Acceptable technical variation**
   - Unknown: acceptable replicate coefficient of variation, drift, or batch effect size.
   - Calibration: use pooled quality-control samples, technical replicates, extraction blanks, internal standards and reference materials. Accept correction only if it reduces batch association or QC variation without degrading replicate concordance.

7. **Validation success threshold**
   - Unknown: how much replication is sufficient in a small cohort.
   - Calibration: define aggregate tests and use binomial or permutation nulls. For sign concordance, calculate the number of core features that must show the same direction under a binomial null probability of 0.5 at the chosen error rate. For a program score, use a paired test with a pre-specified one-sided error rate.

---

## Operational ordered protocol

### 1. Pre-registration and analysis lock

Before looking at validation data:

1. Write an analysis plan specifying:
   - primary omics and fallback omics;
   - feature inclusion rules;
   - batch-adjustment strategy;
   - paired statistical model;
   - integration method;
   - enrichment gene sets or pathway databases;
   - program score definition;
   - validation hypothesis and acceptance criteria.

2. Freeze the development-cohort feature list, normalization parameters, weights and scoring formula.

3. Record code version and random seeds.

The untouched cohort is not used for any of these decisions.

---

### 2. Independent units

The independent biological unit is the **patient**, not the assay, aliquot, batch or technical replicate.

Consequences:

- paired pretreatment/post-treatment samples from one patient are not independent;
- technical replicates inform measurement error only;
- cross-validation, bootstrap and permutation must resample patients or patient pairs;
- validation success must be assessed at the patient-pair level.

For permutation testing, permute the pretreatment/post-treatment labels within patients, or equivalently randomly flip the signs of paired differences, to preserve the paired structure.

---

### 3. Allocation and blinding

If samples have already been collected and assayed, allocation is retrospective. The goal is to document and, where possible, correct design imbalance.

For any remaining or repeat assays:

1. Randomize sample run order within batches.
2. Balance pretreatment and post-treatment samples across batches.
3. Include pooled reference or bridge samples in every batch.
4. Keep the analyst blinded to validation cohort identity until the locked analysis is run.
5. If clinical variables other than treatment timing exist, keep them masked during feature selection unless they are pre-specified covariates.

For the existing data:

- document whether pretreatment and post-treatment samples were randomized across extraction, library preparation, plate and instrument batches;
- if not, treat batch as a potential confounder.

---

### 4. Intervention and sampling

The biological question is treatment-associated change, so sampling must be interpretable as pretreatment versus post-treatment.

Record or calibrate:

- time of treatment;
- time of biopsy relative to treatment;
- biopsy site and tumor cellularity;
- ischemia time, preservation method and storage conditions;
- sample quality indicators for each omic.

If biopsy timing or tumor cellularity differs systematically between pretreatment and post-treatment samples, treatment-associated changes may be confounded with tissue composition or handling. If pathology estimates are available, include tumor cellularity as a sensitivity covariate or restrict analysis to samples within an acceptable range. If no acceptable range is known, estimate the relationship between cellularity markers and principal components and document whether the program is sensitive to this adjustment.

---

### 5. Measurements and quality controls

Use separate quality-control standards for each omic.

#### RNA

Minimum QC diagnostics:

- library size and sequencing depth;
- mapping rate;
- ribosomal RNA or mitochondrial RNA fraction;
- gene-body coverage or equivalent integrity metric;
- number of detected genes;
- outlier status in principal component analysis.

Controls:

- external RNA spike-ins if available;
- reference RNA sample run across batches;
- technical replicates if available.

Normalization:

- use a count-based normalization appropriate to the assay, such as library-size normalization and variance-stabilizing transformation for sequencing, or robust quantile normalization for array-like data.
- calibrate normalization by checking that QC replicates cluster together and that global intensity distributions are comparable across samples without removing known biological differences.

#### Protein

Minimum QC diagnostics:

- total signal or peptide amount;
- missingness by sample;
- intensity distribution;
- reference pooled sample stability;
- batch and plate effects in principal component space.

Controls:

- pooled reference sample in every batch;
- technical replicates;
- blank or negative-control samples;
- known positive-control proteins if treatment biology is partly known.

Normalization:

- use median, quantile, variance-stabilizing or reference-sample normalization depending on platform.
- calibrate by minimizing variation among pooled QC samples while preserving correlation among technical replicates.

#### Metabolites

Minimum QC diagnostics:

- peak detection and annotation confidence;
- blank contamination;
- internal-standard recovery;
- retention-time or mass accuracy drift;
- pooled QC stability;
- batch distribution relative to pretreatment/post-treatment status.

Controls:

- extraction blanks;
- pooled QC samples;
- internal standards across chemical classes;
- reference materials or calibration standards if available;
- injection-order records.

Normalization:

- normalize to internal standards and pooled-QC drift correction where appropriate.
- calibrate drift correction using only QC samples, then verify that technical replicate correlation improves and that blanks do not generate false biological signal.

Because most post-treatment metabolomics samples share one batch, metabolomics requires an additional gate before primary use:

> Metabolomics may enter primary discovery only if batch is not collinear with treatment, or if QC and bridge samples demonstrate that the apparent treatment effect is not explained by batch.

If this condition fails, metabolomics is exploratory only.

---

### 6. Feature definition and missing-data handling

For each omic:

1. Create a feature-by-sample matrix.
2. Record which features are missing and why, if known.
3. Separate three types of missingness:
   - feature not measured in any sample;
   - feature measured but below detection in some samples;
   - sample failed for that omic.

Feature inclusion should be calibrated, not arbitrary. Procedure:

1. For a grid of minimum complete-pair requirements, estimate paired effects.
2. Repeat under permuted paired labels.
3. Choose the minimum-pair requirement where true-label discoveries are stable and exceed the permutation null.

For missing values:

- Do not impute a feature that is systematically absent in one condition unless there is strong evidence that absence is technical.
- For low-abundance values below detection, use censored-data-aware methods or conservative imputation only after checking technical replicates and negative controls.
- For primary analysis, prefer complete-pair feature tests or mixed models that explicitly handle missingness over unconditional imputation.

For patient-level integrated scores:

- compute the score only for patients with enough observed core features;
- calibrate the minimum observed fraction by masking core features in the development cohort and checking whether the score remains stable;
- if too many core features are missing, switch to pathway-level scoring or reduce the core program.

---

### 7. Batch diagnostics and batch correction

For each omic:

1. Cross-tabulate batch against pretreatment/post-treatment status.
2. Test whether batch explains major variation using PCA, variance partitioning or mixed models.
3. Examine whether paired differences correlate with batch.

Cases:

#### Batch is balanced across timepoints

If batches contain both pretreatment and post-treatment samples, include batch as a covariate or use a standard batch-correction method appropriate to the platform.

Examples:

- linear mixed model with batch as fixed or random effect;
- empirical Bayes batch adjustment if design is balanced;
- regression of batch effects from transformed features only when treatment is not confounded.

Acceptance check:

- batch association decreases;
- paired treatment signal remains;
- QC replicates remain consistent;
- negative controls do not acquire false time-associated signals.

#### Batch is partially confounded

If some but not all post-treatment samples are in one batch:

- estimate treatment effect using the subset where batch and time are separable;
- perform sensitivity analysis excluding the dominant batch;
- require that findings are not driven only by the confounded subset.

#### Batch is almost completely confounded

This is the key metabolomics risk. If nearly all post-treatment metabolomics samples are in one batch:

- do not claim metabolite changes are treatment-associated from those data alone;
- exclude metabolomics from primary program discovery, or restrict it to a balanced subset if one exists;
- use metabolite information only as supportive if the same pathway is independently supported by RNA or protein;
- consider targeted re-measurement of metabolites in a balanced design.

---

### 8. Primary paired feature analysis

For each retained feature, estimate the within-patient treatment-associated change.

Simple paired model:

\[
d_{if} = y_{i,post,f} - y_{i,pre,f}
\]

where \(d_{if}\) is the paired difference for patient \(i\) and feature \(f\). Test whether the mean of \(d_{if}\) differs from zero using a paired test or empirical Bayes moderated paired model.

If batch or covariates must be included, use a model such as:

\[
y_{itf} = \mu_f + \beta_f \cdot post_{it} + \gamma_f \cdot batch_{it} + b_i + \epsilon_{itf}
\]

where \(b_i\) is a patient random effect. The treatment-associated effect is \(\beta_f\). If \(\beta_f\) is not identifiable because batch and post-treatment status are collinear, the feature cannot support primary inference for that omic.

For each omic:

- estimate signed effect size and uncertainty;
- adjust for multiple testing within the omic using false-discovery control;
- record direction of change;
- identify features whose estimated change is robust to exclusion of individual batches or patients.

Do not select the final program using unadjusted per-feature p-values alone. With 30 patients, feature-level selection can be unstable.

---

### 9. Integration and construction of a treatment-associated program

Integration should be performed on paired changes or on batch-adjusted values with patient pairing preserved.

A robust workflow is:

#### Step 9.1: Standardize features

Within each omic, transform features to comparable scales, for example robust z-scores. Do not combine raw RNA, protein and metabolite intensities directly.

#### Step 9.2: Estimate patient-level paired change profiles

For each patient, compute standardized post minus pretreatment changes for retained features. The resulting matrix has patients as rows and features as columns.

#### Step 9.3: Identify coordinated components

Use a paired-aware multi-omics dimension-reduction method. Suitable classes of methods include:

- multilevel sparse partial least squares or multi-block regression for paired designs;
- multi-omics factor models that allow covariates and missing views;
- consensus PCA or factor analysis on paired change matrices.

The component of interest should represent coordinated post-treatment shift across patients and omics.

#### Step 9.4: Select core features by stability

Because 30 patients is small, use stability selection:

1. Resample patients with replacement many times.
2. In each bootstrap sample, repeat paired feature ranking and component fitting.
3. Record how often each feature contributes to the treatment-associated component.
4. Compare selection frequencies to a permutation null where paired labels are shuffled.

Retain features whose stability exceeds the calibrated null threshold.

#### Step 9.5: Define a program score

A simple and less overfit score is an unweighted signed score:

\[
Score_i(t) = \frac{1}{|C|} \sum_{f \in C} s_f z_{if}(t)
\]

where \(C\) is the core feature set and \(s_f\) is the sign of the feature’s treatment-associated change in the development cohort.

The paired program change is:

\[
\Delta Score_i = Score_i(post) - Score_i(pre)
\]

If weighted loadings are used, they must be frozen after development and not tuned in validation.

#### Step 9.6: Check overfitting

Before validation:

- test the program score in leave-one-patient-out or cross-validated paired discrimination;
- compare performance against permuted paired labels;
- ensure the program is not driven by one batch, one patient or one omic;
- verify that the score change remains after excluding metabolomics if metabolomics are batch-confounded.

---

### 10. Enrichment and biological interpretation

Enrichment should be performed after the core program or ranked feature list is defined.

Steps:

1. Rank features by signed paired evidence, for example signed effect size or signed moderated statistic.
2. Test enrichment against predefined sets:
   - pathway databases;
   - metabolic reaction sets;
   - protein complexes;
   - transcriptional regulatory programs;
   - disease or hallmark sets, if relevant.
3. Use the set of measured features as the background, not all possible genes or metabolites.
4. Map metabolites to genes, reactions or pathways only using confident annotation. Exclude ambiguous metabolite identifiers from primary interpretation.
5. Control false discoveries across pathway tests.

For multi-omic interpretation:

- test enrichment separately within RNA, protein and metabolites;
- prioritize pathways that show concordant enrichment in at least two omics;
- construct pathway-level signed scores using only features mapped to the pathway.

Enrichment can support the biological plausibility of the program, but the final reproducibility claim should still depend on external validation.

---

### 11. External validation in the untouched cohort

Validation must occur only after the program is locked.

#### 11.1: Apply the same preprocessing logic

For the validation cohort:

- perform the same QC checks;
- normalize using the same general procedure;
- map features to the locked core program;
- do not reselect features or retrain weights.

If the validation cohort uses a different platform, map to the closest shared features or to pathway-level features.

#### 11.2: Compute the locked program score

Use the frozen signs or weights to compute pretreatment and post-treatment program scores. If many core features are missing, predefine one of two fallback strategies:

1. use the subset of available core features if enough are observed, where “enough” is calibrated from development by masking experiments;
2. or switch to the corresponding pathway-level score if the core feature overlap is too low.

This fallback must be specified before validation.

#### 11.3: Primary validation test

The primary validation hypothesis is:

> The locked program changes in the same direction after treatment in the independent cohort.

Test \(\Delta Score_i\) with a paired one-sided test or exact signed-rank test if the validation cohort is very small. The error rate should be pre-specified or calibrated.

#### 11.4: Secondary validation evidence

Secondary evidence may include:

- sign concordance among core features;
- enrichment of the development-ranked program among validation-ranked features;
- replication of top pathways;
- meta-analysis of paired effects across development and validation cohorts.

For sign concordance, use a binomial calibration. If the program has \(K\) core features, under the null each feature has probability 0.5 of changing in the expected direction. Choose the minimum number of concordant features required to achieve the desired null error rate.

#### 11.5: Interpretation rules

Accept the program as reproducible only if:

- the primary aggregate validation test is positive in the expected direction at the calibrated threshold; and
- the program is not explained by a validation batch artifact; and
- secondary evidence is directionally consistent.

If only the secondary evidence is positive but the primary aggregate test is not, classify the result as hypothesis-generating, not validated.

---

### 12. Acceptance and stopping criteria

#### QC acceptance

Proceed only if:

- sufficient samples pass per-omic QC;
- technical replicates show acceptable measurement reproducibility, as calibrated from QC data;
- batch metadata are complete;
- negative controls do not show strong spurious time effects.

If metabolomics QC shows that post-treatment status is inseparable from batch, stop metabolomics primary discovery.

#### Development acceptance

Accept a candidate program only if:

- it is based on features with enough paired observations, as calibrated by stability and permutation;
- it shows stability across bootstrap resamples;
- it remains after excluding high-risk batches;
- its cross-validated performance exceeds permuted-label controls;
- its biological interpretation is not dependent on ambiguous metabolite annotations.

If no stable program emerges, do not force a conclusion. Report the absence of a reproducible signal or reduce the scope to single-omic or pathway-level hypotheses.

#### Validation acceptance

Accept validation if:

- the locked program score changes in the expected direction with statistical evidence beyond the calibrated null;
- or, if the validation cohort is too small for a powerful score test, the pre-specified pathway-level or sign-concordance criterion is met and the direction is consistent.

If validation fails:

- do not retrain using validation data;
- report the failure transparently;
- if additional independent data become available, repeat validation with a new locked version.

---

### 13. Troubleshooting

#### Problem: metabolomics batch is confounded with treatment

Actions:

- remove metabolomics from primary discovery;
- analyze only metabolites measured in balanced batches, if any;
- use pathway-level support from RNA and protein;
- plan targeted re-measurement with randomized pretreatment/post-treatment balance.

#### Problem: RNA and protein batches differ

Actions:

- analyze each omic separately before integration;
- adjust for batch within each omic if estimable;
- integrate at the level of paired effect sizes or pathway scores rather than raw values.

#### Problem: many missing assays

Actions:

- determine whether missingness is associated with timepoint or sample quality;
- restrict primary analysis to features with calibrated minimum paired completeness;
- use missing-tolerant latent models only if missingness appears technical;
- avoid imputing entire missing omic blocks.

#### Problem: feature selection is unstable

Actions:

- reduce dimensionality by using pathways instead of individual molecules;
- increase stability by requiring cross-omic or cross-pathway support;
- use unweighted program scores rather than heavily weighted models;
- report uncertainty and do not claim a precise feature-level program.

#### Problem: validation cohort is too small

Actions:

- prioritize aggregate program or pathway tests;
- use exact paired tests appropriate for small samples;
- interpret feature-level replication cautiously;
- if possible, combine validation with future cohorts in a pre-specified meta-analysis, but do not reuse the same validation cohort for training.

#### Problem: enrichment gives many weakly supported pathways

Actions:

- require enrichment to be based on measured-feature background;
- prioritize pathways with concordant multi-omic support;
- treat enriched but unvalidated pathways as exploratory.

---

## Alternatives and limits

### Alternatives

1. **Pathway-first rather than feature-first program**
   - Define treatment-associated pathway scores per omic, then require concordant pathway changes across omics.
   - This is more robust when individual features are unstable.

2. **Latent factor integration**
   - Use multi-omics factor models that handle missing views and covariates.
   - Useful if missingness is moderate and batch is not confounded.
   - Requires careful checking that factors represent treatment change, not batch.

3. **Single-omic fallback**
   - If metabolomics are unusable and protein data are sparse, define the program from RNA alone and treat other omics as supportive.
   - A reproducible single-omic program is preferable to an overinterpreted multi-omic program.

4. **Targeted validation**
   - If the discovery program is reproducible but broad, design a targeted panel of RNA/protein/metabolite assays for future validation.
   - The targeted assay should be randomized across batches and include pretreatment/post-treatment balance.

### Limits

- **Treatment-associated does not prove treatment-caused.** Without an untreated longitudinal control, changes may reflect time, biopsy effects, supportive care or disease evolution.
- **Batch confounding can be fatal.** If post-treatment status and batch are collinear, no statistical method can fully recover the treatment effect.
- **Small sample size limits feature-level reproducibility.** A stable pathway-level program is more plausible than a stable list of individual genes, proteins and metabolites.
- **Missing assays may bias results.** If missingness depends on biology, complete-case or imputed analyses may both fail.
- **Validation power may be low.** A negative validation may mean absence of effect or insufficient power; calibration and confidence intervals should be reported.
- **Metabolite annotation uncertainty.** Weakly identified metabolites can create false pathway enrichment; only confident annotations should drive primary conclusions.

---

## Final recommended workflow in brief

1. Use the 30 paired tumors as development data.
2. QC each omic separately.
3. Tabulate batch versus timepoint.
4. Exclude or downgrade any omic whose treatment contrast is confounded with batch, especially metabolomics.
5. Estimate paired feature effects using patient as the independent unit.
6. Use stability selection and paired-aware integration to define a core multi-omic program.
7. Interpret the program with pathway enrichment using measured features as background.
8. Lock the program score or pathway signature.
9. Test it once in the untouched validation cohort using paired directional hypotheses.
10. Claim reproducibility only if the locked program passes pre-specified, calibrated validation criteria.
