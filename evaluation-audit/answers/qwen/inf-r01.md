# Qwen3.8 Max (0902) / inf-r01

Original final answer, shared by both scoring rounds.

Recommended next action: treat the information-sharing, Normal-prior count-model estimator as the primary candidate method, but accept it only after a pre-specified falsifiable evaluation showing that it reduces unstable low-information fold-change extremes while preserving strong effects that are supported by sufficient information. This is a proposed protocol only; no dataset has been analyzed and no proposed results are claimed as observed. This is one independent attempt, with no prior attempts or evaluation feedback incorporated.

---

## 1. Unresolved biological question

**Biologically relevant question:**  
In an RNA-seq experiment comparing two biological conditions with few replicates, can we recover the direction and approximate magnitude of true gene-level expression changes, especially for low-count or highly variable genes, without mistaking sampling noise for large biological effects?

A concrete biological version is: *Which low-abundance regulatory genes are genuinely induced or repressed by a treatment, and which apparent large fold changes are artifacts of low-count sampling noise?* Low-abundance transcripts are biologically important because they can include transcription factors, cytokines, receptors, or stress-response genes, but they are also statistically fragile in short-read count data.

### Competing mechanisms

| Mechanism | Biological/statistical meaning | Distinct prediction |
|---|---|---|
| **M1: Noise-dominant extremes** | Large fold changes among low-count genes are mostly sampling noise or unstable dispersion estimates. | Shrinkage should reduce extreme low-count estimates, improve validation concordance, and decrease false sign rates. |
| **M2: Real rare strong regulation** | Some low-count genes truly change strongly, and zero-centered shrinkage may incorrectly attenuate them. | Strong low-count effects should validate despite shrinkage; if shrinkage removes them, a heavier-tailed or adaptive prior may be needed. |
| **M3: Model misspecification or confounding** | Apparent instability comes from unmodeled batch effects, library-composition artifacts, or incorrect count-model assumptions. | Both shrunk and unshrunk estimates may validate poorly; improvement from shrinkage alone will be limited. |

The packet supports the rationale for shrinkage but explicitly does **not** establish every possible underlying distribution of biological effects. Therefore, the evaluation must test whether shrinkage improves recovery without blindly suppressing true strong effects.

---

## 2. Evidence-to-inference-to-conclusion chain

**Evidence supplied:**

1. RNA-seq analysis estimates gene-level expression differences using a count model.  
2. With few biological replicates, low or variable counts can yield unstable fold-change estimates.  
3. A method stabilizes dispersion and fold-change estimates by sharing information across genes and using a Normal prior on effects.  
4. The packet establishes the rationale for shrinkage but does not supply evidence about every possible underlying distribution of biological effects.

**Inferences:**

1. Count-based estimates have sampling noise. When counts are low or dispersed, gene-specific maximum-likeelihood fold-change estimates can have high variance.  
2. Sharing information across genes can stabilize nuisance parameters such as dispersion.  
3. A Normal prior on effects can reduce variance by pulling uncertain estimates toward a central value, usually no change.  
4. Because the true distribution of biological effects is not fully known, shrinkage could improve average accuracy while still biasing rare true large effects.  
5. Therefore, the method should be evaluated using known truth, stability diagnostics, and independent validation, with explicit criteria for both false-extreme suppression and strong-effect preservation.

**Conclusion:**  
Use the shrinkage count model as the proposed estimator, but only endorse it if it satisfies pre-specified criteria: lower low-information false-extreme rates, improved fold-change accuracy or stability, calibrated uncertainty, and preservation of strong effects when information is adequate.

---

## 3. Proposed method: information-sharing shrinkage for count-based expression changes

### 3.1 Core model

For gene \(g\) in sample \(i\), let \(Y_{gi}\) be the gene-level read count. Use a count model with a mean and a dispersion parameter:

\[
Y_{gi} \sim \text{CountModel}(\mu_{gi}, \alpha_g)
\]

with

\[
\log(\mu_{gi}) = \log(s_i) + x_i \beta_g + z_i \gamma_g
\]

where:

- \(s_i\) is a library-size or normalization factor for sample \(i\);
- \(x_i\) encodes the biological condition comparison;
- \(\beta_g\) is the gene-level log fold-change, for example log2 fold-change;
- \(z_i\) encodes optional batch or nuisance covariates;
- \(\gamma_g\) are gene-specific nuisance coefficients;
- \(\alpha_g\) is a dispersion or variability parameter.

The count-model family is left generic because the packet specifies a count model but not a unique distribution. Any instantiated overdispersed count model must be recorded and justified.

### 3.2 Dispersion stabilization

For each gene:

1. Obtain a gene-wise dispersion estimate \(\hat{\alpha}_g\).  
2. Fit a dispersion trend \(\alpha_{\text{trend}}(\bar{\mu}_g)\) as a function of mean expression.  
3. Combine gene-wise and trend information to obtain a stabilized dispersion estimate \(\tilde{\alpha}_g\).  

Conceptually:

\[
\log \tilde{\alpha}_g \approx w_g \log \hat{\alpha}_g + (1 - w_g) \log \alpha_{\text{trend}}(\bar{\mu}_g)
\]

where \(w_g\) is larger when the gene has high information and smaller when the gene-level estimate is unreliable.

### 3.3 Fold-change shrinkage using a Normal prior

Place a zero-centered Normal prior on the condition effect:

\[
\beta_g \sim N(0, \tau^2)
\]

The prior width \(\tau\) is estimated from the data, preferably using robust estimation to avoid a small number of extreme genes dictating the prior scale. The posterior or penalized estimate is:

\[
\tilde{\beta}_g = \arg\max_{\beta_g}
\left[
\log L_g(\beta_g) - \frac{\beta_g^2}{2\tau^2}
\right]
\]

where \(\log L_g\) is the gene-specific log-likelihood under the count model.

A useful approximation is:

\[
\tilde{\beta}_g \approx
\frac{J_g}{J_g + \tau^{-2}}
\hat{\beta}_g
\]

where \(\hat{\beta}_g\) is the unshrunk estimate and \(J_g\) is the observed information. This shows the intended behavior:

- High-information genes: \(J_g\) large, shrinkage small, \(\tilde{\beta}_g \approx \hat{\beta}_g\).  
- Low-information genes: \(J_g\) small, shrinkage stronger, \(\tilde{\beta}_g\) moves toward zero.  
- Strong effects supported by sufficient evidence are preserved because the likelihood dominates the prior.  
- Unsupported low-count extremes are attenuated.

### 3.4 Information metric

Define a pre-analysis information score for each gene:

\[
I_g = \text{inverse estimated variance of } \hat{\beta}_g
\]

or, if the model does not directly provide this, use a composite proxy:

\[
I_g = \log_{10}
\left(
\frac{\text{total normalized count for gene } g}
{1 + \tilde{\alpha}_g}
\right)
\]

This score must be calculated without using the true effect size in simulations. It will be used to stratify genes into low-, medium-, and high-information groups.

---

## 4. Complete proposed protocol

### Step 0: Pre-registration and no-results statement

Before analysis, record:

- eligible dataset criteria;
- count-model specification;
- normalization strategy;
- prior specification and estimation procedure;
- simulation scenarios;
- validation gene-selection rules;
- performance metrics;
- pass/fail thresholds;
- random seeds;
- software versions.

No result described below is claimed to have been observed.

---

## 5. Dataset eligibility

A dataset is eligible for method evaluation only if it satisfies the following.

### 5.1 Required biological design

1. At least two biological conditions, for example treated versus control.  
2. Biological replicates within each condition.  
   - Minimum: two replicates per condition.  
   - Preferred: three or more replicates per condition.  
   - Datasets with one replicate per condition are ineligible for primary evaluation because dispersion and fold-change stability cannot be assessed credibly.  
3. Condition labels must not be completely confounded with batch, library preparation date, sequencing lane, or operator. If confounding exists, the dataset may be used only for diagnostic exploration, not for biological validation claims.

### 5.2 Required data types

1. Raw sequencing reads, preferably FASTQ files, or raw read equivalents with sufficient provenance.  
2. Gene annotation compatible with the quantification method.  
3. Sample metadata including condition, biological replicate identifier, batch if known, species, tissue or cell type, library preparation, and sequencing platform.  
4. Independent validation material or a credible plan to generate it:
   - spike-in RNAs with known fold changes,
   - qPCR or digital PCR on the same RNA samples,
   - or an independent replicate RNA-seq cohort processed separately.

