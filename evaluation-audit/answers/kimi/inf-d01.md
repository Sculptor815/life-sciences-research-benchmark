# Kimi K3 / inf-d01

Original final answer, shared by both scoring rounds.

# Analysis design: paired tumor RNA–protein–metabolite data for a reproducible treatment-associated program

## 1. Bottom line and recommended next action

**Do not integrate anything until the metabolomics batch problem is resolved.** The decisive first step is a batch × timepoint audit per omics layer, followed (if the audit confirms aliasing) by a blinded, randomized bridge/rerun experiment on a subset of pre/post pairs. Only then:

1. Compute within-patient changes (Δ = post − pre; **patient is the independent unit, n = 30**) separately per omics layer.
2. Aggregate per-layer results to **pathway/program level** via ranked enrichment — this is the power-efficient unit of inference at n = 30.
3. Define the treatment-associated program as pathways **concordant across ≥2 omics layers**, with metabolomics counting only if the batch gate is passed.
4. Freeze every parameter, threshold, and feature list, then run **one single pre-registered evaluation** on the untouched second cohort (M4). Verdicts: *consistent / inconclusive / inconsistent*. No re-modeling afterward.

If the batch de-confounding fails or is infeasible, metabolomics is downgraded to exploratory, and the program claim rests on RNA + protein alone.

## 2. Consequential uncertainties (what would change the recommendation)

1. **Metabolomics batch–timepoint aliasing (M2).** If all or most post-treatment metabolomics samples sit in one batch containing no pretreatment samples, the treatment effect and batch effect are collinear and *not identifiable* from existing data. This determines whether metabolomics can support any claim at all.
2. **Missingness mechanism (M3).** Missing-not-at-random (e.g., below-detection censoring in metabolomics) vs. missing-at-random dictates imputation strategy and whether complete-case analysis is biased.
3. **Validation cohort size and design (M4, "small").** Determines whether M4 is confirmatory or merely supportive. Knowing its *n* and whether it is paired is metadata, not "touching" the data — obtain these before locking the analysis plan.
4. **Absence of an untreated control arm.** Nothing in the packet separates treatment effect from elapsed time, progression, or biopsy/handling effects. The honest estimand is "within-patient change over the treatment interval," i.e., *treatment-associated*, not treatment-caused. If a control cohort exists, the design upgrades to a difference-in-changes analysis.

## 3. Evidence → inference → conclusion chain

| Evidence | Inference | Consequence for design |
|---|---|---|
| **M1**: 30 patients, pre + post samples | Repeated measures on 30 independent units; pairing controls baseline heterogeneity; power suffices only for moderate–large per-feature effects (paired dz ≈ 0.5 at 80% power, α = 0.05, before multiplicity) | Unit = patient; analyze Δ per patient; all resampling, cross-validation, imputation at patient level; aggregate to programs for power |
| **M2**: RNA and protein in distinct batches; most post-treatment metabolomics share one batch | Batch may be confounded with timepoint; for metabolomics likely near-perfect aliasing → treatment signal not separable from batch artifact | Mandatory batch audit; per-omics-first analysis (integration would average the artifact in); blinded bridge/rerun experiment as gate for metabolomics claims |
| **M3**: Some assays missing | Information loss with unknown mechanism; naive complete-case analysis risks bias and further power loss | Diagnose mechanism; mechanism-appropriate imputation fitted on discovery data only; prespecified sensitivity analyses |
| **M4**: second small cohort, untouched | One-shot external validation resource; too small for discovery | Lock entire pipeline before use; pre-register success criteria; frame results as estimation with confidence intervals, not powered confirmation |

## 4. Roles of integration, enrichment, and external validation — and their correct relationship

The pipeline is: **per-omics paired statistics → ranked lists → enrichment → cross-omics concordance → frozen program score → single external test.** Each concept has a distinct job:

