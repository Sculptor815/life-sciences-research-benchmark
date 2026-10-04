# Kimi K3 / inf-d03

Original final answer, shared by both scoring rounds.

# Proposed analysis and validation protocol

**Status:** Every experiment, calibration step, analysis, and validation procedure below is **proposed**. No study-specific counts, effect sizes, variance components, results, or author methods are assumed.

## Recommended next action

Before collecting confirmatory data or unblinding outcomes, designate each **donor or animal receiving treatment assignment as the only independent treatment replicate**. Cells and fields measured within a donor should be retained as dependent observations but must not be entered as independent rows in an unclustered treatment test.

The recommended primary approach is:

1. Analyze treatment at the **donor/animal level**, using either:
   - a donor-level pseudobulk summary, or
   - a hierarchical model with donor—and, where appropriate, field-within-donor—random effects.
2. Use **grouped permutation and donor-level bootstrap** procedures that preserve all observations belonging to the same randomized unit.
3. Calibrate the null distribution empirically because donor numbers, within-donor variance, and intraclass correlation are currently unknown.
4. Reserve entire donors or animals for held-out validation; never split cells from one donor between training and validation.
5. Report both the number of randomized units and the number of observed cells and fields, without presenting observed-cell count as treatment replication.

If donor-level inference is impossible because too few randomized units are available, the study should be reported as a feasibility or hypothesis-generating study rather than rescued by counting cells as replicates.

---

## 1. Evidence-to-inference-to-conclusion chain

| Evidence in the supplied packet | Inference | Conclusion for this protocol |
|---|---|---|
| Pseudoreplication is inference that treats treatment subsamples or dependent observations as independent replication. | Many cells from one treated donor do not provide many independent observations of treatment assignment. | Treatment tests, confidence intervals, and resampling must use the donor/animal as the independent unit. |
| The randomized treatment level defines the experimental unit. | Because treatment is assigned to donors or animals, donor/animal-level variation determines the relevant treatment uncertainty. | The primary estimand should be a donor-population treatment effect, with one randomized unit contributing one unit of treatment replication. |
| Observational and biological units can differ. | A cell can be the measurement unit while the donor is the unit to which treatment inference applies. | Cell-level distributions may be described or modeled, but they require donor-level uncertainty and must be labeled as secondary or conditional inference. |
| Very small independent \(n\) affects precision and robustness but does not automatically invalidate every model-based test. | A small donor number does not make all hierarchical analyses categorically invalid, but their assumptions and uncertainty require extra scrutiny. | Use model diagnostics, donor-level sensitivity analyses, null calibration, and cautious interpretation rather than either ignoring clustering or declaring all modeling impossible. |
| Clustering may alter uncertainty without changing a point estimate. | Correcting for dependence can widen intervals even when the estimated mean difference remains similar. | Do not interpret loss of significance after clustering as proof that the observed biological difference was false. |
| High intraclass correlation or loss of significance alone does not prove a false biological effect. | Dependence affects information content and error estimation, not by itself the existence of an effect. | Report the effect estimate, uncertainty, variance components, and validation outcome instead of treating nonsignificance as evidence of no effect. |
| Exact donor, field, cell, effect-size, and variance-component values are unavailable. | No defensible numeric sample size, holdout fraction, or universal acceptance threshold can be supplied now. | These parameters must be calibrated from proposed pilot data, variance-only internal review, and hierarchical simulation. |

**Overall chain:** treatment is randomized at the donor/animal level → cells from the same donor are dependent → cell count is not treatment replication → primary inference must preserve donor-level sampling → unknown cluster parameters must be calibrated → conclusions should be based on donor-level effect estimates, calibrated uncertainty, and donor-held-out validation.

---

## 2. Proposed unit and estimand structure

Use a hierarchy such as:

\[
\text{Treatment arm}
\rightarrow
\text{randomized donor/animal}
\rightarrow
\text{field or sampling location}
\rightarrow
\text{cell}.
\]

- **Randomized unit:** donor or animal.
- **Primary treatment-replication count:** number of independently randomized donors/animals per arm.
- **Observational units:** fields and cells.
- **Potential biological units:** donor, tissue region, field, or cell, depending on the scientific question. These roles must be declared rather than inferred from convenience.
- **Primary estimand:** the average donor-level treatment effect on a prespecified biological endpoint.
- **Secondary estimands:** within-donor distributions, donor-to-donor heterogeneity, field-to-field variation, and cell-state proportions. These should not be presented as independent evidence of treatment efficacy unless their design supports that claim.

