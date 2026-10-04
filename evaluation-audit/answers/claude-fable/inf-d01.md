# Claude Fable 5 / inf-d01

Original final answer, shared by both scoring rounds.

# Analysis Design: Identifying a Reproducible Treatment-Associated Multi-Omic Program

## Bottom line / recommended action

Run a **paired (within-patient) pre/post analysis** with RNA and protein as the primary discovery layers, treat the **metabolomics layer as confounded and supporting-only** (because post-treatment samples largely share a batch, treatment effect and batch effect are nearly non-identifiable there), use **missing-data-tolerant latent-factor integration** (e.g., a MOFA-class model) rather than hard imputation, define the "program" at the **pathway/module level via enrichment**, **lock a single signature with a frozen scoring rule**, and spend the second cohort **exactly once** as a confirmatory test with pre-registered pass/fail criteria. The single most consequential uncertainty is the metabolomics batch–timepoint confound; the single most consequential rule is never touching cohort 2 during development.

---

## 1. Evidence → inference → conclusion chain

| Evidence | Inference | Design conclusion |
|---|---|---|
| **M1:** 30 patients with pre- and post-treatment samples | Pairing allows each patient to serve as their own control, removing stable inter-patient variation (germline, baseline tumor state); n = 30 pairs is modest, so power is limited for feature-level discovery but better for module-level effects | Use paired statistics (within-patient deltas or mixed models with patient random effect); aggregate to pathways/factors to gain power; do not expect reliable single-feature discovery |
| **M2:** RNA and protein in different batches; most post-treatment metabolomics in one shared batch | RNA/protein batch structure is correctable *if* batch is not aligned with timepoint; for metabolomics, batch ≈ timepoint, so standard batch correction would also remove (or fabricate) the treatment signal — the effect is statistically confounded | Demote metabolomics from discovery to corroboration; quantify the confound (check the design matrix rank/aliasing); for RNA/protein, verify batch–timepoint balance before correcting; require cross-omic concordance rather than metabolite-only claims |
| **M3:** Some assays missing | Complete-case analysis shrinks n and can bias toward patients with complete sampling (missingness may not be random); naive imputation can manufacture cross-omic correlation | Use integration methods that natively handle block-wise missingness; characterize missingness mechanism; run complete-case sensitivity analysis; never impute across omic layers before testing cross-layer concordance |
| **M4:** Second cohort must remain untouched | Any peeking (even QC-level tuning informed by cohort-2 signal) invalidates it as external validation | Freeze all pipeline choices, thresholds, gene/protein lists, and the scoring function on cohort 1; apply once to cohort 2; report the result regardless of outcome |

**Overall conclusion:** reproducibility is achievable only for a program that (a) survives paired testing in RNA and protein independently, (b) is coherent at the pathway level, (c) is at most *consistent with* (not driven by) metabolomics, and (d) replicates as a pre-locked score in cohort 2.

---

## 2. Roles of the three pillars

**Integration.** Its role is to find *shared* treatment-associated variation across molecular layers, which protects against layer-specific artifacts (an RNA batch effect is unlikely to reproduce as a correlated protein shift in the same patients). Concretely: a multi-omic factor model fit on within-patient pre→post changes yields latent factors; a treatment program is a factor with significant loading structure in ≥2 layers and a consistent direction across patients. Integration also pools power across layers — critical at n = 30. It does **not** rescue the metabolomics confound: a factor loading only on metabolites and separating timepoints is presumptively a batch factor.

**Enrichment.** Its role is to translate feature-level statistics into a *biologically interpretable, statistically more stable* unit — the program. Pathway/gene-set tests (paired-contrast ranks → competitive gene-set enrichment; analogous protein-set and, cautiously, metabolite-set enrichment) average over noisy individual features, reducing variance and multiple-testing burden. Enrichment is also the natural layer at which to demand **cross-omic concordance**: the same pathway should enrich in RNA-derived and protein-derived rankings. Limit: enrichment inherits annotation bias (well-studied pathways look "significant" more easily), so use competitive tests with permutation of patient labels (not gene labels) to preserve inter-feature correlation.

