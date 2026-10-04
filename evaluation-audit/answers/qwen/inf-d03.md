# Qwen3.8 Max (0902) / inf-d03

Original final answer, shared by both scoring rounds.

All experiments and analyses below are **proposed**. No completed experiments, completed analyses, or numerical results are being reported.

## Recommended conclusion / next action

The study should treat the **donor or animal** as the independent randomized treatment unit and should not treat cells or fields measured within the same donor as independent treatment replicates. The primary analysis should therefore be either:

1. a **donor-level pseudobulk comparison**, in which all cells or fields from each donor are summarized into one donor-level value, or  
2. a **hierarchical model** with donor-level random effects or equivalent donor-level clustering, where the treatment effect is estimated at the donor level and uncertainty is calibrated by donor-level resampling.

Validation and resampling must operate on **whole donors**, not individual cells. Reporting must separately state:

- the number of **randomized independent units**: donors or animals assigned to treatment; and  
- the number of **observed subunits**: cells or fields measured within each randomized unit.

This protocol is justified by the supplied evidence packet, which states that the randomized treatment level defines the experimental unit, that observational and biological units can differ, and that treating dependent observations as independent replication is the core pseudoreplication concern.

---

## Evidence-to-inference-to-conclusion chain

| Evidence from supplied packet | Inference | Protocol consequence |
|---|---|---|
| Treatment is assigned to donors or animals, while many cells or fields are measured per donor. | The donor/animal is the unit receiving the randomized intervention. Cells/fields are nested observational subunits. | Define donor/animal as the independent experimental unit. |
| The randomized treatment level defines the experimental unit; observational and biological units can differ. | Cell-level measurements cannot substitute for donor-level replication. | Primary inference must be donor-level or must explicitly model donor clustering. |
| Treating treatment subsamples or dependent observations as independent replication is the concern. | Treating cells as independent replicates can overstate precision and produce misleading significance. | Use donor-level summaries, donor random effects, clustered standard errors, and donor-level resampling. |
| Very small independent n affects precision and robustness but does not automatically invalidate every model-based test. | Low donor numbers reduce reliability but do not automatically make all analyses invalid. | Use calibration, permutation or bootstrap by donor, and state uncertainty clearly. |
| Clustering may alter uncertainty without changing a point estimate. | A treatment effect estimate may remain similar after proper clustering while confidence intervals or p-values change. | Report both point estimates and donor-calibrated uncertainty. |
| High intraclass correlation or loss of significance alone does not prove a false biological effect. | Loss of significance after correction is not proof of absence of effect. | Interpret loss of significance as reduced evidential strength or insufficient independent replication, not as disproof. |

---

## Proposed operational protocol

### 1. Preparation and quality checks

All steps in this section are proposed.

#### 1.1 Define the unit hierarchy

Before data collection or analysis, define:

- **Randomized unit / independent treatment replicate**: donor or animal assigned to treatment.
- **Observational subunit**: cell, field, image, well region, or other measurement nested within a donor.
- **Biological unit of inference**: the level to which the treatment effect should generalize. In this design, it is the donor/animal population, not individual cells.

A written mapping must be created:

```text
Donor/animal ID -> treatment assignment -> batch -> sampled cells/fields -> measurements
```

#### 1.2 Define primary donor-level outcome

Choose one primary outcome that can be summarized per donor. Examples include:

- mean intensity per donor;
- proportion of positive cells per donor;
- normalized pseudobulk count per donor;
- mean morphological score per field per donor;
- donor-level rate or ratio.

The primary outcome should be defined before unblinding treatment assignment.

#### 1.3 Data structure requirements

Create two linked tables:

1. **Donor-level table**  
   One row per donor/animal. Fields should include:
   - donor ID;
   - treatment arm;
   - batch;
   - sex, age, genotype, or other stratification variables if known;
   - number of cells/fields observed;
   - donor-level summary outcome;
   - inclusion/exclusion status.

2. **Cell/field-level table**  
   One row per cell or field. Fields should include:
   - cell/field ID;
   - donor ID;
   - treatment arm, copied from donor record;
   - measurement value;
   - technical covariates such as plate, image, stain batch, scan date;
   - quality-control flags.

