# GPT-6 Astra / inf-r01

Original final answer, shared by both scoring rounds.

## Recommended next action

**Build an information-stratified benchmark of Normal-prior shrinkage, then test whether a more flexible effect prior preserves independently supported large changes without reviving low-information extremes.** Do not assume either that biological effects are Normally distributed or that the largest estimated fold changes are real.

Everything below is a **proposed protocol**, not an executed analysis. The packet supplies no dataset, accession, implementation, fitted parameters, or biological results.

## 1. Biological question, estimand, and competing explanations

### Unresolved biological question

In a defined cell population exposed to an experimental perturbation versus matched controls, **which apparent large transcriptional responses represent reproducible regulation, and which arise from low or variable counts when biological replication is limited?**

A related methodological question is whether Normal-prior shrinkage suppresses genuine large responses more than necessary while appropriately stabilizing weakly informed estimates.

The organism, cell population, perturbation, dose, and sampling time are **unreported**. These must be fixed before dataset selection; selecting a biological system after seeing favorable results would weaken the test.

### Target quantity

For gene \(g\), estimate

\[
\beta_g=\log_2
\left(
\frac{\text{expected normalized expression under perturbation}}
{\text{expected normalized expression under control}}
\right).
\]

This is a **relative expression estimand**. Without an appropriate external scale, it is not necessarily a change in molecules per cell. In bulk samples, it can also reflect changing cell composition rather than within-cell regulation.

### Competing explanations and predictions

| Explanation | Biological/statistical mechanism | Distinct prediction |
|---|---|---|
| **Noise-dominated extremes** | Small counts, few replicates, or high between-replicate variability generate extreme estimates. | Extremes concentrate in low-information genes, change substantially between replicate subsets, and fail independent validation. Shrinkage improves recovery. |
| **Rare, genuine large responses** | A small subset of genes responds much more strongly than the background. | Large effects recur in independent biological samples. At adequate information, they remain large across resampling and depth changes. A flexible prior may reduce attenuation relative to a single Normal prior. |
| **Broad, mostly moderate responses** | Many genes change, without a distinct large-effect subgroup. | A single Normal prior may perform as well as a more flexible alternative; added flexibility may mainly increase variance. |
| **Reproducible non-target signal** | Batch, cell composition, or other sample differences track condition. | Effects can replicate yet fail to establish the intended within-cell regulatory mechanism. Balanced design and relevant metadata are necessary to distinguish this explanation. |

These explanations are not mutually exclusive. A dataset can contain both genuine strong responses and unstable extremes.

## 2. Evidence → inference → conclusion

Evidence locations below refer to the four sentences of the supplied packet.

| Packet evidence | Supported inference | Consequence for this proposal |
|---|---|---|
| **E1:** Gene-level differences are estimated using a count model. | Read counts and the sampling design should enter estimation directly. | Use a count likelihood with library-size offsets and condition effects. |
| **E2:** Few replicates and low or variable counts can produce unstable fold changes. | Effect magnitude alone does not establish reliability. | Stratify evaluation by information, abundance, and variability; explicitly measure instability. |
| **E3:** Information sharing stabilizes dispersion and effects, using a Normal effect prior. | Normal-prior shrinkage is the supplied methodological baseline. | Compare it with otherwise matched estimation without effect shrinkage. |
| **E4:** The packet does not establish every possible biological effect distribution. | Good performance under a Normal generating distribution cannot establish general superiority. | Test multiple effect distributions, including alternatives unfavorable to each candidate. |

**Conclusion:** The packet supports investigating shrinkage, but it does not establish that a particular alternative prior is superior, that large biological effects are common, or that any published biological result can be reproduced.

## 3. Proposed end-to-end protocol

All numerical thresholds below are **proposed registration choices**, not findings or recommendations established by the packet.

### Step 1 — Freeze the biological contrast and analysis plan

Before inspecting differential-expression results, register:

- Biological system, intervention, control, dose, time point, and target population.
- Independent experimental unit: for example, donor, animal, or independently established culture.
- Primary estimand and relevant nuisance variables.
- Eligibility, quality-control, normalization, filtering, simulation, and evaluation rules.
- Primary comparisons and acceptance gates.
- Software environment, random seeds, and planned figures.

