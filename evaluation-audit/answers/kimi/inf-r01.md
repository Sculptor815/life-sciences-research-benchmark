# Kimi K3 / inf-r01

Original final answer, shared by both scoring rounds.

# Recommended next action

Conduct a locked, three-part benchmark rather than assuming that shrinkage has recovered biological truth:

1. Fit an empirical-Bayes count model that shrinks dispersions and treatment effects toward distributions learned across genes.
2. Test it in high-replicate downsampling and simulations that deliberately violate the assumed Normal effect distribution.
3. Validate locked discovery calls in an independent cohort and, where feasible, with an orthogonal expression assay.

The directional, testable forecast is that shrinkage will reduce unstable low-count fold-change extremes while leaving high-information strong effects close to their unshrunk estimates. This is a methods hypothesis, not an observed result. No published biological result is reproduced here.

---

## 1. Unresolved biological question

Within an eligible treatment-versus-control bulk RNA-seq experiment with few biological replicates:

> **Does the perturbation induce a reproducible, coordinated transcriptional change in an investigator-prespecified response pathway, and which genes support that change, rather than the apparent response being dominated by isolated effects or unstable low-count fold changes?**

The primary estimand is the conditional gene-level log-fold change associated with treatment among independent biological samples, adjusted for prespecified design variables. For bulk tissue, this is an average over the sampled cell mixture; it is not automatically a change in expression within a fixed cell type.

A pathway should be used only if it and its gene membership are specified before examining treatment effects. Otherwise the safer primary question is gene-level reproducibility, with pathway interpretation deferred.

### Competing explanations and distinct predictions

| Mechanism | Expected pattern in discovery data | Expected validation pattern |
|---|---|---|
| **M1. Coordinated biological program** | Multiple pathway genes change concordantly; effects are distributed across sufficient expression levels and remain directionally stable across replicates | Direction and approximate magnitude reproduce in independent samples and orthogonal measurements |
| **M2. Sparse direct response** | A small number of high-information genes have strong effects; little coordinated pathway signal | Those genes reproduce, but pathway-level enrichment does not |
| **M3. Count-sampling or processing noise** | Largest unshrunk fold changes are concentrated among low counts, high standard errors, zero-count patterns, or inconsistent replicates | Extremes shrink toward zero and fail independent replication |
| **M4. Batch, annotation, or sample-quality artifact** | Effects align with processing batch, lane, mapping rate, duplication, contamination, or other technical variables | Effects disappear after balanced processing or fail in a differently processed cohort |
| **M5. Cell-composition shift** | Apparent pathway changes track cell-type marker composition | Signal is attenuated after composition-aware validation, sorted-cell measurements, or single-cell resolution, if such data are available |

These mechanisms are not mutually exclusive.

---

## 2. Evidence-to-inference-to-conclusion chain

| Evidence in the supplied packet | Defensible inference | Conclusion for this study |
|---|---|---|
| Gene-level expression differences are estimated with a count model | Count size, overdispersion and sampling design should affect uncertainty | Ratios of normalized counts alone are insufficient |
| With few biological replicates, low or variable counts can produce unstable fold changes | The largest observed fold changes need not be the largest true effects | Ranking by unshrunk fold change is vulnerable to noise |
| The method shares information across genes to stabilize dispersions and fold changes | Common mean–dispersion structure and effect variability can regularize low-information estimates | Empirical-Bayes shrinkage is a reasonable primary estimator |
| A Normal prior is placed on effects | Effects with weak likelihood support will be pulled toward the prior center, while sufficiently precise effects can remain close to their data estimates | Shrinkage should be tested separately for strong/high-information and extreme/low-information genes |
| The packet does not establish the true distribution of biological effects | A Normal prior may be misspecified when effects are sparse, asymmetric, multimodal or heavy-tailed | Simulations must include effect distributions that violate the prior, followed by independent validation |

Thus, the warranted conclusion is: **use shrinkage prospectively as the primary effect estimator, but make strong-effect preservation and low-information-extreme rejection explicit falsification tests.** Do not equate a large shrunken estimate with biological truth without independent support.

---

## 3. Proposed estimation method

