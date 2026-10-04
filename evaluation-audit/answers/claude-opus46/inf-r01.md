# Claude Opus 4.6 / inf-r01

Original final answer, shared by both scoring rounds.

# Recovering Real Expression Changes from Noisy RNA-Seq Data: A Complete Methodological Proposal

---

## 1. THE BIOLOGICAL QUESTION

**Can a shrinkage-based estimation framework recover the true ranking and magnitude of gene-level expression differences in a low-replicate RNA-seq experiment, preserving genuinely large biological effects while suppressing the unstable extremes that arise from low-count, high-variance genes?**

This question is biologically relevant because downstream decisions—which genes to validate by qPCR, which pathways to prioritize, which candidates to perturb—depend on accurate effect-size estimates, not merely on statistical significance. If the method systematically attenuates real large effects or, conversely, fails to tame spurious extremes, biological interpretation is compromised.

### 1.1 Competing Mechanisms of Estimation Error

Two distinct failure modes compete:

- **Mechanism A (Under-shrinkage):** The Normal prior on log-fold-change is too diffuse, leaving noisy estimates essentially unregularized. Low-count genes retain extreme, unstable fold-changes. Consequence: false prioritization of biologically irrelevant genes.
- **Mechanism B (Over-shrinkage):** The prior is too concentrated, pulling genuinely large effects toward zero. Consequence: real biological signal—especially for lowly-expressed but truly differentially regulated genes—is lost.

A well-calibrated shrinkage estimator navigates between these extremes. The question becomes: **under what data conditions (replicate number, count depth, true effect-size distribution) does the method achieve this balance, and when does it fail?**

### 1.2 Distinct Predictions

| Scenario | Prediction if method well-calibrated | Prediction if over-shrunk | Prediction if under-shrunk |
|---|---|---|---|
| Genes with high counts and large true LFC | Shrunken LFC ≈ true LFC | Shrunken LFC < true LFC | Shrunken LFC ≈ MLE (noisy but centered on truth) |
| Genes with low counts and large true LFC | Shrunken LFC moderately attenuated but rank preserved | Shrunken LFC severely attenuated; rank lost | Shrunken LFC = MLE; extreme and unstable |
| Genes with low counts and zero true LFC | Shrunken LFC ≈ 0 | Shrunken LFC ≈ 0 (correct but for wrong reason) | Shrunken LFC = MLE; spurious extremes |

---

## 2. PROPOSED METHOD

### 2.1 Conceptual Framework

The method uses a **hierarchical negative-binomial count model** with gene-wise dispersion estimates stabilized by borrowing strength across all genes, combined with a **Normal prior on log₂-fold-change (LFC)** centered at zero. This is the framework described in the evidence packet. The key parameters are:

- **Gene-level dispersion (α_i):** estimated per gene, then moderated toward a trend fitted across all genes as a function of mean count.
- **Log₂-fold-change (β_i):** maximum-likelihood estimate (MLE) obtained from the negative-binomial GLM, then shrunk toward zero using an empirical Bayes Normal prior whose scale is estimated from the data.

The posterior mode (MAP estimate) replaces the MLE as the reported effect size.

### 2.2 Formal Model

For gene *i*, sample *j*, condition *k*:

K_ij ~ NegBin(μ_ij, α_i)

log₂(μ_ij) = β_i0 + β_i1 · X_j + log₂(s_j)

where s_j is a size factor, X_j is the condition indicator, and β_i1 is the LFC of interest.

Prior: β_i1 ~ Normal(0, σ²_prior), with σ²_prior estimated from the observed distribution of MLEs across genes (empirical Bayes).

Dispersion: α_i is estimated gene-wise, then shrunk toward a mean-dispersion trend using a log-normal prior.

### 2.3 Critical Design Choice: Handling Strong Effects

