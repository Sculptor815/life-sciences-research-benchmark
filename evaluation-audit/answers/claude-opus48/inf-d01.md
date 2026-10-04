# Claude Opus 4.8 / inf-d01

Original final answer, shared by both scoring rounds.

## Bottom line / recommended approach

Analyze within-patient **pre→post differences** (each patient is its own control), run **per-assay paired differential analysis first**, then integrate and interpret at the **pathway level** via enrichment, and define the "treatment-associated program" as the set of pathways that change **concordantly across at least two assays whose technical batches are independent of each other** (RNA and protein — M2). Keep raw-feature multi-omics integration (e.g., latent-factor models) as a secondary, hypothesis-generating layer. Treat the metabolome as **supportive only**, because its batch is confounded with timepoint (M2) and that confound is not statistically removable from this cohort. Freeze the entire pipeline — feature list, directions, and a single scoring function — **before** opening cohort 2 (M4), which provides the only genuine test of reproducibility.

The single most consequential decision is how you handle the metabolomics confound. If you let it enter the "program" definition on equal footing, any apparent metabolite signature is uninterpretable. The design below quarantines it.

---

## Concepts and their relationships

- **Paired design (M1)** is the backbone: the post−pre contrast within a patient removes all time-invariant patient-level confounders (genetics, baseline disease, demographics). The independent experimental unit is the **patient (n≈30)**, not the sample.
- **Integration** combines information across assays. Its scientific value here is *corroboration under independent error structures*: because RNA and protein were processed in different batches (M2), a change seen in both is unlikely to be a shared technical artifact. Integration raises specificity; it does not create power from nothing.
- **Enrichment** aggregates many weak, noisy feature-level signals into pathway-level statements and provides a **common coordinate system** across platforms (genes, proteins, and metabolites all map to pathways/reactions). This is what makes "concordance across assays" operational — you rarely get the identical analyte on all three platforms.
- **External validation (M4)** is the reproducibility test. Development data always produce an optimistically biased program; only a locked analysis applied to untouched data estimates real effect size.

Relationship: discovery (per-assay deltas) → integration/enrichment (program definition) → external validation (reproducibility estimate). Each stage narrows claims; none substitutes for the next.

---

## Evidence → inference → conclusion

**Chain 1 (design).** M1: paired pre/post for 30 patients → within-patient deltas eliminate static confounders and increase power versus unpaired comparison → **Conclusion:** model the contrast with paired/mixed-effects methods, treat patient as the replication unit, n=30.

**Chain 2 (metabolomics confound — the hard limit).** M2: most post-treatment metabolomics share one batch → batch is (nearly) collinear with timepoint for metabolites → treatment effect and batch effect are not separable by covariate adjustment → **Conclusion:** you cannot make a defensible causal/treatment claim from metabolomics in this cohort. Use it only to generate hypotheses and to *check consistency* with RNA/protein; require cohort-2 confirmation before any metabolite is called part of the program.

**Chain 3 (RNA vs protein batches — turn a problem into a control).** M2: RNA and protein were run in different batches → their technical artifacts are statistically independent of each other → a biological change in a pathway should appear in both, but a batch artifact should not → **Conclusion:** cross-assay RNA–protein concordance is a built-in negative control for technical artifact and should be the *primary* program-definition criterion.

**Chain 4 (missingness).** M3: some assays missing → missingness has (at least) two mechanisms: structural (a whole assay absent for a patient — plausibly missing-at-random w.r.t. biology) and analyte-level left-censoring in metabolomics (missing-not-at-random, below detection) → different handling required → **Conclusion:** use methods that tolerate unbalanced data (mixed models, limma on available pairs) rather than cross-assay imputation that would smear the confounded batch structure.

**Chain 5 (validation).** M4: second cohort must stay untouched during development → any parameter touched by cohort 2 invalidates it as a test → **Conclusion:** prespecify and freeze everything; cohort 2 yields one or a few prespecified tests, not a re-optimization.

---

## Operational protocol (ordered)

### 1. Preparation and quality checks

1. **Assemble a sample/feature manifest.** For every patient record: assay availability, timepoint, processing batch, run order, extraction date. Explicitly tabulate the **batch × timepoint cross-table for each assay**; this is how you confirm the M2 confound severity before analysis.
2. **Per-assay QC.** Standard steps: remove low-quality samples (RNA: library size, rRNA %, mapping rate; protein: ID counts, TIC; metabolite: internal-standard recovery, QC-sample CV). *Calibration (not fixed thresholds):* set exclusion cutoffs from the empirical distribution of QC metrics (e.g., flag samples beyond a prespecified quantile or median-absolute-deviation rule), decided and recorded **before** differential testing.
3. **Quantify batch severity — decision gate for metabolomics.** 
   - If pooled QC samples / internal standards exist, estimate technical CV and the fraction of total variance attributable to batch using variance-partition (random-effects for batch) or PCA with batch coloring. 
   - *Calibration procedure:* compute the proportion of timepoint-associated variance that is collinear with batch. If collinearity is near-complete (VIF effectively infinite / batch and timepoint perfectly nested), record metabolomics as **not batch-correctable** and route it to the supportive-only track. Do not invent a correction that the design cannot support.
