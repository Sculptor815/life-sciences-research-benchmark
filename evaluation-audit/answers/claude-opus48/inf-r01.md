# Claude Opus 4.8 / inf-r01

Original final answer, shared by both scoring rounds.

# Recovering Real Expression Changes from Noisy RNA-seq: A Shrinkage Evaluation Plan

## Bottom line up front

**Recommended action:** Evaluate whether empirical-Bayes shrinkage of log fold-changes (LFCs), as described in the evidence packet, improves recovery of true differential expression without distorting genuinely strong effects. Do this by (1) estimating effects on real data with few replicates, (2) running a simulation whose ground truth is known, (3) validating ranking stability against an independent held-out split or orthogonal measurement, and (4) generating diagnostic figures (MA plots, calibration curves, rank-concordance plots) that directly test the "preserve strong, shrink weak" claim.

**Critical framing:** This is a **methods-direction forecast** — a test of whether the shrinkage estimator behaves as its rationale predicts (stabilizing low-information estimates while leaving high-information estimates nearly untouched). It is **not** a reproduction of any specific published biological finding. The evidence packet supplies a rationale for shrinkage but explicitly does **not** characterize the true distribution of biological effects, so any conclusion is conditional on the assumed effect distributions I simulate. I flag this boundary throughout.

---

## 1. The unresolved biological question

**Question:** When only a few biological replicates are available, can we recover the true set and magnitude of differentially expressed genes from noisy counts — and specifically, can information-sharing shrinkage recover *real* changes without either (a) inventing stable-looking estimates for genes with almost no information, or (b) erasing genuinely large, well-supported effects?

This matters biologically because the genes with the most extreme raw fold-changes in small experiments are frequently low-count genes whose apparent effects are statistical artifacts. If a downstream researcher ranks candidates by raw LFC, they will chase noise. Conversely, an overly aggressive estimator could shrink a real, large regulatory change (e.g., a transcription factor induced 8-fold) toward zero, causing a false negative on exactly the biology of interest.

The tension is between **stability** (don't trust low-information extremes) and **fidelity** (don't destroy strong, well-supported effects). The packet's method — sharing dispersion information across genes and placing a Normal prior on effects — is a specific proposal to resolve that tension. The question is whether it actually does.

---

## 2. Competing mechanisms and their distinct predictions

I frame three competing "mechanisms" (estimator behaviors) with falsifiably different predictions.

