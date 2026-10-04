# Grok 4.7 / inf-d03

Original final answer, shared by both scoring rounds.

The confirmatory analysis must treat the donor or animal as the experimental unit, because that is the level at which treatment is assigned. Cell- or field-level observations are nested subsamples. They may support a biological description, but they are not independent treatment replicates. All experiments, simulations, and analyses below are proposed; no donor counts, cell counts, effect sizes, or variance components are known and none are invented here.

**Recommended next action:** lock a donor-level estimand and a donor-level primary analysis (pseudobulk comparison and/or a hierarchical model whose uncertainty is calibrated at the donor level), then accept or reject that analysis only after grouped resampling, null calibration across a variance grid, and donor-held-out validation. Report both the observed-cell (or field) count and the randomized-unit count in every result. Do not claim a treatment effect from a test that treats cells as independent.

## Evidence → inference → conclusion

**Evidence (fixed packet only).** The pseudoreplication record, via the curator interpretation, defines the concern as inference that treats treatment subsamples or dependent observations as independent replication. It states that the randomized treatment level defines the experimental unit and that observational and biological units can differ. It notes that very small independent \(n\) affects precision and robustness but does not automatically invalidate every model-based test; that clustering may alter uncertainty without changing a point estimate; and that high intraclass correlation (ICC) or loss of significance alone does not prove a false biological effect. The hypothetical constraints are that treatment is assigned to donors or animals, many cells or fields are measured per donor, donor-level inference must be distinguished from cell-level inference, and exact \(n\), effect sizes, and variance components are unavailable and must be calibrated.

**Inference.** Under those constraints, randomizing treatment to donors makes the donor the experimental unit for a treatment contrast. A cell or field is an observational unit nested in that donor. The biological unit of scientific interest may be the cell, the field, or the donor; that choice does not move the experimental unit. If cells within a donor are correlated, the information for the treatment contrast is limited by the number of randomized donors and by between-donor variation, not by the raw cell count. A cell-level model that ignores clustering can leave the point estimate nearly unchanged, especially under balanced sampling, while shrinking the standard error and inflating Type I error. Loss of significance after clustering is therefore evidence of insufficient donor-level precision or of a design-effect correction, not automatic proof that the biology is false. Conversely, a tiny donor \(n\) weakens precision and robustness; it does not, by itself, forbid a model-based test whose uncertainty is actually computed at the donor level.

**Conclusion.** Primary confirmatory inference is donor-level. Cell-level naive tests are diagnostic of pseudoreplication, not acceptance criteria. A treatment claim is supportable only if a pre-specified donor-level procedure remains calibrated under grouped null resampling and, where donor \(n\) allows, replicates in donors held out of model development. Both counts must be reported so readers can see the gap between observations and replicates.

## Concepts in their correct relationships

| Role | Unit in this design | What it justifies |
| --- | --- | --- |
| Randomized / experimental unit | Donor or animal | Treatment contrast, degrees of freedom, permutation and bootstrap clusters |
| Observational unit | Cell or field | Measurement, within-donor sampling variance, quality control |
| Biological unit | Question-dependent; may be cell, field, or donor | Interpretation of mechanism, not the treatment replicate count |
| Analysis unit for the primary claim | Donor summary, or cell data with donor-level uncertainty | Inference |
| Invalid replicate for the treatment claim | Individual cell or field treated as independent | Pseudoreplication if used as \(n\) |

Two estimands must stay separate. The **donor-level treatment estimand** is the contrast in a donor summary (mean, median, proportion, or other pre-specified functional) between treatment arms. Randomization supports that contrast. The **cell-level descriptive estimand** describes within-donor heterogeneity, measurement error, or composition. It is not a second independent copy of the treatment experiment.

Clustering changes uncertainty more reliably than it changes the point estimate. Agreement of cell-level and donor-level point estimates is therefore not evidence that cell-level \(p\)-values are valid. High ICC explains why extra cells per donor stop adding treatment information; it does not, alone, prove the effect is an artifact.

## Assumptions and unreported parameters

**Assumptions (proposed, to be checked).** Treatment is assigned wholly at donor or animal level, not independently to cells or fields. Cells or fields from the same donor are exchangeable for the chosen summary only after pre-specified quality filters. Donors are the independent units for the treatment contrast. Measurement systems can be blinded to treatment. Batch is not perfectly confounded with treatment. Missing donors and excluded fields will be documented before outcome unblinding.