Treatment assignment must not be inferred from cells; it must come from the donor record.

#### 1.4 Pre-analysis quality checks

Proposed quality checks:

- confirm each cell/field maps to exactly one donor;
- confirm treatment is constant within donor;
- identify donors with too few cells/fields for stable summaries;
- identify batch variables confounded with treatment or donor;
- inspect missingness by donor and treatment arm;
- examine cell-level outliers before unblinding where possible;
- check whether cell counts per donor differ systematically by treatment.

If treatment is confounded with batch, stop and redesign or restrict inference. Do not attempt to statistically “fix” a fully confounded design without strong assumptions.

---

### 2. Independent units, allocation, blinding, and calibration

#### 2.1 Independent units

The independent replicate count is the number of donors or animals randomized and analyzed, not the number of cells or fields.

Define:

- `N_randomized_donors`: donors/animals assigned to treatment;
- `N_analyzed_donors`: donors/animals included in the primary analysis;
- `N_cells_total`: total cells/fields measured;
- `N_cells_per_donor`: cell/field count for each donor.

Both randomized-unit counts and observed-cell counts must be reported.

#### 2.2 Allocation

Proposed allocation procedure:

- randomize donors/animals to treatment groups;
- use blocking or stratification if known donor-level covariates are expected to influence outcome, for example sex, genotype, age, litter, batch, or experiment date;
- record the randomization seed or randomization list;
- preserve the randomization structure in downstream permutation tests.

If treatment is not randomized, this protocol must be expanded to address confounding. The supplied design assumes treatment is assigned to donors/animals.

#### 2.3 Blinding

Proposed blinding procedure:

- laboratory personnel performing measurements should be blinded to treatment where feasible;
- analysts should receive a blinded dataset until the analysis plan is locked;
- unblinding should occur only after primary outcome definitions, exclusions, and analysis code are finalized;
- any unblinding event must be logged.

#### 2.4 Calibration for unknown parameters

The supplied packet states that exact donor numbers, cell numbers, effect sizes, and variance components are unavailable. These must therefore be calibrated, not invented.

Proposed calibration procedure:

1. Use a pilot or interim dataset, preferably from control or untreated donors, to estimate:
   - between-donor variance;
   - within-donor cell/field variance;
   - mean and variability of cells/fields per donor;
   - intraclass correlation, ICC;
   - batch effects if present.

2. Fit a simple donor-clustering model to the pilot data:

   ```text
   y_ij = mu + u_i + e_ij
   ```

   where:
   - `y_ij` is the measurement for cell/field `j` in donor `i`;
   - `u_i` is the donor-level deviation;
   - `e_ij` is the within-donor residual deviation.

3. Estimate:

   ```text
   tau^2 = between-donor variance
   sigma^2 = within-donor variance
   ICC = tau^2 / (tau^2 + sigma^2)
   ```

4. Estimate the variance of a donor mean for `m_i` cells/fields:

   ```text
   Var(donor mean_i) ≈ tau^2 + sigma^2 / m_i
   ```

5. Use these estimates to plan donor sample size or precision. Increasing cells per donor mainly reduces `sigma^2 / m_i`; it does not remove `tau^2`, which is the donor-to-donor variation relevant for treatment comparison.

6. If no pilot data exist, use sequential accrual:
   - collect donors in prespecified batches;
   - re-estimate variance components after each batch;
   - stop when donor-level precision reaches a prespecified range or when a maximum feasible donor number is reached.

Unreported parameters requiring calibration:

- number of donors per group;
- number of cells/fields per donor;
- effect size;
- between-donor variance;
- within-donor variance;
- ICC;
- batch variance;
- missingness rate;
- overdispersion for count outcomes.

These should be treated as unknown until estimated from appropriate calibration data.

---

### 3. Intervention and sampling

All steps are proposed.

#### 3.1 Treatment delivery

Treatment must be applied at the donor or animal level. Record:

- donor/animal ID;
- treatment arm;
- dose or condition;
- time of treatment;
- route or mode where relevant;
- deviations or failures.

#### 3.2 Sampling scheme

For each donor, define a standardized sampling scheme:

- target number of cells or fields per donor;
- sampling locations or regions;
- time point after treatment;
- rules for excluding unusable fields or cells;
- rules for handling donors with insufficient material.