- **Integration** (cross-omics combination) *discovers and defines* the program. Its value is discriminating robust biology from platform-specific noise: a change visible in RNA *and* protein *and* metabolites is far less likely to be an artifact of any one assay. **Critical caveat: integration cannot repair confounding — it propagates it.** Because of M2, joint latent-factor models (MOFA, DIABLO/mixOmics) run on all layers up front risk a dominant "factor" that is simply the metabolomics batch. Integration is therefore staged: per-layer analysis first, cross-layer concordance second, joint latent-factor modeling third as a sensitivity analysis with explicit batch-association checks on every factor.
- **Enrichment** (pathway/gene-set analysis) *names and stabilizes* the program. Three functions: (a) **power** — at n = 30, single features rarely survive FDR, but coordinated moderate shifts across a pathway do; (b) **common currency** — genes, proteins, and metabolites all map onto pathways, enabling cross-layer comparison despite incompatible measurement scales; (c) **transportability** — pathway-level scores replicate across cohorts and platforms better than individual feature lists.
- **External validation** (M4) *certifies* reproducibility. It is the only evidence in the packet bearing on the word "reproducible." It tests transportability of a **frozen** score — no re-derivation, no threshold tuning, single use. Its small size means it yields an effect estimate with a confidence interval, not a definitive proof.

## 5. Operational protocol (ordered)

### Step 0 — Governance and pre-specification
- Write and date the full analysis plan *before* touching outcome structure: primary endpoint (program score Δ), program definition rule, FDR levels, missing-data rules, validation success criteria, and the metabolomics decision tree.
- Data-use rule: M4 stays sealed until Step 7.7 lock. Obtain only metadata (n, paired vs. unpaired, treatment regimen, platform).
- **Assumption (stated):** treatment has already been administered and samples collected; this is a retrospective analysis plus prospective calibration experiments. Treatment allocation is not under analyst control.

### Step 1 — Preparation and quality checks
- Build the patient × timepoint × omics presence matrix; draw the sample-flow diagram (M1, M3).
- **Batch audit (M2):** per omics, cross-tabulate batch × timepoint. Flag aliasing: any post-treatment batch containing no pretreatment samples.
- Sample-level QC: RNA (yield, integrity, mapping metrics where available); protein (per-sample missing rate, intensity distributions); metabolites (pooled-QC coefficients of variation, run-order drift).
- Feature-level QC: detection rates, variance.
- **Gate 0 — metabolomics identifiability.** If aliased:
  - **Proposed experiment (labeled): bridge/rerun.** Re-assay a subset of complete pre/post pairs (target 12–15 pairs, budget permitting) with: randomization of all samples across ≥2 new batches; pooled QC samples interleaved; technical replicates; operators blinded to pre/post status and patient identity.
    - *Calibration — subset size:* choose the smallest n for which the 95% CI half-width on the rerun-vs-original Δ correlation is below a pre-chosen margin; estimate required n from a small pilot (e.g., 4 pairs) or published platform repeatability — do not invent a fixed number.
    - *Calibration — concordance threshold:* compute Lin's CCC and Spearman ρ between original and rerun Δ values; compare against the null distribution from 1,000 within-patient label permutations; require observed concordance above the 95th null percentile.
  - Outcomes: **(a)** concordant → retain metabolomics with batch adjustment informed by rerun-estimated batch effects; **(b)** discordant → metabolomics exploratory only; **(c)** rerun infeasible → sensitivity bounds using the minority of post samples in other batches, exploratory label only.
- RNA/protein: if batches are mixed across timepoints, plan covariate adjustment or batch correction *with the timepoint term protected*; verify afterward via variance components (Step 9).

### Step 2 — Independent units
- The independent unit is the **patient** (n = 30), not the sample (60). Primary observation: per-feature Δ vector per patient.
- Never split a patient's pre/post samples across training/test folds, imputation groups, or normalization reference sets.
- Patients missing an entire layer (M3) enter listwise per layer — never drop a patient from RNA because metabolites are missing.

### Step 3 — Allocation and blinding
- No treatment randomization possible (retrospective). Blinding measures that *are* possible:
  - Rerun laboratory staff blinded to timepoint and identity; randomized plate layout.
  - Discovery analysis (analyst/script A) separated from validation execution (analyst/script B), with B receiving only the frozen pipeline.
  - All decisions documented as outcome-independent (based on QC metadata only) or flagged as outcome-dependent.

