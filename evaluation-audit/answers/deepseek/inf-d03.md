# DeepSeek V4.1 Flash / inf-d03

Original final answer, shared by both scoring rounds.

All items below are **proposed**; no experiments or analyses have been performed. Exact donor/animal numbers, cells/fields per donor, effect sizes, ICCs, and variance components are unavailable and must be calibrated rather than assumed.

## Bottom line

Treat the **donor or animal** as the experimental unit and the **cell or field** as an observational/subsampling unit. The primary treatment inference should be at the donor/animal level, using either:

1. **Pseudobulk donor-level comparison** — aggregate cells/fields per donor, then compare donors between arms; or
2. **Hierarchical/mixed model at the cell/field level with donor as a random effect** — treatment is a donor-level covariate, and inference uses donor-level uncertainty.

Support this with **grouped resampling at the donor/animal level**, **null calibration by permuting treatment labels across donors/animals**, **held-out validation across donors/animals**, and explicit reporting of **both randomized-unit counts and observed-cell counts**. Cell-level p-values may be reported only as secondary/conditional evidence, not as independent treatment replication.

## Evidence-to-inference-to-conclusion chain

| Evidence from fixed packet | Inference | Protocol consequence | Conclusion |
|---|---|---|---|
| Randomized treatment level defines the experimental unit. | Treatment assigned to donor/animal makes donor/animal the unit of treatment inference. | Randomize and analyze at donor/animal level; cells/fields are nested subsamples. | Primary estimand is a donor-level treatment effect. |
| Observational and biological units can differ. | Many cells/fields per donor are observations, not independent biological replicates. | Model hierarchy: cells/fields within donor/animal; report both counts. | Do not treat cell/field n as treatment n. |
| Very small independent n affects precision and robustness but does not automatically invalidate every model-based test. | Small donor/animal n constrains power and stability, but model-based or resampling tests may still be informative if calibrated. | Calibrate power, ICC, and operating characteristics; use resampling and sensitivity analyses. | Report uncertainty and limitations; avoid overclaiming from small donor n. |
| Clustering may alter uncertainty without changing a point estimate. | Naive and hierarchical point estimates may be similar, but SEs/CIs can differ substantially. | Use cluster-robust/hierarchical SEs, grouped bootstrap, and permutation. | Judge by calibrated CIs and effect sizes, not by naive p-values alone. |
| High ICC or loss of significance alone does not prove a false biological effect. | A non-significant cell-level test or high ICC is not proof of no effect. | Do not declare null solely from significance loss; use effect sizes, CIs, null calibration. | Biological interpretation must separate treatment effect from cell-level noise. |

The chain is: the randomized unit defines the inferential unit → cells/fields are dependent subsamples → naive cell-level replication inflates precision and can misstate significance → primary analysis must be donor/animal-level, with grouped resampling and null calibration → conclusions are about donor/animal treatment effects, with cell-level results conditional and exploratory unless separately justified.

## 1. Definitions and estimand

- **Experimental unit / randomized unit:** donor or animal.
- **Observational unit:** cell, field, image, well, or technical measurement.
- **Biological unit:** the donor/animal whose biology is being treated.
- **Primary estimand:** effect of treatment assigned at donor/animal level on a donor-level outcome summary or on the donor-level treatment coefficient in a hierarchical model.
- **Secondary estimand:** cell-level or field-level effects conditional on donor/animal, useful for mechanism but not by itself for population treatment inference.
- **Reported counts:** number of randomized donors/animals per arm; number of observed cells/fields per donor and total; number analyzed; number excluded and why.

All above are proposed definitions to be pre-registered.

## 2. Preparation and quality checks

**Proposed preparation**

1. Pre-register the primary outcome, cell/field definition, sampling frame, exclusion rules, primary model, resampling scheme, null calibration, and validation plan.
2. Pilot or calibrate unknown parameters: donor/animal-level variance, ICC, average cells/fields per donor, batch effects, treatment effect size, and missingness.
3. If pilot data are unavailable, perform simulation-based calibration across plausible ICC and effect sizes; do not invent donor numbers or variance components.
4. Define quality-control (QC) gates before unblinding: viability, doublets, debris, field coverage, image focus, batch metrics, and minimum cells/fields per donor.
5. Pre-specify whether exclusions occur at donor/animal level, cell/field level, or both. Cell-level exclusions must not be used to change the randomized-unit count.

