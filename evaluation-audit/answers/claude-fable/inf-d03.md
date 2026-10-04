# Claude Fable 5 / inf-d03

Original final answer, shared by both scoring rounds.

# Proposed Analysis and Validation Protocol for Donor-Randomized, Cell-Level Measured Studies

**Status statement: Every experiment, analysis, simulation, and validation step below is *proposed*. No data have been collected or analyzed. All quantitative thresholds flagged as "calibration targets" are placeholders to be set by the calibration procedures described, not reported results.**

---

## 1. Headline recommendation

Conduct all confirmatory inference at the level of the **randomized unit (donor or animal)**, using pseudobulk aggregation and/or hierarchical mixed models, with grouped (donor-level) resampling and permutation-based null calibration. Treat cell-level analyses as **descriptive or exploratory only**, and report both the observed-cell count and the randomized-unit count in every figure, table, and statistical statement. Validate any cell-level classifier or signature on **held-out donors**, never held-out cells from training donors.

---

## 2. Evidence-to-inference-to-conclusion chain

**Evidence (from the supplied pseudoreplication record):**

1. Pseudoreplication is defined as inference that treats treatment subsamples or dependent observations as independent replication.
2. The randomized treatment level defines the experimental unit; observational units (cells, fields) and biological units can differ from it.
3. Very small independent n affects precision and robustness but does **not** automatically invalidate every model-based test.
4. Clustering may alter uncertainty estimates without changing the point estimate; high intraclass correlation (ICC) or loss of significance after correction does not, by itself, prove the biological effect is false.

**Inference:**

- Because treatment is assigned to donors/animals, cells within a donor share the donor's random assignment and donor-level biological/technical variation; they are dependent observations under point (1)–(2). Treating them as independent inflates the effective sample size and deflates standard errors, producing anti-conservative p-values.
- Point (4) implies the correct remedy is to **repair the uncertainty model**, not to discard effect estimates: point estimates from cell-level and donor-level analyses may agree, and divergence between naive and corrected p-values is expected, not evidence of a false effect.
- Point (3) implies that with small donor n, model-based tests (mixed models, pseudobulk t-tests) can remain valid if assumptions are checked and calibrated — hence the need for explicit null calibration rather than blanket rejection of small-n designs.

**Conclusion:** The protocol must (a) make the donor the inferential unit, (b) propagate donor-level variance via hierarchical models or pseudobulk, (c) empirically calibrate type-I error under donor-level permutation/resampling because variance components and donor n are unknown, (d) validate predictive claims on held-out donors, and (e) report both unit counts so readers can assess the true replication structure.

---

## 3. Ordered operational protocol (all steps proposed)

### Step 0 — Preregistration and definitions

- Preregister: the experimental unit (donor/animal receiving randomized treatment), the observational unit (cell or field), the biological unit if distinct, the primary endpoint(s), the primary analysis (Section 3.6), and the acceptance criteria (Section 3.8).
- Explicitly write: "n for inference = number of randomized donors per arm; cells are repeated measures."

### Step 1 — Preparation and quality checks

1. **Metadata schema:** every cell/field record must carry donor ID, treatment arm, batch/run, plate/slide, acquisition date, operator, and position (field/well). Missing donor ID is a disqualifying QC failure because grouped analysis is impossible without it.
2. **Technical QC (proposed thresholds to be calibrated on pilot/control data, not invented):** per-cell quality filters (e.g., viability, segmentation quality, library size or signal-to-noise as appropriate to the modality) defined **blinded to treatment** and applied uniformly across arms.
3. **Confounding audit:** cross-tabulate donor × batch × arm *before* unblinding outcomes. If treatment is confounded with batch (all treated donors in one run), flag this as a design fault requiring re-run or batch-randomized re-acquisition; no statistical correction fully rescues complete confounding.
4. **Per-donor cell-count audit:** record cells per donor; donors with extreme low counts (threshold to be calibrated; see Section 4) are flagged for sensitivity analysis (include/exclude) rather than silently dropped.