### 5.3 Exclusion criteria

Exclude datasets if:

- only processed normalized counts are available and raw-read provenance cannot be reconstructed;
- biological condition is indistinguishable from technical batch;
- samples fail basic sequencing quality control;
- replicate identity is missing or ambiguous;
- library preparation or sequencing protocol changed in a way that cannot be modeled;
- the organism or annotation is unknown.

---

## 6. Raw-read provenance and processing

### 6.1 Provenance manifest

Create a manifest containing:

1. FASTQ file names and checksums.  
2. Source repository or lab storage location.  
3. Sample-to-file mapping.  
4. Sequencing instrument model.  
5. Read length and single-end or paired-end status.  
6. Strandedness.  
7. UMI status, if applicable.  
8. Library preparation protocol.  
9. Biological condition, batch, replicate, and any spike-in information.  
10. Reference genome or transcriptome version.  
11. Gene annotation version.  
12. Software versions and command-line parameters.

### 6.2 Read processing

1. Perform read-quality inspection.  
2. Trim adapters or low-quality bases only if required; record all parameters.  
3. Map reads, or pseudo-align reads, to the fixed reference.  
4. Generate a gene-level raw count matrix.  
5. Record genes excluded due to ambiguous annotation.  
6. Store the count matrix, sample sheet, and all logs together.

### 6.3 Sample QC

Before estimation:

- check total counts per sample;
- check proportion of mapped reads;
- check replicate clustering by condition;
- identify outlier samples;
- record whether any sample is excluded and why.

Exclusion of samples after inspection must be documented to avoid selective reporting.

---

## 7. Estimation workflow

### 7.1 Gene retention

For primary estimation:

- retain all genes with at least one read in at least one sample;
- separately annotate genes that would be removed by independent filtering for discovery;
- do not silently discard low-count genes from the evaluation, because they are central to the biological question.

For final discovery lists, independent filtering may be applied, but the filtering rule must be reported.

### 7.2 Normalization

Estimate sample-specific size factors \(s_i\) using the count model or a robust library-size normalization method. The method must be insensitive to a minority of strongly changing genes. Record:

- normalization method;
- size factors;
- whether spike-ins or external controls were used.

### 7.3 Fit unshrunk model

For each gene:

1. Estimate gene-wise dispersion \(\hat{\alpha}_g\).  
2. Estimate unshrunk log fold-change \(\hat{\beta}_g\).  
3. Estimate the standard error or inverse information \(J_g\).  

These unshrunk estimates are retained as the baseline comparator.

### 7.4 Stabilize dispersion

1. Fit the mean-dispersion trend.  
2. Estimate gene-wise posterior or penalized dispersions \(\tilde{\alpha}_g\).  
3. Inspect genes with extreme dispersion estimates for possible annotation or mapping artifacts.  
4. Record dispersion weights and trend parameters.

### 7.5 Estimate Normal-prior shrinkage

1. Estimate prior width \(\tau\) robustly from the distribution of high-information unshrunk effects.  
2. Fit the posterior log fold-change \(\tilde{\beta}_g\) under the Normal prior.  
3. Obtain posterior standard errors or credible intervals.  
4. Record the shrinkage factor for each gene, approximately:

\[
S_g = \frac{\tilde{\beta}_g}{\hat{\beta}_g}
\]

where defined.

### 7.6 Output table

For every gene, report:

- gene identifier;
- mean normalized expression;
- dispersion estimate;
- unshrunk log fold-change \(\hat{\beta}_g\);
- shrunk log fold-change \(\tilde{\beta}_g\);
- posterior uncertainty;
- information score \(I_g\);
- shrinkage factor;
- posterior probability of positive or negative change;
- discovery status under pre-specified rules;
- flags for low information, extreme raw estimate, or filter exclusion.

---

## 8. Simulation plan with known truth

Simulation is needed because the packet does not provide the true distribution of biological effects.

### 8.1 Simulation source

Use one or more eligible real datasets to estimate:

- library sizes;
- gene mean expression distribution;
- dispersion trend;
- replicate structure;
- batch structure if present.