Proposed sampling principles:

- sample fields/cells without using knowledge of treatment;
- avoid selecting “best” or “representative” fields after observing outcomes;
- if fields are selected from a spatial structure, use random or systematic unbiased sampling;
- record the denominator: number of fields imaged, number of cells segmented, number of cells passing QC.

#### 3.3 Distinguish biological replication from subsampling

Cells or fields from the same donor are subsamples of that donor. They improve measurement precision for that donor but do not create additional independent treatment replicates.

---

### 4. Measurements

All steps are proposed.

#### 4.1 Measurement pipeline

Define and version-control the measurement pipeline:

- image acquisition settings or assay readout settings;
- segmentation rules;
- gating or classification rules;
- normalization method;
- batch-correction method, if any;
- quality thresholds.

The pipeline should be fixed before treatment unblinding where possible.

#### 4.2 Cell/field-level outcomes

For each cell/field, record raw and processed values. Examples:

- marker intensity;
- cell count;
- proportion of positive cells;
- morphological feature;
- categorical state.

#### 4.3 Donor-level summaries

For each donor, compute the primary summary before treatment comparison. Examples:

```text
S_i = mean(y_ij) over cells j in donor i
S_i = sum(y_ij) / exposure_i
S_i = proportion of positive cells in donor i
```

For count outcomes, define exposure, such as number of cells analyzed or number of fields imaged.

---

### 5. Controls

All controls are proposed.

#### 5.1 Concurrent treatment controls

Include donors/animals processed in the same experimental blocks as treated donors:

- vehicle, sham, untreated, or baseline control as appropriate;
- controls distributed across batches and measurement days.

#### 5.2 Negative-control outcome

Use a negative-control outcome expected to be unaffected by treatment. This helps detect assay drift, batch effects, or analysis leakage.

#### 5.3 Reference control sample

If feasible, include a common reference sample or pooled control sample in each batch. This is useful for monitoring technical variation but does not replace donor-level replication.

#### 5.4 Positive control, if available

A positive control can show assay sensitivity but does not validate donor-level inference for the experimental treatment.

---

## 6. Proposed analysis plan

All analyses below are proposed. The primary analysis should be locked before unblinding.

### 6.1 Primary analysis principle

The treatment effect must be estimated from variation between randomized donors/animals, not from variation among cells within the same donor.

Let:

- `i = 1, ..., N` index donors/animals;
- `j = 1, ..., m_i` index cells/fields within donor `i`;
- `T_i` be the treatment assigned to donor `i`;
- `y_ij` be the measurement for cell/field `j`.

The primary estimand is the treatment effect comparing donor-level outcomes between treatment groups.

---

### 6.2 Option A: Donor-level pseudobulk comparison

This is the simplest and most transparent primary analysis.

#### Step 1: Create donor-level summary

For each donor, calculate:

```text
S_i = summary(y_i1, y_i2, ..., y_im_i)
```

The summary should match the biological question. Possible summaries:

- mean or median continuous measurement;
- proportion of positive cells;
- normalized sum of counts;
- rate per field;
- log-transformed count with offset.

#### Step 2: Compare donor summaries

Use donor as the observation:

```text
S_i = beta_0 + beta_1 T_i + optional donor-level covariates + error_i
```

The treatment effect is `beta_1`.

For continuous summaries, a linear model or robust location test may be used. For proportions or counts, use an appropriate binomial, beta-binomial, Poisson, or negative-binomial model with donor-level exposure if needed.

#### Step 3: Report donor-level uncertainty

Confidence intervals and p-values must reflect the number of donors, not the number of cells.

#### Advantages

- avoids pseudoreplication;
- easy to audit;
- transparent reporting;
- robust when cell-level models converge poorly.

#### Limitations

- discards some within-donor structure;
- may be inefficient if cell counts vary widely;
- requires a defensible summary measure.

---

### 6.3 Option B: Hierarchical donor-level model

A hierarchical model may be used as primary or secondary analysis.

For continuous outcomes:

```text
y_ij = beta_0 + beta_1 T_i + u_i + e_ij
u_i ~ donor-level random effect
e_ij ~ within-donor residual
```