If animals share cages, litters, preparation batches, or other sources of dependence, independence at the animal level must be verified rather than assumed. Any higher-level dependence should be incorporated into randomization, modeling, and resampling.

---

# 3. Operational protocol, in proposed order

## Step 1 — Preparation and quality checks

### 1.1 Define the scientific question

Before allocation:

- Specify the primary endpoint and whether it is:
  - a donor mean or median,
  - a cell proportion,
  - a distributional distance,
  - a field-level measurement, or
  - another donor-level summary.
- Define the minimum biologically meaningful treatment difference through subject-matter criteria. Do not choose it after seeing the treatment comparison.
- Specify whether inference concerns:
  - the population represented by the donors,
  - only the observed donors, or
  - average cell behavior conditional on donor.

### 1.2 Create an auditable unit map

Assign globally unique identifiers for:

- donor/animal,
- treatment arm,
- randomization stratum or batch,
- sampling session,
- field,
- cell,
- operator or instrument,
- exclusion reason.

The data structure must make it impossible to mistake cell rows for randomized units.

### 1.3 Propose calibration of unknown design parameters

Because no donor count, cell count, effect size, or variance components are available:

1. Conduct a proposed assay-repeatability study using appropriate neutral or quality-control material to estimate measurement variation.
2. Conduct a proposed pilot spanning the expected range of donors, fields, and cell densities.
3. Fit a provisional hierarchical model to estimate:
   - donor-to-donor variance,
   - field-within-donor variance,
   - cell or residual variance,
   - intraclass correlation at donor and field levels.
4. Treat pilot estimates as uncertain and simulate across plausible ranges rather than relying on point estimates.
5. Vary candidate:
   - donors per arm,
   - fields per donor,
   - cells per field,
   - effect sizes,
   - variance components.
6. For each candidate design, estimate by simulation:
   - confidence-interval width,
   - confidence-interval coverage,
   - null rejection frequency,
   - probability of detecting the prespecified meaningful effect.
7. Add cells or fields only until the estimated precision of each donor summary stops improving materially relative to donor-to-donor variance. Beyond that point, additional donors contribute more independent treatment information than additional cells.

If no advance pilot is feasible, use a proposed two-stage design with blinded, variance-only re-estimation. The final analysis should retain all randomized donors. Do not revise the donor target based on an unblinded observed treatment effect unless a prespecified, error-controlled adaptive procedure is used.

---

## Step 2 — Establish independent units

1. Enumerate eligible donors or animals before treatment assignment.
2. Verify that they can reasonably be treated as independent.
3. Investigate possible shared sources of dependence, such as relatedness, housing, batch, operator, or sample-processing group.
4. If such structure exists:
   - incorporate it into allocation,
   - preserve it in grouped resampling,
   - include an appropriate higher-level variance component where estimable.
5. Define exclusions using characteristics available before outcome measurement.
6. Record the number of randomized, treated, measured, excluded, and analyzed donors separately from cell and field counts.

The protocol should not declare a minimum number of donors before calibration. If the achievable donor number falls below the calibrated requirement, the study remains interpretable as pilot evidence, but confirmatory claims should not be made.

---

## Step 3 — Allocation and blinding

### Proposed allocation

- Randomize whole donors or animals to treatment arms.
- All fields and cells from a donor inherit that donor’s assignment.
- Randomize within prespecified strata if important baseline factors or processing batches cannot be balanced by simple randomization.
- Use allocation concealment so investigators cannot predict the next assignment.
- Record the randomization seed or audit trail according to local reproducibility requirements.

Do not randomize individual cells or fields to different analyses as though treatment had been assigned at those levels.

### Proposed blinding

Where feasible:

- conceal treatment identity from personnel administering the intervention;
- blind staff selecting fields and measuring cells;
- blind outcome extraction and image-analysis personnel;
- conduct preprocessing and quality-control decisions without access to treatment labels;
- maintain an audit trail for any necessary unblinding.

If intervention staff cannot be blinded, separate them from outcome measurement and analysis.

---

## Step 4 — Intervention and sampling