**Unreported and not invented.** Number of donors per arm; cells or fields per donor and their imbalance; within-donor variance \(\sigma^2_w\); between-donor variance \(\sigma^2_b\); ICC \(=\sigma^2_b/(\sigma^2_b+\sigma^2_w)\); treatment effect size on the donor-summary scale; batch structure; cell-type composition shifts; missingness mechanism. These are calibration targets, not inputs.

**What would change the recommendation.** If treatment were independently randomized to cells, wells, or fields, that lower level would become the experimental unit. If the only question were within-donor description, cell-level models would be appropriate for that different estimand. If a calibration grid showed ICC near zero across plausible designs, cell-level and donor-level uncertainty would converge, but both counts would still be reported. If donor \(n\) cannot support a held-out split, confirmation would rest on pre-specification plus donor-level permutation, with the split limitation stated rather than hidden.

## Proposed protocol (ordered)

### 1. Preparation and quality checks

**Proposed preparatory experiment P0 (pilot or historical variance extraction, not confirmatory).** Before locking the confirmatory test, obtain variance components from a pilot with the same nesting, or from non-outcome technical metrics if a pilot is impossible. Do not use the confirmatory endpoint’s treatment contrast to choose the primary test.

Quality checks, applied with treatment labels hidden from the analyst where feasible:

- Define the sampling frame: which donors, which tissues, which fields, which cells, and which exclusion rules.
- Record hierarchy IDs on every observation: study, batch or plate, donor or animal, field, cell. An observation without a donor ID cannot enter a treatment test.
- Check that treatment is constant within donor. If any donor has mixed treatments, stop and reclassify the experimental unit; do not average across conflicting assignments.
- Quantify missingness and exclusion rates by donor and by batch before looking at the endpoint.
- Inspect cells-per-donor distribution (minimum, median, maximum, and whether yield tracks treatment or batch). Differential yield is a design flaw to report, not a reason to switch the experimental unit to the cell.
- Screen for duplicate cells, field overlap, and plate effects. Overlapping fields are dependent observational units, not extra donors.
- Lock the primary endpoint, the donor-summary functional, the covariate set, \(\alpha\), and the sidedness of the test before unblinding.

### 2. Independent units

State in the protocol and in every output:

- \(N_{\text{rand}}\): number of randomized donors or animals, overall and per arm. This is the independent replicate count for treatment.
- \(N_{\text{obs}}\): number of measured cells or fields, overall and per donor.
- Effective information is not \(N_{\text{obs}}\). A calibration approximation, to be computed after ICC is estimated rather than assumed, is the design effect \(\mathrm{DEFF}\approx 1+(\bar{m}-1)\widehat{\mathrm{ICC}}\) and \(N_{\text{eff}}\approx N_{\text{obs}}/\mathrm{DEFF}\), where \(\bar{m}\) is the mean number of observations per donor. When ICC is high and \(m\) is large, \(N_{\text{eff}}\) approaches \(N_{\text{rand}}\), not \(N_{\text{obs}}\). Report the approximation as descriptive, not as a substitute for the donor-level test.

Primary inference uses \(N_{\text{rand}}\). \(N_{\text{obs}}\) describes measurement intensity.

### 3. Allocation and blinding

**Proposed experiment P1 (confirmatory randomization).** Randomize donors or animals to treatment, not cells or fields.

- Use a pre-specified allocation list with allocation concealment until the donor is enrolled.
- Stratify or pair on strong baseline donor factors only if those factors are known before treatment and are few relative to donor \(n\). Do not stratify on post-treatment cell measurements.
- Assign donors to batches so that batch is crossed with treatment or, if that is impossible, blocked in a way that treatment and batch are not aliases. If a batch contains only one treatment, that batch cannot support a treatment contrast.
- Blind sample processing, field selection, segmentation, and endpoint scoring to treatment. If full blinding is impossible, blind the endpoint analyst and pre-specify the unblinded steps.
- Do not re-randomize cells within a donor and call that a treatment replicate.

### 4. Intervention and sampling

- Apply the intervention at the randomized unit (donor or animal), with a concurrent control (vehicle, sham, or pre-specified comparator) assigned at the same level.
- Pre-specify the target and the maximum number of fields and cells per donor. Caps prevent a high-yield donor from dominating weighted analyses.
- Sample fields by a spatial rule fixed before outcome review (for example, a grid or random coordinates), not by visual richness that could correlate with treatment.
- If a donor yields no acceptable fields, retain the donor in the allocation log as a randomized unit with a missing summary. Dropping failed donors only from the cell table understates \(N_{\text{rand}}\) and can bias the contrast if failure depends on treatment.
- Record time, dose, and technical batch at donor level so they cannot be mistaken for cell-level covariates that “increase \(n\).”