**Quality checks**

- Donor/animal-level completeness: treatment assignment, sampling time, batch, sex, age, litter/cage, and other covariates.
- Cell/field-level QC: segmentation, gating, thresholding, normalization; record all thresholds.
- Batch/plate/field position: randomize or block; include batch as covariate or random effect where possible.
- Technical controls: vehicle, positive control, negative control, unstained/isotype, spike-in, or reference sample as appropriate.
- Negative control outcomes: features/regions expected not to change with treatment, used to calibrate false positives.

## 3. Independent units, allocation, and blinding

- Randomize treatment at the **donor/animal level** only. Never assign treatment to individual cells or fields.
- Use stratified/blocked randomization by batch, sex, age, litter/cage, or baseline donor-level covariates when applicable.
- Conceal allocation until donor/animal assignment is fixed.
- Blind sample processing, image acquisition, gating, and outcome measurement where feasible.
- Randomize acquisition order, plate positions, fields, and analysis order to reduce technical confounding.
- Sample size/power: base on donor/animal-level variance and ICC. If unknown, calibrate via pilot variance components or simulation across plausible ICCs. Do not base power on cell/field counts alone.

**Independent units:** treatment replicates are donors/animals per arm. Cells/fields are repeated measures within those units. If repeated measures over time occur within the same animal, the animal remains the cluster and time is a within-animal variable.

## 4. Intervention and sampling

- Apply intervention to donor/animal according to randomized allocation.
- After intervention, sample cells/fields using a pre-specified sampling frame designed to represent the donor/animal.
- Record hierarchical IDs: donor/animal → sample → batch/plate → field/cell.
- Pre-specify target number of cells/fields per donor, but treat this as sampling effort, not as independent n.
- Record missingness at donor and cell/field levels.
- Controls: vehicle/untreated, positive control, negative control, technical control, and if possible a donor-level baseline or pre-treatment measurement.

## 5. Measurements

- Primary measurement: donor-level summary (mean, median, proportion, total counts, normalized expression, or model-derived donor parameter).
- Secondary measurements: cell/field-level values, subtype proportions, spatial features, etc.
- For single-cell data: pseudobulk per donor and per relevant cell type.
- For imaging: donor-level summaries across fields, with field-level values retained for hierarchical modeling.
- Pre-specify normalization and transformation. Avoid changing the primary outcome after seeing treatment results.

## 6. Analysis

### 6.1 Primary analysis: pseudobulk donor-level comparison

Proposed steps:

1. Aggregate cells/fields to one value per donor/animal. Examples: mean expression, median intensity, proportion of positive cells, total counts, or normalized pseudobulk counts.
2. Compare treatment arms at donor level using:
   - two-sample t-test, Welch t-test, or Wilcoxon rank-sum for simple designs;
   - linear model with covariates/blocking factors;
   - negative binomial/quasi-Poisson GLM for donor-level counts with offset;
   - beta regression or logit-transformed linear model for proportions;
   - for omics pseudobulk: limma-voom, DESeq2, or edgeR with donor as the sample unit and design including treatment plus covariates.
3. If repeated measures per donor, use a donor-level mixed model or generalized least squares with donor random effect.
4. Report effect size, confidence interval, and calibrated p-value.

This is the most robust primary analysis when donor/animal n is small and cells/fields are many.

### 6.2 Primary alternative: hierarchical/mixed model

Use a cell/field-level model with donor/animal random effects. For a continuous outcome:

\[
y_{ij} = \beta_0 + \beta_1 \text{treatment}_i + b_i + \varepsilon_{ij}
\]

where \(i\) indexes donor/animal, \(j\) indexes cell/field, \(b_i \sim N(0,\sigma_b^2)\), and \(\varepsilon_{ij} \sim N(0,\sigma^2)\). Treatment is a donor-level covariate. \(\beta_1\) is the donor-level treatment effect.

Extensions:

- Random slope for treatment if treatment effects vary by donor.
- GLMM for binomial, Poisson, or negative binomial outcomes.
- GEE with cluster-robust SE at donor level for population-average effects.
- Bayesian hierarchical model with weakly informative priors when donor n is very small.