**External validation.** Its role is to estimate out-of-sample reproducibility free of the selection, tuning, and overfitting that discovery necessarily incurs. With 30 pairs, internal cross-validation is optimistic (pipeline choices leak information). The second cohort provides the only unbiased estimate — but only if it is used once, blind, with a frozen artifact: the feature list, the weights/direction, the normalization recipe (anchored to cohort-2-internal references, not cohort-1 scaling constants), and the success criterion, all written down before unblinding.

---

## 3. Operational protocol (ordered)

### Step 0 — Pre-registration and freeze discipline
Write an analysis plan before touching data beyond QC: hypotheses, layer roles (RNA/protein primary; metabolomics supporting), statistical models, thresholds (or the calibration procedures that will set them), and cohort-2 success criteria. Sequester cohort 2 (separate storage/access; ideally a colleague holds it).

### Step 1 — Preparation and quality checks
1. **Sample manifest audit:** reconcile IDs across layers; verify pre/post labels; build a patient × (layer × timepoint) availability matrix (addresses M3).
2. **Per-layer QC:** RNA — library size, mapping/duplication rates, degradation metrics; protein — missingness per sample, CV on any replicate/pooled QC runs; metabolomics — internal standards, total signal drift, QC-pool CVs if pooled QCs were run.
3. **Confound mapping (critical):** cross-tabulate batch × timepoint × patient for each layer. Compute the aliasing: for metabolomics, quantify what fraction of post samples share the batch (M2 says "most"). The off-batch post samples and any mixed-batch pre samples are the only leverage for separating batch from treatment — identify and protect them.
4. **Unsupervised structure check:** PCA/UMAP per layer colored by batch, timepoint, patient. Expected: patient pairing visible; batch effects visible in RNA/protein; in metabolomics, batch and timepoint will co-separate — document this.
5. **Missingness mechanism:** test whether missing assays associate with timepoint, batch, or clinical covariates (logistic regression of missingness indicator). If missingness tracks treatment/response, flag as a bias risk for all downstream claims.

### Step 2 — Independent units
The **independent unit is the patient** (n = 30). The paired pre/post samples within a patient are not independent; all tests must respect this (paired tests, patient random effects, permutations that shuffle *patient-level* labels or sign-flip within-patient deltas). Features within a pathway are also correlated — enrichment nulls must be sample-permutation based, not feature-permutation based.

### Step 3 — Allocation and blinding
Treatment allocation is already fixed (observational pre/post); the controllable allocation is **analytic**:
- Blind analysts to clinical outcomes during pipeline construction where feasible.
- Use scrambled sample IDs for batch-correction tuning so correction choices cannot be steered by desired biology.
- Create **negative-control labels**: randomly permuted pre/post assignments (sign-flips of deltas) processed through the identical pipeline. The pipeline's false-positive behavior is calibrated on these.

### Step 4 — Intervention and sampling
Intervention (treatment) and sampling are historical; the design task is to **encode their structure**: record time-from-treatment-to-biopsy, biopsy site (same lesion vs different), and tumor purity per sample. Within-patient purity shifts pre→post are a major alternative explanation for any "program" (see §5). Estimate purity from RNA (e.g., deconvolution/immune-stromal scores) and include the pre→post purity delta as a covariate or run purity-adjusted sensitivity analyses.

### Step 5 — Measurements and preprocessing
1. **RNA:** standard normalization (e.g., TMM/variance-stabilized counts); filter low-expressed genes using a data-driven threshold (see §6 calibration).
2. **Protein:** log-transform, normalize (median or variance-stabilizing); distinguish missing-at-random from below-detection missingness; do not impute below-detection values with means.
3. **Metabolomics:** log-transform; drift-correct within batch using QC pools if available; **do not apply cross-batch correction that uses timepoint-confounded batches** — instead carry batch as an acknowledged, uncorrectable covariate aliased with timepoint.
4. **Batch correction (RNA/protein only):** apply only if batch and timepoint are demonstrably non-aliased (Step 1.3). Prefer including batch as a fixed covariate in the differential model over pre-correcting the matrix; if pre-correction is needed for the factor model, use a method that preserves specified covariates (timepoint, patient) and verify via before/after PCA and via negative-control sign-flip runs that correction does not inject timepoint signal.