Technical libraries or sequencing lanes from the same biological sample are not independent biological replicates.

### Step 2 — Establish dataset eligibility and separation

Use three non-overlapping data roles:

1. **Development cohort:** calibrate nuisance-parameter ranges and finalize implementation. Proposed minimum: six independent units per condition.
2. **Benchmark cohort:** proposed minimum of 15 units per condition, allowing a primary split into three per condition for small-sample estimation and 12 per condition for a higher-information reference.
3. **Independent validation cohort:** proposed target of at least 12 new units per condition, matched for biological contrast and sampling time.

These sample sizes are starting targets, not guarantees of precision. Development simulations must assess whether larger reference and validation cohorts are required.

**Eligibility requirements**

- Raw reads and sample-level metadata are available.
- Condition is not perfectly confounded with batch, donor category, or processing date.
- Replication permits dispersion estimation after accounting for the design.
- Library chemistry, RNA selection, and gene annotation are compatible across the contrast.
- The independent validation cohort contains no reused individuals, cultures, libraries, or reads.
- Sample exclusions can be applied without examining gene-level condition effects.

For paired designs, retain whole pairs during splitting and resampling.

If only one sufficiently replicated cohort is available, internal benchmarking remains possible, but **independent biological validation is unavailable**. Read splitting or deeper sequencing of the same library does not remedy that limitation.

### Step 3 — Preserve raw-read provenance

Construct an auditable sample manifest linking:

\[
\text{study} \rightarrow \text{biological unit} \rightarrow
\text{library} \rightarrow \text{run/lane} \rightarrow
\text{raw files} \rightarrow \text{count column}.
\]

Record:

- Accessions or source identifiers, retrieval date, checksums, and file sizes.
- Organism, condition, biological-unit identifier, batch, and relevant covariates.
- Paired- or single-end layout, strandedness, library preparation, and any molecular barcodes.
- Reference genome and gene-annotation versions and checksums.
- Processing commands, software versions, container/environment identifiers, and seeds.
- Every exclusion or sample-label correction, with its reason.

**Currently unreported:** all actual identifiers, versions, sequencing characteristics, and covariates. They must be supplied before execution.

Combine technical lanes belonging to the same library without counting them as separate samples.

### Step 4 — Process reads and produce gene counts

Use one frozen workflow across cohorts wherever assay compatibility permits:

1. Verify checksums and sample identities.
2. Inspect read quality, adapters, contamination indicators, library complexity, and strandedness.
3. Trim only according to registered rules.
4. Align to the pinned reference.
5. Count fragments for paired-end data, not both mates as separate observations.
6. Count uniquely assigned fragments overlapping the registered gene features.
7. Record ambiguous and multimapping fragments separately rather than allocating them differently by condition.
8. Do not automatically remove duplicate-looking reads from ordinary RNA-seq; use barcode-based deduplication only when the library design supports it.
9. Produce sample-level mapping, assignment, depth, and count-distribution reports.

Define quantitative QC cutoffs on the development cohort and freeze them before benchmark evaluation. Review failures blinded to condition where practical. Retain a sensitivity analysis including borderline samples.

Report changes in sample balance after QC; exclusions that destroy identifiability invalidate the contrast.

### Step 5 — Define the gene universe and normalization

- Freeze gene identifiers and rules for duplicated or overlapping identifiers.
- Keep a complete ledger of genes retained, filtered, and unestimable.
- Exclude genes with zero counts in every small-sample observation from expression-change claims.
- Use a condition-blind abundance rule for the primary analysis; a proposed rule is at least ten total fragments across the six small-sample libraries.
- Repeat evaluation without that abundance filter as a low-information sensitivity analysis.

Report filter attrition rather than allowing filtering to hide failures on difficult genes.

**Proposed normalization:** estimate sample size factors using median ratios to gene-wise geometric means among suitable nonzero genes, then scale factors to geometric mean one.

**Assumption:** a sufficiently large set of genes supplies a stable relative reference. If broad directional changes violate this assumption, examine appropriate external controls if available. Without them, absolute global expression shifts remain unidentified.

