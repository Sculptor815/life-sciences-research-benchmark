# GPT-5.6 Terra / inf-r01

Original final answer, shared by both scoring rounds.

# Proposed question, conclusion, and scope

**Biological question.**  
In a defined tissue or cell system, does condition A versus matched condition B produce reproducible, gene-specific changes in bulk RNA abundance—especially biologically material large effects—or are apparently large fold changes primarily consequences of low counts, variable sampling, or changes in sample composition?

**Recommended next action.**  
Use a pre-specified count-model analysis with dispersion and fold-change shrinkage as a **methods-direction workflow**, then test its ability to preserve real strong effects and suppress unstable low-information extremes using (i) simulations with known truth and (ii) independently generated biological data. The supplied packet supports this workflow, but does **not** establish that a Normal prior is the true distribution of biological effects, nor does it provide a dataset or any published biological result to reproduce.

This is therefore a **proposed independent protocol and forecast**, not a report of observed results.

---

# 1. Competing biological and technical explanations

## Unresolved biological question

The central biological uncertainty is whether condition A changes RNA abundance within cells, changes the mixture of cells contributing RNA, or produces no reproducible expression change beyond sampling and technical variation.

## Competing explanations and predictions

| Explanation | Biological/technical mechanism | Prediction in discovery and independent validation |
|---|---|---|
| **H1: Reproducible condition-responsive regulation** | The condition changes RNA abundance of particular genes within the sampled biological system. | Estimated effects retain their direction and approximate magnitude in independent biological samples; strong, well-measured effects remain large after shrinkage; orthogonal measurements agree. |
| **H2: Altered cellular composition** | The condition changes the proportions of constituent cell types or states, creating bulk RNA differences without necessarily changing expression within a given cell type. | Bulk effects can reproduce, but they covary with independently measured composition. Bulk RNA-seq alone cannot distinguish this explanation from cell-intrinsic regulation. |
| **H3: Sampling/estimation instability** | Low counts, variable counts, few replicates, or technical artifacts create extreme estimated fold changes. | Large effects are concentrated among low-information genes, vary under resampling of biological replicates, shrink strongly toward zero, and fail to reproduce in independent samples. |
| **H4: A broad or asymmetric biological response not well represented by the prior** | Many genes change in one direction, or the true effect distribution is not approximately centered Normal. | A centered Normal prior may over-shrink genuine effects or distort their ranking; simulations representing these alternatives reveal excess bias or loss of sensitivity. |

The analysis can discriminate H1 from H3 more directly than it can discriminate H1 from H2. A reproducible bulk RNA difference is not, by itself, proof of cell-intrinsic transcriptional regulation.

---

# 2. Evidence-to-inference-to-conclusion chain

## Fixed evidence

1. RNA-seq differential expression analysis uses a gene-level **count model**.
2. With few biological replicates, low or variable counts can produce unstable fold-change estimates.
3. Dispersion and fold-change estimates can be stabilized by sharing information across genes.
4. A Normal prior on effects can shrink noisy fold changes.
5. The packet provides **no evidence** that all real biological effects follow a Normal distribution or any other single distribution.

## Inferences justified by that evidence

1. Unshrunk gene-wise fold changes should not be treated as equally reliable across genes.
2. Shrinkage is expected to reduce variance for weakly informed estimates.
3. Shrinkage can also bias genuine effects toward zero, particularly if the prior is too restrictive or the data are weak.
4. Therefore, effect recovery must be evaluated separately for:
   - high-information, truly strong effects;
   - weak or near-null effects;
   - low-information genes with apparently extreme estimates; and
   - biological settings that depart from the assumed prior shape.

## Conclusion

The justified conclusion at this stage is methodological: **a shrinkage estimator is a plausible candidate for improving recovery of real expression changes from noisy counts, but it must demonstrate both strong-effect preservation and low-information error control before it supports biological claims.**

---

# 3. Pre-specified protocol

## Definitions to lock before inspecting condition-specific results

The following parameters are not supplied in the packet and must be documented before final inference:

- **Biological materiality threshold, \(L\):** the smallest absolute log fold change regarded as biologically meaningful in this system.
- **Information criterion, \(I\):** a pre-specified criterion based on average expression, estimated precision, dispersion, and replicate support—not on the observed sign of the effect—for classifying estimates as high or low information.
- **Stability criterion, \(S\):** the required consistency of effect sign and magnitude across biological-replicate resampling.
- **Validation agreement margin, \(V\):** the pre-specified acceptable discrepancy between discovery and validation effect estimates.
- **Inclusion/exclusion and filtering rules:** especially how very low-expression genes are labeled as uninformative rather than silently treated as unchanged.
- **The count-model implementation:** the evidence packet says “count model” but does not state its exact likelihood, normalization method, estimator, uncertainty procedure, or prior-width fitting procedure.

No numerical cutoff should be chosen after examining which genes appear biologically interesting.

---

## Step 1 — Dataset eligibility

A dataset is eligible for the full protocol only if all of the following are available.

### Required biological design information

1. A clearly defined condition A versus B contrast.
2. Biological replicates, not merely repeated sequencing of the same biological material.
3. Sample-level metadata containing, as applicable:
   - condition assignment;
   - biological replicate identity;
   - tissue/cell source;
   - collection time;
   - extraction and library-preparation batch;
   - sequencing run;
   - known covariates such as sex, genotype, donor, or paired subject;
   - any evidence relevant to cell composition.
4. A design in which condition is not perfectly confounded with batch, run, or another technical variable.

If all condition-A samples were prepared in one batch and all condition-B samples in another, the data may describe a difference but cannot support a clean causal claim about the condition. Modeling cannot fully repair perfect confounding.

### Required data availability

- Original raw reads or an equivalent archived primary read source.
- A sample sheet mapping each read file to one biological specimen.
- Reference genome/transcriptome and gene annotation versions.
- Sufficient biological material for an independent validation set, either already held out or newly collected.

### Eligibility decision

- **Eligible for discovery plus validation:** raw reads, complete provenance, balanced metadata, and independent biological samples are available.
- **Eligible only for exploratory reanalysis:** a count matrix is available but raw-read provenance or independent samples are unavailable.
- **Ineligible for a causal biological conclusion:** condition is confounded with technical factors, sample identity is uncertain, or replicates are technical rather than biological.

The fixed packet does not specify a minimum number of replicates. Thus, the exact minimum is an unreported design parameter. If the number is too small to split data into discovery and validation while retaining meaningful estimation, new samples are required.

---

## Step 2 — Raw-read provenance and processing record

Construct a read-provenance manifest before differential expression fitting. For every sample, record:

1. archive accession or local source identifier;
2. read-file names and checksums;
3. specimen identifier and biological replicate identifier;
4. condition label and all known covariates;
5. library preparation, read layout, sequencing run, and lane;
6. reference and annotation versions;
7. read-processing, alignment/quantification, and gene-counting settings;
8. exclusions, with reasons decided without reference to desired biological results.

### Proposed quality-control checks

- Verify that all files match the manifest and that sample labels are internally consistent.
- Check read quality, adapter contamination, mapping/assignment rates, gene-body or positional bias if relevant, duplicated samples, and outlying library composition.
- Examine library size and expression-profile clustering against batch and condition.
- Confirm that a technical outlier is not actually an unrecorded biological subgroup before exclusion.
- Freeze the gene-count matrix and sample metadata used for analysis.

These checks establish data provenance and technical suitability; they do not establish that an observed expression difference is biologically causal.

---

## Step 3 — Discovery/validation separation

Before model fitting, partition samples and analyses as follows.

### Preferred design: newly generated independent validation

Use independently collected biological specimens from the same defined system, processed in a separate extraction/library/sequencing workflow where feasible. This best tests biological reproducibility.

### Acceptable intermediate design: held-out biological replicates

If enough pre-existing biological replicates exist, hold out specimens before fitting. They must be distinct organisms, donors, cultures, or biological preparations—not technical sequencing replicates.

### Insufficient substitute