### Step 2 — Independent units

- **Experimental/inferential unit:** donor or animal (the level at which treatment is randomized).
- **Observational unit:** cell or field.
- If animals are co-housed and treatment is assigned per cage, the cage becomes the experimental unit; audit the randomization protocol to determine the true assignment level and adjust all grouping accordingly.
- Document n_donors per arm and n_cells per donor per arm in a standing table ("unit ledger") updated at every analysis stage.

### Step 3 — Allocation and blinding

- **Allocation:** randomize donors/animals to arms using a documented seed; stratify or block on known prognostic covariates (age, sex, baseline measures) if donor n is small, to reduce donor-level imbalance.
- **Blinding:** acquisition operators and image/cell annotators blinded to arm; analysis scripts run on coded arm labels until the primary analysis is locked. Segmentation, gating, and QC thresholds frozen before unblinding.

### Step 4 — Intervention and sampling

- Apply treatment per randomized donor assignment.
- **Sampling plan for cells/fields:** pre-specify fields per sample and a sampling scheme (e.g., systematic random field placement) to avoid operator selection of "good-looking" fields. Record field coordinates.
- Where feasible, **interleave arms within acquisition sessions** so batch and arm are crossed, not nested.

### Step 5 — Measurements

- Define the primary cell-level readout(s) and the donor-level summaries derivable from them (mean, median, proportion positive, per-donor distributional features).
- Include spike-in or reference controls per batch to allow technical-variance estimation (feeds the calibration in Section 4).

### Step 6 — Controls

- **Negative/vehicle control arm** randomized identically to treatment.
- **Technical replicate controls:** where possible, split one or more donors' material across batches to estimate batch variance separately from donor variance.
- **Negative-control analytes/features:** pre-specify features not expected to respond to treatment; these serve as empirical nulls for calibration (Section 4).

### Step 7 — Analysis plan (confirmatory + validation layers)

**7a. Primary: pseudobulk / donor-summary comparison.**
- Collapse each donor's cells to one (or a small fixed set of) summary statistic(s) per endpoint (mean, proportion, or sum as modality-appropriate).
- Compare arms with a test on donor summaries: two-sample t-test / Welch test, Wilcoxon rank-sum if donor n permits, or a linear model on donor summaries with batch covariates. Degrees of freedom = donor-level.
- Weighting: consider precision-weighting donor summaries by cell count only if calibration (Section 4) shows it preserves type-I error; otherwise unweighted.

**7b. Co-primary / sensitivity: hierarchical mixed model.**
- Cell-level outcome ~ treatment (fixed) + (1 | donor) [+ (1 | batch) or batch fixed effect], with distribution family matching the readout (Gaussian, binomial, negative binomial).
- Use small-sample df corrections (e.g., Kenward–Roger/Satterthwaite-type adjustments) because donor n is small; verify their calibration empirically (Section 4) rather than assuming asymptotics.
- Report the estimated ICC and variance components (donor, batch, residual). Per the evidence record, a high ICC changes uncertainty, not necessarily the point estimate — report both the naive cell-level estimate and the hierarchical estimate side by side to make this explicit.

**7c. Grouped resampling.**
- **Cluster (donor-level) bootstrap:** resample donors with replacement within arm, carrying all their cells; recompute the effect estimate; report percentile or BCa intervals. Never bootstrap cells across donors for confirmatory inference.
- **Donor-level permutation test:** permute arm labels across donors (respecting any stratification/blocking), recompute the test statistic; the permutation distribution provides an exact-level reference given small donor n. With very small n per arm, enumerate all permutations and report the minimum achievable p-value (e.g., with 3 vs 3 donors the smallest two-sided p is 0.1); if the minimum achievable p exceeds the significance threshold, state that confirmatory significance is unattainable at this n and treat results as estimation-only.

