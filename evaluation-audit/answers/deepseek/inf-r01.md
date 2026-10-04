# DeepSeek V4.1 Flash / inf-r01

Original final answer, shared by both scoring rounds.

**Recommended next action:** Treat the supplied Normal-prior shrinkage method as a candidate estimator, not as a validated biological discovery tool. Pre-register a methods-direction evaluation that (i) defines eligible RNA-seq datasets, (ii) reproduces the count-model/dispersion-sharing/Normal-prior pipeline as the starting point, (iii) simulates true effects across Normal, heavy-tailed and sparse-mixture distributions, (iv) validates on held-out or independent data, (v) reports calibration and preservation of strong effects, and (vi) rejects unstable low-information extremes. This is a **methods-direction forecast**, not a reproduction of any published biological result. No proposed result below has been observed.

---

## 1. Unresolved biological question and competing mechanisms

**Question.** For a two-condition or multi-condition RNA-seq contrast with few biological replicates, which genes show real condition-associated expression changes, and does a count-model analysis that shares dispersion information across genes and applies a Normal prior to effect sizes recover those real changes without inflating unstable low-information extremes?

The biological relevance is that low- or variably expressed genes can be genuine regulators, but their fold changes are easily driven by one or two reads in one replicate. The practical question is not simply “which genes have large observed fold changes?” but “which observed changes are reproducible biological effects rather than noise?”

**Competing mechanisms and distinct predictions**

- **H1: Approximate-Normal effects.** True gene-level effects are roughly symmetrically distributed around zero with moderate tails; the Normal prior is a reasonable approximation.  
  **Prediction:** Strong high-information effects are preserved; low-count large observed fold changes are shrunk; posterior probabilities are well calibrated; held-out validation agrees for high-information genes.

- **H2: Heavy-tailed or sparse-mixture effects.** True effects are mostly near zero but include a subset of large, biologically important changes, possibly enriched in low-count genes. A single Normal prior over-shrinks the large true effects and under-regularizes moderate noise.  
  **Prediction:** Sensitivity for true strong effects falls, especially when counts are low; bias of large effects is toward zero; heavy-tailed simulations show worse recall than an unshrunk or heavier-tailed comparator; validation reveals false negatives.

- **H3: Dispersion misspecification.** Sharing dispersion across genes stabilizes estimates but distorts gene-specific overdispersion, so ranking is driven by the shared trend rather than by the gene’s own variance.  
  **Prediction:** Residual overdispersion remains in validation; genes with atypical dispersion are misranked; calibration is poor in dispersion-stratified bins.

These are distinguishable by simulation under known truth and by held-out validation. If H1 holds, shrinkage improves stability without sacrificing strong true effects. If H2 or H3 holds, the Normal-prior starting point must be modified or its conclusions limited.

---

## 2. Evidence-to-inference-to-conclusion chain

**Evidence supplied by the packet**
1. An RNA-seq analysis estimates gene-level expression differences using a count model.
2. With few biological replicates, low or variable counts can yield unstable fold-change estimates.
3. A method stabilizes dispersion and fold-change estimates by sharing information across genes and using a Normal prior on effects.
4. The packet establishes the rationale for shrinkage but does not supply evidence about every possible underlying distribution of biological effects.

**Inferences**
- Sharing information can reduce variance when genes are exchangeable in their dispersion and effects.
- A Normal prior is a strong shape assumption. If true effects are heavy-tailed, sparse or asymmetric, shrinkage can bias the largest real effects and distort rankings.
- Because the packet lacks evidence on the true effect distribution, the method’s biological validity cannot be assumed; it must be tested under multiple plausible truths.
- The evaluation must separate “strong effect” from “low-information extreme.” A large fold change in a gene with very low counts and wide uncertainty is not equivalent to a large fold change supported by many reads and consistent replicates.

**Conclusion**
Use the supplied count-model/dispersion-sharing/Normal-prior method as the starting estimator. Pre-register simulations across effect distributions plus independent validation. Accept the method only if it preserves strong, well-supported effects and calibrates low-information extremes toward the null or toward explicit uncertainty. Otherwise, report low-count large fold changes as unresolved and consider a heavier-tailed or mixture prior as an alternative.

