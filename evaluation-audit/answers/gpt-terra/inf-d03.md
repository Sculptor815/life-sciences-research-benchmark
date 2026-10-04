# GPT-5.6 Terra / inf-d03

Original final answer, shared by both scoring rounds.

# Proposed analysis and validation protocol for donor-/animal-randomized, cell-/field-measured studies

**Recommendation:** Make the donor or animal that received randomized treatment the primary inferential unit. Analyze cells and fields as nested measurements that improve measurement of each donor/animal, not as independent treatment replicates. Pre-specify a donor-level (or animal-level) primary endpoint, validate it with grouped resampling and treatment-label permutations at the randomized-unit level, and confirm any data-derived finding in held-out randomized units or an independent cohort.

**Status:** All experiments, procedures, analyses, thresholds, and decision rules below are **proposed**. Exact donor numbers, cell/field counts, effect sizes, intraclass correlations (ICCs), variance components, and assay-failure rates are unreported and must be calibrated before a definitive study.

---

## 1. Evidence-to-inference-to-conclusion chain

### Evidence
The supplied evidence packet states that:

1. Pseudoreplication occurs when treatment subsamples or otherwise dependent observations are treated as independent replicates.
2. The level at which treatment is randomized defines the experimental unit.
3. Observational units (cells, fields, images) and biological units (donors, animals) can differ.
4. Small numbers of independent units reduce precision and robustness but do not automatically invalidate every model-based analysis.
5. Accounting for clustering can change uncertainty without changing the estimated effect.
6. High ICCs or loss of nominal significance after clustering do not, by themselves, prove that an apparent biological effect is false.

### Inference
If treatment is assigned to donors or animals and many cells or fields are measured within each treated unit, cells/fields from the same donor share treatment assignment and may share donor-specific biology, handling, sampling, and batch effects. They therefore cannot generally be exchanged as independent treatment replicates.

### Conclusion
The primary comparison must be based on the number of independently randomized donors/animals. Cell- and field-level observations should be retained to measure donor-level outcomes more precisely and to model within-donor variation, but they must not inflate the apparent treatment sample size. Resampling, permutations, data splitting, and validation must preserve donor/animal membership.

**Evidence location:** Fixed evidence packet, “Source summary and curator interpretation.”

---

## 2. Define the scientific estimand before collecting definitive data

The protocol should specify which treatment effect is intended, because different summaries answer different questions.

### Proposed primary estimand
For a donor-/animal-level endpoint \(S_i\), estimate the average treatment effect across randomized units:

\[
\Delta = E(S_i \mid T_i=1)-E(S_i \mid T_i=0),
\]

where \(i\) indexes donors or animals and \(T_i\) is randomized treatment assignment.

Each \(S_i\) should summarize that donor/animal using a pre-specified sampling and aggregation rule.

### Examples of proposed donor-level summaries
The exact choice depends on the assay:

- **Continuous cell/field measurement:** donor mean, trimmed mean, median, or a pre-specified robust location summary across sampled fields/cells.
- **Binary cell phenotype:** donor-specific proportion positive, with both numerator and denominator retained.
- **Cell-type abundance:** donor-specific fraction or density, defined with an explicit denominator such as total cells assessed, tissue area, or sampled volume.
- **Count or molecular data:** donor-level pseudobulk count/profile within a pre-specified cell class, analyzed using an appropriate donor-level count or expression model.
- **Repeated fields within tissue regions:** a donor-level region-standardized summary if regions are sampled systematically.

### Important distinction
A pooled analysis over all observed cells estimates an **observed-cell-weighted** quantity: donors with more captured cells contribute more. That can be useful descriptively, but it is not automatically the same as the treatment effect averaged across donors/animals. The proposed primary analysis should use the donor-/animal-level estimand unless the protocol explicitly justifies a different target population.

---

# 3. Ordered operational protocol

## A. Preparation and quality checks

### A1. Establish the hierarchy and identifiers
Before treatment allocation, create linked identifiers for:

- randomized unit: donor or animal;
- any higher-level shared unit: cage, litter, clinic day, tissue-processing batch, operator, sequencing run, imaging session;
- specimen and tissue region;
- field/image;
- cell/segmentation object;
- technical replicate.

Construct a hierarchy diagram, for example:

\[
\text{batch/cage} \rightarrow \text{donor or animal} \rightarrow \text{specimen} \rightarrow \text{field} \rightarrow \text{cell}.
\]

This diagram is a required quality-control document because it determines what may be treated as independent.

### A2. Confirm the true randomized unit
The nominal donor/animal is the experimental unit only if its treatment was independently assigned.

Examples requiring reassessment:

- If all animals in a cage receive the same exposure and cannot be independently exposed, the cage may be the effective randomized unit.
- If donors are processed together in a treatment-specific batch, treatment and batch may be inseparable.
- If repeated tissues from one animal receive the same assigned treatment, tissues are subsamples of that animal, not separate treatment replicates.

**Proposed rule:** use the highest level at which treatment was independently randomized and interference is plausibly limited as the randomized unit for confirmatory inference.

### A3. Pre-specify outcomes and analysis choices
Before unblinding outcomes, register or lock:

- one primary outcome and one primary donor-level summary;
- primary treatment contrast and directionality;
- covariates justified before treatment, such as baseline value, sex, blocking factor, or cohort;
- handling of repeated regions, fields, and technical replicates;
- planned transformations and model family;
- exclusion rules for donors/animals, fields, and cells;
- missing-data rules;
- multiplicity control for secondary endpoints or high-dimensional features;
- the allocation-constrained permutation scheme;
- the held-out validation plan.

For high-dimensional assays, distinguish:

1. a **confirmatory, pre-specified endpoint**, if feasible; and  
2. an **exploratory discovery analysis** requiring held-out confirmation.

### A4. Proposed pilot calibration
Run a treatment-blinded or treatment-neutral pilot, if feasible, to estimate:

- cells and fields obtainable per donor/animal;
- assay failure and attrition rates;
- variation between donors/animals, fields, and cells;
- ICCs at donor and field levels;
- effects of batch, operator, and processing date;
- stability of donor summaries as additional fields/cells are sampled.

Use these estimates, with uncertainty, in simulation-based design calibration. The simulation should vary plausible:

- numbers of independently randomized units;
- allocation ratio;
- donor-level variance;
- field/cell-level variance;
- ICC;
- missingness;
- effect size scenarios;
- batch imbalance;
- multiplicity burden.

The number of **donors/animals**, not cells alone, should be selected to achieve the pre-specified precision or power target. Increasing cells per donor may reduce measurement error, but it cannot generally replace additional independently randomized donors/animals.

---

## B. Independent units, allocation, and blinding

### B1. Allocation
Randomize treatment at the verified experimental-unit level. Use blocked or stratified randomization when necessary to balance important pre-treatment factors, such as cohort, sex, site, baseline phenotype, or processing day.

The randomization record should retain:

- random seed or auditable allocation procedure;
- block/stratum membership;
- date and time of assignment;
- any deviations from assigned treatment.

If allocation is blocked, all later permutation tests must permute treatment labels **within the same blocks or strata**.

### B2. Blinding
Proposed blinding procedures:

- use coded donor/animal and specimen identifiers;
- blind field selection, image annotation, segmentation review, and quality-control review to treatment;
- blind analysts during preprocessing and feature construction when feasible;
- unblind treatment only after the preprocessing and analysis plan are locked.

If complete blinding is impossible, document which steps were unblinded and perform sensitivity analyses for operator or batch effects.

---

## C. Intervention and sampling

### C1. Intervention fidelity
Record proposed treatment delivery, timing, dose/exposure, protocol deviations, adverse events, and co-interventions at the randomized-unit level.

Define in advance whether the primary analysis is:

- **intention-to-treat:** comparison by assigned treatment; or
- **per-protocol:** restricted to predefined adherence criteria.

The intention-to-treat analysis is generally the primary randomized comparison when treatment assignment is the basis for inference. Per-protocol analyses should be secondary and clearly labeled.

