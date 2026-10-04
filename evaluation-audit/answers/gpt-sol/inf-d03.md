# GPT-5.6 Sol / inf-d03

Original final answer, shared by both scoring rounds.

# Proposed analysis and validation protocol

## Recommended design and conclusion

**All experiments and analyses described below are proposed; no completed results are implied.**

The proposed study should treat the **donor or animal receiving the randomized treatment as the independent experimental unit**. Cells and fields would be treated as nested observational units, not as independent treatment replicates. The recommended primary analysis would therefore be a **donor-level pseudobulk comparison with equal donor weighting**, supported by a **hierarchical model**, donor-grouped resampling, treatment-label permutation at the randomized-unit level, and validation in donors or animals held out before model development.

A treatment conclusion would be accepted only if it is supported at the randomized-unit level, survives prespecified multiplicity and robustness checks, and shows compatible performance in held-out independent units. Large cell counts could improve measurement of each donor but would not compensate for too few donors. Cell-level findings could be reported as descriptive heterogeneity or conditional cell-level associations, but not as evidence that the treatment was independently replicated across cells.

---

## Evidence-to-inference-to-conclusion chain

1. **Evidence:** Treatment is assigned to donors or animals, while many cells or fields are measured from each treated unit. The evidence packet defines pseudoreplication as treating dependent subsamples as independent treatment replicates and states that the randomized treatment level defines the experimental unit.

2. **Inference:** Cells and fields from the same donor share treatment assignment and biological context. Their errors may therefore be correlated. Treating them as independent would generally understate uncertainty and inflate the apparent treatment replication.

3. **Proposed analysis consequence:** Treatment labels would be compared, permuted, bootstrapped, split into training and validation sets, and counted at the **donor/animal level**. Cells and fields would remain available for estimating donor summaries, within-donor heterogeneity, and measurement error.

4. **Evidence-qualified interpretation:** Clustering may change uncertainty without materially changing a point estimate. High intraclass correlation or loss of nominal significance after clustering would not by itself prove that the biological effect is false. Conversely, a stable cell-level estimate would not establish treatment efficacy if donor-level uncertainty remains large.

5. **Conclusion rule:** The study could support a donor/animal-level treatment claim only from analyses whose effective replication is based on independent randomized units. Exact precision, power, and robustness cannot yet be determined because donor counts, cell counts, effect sizes, and variance components are unreported; these would be calibrated as described below.

---

# Ordered proposed protocol

## 1. Preparation and quality checks

### 1.1 Define the estimand

Before enrollment or unblinding, the investigators would specify:

- The primary biological outcome.
- The target population of donors or animals.
- The primary contrast, such as mean treatment versus control difference.
- The relevant time point, tissue, cell population, or field type.
- Whether the primary estimand is:
  - a difference in the **average donor-level outcome**, recommended for the treatment claim; or
  - another explicitly defined donor-level quantity, such as the proportion of donors exceeding a biological threshold.
- A minimum biologically meaningful effect, derived from prior evidence, an independent pilot, or domain requirements rather than selected from the study results.
- A prespecified error criterion and multiplicity procedure for multiple outcomes or cell types.

Any analyses of individual-cell response distributions would be labeled secondary unless the estimand explicitly concerns within-donor heterogeneity.

### 1.2 Map the hierarchy

A proposed data hierarchy would be recorded for every observation:

- treatment arm;
- randomized donor or animal ID;
- randomization block, litter, cage, site, batch, or matched pair, if applicable;
- tissue/sample ID;
- field ID nested within donor;
- cell ID nested within field and donor;
- assay batch, plate, operator, instrument, and acquisition time.

If treatment is administered at a level above the donor, such as cage or litter, that higher level would become the experimental unit unless the design permits independent treatment assignment within it.

### 1.3 Calibrate unknown design parameters

Because the exact numbers and variance components are unavailable, a proposed blinded pilot or historical-data calibration would estimate:

- between-donor variance;
- between-field variance within donor;
- cell-level residual variance;
- intraclass correlations;
- expected cells and fields per donor;
- donor-to-donor differences in cell yield;
- dropout and assay-failure rates;
- prevalence of target cell types;
- plausible treatment-effect sizes.

Simulations would then reproduce the planned hierarchy and compare candidate donor counts, allocations, and sampling depths. The selected design would target prespecified power and interval coverage for the donor-level estimand. Increasing donor count would be prioritized once additional cells per donor provide little gain in the precision of donor summaries.

No effect estimate from an unblinded pilot would be used to adapt a confirmatory test unless that adaptation were prespecified and statistically accounted for.

### 1.4 Quality-control rules