**Forecast versus reproduction.** This is a forecast about methodological direction: it predicts what should happen under stated assumptions. An actual reproduction would require applying a specific published method to a named dataset and comparing its called genes with that study’s reported biological results. The packet does not contain such a dataset or published result set, so no biological reproduction is claimed.

---

## 3. Dataset eligibility and raw-read provenance

**Eligibility criteria**
- Gene-level RNA-seq count matrix with two or more conditions, including the primary contrast of interest.
- Biological replicates, not technical replicates alone. “Few” should be pre-specified, e.g., n = 2–5 per group, with sensitivity analyses at n = 3, 5, 10.
- Sample metadata: condition, batch, pairing, library size, RNA extraction, library prep, species, annotation version.
- No perfect confounding between condition and batch.
- Counts are raw or minimally filtered, not already transformed or batch-corrected in a way that hides uncertainty.

**Exclusion criteria**
- No biological replication.
- Condition confounded with batch or processing date.
- Pre-normalized or pre-shrunk effect estimates supplied instead of counts.
- Failed QC, severe 3′ bias, or unknown library strandedness if required by the quantification pipeline.
- No usable provenance for raw reads or count generation.

**Raw-read provenance fields**
If FASTQ files are available, record: repository accession, sample accession, checksum, read length, single/paired-end, adapter content, quality trimming, aligner or transcriptome quantifier, reference genome/transcriptome build, gene annotation version, and counting rule. If only counts are available, record the quantification pipeline and state that a full raw-read audit cannot be performed.

**Contrast definition**
Pre-specify the tested coefficient, e.g., condition B versus A, adjusted for batch if eligible. Do not choose the contrast after seeing the shrinkage results.

**Unreported parameters that must be supplied**
Number of replicates, read depth, dispersion trend, true effect distribution, validation dataset, and biological system. Without these, the plan is conditional.

---

## 4. Estimation method using the supplied starting point

**Count model**
For gene \(g\), sample \(j\), condition \(i\):
\[
Y_{gj} \sim \text{Negative Binomial}(\mu_{gj}, \alpha_g)
\]
\[
\log \mu_{gj} = \log(s_j) + \log(\beta_{g0}) + x_i \beta_{g1}
\]
where \(s_j\) is a library-size offset, \(\alpha_g\) is gene-wise dispersion, and \(\beta_{g1}\) is the condition effect on the log scale.

**Dispersion sharing**
Estimate a mean-dispersion trend across genes and shrink each \(\alpha_g\) toward that trend. This is the packet’s “sharing information across genes” step. Record the amount of shrinkage and the dispersion trend.

**Normal prior on effects**
Place a Normal prior on the condition effect:
\[
\beta_{g1} \sim N(0, \tau^2)
\]
Estimate \(\tau^2\) by empirical Bayes or hierarchical Bayes. The posterior mean is a weighted compromise between the raw count-model estimate and zero. Report posterior mean, posterior standard deviation, and a credible interval for each gene.

**Decision rule that separates strong effects from low-information extremes**
Pre-register a rule such as:
- **Strong, well-supported effect:** posterior mean \(|\beta| \ge \log_2(1.5)\) or \(\log_2(2)\), lower bound of the 95% credible interval above the null threshold, and sufficient information (e.g., mean count above a pre-specified floor or posterior SD below a pre-specified ceiling).
- **Low-information extreme:** large raw fold change but low count, high posterior SD, or one-replicate dominance. These should not be promoted to “strong” solely because the raw fold change is large.
- **Uncertain:** posterior interval crosses the threshold or information is marginal.

Thresholds are proposed, not established. They must be sensitivity-tested.

**How to test preservation without accepting unstable extremes**
Use two independent criteria:
1. **Preservation:** Among simulated or validated true strong effects, the method should retain them at high sensitivity.
2. **Rejection:** Among null or unvalidated low-information extremes, the method should not call them strong at a higher rate than a pre-specified false-positive tolerance.

