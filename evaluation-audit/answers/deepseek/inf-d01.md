# DeepSeek V4.1 Flash / inf-d01

Original final answer, shared by both scoring rounds.

## Recommended next action

Lock a pre-specified, patient-blocked multi-omic analysis plan before touching the second cohort. First audit the timepoint-by-batch cross-tab, especially for metabolomics. If post-treatment metabolomics is perfectly or near-perfectly confounded with batch and no bridging/QC samples can separate them, metabolomic treatment effects are unidentifiable; report that limit and rely on external validation or re-run a bridging subset. Otherwise, proceed with paired change scores, patient-level integration, pathway enrichment, and locked external validation in the untouched second cohort.

## Evidence-to-inference-to-conclusion chain

| Evidence | Inference | Consequence for analysis |
|---|---|---|
| M1: 30 patients with pre- and post-treatment samples | Paired design supports within-patient change estimation; n=30 limits high-dimensional discovery power | Unit of inference is the patient, not the sample. Use paired/blocked models. Treat discovery as hypothesis-generating. |
| M2: RNA and protein in different batches; most post-treatment metabolomics samples share a batch | RNA/protein batch effects may be partially separable if timepoints are balanced across batches; metabolomics time and batch may be collinear | Model batch where estimable. For metabolomics, do not interpret batch-confounded changes as treatment effects without bridging, QC drift correction, or external validation. |
| M3: some assays missing | Complete-case multi-omic analysis reduces n and may bias if missingness is non-random | Use missing-data-aware integration and sensitivity analyses. Report missingness by patient, timepoint, modality, and batch. |
| M4: second small cohort available but must remain untouched | External validation is possible but underpowered for individual features | Lock the program before validation. Validate program-level scores and pathway enrichment, not only top individual features. |
| Conclusion | A reproducible treatment-associated program requires a stable integrated signature that replicates in M4 and is not explained by batch or missingness | Claim reproducibility only if the locked program replicates in M4. Otherwise report as candidate/hypothesis-generating. |

## Estimand and design

Primary estimand: the within-patient change from pre- to post-treatment in a multi-omic program score, where the program is a coordinated set of RNA, protein, and metabolite features. Secondary estimands: modality-specific paired changes, cross-modal correlation of changes, and pathway-level changes.

This design estimates treatment-associated change, not necessarily causal treatment effect. Without an untreated or alternative-treatment control, pre-post changes may reflect tumor evolution, time, biopsy variability, or batch. External validation in an independent treated cohort strengthens reproducibility but does not by itself prove causality.

## Operational protocol

### 1. Preparation and quality checks

Create a data dictionary with patient ID, timepoint, treatment regimen, dose, cycle, biopsy site, time interval, tumor purity/histology, batch, run order, and clinical outcome if available.

Per modality:
- RNA: library size, mapping rate, ribosomal content, RIN or equivalent, 3′/5′ bias, PCA, outlier detection.
- Protein: digestion efficiency, LC-MS QC metrics, missing-value rate, intensity distribution, replicate correlation.
- Metabolite: peak picking, annotation confidence, missingness, QC drift, intensity distribution, batch/run-order effects.

Cross-tab timepoint versus batch for each modality. For metabolomics, quantify whether post-treatment samples are fully or mostly nested within one batch. If yes, batch and time are confounded.

Calibrate QC thresholds from platform QC samples and technical replicates, not from arbitrary fixed cutoffs. For example, set sample exclusion thresholds at the 95th percentile of QC-sample deviation or at a level that maximizes technical reproducibility without discarding biological signal.

Normalize each modality separately before integration. Use standard pipelines for the platform. For batch correction, consider ComBat, limma removeBatchEffect, or mixed models only when batch is estimable. For metabolomics with time-batch confounding, prefer QC-based drift correction and flag the confounding; do not apply naive batch correction that may remove treatment signal.

### 2. Independent units, allocation, blinding

Independent unit: patient. Pre- and post-treatment samples from the same patient are repeated measures. Do not treat them as independent in tests, cross-validation, or enrichment.

If prospective, randomize sample processing order across batches and timepoints where possible. Avoid placing all post-treatment samples in one batch. If retrospective, document the existing allocation and treat it as a limitation.

