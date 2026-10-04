# GPT-6 Astra / inf-d03

Original final answer, shared by both scoring rounds.

## Recommendation and status

**Use the donor or animal—not the cell or field—as the independent treatment replicate.** The proposed primary analysis would compare donor-level outcomes, with a hierarchical analysis addressing within-donor structure and heterogeneity. Resampling, null calibration, and held-out validation would all preserve donor membership.

**All experiments, measurements, analyses, and validation steps below are proposed. No completed results are implied.** Donor numbers, cell counts, effect sizes, variance components, assay details, and numerical decision thresholds are unreported. They would be established through calibration and prespecification, not invented.

## Evidence-to-inference-to-conclusion chain

Evidence locations refer to the supplied packet; it provides no page numbers or experimental methods.

| Supplied evidence and location | Inference | Proposed consequence |
|---|---|---|
| **Source summary: pseudoreplication definition.** Dependent observations or treatment subsamples must not be treated as independent replication. | Numerous cells can improve characterization of a donor without supplying numerous independent treatment assignments. | Preserve donor membership in analysis, resampling, and validation. |
| **Source summary: randomized treatment level defines the experimental unit; biological and observational units may differ.** | A cell may be the measured biological object while the donor remains the experimental unit. | Distinguish donor-level treatment effects from cell-level distributions and within-donor heterogeneity. |
| **Source summary: very small independent sample sizes affect precision and robustness but do not automatically invalidate every model-based test.** | Neither automatic rejection of all models nor reliance on large-sample approximations is warranted. | Calibrate procedures at the intended donor count and state their assumptions and resolution limits. |
| **Source summary: clustering can change uncertainty without changing a point estimate; high intraclass correlation or lost significance does not prove a false biological effect.** | Changes in uncertainty must be distinguished from changes in estimated biological magnitude. | Report estimates and intervals, not just significance transitions. |
| **Hypothetical constraints: donor/animal treatment assignment, repeated cellular/field measurements, and unavailable numerical parameters.** | The design requires hierarchical handling and parameter calibration. | Conduct a proposed pilot/calibration phase before locking a confirmatory protocol. |

## Ordered proposed protocol

### 1. Preparation and quality checks

Create a protocol, data dictionary, and analysis plan linking every observation to:

- donor or animal identifier;
- assigned treatment and allocation block;
- specimen, field, and cell identifiers, as applicable;
- sampling time, processing batch, plate or imaging run;
- inclusion status, exclusion reason, and missingness reason.

**Proposed calibration experiment:** use a pilot set, separate from confirmatory validation where feasible, to characterize measurement reliability, donor-to-donor variation, within-donor variation, sample yield, and batch effects. Pilot estimates would be treated as uncertain inputs rather than fixed population truths.

Proposed quality checks would identify:

- duplicated or incorrectly linked observations;
- segmentation or measurement artifacts;
- inconsistent measurement scales;
- treatment-associated differences in missingness, yield, or quality;
- confounding of treatment with batch, collection time, or processing order.

Quality thresholds would be calibrated against measurement reliability and finalized without optimizing the treatment contrast. A biologically responsive feature—such as cell loss—would not automatically be classified as technical failure. Excluding affected cells could change the question from an effect on the sampled population to an effect among surviving or measurable cells.

### 2. Define independent units, estimands, and sample size

**Experimental unit:** each donor or animal independently assigned treatment.

**Observational units:** cells, fields, or other measurements nested within that donor. Fields would not become treatment replicates merely because they were sampled separately.

The proposed primary estimand would be specified before analysis, for example:

> The treatment difference in the average donor-level phenotype, over the prespecified donor population and sampling window.

Donors would ordinarily receive equal weight for an “average donor” estimand. A pooled-cell average would instead weight donors according to their observed cell yield unless corrected, potentially answering a different question.

Separate secondary estimands could describe:

- treatment differences in donor-specific cell-state proportions;
- within-donor distributional changes;
- treatment differences in donor-specific variability;
- effects within prespecified cell classes.

These would remain donor-replicated treatment comparisons. A description of cells within the observed donors would be labeled as such, not presented as independent replication across cells.

**Proposed sample-size calibration:** simulate candidate donor counts and cells/fields per donor across plausible ranges of:

- donor and residual variance;
- intraclass correlation;
- unequal sampling depth;
- missing donors and missing measurements;
- scientifically meaningful effects.

The biologically meaningful effect would be defined from the study objective, not selected to match an optimistic pilot result. Designs would be compared on interval precision, false-positive calibration, and power. Where donor variation dominates under the simulated model, adding donors would generally be prioritized over collecting substantially more cells from existing donors.

### 3. Allocation and blinding

For a prospective experiment, treatment would be randomized at donor/animal level. Any stratification or blocking would use prespecified pretreatment characteristics.

The proposed allocation process would:

1. document the allowed assignments;
2. balance treatments across processing batches where feasible;
3. conceal allocation during enrollment or sample inclusion where practicable;
4. blind measurement, annotation, and quality review;
5. retain a reproducible allocation record.

The actual allocation scheme would determine later permutation restrictions.

**Limit:** “assigned” does not establish that allocation was randomized. If analyzing existing nonrandomized assignments, donor counts would be reported as assigned rather than randomized. Covariate-adjusted comparisons could be proposed, but causal interpretation and permutation validity would require additional, explicitly stated assumptions.

### 4. Intervention and sampling

The proposed intervention dose, timing, delivery, and sampling window would be calibrated in a preliminary feasibility experiment appropriate to the biological system. None is specified in the packet.

A standardized sampling plan would then define:

- anatomical or specimen locations, if relevant;
- field-selection rules;
- cell-selection and identification rules;
- collection times;
- target sampling depth and handling of shortfalls.

Fields would be selected systematically or randomly rather than chosen for apparent response. Technical repeat measurements would retain their donor identity.

If longitudinal sampling were used, repeated times would remain nested within donor. Treatment timing, attrition, and deviations would be recorded. Unequal cell counts would not be hidden: their possible relationship to treatment and phenotype would be investigated.

### 5. Measurements

The proposed plan would prespecify one primary endpoint, its scale, and its donor-level construction. Suitable constructions would depend on the eventual assay:

- **Continuous phenotype:** a donor-level mean, median, or other prespecified summary.
- **Cell-state prevalence:** each donor’s numerator and eligible-cell denominator.
- **Count-based molecular measurement:** donor-level aggregation with assay-appropriate normalization or exposure handling.
- **Spatial phenotype:** a donor-level summary incorporating the planned field-sampling design.

“Pseudobulk” would mean an explicitly defined aggregation within donor, not arbitrary summation across incompatible scales.

A proposed measurement-validation subset would include blinded repeat measurement or annotation to assess technical reliability. Such repeats would characterize measurement error, not increase the number of randomized units.

### 6. Controls

Proposed controls, conditional on the eventual intervention and assay, would include:

- a contemporaneous comparator group allocated at donor/animal level;
- vehicle, sham, or handling controls where scientifically appropriate;
- assay background or negative controls;
- a positive assay control where one can be justified;
- balanced processing and reference material across batches where feasible.

Technical controls would assess assay performance, not substitute for treatment replication.

Complete treatment–batch confounding would trigger redesign or a limitation on interpretation; adding a batch term would not create information that the design failed to supply.

### 7. Primary analysis, hierarchical comparison, and grouped resampling

#### 7a. Proposed donor-level primary analysis

For donor \(i\), let \(S_i\) be the prespecified summary and \(T_i\) its treatment assignment. For a continuous endpoint, a candidate comparison would be

\[
S_i=\alpha+\beta T_i+\gamma^\top X_i+\varepsilon_i,
\]

where \(X_i\) contains prespecified pretreatment covariates or allocation-block terms.

The endpoint distribution would determine the actual model. The number of independent donors—not cells—would govern available treatment replication. Covariate complexity would be restricted according to the donor count and calibration results.

#### 7b. Proposed hierarchical comparison

A candidate hierarchical model would be

\[
g\{E(Y_{ij}\mid b_i)\}
=\alpha+\beta T_i+\gamma^\top X_i+b_i,
\]

with donor effect \(b_i\). Field-within-donor or repeated-time components would be added only where supported by the measurement structure.

The response distribution, link, and variance structure are **unreported parameters/model choices**. They would be selected through assay considerations and proposed pilot checks. A random intercept would not automatically be assumed to capture every relevant dependence.

Both approaches would be compared on a matched estimand. For nonlinear models, a conditional model coefficient need not equal a marginal donor-level contrast; an appropriate donor-standardized contrast would therefore be reported when needed.

Disagreement would prompt examination of weighting, endpoint construction, missingness, scale, and model assumptions—not selection of whichever method gives the smaller \(p\)-value.

#### 7c. Proposed grouped resampling

For a donor-population bootstrap:

- resample whole donors;
- carry each selected donor’s associated observations together;
- preserve treatment-group sizes where appropriate;
- resample complete blocks or matched groups when required by the design;
- refit the complete prespecified analysis within each resample.

Cells would not be bootstrapped as though they were independent donors. An optional multistage bootstrap could additionally resample fields or cells within selected donors if that matched the sampling process. It would still not create new treatment assignments.

With very few donors, bootstrap distributions could be unstable. Resampling would therefore supplement, rather than replace, null calibration and assumption checks.

### 8. Null calibration and sensitivity analysis

#### Proposed allocation-based calibration

Where treatment is randomized, treatment labels would be reassigned **only at the randomized-unit level**, using assignments permitted by the actual design. All cells from a donor would move with that donor’s label.

- Blocked designs would use block-restricted assignments.
- Paired designs would preserve the pairing restrictions.
- Cell-wise treatment-label shuffling would not be used.