### Step 4 — Intervention and sampling (documentation and rival hypotheses)
- **Unreported parameters to request/record:** drug, dose, schedule; interval between pre and post sampling; biopsy procedure and site; collection-to-freeze times; storage conditions.
- Because no control arm exists, enumerate rival explanations for Δ (progression, wound-healing/biopsy response, handling drift, interval-length variation) and address each: interval length as covariate in sensitivity analysis; stability-negative controls (Step 6); external validation.
- **Proposed experiment (labeled):** prospective controlled cohort (treated vs. untreated/standard-of-care) with randomized sampling order to separate treatment from time — required for any eventual causal claim.

### Step 5 — Measurements
- **RNA:** filter low-count features (*calibration:* threshold from the detection-vs-mean curve, not a fixed count); library-size normalization (TMM or median-of-ratios); log2. Batch: covariate in the model, or correction preserving the timepoint term.
- **Protein:** platform is an **unreported parameter** — assume a quantitative abundance matrix. Log2; median or quantile normalization; same batch handling; record antibody/assay versions.
- **Metabolites:** pooled-QC drift correction (e.g., LOESS over run order), quotient normalization, log/glog transform. Flag left-censored (below-LOD) values explicitly; never silently impute.
- Harmonize identifiers across layers (gene symbols/Ensembl; HMDB/KEGG for metabolites). **Assumption:** sufficient identifier overlap between discovery and validation platforms; quantify mapping rate and report it.
- Store every normalization parameter for frozen application to M4.

### Step 6 — Controls
- **Technical:** pooled QCs; bridge replicates; randomized run order (rerun).
- **Statistical negative controls:** (a) within-patient timepoint-label permutation (preserves pairing) → empirical null for Δ statistics *and* enrichment results; (b) size-matched random pathway sets → detect enrichment inflation; (c) technical replicates → measurement noise floor.
- **Positive controls:** drug identity is unreported; if known, pre-specify 2–3 pathways with expected response from prior literature as positive controls; if unknown, omit and note.
- **Biological controls:** none available — stated as a core limitation; rival-hypothesis checklist reported with results.

### Step 7 — Analysis
1. **Per-omics paired inference.** Δ per patient per feature; moderated paired tests (patient-blocked linear models) plus Wilcoxon signed-rank as robustness; Benjamini–Hochberg FDR within each layer; report effect sizes with CIs, not p-values alone.
2. **Missing data (M3).** Diagnose mechanism first: regress missingness indicators on timepoint, batch, and observed intensities (left-censoring signature = missingness concentrated at low abundance). MNAR-type → LOD-based or left-censor-appropriate imputation; MAR → multiple imputation fitted **within discovery data only**. Sensitivity: correlation of Δ statistics between complete-case and imputed analyses; report both.
3. **Enrichment.** Pre-ranked enrichment on the signed paired statistic per layer, against pre-specified pathway databases with fixed versions. *Calibration:* run two independent databases; only pathways concordant across both enter the primary program (reduces database-arbitrariness). FDR per layer; check against negative-control sets.
4. **Integration (secondary/sensitivity).** MOFA or sparse multi-block PLS on Δ matrices (MOFA handles missingness natively — relevant to M3). *Calibration:* factor count by variance-explained plateau plus patient-level cross-validation. Annotate each factor by enrichment; **test every factor for association with batch labels before biological interpretation**; discard batch-associated factors.
5. **Program definition.** Program = pathways with FDR < 0.05 in ≥2 of 3 layers (metabolomics counts only if Gate 0 passed) *or* mapping onto a significant batch-clean integrated factor.
6. **Program score.** Per patient: mean of per-layer pathway scores (single-sample enrichment-style scores of Δ), combined with **pre-specified equal weights** to avoid overfitting; data-driven weights via nested patient-level CV only as sensitivity.
7. **Internal reproducibility.** Patient-level bootstrap (≥500 resamples) → selection frequency per pathway. *Calibration:* cutoff = 95th percentile of selection frequency under the label-permutation null.
8. **Lock.** Freeze code, parameters, feature/pathway lists, weights, thresholds; archive with hash. Register the validation hypothesis.
9. **External validation — single run.** Compute the frozen score on M4. Primary: one-sided test of program Δ in the predicted direction with 95% CI. Secondary: rank correlation of pathway-level effects between cohorts (*calibration:* floor from permutation null). Verdict per pre-registered rule: **consistent / inconclusive / inconsistent.** No downstream changes.