A method that preserves strong effects by also accepting every low-count extreme fails. A method that rejects all low-count genes, including true low-count regulators, also fails if those genes are recoverable by independent validation.

---

## 5. Simulation plan

**Purpose.** Simulation provides known truth so that bias, sensitivity, false discovery and calibration can be measured without relying on an unavailable gold-standard biological result.

**Scenarios**
- **S1 Normal effects:** \(\beta_{g1} \sim N(0, \tau^2)\), matching the prior.
- **S2 Heavy-tailed effects:** \(\beta_{g1} \sim t\) or Cauchy-like, with more large true effects.
- **S3 Sparse mixture:** most genes null, a minority with large positive or negative effects.
- **S4 Low-count true effects:** true effects enriched in genes with low mean counts.
- **S5 High-count true effects:** true effects enriched in highly expressed genes.
- **S6 Null-only:** all effects zero, to estimate false positives.
- **S7 Dispersion heterogeneity:** gene-specific dispersion drawn from a wide distribution, to test the sharing step.

**Simulation parameters**
Use realistic library sizes, gene mean expression and dispersion trend estimated from the eligible dataset. Vary replicate number \(n = 2, 3, 5, 10\). Vary effect variance \(\tau^2\). Generate many independent simulation replicates.

**Comparators**
- The starting method: dispersion sharing + Normal prior.
- Ablations: no dispersion sharing; no Normal prior; no shrinkage.
These are internal controls, not external claims.

**Metrics**
- Sensitivity and false discovery rate for true effects.
- Bias and mean squared error of \(\hat\beta\).
- Precision-recall for strong effects.
- Calibration: observed validation rate versus posterior probability.
- Preservation of the top true effects.
- False-positive rate for low-information nulls.
- Performance stratified by mean count and dispersion.

**Falsifiable criteria**
- **Positive:** For true strong effects with adequate information, sensitivity ≥ 80% at a pre-specified FDR ≤ 5%; bias toward zero ≤ 20% of true effect; calibration slope between 0.9 and 1.1.
- **Negative:** Sensitivity for true strong low-count effects < 50%, or bias > 50%, or false-positive rate for low-information nulls > 10%, or calibration slope outside 0.7–1.3.
- **Ambiguous:** Normal simulations pass but heavy-tailed or low-count simulations fail; or results depend materially on the pre-specified information floor.

---

## 6. Independent validation

**Held-out sample validation**
If enough biological replicates exist, split them into training and test sets. Fit the shrinkage model on training only. On the held-out test set, compute a simple independent effect measure, such as the difference in mean normalized counts or a rank-based statistic, without using the training shrinkage. For genes called strong in training, test whether the held-out effect has the same sign and comparable magnitude. For low-information extremes, test whether they replicate at all.

**External or orthogonal validation**
If an independent dataset, qPCR, reporter assay or knock-down validation is available, use it only after the primary model is frozen. Do not tune the model on the validation data. Pre-specify the validation gene set.

**Negative controls**
- Permute condition labels and rerun the pipeline. Strong calls should collapse to the null expectation.
- Include simulated null genes in the count matrix.
- Test whether low-information extremes are enriched among genes that fail validation.

**Validation metrics**
- Sign concordance for strong training effects.
- Spearman correlation between training and held-out effects for high-information genes.
- Validation rate of low-information extremes.
- Calibration of posterior probabilities against held-out outcomes.

**Falsifiable criteria**
- **Positive:** Sign concordance ≥ 80% for high-information strong effects; low-information raw extremes replicate at ≤ 10% or near the nominal false-positive rate; calibration within ±10%.
- **Negative:** Sign concordance ≤ 60%; low-information extremes replicate at a rate comparable to or higher than strong effects; calibration fails.
- **Ambiguous:** Validation set is underpowered; only a subset of genes can be tested; or results differ by count stratum.

---

## 7. Figure generation and interpretation

**Figure 1: Raw versus shrunken effects.** MA plot or scatter of raw log fold change versus posterior mean, colored by mean count. Highlight low-count extremes. Interpretation: if low-count extremes move strongly toward zero while high-count strong effects remain, this supports stabilization without erasing strong effects.