Blinding: analysts performing QC and unsupervised integration should be blinded to timepoint and clinical outcome where feasible. For supervised steps, use nested cross-validation with patient-grouped folds. Keep the external cohort locked and unexamined until the program is fixed.

### 3. Intervention and sampling

Treatment is the intervention. Record regimen, dose, schedule, concomitant medications, and whether treatment was neoadjuvant, adjuvant, or metastatic.

Sampling: pre-treatment sample before first dose; post-treatment sample at a pre-specified time or clinical milestone. Standardize biopsy site, cold ischemia time, preservation, and handling. If timing varies, include time interval as a covariate and perform sensitivity analysis restricted to a narrow window. Calibrate the acceptable window from the observed distribution and from prior technical variability.

### 4. Measurements

RNA: bulk RNA-seq or array. Quantify, filter low-expression features, normalize, and transform as appropriate for the platform.

Protein: mass spectrometry or antibody-based. Filter low-confidence proteins, log-transform, normalize, and handle missing values.

Metabolite: LC-MS, GC-MS, or NMR. Annotate features at known confidence levels, normalize, and impute or model missingness.

Calibration for unknown platforms: use pooled QC samples, spike-ins, reference standards, and technical replicates to estimate coefficient of variation, batch effects, and detection limits. Use these to set feature filters and normalization choices.

### 5. Controls

Technical controls: blanks, pooled QC samples, reference standards, randomized run order, and technical replicates.

Biological controls: pre-treatment samples serve as within-patient controls. If adjacent normal tissue is available, use it to estimate tumor purity and baseline tissue effects. There is no untreated control in M1, so treatment cannot be fully separated from time.

Batch controls: include QC samples in every batch. If possible, include bridging samples that appear in multiple batches. For metabolomics, bridging pre-treatment samples into the post-treatment batch or post-treatment samples into the pre-treatment batch is the cleanest way to estimate batch separately from time.

### 6. Analysis

#### Step A: Modality-specific paired analysis

For each modality, compute a paired change score per patient per feature: Δ = post − pre, or log(post/pre) for positive intensities. Use paired tests or linear models with patient as the unit. For RNA and protein, limma or mixed models can account for patient pairing and covariates. For metabolites, paired t-tests, Wilcoxon tests, or mixed models are options.

Include covariates where estimable: tumor purity, cellular composition, time interval, treatment regimen, and batch. For metabolomics, if batch is confounded with time, batch cannot be included as an ordinary covariate; estimate it only from QC/bridging samples or leave it unresolved.

Apply FDR correction within each modality. Report effect sizes and confidence intervals, not only p-values.

#### Step B: Integration

Goal: identify latent factors or multi-omic programs that capture coordinated changes across RNA, protein, and metabolites.

Options:
- MOFA+ on pre/post samples with RNA, protein, and metabolite views. Include patient as a group/random effect and batch as a covariate where estimable. Factors that differ pre versus post are candidate programs.
- DIABLO or multi-block sPLS-DA to classify pre versus post using all modalities, with leave-one-patient-out cross-validation.
- JIVE, iCluster, or MFA for unsupervised joint dimension reduction on Δ matrices.
- Bayesian factor models or sparse canonical correlation analysis for cross-modal covariance.

Use stability selection or bootstrap resampling by patient. Retain features whose selection frequency exceeds a threshold calibrated from permutation null data. Define a program score as a weighted sum of top features per modality or as a factor score. Lock the weights and thresholds before external validation.

Critical point: integration does not create independence. If the program is selected using all 30 patients, its apparent association with treatment is optimistic. Use nested cross-validation: inner folds select features and parameters; outer folds estimate the treatment association. Report the cross-validated performance.

#### Step C: Enrichment

After the program is defined, annotate it:
- RNA and protein: GSEA, ORA, or similar with pre-specified gene sets such as Hallmark, KEGG, or Reactome.
- Metabolites: MSEA, mummichog, or joint pathway analysis with metabolite sets.
- Cross-modal: test whether the same pathways are enriched across modalities. Use Fisher, Stouffer, or joint pathway methods.

Enrichment is interpretation, not discovery. Do not use enrichment results to re-select features and then test the same features in the same data. If enrichment is used to reduce dimensionality, do it within cross-validation folds. Report pathway-level effect sizes and FDR.