### C2. Sampling plan
Avoid selecting visually interesting fields or cells after inspecting treatment-associated outcomes.

Proposed sampling methods include:

- systematic random fields across pre-specified tissue regions;
- fixed grid or randomized coordinate sampling;
- stratified random selection of regions if anatomy is heterogeneous;
- pre-specified numbers of fields per region, calibrated in the pilot;
- identical sampling rules across treatment arms.

Record the reason for every unavailable specimen, field, or cell. Do not treat a donor with many cells as more independent than a donor with few cells.

### C3. Treatment-related cell yield changes
If treatment changes tissue cellularity, viability, capture efficiency, or cell-type composition, this may be biologically meaningful rather than merely technical. Therefore, analyze separately:

1. **abundance/composition outcomes**, such as cells per area or fraction of a cell type; and  
2. **within-cell-type outcomes**, such as marker expression among a defined cell type.

Conditioning only on observed cells of a selected type can obscure a treatment effect on the abundance of that type. The denominator and inclusion rule must therefore be reported.

---

## D. Measurements and controls

### D1. Measurement quality control
Proposed pre-specified quality checks include:

- calibration and stability checks for instruments;
- image focus, illumination, segmentation, and artifact thresholds;
- molecular library quality, mapping/feature-detection quality, and contamination criteria where applicable;
- duplicate or repeated reference specimens across batches;
- blinded review of a sample of fields/cells;
- documented software versions and fixed preprocessing pipelines.

Cell/field exclusions should use treatment-blind, technically justified rules. Report exclusions by treatment arm and by hierarchical level.

### D2. Proposed controls
Include, where scientifically appropriate:

- negative or sham treatment controls;
- positive assay controls demonstrating that the assay can detect a known technical or biological signal;
- reference materials or repeated control specimens across batches;
- blinded duplicate specimens for technical reproducibility;
- negative-control outcomes or markers expected not to respond to treatment, if such outcomes are justified.

These controls assess assay performance or bias. They do **not** create additional independent treatment replicates.

---

# 4. Proposed primary and supporting analyses

## A. Primary donor-/animal-level comparison

For each randomized unit, calculate the pre-specified summary \(S_i\). Compare treatment arms using a donor-/animal-level contrast, preferably adjusted for randomization blocks and pre-specified baseline covariates.

For a simple unblocked design, the primary estimate may be:

\[
\widehat{\Delta} = \overline{S}_{T=1} - \overline{S}_{T=0}.
\]

For blocked designs, estimate and combine within-block treatment contrasts.

Display raw donor/animal summaries, not only pooled cell distributions. Plots should identify the randomized unit, show the number of nested observations per unit, and avoid graphs that visually imply cells are independent treatment replicates.

## B. Pseudobulk or donor-summary analysis

### Proposed use
Use pseudobulk/donor-summary analysis as the primary or major sensitivity analysis when the target is a donor-level molecular, imaging, composition, or phenotype outcome.

Examples:

- aggregate expression/counts across cells from each donor within a pre-specified cell type;
- calculate each donor’s proportion of positive cells;
- calculate a donor-level mean or median field measurement;
- aggregate fields using fixed region weights.

The resulting analysis table should have one row per donor/animal per outcome or cell type. Treatment testing is then based on the number of donor/animal rows.

### Limits
Pseudobulk may discard information about within-donor heterogeneity and requires careful normalization. For compositional outcomes, define the denominator. For molecular counts, define the aggregation and normalization method before viewing treatment results. If treatment affects total captured cells, analyze that outcome separately rather than allowing an implicit normalization choice to hide it.

## C. Hierarchical analysis

As a complementary analysis, fit a multilevel model that explicitly represents nesting. A generic proposed model is:

\[
g\{E(Y_{ijk})\} =
\alpha + \beta T_i + \gamma^\top X_i + u_i + v_{ij},
\]

where:

- \(Y_{ijk}\) is a cell-level observation \(k\) in field \(j\) from donor/animal \(i\);
- \(T_i\) is treatment;
- \(X_i\) are pre-specified covariates or blocks;
- \(u_i\) is a donor/animal-level effect;
- \(v_{ij}\) is a field-level effect;
- \(g\) is chosen for the outcome type, such as identity, logit, or log.

