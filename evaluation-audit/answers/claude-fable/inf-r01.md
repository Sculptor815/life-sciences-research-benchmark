# Claude Fable 5 / inf-r01

Original final answer, shared by both scoring rounds.

# Recovering true expression changes under shrinkage: does a Normal prior on log fold changes systematically attenuate large, biologically decisive effects?

---

## 1. The unresolved biological question

**Question.** In RNA-seq experiments with few biological replicates (n = 2–5 per condition), do empirical-Bayes shrinkage estimators that place a **Normal prior on log2 fold changes (LFCs)** recover the true magnitude of *strong* expression changes (|LFC| ≥ 2) — the changes most often biologically decisive (master regulators, pathway switches, dose-dependent drug targets) — or do they systematically attenuate them, and can a prior whose tail behavior is *estimated from the data* restore those magnitudes without re-admitting the unstable extreme estimates that shrinkage exists to suppress?

**Why this is biologically relevant.** Downstream biology consumes effect *magnitudes*, not just significance calls: gene-set enrichment with LFC weighting, ranking of candidate targets, dose–response modeling, comparison of effect sizes across tissues or species. If the largest true effects are shrunk by 30–50%, prioritization and cross-study comparisons are distorted precisely for the genes that matter most. Conversely, if shrinkage is removed naïvely, low-count genes with 2–3 replicates produce maximum-likelihood LFC estimates of ±5 to ±10 that are pure noise. The biological question is therefore a bias–variance question with a biological payload: *what is the shape of the distribution of true effects across genes, and is the estimator's prior compatible with it?*

**What the supplied packet establishes, and what it does not.** The packet establishes (i) a negative-binomial / count-model framework for gene-level differences; (ii) the rationale for sharing information across genes to stabilize dispersion; (iii) a Normal prior on effects to stabilize fold changes. It explicitly does **not** supply evidence about the true underlying distribution of biological effects. That gap is exactly the scientific opening: the Normal prior is an *assumption about biology* (effects concentrated near zero with light tails), not a demonstrated fact.

---

## 2. Competing mechanisms and their distinct predictions

The "mechanism" here is the generative distribution of true per-gene effects, which determines the optimal shrinkage behavior.

**H1 — Light-tailed (Normal-like) effect distribution.** True LFCs across genes are approximately Gaussian: most near zero, large effects genuinely rare and not much larger than the bulk.
*Prediction:* Normal-prior shrinkage is close to Bayes-optimal. Estimated LFCs for high-count, well-replicated genes will match unshrunk estimates from a large-replicate "gold" experiment with near-zero bias at all effect sizes. Mean squared error (MSE) stratified by true-effect magnitude shows no bias inflation in the ≥2 LFC stratum.

**H2 — Heavy-tailed (spike-plus-tail) effect distribution.** Most genes are null or near-null, but a minority carry large effects drawn from a heavy-tailed component (plausible for strong perturbations: knockouts, differentiation, drug treatment of a direct target pathway).
*Prediction:* Normal-prior shrinkage over-shrinks the tail. Bias for true |LFC| ≥ 2 will be systematically toward zero, growing with |true LFC| and shrinking with counts/replicates; a comparison against gold-standard estimates shows a "flattening" in the upper tail of an estimated-vs-truth scatter (slope < 1 at the extremes). Sign errors remain rare, but magnitude recovery fails.

**H3 — Information-confounded tail.** Apparent heavy tails in raw estimates are an artifact of low-information genes (low counts, high dispersion); true effects are light-tailed and shrinkage is removing noise, not biology.
*Prediction:* The apparent over-shrinkage under H2-style diagnostics disappears once genes are stratified by information content (e.g., mean normalized count, estimated dispersion). In high-information strata, Normal shrinkage shows no tail bias; "lost" large effects are concentrated in low-information strata and are not confirmed by independent validation (qPCR, held-out replicates).

These three hypotheses make **distinct, falsifiable predictions** about (a) tail bias in high- vs low-information strata and (b) whether an adaptively heavy-tailed prior improves or degrades accuracy.

---