Exact enumeration would be proposed when feasible; otherwise, a prespecified number of sampled assignments would be used. The null hypothesis—such as a sharp no-treatment-effect null—would be stated explicitly. An exact randomization test would not automatically be described as exact for every possible average-effect null.

#### Proposed simulation-based calibration

Simulations would generate donor clusters under a specified null, preserving or varying:

- plausible intraclass correlations;
- donor counts and unequal cell counts;
- field-level dependence;
- batch structure;
- missingness patterns;
- outcome-distribution and variance-model misspecification.

The full pipeline, including permitted preprocessing and model selection, would be rerun. Calibration outcomes would include false-positive frequency, interval coverage, convergence, and estimator bias.

The significance level \(\alpha\), acceptable calibration tolerance, and Monte Carlo precision target would be chosen and documented before confirmatory analysis. Simulation repetitions would be increased until calibration uncertainty was sufficiently narrow for that decision.

Non-null simulations would separately assess power and precision. Passing calibration under selected scenarios would support performance **under those scenarios**, not prove validity under all possible data-generating mechanisms.

### 9. Held-out validation

The proposed split would occur **by donor before data-dependent training or feature selection**. No cells, fields, or repeated samples from a held-out donor would enter training.

A development set would be used to fix:

- preprocessing and normalization rules;
- feature selection or phenotype definitions;
- model specification;
- decision thresholds;
- the validation endpoint.

The locked pipeline would then be applied to held-out donors. Validation would evaluate the treatment contrast, uncertainty, measurement stability, and prespecified performance criteria—not merely cell-level prediction accuracy.

Where feasible, a separate donor cohort and processing run would provide stronger evidence of transportability than a within-cohort split.

If donor numbers were insufficient for a useful holdout, grouped cross-validation or leave-one-donor-out validation could be proposed for development assessment. These would be labeled as internal validation, not equivalent to an independent replication. Fold results would not be counted as independent treatment replicates. A new donor cohort would remain the preferred confirmatory next step.

### 10. Acceptance, stopping, and troubleshooting

#### Proposed acceptance criteria

Before unblinding confirmatory outcomes, the study would define numerical criteria for:

1. measurement reliability and protocol adherence;
2. null calibration and interval coverage;
3. primary effect magnitude and precision;
4. held-out performance or replication;
5. acceptable sensitivity to donor influence and plausible modeling alternatives.

A positive confirmatory conclusion would require the prespecified evidentiary criteria, not simply a significant cell-level test. A nonsignificant result would not establish absence of a biologically meaningful effect; an equivalence claim would require a prespecified margin and an adequately precise analysis.

#### Proposed stopping rules

Enrollment and sampling would follow a fixed donor-count design or a prospectively calibrated sequential design. Investigators would not repeatedly add cells until significance appeared.

Assay failure or excessive missingness would trigger a prespecified pause and review. If too few donors remained for useful precision, or too few allowed assignments existed to attain the intended randomization-test threshold, the study would be designated exploratory or additional donors sought under an amended plan.

#### Proposed troubleshooting

| Problem | Proposed response |
|---|---|
| One donor dominates the estimate | Inspect donor-level displays and leave-one-donor-out estimates; investigate errors without outcome-driven exclusion. |
| Cell yield differs by treatment | Examine whether yield is an outcome or selection mechanism; compare justified donor-weighting and missingness sensitivities. |
| Hierarchical model is unstable | Reduce unsupported complexity and emphasize the prespecified donor-level analysis; disclose instability. |
| High intraclass correlation | Revise uncertainty and future sampling allocation; do not infer that the effect is false. |
| Significance disappears after clustering | Report whether the point estimate changed, the interval widened, or both. |
| Null calibration fails | Revise the development procedure and recalibrate before validation; do not tune against held-out outcomes. |
| Held-out validation fails | Investigate measurement drift, donor composition, and model dependence; report failure without redefining success retrospectively. |

## Proposed reporting package

For each treatment arm and analysis set, the report would give:

- **randomized-unit counts:** allocated, treated, sampled, excluded, analyzed, and held out;
- **observed-unit counts:** specimens, fields, cells, and technical repeats;
- the distribution of cells/fields per donor, not only the pooled total;
- exclusions and missingness at each level;
- the experimental unit, estimand, weighting, and sampling scheme;
- donor-level displays, treatment estimates, and uncertainty intervals;
- hierarchical variance estimates and their uncertainty;
- resampling units, permutation restrictions, simulation assumptions, and validation splits;
- primary, secondary, exploratory, and multiplicity-adjusted analyses clearly distinguished.

The governing interpretation would be: **many measured cells can strengthen measurement of each donor, but donor/animal assignments supply the independent replication for treatment inference.** Whether the proposed study supports a biological conclusion would depend on calibrated uncertainty, effect magnitude, design validity, and donor-held-out validation—not on the pooled cell count alone.