The following is an explicit operationalization compatible with the packet. The packet does not specify every distributional or implementation detail, so these are proposed assumptions, not reported evidence.

### 3.1 Count model

For gene \(g\) and biological sample \(i\), model the observed count as

\[
Y_{gi}\sim \operatorname{NB}(\mu_{gi},\alpha_g),
\]

\[
\log(\mu_{gi})=\log(s_i)+x_i^{T}\beta_g,
\]

where:

- \(s_i\) is a sample-specific size or normalization factor;
- \(x_i\) contains treatment and prespecified covariates;
- \(\alpha_g\) is the gene-specific dispersion;
- the treatment coefficient \(\beta_{g,T}\) is converted to a log2 fold change for reporting.

Estimate dispersions gene by gene, fit a mean-dependent dispersion trend across genes, and use shrunken dispersion estimates that balance gene-specific data with that trend.

### 3.2 Fold-change shrinkage

Place a zero-centered Normal prior on the treatment effect:

\[
\beta_{g,T}\sim N(0,\tau^2),
\]

with \(\tau^2\) estimated from the distribution of effects across genes. Report the posterior mean or mode as the primary magnitude estimate.

The intended operating characteristic is:

- a gene with a precise likelihood should remain close to its unshrunk estimate;
- a gene with a large standard error should be pulled more strongly toward zero.

This is a model-based expectation, not evidence that preservation will occur in every dataset.

### 3.3 Testing versus estimation

Use the count model to obtain an unregularized treatment test statistic or another prespecified uncertainty measure. Use the shrunken coefficient primarily for:

- effect-size reporting;
- ranking;
- visualization;
- selection of genes for validation.

This avoids treating a shrunken estimate and an unadjusted testing procedure as interchangeable. Multiple-testing control may be applied with a locked procedure, but an adjusted \(P\)-value alone should not establish biological relevance.

Genes with all-zero counts, or with no variation that permits estimation, are not interpretable differential-expression candidates. Minimal filtering may remove unidentifiable genes, but low-expressed genes should otherwise be retained and flagged by information level rather than silently equated with absent biology.

---

## 4. Complete proposed protocol

### Stage A. Preregistration and analysis lock

Before examining treatment outcomes:

1. Define the biological system, treatment contrast, pathway hypothesis and eligible sample population.
2. Specify the biological unit of replication. Technical replicates or cells from one biological sample must not be counted as independent biological replicates.
3. Define the primary gene-level endpoint and the secondary pathway endpoint.
4. Lock preprocessing, filtering, model formula, shrinkage implementation, simulation scenarios and validation metrics.
5. Declare that this is a methods benchmark with a conditional biological analysis, not a reproduction of an unpublished or unavailable result.

No prior evaluation feedback is assumed. Thresholds below are proposed decision criteria, not established biological constants.

### Stage B. Dataset eligibility

Use three classes of data when available.

#### B1. High-replicate benchmark dataset

Include a treatment-control dataset with:

- at least approximately eight independent biological replicates per condition, as an operational high-information benchmark;
- raw reads available;
- comparable biological material and a documented design;
- enough samples to create a high-replication reference and repeatedly downsample to three to five replicates per condition.

The eight-replicate boundary is an operational benchmark choice, not a claim that eight samples reveal absolute truth.

#### B2. Target low-replication dataset

Include the biologically relevant low-replication setting, preferably three to five biological replicates per condition, matching the instability problem described in the packet.

#### B3. Independent validation dataset or assay

Use an independent biological cohort subjected to the same perturbation in a comparable system. If no transcriptome-wide cohort exists, use a targeted orthogonal expression assay on newly collected independent samples.

#### Exclusion criteria

Exclude a dataset from the primary benchmark if:

- raw reads or sample-to-run provenance are unavailable;
- treatment is completely confounded with sequencing batch;
- replicates are technical rather than biological;
- sample identity cannot be resolved;
- library protocol or reference genome is undocumented;
- objective prespecified QC failure, contamination or duplication cannot be corrected;
- the independent validation system is too biologically different to test the same question.

A processed count matrix without raw-read provenance may be used only in sensitivity analyses.

### Stage C. Raw-read provenance

Create an immutable manifest containing:

- study and run accessions or internal file identifiers;
- sample-to-run mapping;
- download or generation date;
- file checksums;
- biological and technical replicate labels;
- treatment, batch, lane, library type, read length and strandedness;
- reference genome and annotation versions;
- every preprocessing command and software version;
- random seeds and execution environment.

Retain raw files unchanged. Record whether reads were merged, trimmed, filtered, aligned or directly quantified, and how ambiguous or multi-mapping reads were assigned to genes. The output should be a gene-by-biological-sample count matrix linked to the manifest.

### Stage D. Blind QC

Before fitting the treatment model:

1. Inspect read depth, mapping or assignment rate, duplication, contamination, detectable gene count and sample clustering.
2. Check that treatment is not inseparable from batch or processing date.
3. Apply only prespecified exclusion rules.
4. Examine whether QC variables correlate with treatment after modeling.
5. Retain QC-failed samples in an auditable exclusion table rather than deleting them without documentation.

Do not use the resulting differential-expression calls to decide retrospectively which samples “look correct.”

### Stage E. Primary estimation

For each dataset:

1. Estimate normalization factors.
2. Fit the count model using treatment plus prespecified covariates.
3. Estimate and shrink gene dispersions.
4. Estimate the empirical effect-prior variance.
5. Produce unshrunk and shrunken treatment log2 fold changes with uncertainty.
6. Classify genes by mean normalized count and coefficient standard error before examining validation.
7. Store the model fit, null and alternative test statistics, prior variance, dispersion estimates and complete software state.

If a balanced batch variable exists, include it in the design. If batch and treatment are confounded, estimate only a descriptive contrast and mark causal or treatment-specific interpretation as unsupported.

### Stage F. High-replication reference and downsampling

1. Fit the same model to all eligible high-replicate samples to create an internal reference.
2. Define reference strong effects using both magnitude and precision, not magnitude alone.
3. Repeatedly draw nonoverlapping subsets of three to five samples per condition without replacement.
4. Run the identical low-replication pipeline on each subset.
5. Compare unshrunk and shrunken estimates with the reference.

This tests small-sample behavior, but it is not fully independent validation because the reference and subsets arise from the same experiment and platform.

### Stage G. Simulation

Use fitted means, dispersions and library-size patterns from real eligible data so that simulations retain realistic count noise.

For each simulation replicate:

1. Draw baseline expression and dispersion values from the fitted empirical parameter collection.
2. Assign true treatment effects under several locked scenarios:
   - all-null calibration;
   - Normal effects, matching the prior;
   - sparse effects, with most genes null and a small fraction moderate or strong;
   - a heavy-tailed mixture containing rare large effects;
   - a coordinated pathway scenario with several concordant moderate effects;
   - a scenario with additional dispersion heterogeneity or outlier samples.
3. Generate counts under the proposed count model and observed design.
4. Rerun the full estimation pipeline, including estimation of the prior variance from each simulated dataset.
5. Repeat until Monte Carlo uncertainty is sufficiently small; an initial target of 1,000 replicates is reasonable if computationally feasible.

The non-Normal scenarios are essential because the packet does not establish that actual biological effects are Normal.

### Stage H. Independent validation

Freeze all discovery calls before validation.

Select validation genes from prespecified strata:

- strong, high-information effects retained after shrinkage;
- strong effects that shrink materially;
- extreme unshrunk low-information effects;
- pathway genes with moderate effects;
- null or stable-control genes;
- genes spanning low, medium and high expression.

Include both directional candidates and controls so that validation does not test only the most favorable calls.

For an independent RNA-seq cohort, use the same contrast and a locked definition of replication, while allowing for genuine effect-size heterogeneity. For targeted assays, use independent biological samples, blinded sample labels where feasible and prespecified normalization controls.

If cell-composition change is plausible, add a composition-sensitive validation layer—for example, sorted-cell measurements or independently annotated cell-type-resolved data. If those data are unavailable, composition remains an explicit limitation rather than being ruled out.

---

## 5. Testing strong-effect preservation without accepting noisy extremes

### 5.1 Reference strong-effect set

Define strong high-information reference genes before low-replication analysis. An example operational definition is:

- absolute reference log2 fold change at least 1;
- sufficiently small reference standard error;
- adequate normalized count;
- consistent sign across independent reference subsets.

The two-fold threshold is an arbitrary operational benchmark. Repeat the analysis at lower and higher effect thresholds to determine whether conclusions depend on that choice.

### 5.2 Preservation metrics

For the strong reference set, calculate:

- sign retention;
- median signed ratio of low-replicate shrunken estimate to reference estimate;
- absolute error and mean squared error;
- interval coverage;
- proportion of reference strong genes excluded from the candidate list;
- rank correlation among strong genes.

A proposed clear-preservation criterion is median signed recovery near unity, with the lower confidence limit compatible with no more than modest attenuation—for example, a median recovery of at least 0.8—together with high sign agreement. This threshold is a testable benchmark, not a universal standard.

### 5.3 Low-information-extreme set

Separately define genes with:

- large absolute unshrunk fold changes;
- high coefficient standard errors, low normalized counts or near-zero counts in one condition.

For these genes, calculate:

- amount of shrinkage;
- change in rank;
- replication across resamples;
- independent-cohort validation;
- false-extreme rate in simulations.

A large unshrunk fold change must not be accepted as a strong biological effect merely because it is extreme. Candidate status requires adequate information, stable direction across biological replicates and independent support. In particular, an all-zero treatment group can generate a very large ratio but may provide little information about the magnitude of the change.

### 5.4 Decisive comparison

Success requires both:

1. high-information strong effects are not systematically collapsed toward zero; and
2. low-information extremes are less likely to be called or validated after shrinkage.

If only the second condition holds, the method is conservative but does not demonstrate preservation of strong biology. If only the first holds, it may still be rewarding unstable extremes.

---

## 6. Evaluation metrics

### Gene-level estimation

- Bias and mean squared error against simulated truth.
- Signed error against high-replicate reference.
- Standard-error calibration and interval coverage.
- Sign-error and exaggerated-magnitude rates.
- Sensitivity and false-discovery proportion for true effects.
- Results stratified by expression, dispersion and information level.

### Strong-effect preservation

- Recovery of strong reference effects.
- Sign concordance.
- Attenuation as a function of count and standard error.
- Performance under sparse and heavy-tailed simulated effects.

### Low-information robustness

- Fraction of extreme unshrunk calls removed or reduced by shrinkage.
- Validation rate of extreme calls before and after shrinkage.
- Null simulation false-positive behavior.
- Stability across resampling.

### Biological hypothesis

- Reproducibility of individual candidate genes.
- Concordance of prespecified pathway effects.
- Independence from batch and QC variables.
- Robustness to cell-composition-sensitive analyses where possible.

---

## 7. Planned figure and table sequence

All figures below are planned outputs; none is being claimed as already generated.

1. **Dataset provenance flow diagram**  
   Eligible datasets, excluded samples, reasons for exclusion and final biological replicate counts.

2. **QC and design plot**  
   Library depth, assignment rate, batch and treatment relationships, demonstrating whether the contrast is identifiable.

3. **Dispersion diagnostic**  
   Gene-wise, trend and shrunken dispersion estimates against mean expression.

4. **Unshrunk-versus-shrunk MA plot**  
   Effect estimates against mean normalized count, with low-information genes visually distinguished.

5. **Shrinkage calibration plot**  
   Shrinkage amount versus coefficient standard error and mean count.

6. **Strong-effect retention plot**  
   Low-replicate estimates against high-replicate reference estimates for prespecified strong genes.

7. **Extreme-call fate plot**  
   Shows whether low-information unshrunk extremes move toward zero, remain extreme and/or validate independently.

8. **Simulation performance panels**  
   Error, calibration, sign error, false discovery and strong-effect retention across Normal, sparse, heavy-tailed and pathway scenarios.

9. **Independent validation concordance plot**  
   Discovery estimates against independent estimates, with confidence intervals and validation strata.

10. **Biological interpretation figure**  
    Prespecified pathway effects shown with uncertainty, not as a pathway picture inferred after selecting significant genes.

The accompanying machine-readable tables should include counts, unshrunk and shrunken effects, standard errors, test results, simulation truth where applicable and validation outcomes.

---

## 8. Conditional conclusions