**7d. Held-out validation (for any predictive/classifier claim or multivariate signature).**
- **Leave-one-donor-out or grouped k-fold CV with donors as groups.** Cells from a donor never appear in both training and test folds.
- Report donor-level performance (e.g., per-donor AUC or per-donor predicted class), not pooled cell-level accuracy, as the headline metric; cell-level metrics may be shown as secondary with the caveat that they overstate independent evidence.
- If sufficient donors exist, hold out a fully untouched donor set for final validation after model lock.

**7e. Exploratory cell-level analyses.**
- Permitted for hypothesis generation (subpopulation discovery, dose-response shape within donors) but labeled exploratory; any cell-level p-value must be accompanied by the donor-level counterpart or omitted.

### Step 8 — Null calibration (central because variance components are unavailable)

Because exact donor numbers, cell numbers, effect sizes, and variance components are not given, **all thresholds and the choice among 7a/7b must be calibrated**, not assumed:

1. **Empirical null via permutation:** as in 7c, donor-label permutation gives a design-exact null for the primary test.
2. **Parametric-bootstrap calibration of the mixed model:** fit the model under the null (no treatment effect), simulate datasets with the *estimated* variance components and the *actual* donor/cell counts, refit, and record the distribution of p-values. Acceptance: null p-values approximately uniform (e.g., observed type-I error within a pre-specified tolerance of nominal at α = 0.05; tolerance to be preregistered, suggested ±2 percentage points as a placeholder calibration target).
3. **Negative-control feature calibration:** apply the full pipeline to the pre-specified non-responsive features; their p-value distribution should be approximately uniform and their FDR-significant count near zero.
4. **Mock-split calibration:** within the control arm only, randomly split donors into pseudo-arms and run the full pipeline; repeat many times. Any analysis variant that produces excess "significant" results in mock splits is rejected from the confirmatory toolkit.
5. **Method selection rule (preregistered):** if the mixed model fails calibration (common at very small donor n or with convergence problems), fall back to pseudobulk + permutation, which remains valid by construction.

### Step 9 — Power/precision calibration (proposed, since effect sizes unknown)

- Simulation grid: vary donor n per arm, cells per donor, ICC, and standardized effect size over plausible ranges informed by pilot data or literature for the modality.
- Deliverables: curves of power vs donor n at fixed ICC, demonstrating the expected plateau where adding cells (not donors) yields diminishing power — this directly operationalizes the record's point that cells do not substitute for independent replication.
- Use these curves to justify the final donor n and a minimum-cells-per-donor floor; the floor is where the power curve in cells-per-donor flattens (calibration output, not an invented number).

### Step 10 — Acceptance / stopping criteria (preregistered placeholders)

A treatment effect is declared **supported** only if all hold:
- Pseudobulk donor-level test significant at the preregistered α under the permutation null (7c), AND
- Hierarchical-model estimate agrees in sign and the cluster-bootstrap CI excludes the null, AND
- Null-calibration checks (Step 8, items 2–4) passed for the chosen analysis, AND
- For predictive claims: held-out-donor performance exceeds the permutation-derived chance band.

Declare **inconclusive** (not "effect absent") if the point estimate is directionally consistent but donor-level CIs include the null — consistent with the evidence record's caution that loss of significance after clustering correction does not prove a false effect. In that case recommend additional donors, not additional cells.

**Stopping:** stop enrollment when the preregistered donor n is reached; any sample-size re-estimation must be blinded (variance-only) and preregistered.

### Step 11 — Reporting requirements

Every result must state, in-line and in a unit ledger table:
- **n_donors per arm** (randomized-unit count) — basis of inference;
- **n_cells (or fields) total and per donor per arm** (observed-cell count) — basis of measurement precision;
- ICC and variance components;
- naive cell-level p-value alongside donor-level p-value (transparency about the pseudoreplication gap);
- permutation minimum-achievable p where donor n is small;
- which analysis (pseudobulk vs mixed model) was primary and why calibration selected it.

### Step 12 — Troubleshooting