Reprocessing the same reads, resequencing the same library, or changing software settings is not independent biological validation. It can assess technical robustness but not reproducibility of the biological contrast.

---

## Step 4 — Count-model estimation

For gene \(g\) in sample \(i\), use the selected count-model implementation with an expected count of the general form

\[
E(K_{gi}) = s_i \exp(\alpha_g + x_i\beta_g + {\bf z}_i^\mathsf{T}{\boldsymbol\gamma}_g),
\]

where:

- \(K_{gi}\) is the observed gene count;
- \(s_i\) is a library-size or normalization offset;
- \(x_i\) encodes condition A versus B;
- \(\beta_g\) is the condition-associated log fold change;
- \({\bf z}_i\) represents non-confounded recorded covariates;
- gene-specific dispersion controls variability beyond the mean in the count model.

This equation is a proposed model skeleton consistent with the supplied count-model rationale. The precise likelihood and normalization method are **not stated in the evidence packet** and must be recorded rather than assumed.

### Required estimation outputs

For every analyzed gene, retain:

1. a gene-wise, unshrunk effect estimate where estimable;
2. a shrunken effect estimate;
3. the estimated dispersion and its stabilized/shrunk form;
4. an uncertainty measure if the selected method supplies one;
5. average normalized expression and other pre-specified information measures;
6. a flag for genes whose data are insufficient for stable estimation.

### Shrinkage specification

The proposed estimator shares information across genes to stabilize dispersion and applies a centered Normal prior to effects:

\[
\beta_g \sim N(0,\tau^2).
\]

The packet supports the rationale for this prior as a stabilizer, not as a demonstrated law of biology. The fitting method for \(\tau\), the handling of outliers, and the exact posterior or penalized estimator are not supplied and must be fixed and reported.

### Important comparison

Retain the unshrunk estimate as a **diagnostic comparator**, not as ground truth. The comparison reveals where shrinkage changes results and whether those changes occur primarily in low-information genes, as intended.

---

## Step 5 — Rule for strong effects and low-information extremes

The workflow must avoid the two opposite errors:

- over-shrinking genuinely large, well-supported effects; and
- accepting dramatic estimates based mainly on low counts or a single unstable replicate.

### Pre-specified evidence classes

| Class | Definition | Interpretation |
|---|---|---|
| **High-confidence material effect** | Absolute shrunken effect exceeds \(L\), information exceeds \(I\), biological-replicate stability satisfies \(S\), and independent validation meets \(V\). | Supported reproducible difference in bulk RNA abundance. |
| **Candidate material effect** | Effect exceeds \(L\), but validation is pending or information/stability is incomplete. | Hypothesis for follow-up, not a confirmed result. |
| **Low-information extreme** | Large unshrunk or shrunken effect but fails \(I\) or \(S\). | Do not accept as a biological hit; retain for targeted validation because a real rare/low-expression effect remains possible. |
| **Insufficient information** | Counts or model support do not permit stable estimation. | Not evidence of no change. |
| **No supported material effect** | Data are sufficiently informative but do not support an effect of at least \(L\). | Conditional negative evidence, not proof of exact equality. |

### Specific test of strong-effect preservation

Strong effects will be assessed in two complementary ways:

1. **Known-truth simulations:** among simulated genes with true \(|\beta_g| \geq L\) and high information, measure shrinkage-induced bias, sign recovery, ranking, and sensitivity.
2. **Independent biological validation:** validate the union of:
   - genes with large shrunken effects; and
   - genes with large unshrunk effects that were strongly attenuated by shrinkage.

The union is essential. Validating only genes retained after shrinkage would fail to detect genuine large effects that the prior had incorrectly suppressed.

Low-information extremes will not be accepted merely because they are numerically large. They may be selected for targeted validation, but remain candidates unless they meet the pre-specified stability and validation criteria.

---

## Step 6 — Simulation study with known truth

Simulation is needed because independent biological validation alone does not reveal the true effect for every gene.

### Simulation construction