The Normal prior will always exert *some* pull toward zero. For genes with high information (many counts, low dispersion), the likelihood dominates and shrinkage is minimal. For genes with low information, shrinkage is substantial. The concern is that a gene with a genuine LFC of 5 but only 10 total counts will be pulled strongly toward zero.

**Our proposal tests this explicitly** by stratifying evaluation by information content (Fisher information for each gene's LFC, approximately proportional to mean count / dispersion).

---

## 3. FALSIFIABLE EVALUATION PLAN

### 3.1 Overview of the Five-Stage Pipeline

```
Stage 1: Dataset eligibility and raw-read provenance
Stage 2: Estimation on real data
Stage 3: Simulation with known truth
Stage 4: Independent validation
Stage 5: Figure generation and interpretation
```

---

### 3.2 Stage 1: Dataset Eligibility and Raw-Read Provenance

**Eligibility criteria for a real dataset:**

1. Publicly deposited RNA-seq data (e.g., GEO/SRA) from a two-group comparison (e.g., treatment vs. control) in a model organism with well-annotated genome.
2. Low biological replication: n = 2–4 per group, to exercise the regime where shrinkage matters most.
3. Paired-end, polyA-selected or ribo-depleted library preparation.
4. Raw FASTQ files available (not only processed counts), to control the alignment pipeline.
5. At least partial independent validation available (qPCR, proteomics, or a higher-replicate companion study for the same biological comparison).

**Example candidate:** A publicly available dataset comparing a knockout vs. wild-type mouse tissue with n = 3 per group and accompanying qPCR validation of ~20 genes.

**Raw-read provenance documentation:**
- Record SRA accession numbers, sequencing platform, read length, adapter sequences.
- Perform FastQC on raw reads; document per-base quality, duplication rate, adapter contamination.
- Align with a documented aligner (e.g., STAR, version-locked) to a specified genome build (e.g., GRCm39).
- Quantify at the gene level using a specified annotation (e.g., GENCODE vM33) with a documented tool (e.g., featureCounts with specified parameters: paired-end, strand-specific or unstranded as appropriate, minimum mapping quality).
- Output: a raw integer count matrix (genes × samples) with full parameter provenance.

**Why this matters:** Shrinkage estimator behavior depends on the count distribution. Differences in alignment or quantification can change the distribution of counts and dispersions, potentially altering which genes appear extreme.

---

### 3.3 Stage 2: Estimation on Real Data

**Protocol:**

1. **Filtering:** Remove genes with fewer than 10 total counts across all samples (standard practice to exclude genes with essentially no information).
2. **Size-factor estimation:** Median-of-ratios method.
3. **Dispersion estimation:** Gene-wise MLE → fit mean-dispersion trend → shrink gene-wise estimates toward trend.
4. **LFC estimation (two versions):**
   - (a) MLE: standard GLM fit, no prior.
   - (b) MAP (shrinkage): Normal prior on LFC, σ_prior estimated from data.
5. **Record for every gene:**
   - Mean normalized count (baseMean)
   - MLE of LFC and its standard error
   - MAP (shrunken) LFC
   - Wald test p-value and Benjamini-Hochberg adjusted p-value
   - Gene-wise dispersion (MLE and shrunken)
   - Fisher information proxy: baseMean / shrunken dispersion

**Key comparison:** Plot MLE vs. MAP estimates, colored by information content. This is the classic "MA-plot with shrinkage" but with explicit stratification.

---

### 3.4 Stage 3: Simulation with Known Truth

This is the core falsifiable component. We simulate data where the ground truth is known, then ask whether the estimator recovers it.

#### 3.4.1 Simulation Design

**Parameters drawn from the real dataset (Stage 2):**
- Use the observed distribution of baseMean values and shrunken dispersions from the real data as the simulation's gene-wise parameters. This ensures realistic count and dispersion structure.
- Number of genes: same as filtered real dataset (typically 12,000–18,000).
- Number of replicates per group: match real data (e.g., n = 3 per group), plus explore n = 2 and n = 6 for sensitivity.

**True LFC assignment:**
- 80% of genes: true LFC = 0 (null genes).
- 10% of genes: true LFC drawn from Normal(0, 1.5²), representing moderate effects.
- 5% of genes: true LFC drawn from Uniform(3, 6), representing strong positive effects.
- 5% of genes: true LFC drawn from Uniform(−6, −3), representing strong negative effects.

This mixture is deliberately designed to include both the bulk of null/moderate genes (where the Normal prior is appropriate) and a tail of strong effects (where over-shrinkage is the concern).

**Simulation procedure:**
For each gene *i*:
1. Assign baseMean_i and dispersion_i from the real data's empirical distribution.
2. Assign true LFC_i from the mixture above.
3. For each sample *j* in condition *k* ∈ {0, 1}:
   - μ_ij = baseMean_i · s_j · 2^(LFC_i · X_j), where X_j = k.
   - K_ij ~ NegBin(μ_ij, α_i).

Repeat the entire simulation B = 50 times to assess estimator variability.

#### 3.4.2 Metrics

For each simulation replicate, compute:

1. **Mean squared error (MSE)** of shrunken LFC vs. true LFC, overall and stratified by:
   - True LFC magnitude (null, moderate, strong)
   - Information content (low, medium, high baseMean)

2. **Bias** of shrunken LFC for the "strong effect" genes, stratified by baseMean.

3. **Rank correlation** (Spearman) between |shrunken LFC| and |true LFC| among truly DE genes.

4. **False discovery proportion** among genes called significant at adjusted p < 0.05.

5. **Sensitivity for strong effects:** Proportion of genes with |true LFC| > 3 that are (a) called significant, (b) have |shrunken LFC| > 2 (i.e., not shrunk below a biologically meaningful threshold).

6. **Instability metric for low-information extremes:** Among null genes in the lowest baseMean quartile, compute the variance of MLE and MAP estimates across simulation replicates. The prediction is that MAP variance << MLE variance.

#### 3.4.3 The Critical Test: Preservation of Strong Effects Without Accepting Unstable Extremes

**Operationalization:**

Define two gene sets in each simulation:
- **"Strong-true" set:** genes with |true LFC| > 3 AND baseMean > median (high-information strong effects).
- **"Unstable-null" set:** genes with true LFC = 0 AND baseMean in the lowest decile (low-information nulls).

**Test 1 (Preservation):** For the strong-true set, compute the fraction of genes whose shrunken |LFC| is within 50% of the true |LFC|. Prediction: this fraction > 0.90 for n ≥ 3.

**Test 2 (Suppression):** For the unstable-null set, compare the 95th percentile of |MLE| vs. |MAP|. Prediction: the 95th percentile of |MAP| < 1 (biologically negligible), whereas the 95th percentile of |MLE| > 2 (spuriously large).

**Test 3 (Ranking):** Among all truly DE genes (|true LFC| > 0), compute the Spearman correlation between |MAP| ranking and |true LFC| ranking. Compare with the same correlation using |MLE| ranking. Prediction: MAP ranking has higher correlation with truth.

**Falsifiability:** If any of these tests fail—specifically, if the MAP estimator attenuates strong-true effects by more than 50%, or fails to suppress unstable-null extremes below |LFC| = 2, or has lower rank correlation than the MLE—then the method is inadequate for the tested data regime, and the Normal prior specification is called into question.

#### 3.4.4 Sensitivity to Prior Misspecification

The evidence packet notes that the method uses a Normal prior but does not assume the true biological effect distribution is Normal. We test robustness:

- **Scenario A:** True LFC distribution is exactly Normal → prior is well-specified.
- **Scenario B:** True LFC distribution is a heavy-tailed t-distribution (df = 3) → prior is misspecified in the tails.
- **Scenario C:** True LFC distribution is bimodal (mixture of point mass at 0 and Normal(±3, 0.5²)) → prior is misspecified in shape.

For each scenario, repeat the simulation and metrics. If the Normal-prior estimator shows severely degraded performance under Scenario B or C (e.g., rank correlation drops below that of the MLE), this identifies a regime where alternative priors (e.g., Cauchy, Laplace, or adaptive mixture priors) may be needed.

---

### 3.5 Stage 4: Independent Validation

**Purpose:** Bridge from simulation (where truth is known but artificial) to real biology (where truth is unknown but partially accessible).

#### 3.5.1 Validation Against qPCR or Independent High-Replicate Data

If the chosen dataset has qPCR measurements for a subset of genes:

1. For each qPCR-validated gene, obtain the qPCR-based LFC estimate and the RNA-seq-based MLE and MAP estimates.
2. Compute correlation (Pearson and Spearman) of qPCR LFC with MLE and with MAP.
3. Compute MSE of each estimator relative to qPCR.
4. **Prediction:** MAP estimates should have equal or higher correlation with qPCR and equal or lower MSE, particularly for genes with low RNA-seq counts.

If an independent higher-replicate RNA-seq study of the same comparison is available:
1. Treat the high-replicate study's estimates as "near-truth" (with n ≥ 10, MLEs are already well-estimated).
2. Repeat the correlation/MSE analysis above.

#### 3.5.2 Held-Out Replicate Approach

If no external validation is available:
1. Randomly hold out one replicate from each condition.
2. Estimate LFC (MLE and MAP) from the reduced dataset (n − 1 per group).
3. Use the held-out replicates to compute a "pseudo-truth" LFC for each gene (ratio of held-out counts, with pseudocount).
4. Compare MLE and MAP from the reduced dataset against the pseudo-truth.
5. **Caveat:** This pseudo-truth is itself noisy (single replicate), so the comparison is weaker. It primarily tests gross failures rather than subtle calibration.

---

### 3.6 Stage 5: Figure Generation and Interpretation

**Figure 1: MA Plot with Shrinkage**
- x-axis: log₂(baseMean); y-axis: LFC.
- Panel A: MLE estimates (real data). Panel B: MAP estimates (real data).
- Color: adjusted p-value (significant in red, non-significant in grey).
- **Expected pattern:** Panel A shows a "fan" shape with extreme LFC at low baseMean. Panel B shows compression of this fan, with strong effects at high baseMean preserved.

**Figure 2: Simulation Truth Recovery**
- x-axis: true LFC; y-axis: estimated LFC (one panel for MLE, one for MAP).
- Points colored by information content (baseMean quartile).
- Identity line in black; loess fit in blue.
- **Expected pattern:** MAP estimates lie closer to the identity line, especially for high-information genes. Low-information genes are visibly shrunk toward zero. MLE estimates scatter widely, especially at low baseMean.

**Figure 3: Stratified MSE Comparison**
- Bar plot or box plot of MSE for MLE vs. MAP, stratified by (true LFC category) × (baseMean quartile).
- **Expected pattern:** MAP has lower MSE in all strata, with the largest improvement in the low-baseMean strata. For high-baseMean, strong-true-LFC genes, MLE and MAP MSE are similar (because shrinkage is minimal when information is high).

**Figure 4: The Critical Diagnostic**
- x-axis: information content (Fisher information proxy); y-axis: |estimated LFC| − |true LFC| (bias in magnitude).
- Separate curves for MLE and MAP.
- Horizontal line at zero (no bias).
- **Expected pattern:** MLE shows near-zero average bias but huge variance at low information. MAP shows slight negative bias (attenuation) at low information, but much smaller variance. At high information, both converge to zero bias.

**Figure 5: Validation Concordance**
- Scatter plot: qPCR LFC (x-axis) vs. RNA-seq LFC (y-axis), with MLE in one panel and MAP in another.
- Pearson/Spearman correlations annotated.
- **Expected pattern:** MAP panel shows tighter clustering around the identity line, especially for genes with lower RNA-seq counts.

**Figure 6: Prior Misspecification Sensitivity**
- MSE (or rank correlation) across Scenarios A, B, C, plotted for MLE and MAP.
- **Expected pattern:** MAP outperforms MLE in all scenarios, but the advantage is reduced under heavy-tailed (Scenario B) or bimodal (Scenario C) true distributions.

---

## 4. CONDITIONAL CONCLUSIONS

### 4.1 Positive Conclusion (All Tests Pass)

If the MAP estimator:
- Preserves >90% of strong-true effects within 50% of their true magnitude (Test 1),
- Suppresses 95th percentile of unstable-null |LFC| below 1 (Test 2),
- Achieves higher rank correlation with truth than MLE (Test 3),
- Shows comparable or better concordance with qPCR/independent data (Stage 4),

then we conclude: **The Normal-prior shrinkage estimator effectively recovers real expression changes from noisy low-replicate RNA-seq data across the tested count and effect-size regimes.** The method is appropriate for ranking candidate genes by biological effect size. The benefit is greatest for low-information genes and in low-replicate experiments.

### 4.2 Negative Conclusion (Critical Tests Fail)

If:
- Test 1 fails: strong-true effects are attenuated below 50% of their true magnitude, especially for low-baseMean genes,
- OR Test 3 fails: MAP ranking is no better than MLE ranking,
- OR Stage 4 shows lower concordance for MAP than MLE with qPCR,

then we conclude: **The Normal prior is too restrictive for the effect-size distribution in this biological system.** The method over-shrinks real large effects. Recommended next step: test alternative priors (e.g., Cauchy prior, which has heavier tails and exerts less shrinkage on large effects; or an adaptive shrinkage approach that estimates the prior from the data without constraining it to be Normal).

### 4.3 Ambiguous Conclusion

If:
- MAP outperforms MLE on MSE and rank correlation in simulation, but
- Validation data (Stage 4) show no significant difference (e.g., because qPCR validation covers only 15 genes and power is low),
- And prior misspecification scenarios (B, C) show degraded MAP performance,

then we conclude: **The method is likely beneficial under the assumptions of the simulation, but the evidence is insufficient to confirm benefit in the real biological system, and robustness to non-Normal effect distributions is uncertain.** The priority next step is to obtain or generate higher-replicate data or broader qPCR panels to power the validation comparison.

---

## 5. DISTINGUISHING METHODS-DIRECTION FORECAST FROM BIOLOGICAL REPRODUCTION

**This proposal is a methods-direction forecast, not a reproduction of published biological results.**

Specifically:
- We do **not** claim that any of the described figures or numerical results have been observed. Every stated "expected pattern" is a **prediction** based on the logic of the method and the evidence packet, not a reported finding.
- We do **not** claim to reproduce the specific differential expression results of any published study. Our simulation uses parameters drawn from a real dataset but assigns artificial true LFCs; it tests the *statistical method*, not the *biological conclusion* of the original study.
- If this plan were executed and the positive conclusion obtained, it would support the claim that "the method is a reliable statistical tool" but would **not** by itself confirm any specific biological finding (e.g., "Gene X is upregulated 4-fold in the knockout"). Biological conclusions require the additional assumption that the model correctly captures the data-generating process for the specific experiment.
- Conversely, published biological results (e.g., "these 200 genes are differentially expressed in condition Y") cannot be reproduced solely by re-analyzing with a different shrinkage estimator. Differences in results would reflect statistical methodology, not new biological evidence.

---

## 6. EVIDENCE-TO-INFERENCE CHAIN

| Evidence (from packet) | Inference | Conclusion/Action |
|---|---|---|
| Count model is used for gene-level expression | Discrete count distribution (NB) is appropriate; Gaussian approximations of counts are not | Use negative-binomial likelihood throughout |
| Few replicates yield unstable fold-change estimates | Low Fisher information per gene → high MLE variance → need for regularization | Shrinkage estimator is motivated; test its calibration |
| Method shares information across genes | Empirical Bayes: population of genes informs per-gene estimates | Dispersion and LFC priors are data-driven; evaluate whether the estimated prior is appropriate |
| Normal prior on effects is used | Assumes most true LFCs are near zero, with symmetric tails | Test whether this assumption holds; evaluate robustness to heavy-tailed and bimodal truth |
| Packet does not supply evidence about every possible biological effect distribution | Prior may be misspecified for some real systems | Explicitly test misspecification scenarios in simulation |

---

## 7. ASSUMPTIONS AND UNREPORTED PARAMETERS

1. **Assumption:** Negative-binomial model adequately captures the mean-variance relationship in the real data. *If violated (e.g., zero-inflation, batch effects):* dispersion estimates and hence shrinkage may be miscalibrated. Mitigation: check goodness-of-fit via dispersion plots and Cook's distance.

2. **Assumption:** Size factors adequately normalize library composition differences. *If violated:* systematic bias in LFC estimates. Mitigation: compare median-of-ratios with alternative normalization (TMM, upper-quartile).

3. **Unreported parameter:** The scale of the Normal prior (σ_prior). This is estimated from data but its value critically determines shrinkage strength. **We will report this estimated value and test sensitivity by repeating analysis with σ_prior fixed at 0.5× and 2× the estimated value.**

4. **Unreported parameter:** The exact filtering threshold. We specify ≥10 total counts, but results may depend on this choice. **We will repeat with thresholds of 1, 5, 10, and 50 to assess sensitivity.**

5. **Assumption:** Independence of genes. The hierarchical model treats genes as exchangeable. Correlated genes (e.g., co-regulated in a pathway) violate this. *Impact:* the empirical Bayes prior may be over-influenced by large co-regulated gene sets. Mitigation: not fully addressed here; noted as a limitation.

---

## 8. ALTERNATIVES AND LIMITS

### Alternative Approaches
- **Cauchy or t-prior on LFC:** Heavier tails; less shrinkage on large effects. Would be preferred if Scenario B shows substantial degradation.
- **Adaptive shrinkage (ash-type):** Estimates a flexible mixture prior from the data. Avoids assuming Normality. More complex; may overfit with very few genes.
- **No shrinkage + stringent filtering:** Simply discard low-count genes. Loses power; biases toward highly-expressed genes.
- **Bayesian full posterior:** Report posterior intervals rather than point estimates. More informative but computationally heavier and harder to rank genes.

### Fundamental Limits
- With n = 2 per group, even optimal shrinkage cannot rescue genes with very few counts. The method improves ranking but cannot create information that does not exist.
- The true biological effect-size distribution is never known. Simulation can test a range of plausible distributions but cannot exhaust all possibilities.
- External validation (qPCR) is itself imperfect and limited in gene coverage. Concordance analyses have limited power.

---

## 9. SUMMARY

**Unresolved question:** Does Normal-prior shrinkage of RNA-seq fold-change estimates preserve genuine large biological effects while suppressing noise-driven extremes, and under what conditions does it fail?

**Proposed method:** Hierarchical negative-binomial model with empirical Bayes Normal prior on LFC, applied to a real low-replicate dataset with full raw-read provenance.

**Evaluation:** Simulation with known truth (drawn from the real data's count/dispersion structure), stratified by information content and true effect size, with explicit falsifiable criteria. Independent validation against qPCR or high-replicate data. Sensitivity analysis for prior misspecification.

**Key falsifiable prediction:** The MAP estimator will (a) attenuate strong-true high-information effects by less than 50%, (b) suppress spurious extremes among low-information null genes, and (c) achieve higher rank correlation with truth than the MLE. Failure of any criterion triggers specific methodological revisions.

**This is a methods-direction forecast:** no results are claimed as observed; the plan describes what would be done and what outcomes would mean, not what was found.