1. Apply the intervention to the entire randomized donor or animal under standardized conditions.
2. Prespecify timing, handling, sampling order, and acceptable protocol deviations.
3. Select fields using a blinded random or systematic scheme. Do not select fields because they visually support an expected result unless that selection is itself the prespecified measurement.
4. Keep sampling intensity as consistent as practicable across donors and arms.
5. Record the number of fields attempted, acquired, and rejected, with rejection reasons.
6. Record the number of cells observed and retained per field and donor.
7. Prevent differential cell-count requirements by treatment arm unless scientifically necessary and prespecified.

Cell-count targets should come from the calibration procedure in Step 1. A very large number of cells from few donors does not compensate for inadequate donor replication.

---

## Step 5 — Measurements

### Proposed measurement controls

- Use standardized acquisition and processing settings where feasible.
- Retain raw data and preprocessing outputs.
- Record instrument, operator, session, and batch.
- Use objective quality criteria established before outcome comparison.
- Separate technical failures from biological outlying observations.
- Preserve cell-level denominators for proportions.
- Preserve enough information to reproduce every donor summary from raw observations.

### Proposed quality checks

Before unblinding or primary analysis:

- assess missing fields and cells by donor and arm;
- compare cell yield and field yield across arms;
- inspect batch and operator distributions;
- check for differential dropout, viability, segmentation, or image-quality problems;
- verify that no donor contributes an overwhelming fraction of analyzed cells;
- document all exclusions.

Any quality-control threshold learned from unblinded treatment comparisons should be treated as exploratory and subjected to held-out evaluation.

---

## Step 6 — Experimental and analytical controls

Proposed controls should be selected for the specific assay and may include:

- negative or vehicle procedural controls;
- positive assay-performance controls;
- batch or calibration standards;
- blinded replicate measurements;
- null samples used to estimate technical and within-donor variation.

These controls support assay validity but do not create additional treatment replicates unless they are independently randomized at the appropriate level.

Randomization-balance checks should compare baseline variables and processing factors across arms. Baseline imbalance should be reported rather than used as a post hoc reason to remove randomized donors.

---

## Step 7 — Analysis

The primary analysis method should be selected and locked before unblinding. The other method should be retained as a sensitivity analysis.

### 7.1 Proposed donor-level pseudobulk comparison

For each donor:

1. Apply locked quality-control rules.
2. Compute the prespecified endpoint from eligible cells and fields.
3. Preserve numerators and denominators for proportion endpoints.
4. Produce one donor-level value.
5. Compare donor-level values between treatment arms.

Weighting must match the estimand:

- For an average-donor effect, weight donors equally.
- Do not accidentally give a donor more influence merely because more cells or fields were acquired.
- If fields are intended as equally representative samples, summarize fields first and then summarize field values within donor.
- If cell-weighted biology is the explicit target, state that choice and use a corresponding sensitivity analysis.

**Strengths:** transparent, directly aligned with the randomized unit, and robust to inappropriate cell-level independence assumptions.

**Limits:** may discard within-donor distributional information and can be inefficient if donor summaries have very different precision.

### 7.2 Proposed hierarchical comparison

For a continuous cell- or field-level outcome, a proposed model is:

\[
y_{dfi}
=
\beta_0+\beta_1T_d+X_d\gamma+b_d+b_{df}+\varepsilon_{dfi},
\]

where:

- \(T_d\) is the donor’s treatment assignment;
- \(b_d\) is the donor effect;
- \(b_{df}\) is the field-within-donor effect where fields are meaningful;
- \(\varepsilon_{dfi}\) is residual cell-level variation.

Use an outcome distribution and link appropriate to the measurement. The treatment parameter \(\beta_1\) must be tested against donor-level uncertainty, not residual cell-level uncertainty alone.

For cell-state proportions or strongly distributional endpoints, either:

- model the appropriate within-donor outcome hierarchically, or
- calculate a prespecified donor-level distributional summary and compare those summaries.

**Strengths:** retains cell and field information and estimates variance components.

**Limits:** random-effect variance may be poorly estimated with few donors; convergence and distributional assumptions require diagnostics. Small donor \(n\) does not automatically invalidate the model, but it reduces confidence in model-dependent uncertainty.

### 7.3 Grouped resampling

All proposed resampling must keep each donor’s observations together.

**Grouped permutation:**

1. Shuffle treatment labels only among whole donors or animals.
2. Respect randomization strata, matched sets, and batch restrictions.
3. Carry all fields and cells with the donor label.
4. Refit the complete locked analysis pipeline for every permutation.
5. Calculate a permutation interval or \(p\)-value with Monte Carlo uncertainty.