Use model families appropriate to continuous, binary, proportion, or count outcomes. Assess residual behavior, overdispersion, separation, convergence, and sensitivity to distributional assumptions.

### Interpretation
The treatment coefficient estimates a treatment association while accounting for within-donor clustering. It does not make cells independent randomized replicates. With very few donors/animals, model-based uncertainty may be unstable; therefore pair this analysis with randomized-unit permutation tests and transparent donor-level displays.

## D. Grouped resampling

### Proposed bootstrap procedure
Resample **donors/animals**, not individual cells alone, within treatment arm and within randomization block where relevant. For each resample:

1. select randomized units with replacement;
2. retain all nested observations belonging to each selected unit;
3. optionally resample fields and then cells within selected donors if the target includes sampling uncertainty;
4. recompute the full donor-summary or hierarchical analysis.

Use the distribution of donor-grouped estimates for confidence intervals and sensitivity assessment.

### Limits
Grouped bootstrap intervals can be unstable with very few independent units. They must not be presented as solving low donor/animal replication. If donor numbers are very small, emphasize effect estimates, raw unit-level values, randomization-test results, and the limited attainable resolution.

---

# 5. Null calibration and randomization inference

## A. Proposed treatment-label permutation test
For the primary endpoint, calculate the observed donor-level test statistic. Then repeatedly permute treatment labels across **randomized donors/animals**, respecting the original allocation scheme:

- permute only within randomization blocks/strata;
- if cages or clusters were randomized, permute at that cluster level;
- retain every cell/field with its original donor/animal;
- recompute the entire pre-specified summary and test statistic for every permutation.

Compare the observed statistic with the randomization distribution. If all allowable allocations can be enumerated, use an exact test; otherwise use a Monte Carlo permutation procedure with its simulation uncertainty reported.

This calibration directly tests whether the observed donor-level contrast is unusual under assignments compatible with the original randomization.

## B. Pipeline-level null calibration
Before the definitive analysis, use pilot-derived or negative-control data to simulate null datasets across plausible ICC, variance, missingness, and imbalance scenarios. Apply the complete proposed pipeline, including:

- filtering and quality control;
- feature selection;
- aggregation;
- hierarchical modeling;
- multiplicity adjustment;
- permutation testing;
- held-out evaluation.

The goal is to verify that the chosen procedure controls false-positive behavior at the pre-specified nominal error rate under plausible null conditions.

Because variance components are unknown, use a range of plausible values rather than a single assumed value. If calibration shows anti-conservative false-positive rates, revise the preprocessing, model, randomization test, or multiplicity method before unblinding definitive results.

## C. Negative-control diagnostics
For justified negative-control outcomes, treatment-label permutations and model estimates should not show systematic treatment signals. A failure suggests batch confounding, leakage, incorrect blocking, or an analysis pipeline artifact; it does not establish a treatment effect.

---

# 6. Held-out validation

## A. Preferred validation: independent randomized cohort
The strongest proposed validation is a second, independently randomized donor/animal cohort processed in a different recruitment or experimental wave. Lock the discovery endpoint, feature definition, model, and direction of effect before analyzing the validation cohort.

A validated result should show:

- the pre-specified effect direction;
- compatible effect magnitude and uncertainty;
- donor-/animal-level evidence under the locked analysis;
- no material failure of quality-control or null-calibration diagnostics.

## B. If only one cohort is feasible
Reserve a donor-/animal-level held-out subset before exploratory analyses. Split at the randomized-unit level, stratified by treatment and blocks. All cells, fields, and technical replicates from a donor/animal must remain in the same split.

Use:

- a discovery subset for feature selection, threshold selection, or model development;
- a locked held-out subset for one final evaluation.

For predictive signatures, use nested grouped cross-validation: all preprocessing and feature selection occur within each training split, and evaluation occurs only on held-out donors/animals.