Use the fitted discovery count model, observed library-size structure, and estimated dispersion behavior as a basis for generating synthetic count data. Assign known true effects \(\beta_g\) before generating counts, then rerun the complete pipeline blindly.

This is a **model-based performance experiment**, not a claim that simulated effects reproduce the true biology.

### Required truth scenarios

Because the packet gives no evidence for a universal effect distribution, evaluate several deliberately distinct scenarios:

1. **Global null:** all true effects are zero.
2. **Sparse effects:** few nonzero genes, including a subset with \(|\beta_g| \geq L\).
3. **Many modest effects:** broad but weak condition response.
4. **Strong effects in high-information genes.**
5. **Strong effects in low-information genes.**
6. **Asymmetric effects:** more positive than negative, or the converse.
7. **Non-Normal or mixture-like effect patterns:** for example, many nulls plus a small strong-effect component.
8. **Dispersion and library-size conditions spanning the observed range.**
9. **Stress conditions departing from the fitted assumptions**, clearly labeled as stress tests rather than inferred biology.

### Metrics

For each scenario, stratified by expression information and true effect magnitude, estimate:

- bias: \(\hat{\beta}_g-\beta_g\);
- root-mean-square error;
- sign accuracy;
- sensitivity for true material effects, \(|\beta_g| \geq L\);
- false acceptance rate for null or low-information extreme genes;
- ranking performance for true strong effects;
- uncertainty calibration and interval coverage, if intervals are provided by the implementation;
- stability under resampling biological replicates.

### Falsifiable performance criteria

Before looking at real biological results, define acceptable margins for:

1. loss of sensitivity for high-information true strong effects;
2. maximum bias tolerated for those effects;
3. reduction in false large-effect calls among low-information null genes relative to the unshrunk estimator;
4. calibration of uncertainty estimates, if available.

The packet does not provide acceptable numerical margins. They must be justified by the biological decision context and fixed before execution.

A method would fail the intended use if it reduces low-count extremes but also systematically erases known strong effects in high-information simulated data.

---

## Step 7 — Independent validation

### Validation sample design

Use independent biological samples matched as closely as possible to the discovery population, with condition assignment, processing date, batch, and sample identity documented prospectively.

A useful validation panel includes:

1. randomly sampled high-confidence discovery candidates;
2. the strongest shrunken effects;
3. strongly attenuated unshrunk effects;
4. low-information extremes;
5. genes estimated near zero;
6. randomly selected genes across the information range.

The random component prevents validation from being restricted to visually attractive or biologically familiar genes.

### Validation measurements

Two complementary validation routes are proposed:

- **Independent RNA-seq** on newly collected biological samples, analyzed under the locked count-model protocol.
- **Orthogonal targeted RNA measurement** on independent samples for the selected panel.

The latter is useful for checking that the result is not specific to the original sequencing/counting workflow. It remains a measurement of RNA abundance, not necessarily transcription rate.

### Tests

For each selected gene, assess:

- agreement of effect direction;
- agreement in magnitude within the pre-specified margin \(V\);
- whether high-information strong effects remain material;
- whether low-information extremes disproportionately fail replication;
- comparative prediction from shrunken versus unshrunk discovery estimates.

If composition is a central alternative explanation, obtain an independent composition measurement or a design that isolates relevant cell populations. Without that information, a reproducible bulk effect should remain interpreted as a bulk RNA-abundance difference.

---

# 4. Planned figures and their interpretation

## Figure 1 — Data provenance and design

A flow diagram from source reads to final samples and count matrix, with exclusions and reasons.

**Interpretation:** establishes traceability and guards against sample-label or provenance failures. It does not support differential-expression conclusions by itself.

## Figure 2 — Count and dispersion behavior

Plots of mean expression versus dispersion before and after information sharing, plus distribution of library sizes and sample-level QC.

**Interpretation:** shows whether the stabilization target is relevant to the data and whether broad quality differences coincide with condition.

## Figure 3 — Shrinkage diagnostic

For each gene, plot shrunken against unshrunk fold change, colored or faceted by information level.

**Expected useful pattern:** large changes in estimates occur mostly for low-information genes; high-information strong estimates remain comparatively data-driven.