### Step 6 — Controls
- **Negative controls:** (a) sign-flipped pre/post labels (null pipeline runs); (b) housekeeping/stability feature sets expected to show no treatment effect — their enrichment statistics calibrate the null; (c) batch-indicator "pseudo-treatment" in RNA/protein to measure residual batch leakage after correction.
- **Positive controls:** known pharmacodynamic markers of the treatment class, if any exist in annotation — not required for discovery, but their behavior is a sanity check on direction and assay sensitivity. (If the treatment's expected markers are unknown, state this as a limit rather than inventing them.)
- **Technical controls:** pooled QC samples and internal standards per layer, used for CV thresholds and drift assessment.

### Step 7 — Analysis (ordered)
1. **Paired differential analysis per layer:** mixed model or paired moderated test (feature ~ timepoint + batch [RNA/protein] + purity-delta, patient as random/blocking factor). Output: per-feature effect sizes and ranks. For metabolomics, run the same model *without* batch (impossible to include) and label all results "treatment-OR-batch."
2. **Enrichment per layer:** rank-based competitive gene-set/protein-set/metabolite-set enrichment with patient-level sign-flip permutation nulls; FDR control within layer.
3. **Integration:** fit a multi-omic latent factor model on within-patient delta matrices (RNA, protein, metabolite deltas), using a method tolerant of block-missing samples (M3). Identify factors with (i) non-zero variance explained in ≥2 layers, (ii) consistent sign across ≥~2/3 of patients (threshold calibrated by sign-flip null, §6), and (iii) loadings enriched for the pathways found in step 2 (cross-check, not circular proof — the factor model and the enrichment use the same data; concordance here is internal coherence, not validation).
4. **Program definition:** the candidate program = the pathway/module set jointly supported by RNA and protein enrichment and by a cross-layer factor; metabolite loadings reported as "consistent/inconsistent," never as primary evidence.
5. **Signature construction and freeze:** build a simple, transferable score — e.g., mean of z-scored expression of the program's RNA genes (and optionally a parallel protein score) applied to pre→post deltas. Simplicity matters: cohort 2 is small, and complex weighted models overfit. Freeze: feature lists, signs, scoring formula, cohort-internal normalization recipe, and the statistical test (paired one-sided test of score delta in the pre-registered direction).
6. **Internal robustness (before external test):** leave-one-patient-out stability of the feature list (report overlap/Jaccard); sign-flip null distribution of the frozen score; purity-adjusted re-run.
7. **External validation (single shot):** apply the frozen score to cohort 2. Pass/fail per Step 8. Report the result either way; no post-hoc modification of the signature after seeing cohort-2 data.

### Step 8 — Acceptance and stopping criteria (pre-registered)
- **Discovery acceptance:** ≥1 pathway/factor with FDR < pre-set level (calibration in §6) in *both* RNA and protein enrichment, consistent direction, surviving purity adjustment, and leave-one-out feature stability above the null-calibrated threshold. If metabolomics agrees, report as corroborating; if it disagrees, report, and attribute cautiously given the confound.
- **Stopping rule (discovery):** if no cross-layer concordant signal passes after the pre-registered analysis plus the pre-listed sensitivity analyses, stop; do **not** iterate thresholds until something passes. Report a null result for a cross-omic program; feature-level or single-layer findings may be reported as hypothesis-generating only.
- **Validation acceptance:** cohort-2 paired score shift in the pre-specified direction at the pre-registered α (one test, no multiplicity). Secondary descriptive endpoint: directional consistency of individual program features (fraction concordant vs. binomial null). Failure in cohort 2 = the program is not validated; it may still motivate a new, larger study, but it cannot be rescued by re-analysis of cohort 2.

### Step 9 — Troubleshooting (decision rules, pre-listed)
- **Batch correction leaks or over-corrects (RNA/protein):** detected via negative-control pseudo-treatment runs; switch from matrix pre-correction to covariate modeling, or restrict analysis to batch-balanced subsets.
- **Metabolomics confound total (no off-batch leverage at all):** drop metabolomics from all inferential claims; optionally propose (as a **new experiment**) re-running a bridging subset of pre and post samples in a single fresh batch to break the aliasing — this is the only clean fix.
- **High missingness concentrated in one timepoint/layer:** report, restrict the factor model to patients with ≥2 layers per timepoint, and present complete-case vs. full-model concordance.
- **Factor dominated by purity:** if factor loadings correlate strongly with purity-delta, re-fit with purity regressed out; if the program vanishes, report it as confounded by tumor-content shift.
- **Unstable feature list (low leave-one-out overlap):** report at pathway level only; do not freeze a feature-level signature; validation then tests pathway-score reproducibility instead.

---

## 4. Calibration procedures for unknown parameters (not invented values)

- **FDR/α thresholds:** set the discovery FDR by requiring that the sign-flip negative-control pipeline yields ~0 passing programs across many null runs; choose the strictest conventional level consistent with retaining power in null-calibration simulations on the real data's correlation structure.
- **Number of latent factors:** choose by variance-explained elbow plus parallel analysis against sign-flip/permuted data — retain factors whose variance explained exceeds the null's 95th percentile.
- **Low-expression / high-missingness feature filters:** sweep the filter, pick the value maximizing replicate/QC-pool reproducibility (or pre/post rank stability under subsampling), not the value maximizing downstream significance.
- **Patient-consistency threshold for a factor (step 7.3):** take the 95th percentile of consistency under sign-flip nulls.
- **Leave-one-out stability threshold:** compare observed Jaccard overlap to the null distribution from sign-flipped runs; require exceedance of the null's upper tail.
- **Cohort-2 normalization:** anchored entirely within cohort 2 (its own medians/variances), validated in advance on cohort-1 held-out folds to confirm the recipe is self-contained — this check uses only cohort 1.

---

## 5. Alternatives considered and limits

**Alternatives.**
- *Early (concatenation) integration:* simple but dominated by the layer with most features and intolerant of block missingness — rejected given M2/M3.
- *Late integration only (per-layer tests + overlap):* robust and interpretable; kept as the enrichment-concordance backbone, but it misses weak shared signals the factor model can pool — so both are used, with concordance between them required.
- *Supervised cross-omic models (e.g., sparse CCA/PLS on deltas):* higher power but higher overfitting risk at n = 30; acceptable only with the same freeze-and-validate discipline; the unsupervised factor route is preferred as primary.
- *Imputing missing assays:* rejected for cross-layer inference (fabricates concordance); permitted only within-layer for technical missingness with sensitivity checks.

**Limits.**
- The metabolomics treatment effect is **not identifiable** in this dataset as described; any metabolite claim is "treatment-or-batch" unless bridging samples are re-run. This is a hard limit, not a statistical nuisance.
- n = 30 paired + a "small" validation cohort gives limited power; a validation failure is ambiguous between a false discovery and underpowered confirmation — the pre-registered report must say which effect size cohort 2 could detect (computable from cohort-2 n and cohort-1 variance, before unblinding, using cohort-2 sample count only).
- Observational pre/post design: time, disease progression, prior biopsies, and sampling-site differences are all confounded with "treatment." The program is honestly described as **treatment-associated**, not treatment-caused.
- Enrichment annotation bias and purity shifts remain partially controllable only; both are addressed by sensitivity analyses, not eliminated.
- If missingness (M3) is outcome-related, even the validated program may generalize only to the sampled sub-population.

**What would change the recommendation:** discovery of a substantial set of off-batch post-treatment metabolomics samples (restores metabolomics as a discovery layer, with batch as a covariate); evidence that RNA/protein batches are also aliased with timepoint (would force the bridging-rerun proposal for those layers too, as a new experiment); or a larger second cohort (would justify a weighted, learned signature rather than the simple mean-z score).