**Figure 2: Bias and uncertainty by count stratum.** Estimated bias versus true effect in simulations, faceted by mean count. Interpretation: bias toward zero should be small for strong high-information effects and larger only where information is genuinely low.

**Figure 3: Calibration plot.** Binned posterior probability versus observed validation rate. Interpretation: points near the diagonal indicate calibrated uncertainty; systematic overconfidence or underconfidence indicates misspecification.

**Figure 4: Precision-recall for strong effects.** Curves for Normal, heavy-tailed and sparse-mixture simulations. Interpretation: if the Normal prior is adequate, curves should be similar across scenarios; if not, heavy-tailed scenarios will show lower recall.

**Figure 5: Dispersion sharing diagnostic.** Gene-wise dispersion estimates before and after sharing. Interpretation: excessive collapse to the trend suggests H3.

**Figure 6: Validation concordance.** Held-out effect versus training effect for strong and low-information genes. Interpretation: strong genes should lie near the identity line; low-information extremes should scatter or regress toward zero.

**Interpretation rules**
- **Positive conclusion:** The method preserves strong, high-information effects, shrinks low-information extremes, and is calibrated on independent validation. The biological conclusion is that the method can be used to prioritize real expression changes, with low-count genes reported as uncertain.
- **Negative conclusion:** The method over-shrinks true strong effects or accepts unstable extremes. The biological conclusion is that Normal-prior shrinkage alone is not sufficient for this contrast.
- **Ambiguous conclusion:** Performance depends on the assumed effect distribution, count threshold or validation availability. The biological conclusion is that the method may be useful for high-information genes but cannot resolve low-count changes without additional data.

---

## 8. Conditional conclusions

**Conditional positive conclusion.** If simulations show that the Normal prior matches or approximates the true effect distribution, and held-out validation confirms that strong high-information effects replicate while low-information extremes do not, then the method is a defensible filter for real expression changes. It would not prove that every called gene is causal, but it would support using shrunken effects for prioritization.

**Conditional negative conclusion.** If heavy-tailed simulations show substantial attenuation of true large effects, or if low-count extremes are called at high rates and fail validation, then the Normal prior is too restrictive or the dispersion-sharing step is distorting ranking. The method should not be used to claim recovery of real expression changes without modification.

**Conditional ambiguous conclusion.** If results are favorable only under Normal simulations but fail under sparse-mixture or low-count simulations, or if validation is underpowered, the correct conclusion is uncertainty. The method may still be useful for high-count genes, but low-count differential expression remains unresolved.

---

## 9. Alternatives, limits and what would change the recommendation

**Alternatives**
- No shrinkage: retains large raw effects but accepts unstable low-information extremes.
- Heavier-tailed prior: may preserve large true effects better but may be less stable.
- Mixture or spike-and-slab prior: explicitly models null and non-null genes, but adds assumptions.
- Nonparametric or rank-based approaches: avoid the Normal prior but may lose power with few replicates.

**Limits**
- The packet establishes rationale, not the true biological effect distribution.
- Simulation truth is assumed; it cannot prove what real biology does.
- Independent validation may be unavailable or underpowered.
- Low-count genes may be biologically important but statistically unmeasurable.
- A count model estimates association, not causation.
- This is one independent attempt; no prior attempts or evaluation feedback are available.

**What would change the recommendation**
- Evidence that true effects are approximately Normal and that validation confirms strong-effect preservation would support the Normal prior.
- Evidence of heavy-tailed or sparse true effects would favor a heavier-tailed or mixture prior.
- Evidence that low-count true effects are recoverable by orthogonal assays would raise the cost of over-shrinkage and change the acceptable decision rule.
- Absence of independent validation would limit conclusions to simulation-based methodological direction, not biological recovery.

**Final statement.** No biological result has been reproduced or observed here. The proposal is a falsifiable evaluation plan for a methods-direction forecast. Its value is to specify in advance what would count as success, failure or ambiguity when recovering real expression changes from noisy sequencing data.