Before treatment labels are inspected, the protocol would define:

- donor/animal eligibility and exclusion criteria;
- minimum sample integrity and assay-quality requirements;
- cell- and field-level quality filters;
- rules for doublets, segmentation failures, dead cells, low-complexity measurements, or contaminated fields;
- minimum information needed to calculate a donor-level endpoint;
- handling of missing fields, failed assays, and low-yield donors;
- whether failed measurements may be repeated and under what conditions.

A donor would not be excluded solely because its outcome is extreme. Outcome-dependent exclusions would be prohibited unless based on independently adjudicated technical failure.

---

## 2. Independent units and replication

The proposed experimental unit would be the **donor or animal to which treatment is independently assigned**. Consequently:

- \(n\) for treatment replication would be the number of randomized donors or animals, not the number of cells.
- Fields and cells would be subsamples nested within donors.
- Technical repeats would be averaged or modeled as technical variation and would not increase randomized-unit \(n\).
- If there are repeated time points, the donor would remain the independent unit, with time nested or repeated within donor.
- If allocation is blocked or paired, inference and resampling would preserve those blocks or pairs.

A flow diagram would distinguish randomized units, sampled tissues, observed fields, detected cells, retained cells, and analyzed donors.

---

## 3. Allocation and blinding

### 3.1 Randomization

Donors or animals would be randomized to treatment using a concealed, reproducible schedule. Randomization could be blocked on prespecified strong prognostic factors, such as sex, baseline value, site, age group, litter, or assay batch, provided block sizes and analysis are specified in advance.

Cells or fields would not be described as randomized to treatment unless they genuinely receive independent treatment assignments.

### 3.2 Batch balancing

Where possible, samples from different treatment arms would be balanced across:

- collection days;
- tissue-processing runs;
- plates;
- sequencing lanes or imaging sessions;
- instruments;
- operators.

Batch should not be perfectly confounded with treatment. If unavoidable, the treatment effect would not be separable from batch without additional assumptions and the study might need redesign rather than statistical adjustment.

### 3.3 Blinding

Proposed blinding would include:

- masked treatment labels during sample processing and image acquisition;
- masked identifiers during quality control and feature extraction;
- locked exclusion and transformation rules before unblinding;
- a held-out donor set whose outcomes are not inspected during model selection.

---

## 4. Intervention and sampling

- Treatment would be administered at the randomized-unit level according to a standardized protocol.
- Sampling time, anatomical location, field-selection method, and number of intended fields would be standardized across arms.
- Fields would preferably be selected by systematic or random sampling rather than chosen for apparent response.
- Sampling depth per donor would be approximately balanced where feasible.
- All eligible cells in selected fields, or a reproducible probability sample, would be measured.
- Reasons for unequal cell yield would be recorded because treatment-related yield can cause informative cluster size.

If treatment affects survival, tissue yield, or the probability that a cell is observed, analyses restricted to retained cells may describe a selected post-treatment population. The study would therefore report yield and missingness as outcomes or process measures where biologically relevant.

---

## 5. Measurements and controls

### 5.1 Proposed primary measurement

The primary endpoint would be calculated for each donor using a locked procedure. Depending on the assay, this could be:

- a mean, median, proportion, rate, count, or transformed abundance;
- a normalized pseudobulk molecular count;
- a donor-level model coefficient estimated from that donor’s cells.

The aggregation method would match the measurement distribution. For example, count assays would generally use summed counts plus an appropriate exposure or library-size offset rather than an unqualified mean of normalized cell values.

### 5.2 Controls

Proposed controls would include:

- untreated, vehicle, sham, or reference controls as scientifically appropriate;
- technical positive and negative controls;
- batch controls or common reference samples;
- blinded replicate measurements on a subset of samples;
- baseline measurements, if available and obtained before treatment;
- null features or negative-control outcomes expected not to respond, where scientifically defensible.

Technical controls would diagnose assay behavior but would not substitute for independently treated donors.

---

## 6. Proposed statistical analysis

### 6.1 Primary pseudobulk analysis

For each donor and prespecified outcome or cell type, the investigators would construct a donor-level summary. The primary model would compare these summaries between treatment arms while incorporating prespecified blocking or baseline covariates.

Key principles:

- Each donor would ordinarily receive equal inferential weight unless precision weights are prespecified and validated.
- The denominator degrees of freedom and uncertainty would reflect donor count.
- Cell number would contribute to the precision of the donor summary but not create additional treatment replicates.
- Contrasts, transformations, covariates, and multiplicity correction would be locked before validation.