Each small-sample fit estimates normalization from its own eligible data. Reference and validation outcomes must not inform its size factors.

### Step 6 — Fit the count model and share dispersion information

A **proposed implementation assumption**, not specified by the packet, is a negative-binomial count model:

\[
Y_{gi}\sim \operatorname{NB}(\mu_{gi},\phi_g),
\qquad
\operatorname{Var}(Y_{gi})=\mu_{gi}+\phi_g\mu_{gi}^{2},
\]

\[
\log\mu_{gi}
=\log s_i+\alpha_g+(\log 2)\beta_g x_i+\mathbf z_i^\top\boldsymbol\gamma_g.
\]

Here \(s_i\) is the size factor, \(x_i\) identifies condition, and \(\mathbf z_i\) contains registered covariates.

For dispersion stabilization:

1. Obtain initial gene-level dispersion estimates.
2. Fit a mean–dispersion trend.
3. Estimate between-gene dispersion variation around that trend.
4. Shrink gene dispersions toward the trend using a registered empirical-Bayes procedure.

One implementable choice is a Normal distribution for log-dispersion around a smooth mean-dependent trend. This is a proposed dispersion model, not evidence about the actual data.

Inspect trend fit, boundary estimates, residual patterns, influential samples, and convergence. Dispersion and effect-prior fitting must be repeated within each benchmark subset and simulated dataset.

### Step 7 — Compare matched effect estimators

Use identical counts, offsets, design matrices, and stabilized dispersions for the primary comparison.

**A. No effect shrinkage**

Estimate \(\beta_g\) by likelihood maximization. Retain boundary and infinite estimates as explicit failures of finite magnitude estimation; do not silently cap them.

**B. Supplied-direction baseline: Normal shrinkage**

\[
\beta_g\sim N(0,\tau^2).
\]

Estimate \(\tau\) across genes by marginal-likelihood fitting, accounting for differing likelihood precision rather than treating raw fold-change estimates as equally reliable. Do not shrink the intercept.

**C. Proposed challenger: two-scale Normal mixture**

\[
\beta_g\sim
(1-w)N(0,\tau_0^2)+wN(0,\tau_1^2),
\qquad \tau_1\geq\tau_0.
\]

Fit the mixture weight and scales using the same empirical-Bayes principle. This allows a concentrated background and a broader component. It is a **hypothesis to test**, not an established improvement.

For B and C, report posterior means and 95% posterior intervals using numerical integration where feasible. Record optimizer starts, tolerances, boundary solutions, and failures. Assess uncertainty from estimated nuisance parameters through whole-analysis resampling; conditional posterior intervals alone may be too optimistic.

As a separate ablation, compare dispersion sharing with unshared dispersion estimation. This distinguishes benefits of dispersion stabilization from benefits of effect shrinkage.

### Step 8 — Explain and test the shrinkage mechanism

Under a locally Normal likelihood,

\[
\widehat\beta_g\mid\beta_g\approx N(\beta_g,s_g^2),
\]

the Normal-prior posterior mean is approximately

\[
\widetilde\beta_g=
\frac{\tau^2}{\tau^2+s_g^2}\widehat\beta_g.
\]

Thus shrinkage depends on **information relative to prior scale**, not simply on estimated effect size.

Consequences to test:

- Precise effects should usually experience less shrinkage.
- Imprecise large estimates may appropriately be strongly reduced.
- Rare genuine large effects may still be attenuated if the fitted prior scale is narrow.
- A broader prior component could reduce that attenuation but might also admit noisy extremes.

An all-zero treatment arm with substantial counts in controls can support a large directional change while leaving its exact magnitude poorly bounded. Report such cases separately; an infinite unshrunk estimate is neither a measured infinite biological effect nor proof of no response.

## 4. Simulation: known truth without assuming the answer

### Generating settings

Use development data only to calibrate plausible mean, dispersion, depth, and covariate distributions. In parallel, use a fully specified synthetic grid so conclusions do not depend on one calibration dataset.

Proposed grid anchors are:

- Mean counts: 1, 5, 20, 100, and 1,000.
- Dispersions: 0.01, 0.1, and 1.
- Replicates per condition: 3, 5, 10, and 20.
- Depth multipliers: 0.5, 1, and 2.