For binary, count, or skewed outcomes, use a generalized hierarchical model with an appropriate link function.

The treatment variable `T_i` varies only at the donor level. The treatment effect `beta_1` is therefore a donor-level effect.

#### Required features

- donor random intercept at minimum;
- treatment assigned at donor level;
- clustering by donor in uncertainty estimation;
- adjustment for batch or stratification variables only if prespecified;
- diagnostics for convergence and donor influence.

#### Advantages

- can handle unequal numbers of cells/fields per donor;
- can estimate ICC and variance components;
- can include cell-level covariates while preserving donor-level treatment inference.

#### Limitations

- may be unstable with very few donors;
- depends on distributional assumptions;
- may fail to converge if the model is too complex;
- must be calibrated by donor-level resampling or permutation.

If the hierarchical model and pseudobulk model disagree materially, investigate donor influence, unequal cell counts, outliers, batch effects, and model assumptions before drawing conclusions.

---

### 6.4 Grouped resampling by donor

Grouped resampling is required because cells within donors are not independent.

#### 6.4.1 Donor-level bootstrap

Proposed procedure:

1. Resample donors with replacement.
2. Preserve all cells belonging to each selected donor.
3. Preserve treatment assignment as attached to donor.
4. Recompute the treatment effect.
5. Repeat many times.
6. Use the bootstrap distribution to estimate confidence intervals.

If randomization used blocks or strata, resample donors within blocks/strata.

#### 6.4.2 Donor-level permutation

For hypothesis testing, permute treatment labels across donors, not across cells.

Proposed procedure:

1. Keep each donor’s cells together.
2. Shuffle treatment labels among donors.
3. If blocked randomization was used, permute only within blocks.
4. Recompute the treatment statistic.
5. Repeat for all or many permutations.
6. Compare the observed statistic to the donor-permutation distribution.

This permutation test directly respects the randomization unit.

#### 6.4.3 Reporting resampling details

Report:

- number of resamples or permutations;
- whether resampling was by donor;
- whether blocks/strata were preserved;
- statistic used;
- confidence interval method;
- p-value calculation rule.

---

### 6.5 Null calibration

Null calibration is needed because exact donor numbers, variance components, and cell counts are unknown and must be checked.

#### 6.5.1 Permutation null calibration

Use donor-level permutation to check whether the primary test behaves appropriately under the sharp null of no treatment effect.

Proposed checks:

- the p-value distribution should be approximately uniform under permutation when no true effect is present;
- empirical rejection rate at nominal alpha should be compatible with the nominal rate, allowing for Monte Carlo error;
- if the test is anti-conservative, use a more conservative donor-level method or collect more donors.

#### 6.5.2 Negative-control outcome calibration

Analyze a negative-control outcome expected to have no treatment effect.

Acceptance criterion:

- the treatment effect on the negative-control outcome should be small and statistically indistinguishable from zero, within the uncertainty expected from the donor sample size.

A single noisy negative-control result does not prove failure, but systematic inflation across controls indicates a problem.

#### 6.5.3 Simulation-based calibration using estimated variance components

When pilot or interim data are available:

1. Estimate donor-level and cell-level variance components.
2. Simulate many datasets under no treatment effect.
3. Assign treatment to donors according to the planned randomization scheme.
4. Generate nested cells/fields using estimated variance components.
5. Apply the full analysis pipeline.
6. Estimate the empirical false-positive rate.

This procedure calibrates the analysis pipeline under plausible data-generating conditions. It does not invent results; it tests the behavior of the proposed analysis.

#### 6.5.4 Interpretation of calibration failures

If calibrated donor-level analysis loses significance compared with a naive cell-level analysis, this does not prove the biological effect is false. The supplied evidence states that high ICC or loss of significance alone does not prove a false biological effect. It means the cell-level analysis likely overstated precision, and the donor-level evidence should be interpreted with appropriate uncertainty.

---

### 6.6 Held-out validation by donor

Held-out validation must separate donors, not individual cells.

#### 6.6.1 Donor-level split

If enough donors are available:

1. Reserve one or more donors as a held-out validation set before model fitting.
2. Fit the analysis model only on training donors.
3. Apply all normalization, scaling, and parameter estimates from the training set to the held-out donors.
4. Predict donor-level summaries or treatment-related outcomes in held-out donors.
5. Evaluate prediction performance at the donor level.

No cells from held-out donors should influence model fitting or normalization.

#### 6.6.2 Leave-one-donor-out validation

If donor numbers are small but more than a few donors exist:

- use leave-one-donor-out cross-validation as an exploratory validation step;
- each iteration leaves out all cells from one donor;
- performance should be summarized across left-out donors.

This is not a substitute for independent donor replication but can reveal whether the analysis is driven by one donor or by cell-level leakage.

#### 6.6.3 External donor validation

If the current study has too few donors for meaningful internal held-out validation, propose an external validation cohort:

- collect or obtain independent donors processed under comparable conditions;
- apply the same donor-level analysis;
- evaluate whether the treatment effect direction, magnitude, and uncertainty are compatible.

External validation is proposed, not assumed.

#### 6.6.4 Limits of held-out validation

Held-out validation assesses generalization or predictive stability. It does not by itself prove causality. Causal interpretation still depends on randomization, controls, and absence of confounding.

---

### 6.7 Sensitivity analyses

Proposed sensitivity analyses:

1. Compare pseudobulk and hierarchical model estimates.
2. Use weighted and unweighted donor summaries.
3. Exclude donors with extremely low cell/field counts.
4. Repeat analysis after excluding the most influential donor.
5. Adjust or do not adjust for prespecified batch variables.
6. Use alternative transformations for skewed outcomes.
7. Compare permutation p-values with model-based p-values.
8. Estimate ICC and report how uncertainty changes with clustering.

A key expected pattern is that point estimates may be similar while uncertainty widens after donor-level clustering. This is consistent with the supplied evidence.

---

### 6.8 Required reporting

Report both levels of replication explicitly.

#### Randomized-unit counts

Report:

- number of donors/animals randomized per treatment group;
- number excluded after randomization and reasons;
- number analyzed per treatment group;
- blocking or stratification variables used;
- number of donors used in held-out validation, if any.

#### Observed-cell counts

Report:

- total cells/fields measured per group;
- total cells/fields measured overall;
- median cells/fields per donor;
- range or interquartile range of cells/fields per donor;
- number of cells/fields excluded by QC;
- whether cell counts differ by treatment group.

#### Statistical reporting

Report:

- donor-level effect estimate;
- donor-level confidence interval;
- calibrated p-value;
- method used: pseudobulk, hierarchical model, or both;
- resampling method;
- ICC or variance components where estimable;
- assumptions and diagnostics;
- whether significance changed between naive cell-level and donor-level analysis.

The report must not imply that `N_cells` is the number of independent treatment replicates.

---

## 7. Acceptance and stopping criteria

All criteria are proposed.

### 7.1 Acceptance criteria for primary claim

A treatment effect claim should be accepted only if:

1. treatment was assigned at the donor/animal level;
2. the primary analysis uses donor-level pseudobulk or donor-clustered hierarchical inference;
3. resampling or permutation respects donor grouping;
4. null calibration does not show severe anti-conservative behavior;
5. held-out or external validation, if prespecified, is reported;
6. both donor counts and cell/field counts are reported;
7. uncertainty is stated in terms of independent donor replication.

### 7.2 Criteria for exploratory interpretation

The analysis should be downgraded to exploratory if:

- donor number is too low for stable calibration;
- null calibration fails and cannot be corrected;
- batch is confounded with treatment;
- the primary result depends on one or two donors;
- held-out validation cannot be performed or fails;
- the outcome summary is unstable for many donors.

### 7.3 Stopping or redesign criteria

Stop or redesign if:

- treatment is no longer randomized at the donor level;
- donors cannot be linked to cells/fields;
- batch fully confounds treatment;
- too few donors are available to estimate donor-level variation;
- QC shows systematic measurement failure;
- the primary outcome cannot be summarized per donor.

### 7.4 Precision-based stopping

If interim calibration shows that the achievable donor number cannot estimate the treatment effect with acceptable precision, adding more cells per donor will usually not solve the problem. The appropriate response is to:

- increase donor number;
- reduce biological heterogeneity if scientifically acceptable;
- choose a more precise donor-level endpoint;
- reduce the scope of the claim.