If a cell type is absent from some donors, absence would not automatically be treated as missing. The protocol would distinguish biological zero, sampling zero, and assay failure.

### 6.2 Supporting hierarchical analysis

A proposed multilevel model would retain the nested data, for example:

- fixed effect for treatment;
- random intercept for donor;
- optional random effect for field nested within donor;
- repeated-time structure where applicable;
- appropriate distribution and link for continuous, count, binary, or zero-inflated outcomes.

Random slopes would be included only when supported by the design and donor count. Small-sample corrections or unit-level resampling would be used because asymptotic cluster-robust standard errors may be unreliable with few donors.

The hierarchical model would be a corroborating analysis unless simulation demonstrates adequate calibration for the available number of randomized units. Agreement would be assessed in effect direction and magnitude, not only by whether two \(p\)-values cross a threshold.

### 6.3 Grouped resampling

All resampling would preserve donor clusters.

**Proposed donor bootstrap:**

1. Sample donors or animals with replacement within treatment arm or randomization stratum.
2. Include all retained fields and cells belonging to each sampled donor.
3. Recompute pseudobulk summaries and refit the complete analysis.
4. Use the distribution of donor-level contrasts for uncertainty or stability assessment.

If within-donor sampling variability is important, a secondary two-stage bootstrap could first resample donors and then fields within sampled donors. Cells alone would never be bootstrapped as if independent treatment replicates.

**Sensitivity analyses:**

- leave-one-donor-out refitting;
- leave-one-block-out refitting where feasible;
- balanced subsampling of cells or fields within each donor to test dependence on unequal sampling depth;
- comparisons with and without prespecified precision weighting;
- analyses of all randomized donors under an intention-to-treat principle, where applicable.

### 6.4 Null calibration

Before confirmatory interpretation, the proposed pipeline would be calibrated under a no-treatment-effect null.

**Randomization-based calibration:**

- Permute treatment labels among donors or animals, not among cells.
- Preserve matched pairs, blocks, allocation ratios, and any restricted randomization.
- For each permutation, rerun aggregation, modeling, contrasts, and multiplicity correction.
- Compare the observed statistic with this unit-level null distribution.

**Simulation calibration:**

- Simulate nested outcomes using blinded or external estimates of between-donor, field, and cell variance.
- Include realistic imbalance, dropout, cell yield, and intraclass correlation.
- Assess false-positive rate, confidence-interval coverage, bias, and power.
- Repeat under model misspecification, outliers, informative cluster size, and small independent-unit counts.

A model would be retained for confirmatory use only if its null behavior and interval coverage meet prespecified tolerances. If asymptotic and permutation results differ materially, the design-respecting permutation or another demonstrably calibrated method would receive greater weight, subject to the actual randomization scheme.

### 6.5 Held-out validation

The validation split would occur at the **donor/animal level** before outcome-driven model selection. No cells from a held-out donor could appear in training.

A proposed sequence would be:

1. Allocate donors to development and validation sets, stratified by treatment and important blocks.
2. Use development donors to select transformations, features, tuning parameters, and any prediction model.
3. Lock the complete pipeline and directional hypothesis.
4. Apply it once to held-out donors.
5. Estimate the treatment contrast and uncertainty using held-out donors as the independent units.

The held-out analysis would report effect magnitude and interval, not merely significance. If the available donor count is too small to support both model development and a credible holdout, the preferred alternatives would be:

- develop the method using external or historical data and reserve all current donors for validation;
- obtain an additional independent donor cohort;
- use donor-level cross-validation for exploratory model selection while explicitly stating that it is not equivalent to external confirmation.

Repeated random cell-level train/test splits would be prohibited because they leak donor-specific information.

### 6.6 Donor-level versus cell-level inference

The report would separate:

- **Donor-level treatment inference:** whether average donor outcomes differ by assigned treatment.
- **Cell-level descriptive inference:** distributions and heterogeneity among observed cells conditional on sampled donors.
- **Predictive inference:** whether a locked model predicts outcomes in new donors.

A cell-level treatment coefficient from a hierarchical model would be interpreted conditional on the model and donor structure. It would not be presented as having a sample size equal to the number of cells.

---

## 7. Proposed acceptance and stopping criteria

### 7.1 Analysis acceptance

A confirmatory donor-level conclusion would require all of the following:

1. The treatment contrast is estimated using randomized units as replicates.
2. The prespecified primary test passes the locked error or multiplicity criterion.
3. The effect estimate is compatible with the prespecified biologically meaningful direction and magnitude.
4. Unit-level permutation or simulation shows acceptable null calibration.
5. Results are not driven entirely by one donor, one block, or a treatment-confounded batch.
6. The held-out donor analysis shows a compatible direction and an effect interval that does not rule out the prespecified meaningful effect criterion, according to a rule fixed before unblinding.
7. Missingness, cell yield, or post-treatment selection does not provide a more plausible explanation without qualification.