Inference: Wald or likelihood-ratio tests with Kenward–Roger or Satterthwaite degrees of freedom; cluster-robust SEs; or posterior credible intervals. Do not use cell-level residual df as treatment df.

### 6.3 Secondary cell-level analysis

Cell-level models with donor random effects can be reported as conditional/mechanistic analyses. They may answer “within a donor, do treated cells differ?” but not “does treatment affect the donor population?” without donor-level replication. If cell-type interaction is of interest, include treatment × cell type in a hierarchical model, but recognize that composition changes can confound interpretation.

### 6.4 Grouped resampling

**Cluster bootstrap:**

- Resample donors/animals with replacement within treatment arms or within randomization strata.
- Keep all cells/fields from a resampled donor together.
- Recompute pseudobulk or hierarchical treatment effect.
- Repeat many times; use percentile or BCa confidence intervals.
- For hierarchical models, bootstrap donors/animals, not cells.

**Permutation/randomization inference:**

- Permute treatment labels among donors/animals within strata, preserving cell/field structure.
- Recompute the primary statistic.
- The permutation p-value is the proportion of permuted statistics at least as extreme as observed.
- Use the same permutation scheme for all primary outcomes.

**Multiplicity:**

- Pre-specify a primary outcome or use hierarchical/gatekeeping.
- For many outcomes, use resampling-based FDR or hierarchical shrinkage at donor level.
- Report adjusted and unadjusted results.

### 6.5 Null calibration

Proposed null calibration procedure:

1. Generate null datasets by permuting treatment labels at the donor/animal level while keeping the observed cell/field hierarchy intact.
2. Run the full analysis pipeline on each null dataset:
   - pseudobulk donor-level test;
   - hierarchical/mixed model;
   - naive cell-level test treating cells as independent (for comparison).
3. Estimate null distributions, type I error, and false discovery proportion for each pipeline.
4. Compare naive vs donor-level calibration. If the naive cell-level test is inflated, report this explicitly.
5. Use calibrated thresholds or permutation p-values for primary inference.
6. If Bayesian, perform prior/posterior predictive checks under null simulations.

This directly addresses the packet’s warning that high ICC or significance loss alone does not prove a false biological effect: null calibration estimates operating characteristics rather than relying on a single p-value.

### 6.6 Held-out validation

Validate at the **donor/animal level**, not the cell level.

Proposed design:

- Split randomized units into training and validation sets, stratified by treatment and batch.
- Use nested cross-validation: inner folds select features/hyperparameters; outer folds estimate validation performance.
- Train the model, feature selection, thresholds, and normalization on training donors only.
- Evaluate on held-out donors:
  - prediction of donor-level outcome;
  - calibration slope/intercept;
  - discrimination/AUC for classifiers;
  - signature score correlation;
  - hierarchical model predictive checks.
- For treatment-effect estimation, the primary confirmatory analysis should use the pre-specified full dataset. Held-out validation is for model validation, robustness, and specification, not for replacing the primary effect estimate.
- If held-out validation is used for effect estimation, use grouped cross-validation at the donor level and report fold-specific counts.

### 6.7 Sensitivity and troubleshooting analyses

- Naive cell-level analysis to quantify inflation.
- Leave-one-donor-out influence analysis.
- Different donor-level summaries (mean vs median vs total counts).
- Mixed model with/without covariates and batch random effects.
- Exclude low-cell donors and repeat primary analysis.
- Alternative ICC/prior sensitivity.
- Report ICC, variance components, design effect, and effective sample size where possible.

Design effect approximation for cell-level mean: \(1 + (m-1)\text{ICC}\), where \(m\) is average cells/fields per donor. Effective sample size is approximately donor n divided by design effect. Use only as a sensitivity summary; hierarchical modeling is preferred.

## 7. Acceptance, stopping, and troubleshooting criteria

**Acceptance criteria (proposed):**

- Randomization and allocation are valid; no major arm imbalance.
- QC passes at donor and cell/field levels.
- Primary analysis is pre-specified and donor-level.
- Null calibration shows acceptable type I error for the chosen primary analysis.
- Held-out validation performance meets a threshold pre-specified from pilot/simulation or biological context. If no threshold can be justified, report validation estimates with CIs and avoid binary accept/reject language.