---

## 8. Troubleshooting

### 8.1 Very few donors but many cells

Problem: large cell counts but few randomized donors.

Proposed response:

- use exact or near-exact donor-level permutation if possible;
- report effect sizes and intervals rather than relying on p-values;
- treat model-based tests as conditional on strong assumptions;
- collect more donors if feasible;
- label conclusions as limited by independent donor number.

The supplied evidence states that very small independent n affects precision and robustness but does not automatically invalidate every model-based test.

### 8.2 High ICC

Problem: cells within the same donor are highly similar.

Proposed response:

- report ICC;
- emphasize donor-level uncertainty;
- increase donor number rather than cell number;
- avoid interpreting many cells as many independent replicates.

High ICC changes uncertainty but does not by itself refute a biological effect.

### 8.3 Loss of significance after donor-level correction

Problem: naive cell-level analysis is significant, donor-level analysis is not.

Proposed response:

- report both analyses transparently;
- do not claim the effect is false solely because significance was lost;
- examine the effect estimate and confidence interval;
- assess whether additional donors could resolve uncertainty;
- use controls and validation to assess robustness.

### 8.4 Unequal cells per donor

Problem: some donors have many cells/fields, others few.

Proposed response:

- use donor-level summaries with appropriate weighting or exposure offsets;
- use hierarchical model that accounts for unequal subunit counts;
- perform sensitivity analysis excluding low-count donors;
- report cell/field count distribution by donor and treatment.

### 8.5 Batch confounding

Problem: all treated donors processed in one batch and all controls in another.

Proposed response:

- do not rely on statistical adjustment alone;
- redesign with donors from each treatment distributed across batches;
- if already collected, limit inference and label batch-confounded results as uncertain.

### 8.6 Hierarchical model convergence failure

Problem: mixed model fails or gives unstable variance estimates.

Proposed response:

- simplify the model;
- remove unnecessary random slopes;
- use donor-level pseudobulk as primary analysis;
- report convergence diagnostics;
- do not select the model that gives the smallest p-value after seeing the result.

### 8.7 Held-out validation impossible due to small donor number

Problem: not enough donors to hold out any.

Proposed response:

- use leave-one-donor-out only as exploratory;
- propose external donor validation;
- state that internal validation was not feasible;
- reduce confidence in generalization accordingly.

---

## 9. Alternatives and limits

### 9.1 Pseudobulk alternative

A donor-level pseudobulk analysis is often the safest primary approach because it makes the independent unit explicit. It is especially useful when donor numbers are small or hierarchical models are unstable.

Limit: it may discard useful within-donor information and may be sensitive to how the donor summary is defined.

### 9.2 Hierarchical model alternative

A hierarchical model can use all cell/field measurements and estimate variance components.

Limit: it requires assumptions about random effects and residual distributions, and it may be unreliable with very few donors unless carefully calibrated.

### 9.3 Bayesian hierarchical alternative

A Bayesian hierarchical model can express uncertainty more explicitly and can incorporate prior information if justified.

Limit: it still requires donor-level replication for treatment inference and should be calibrated with donor-level null checks.

### 9.4 When this protocol does not apply

This protocol assumes treatment is assigned to donors or animals. If treatment is independently randomized to cells within a donor, the experimental unit and analysis would differ. If treatment is not randomized, confounding must be addressed explicitly.

### 9.5 Limits of validation

Held-out donor validation tests generalization and leakage, but it cannot correct for biased treatment assignment, unmeasured donor-level confounding, or systematic assay bias. Null calibration can detect some statistical anti-conservatism but cannot guarantee biological truth.

---

## Final statement

The proposed protocol is to analyze the study as a donor/animal-randomized experiment with nested cell/field subsamples. The primary treatment comparison should be based on donor-level pseudobulk summaries or donor-clustered hierarchical models. Uncertainty must be calibrated using donor-level permutation, bootstrap, or simulation based on estimated variance components. Held-out validation must hold out whole donors, not individual cells. Results must report both the number of randomized donors/animals and the number of observed cells/fields, and conclusions must be constrained by the number of independent randomized units. All experiments and analyses described above are proposed.