| Problem | Diagnosis | Action |
|---|---|---|
| Mixed model non-convergence / singular fits | Donor n too small to estimate variance components | Fall back to pseudobulk + permutation (preregistered rule) |
| Naive and donor-level results diverge sharply | High ICC / dominant donor variance | Report both; emphasize donor-level; check for a donor outlier via leave-one-donor-out influence analysis |
| One donor drives the effect | Influence analysis flags it | Report with and without that donor; treat as hypothesis-weakening, not data exclusion |
| Batch confounded with arm | Confounding audit | Re-acquire with interleaved batches; do not report confirmatory inference |
| Highly unequal cells per donor | Cell-count audit | Compare weighted vs unweighted pseudobulk; prefer whichever passes calibration |
| Minimum achievable permutation p > α | Donor n too small | Reframe study as estimation/pilot; recruit more donors |

---

## 4. Calibration procedures for unknown parameters (summary)

| Unknown | Calibration procedure |
|---|---|
| Donor/batch/residual variance components | Estimate from pilot or control-arm data via the mixed model; technical-split donors separate batch from donor variance |
| ICC | Derived from variance components; report with bootstrap CI |
| Minimum donors per arm | Power simulation grid (Step 9) at target power over plausible ICC/effect ranges |
| Minimum cells per donor | Plateau point of simulated power/precision vs cells-per-donor curves |
| QC thresholds | Set blinded on control/pilot data; sensitivity analysis across threshold choices |
| Type-I tolerance for mixed model | Parametric bootstrap + permutation agreement (Step 8); preregister tolerance band |
| Weighting scheme | Mock-split and simulation calibration; adopt only if error rates preserved |

---

## 5. Alternatives, limits, and what would change the recommendation

**Alternatives considered:**
- **GEE with cluster-robust (sandwich) standard errors:** valid asymptotically in donor n; with few donors, robust SEs are anti-conservative, so it is acceptable only with small-sample corrections and only if it passes Step 8 calibration. Pseudobulk + permutation is more robust at small n.
- **Fully Bayesian hierarchical model:** attractive at small n (partial pooling, direct uncertainty on variance components); recommended as a sensitivity analysis with prior-sensitivity checks, but calibration (simulation-based coverage checks) is still required.
- **Cell-level analysis with donor as fixed effect:** controls donor mean differences but cannot estimate a between-donor treatment effect when treatment is assigned at donor level (treatment is collinear with donor); not viable for this design.

**Limits:**
- With very small donor n, the permutation test's granularity caps attainable significance; the study may be estimation-only regardless of cell numbers.
- Pseudobulk discards within-donor distributional information; cell-level heterogeneity effects (e.g., treatment changes variance, not mean) require donor-level summaries of dispersion as additional preregistered endpoints.
- Calibration via parametric bootstrap assumes the fitted variance structure is approximately correct; the permutation test guards against this but only for the exchangeability it tests.
- The evidence record itself is a summary; no quantitative parameters are available, so every numeric threshold here is a calibration target, not a result.

**What would change the recommendation:**
- If treatment were (or could be) randomized **within donor** (e.g., paired wells per donor), the donor becomes a block, within-donor contrasts become valid, and power per donor rises substantially — this design change dominates any analysis fix and should be adopted if feasible.
- If calibration shows the mixed model is well-calibrated at the realized donor n, it may be promoted to primary (gaining efficiency over pseudobulk).
- If ICC is estimated to be near zero with tight CIs, cell-level dependence is weak; donor-level inference remains the preregistered primary, but the naive/corrected gap will be small and additional cells gain more power than otherwise.
- Discovery of cage/litter-level assignment would move the inferential unit upward and require re-running all grouped procedures at that level.

**Residual uncertainty statement:** Because donor numbers, cell numbers, effect sizes, and variance components are unavailable, no claim is made here about achievable power or expected significance; the protocol's acceptance criteria are conditional on the preregistered calibration outputs. All content above is a proposal.

*(≈1,900 words)*