**Warning pattern:** large, well-measured estimates are uniformly collapsed toward zero, suggesting over-shrinkage.

## Figure 4 — Simulation recovery

Panels for bias, RMSE, sign accuracy, and strong-effect sensitivity versus information level and true effect magnitude, comparing shrunken and unshrunk estimators.

**Interpretation:** directly tests preservation of simulated truth. It cannot prove that the simulated distribution is the biological truth.

## Figure 5 — Stability of biological-replicate support

For selected genes, display effects across leave-one-biological-replicate-out or other pre-specified biological resampling procedures.

**Interpretation:** identifies estimates driven by a single replicate. With very few replicates, this plot may itself be unstable; that limitation must be stated.

## Figure 6 — Independent validation

Scatter or paired interval plot of discovery versus validation effects, with genes stratified into high-information material effects, attenuated candidates, low-information extremes, and near-null controls.

**Interpretation:** tests reproducibility. Separate annotation should identify genes selected through the shrunken estimate, unshrunk estimate, or both.

No pathway, disease, or mechanistic enrichment figure should be treated as primary evidence until the underlying gene-level effects pass these recovery and validation checks.

---

# 5. Conditional conclusions

## Positive conclusion

A positive methods-and-biology conclusion would require all of the following:

1. Simulations show reduced error for weak/noisy estimates.
2. Simulations show that high-information true strong effects retain acceptable sensitivity and limited bias after shrinkage.
3. Independent samples reproduce the direction and approximate magnitude of the pre-specified high-confidence effects.
4. Low-information extremes fail replication more often than stable, high-information effects, supporting their cautious classification.
5. No major condition-batch confounding or provenance failure is found.

The appropriate biological statement would then be:

> The condition is associated with reproducible differences in bulk RNA abundance for the validated genes under the studied system and contrast.

This would **not** establish direct transcriptional regulation, absolute RNA-output changes, protein-level changes, or cell-intrinsic mechanisms without additional evidence.

## Negative conclusion

A negative conclusion would be supported if:

- shrinkage materially reduces recovery of known strong simulated effects;
- independent validation does not reproduce even well-supported discovery effects;
- results are highly sensitive to omission of one biological replicate;
- condition is confounded with batch or sample provenance is unreliable; or
- the count-model assumptions provide poor fit.

The appropriate conclusion would be that the planned estimator and/or dataset does not provide reliable evidence for the claimed expression changes. This is not proof that the biological condition has no effect.

## Ambiguous conclusion

Ambiguity is expected if:

- simulation performance is acceptable but validation has inadequate precision;
- a few large effects replicate but most do not;
- effects reproduce in bulk RNA but composition information is absent;
- the Normal prior improves low-count behavior but its influence on broad/asymmetric response patterns is unclear; or
- the available sample number is too small for stable resampling or an independent holdout.

In this case, report validated candidates separately from unvalidated candidates and collect additional independent biological samples rather than converting uncertainty into a binary biological claim.

---

# 6. Alternatives and limits

1. **No prior distribution is established by the packet.**  
   The Normal prior is a shrinkage device, not evidence that biology is Normal, sparse, symmetric, or centered at zero. Simulations must therefore test departures from that assumption.

2. **Shrinkage is not a substitute for replication.**  
   Sharing information across genes improves estimation but cannot create biological evidence absent from the samples.

3. **Low-count genes require caution, not automatic dismissal.**  
   A low-information large estimate should not be accepted as a finding, but neither should it be declared absent. Targeted validation is the appropriate resolution.

4. **Bulk RNA-seq measures relative gene-level RNA abundance.**  
   Without composition measures, spike-in-like absolute references, or cell-resolved experiments, the analysis cannot cleanly distinguish cell-intrinsic regulation, composition change, and some global RNA-output changes.

5. **No published result is reproduced here.**  
   No raw dataset, sample metadata, fitted model, gene list, parameter values, simulation outcomes, or validation measurements were supplied. The plan is an independent, falsifiable implementation of the methodological rationale in the packet.