4. **Normalization.** RNA: within-sample normalization + variance stabilization (e.g., log-CPM/VST). Protein: log-transform + median/quantile normalization suitable for the platform. Metabolites: log-transform, probabilistic-quotient or internal-standard normalization. *Calibration:* choose among normalization options by maximizing agreement of technical replicates / QC samples, not by looking at the treatment effect.

### 2. Independent units

- The replicate unit is the **patient**. All n for power and all resampling (permutation, bootstrap) operate at the patient level. A patient contributes a paired delta per assay where both timepoints exist.

### 3. Allocation / blinding

- There is no randomization to design (observational pre/post), but impose **analytic blinding**: QC, normalization, and missingness decisions are made with timepoint/outcome labels masked where possible (e.g., label batches/samples by code). This prevents QC choices from being tuned to the hoped-for signal.
- **Cohort 2 is sealed** (M4): no cohort-2 file is opened, inspected, or used to choose any parameter during development.

### 4. Intervention and sampling

- Intervention is the treatment already administered (M1). Record, per patient, the pre and post sampling times relative to dosing and any protocol deviations; model them as covariates if variable (see analysis).

### 5. Measurements

- Three readouts per patient-timepoint: RNA abundance, protein abundance, metabolite abundance, as supplied. Define the analyte-feature space per assay after QC/filtering (step 7a).

### 6. Controls

- **Internal technical control:** QC/pooled samples and internal standards (used in step 1c).
- **Biological pairing control:** within-patient baseline is the comparator.
- **Artifact control:** RNA↔protein concordance across independent batches (Chain 3).
- **Statistical null control:** label-permutation (shuffle pre/post *within patient*, preserving pairing and patient structure) to calibrate concordance and enrichment significance.
- **Negative-control features:** housekeeping genes/proteins and spike-ins should show no pre/post shift; a shift flags residual technical drift.

### 7. Analysis

**7a. Feature filtering and missingness.**
- Retain a feature if detected in ≥ a fraction *f* of informative samples. *Calibration of f:* run a sensitivity sweep (e.g., f from lenient to strict) and choose the value at which the number of retained features and downstream pathway results stabilize; record the chosen f before enrichment. 
- Classify metabolite missingness: if left-censored (MNAR), either analyze presence/absence separately or use a left-censoring-aware model; **do not mean-impute** across the confounded batch.
- Structural (whole-assay) missingness: handle by using all available pairs in mixed models rather than discarding patients.

**7b. Per-assay differential (discovery).**
- Model the within-patient contrast with a paired/mixed-effects approach: outcome = feature value, fixed effect = timepoint, random intercept = patient; include available technical covariates (batch, run order) **only where they are not collinear with timepoint**. For RNA and protein, include their respective batch terms. For metabolites, batch cannot be included (confounded) — so metabolite results carry an explicit confound caveat.
- Produce a ranked statistic (moderated t / signed log-p) per feature per assay.
- Multiplicity: prespecify FDR control (Benjamini–Hochberg at a fixed level, e.g., 5%) — this is a *prespecified rule*, not a tuned parameter.

**7c. Enrichment (common coordinate system).**
- Run pathway/gene-set enrichment on each assay's ranked statistics (rank-based GSEA for RNA/protein; metabolite-set enrichment for metabolites). Map all three to shared pathway ontologies where possible.
- *Calibration of significance:* derive the enrichment null from the patient-level permutation (7, Controls), not only the analytic null, because n is small.

**7d. Integration — define the program.**
- **Primary (confirmatory-style) definition:** a pathway enters the candidate program if it is enriched in **both RNA and protein** with **consistent direction**. Because those assays have independent batch structure (Chain 3), concordance argues for biology. 
   - *Calibration of the concordance threshold:* estimate the null concordance rate by permutation; set the acceptance bar above that null (e.g., require observed concordance beyond the permutation 95th percentile). 
- **Secondary (hypothesis-generating) layer:** fit an unsupervised multi-omics latent-factor model (e.g., a factor model such as MOFA-type decomposition) on the jointly available deltas to find a shared axis; test whether any factor separates pre vs post. Use this to enrich/annotate the program, not to define it. 
   - *Why unsupervised, not supervised integration:* with n≈30, supervised multi-omics classifiers (e.g., sparse PLS/DIABLO) overfit easily; if used at all, assess them only by nested cross-validation and never let them set the frozen feature list without that honesty check.
   - *Calibration of factor number:* choose by cross-validated reconstruction error / factor stability across resamples, decided before interpretation.
- **Metabolite incorporation:** metabolite pathways may *annotate* or *support* the program but are flagged "confounded, needs cohort-2 confirmation." A metabolite pathway alone never defines the program.