These are stress-test settings, not reported biological distributions.

### Effect distributions

Include:

1. All-null effects.
2. Single Normal effects at several scales.
3. Sparse moderate effects.
4. Rare strong effects, with 1% or 5% of genes assigned effects between one and four log2 units.
5. Symmetric fixed strong effects, such as \(\pm2\) or \(\pm4\), avoiding exclusive use of the challenger’s own generating family.
6. Broad responses affecting a large fraction of genes.
7. Asymmetric responses.
8. Relationships between effect size and baseline abundance or dispersion.

Vary strong-effect frequency separately from strong-effect magnitude.

### Model-stress scenarios

Add prespecified scenarios with:

- Balanced and imbalanced batches.
- Sample-level latent variation shared across genes.
- Outlying samples.
- Dispersion-trend misspecification.
- Compositional shifts and normalization failure.

For global shifts, distinguish normalization-compatible relative truth from unidentifiable absolute per-cell truth. Do not attribute an identifiability failure solely to the shrinkage prior.

### Execution rules

For every simulated study:

1. Generate biological samples and counts.
2. Run the complete filtering, normalization, dispersion, and effect-estimation workflow.
3. Re-estimate all empirical-Bayes parameters.
4. Save truth, estimates, intervals, flags, and rankings.

Begin with at least 1,000 independent simulated studies per primary configuration and extend runs if key study-level error-rate Monte Carlo standard errors exceed 0.01. Reserve additional effect-distribution configurations for a final locked robustness test.

## 5. Evaluation: preserve strong effects without rewarding extremes

### Information strata

Evaluate jointly by abundance, dispersion, true/reference effect size, and likelihood information.

Proposed information cutoffs:

- **High information:** likelihood standard error at most 0.25 log2 units.
- **Low information:** standard error at least 1, or poorly bounded likelihood.
- Intermediate cases remain a separate group.

Use truth-based expected information in simulations and likelihood-based diagnostics in real data. Report sensitivity to these cutoffs.

### Primary metrics

**Recovery**

- Bias, mean squared error, and median absolute error.
- Sign errors.
- Strong-effect attenuation: signed estimate divided by true effect, restricted to \(|\beta|\geq1\).
- Magnitude recovery separately from directional detection.

**Protection against unstable extremes**

- For low-information genes with \(|\beta|\leq0.25\), frequency of \(|\widetilde\beta|\geq2\).
- Frequency of large estimates that reverse sign or disappear across biological subsets.
- Unbounded-estimate and optimizer-failure rates.
- False strong-effect claims and false signs among selected genes.

**Uncertainty and ranking**

- Coverage and width of nominal 95% intervals.
- Precision and recall for strong effects.
- Stability and independent confirmation of top-ranked genes.

Do not rank by absolute point estimate alone. A proposed strong-effect claim requires either

\[
P(\beta_g>1\mid Y)>0.975
\quad\text{or}\quad
P(\beta_g<-1\mid Y)>0.975.
\]

These posterior thresholds do **not** establish frequentist error control; simulation and validation must measure it. If fewer than the requested number of genes pass, do not fill the ranking with unsupported candidates.

### Proposed falsifiable acceptance gates

For the challenger versus Normal shrinkage, preregister the following in core, model-compatible scenarios:

1. At least 10% lower strong-effect mean squared error in sparse-large-effect settings, with uncertainty supporting improvement.
2. High-information strong-effect median retention between 0.9 and 1.1.
3. No more than a 5% increase in overall mean squared error.
4. Low-information false-extreme frequency no greater than 5%, and no more than one percentage point above the Normal baseline.
5. Nominal 95% interval coverage within a registered tolerance, proposed as 92.5%–97.5%, in sufficiently populated evaluation strata.

Assess paired differences across the same simulated studies. Report uncertainty and results for every registered primary scenario; do not average away an important failure.

These gates are deliberately joint: **better recovery of large effects is insufficient if obtained by releasing noisy extremes.**

For the unshrunk comparator, report finite-estimate accuracy on a common estimable set alongside failure rates over the full eligible universe.

## 6. Higher-information reference and independent validation

### Benchmark analysis