Then simulate new count data with known true log fold-changes.

### 8.2 Simulation scenarios

Use at least four scenarios.

#### Scenario S1: Null only

All genes have true \(\beta_g = 0\).  
Purpose: measure false-extreme rate and false sign rate.

#### Scenario S2: Sparse small-to-moderate effects

Most genes are null. A small fraction have true effects drawn from a narrow Normal distribution.  
Purpose: test ordinary shrinkage performance.

#### Scenario S3: Heavy-tailed rare strong effects

Most genes are null, but a small fraction have large true effects, including some low-information genes.  
Purpose: test preservation of strong effects when the true effect distribution is not well described by a simple zero-centered Normal prior.

#### Scenario S4: Low-count strong effects

Strong true effects are intentionally assigned to genes with low expected counts or high dispersion.  
Purpose: directly test whether the method suppresses real low-information biology.

### 8.3 Simulation parameters to record

The following parameters are proposed and must be explicitly reported:

- number of simulated datasets;
- number of genes;
- number of replicates per condition;
- library depths;
- proportion of differentially expressed genes;
- true effect-size distribution;
- dispersion model;
- batch model, if any;
- random seed.

### 8.4 Methods compared

Compare:

1. **Unshrunk count-model estimator**: \(\hat{\beta}_g\).  
2. **Shrinkage estimator**: \(\tilde{\beta}_g\).  
3. Optional diagnostic comparator: unshrunk estimator with low-count filtering.  

The primary comparison is shrinkage versus unshrunk estimation under the same count model.

---

## 9. Falsifiable evaluation metrics

### 9.1 Primary hypotheses

**Methods-direction forecast:**  
The shrinkage estimator will reduce false low-information extremes and reduce fold-change error relative to the unshrunk estimator.

**Falsifiable null:**  
The shrinkage estimator does not improve low-information accuracy, or it unacceptably attenuates strong high-information effects.

### 9.2 Metrics

For each gene stratum defined by information \(I_g\):

1. **Log-fold-change RMSE**

\[
\text{RMSE} =
\sqrt{
\frac{1}{G}
\sum_g
(\tilde{\beta}_g - \beta^{\text{true}}_g)^2
}
\]

2. **Bias**

\[
\text{Bias} =
\frac{1}{G}
\sum_g
(\tilde{\beta}_g - \beta^{\text{true}}_g)
\]

3. **False sign rate**  
Among genes with true nonzero effects, the fraction whose estimated sign is wrong.

4. **False extreme rate**  
Among true null genes in low-information strata, the fraction with high-confidence extreme estimates, for example:

\[
|\tilde{\beta}_g| > 1
\quad \text{and} \quad
P(\text{direction} \mid \text{data}) > 0.95
\]

Thresholds such as \(|\log_2 \text{FC}| > 1\) are proposed and must be fixed before analysis.

5. **Strong-effect preservation score**  
For genes with true strong effects, for example \(|\beta^{\text{true}}_g| \ge 1.5\), and with information above the median:

\[
\text{Preservation} =
\Pr(
\text{correct sign and }
|\tilde{\beta}_g - \beta^{\text{true}}_g| \le 0.5
)
\]

6. **Shrinkage factor by information and true effect size**

\[
S_g =
\frac{\tilde{\beta}_g}{\beta^{\text{true}}_g}
\]

computed only when the true effect is nonzero.

7. **Calibration**  
For posterior credible intervals, compute the fraction of true effects inside 95% intervals. Severe under-coverage or over-coverage indicates miscalibrated uncertainty.

### 9.3 Proposed pass/fail criteria

These are example criteria; they must be pre-specified.

The method passes if:

1. In low-information null genes, the false extreme rate is lower than or equal to the unshrunk method and does not exceed the nominal error rate.  
2. Across simulation scenarios, low-information RMSE is reduced by at least 10% relative to unshrunk estimation.  
3. For strong true effects in high-information genes, preservation is not reduced by more than 5 percentage points relative to unshrunk estimation at matched precision.  
4. Mean shrinkage factor for high-information strong effects is at least 0.8.  
5. Credible intervals are approximately calibrated, for example 95% coverage between 90% and 99% in well-specified scenarios.  

The method fails if:

1. It reduces false extremes by over-shrinking true strong high-information effects below acceptable preservation thresholds.  
2. It produces overconfident false discoveries in low-information null genes.  
3. It improves simulation metrics but fails independent validation without explanation.  
4. It is highly sensitive to arbitrary prior-width estimation in a way that changes biological conclusions.

---

## 10. Testing preservation of strong effects without accepting unstable low-information extremes

This is the central evaluation requirement.

### 10.1 Define strong effects and low information before testing

- **Strong effect:** proposed as true or validated \(|\log_2 \text{FC}| \ge 1.5\).  
- **Low information:** genes in the lowest quartile of \(I_g\), or genes with expected counts and replicate information below a pre-specified threshold.  
- **High information:** genes in the upper half or quartile of \(I_g\).

These definitions must be fixed before simulation or validation analysis.

### 10.2 Simulation-based preservation test

In simulated data:

1. Insert true strong effects into high-information genes.  
2. Insert true strong effects into low-information genes.  
3. Compare recovery separately.

Expected acceptable behavior:

- High-information strong effects: estimates remain close to truth, sign is correct, and posterior intervals cover the true value.  
- Low-information strong effects: estimates may be attenuated, but uncertainty should be large. The method should not report a high-confidence extreme unless the data genuinely support it.

Unacceptable behavior:

- High-information strong effects are systematically erased.  
- Low-information null genes are reported as high-confidence large changes.  
- Low-information true strong effects are reported as high-confidence only when their raw estimates are extreme, but posterior uncertainty remains high.

### 10.3 Real-data stability test

If enough replicates exist, perform leave-one-replicate-out or read-subsample refitting.

For each gene:

1. Fit the model on the full data.  
2. Refit after omitting one replicate, or after subsampling reads.  
3. Record whether direction and high-confidence status persist.

Define a **stable call** as one where:

- the estimated direction remains the same;
- the posterior probability remains above threshold;
- the shrunk fold-change does not collapse to near zero;
- this occurs in a pre-specified majority of perturbations, for example at least 80%.

Low-information extreme raw fold-changes that disappear under small perturbations are classified as unstable and are not accepted as biological findings.

### 10.4 Independent-validation safeguard

Select validation genes not only from the top shrunk hits but also from:

- high-information strong effects;
- low-information strong raw effects;
- low-information genes whose estimates were strongly shrunk;
- genes with contradictory raw and shrunk estimates.

This avoids circular validation of only the genes the method is already confident about.

---

## 11. Independent validation plan

Simulation alone is not enough to claim recovery of real biological expression changes. At least one independent validation layer is required.

### 11.1 Validation option A: spike-in controls

If spike-in RNAs with known concentrations and known fold changes are available:

1. Treat spike-in fold changes as truth.  
2. Compare unshrunk and shrunk estimates against known values.  
3. Stratify by spike-in abundance.  
4. Test whether shrinkage reduces error at low spike-in counts while preserving high-count strong changes.

Pass criteria:

- lower RMSE for low-abundance spike-ins;
- no substantial loss of recovery for high-abundance strong-change spike-ins;
- calibrated uncertainty intervals.

### 11.2 Validation option B: qPCR or digital PCR

Use the same RNA samples as the RNA-seq experiment.

Gene selection:

- 10 high-information strong RNA-seq hits;
- 10 low-information strong raw effects;
- 10 genes with large raw effects that were strongly shrunk toward zero;
- 10 stable null or weak-effect genes.

Proposed total: at least 40 genes, though the exact number depends on cost and sample availability.

Validation procedure:

1. Use pre-specified reference genes whose stability is justified.  
2. Measure expression in the same biological replicates.  
3. Compute independent log2 fold-changes.  
4. Compare RNA-seq estimates to qPCR estimates using correlation, slope, sign concordance, and absolute error.

Pass criteria:

- shrunk estimates have lower absolute error than unshrunk estimates in low-information genes;
- high-information strong effects remain concordant;
- genes with unstable low-information raw extremes show poor qPCR support, whereas stable high-information effects show good qPCR support.

### 11.3 Validation option C: independent replicate cohort

If new qPCR or spike-ins are not feasible:

1. Obtain an independent biological cohort with the same condition comparison.  
2. Process and sequence it independently.  
3. Compare sign concordance, effect-size correlation, and replication rate of high-confidence calls.

This is weaker than known-truth validation but can still test stability.

### 11.4 If no independent validation is possible

If no spike-ins, qPCR, or independent cohort are available, the conclusion must be limited to:

- simulation-based method behavior;
- internal stability diagnostics;
- model-based uncertainty estimates.

In that case, one may forecast that shrinkage is likely beneficial, but one cannot claim recovery of published or true biological results.

---

## 12. Figure generation and interpretation plan

### Figure 1: Dataset provenance and workflow

**Contents:**

- raw-read sources;
- QC steps;
- count generation;
- estimation pipeline;
- simulation and validation branches.

**Interpretation:**  
Shows that conclusions depend on traceable raw data and pre-specified processing.

---

### Figure 2: Mean-dispersion relationship and dispersion stabilization

**Contents:**

- gene-wise dispersion estimates;
- fitted dispersion trend;
- stabilized dispersion estimates.

**Interpretation:**  
If dispersion estimates are wildly scattered at low counts but stabilized near the trend, this supports the need for information sharing. If dispersion remains chaotic after stabilization, model fit is suspect.

---

### Figure 3: Fold-change shrinkage behavior

**Contents:**

- unshrunk log fold-change versus mean expression;
- shrunk log fold-change versus mean expression;
- shrinkage factor versus information score.

**Interpretation:**  
Expected behavior is strong shrinkage for low-information genes and weak shrinkage for high-information genes. If high-information genes are strongly shrunk, the prior may be too narrow or misspecified.

---

### Figure 4: Simulation accuracy by information stratum

**Contents:**

- RMSE, bias, false sign rate, and false extreme rate for unshrunk versus shrunk estimates;
- results separated by low-, medium-, and high-information genes.

**Interpretation:**  
The method is supported if low-information error and false extremes decrease while high-information accuracy is maintained.

---

### Figure 5: Preservation of strong effects

**Contents:**

- true effect size versus estimated effect size;
- shrinkage factor versus true effect size;
- separate panels for low-information and high-information genes.

**Interpretation:**  
Strong high-information effects should lie near the identity line. Low-information true strong effects may be attenuated but should have wide uncertainty. If true high-information strong effects are systematically pulled toward zero, the method fails preservation.

---

### Figure 6: Low-information false extremes

**Contents:**

- histogram of raw and shrunk fold-changes for simulated null low-information genes;
- number of high-confidence false discoveries before and after shrinkage.

**Interpretation:**  
A successful method should remove the long tails produced by unsupported low-count estimates.

---

### Figure 7: Independent validation concordance

**Contents:**

- RNA-seq log fold-change versus qPCR, spike-in, or independent cohort log fold-change;
- points colored by information stratum;
- separate panels for unshrunk and shrunk estimates.

**Interpretation:**  
Support for the method requires improved agreement in low-information genes without loss of agreement for high-information strong effects.

---

### Figure 8: Stability under replicate perturbation

**Contents:**

- full-data estimate versus leave-one-out or subsampled estimates;
- point transparency proportional to information score.

**Interpretation:**  
Stable high-information effects should remain on the diagonal. Low-information extremes that scatter widely are not accepted as reliable biological changes.

---

## 13. Conditional conclusions

### 13.1 Positive conclusion

If the evaluation shows:

- reduced false extreme rate among low-information null genes;
- lower fold-change RMSE or higher stability in low-information genes;
- calibrated uncertainty;
- preservation of strong high-information effects;
- independent validation concordance equal to or better than unshrunk estimation;

then the conclusion is:

**The Normal-prior, information-sharing count-model estimator improves recovery of real gene-level expression changes under low-replicate noisy RNA-seq conditions, while limiting unstable low-information extremes.**

This conclusion would still be conditional on the evaluated datasets, simulation scenarios, and validation design.

### 13.2 Negative conclusion

If the evaluation shows:

- no reduction in low-information false extremes;
- no improvement in RMSE or stability;
- overconfident false discoveries;
- severe attenuation of true strong high-information effects;
- poor independent validation concordance;

then the conclusion is:

**The proposed shrinkage method does not reliably recover true expression changes under these conditions and should not be used as the primary estimator without modification, additional replicates, or a different prior/model.**

### 13.3 Ambiguous conclusion

If the evaluation shows:

- improved simulation RMSE but poor independent validation;
- good suppression of false extremes but meaningful loss of low-information true strong effects;
- acceptable average performance but strong sensitivity to prior-width estimation;
- improvement only in some datasets or simulation scenarios;

then the conclusion is:

**The method is conditionally useful but not universally reliable. It may be appropriate for ranking and cautious inference, but strong biological claims require more replicates, heavier-tailed priors, spike-in controls, or independent validation.**

---

## 14. Methods-direction forecast versus reproduction of published biological results

This proposal is a **methods-direction forecast**, not a reproduction.

### Methods-direction forecast

A methods-direction forecast says:

> Given the packet’s evidence that low-count estimates are unstable and that information sharing with a Normal prior stabilizes dispersion and fold-change estimates, we expect the proposed shrinkage method to reduce false extremes and improve low-information accuracy, provided the prior is not too aggressive and the count model is adequate.

This forecast is testable but has not been tested here.

### Actual reproduction of published biological results

An actual reproduction would require:

1. the original published raw reads or equivalent raw data;
2. the exact biological comparison;
3. the original sample metadata;
4. the original software, parameters, or a faithful reimplementation;
5. the published target result, such as a gene list, fold-change table, pathway result, or biological claim;
6. explicit success criteria for matching that result.

None of those are supplied here. Therefore, no published biological result is being reproduced, and no gene list, pathway, or treatment effect should be interpreted as reproduced.

---

## 15. Assumptions, unreported parameters, and limitations

### Assumptions

1. The count model is sufficiently correct for the data.  
2. Biological replicates within a condition are exchangeable except for modeled covariates.  
3. Dispersion can be meaningfully shared across genes.  
4. A zero-centered Normal prior is a reasonable default for effects.  
5. Library-size normalization is adequate.  
6. Independent validation measures the same gene-level quantity as RNA-seq.  
7. Simulated data capture important features of real noise.

### Unreported parameters that must be specified

- prior width \(\tau\);
- dispersion trend parameters;
- normalization factors;
- gene filtering thresholds;
- information-score definition;
- discovery posterior probability threshold;
- minimum fold-change threshold, if used;
- simulation effect-size distributions;
- number of simulated genes and replicates;
- random seeds;
- qPCR reference genes and efficiency corrections;
- spike-in concentrations and fold-change definitions.

### Limitations

1. The packet does not specify the true distribution of biological effects.  
2. Zero-centered Normal shrinkage may bias rare true large effects.  
3. Simulations may not capture unknown biological heterogeneity.  
4. Independent validation may be limited by assay sensitivity.  
5. Gene-level analysis ignores isoform-level changes.  
6. Batch effects or hidden confounders can invalidate both shrunk and unshrunk estimates.  
7. With very few replicates, even shrinkage cannot fully compensate for weak experimental design.

---

## 16. Alternatives if the proposed method fails

1. **Use unshrunk estimates with stricter filtering**  
   This may preserve extreme effects but will likely retain more low-count false positives.

2. **Use a heavier-tailed prior**  
   If true effects include rare large changes, a heavier-tailed prior may protect them better than a Normal prior. This is an alternative beyond the supplied starting point and would need separate evaluation.

3. **Use spike-in-informed priors**  
   If spike-ins are available, they can help calibrate expected noise and effect sizes.

4. **Increase biological replication**  
   More replicates directly reduce reliance on shrinkage.

5. **Model batch or random effects explicitly**  
   If instability arises from hidden structure, shrinkage alone will not solve the problem.

6. **Validate at the gene-set level**  
   If individual low-count genes are too unstable, gene-set or module-level validation may be more robust.

---

## Final recommendation

Proceed with the information-sharing Normal-prior count-model estimator, but only as part of a pre-registered evaluation. The method should be accepted only if it demonstrates: reduced unstable low-information extremes, improved fold-change accuracy or stability, calibrated uncertainty, preservation of strong high-information effects, and support from spike-in, qPCR, or independent replicate validation. Without such evidence, the method remains a plausible but unverified approach, and no biological reproduction claim should be made.