## 3. Proposed method

**Core estimator (proposed, not yet run).** Retain the packet's count model (negative binomial GLM with moderated, information-shared dispersion) and replace the fixed Normal prior on LFCs with a **scale-mixture-of-Normals prior whose tail weight is estimated from the data** by empirical Bayes:

- Prior family: βg ~ Normal(0, σ² · λg), with λg ~ Inverse-Gamma(ν/2, ν/2), i.e., marginally a scaled Student-t with ν degrees of freedom. ν → ∞ recovers the Normal prior (H1); small ν gives heavy tails (H2).
- Hyperparameters (σ, ν) estimated by maximizing the marginal likelihood across all genes (empirical Bayes), using the per-gene likelihoods from the NB model. This lets the data itself choose between light and heavy tails, operationalizing the packet's acknowledged gap.
- Report posterior mode (MAP) per gene plus a posterior-SD-based uncertainty, so downstream users can distinguish a large-but-uncertain estimate from a large-and-precise one.

**Rationale chain (evidence → inference → conclusion):**
Evidence (packet): few replicates ⇒ unstable MLE LFCs; sharing information + Normal prior stabilizes them.
Inference: stabilization is a bias–variance trade; a Normal prior's bias is proportional to the true effect, so it is maximal exactly for the strongest effects; the packet supplies no evidence that true effects are Normal.
Conclusion: a prior family that *nests* the Normal and lets tail weight be a fitted parameter cannot be worse in principle and will be better exactly when H2 holds — a claim we then test, not assume.