**Donor-level bootstrap:**

1. Resample donors or animals with replacement within the prespecified design structure.
2. Include every retained field and cell belonging to each selected donor.
3. Refit the pseudobulk or hierarchical analysis for each replicate.
4. Use the resulting donor-level distribution for uncertainty and sensitivity assessment.

Do not bootstrap cells independently within donors for treatment inference. A within-donor bootstrap may describe conditional cell-level precision, but it does not estimate between-donor treatment uncertainty.

### 7.4 Null calibration

Because variance components and donor numbers are unknown, analytic nominal error rates should be calibrated rather than assumed.

Use two complementary proposed procedures:

1. **Restricted donor-label permutation**
   - Generate a null by permuting treatment assignments only at the randomized-unit level.
   - Preserve the observed dependence within each donor.
   - Use it to test whether donor-level summaries are exchangeable across arms.

2. **Hierarchical null simulation**
   - Simulate datasets under no treatment effect using plausible donor, field, and residual variance components from the pilot or blinded internal calibration.
   - Run the entire preprocessing, model-fitting, and testing pipeline.
   - Estimate null rejection frequency and confidence-interval coverage.
   - Repeat over a range of plausible intraclass correlations rather than only the observed point estimate.

The null rejection rate should be compatible with the nominal level within Monte Carlo uncertainty. If calibration shows substantial size distortion, use a corrected or resampling-based test, or report that confirmatory \(p\)-values are not calibrated.

A null calibration demonstrates that the procedure behaves appropriately under the simulated null; it does not prove that an observed treatment effect is real.

### 7.5 Held-out validation

If calibrated donor numbers permit:

1. Split data by **entire donor or animal**, stratified by treatment arm and important randomization factors.
2. Use the training donors to choose preprocessing, endpoint summaries, model structure, and tuning parameters.
3. Freeze those choices.
4. Apply the locked pipeline to held-out donors without letting any of their cells or fields influence training.
5. For a treatment-effect study, estimate the same treatment contrast in the held-out donors using the locked specification.
6. Compare:
   - direction,
   - effect magnitude,
   - uncertainty intervals,
   - donor-level prediction or calibration where prediction is relevant,
   - concordance with the prespecified decision criterion.

No universal holdout fraction can be specified without knowing donor numbers and variance. The split should be selected by grouped simulation.

If too few donors exist for a stable holdout set, use nested grouped cross-validation as an exploratory robustness analysis and prioritize an independently recruited replication cohort. Do not describe grouped cross-validation as fully independent validation.

### 7.6 Multiplicity and secondary analyses

- Specify one primary endpoint and one primary donor-level analysis.
- Control or clearly describe error across multiple endpoints, cell states, and field summaries.
- Label cell-level and distributional analyses as secondary.
- Avoid selecting the analysis that gives the most favorable result after unblinding.

---

## Step 8 — Proposed acceptance criteria

Numeric thresholds should be calibrated rather than invented. Acceptance should require all applicable categories below.

### Design acceptance

- The calibrated number of randomized donors/animals is available.
- Treatment assignment and processing are not confounded with batch or another unavoidable factor.
- Field and cell sampling are sufficiently consistent to support the donor estimand.
- Quality-control exclusions do not compromise randomization or create severe arm imbalance.

### Analytical acceptance

- The pseudobulk or hierarchical model matches the endpoint scale.
- The hierarchy reflects the actual sampling design.
- Variance components are estimable and model convergence is satisfactory.
- Donor-level residuals and influential donors are examined.
- Null calibration is compatible with the intended error rate.
- Results are not dependent on treating cells as independent.

### Scientific acceptance

- The donor-level effect estimate and uncertainty interval are reported.
- Conclusions are consistent across the prespecified primary and sensitivity analyses, or discrepancies are transparently explained.
- Held-out or independent validation meets the criteria established before analysis.
- Secondary cell-level patterns are not presented as independent confirmation of treatment.

If the donor count is below the calibrated requirement, the accepted conclusion should be limited to feasibility, variance estimation, and hypothesis generation.

---

## Step 9 — Proposed stopping rules

### Technical or integrity stopping

Stop or suspend the study if:

- allocation or blinding is materially compromised;
- treatment assignment becomes confounded with processing batch;
- assay drift cannot be corrected;
- required randomized units are lost;
- data provenance is inadequate;
- prespecified humane or safety endpoints require stopping.

### Statistical stopping

- Do not stop merely because many cells have been measured.
- Do not repeatedly inspect unblinded treatment effects and stop when a nominal threshold is crossed.
- A blinded variance-only internal pilot may revise recruitment targets.
- Any unblinded interim efficacy or futility analysis must use a prespecified error-controlled adaptive plan.
- If the minimum calibrated donor number cannot be reached, stop the confirmatory portion and report the study as pilot evidence.

---

## Step 10 — Troubleshooting

| Proposed problem | Recommended response |
|---|---|
| High donor-level intraclass correlation | Prioritize more donors rather than more cells; use donor-level analysis and grouped resampling. Do not conclude that the biological effect is false solely from high correlation. |
| Very few donors | Use exact or restricted donor permutation and report wide uncertainty; classify conclusions as exploratory unless assumptions and calibration strongly support a model-based analysis. |
| Hierarchical model does not converge | Simplify only prespecified random-effects components, use donor-level pseudobulk, or obtain more donors. Do not replace donor clustering with independent-cell analysis. |
| Unequal cell or field counts | Check acquisition bias; use donor summaries with weights aligned to the estimand; perform capped or sensitivity sampling analyses. |
| One donor contributes most cells | Prevent that donor from dominating by analyzing donor summaries or applying a prespecified sampling/weighting rule. |
| Batch differs by treatment | Rebalance future allocation if possible; otherwise report confounding and avoid strong causal claims that grouped statistics cannot repair. |
| Null calibration rejects too often under the null | Revise the test, use restricted permutation, improve variance estimation, or suspend confirmatory \(p\)-value interpretation. |
| Training and held-out effects disagree | Check sampling, variance, protocol deviations, and model stability. Report the disagreement; do not tune the pipeline on the holdout and revalidate repeatedly. |
| Clustered interval is wider than the unclustered interval | Interpret this as loss of independent information, not proof that the point estimate or biological effect is false. |

---

# 4. Required reporting

The proposed report should include all of the following:

### Unit counts

- Number of donors/animals randomized, total and per arm.
- Number of donors/animals treated, measured, excluded, and analyzed.
- Number of fields observed and analyzed, total, per arm, and per donor.
- Number of cells observed and analyzed, total, per arm, and per donor.
- Minimum, median, maximum, and distribution of fields and cells per donor.
- Numerators and denominators for cell proportions.
- Clear statement that **observed-cell count is not the randomized-unit count**.

### Design and conduct

- Allocation method, strata, blinding, and deviations.
- Field-selection and cell-inclusion procedures.
- Exclusions and missing-data patterns by donor and arm.
- Batch, operator, and instrument information.

### Analysis and validation

- Primary estimand and donor-level analysis.
- Hierarchical or pseudobulk model specification.
- Variance components and intraclass correlation, with uncertainty where estimable.
- Grouped permutation/bootstrap procedure.
- Null-calibration procedure and estimated error behavior.
- Held-out donor composition and validation results.
- Effect estimates, confidence intervals, and uncertainty-qualified \(p\)-values.
- Sensitivity analyses and secondary cell-level results, explicitly distinguished from primary donor-level inference.

---

# 5. Alternatives and limits

A donor-level rank or permutation analysis, donor-level pseudobulk regression, hierarchical likelihood model, cluster-robust marginal model, or Bayesian hierarchical model may all be defensible if they respect the randomized-unit hierarchy. The choice should be driven by endpoint type, calibrated donor number, missingness, and the desired population interpretation.

The protocol has important limits:

- Donor-level inference generalizes only to the population represented by the donor-sampling frame.
- Held-out donors from the same experiment do not establish external reproducibility in a new laboratory or population.
- Grouped statistics cannot repair nonrandom treatment assignment or treatment–batch confounding.
- A paired, crossover, litter-based, or cage-assigned design would change the appropriate unit structure and require a revised protocol.
- Null calibration and simulation depend on whether pilot variance estimates represent the final experiment.
- Small donor \(n\) may permit a model-based analysis under suitable assumptions, but precision and robustness remain limited.
- High intraclass correlation, wider clustered intervals, or loss of nominal significance should not be reported by themselves as proof that there is no biological effect.