### Positive methodological conclusion

Conclude that the shrinkage procedure is fit for this estimation setting if:

- low-replicate shrunken estimates have lower error and fewer sign reversals than unshrunk estimates;
- strong high-information effects are preserved within the prespecified recovery bounds;
- extreme low-information calls are reduced without a comparable loss of validated strong effects;
- calibration remains acceptable under simulations that violate the Normal prior;
- locked calls reproduce independently.

This would support the method for estimation and prioritization, not prove that every individual shrunken estimate is true.

### Positive biological conclusion

Conclude that the perturbation produces a coordinated response only if:

- multiple prespecified pathway genes change concordantly;
- the result is not explained by batch or QC structure;
- key genes reproduce independently;
- the signal is not adequately explained by cell-composition change;
- the pathway conclusion remains after sensitivity analysis.

A positive biological conclusion can occur even if shrinkage performs poorly, provided the evidence comes from stable high-information and independently validated effects.

### Negative methodological conclusion

Reject or revise the shrinkage implementation if:

- true strong effects are materially attenuated or reordered;
- intervals are overconfident;
- a small number of strong genes causes the shared prior to misfit other genes;
- apparent gains arise only under simulations that exactly match the Normal prior;
- low-information extremes still dominate calls or validation failures.

### Negative biological conclusion

Do not claim a treatment program if the apparent effects:

- concentrate in low-information genes;
- disappear under shrinkage and resampling;
- align with batch or processing variables;
- fail independent replication.

### Ambiguous conclusion

The result is ambiguous if:

- simulation performance is good but independent validation is poor;
- high-replicate and independent references disagree;
- only a few strong genes validate;
- pathway effects validate but composition cannot be examined;
- shrinkage preserves strong effects but produces poorly calibrated uncertainty;
- independent samples show the same direction with materially different magnitudes.

Ambiguity should trigger design improvements or additional biological replication, not post hoc threshold selection.

---

## 9. Alternatives and limits

### Alternatives

- **Unshrunk count-model estimation:** preserves the data’s direct estimate but leaves low-count rankings vulnerable to extreme sampling error.
- **Low-count filtering:** removes some unstable estimates but can discard biologically real low-expression effects.
- **Pseudocount fold changes:** produce finite ratios but impose arbitrary bias and do not create information.
- **Flexible or mixture priors:** may represent sparse or heavy-tailed effects better, but such performance is not established by the packet and would require a separate benchmark.
- **Independent evidence only:** targeted validation can adjudicate a small number of candidates but cannot by itself repair transcriptome-wide instability.

### Principal limits

1. **Prior misspecification:** A zero-centered Normal prior may be inappropriate for sparse, asymmetric, multimodal or globally shifted effects.
2. **Intentional bias:** Shrinkage trades unbiasedness of individual estimates for potentially lower overall error; a true low-information strong effect can still be over-shrunk.
3. **Information floor:** Low counts cannot support arbitrarily precise fold changes. Shrinkage stabilizes estimates but does not create missing biological information.
4. **Reference imperfection:** High-replicate estimates are references, not absolute truth.
5. **Simulation dependence:** Simulations based on the fitted count model may miss alignment, annotation or library-preparation artifacts.
6. **Confounding:** No shrinkage method can separate treatment from a completely confounded batch.
7. **Bulk composition:** A gene-level change can reflect altered cell proportions rather than regulation within cells.
8. **Relative measurement:** RNA-seq contrasts relative abundance; global changes in total RNA or composition may complicate interpretation.

---

## 10. Forecast versus reproduction

This proposal is a **methods-direction forecast**: the supplied rationale predicts that sharing information across genes should improve stability, while a zero-centered Normal prior should preferentially restrain low-information effects. The proposed benchmark would test that forecast.

It is **not an actual reproduction of published biological results**, because the evidence packet supplies neither:

- a named published dataset;
- its raw files and original analysis state;
- reported effect estimates or biological calls;
- an original numeric result against which output can be compared.

A genuine reproduction would require the original study’s data, protocol, versions and stated endpoints, followed by comparison of regenerated outputs with reported values. Here, all performance and biological conclusions remain prospective until the specified data, simulations and independent validation are completed.