Failure of one item would lead to an inconclusive or exploratory conclusion, not automatic declaration of no biological effect.

### 7.2 Enrollment and assay stopping

Stopping rules would be based on randomized units and prespecified feasibility criteria, not on accumulated cell counts or repeatedly inspected significance.

Proposed rules would include:

- stop or redesign if treatment is confounded with batch;
- pause if assay-control failure exceeds a prespecified calibration-derived limit;
- replace technical measurements only under blinded, predefined rules;
- conduct blinded sample-size re-estimation using pooled variance, if planned;
- stop for futility, efficacy, or safety only under a prespecified sequential design with appropriate error control.

A maximum donor/animal enrollment and minimum analyzable donor count would be selected through the variance and power calibration, not invented after observing results.

---

## 8. Troubleshooting and sensitivity analyses

| Problem | Proposed response |
|---|---|
| Very few independent donors | Emphasize estimates and wide intervals; use exact/restricted permutation if feasible; avoid complex random-effects structures; seek an independent cohort. |
| Many cells but imprecise donor effect | Add donors rather than more cells once donor summaries are stable. |
| Unequal cells per donor | Use equal-donor pseudobulk as primary; examine balanced subsampling and informative-cluster-size sensitivity. |
| High intraclass correlation | Report it and use unit-aware uncertainty; do not interpret it alone as disproving the effect. |
| Pseudobulk and hierarchical estimates differ | Check weighting, link scale, nonlinear aggregation, cell composition, informative yield, and model misspecification. |
| One donor changes the conclusion | Report leave-one-donor-out results; classify the finding as fragile unless independently replicated. |
| Treatment alters cell composition | Separate composition outcomes from within-cell-type outcomes; avoid conditioning interpretations that obscure treatment-induced selection. |
| Batch is partly imbalanced | Adjust only if treatment remains identifiable; perform within-batch contrasts or restricted permutation where justified. |
| Batch perfectly matches treatment | Do not claim treatment identification; repeat or redesign with crossed treatment and batch. |
| Too few donors for a holdout | Use external development data or recruit a separate validation cohort; label internal donor-level cross-validation exploratory. |
| Cell-level significance but donor-level uncertainty | Report the cell pattern descriptively; do not claim replicated treatment efficacy. |
| Donor-level estimate remains similar but significance is lost after clustering | Report the similar estimate with wider uncertainty; do not infer that the point estimate is false solely from the changed \(p\)-value. |

---

# Reporting requirements

For every arm and analysis set, the proposed report would provide both independent-unit and observational-unit counts:

- donors/animals randomized;
- donors/animals receiving treatment;
- donors/animals sampled;
- donors/animals passing QC;
- donors/animals included in primary, hierarchical, and validation analyses;
- fields intended, observed, excluded, and analyzed;
- cells detected, excluded, and analyzed;
- per-donor distributions of field and cell counts, not only totals;
- counts by cell type and time point;
- reasons for every donor-, field-, and cell-level exclusion;
- number of development and held-out donors by arm;
- number of permutations or bootstrap replicates used;
- missingness and assay-failure counts by treatment arm.

Results would include donor-level effect estimates, confidence or credible intervals, exact or calibrated \(p\)-values where applicable, intraclass-correlation estimates with uncertainty, and donor-level plots overlaid on cell-level distributions. Cell counts would never be used as the treatment replication count.

---

# Alternatives and limits

- **Pseudobulk** is transparent and directly aligns treatment inference with randomized units, but it may discard within-donor structure and can be unstable for rare cell types.
- **Hierarchical models** use all measurement levels and can estimate heterogeneity, but their validity depends on distributional assumptions and may be fragile with very few donors.
- **Unit-level permutation** closely follows randomization but may have coarse resolution when donor numbers are small or when the allocation scheme permits few permutations.
- **Grouped bootstrap** assesses donor-to-donor stability but can also be unreliable with extremely few independent units.
- **Held-out validation** protects against model-selection optimism but reduces development and validation precision unless enough donors are available.

No protocol can recover independent treatment replication from additional cells alone. With very small donor or animal \(n\), model-based tests may still be informative if well calibrated, but precision and robustness will remain limited. The final recommendation would therefore depend most strongly on calibrated between-donor variance, the number and allocation of randomized units, treatment–batch identifiability, and the availability of a genuinely independent validation cohort.