**7e. Freeze.**
- Lock: the program feature list, each feature's expected direction, the pathway set, and a **single scoring function** (e.g., a direction-weighted per-sample score computable from any one assay or from the combined assays). Version-control and hash the frozen object. Record the prespecified primary endpoint and test for cohort 2.

**7f. External validation (cohort 2, M4).**
- Apply the frozen pipeline (same normalization recipe, same features) to cohort 2 **once**. 
- Primary test: does the program score change pre→post in the prespecified direction (paired test within cohort-2 patients)? Report effect size with confidence interval, not just a p-value. 
- Report concordance of per-pathway directions between cohorts.

### 8. Acceptance / stopping criteria (prespecify all)

- **Discovery gate:** proceed to integration only if per-assay QC passes and negative-control features show no pre/post shift.
- **Metabolomics gate:** if batch–timepoint collinearity is near-complete (step 1c), metabolomics is restricted to the supportive track; this is a documented stop, not a failure to hide.
- **Program existence:** a program is declared only if ≥1 pathway is RNA–protein concordant beyond the permutation null (7d).
- **Reproducibility (primary success):** program score changes in the prespecified direction in cohort 2 at the prespecified significance level, with a confidence interval excluding the null. 
- **Partial result:** if cohort 2 confirms direction but not significance (plausible given small validation n), report as "directionally consistent, underpowered," with the CI — do **not** re-tune and re-test.
- **Stop/declare negative:** if cohort-2 direction is inconsistent, declare the program non-reproducible; do not mine subgroups post hoc.

### 9. Troubleshooting

- **Batch and timepoint collinear in RNA or protein too.** Re-check the cross-table (step 1). If true, that assay also loses its artifact-control status and drops toward the supportive track; the program must then rest on whichever assay retains independent batch structure, with heavier reliance on cohort 2.
- **Very few paired complete cases after filtering (M3).** Switch from complete-case to mixed-models using all available pairs; report the effective n per feature. If still too sparse, reduce feature space to robustly detected analytes.
- **Enrichment driven by one or two outlier patients.** Leave-one-patient-out the enrichment and concordance results; keep only pathways stable to patient removal.
- **Score not computable in cohort 2 (missing features).** Prespecify a graceful-degradation rule (e.g., score from the subset of program features present, with a minimum-coverage requirement) — define this before unsealing cohort 2.
- **Negative controls shift pre→post.** Indicates residual technical drift/normalization failure; return to step 1 normalization calibration before any inference.

---

## Alternatives and why the chosen path is preferred

- **Supervised joint integration (predict timepoint from all omics at once).** Tempting and more "integrative," but at n≈30 it conflates discovery with model-fitting and overstates performance unless rigorously nested-cross-validated; it also lets the confounded metabolome leak into the classifier. Preferred use: only as a sensitivity analysis with honest cross-validation.
- **Feature-level intersection instead of pathway-level concordance.** Direct RNA↔protein feature matching is cleaner in principle but limited by incomplete gene–protein mapping and post-transcriptional discordance; pathway-level concordance (enrichment) is more robust and is what makes three heterogeneous platforms comparable.
- **Imputing missing assays / batch-correcting metabolomics anyway.** Rejected: imputation across the confounded batch structure can manufacture a "treatment" signal that is batch; batch correction of a fully nested factor removes the biology with it.
- **Using cohort 2 to pick thresholds, then reporting cohort-2 performance.** This is the most common and most damaging error; it destroys the only reproducibility estimate (M4).

---

## Limits and honest uncertainties

1. **Metabolomics is fundamentally limited here (M2).** No analysis can separate treatment from batch when they are nested; the best achievable is cross-platform consistency plus cohort-2 confirmation. Any metabolite claim is provisional.
2. **Power is modest (n≈30, M1), and missingness (M3) reduces effective n per feature.** The study is better powered to detect coordinated pathway-level programs than individual low-abundance analytes; report confidence intervals, not just significance.
3. **Cohort 2 is described only as "small" (M4).** It may be underpowered to confirm at conventional thresholds even for a real program; prespecify that a directionally consistent but non-significant result is reported transparently rather than re-mined.
4. **Observational pre/post (no untreated control arm).** Changes could reflect time, disease progression, or concomitant care rather than the treatment per se; the design identifies a *treatment-associated* program, not a proven *treatment-caused* one.
5. **Unreported parameters** (QC cutoffs, filtering fraction f, factor number, concordance threshold, FDR level, validation endpoint) are **not invented**; each is set by the calibration procedures above and frozen before unsealing cohort 2.

**What would change the recommendation:** (a) If audit of step 1 shows metabolomics batch is *not* fully confounded with timepoint (e.g., some post samples in other batches), metabolites could re-enter the primary program with batch as a covariate. (b) If RNA or protein also proves batch-confounded, the artifact-control logic weakens and cohort 2 becomes the dominant evidence. (c) A larger validation cohort would justify a stricter, significance-based acceptance criterion rather than an effect-size/CI emphasis.