### Limitation
A held-out split reduces the number of randomized units available for discovery and validation. If independent-unit numbers are too small to support meaningful splits, do not claim internal cross-validation as independent biological replication. Instead, report the result as exploratory and prioritize a future independent cohort.

---

# 7. Reporting requirements

Every main result should report both observational and experimental-unit counts.

### Required count table, by treatment arm
- randomized donors/animals;
- donors/animals receiving intervention;
- donors/animals completing follow-up;
- donors/animals included in primary analysis;
- donors/animals excluded and reasons;
- samples/specimens;
- fields/images;
- observed cells;
- median and range, or distribution, of fields and cells per donor/animal;
- technical replicates, if applicable.

Use language such as:

> “Treatment effect estimated from \(n\) randomized donors/animals per arm, based on \(N\) observed cells across \(F\) fields.”

Do not write or imply that \(N\) observed cells are \(N\) treatment replicates.

Also report:

- donor-/animal-level effect estimate and confidence interval;
- randomization/permutation result;
- hierarchical-model estimate and assumptions;
- pseudobulk/donor-summary result;
- ICC or variance-component estimates, with uncertainty where possible;
- raw donor/animal values;
- missingness and exclusions by arm;
- all prespecified and exploratory analyses separately.

---

# 8. Acceptance criteria, stopping rules, and troubleshooting

## A. Proposed acceptance criteria
A confirmatory conclusion should require all of the following:

1. the analysis uses the verified randomized unit as the treatment replicate;
2. the primary endpoint and aggregation rule were pre-specified or clearly labeled exploratory;
3. allocation, blinding, and quality-control procedures show no critical protocol failure;
4. the donor-/animal-level estimate and uncertainty are reported;
5. the randomized-unit permutation analysis is consistent with the pre-specified decision rule;
6. null-calibration checks do not show material anti-conservatism or leakage;
7. for data-derived endpoints, the effect is supported in held-out randomized units or an independent cohort.

The numerical significance threshold, confidence level, acceptable false-positive rate, and validation criteria should be specified prospectively. They are not supplied in the evidence packet and should not be invented after results are inspected.

## B. Proposed stopping rules
Stop enrollment based on the pre-calibrated required number of **independent randomized units**, accounting for expected attrition—not when a target number of cells is reached and not when a nominal result appears.

If interim analyses are planned, specify them before enrollment and use a valid sequential decision procedure. Repeated unplanned testing as additional donors or animals accrue can inflate false-positive risk.

## C. Troubleshooting

| Problem | Proposed response |
|---|---|
| High donor-level ICC | Increase randomized donors/animals if feasible; additional cells alone may offer limited gain. |
| Nominal cell-level significance disappears after clustering | Report the changed uncertainty; do not infer automatically that the biological effect is false. |
| Donor-level and pooled-cell analyses differ | Examine unequal cell yields, differing estimands, donor weighting, cell composition, and batch effects. Treat pooled-cell results as descriptive unless justified otherwise. |
| Treatment and batch are confounded | Do not claim they are separable from existing data; redesign future allocation to balance treatment within batch. |
| Too few randomized units | Use exact or constrained permutation where possible, report effect sizes and uncertainty, avoid overconfident null claims, and prioritize additional independent units. |
| Many missing or excluded donors/animals | Report by arm and reason; perform pre-specified missing-data sensitivity analyses. Do not replace missing donors with extra cells from remaining donors. |
| Model nonconvergence or overdispersion | Simplify the model, use donor-level summaries, reassess distributional assumptions, and compare with randomization inference. |
| Held-out performance is poor | Treat discovery finding as unconfirmed; investigate leakage, overfitting, batch dependence, endpoint instability, and insufficient donor-level sample size. |

---

## Final proposed interpretation rule

Cells and fields are valuable repeated observations, but the randomized donor or animal is the unit that supports causal treatment inference. The protocol therefore uses donor-/animal-level summaries or pseudobulk comparisons as the primary inferential basis, hierarchical models as a complementary representation of nested data, grouped resampling and label permutations for calibration, and donor-/animal-level held-out validation for robustness. Small independent sample size remains a consequential limitation even if very many cells are measured.