**Explicit assumptions (labeled):**
- A1: NB adequately models count overdispersion (inherited from the packet's framework).
- A2: True effects are exchangeable across genes within an experiment for purposes of prior estimation (standard empirical-Bayes assumption; violated under strong effect–expression-level dependence — addressed in diagnostics below).
- A3: Gold-standard large-replicate estimates are close enough to truth to serve as reference (checked by subsampling stability analysis, §5).

---

## 4. Full evaluation protocol (proposed)

### 4.1 Dataset eligibility and raw-read provenance

**Eligibility criteria (prespecified before any estimation):**
1. Bulk RNA-seq, two-condition comparison, with **≥ 8 biological replicates per condition** available, so that gold-standard estimates can be computed on the full set and small-n behavior evaluated by subsampling (n = 2, 3, 5 per group).
2. Raw reads (FASTQ) publicly deposited with documented library prep, organism, and reference genome version, so the entire pipeline from reads is reproducible; no reliance on author-supplied count matrices (eliminates hidden preprocessing differences).
3. At least one eligible dataset with an expected **strong perturbation** (e.g., gene knockout, strong drug treatment) and one with an expected **subtle perturbation** (e.g., mild stimulus), so both tail regimes are represented. (The packet does not name datasets; selection is by these criteria. I am not asserting any specific dataset's properties as established.)
4. Independent validation data available for a subset of genes (e.g., qPCR on the same samples, or an orthogonal platform) **or** fully held-out replicates never used in estimation.

**Provenance controls:** record accession IDs, read lengths, strandedness, batch annotations; uniform processing (one aligner/quantifier, one genome build, one annotation release, fixed software versions, containerized); per-sample QC (mapping rate, rRNA fraction, 3′ bias) with prespecified exclusion thresholds applied *before* unblinding any differential results.

### 4.2 Estimation arms

On each small-n subsample, fit three estimators on identical counts, dispersions, and size factors:
- **M0:** unshrunk MLE LFC (NB GLM).
- **M1:** Normal-prior shrinkage (the packet's method).
- **M2:** adaptive scale-mixture prior (proposed method).
All arms share the dispersion-moderation machinery so differences isolate the *effect prior*.

### 4.3 Simulation study (truth known by construction)

- Simulate NB counts with dispersions and mean–dispersion trend estimated from the real eligible datasets (parametric bootstrap anchored to real data, so the simulation is not self-serving).
- Three truth scenarios matching H1/H2/H3: (S1) Normal LFCs; (S2) 90% null + 10% heavy-tailed (t3-distributed, scaled so ~2% of genes have |LFC| ≥ 2); (S3) light-tailed truth but with effect magnitude anti-correlated with expression level, to mimic the information-confounding of H3.
- n per group ∈ {2, 3, 5, 8}; ≥ 50 simulation replicates per cell; seeds logged.
- Also a **model-misspecification arm**: simulate from a zero-inflated / gamma-mixture count model to test robustness beyond NB (A1).

### 4.4 Real-data split-sample validation

- From each ≥8-per-group dataset: repeatedly draw disjoint small subsets (n = 3) for estimation; compute the **gold standard** as the MLE on all remaining replicates (≥ 5 per group), restricted to genes with gold-standard mean count ≥ 20 and gold-standard SE below a prespecified threshold (so the reference itself is stable — see §5).
- Metrics per arm: MSE and bias of estimated vs gold LFC, stratified by (i) gold |LFC| bins (0–0.5, 0.5–1, 1–2, ≥2) and (ii) information strata (mean count tertiles × dispersion tertiles) — this stratification is what separates H2 from H3.
- Concordance-at-top (CAT) curves: overlap of top-k genes ranked by |LFC| between small-n arm and gold standard, k = 50…1000.
- Sign error rate among genes the arm reports with |LFC| ≥ 1.

### 4.5 Independent validation

- qPCR (or orthogonal-platform) measurements on 30–60 genes chosen to span LFC and count strata, selected *blind* to which estimator favors them, including: genes where M1 and M2 disagree by > 0.5 LFC, genes with extreme M0 estimates that both shrinkage arms suppress, and concordant controls. Agreement measured by regression slope and RMSE of sequencing LFC vs qPCR ΔΔCt-derived LFC.
- Where qPCR on the exact samples is infeasible, fully held-out sequencing replicates (never touched during estimation or prior fitting) serve as the independent axis; this is weaker (same platform) and will be labeled as such in interpretation.

### 4.6 Figure generation (prespecified)

F1: Estimated-vs-truth scatter (simulation) per arm with loess fit; H2 predicts M1's loess slope < 1 in the tails, M2's ≈ 1.
F2: Bias and RMSE by true-effect stratum × information stratum × n (small multiples) — the central figure separating H1/H2/H3.
F3: Real-data small-n vs gold MA-style plots with disagreement genes highlighted.
F4: CAT curves per arm and n.
F5: qPCR validation scatter with per-arm regression lines.
F6: Stability figure (next section): distribution of per-gene estimate spread across resampled small-n subsets, by arm.
F7: Fitted prior shapes (ν̂, σ̂) per dataset with bootstrap intervals — a direct empirical readout on the packet's open question about the effect distribution.

### 4.7 Statistical pre-specification

Primary endpoint: RMSE in the (|LFC| ≥ 2, mid/high-information) stratum, M2 vs M1, real-data split-sample design, with bootstrap CIs over subsample draws. Secondary: tail bias, CAT at k = 200, qPCR slope. Analysis plan frozen before validation data are examined.

---

## 5. Testing preservation of strong effects without accepting unstable low-information extremes

This is the crux: a heavy-tailed prior could "win" on tail bias merely by under-shrinking noise. Two guards:

**Guard 1 — Information-stratified tail accuracy.** The claim "M2 preserves strong effects" is only credited if the improvement appears in **mid/high-information strata** (mean count above the lower tertile) *and* is confirmed on independent validation genes. Improvement confined to the low-count stratum, unconfirmed by qPCR/held-out data, is classified as noise re-admission, not effect preservation — i.e., evidence for H3 over H2.

**Guard 2 — Stability criterion.** For each gene, compute the standard deviation of its estimated LFC across repeated disjoint small-n subsamples ("resampling spread"). Define instability as spread above a prespecified quantile (e.g., the 90th percentile of M1's spread distribution, since M1 is the stability benchmark). A prespecified **composite acceptance rule**: M2 is judged superior only if it (a) reduces tail RMSE/bias in informative strata by the primary-endpoint margin **and** (b) does not increase the fraction of unstable extreme calls (|LFC| ≥ 2 with spread above threshold) beyond M1's fraction plus a small tolerance (e.g., +20% relative, prespecified). This makes "preserves strong effects" and "doesn't chase unstable extremes" jointly falsifiable rather than traded off silently.

**Guard on the gold standard itself (A3):** gold-standard genes failing their own SE threshold are excluded from truth-based metrics, so "strong effects" are defined only where the reference is reliable.

---

## 6. Conditional interpretation (none of these results are observed; all are forecasts of what each outcome would mean)

**Positive outcome (supports H2 and the method):** In simulation S2 and real split-sample data, M2 reduces tail bias/RMSE in informative strata, passes the stability guard, qPCR slopes move closer to 1 for M2 than M1, and fitted ν̂ is small with tight bootstrap intervals. Conclusion: true effect distributions in strong-perturbation experiments are heavy-tailed; Normal-prior shrinkage attenuates biologically decisive changes; adaptive-tail shrinkage is the recommended default. Figures F1/F2/F5/F7 carry the inference.

**Negative outcome (supports H1 or H3):** M2 shows no informative-stratum improvement (H1: ν̂ large, M1 ≈ M2 everywhere) or improves only in low-information strata while failing qPCR confirmation and/or the stability guard (H3). Conclusion: the Normal prior's attenuation is either negligible or is correctly removing noise; recommend retaining M1 and report F2/F6 as the decisive evidence. This outcome would falsify the methods forecast below — the plan is designed so it can lose.

**Ambiguous outcome:** results split across datasets (e.g., heavy tails in the knockout dataset, light tails in the mild stimulus) or ν̂ is unstable across bootstrap draws. Conclusion: tail behavior is experiment-dependent; recommend the adaptive prior precisely *because* it nests both regimes, but flag that per-dataset ν̂ uncertainty must be propagated; next step is expanding eligible datasets across perturbation strengths rather than declaring a universal winner. Also ambiguous: simulation and real-data results disagree — then suspect A1 (NB misspecification) via the misspecification arm, and prioritize model-form diagnostics before prior-form conclusions.

---

## 7. Methods-direction forecast vs reproduction of published results — explicit distinction

- **Forecast (made here):** Based solely on the packet's logic — Normal shrinkage bias scales with true effect size, and the packet concedes no evidence about the true effect distribution — I forecast that in strong-perturbation datasets the adaptive heavy-tailed prior (M2) will reduce tail bias while satisfying the stability guard (H2 outcome). This is a *directional prediction about methodology*, falsifiable by the protocol above.
- **Not a reproduction:** I am **not** claiming to have reproduced any published biological result, any published benchmark of shrinkage estimators, or any specific dataset's differential-expression findings. No estimates, metrics, ν̂ values, or validation results exist yet; every number referenced above is a design parameter or a prespecified threshold, not an observation. If the study is run and matches the forecast, that still would not constitute reproducing prior literature — it would be new evidence generated under this protocol.

---

## 8. Alternatives and limits

- **Alternative estimators:** permutation-calibrated LFC thresholds, nonparametric empirical-Bayes (deconvolution of the effect distribution), or hierarchical fully-Bayesian models. The scale-mixture EB approach was chosen because it minimally extends the packet's framework (same likelihood, same dispersion sharing) so differences are attributable to the prior; a deconvolution arm could be added as a secondary comparator.
- **Limits:** (i) Gold standards from 5–8 replicates are imperfect truth; residual reference error biases all arms similarly but caps detectable differences. (ii) Exchangeability (A2) may fail if effect size depends on expression level; F2's stratification detects but does not fully fix this — a count-dependent prior scale is a labeled extension. (iii) qPCR validates dozens, not thousands, of genes; generalization relies on the stratified sampling design. (iv) Results from bulk two-group designs may not transfer to single-cell or multi-factor models. (v) **Unreported parameters** (labeled): exact loess spans, bootstrap counts, qPCR primer efficiencies, and the stability-threshold quantile are implementation choices to be frozen in the analysis plan before unblinding; they are stated as placeholders, not evidence-backed values.