### 5. Measurements

- Measure the pre-specified endpoint at cell or field level, then derive the donor summary with a locked rule (mean, median, proportion, or a composition-stratified mean).
- Also store the raw cell-level table for diagnostic models and for within-donor variance estimation. Storage is not permission to analyze cells as replicates.
- Measure negative-control features expected, on scientific grounds external to this dataset, not to respond to treatment, and at least one process-control metric (for example, a technical marker of assay quality). Do not invent a biological positive control if none is known; if one exists independently of this study, measure it as a donor-level assay check.
- Log cell-type or field-class composition per donor. Composition shift is a donor-level outcome of its own, not a license to pool cells across donors.

### 6. Controls

- Concurrent randomized control at the donor or animal level.
- Technical negative-control features analyzed with the same donor-level procedure. A “significant” cell-level hit on a negative control, with a null donor-level result, is evidence of pseudoreplication in the pipeline, not a biological finding.
- Batch controls as in allocation. Adjustment for batch is allowed only when batch is not an alias of treatment.
- No cell-level sham that is actually the same animal’s untreated cells presented as an independent control, unless those cells were separately randomized and the dependence is modeled. Split-body designs are a different experimental unit and are outside this protocol unless re-specified.

### 7. Analysis (proposed; none of these results exist yet)

Run the following as a locked comparison. Only the donor-level procedures can support a treatment claim.

**A1. Naive cell-level model (diagnostic only).** Fit the endpoint on cells or fields with treatment as a fixed effect and no donor clustering. This is the pseudoreplicated analysis. Retain it solely to show how uncertainty changes. Do not use its \(p\)-value, confidence interval, or “\(n = N_{\text{obs}}\)” in the claim.

**A2. Pseudobulk comparison (eligible primary).** Collapse to one summary per donor. Compare arms with a procedure whose replicate count is \(N_{\text{rand}}\): a two-group test on donor summaries, a linear model on those summaries, or a donor-level permutation test. If cells per donor vary widely, a sensitivity analysis may use precision weights based on within-donor variance. Pre-specify a weight cap. Uncapped inverse-variance weights can recreate pseudoreplication by letting large donors dominate.

**A3. Hierarchical comparison (eligible primary if uncertainty is donor-level).** Fit a mixed model of the form outcome ~ treatment + pre-specified covariates + (1 | donor), or a generalized form with the same nesting. Because treatment is between donors, do not encode treatment as a within-donor effect. The treatment coefficient must be tested with uncertainty and degrees of freedom that reflect between-donor variance (for example, Satterthwaite or Kenward–Roger approximations, cluster-robust standard errors with clusters = donors, or a donor-level bootstrap). A Wald test that uses residual degrees of freedom on the order of \(N_{\text{obs}}\) is not an acceptable hierarchical test. If the mixed model is singular or the donor variance estimate is unstable, fall back to A2 rather than to A1.

**A4. Grouped resampling (required sensitivity and null reference).**

- Permute treatment labels at the donor level, keeping all cells of a donor together. Do not permute cell labels independently.
- Cluster bootstrap: resample donors with replacement, stratified by treatment arm, and keep every cell belonging to each drawn donor. Recompute the A2 and A3 estimates. The resulting interval is a donor-level uncertainty statement.
- Optional two-stage resample: bootstrap cells within donor only to estimate uncertainty of that donor’s summary; then combine with between-donor resampling. Within-donor resampling alone does not test treatment.

Compare point estimates and intervals from A2, A3, and A4. Expectation from the packet: clustering may move the interval without moving the point estimate. A material point-estimate disagreement is a troubleshooting trigger (imbalance, weighting, composition, or misspecified summary), not automatic evidence of a false effect.

**A5. Null calibration (proposed simulation C1; parameters unknown).** Because \(\sigma^2_b\), \(\sigma^2_w\), \(N_{\text{rand}}\), and \(m\) are unreported, do not pick a single ICC. Build a grid:

- Candidate donor \(n\) per arm spanning the smallest operationally feasible study through the largest study that can actually be run.
- Cells or fields per donor: balanced and unbalanced schemes, including the observed or pilot yield distribution once it exists.
- ICC grid from near 0 to high dependence, implemented by varying \(\sigma^2_b\) relative to \(\sigma^2_w\) on the analysis scale. Include a high-ICC region, because that is where pseudoreplication is most misleading.
- Treatment effect fixed at zero for Type I calibration.
- For each grid cell, simulate many datasets from a hierarchical null (donor random intercept, treatment assigned at donor level, cells generated within donor). The number of Monte Carlo replicates must be large enough that the uncertainty in the empirical rejection rate is small relative to the distance from nominal \(\alpha\) that would change a decision. That Monte Carlo size is itself a calibration choice to be reported, not a result already obtained.

Apply A1, A2, and A3 to every simulated dataset. Record empirical Type I error and interval coverage. **Acceptance rule for the confirmatory method:** pre-specify a tolerance (for example, empirical Type I error within Monte Carlo error of nominal \(\alpha\), or a one-sided conservative bound). A method that exceeds that tolerance anywhere in the scientifically plausible ICC and imbalance region is not eligible as primary. Expect A1 to fail as ICC and \(m\) increase. Do not “fix” A1 by citing a small pilot ICC; the grid, not a single estimate, decides eligibility.

**A6. Power and sample-size calibration (proposed simulation C2).** Repeat C1 with a grid of donor-level effect sizes, expressed in between-donor standard-deviation units so that no absolute effect is invented. Estimate power as a function of \(N_{\text{rand}}\) and of cells per donor. The decision-relevant curve is power versus added donors. Added cells per donor should show diminishing returns once within-donor error is small relative to \(\sigma_b\). If, at the maximum feasible \(N_{\text{rand}}\), power remains inadequate for the smallest effect the study claims to care about, do not start confirmatory collection for that endpoint. “Small independent \(n\)” here limits precision; it does not mean a donor-level model is automatically invalid, but it does mean a claim of adequate power would be unsupported.

**A7. Held-out validation (proposed validation V1).** Split by donor, never by cells from the same donor.

- Discovery donors: choose the summary functional, covariates, and any composition adjustment. Freeze them.
- Confirmation donors: run the frozen A2 or A3 procedure once. A cell from a discovery donor must not appear in confirmation.
- If \(N_{\text{rand}}\) is too small for a split to be informative, do not force a split and then interpret noise as replication failure. State that held-out confirmation is infeasible, rely on pre-specification plus A4 permutation, and treat generalizability as unresolved. The packet’s point applies: small independent \(n\) harms robustness; it does not by itself invalidate a correctly uncertainty-calibrated model-based test. It does invalidate any claim that the result has been externally confirmed.

**A8. Multiplicity.** If many endpoints or cell features are tested, correct multiplicity using donor-level statistics. Cell-level false-discovery procedures that use \(N_{\text{obs}}\) as the sample size are not valid treatment screens.

**Reporting requirement (every table, figure, and abstract).** State \(N_{\text{obs}}\) and \(N_{\text{rand}}\) (per arm). State which analysis was primary. Report the donor-level point estimate, its donor-level interval, and the grouped-resampling interval. Place the naive cell-level result, if shown, in a labeled diagnostic column. Report the ICC or variance components used in calibration, the grid ranges, and whether the primary method passed the Type I tolerance. Report held-out status: performed, or infeasible and why. Do not write “\(n =\)” followed only by a cell count.

### 8. Acceptance and stopping criteria

**Accept a treatment claim only if all of the following hold:**

- The primary procedure is A2 or a donor-uncertainty A3 that passed C1 across the pre-specified plausible grid.
- The confirmatory contrast meets the pre-specified \(\alpha\) on the donor-level test, in the pre-specified direction.
- A4 intervals agree in sign with the primary estimate, allowing for width differences.
- If V1 was feasible, the held-out donors show the same direction under the frozen rule. Failure to replicate is a failed confirmation, not a cue to return to A1.
- Both \(N_{\text{obs}}\) and \(N_{\text{rand}}\) are reported, and \(N_{\text{rand}}\) is the replicate count named in the claim.
- Negative-control features do not produce donor-level “effects” beyond the calibrated Type I rate.

**Do not accept a claim if:**

- Significance exists only in A1.
- Weights, unfiltered cell yield, or a cell-level mixed-model residual degrees of freedom are what create significance.
- Batch is aliased with treatment.
- Donors were split across discovery and confirmation.

**Do not interpret the following as proof of a false biological effect:** loss of significance after donor-level correction; a high estimated ICC; a wide donor-level interval. Those results mean the treatment contrast is not established at the experimental unit. They are compatible with a real donor-level effect that this \(N_{\text{rand}}\) cannot resolve.