**Mechanism A — Shrinkage is adaptive (the packet's hypothesis).**
Information-sharing stabilizes dispersion; the Normal prior pulls low-information LFCs toward zero but leaves high-information (high-count, low-variance) LFCs nearly unchanged.
- *Prediction A1:* Shrinkage magnitude scales inversely with per-gene information (count depth, replicate consistency).
- *Prediction A2:* For high-count genes with large true effects, shrunken LFC ≈ raw LFC (within tolerance).
- *Prediction A3:* Ranking and classification of true DE genes improves (higher precision at fixed recall; better AUC/AUPRC) relative to raw LFC ranking.
- *Prediction A4:* Rank stability across independent subsamples improves.

**Mechanism B — Shrinkage is uniform/over-aggressive.**
The prior pulls all effects toward zero by a similar factor regardless of information.
- *Prediction B1:* Large true effects are systematically underestimated even at high counts.
- *Prediction B2:* Sensitivity to genuinely strong DE genes drops versus an unshrunk MLE.

**Mechanism C — Shrinkage adds no value (null for the method).**
With the chosen data/simulation, raw and shrunken estimators perform equivalently.
- *Prediction C1:* No improvement in AUPRC, calibration, or rank stability.

These predictions are mutually distinguishing: A and B diverge on high-count large-effect genes (A2 vs B1); A and C diverge on low-count genes and ranking stability (A3/A4 vs C1). The evaluation is designed so each figure discriminates among them.

---

## 3. Evidence-to-inference-to-conclusion chain

**Evidence (packet):** A count-based model estimates gene-level differences; few replicates yield unstable fold-changes at low/variable counts; a method stabilizes estimates by sharing dispersion across genes and applying a Normal prior to effects. The packet does not specify the true effect distribution.

**Inference:** If the stabilization is information-weighted (Mechanism A), then an estimator comparison on data with *known* ground truth should show improved recovery concentrated where information is scarce, with preservation where information is abundant. Because the packet does not supply the true effect distribution, ground truth must come from **simulation** (where I set it) and from **operational proxies** on real data (independent-split concordance, orthogonal assay). The real-data analysis cannot by itself confirm "truth" — it can only demonstrate stability behavior and plausibility.

**Conclusion structure:** The combination of simulation (controlled truth) + independent validation (external/held-out anchor) + diagnostic figures lets me accept A, accept B, or fall to C, with explicit conditional criteria (Section 9). No single arm is sufficient; the simulation defines truth but is model-dependent, and the real-data arm grounds the simulation's realism.

---

## 4. Step 1 — Dataset eligibility and raw-read provenance

**Eligibility criteria (pre-registered before looking at results):**

1. **Design:** A two-group comparison (treatment vs control) with a small number of biological replicates per group (target 2–4), matching the packet's "few replicates" regime. At least one dataset with 2–3 replicates/group to stress the estimator, and ideally one with ≥5 replicates/group to serve as a "truth-approximating" reference for the real-data validation (see Step 5).
2. **Assay:** Bulk RNA-seq, poly-A or total-RNA, standard Illumina short reads; single modality to avoid confounding the estimator comparison.
3. **Provenance:** Raw reads (FASTQ) must be retrievable from a public archive (e.g., SRA/ENA/GEO) with accession numbers, library layout (single/paired-end), strandedness, and sample-to-condition mapping documented. Reject datasets lacking per-sample metadata or with pooled/ambiguous replicate structure.
4. **Quality gate:** Samples passing standard QC (per-base quality, adapter contamination, rRNA fraction within expected range, mapping rate above a pre-set threshold, e.g., ≥70% uniquely mapped). Samples failing QC are excluded and the exclusion logged.
5. **Exclusion of confounds:** No known severe batch confounding with condition (if batch is perfectly confounded with treatment, reject — effects are unidentifiable). Record batch where available for inclusion as a covariate.

**Raw-read handling (documented, reproducible):**
- Record accessions, checksums (md5) of downloaded FASTQ, tool versions.
- Adapter/quality trimming with fixed parameters (logged).
- Quantification to gene-level counts via a documented pipeline (alignment-based or pseudo-alignment); the *same* pipeline for all samples and both estimators. The estimator comparison must not confound with quantification differences.
- Output: a gene × sample count matrix plus a sample table (condition, batch, library metadata).

*Assumption flagged:* I assume a reference annotation version; I will fix and record it. Different annotations change gene boundaries and counts; this is a reproducibility parameter, not a biological result.

---

## 5. Step 2 — Estimation on real data

On each eligible dataset:

1. **Filter** genes with near-zero counts across all samples using a pre-set low-count filter (e.g., minimum count sum or minimum samples above a threshold). Record the filter; it affects multiple-testing and the low-information tail.
2. **Fit the count model** with dispersion shared across genes (the packet's dispersion stabilization) and estimate per-gene LFCs two ways:
   - **Unshrunk (MLE) LFC** — the baseline.
   - **Shrunken LFC** — Normal prior on effects, per the packet.
3. **Record for each gene:** mean normalized count (information proxy), unshrunk LFC and its standard error, shrunken LFC, dispersion estimate, test statistic / p-value, and multiple-testing-adjusted value.

**Key measured quantity:** the *shrinkage map* — shrunken LFC as a function of (unshrunk LFC, mean count, SE). This directly tests Prediction A1 (shrinkage inversely scales with information).

---

## 6. Step 3 — Simulation with known ground truth

Because the packet does not supply the true effect distribution, simulation is the only arm with exact truth. I will simulate under **multiple effect distributions** to avoid assuming the answer, and I will state each as an assumption.

**Simulation construction:**

1. **Anchor on real data:** Estimate per-gene mean expression and dispersion from a real eligible dataset to make simulated counts realistic (empirical mean–dispersion relationship preserved).
2. **Assign true LFCs** to a defined fraction of genes under several scenarios:
   - *Scenario 1 (sparse, mixed magnitudes):* most genes null; DE genes drawn from a distribution spanning small, moderate, and large effects — including a designated set of **strong effects at high counts** (to test preservation, Prediction A2/B1) and **large nominal effects at low counts** (to test suppression of unstable extremes).
   - *Scenario 2 (many small effects):* a broad set of genes with modest true LFCs — stresses whether shrinkage erases distributed real signal (favors B if it does).
   - *Scenario 3 (heavy-tailed effects):* a few very large effects plus null background — stresses preservation.
   - *Scenario 4 (true null):* no DE genes — tests false-positive control / that shrinkage doesn't manufacture effects.
3. **Replicate structure:** simulate at the small replicate counts of interest (e.g., 2v2, 3v3) and, as a reference, a larger count (e.g., 10v10) to confirm estimators converge when information is abundant.
4. **Replicates of the simulation:** many independent simulated datasets per scenario to quantify variance of each metric (enables error bars and significance of estimator differences).

**What simulation tests:**
- Recovery of true DE set: ROC/AUC, precision–recall/AUPRC for shrunken vs unshrunk ranking.
- Magnitude fidelity: estimated vs true LFC, stratified by count and true effect size — the core test of "preserve strong, shrink weak."
- False-positive control under Scenario 4.

*Assumption flagged:* Simulated effect distributions are my choices, not facts about biology. Conclusions about ranking/recovery are conditional on these distributions. I will report sensitivity across Scenarios 1–4 so a reader sees how robust the behavior is to the unknown true distribution — directly addressing the packet's stated gap.

---

## 7. Step 4 — Independent validation

Simulation realism is never guaranteed. Two independent anchors ground the real-data behavior:

**(a) Held-out split / subsampling concordance (internal independence).**
If a dataset has enough replicates, split samples into disjoint small-replicate subsets. Estimate LFCs (shrunk and unshrunk) independently on each subset. Compute rank concordance (e.g., Spearman correlation, top-K overlap) between subsets. Prediction A4: shrinkage improves cross-subset reproducibility of gene rankings, especially among low/moderate-count genes. This uses *no external truth* but tests stability operationally.

**(b) Larger-replicate reference as a truth proxy.**
Where a higher-replicate dataset exists, treat its high-power DE calls as an approximate gold standard, then subsample to few replicates and ask which estimator better recovers the high-power calls. This is a proxy, not absolute truth (the reference itself has error), so I treat it as corroborating, not definitive.

**(c) Orthogonal measurement (if available).** If the dataset provides matched qPCR, protein, or an independent platform for a subset of genes, use it as an external anchor for direction and relative magnitude on those genes. Flagged as *conditional on availability*; not assumed present.

*Independence principle:* The validation data/split must not have been used to tune the estimator or choose the filter. Pre-register thresholds before computing validation metrics.

---

## 8. Step 5 — Figure generation (each figure tests a specific prediction)

1. **MA plot with shrinkage overlay (real + simulated).** LFC vs mean count, raw vs shrunken. *Tests A1:* low-count extremes should collapse toward zero; high-count effects should barely move. Visual separation of mechanisms A vs B.
2. **Shrinkage-vs-information curve.** Magnitude of shrinkage (|raw − shrunk|) vs mean count and vs SE. *Tests A1 quantitatively.* A: monotone decreasing with information. B: roughly flat.
3. **Estimated-vs-true LFC scatter, stratified (simulation).** Faceted by count bin and true-effect bin. *Core preservation test (A2 vs B1).* On the high-count/large-true-effect facet: A predicts points near the identity line; B predicts systematic downward bias.
4. **Precision–recall and ROC curves (simulation).** Shrunken vs unshrunk ranking across scenarios. *Tests A3 vs C1.*
5. **Calibration curve (simulation).** Binned estimated effect vs observed true effect. *Tests over-shrinkage (B) vs faithful (A).*
6. **Cross-subset rank-concordance plot (real).** Top-K overlap and Spearman vs K, shrunk vs unshrunk. *Tests A4.*
7. **False-positive plot (Scenario 4).** Number of called DE genes under true null, both estimators. *Guards against the estimator manufacturing stable-looking effects.*
8. **Convergence panel (simulation, 2v2 → 10v10).** Difference between estimators shrinks as replicates grow. *Confirms the estimator is information-driven, not a fixed bias.*

Every figure will carry error bars/intervals from simulation replicates or subsampling, and the exact parameters (filter, prior, replicate counts, scenario) in captions.

---

## 9. Conditional conclusions (stated as conditions, not observations)

I have **not** run these analyses; below are the decision rules.

**Positive conclusion (supports Mechanism A / the packet's rationale) — would be warranted if:**
- Figure 2 shows shrinkage monotonically decreasing with information (A1); AND
- Figure 3's high-count/large-effect facet shows shrunken ≈ true (near identity, within a pre-set tolerance), demonstrating **preservation of strong effects** (A2); AND
- Figures 4–5 show improved AUPRC and calibration for shrunken ranking across at least Scenarios 1 and 3 (A3); AND
- Figure 6 shows improved cross-subset rank concordance (A4); AND
- Figure 7 shows no inflation of DE calls under the true null.
*Interpretation:* The method recovers real changes and stabilizes low-information estimates without sacrificing strong effects — a **methods-direction** success, conditional on the simulated effect distributions.

**Negative conclusion (supports Mechanism B, over-shrinkage) — would be warranted if:**
- Figure 3 shows systematic underestimation of large true effects even at high counts (B1); AND/OR
- Figure 4 shows reduced sensitivity to strong DE genes versus unshrunk MLE (B2); AND
- Calibration (Fig 5) shows global compression.
*Interpretation:* Shrinkage buys stability at the cost of fidelity to real strong effects; recommend reporting unshrunk LFCs for high-information genes or using the shrinkage only for ranking low-information genes.

**Null conclusion (Mechanism C) — would be warranted if:**
- Figures 4–6 show no meaningful difference between estimators across scenarios and no stability gain.
*Interpretation:* In this regime/data, shrinkage neither helps nor harms; the packet's rationale is not demonstrable here (possibly because counts are high enough that MLE is already stable — check against Fig 8 convergence).

**Ambiguous conclusion — would be warranted if:**
- Results split by scenario (e.g., A holds under heavy-tailed Scenario 3 but B appears under many-small-effects Scenario 2); OR
- Simulation supports A but real-data concordance (Fig 6) shows no stability gain, implying the simulation's effect distribution is unrepresentative; OR
- Validation anchors (Step 4) disagree with simulation.
*Interpretation:* The method's value depends on the (unknown) true effect distribution — exactly the gap the packet flagged. Report the dependence explicitly; do not issue a blanket recommendation.

---

## 10. How I test "preserve strong without accepting unstable extremes"

This requirement maps to two specific, falsifiable checks that must *both* pass:

- **Preservation of strong effects:** Figure 3, high-count/large-true-effect facet — shrunken LFC must lie near the identity line within a pre-registered tolerance. Failure here = Mechanism B.
- **Rejection of unstable extremes:** Figure 2 + Figure 7 — low-count nominal extremes must shrink toward zero, and the true-null simulation must not produce stable-looking false positives. Failure here (extremes retained) = raw MLE behavior, no stabilization.

Passing one but not the other is explicitly an *ambiguous/negative* outcome, not a success. This prevents declaring victory on stability while quietly losing real biology, or vice versa.

---

## 11. Methods-direction forecast vs reproduction of biological results

**What this plan can establish:** whether the shrinkage estimator *behaves* as its rationale predicts (information-adaptive stabilization) on realistic data and controlled simulation — a forecast about method behavior.

**What it cannot establish:** that any particular gene is truly differentially expressed in the underlying biology, or that a specific published DE list is reproduced. Simulation truth is self-defined; real-data validation uses proxies (held-out splits, higher-replicate references, orthogonal assays) that have their own error. I will state in every conclusion that DE "truth" in the simulation is an assumption and that real-data recovery is corroborative, not confirmatory.

I will **not** present simulated recovery metrics as if they were measured biological effects, and I will not claim to have reproduced prior biological findings unless an orthogonal assay independently confirms specific genes — and even then only for those genes.

---

## 12. Limits, alternatives, and what would change the recommendation

**Limits:**
- The dominant limitation is the **unknown true effect distribution** (packet-stated gap). All ranking/recovery conclusions are conditional on Scenarios 1–4; a real effect distribution unlike all four would invalidate extrapolation. Mitigated by scenario sensitivity analysis, not eliminated.
- Simulation inherits the real data's mean–dispersion structure but may miss real sources of variability (batch, outliers, zero-inflation); if so, both estimators' absolute numbers are optimistic, though their *relative* comparison is more robust.
- The Normal prior is a modeling choice; if true effects are heavy-tailed, a Normal prior could over-shrink the tail (links to Mechanism B under Scenario 3) — Figure 3 Scenario 3 is the specific test.
- Low-count filtering, annotation version, and quantification pipeline are free parameters that affect the low-information tail where shrinkage matters most. All pre-registered and logged.

**Alternatives if the plan fails to discriminate:**
- Add a heavier-tailed prior comparison (if permitted by the method) to see whether over-shrinkage in Scenario 3 is prior-specific.
- Use a t-statistic/ranking-only evaluation if magnitude calibration is the sole failure point.
- Increase simulation replicates / add scenarios interpolating between 1–4.

**What would change the recommendation:**
- If convergence panel (Fig 8) shows MLE already stable at the available replicate counts, shrinkage is unnecessary — recommend against added complexity.
- If orthogonal data become available and contradict simulation-based conclusions, defer to orthogonal data for the affected genes.
- If batch confounding is discovered post hoc, the dataset is disqualified and conclusions withdrawn for it.

---

## 13. Summary chain

Packet rationale (shrinkage stabilizes via shared dispersion + Normal prior, true effect distribution unknown) → estimate on eligible, provenance-documented small-replicate real data (unshrunk vs shrunk) → simulate known truth under multiple effect distributions to supply ground truth the packet lacks → validate stability with independent splits/higher-replicate reference/orthogonal data → generate targeted figures that separately test information-adaptive shrinkage (Fig 2), strong-effect preservation (Fig 3), recovery/calibration (Figs 4–5), reproducibility (Fig 6), and false-positive control (Fig 7) → apply pre-registered positive/negative/null/ambiguous rules → report as a methods-direction forecast conditional on assumed effect distributions, explicitly not a reproduction of published biological results.