### Step 8 — Acceptance and stopping criteria
- **Gate 0:** metabolomics identifiability resolved (Step 1); else descope metabolomics.
- **Gate 1 (discovery):** ≥1 pathway passes cross-layer concordance **and** bootstrap stability. If none: stop; report as hypothesis-generating; do **not** open M4 for exploratory searching.
- **Gate 2 (lock):** all parameters frozen; plan registered.
- **Gate 3 (validation):** pre-specified success rule met or not. If not met: stop; report the negative/inconclusive result; **do not reopen development using M4** — any new attempt requires new data.
- **Futility stop:** if post-QC effective paired n for a layer falls below the minimum for the smallest effect of interest — *calibration:* derive minimum n from a power calculation at a biologically motivated effect size; if no such size can be justified, report the detectable-effect curve instead of inventing one.

### Step 9 — Troubleshooting
- **Batch correction attenuates Δ** (correction eats biology): switch to batch-as-covariate in the paired model or negative-control-based factor adjustment; compare Δ before/after; if unresolved, restrict claims to batch-robust features.
- **Rerun discordant with original metabolomics:** downgrade layer; *proposed experiment:* targeted re-quantification of top candidate metabolites under fully randomized, blinded design.
- **Missingness concentrated post-treatment:** possible informative dropout (toxicity/response-related) — test association with clinical variables; pattern-mixture sensitivity; label affected claims.
- **RNA–protein discordance:** check translation lag, protein half-life, antibody validity; keep layers separate rather than forcing concordance; discordance is a finding, not a bug.
- **Validation platform mismatch:** if member-feature mapping falls below a pre-set floor (*calibration:* floor from simulation of score robustness to member dropout), verdict = *inconclusive*, not failure.
- **Validation underpowered:** report CI and minimum detectable effect; avoid binary overclaiming.

## 6. Alternatives considered and rejected (or demoted)

- **Joint latent-factor integration as primary analysis** — demoted to sensitivity: M2 confounding would contaminate shared factors.
- **Complete-case analysis across all layers** — rejected as primary (M3: discards patients, risks bias); retained as sensitivity.
- **Single-feature discovery with stringent FDR** — rejected as primary: underpowered at n = 30; programs are the appropriate unit.
- **Data-driven program-score weights** — demoted to sensitivity: overfitting risk; equal weights pre-specified.
- **Internal cross-validation instead of external validation** — rejected as sufficient: cannot demonstrate transportability; acceptable fallback only if M4 becomes unusable.

## 7. Limits

- **Association, not causation:** no untreated control arm; Δ mixes treatment, time, progression, and handling effects. The word "treatment-associated" is deliberate.
- **Two timepoints only:** no kinetics, reversibility, or dose-response.
- **Selection:** post-treatment biopsies come from patients well enough to be re-biopsied; expect survivorship/responder enrichment.
- **Metabolomics may be unrecoverable** if reruns are infeasible and aliasing is perfect — no statistical method creates identifiability.
- **Database dependence:** program definitions shift with pathway database choice; mitigated, not eliminated, by dual-database concordance.
- **Small validation cohort:** even a "consistent" verdict carries wide uncertainty; reproducibility claim is graded, not absolute.
- **Unreported parameters** (treatment identity, sampling intervals, protein platform, tumor purity): purity is estimable from RNA deconvolution and usable as a sensitivity covariate; the rest must be obtained as metadata before lock — none can be assumed.