**Stopping criteria:**

- Do not stop or declare success/failure based on cell-level p-values.
- Stopping for futility or superiority should be pre-specified at the donor/animal level and calibrated by simulation.
- If unacceptable confounding or QC failure occurs, pause and troubleshoot; do not interpret treatment effects from a compromised dataset without explicit sensitivity analysis.

**Troubleshooting:**

| Problem | Proposed response |
|---|---|
| Very few donors/animals | Use Bayesian hierarchical model with weakly informative priors; report wide CIs; avoid strong claims. |
| High ICC | Use pseudobulk primary; hierarchical model secondary; report design effect. |
| Unbalanced cells/fields per donor | Weight by donor, not cell; use donor-level aggregation or random effects. |
| Batch confounding | Include batch in design/random effects; sensitivity analysis; report limitations. |
| Zero-inflated or sparse data | Use hurdle/zero-inflated models; pseudobulk with counts; sensitivity to normalization. |
| Naive cell-level analysis significant but donor-level not | Do not claim treatment effect; report both and explain pseudoreplication. |
| Donor-level not significant but effect size large | Report CI and precision; do not conclude no effect solely from p-value. |
| Held-out validation poor | Report; do not overfit; revise model only with pre-specified rules. |

## 8. Reporting requirements

Report:

- **Randomized-unit counts:** number of donors/animals randomized, allocated, analyzed, and excluded per arm.
- **Observed-cell/field counts:** total cells/fields, per donor, per arm, and analyzed after QC.
- **Hierarchy:** cells/fields per donor; number of batches/plates/fields.
- **Primary effect:** donor-level effect size, CI, p-value or posterior probability.
- **Grouped resampling:** bootstrap CIs and permutation p-values.
- **Null calibration:** type I error, FDP, naive vs donor-level comparison.
- **Held-out validation:** training/validation donor counts, performance metrics, calibration.
- **Variance components:** ICC, donor variance, residual variance, design effect, effective sample size if estimated.
- **Sensitivity analyses:** naive cell-level, leave-one-donor-out, alternative models.
- **Limitations:** small independent n, model assumptions, exchangeability, cell-level vs donor-level inference.

## 9. Alternatives and limits

**Alternatives:**

- Pseudobulk t-test/GLM: robust, simple, loses within-donor cell heterogeneity.
- Hierarchical/mixed model: uses all cells, estimates donor variance, but variance components unstable with few donors.
- GEE with cluster-robust SE: population-average, robust to some misspecification, but small-cluster performance can be poor.
- Bayesian hierarchical model: handles small n with priors, but prior sensitivity must be reported.
- Permutation/randomization inference: strong null calibration, but limited by small donor n and exchangeability assumptions.
- Cell-level conditional models: useful for mechanism, not for population treatment effect.

**Limits:**

- Many cells/fields cannot replace independent donors/animals.
- Small randomized-unit n limits precision and robustness.
- ICC and variance components may be poorly estimated.
- Held-out validation reduces effective sample size and may be underpowered.
- Treatment effects may be heterogeneous across donors/animals.
- Cell composition changes can confound cell-type-specific effects.
- Batch, plate, and field effects can masquerade as treatment effects if not randomized/blinded.
- Resampling with very few clusters can have poor coverage.

**What would change the recommendation:**

- If treatment were assigned at the cell/field level, cells could be independent replicates.
- If donor/animal n were large and ICC negligible, a cell-level mixed model might approximate donor-level inference, but donor-level reporting would still be required.
- If the primary question is cell-level mechanism rather than donor-level treatment effect, hierarchical conditional models are appropriate, but population treatment claims remain donor-level.
- If a pilot shows very high ICC, pseudobulk should dominate; if ICC is low, hierarchical models may gain power but must still respect donor-level randomization.

In summary, the proposed protocol uses donor/animal-level primary inference, pseudobulk or hierarchical modeling, grouped resampling, null calibration by donor-level permutation, held-out donor validation, and dual reporting of randomized-unit and observed-cell counts. All experiments and analyses above are proposed; unknown parameters must be calibrated by pilot data or simulation, not assumed.