- Freeze one primary random split: three units per condition for estimation, remaining units for reference.
- Estimate reference effects without effect shrinkage where likelihood information is adequate.
- Treat reference estimates as uncertain measurements, not ground truth.
- Define a reference-supported strong set using intervals entirely outside \([-1,1]\).
- Evaluate all eligible genes, not only this selected set.

Account for reference uncertainty in loss and slope analyses. Otherwise, noisy reference effects can create apparent attenuation or reward a method for matching reference noise.

Repeated small-sample splits assess robustness but are correlated. They are not additional independent studies.

### Independent validation

After locking estimators, rankings, and claims, process the independent cohort through the frozen read workflow.

Evaluate:

- Directional concordance.
- Magnitude agreement with uncertainty.
- Validation rates for strong claims.
- Low-information extremes and prior-sensitive genes.
- Genes supported by all estimators, only one estimator, or none.

Use the full common gene universe for sequencing validation. If only a subset can be assessed, use a registered stratified random sample with known inclusion probabilities—not only attractive candidates.

Resample biological units, preserving pairing and shared gene-level structure. Do not treat thousands of correlated genes as thousands of independent biological replications.

Where randomization permits, within-block label permutations provide a negative control. They are inappropriate when exchangeability is absent.

**Read downsampling is supplementary:** it tests depth sensitivity, not independent biological reproducibility.

## 7. Figure generation and reproducibility outputs

Generate every figure directly from saved analysis tables with versioned scripts, fixed seeds, and recorded exclusions.

1. **Dataset and provenance flow:** cohorts, biological units, libraries, exclusions, and final sample counts.
2. **Information diagnostics:** mean–dispersion relationships, likelihood uncertainty, and boundary cases.
3. **Shrinkage behavior:** unshrunk versus shrunken effects, colored by information; fitted prior distributions shown separately from observed estimate distributions.
4. **Simulation performance:** recovery, attenuation, false extremes, and coverage by generating distribution and information stratum.
5. **Independent validation:** small-sample estimates versus validation estimates, with uncertainty and method-specific claims identified.
6. **Stability:** effects and rankings across biological subsets and read depths, explicitly separating the two operations.

Publish supporting tables containing counts, manifests, normalization factors, dispersions, prior parameters, estimates, intervals, fit flags, and figure source data.

Do not plot a fitted prior as though it were a directly observed distribution of biological effects.

## 8. Conditional interpretation, alternatives, and limits

### Positive outcome

**If Normal shrinkage beats unshrunk estimation:** conclude that information sharing improves recovery under the tested conditions.

**If the challenger also passes all joint gates and validates independently:** conclude that allowing heterogeneous effect scales better preserves supported strong responses in those settings without a detected unacceptable increase in unstable extremes.

This would not prove that all biological effect distributions require a mixture prior.

### Negative outcome

**If the challenger preserves magnitude but increases false extremes or miscalibration:** reject it as a general replacement. Apparent tail recovery would not constitute reliable biological recovery.

**If Normal shrinkage matches or outperforms it:** retain the simpler Normal baseline for the tested domain.

**If neither performs adequately:** investigate normalization, confounding, dispersion modeling, outliers, and replication before adding prior flexibility. More biological replication may be the most useful intervention.

### Ambiguous outcome

The result remains unresolved if:

- Too few independently supported strong effects exist.
- Validation precision is inadequate.
- Cohorts differ materially in biology or composition.
- Reference uncertainty changes the apparent winner.
- Conclusions depend strongly on filtering or prior fitting.
- A method succeeds only under its own assumed generating distribution.

In those cases, report the identifiable limits and specify the additional samples or design changes needed.

## 9. Forecast versus reproduction

**Methods-direction forecast:** An information-aware flexible effect prior might preserve rare strong responses better than a single Normal prior, while dispersion sharing continues to stabilize inference. This is a conditional, falsifiable forecast.

**Actual reproduction:** Not performed and not possible from this packet alone. The supplied material does not identify a publication’s datasets, raw reads, implementation, analysis settings, figures, or biological claims.

Accordingly, this proposal can establish a route to testing methodological behavior. It cannot establish recovery of any published biological result, nor infer a regulatory mechanism merely from improved fold-change estimation.