**Stopping and sample-size changes (proposed, donor-level only).** Interim looks, futility stops, and sample-size re-estimation may use only donor summaries and a pre-specified alpha-spending or re-estimation rule. Do not stop early because a cell-level \(p\)-value crossed a threshold. Stop for futility if C2, updated with blinded or pre-specified variance estimates, shows that the maximum feasible \(N_{\text{rand}}\) cannot detect the pre-specified minimal donor-level effect. Adding cells inside already enrolled donors is not a substitute for that stop rule.

### 9. Troubleshooting

| Observation | Proposed response | Do not |
| --- | --- | --- |
| A1 significant, A2/A3 not | Report insufficient donor-level evidence. Check C1 to confirm A1 is anti-conservative. | Conclude the biology is false, or switch the claim to A1 |
| A2 and A3 point estimates disagree | Inspect imbalance, weight caps, outliers, composition, and summary functional. Re-run with the locked sensitivity set. | Average the two \(p\)-values |
| Mixed model singular or donor variance near zero | Use A2 plus A4 permutation. Treat a near-zero variance as a data result to be checked, not as proof that cells are independent. | Fall back to residual-df cell-level tests |
| Very small \(N_{\text{rand}}\) | Prefer donor-label permutation over asymptotic \(p\)-values. State precision limits. Skip V1 if the split is uninformative. | Invent power or declare the model invalid solely because \(n\) is small |
| Cell yield differs by treatment | Report yield as a donor-level outcome. Use unweighted or capped-weight summaries. | Let high-yield donors define the effect through cell pooling |
| Composition shifts with treatment | Analyze donor-level composition separately. For a marker endpoint, use a pre-specified composition-stratified donor summary, still tested at donor level. | Adjust cell type in a cell-level model and ignore donor clustering |
| Batch confounded with treatment | Stop confirmatory inference for that batch layout. Redesign allocation. | “Correct” an alias with a covariate and claim a treatment effect |
| High ICC on the calibration grid | Increase donors, not cells, if more treatment information is required. | Collect more fields and report them as replicates |
| Held-out direction disagrees | Claim is not confirmed. Discovery results stay exploratory. | Re-split until confirmation succeeds |

## Alternatives and limits

An eligible alternative primary is either pseudobulk plus donor permutation, or a hierarchical model with donor-level uncertainty, but not both as co-primary without a multiplicity rule. Pseudobulk is more transparent when \(N_{\text{rand}}\) is small and is the safer fallback if mixed-model approximations are unstable. Hierarchical models use within-donor information more directly and can include cell-level covariates, but only if the treatment test does not borrow residual degrees of freedom from \(N_{\text{obs}}\). Generalized estimating equations with an exchangeable working correlation and donor clusters are another proposed alternative; sandwich standard errors can be unstable at very small \(N_{\text{rand}}\), so they should pass the same C1 grid before use.

Limits that this protocol does not remove:

- No calibration grid can create information that \(N_{\text{rand}}\) does not contain. Simulation uses assumed generative models; if the true dependence is more complex than a donor intercept (spatial fields, litter, cage, unmeasured batch), C1 must be extended to that structure before the method is accepted. Those extra clusters are currently unreported.
- Held-out validation estimates confirmation under the same protocol, not transport to a new population, species, or assay.
- A calibrated non-significant result is not evidence of no biological difference. The packet explicitly blocks that over-reading of lost significance and of high ICC.
- A calibrated significant result is still conditional on randomization, blinding, no batch aliasing, and the locked estimand. It does not identify a cell-autonomous mechanism. Mechanism claims require a design in which the biological unit and the experimental unit are aligned, or a separate within-donor experiment with its own randomization.
- Observational donor cohorts, in which “treatment” is not randomized, keep the same anti-pseudoreplication rule but lose the causal justification of randomization. This protocol does not convert an observational contrast into a randomized one.
- Exact operating characteristics cannot be stated until C1 and C2 are run. Until then, sample size, power, ICC, and Type I error remain unknown.

**Operational close.** Write the statistical analysis plan so that the randomized unit, the observational unit, and the biological unit are three named objects; pre-register A2 or donor-level A3 as primary; schedule C1 and C2 before confirmatory unblinding; reserve A1 as a pseudoreplication diagnostic; perform A4 on the real data and V1 by donor if \(N_{\text{rand}}\) allows; and withhold any treatment conclusion that cannot be stated with both \(N_{\text{obs}}\) and \(N_{\text{rand}}\) visible. All of those steps are proposed.