#### Step D: External validation

Before touching M4, lock the program: feature list, weights, score formula, normalization, and acceptance thresholds.

Apply the locked program to M4:
- Compute program scores for each sample.
- If M4 has paired pre/post samples, test the change with the same direction and paired model.
- If M4 is unpaired or has different timepoints, compare groups or use the closest available design.
- If M4 lacks some modalities, validate the available modalities and test cross-modal consistency.

Metrics: effect size, 95% CI, p-value, sign consistency of core features, correlation of program scores with the discovery cohort, and replication of pathway enrichment.

Because M4 is small, prioritize program-level and pathway-level replication over individual feature replication. Pre-specify success criteria and calibrate them using permutation and power simulation based on the discovery effect size and M4 sample size.

### 7. Acceptance and stopping criteria

Discovery acceptance:
- Integrated factor or program score shows a paired treatment association after FDR correction.
- Program features are stable across patient-bootstrap resampling.
- Enrichment is coherent across at least two modalities.

Validation acceptance:
- Locked program score changes in the same direction in M4.
- 95% CI for the change excludes zero, or the pre-specified Bayesian probability of a same-direction effect exceeds a calibrated threshold.
- Core feature sign consistency and pathway enrichment replicate above a pre-specified, calibrated level.

Stopping rules:
- Stop and report inconclusive if metabolomics time-batch confounding cannot be resolved and no external validation can separate them.
- Stop if a modality has excessive missingness that cannot be modeled, calibrated from the missingness pattern and sensitivity analyses.
- Stop if the program fails external validation. Do not claim reproducibility.
- Stop if the program is driven by a single patient, a single batch, or a single modality.

### 8. Troubleshooting

Batch confounding: use bridging samples, QC-based drift correction, or external validation. If none are possible, report metabolomic treatment effects as confounded.

Missing data: use multiple imputation for missing features, missing-view integration such as MOFA, or complete-case analysis as sensitivity. Compare missingness by timepoint and batch.

Outliers: use robust normalization, winsorization, or sensitivity analysis excluding outliers. Do not remove samples solely to improve significance.

Small n: use regularization, pathway-level scores, stability selection, and simple models. Avoid deep learning or complex interaction models.

Heterogeneity: if clinical response data are available, test whether the program differs by response. If not, report heterogeneity as an uncertainty.

Tumor purity and cellularity: deconvolve RNA, adjust protein and metabolite analyses where possible, and include purity as a covariate. Metabolite deconvolution is limited; state that.

Multiple testing: use hierarchical FDR within modality, then across integrated factors or pathways.

## Alternatives and limits

Alternatives:
- Analyze each modality separately first, then test cross-modal correlation of paired changes.
- Use supervised integration to classify pre versus post, but only with nested cross-validation.
- Use pathway-level scores as the primary program to improve stability and external validation.

Limits:
- n=30 limits discovery power and stability.
- No untreated control means treatment-associated changes may reflect time, tumor evolution, or biopsy effects.
- Metabolomics batch-time confounding may make treatment effects unidentifiable.
- Missing assays may bias complete-case analyses.
- M4 is small, so external validation may be underpowered for individual features.
- Tumor purity and cellular composition can confound all modalities.

## Assumptions and calibration for unreported parameters

Assumptions: samples are correctly paired; missingness is at random or can be modeled; batch effects are estimable; M4 is comparable to M1.

Calibration procedures for unknowns:
- Batch effect magnitude: estimate from QC and bridging samples; if no overlap, cannot separate.
- Missingness threshold: vary the threshold and report sensitivity; do not hard-code.
- Stability selection cutoff: use permutation null distribution.
- Program score weights: derive in discovery and lock before validation.
- External validation power: simulate using observed discovery effect sizes and M4 sample size.
- Normalization choice: compare methods by QC reproducibility and cross-validation stability.

## Bottom line

Integration discovers a candidate multi-omic program; enrichment interprets it; external validation tests reproducibility. The patient is the independent unit. Metabolomics batch-time confounding is the most consequential threat. If it cannot be resolved, the metabolomic component of any treatment-associated program is not identifiable from M1 alone. A reproducible program can be claimed only if a locked, patient-blocked program replicates in the untouched second cohort.
