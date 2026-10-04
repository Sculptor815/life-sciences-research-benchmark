# GPT-5.6 Sol / inf-r01

Original final answer, shared by both scoring rounds.

# Proposed study: recovering reproducible transcriptional responses from noisy RNA-seq counts

## Recommended next action

Use a preregistered, shared-information count model that shrinks both gene-wise dispersion and log fold change, but require prospective simulation and an independent biological cohort before interpreting any gene as truly changed. Evaluate the method against unshrunk and partially shrunk alternatives, explicitly stratifying results by expression information. The key criterion is that shrinkage must suppress unsupported low-information extremes while retaining large effects when the likelihood contains enough information.

This is a **methods-direction forecast**, not a reproduction of published biological findings. The evidence packet contains no dataset, raw-read identifiers, biological system, sample metadata or observed results.

---

## 1. Unresolved biological question

**In a defined cell type or tissue, does a specified biological perturbation produce a reproducible gene-expression program, or are the largest apparent fold changes primarily consequences of low counts, variable counts and few biological replicates?**

The perturbation, biological system and time point must be specified before analysis. The intended biological output is a set of genes whose changes are:

1. large enough to matter biologically,
2. statistically supported rather than driven by low information,
3. directionally consistent in an independent biological cohort, and
4. not dependent on the Normal-effect assumption alone.

### Competing explanations and predictions

#### Mechanism A: reproducible biological regulation

The perturbation changes transcription in a subset of genes.

**Predictions**

- Effects recur with the same direction in independent biological samples.
- Strong effects with adequate counts and moderate dispersion remain strong after shrinkage.
- Evidence concentrates in genes with informative count likelihoods, rather than exclusively in the lowest-count genes.
- Discovery and validation effect estimates show positive agreement even when validation is generated in a separate batch.

#### Mechanism B: sampling-driven extremes

There is little or no reproducible regulation, but low or variable counts produce unstable unshrunken fold changes.

**Predictions**

- The largest raw fold changes are enriched among low-information genes.
- Their magnitudes and signs vary across resampling or independent cohorts.
- Effect shrinkage moves these estimates substantially toward zero.
- Null simulations generate similar extremes when unshrunken estimation is used.

#### Mechanism C: technical or design-associated differences

Apparent condition effects arise from batch, sample quality, library composition or confounding between biological condition and technical processing.

**Predictions**

- Effects track technical variables or disappear when an estimable adjustment is included.
- A separately processed validation cohort fails to reproduce them.
- If condition and technical batch are perfectly confounded, the biological and technical explanations cannot be separated statistically.

#### Mechanism D: prior misspecification

The biological effects are real but distributed differently from the proposed zero-centered Normal prior—for example, they are sparse, asymmetric, multimodal or contain unusually heavy tails.

**Predictions**

- The Normal-prior method may over-shrink rare large effects or miscalibrate uncertainty.
- Performance will be acceptable under Normal-effect simulations but degrade under heavy-tailed or asymmetric simulations.
- Independent validation may reproduce strong effects more closely than the shrunken discovery estimates predict.

---

## 2. Evidence-to-inference-to-conclusion chain

| Evidence supplied | Methodological inference | Prospective conclusion supported |
|---|---|---|
| Gene-level differences are estimated using a count model. | Analyze integer gene counts with a count regression model and retain count-scale uncertainty. | Count-model estimates are the appropriate starting point for the proposed comparison. |
| Few biological replicates and low or variable counts can generate unstable fold changes. | Quantify information per gene, compare raw and shrunken effects, and treat low-information extremes as unresolved unless independently supported. | Very large raw fold changes are not sufficient evidence of biological change. |
| Dispersion and fold-change estimates can be stabilized by sharing information across genes and placing a Normal prior on effects. | Fit a hierarchical model with shrunk dispersion and a zero-centered Normal prior on condition effects. | Shrinkage is a plausible way to improve stability. |
| The packet does not establish every possible biological effect distribution. | Stress-test Normal-prior performance under sparse, heavy-tailed, asymmetric and multimodal alternatives. | Any favorable conclusion must be conditional on demonstrated robustness; universal optimality cannot be claimed. |

No row establishes that a particular gene, pathway or perturbation has already been validated.

---

## 3. Complete proposed protocol

## Stage 1: preregistration and biological specification

Before looking at condition labels in the count data, record:

- the biological perturbation and comparator;
- tissue or cell type, collection time and inclusion population;
- the primary contrast;
- whether the design is paired, blocked or longitudinal;
- nuisance variables that will enter the model;
- the biological effect threshold, \(\delta\), expressed as an absolute log2 fold change;
- the tolerated false-sign or false-discovery level;
- primary simulation metrics and success criteria;
- validation endpoints;
- all sample- and gene-exclusion rules.

Because the packet supplies no biological context, the value of \(\delta\) is an **unreported parameter**. It should be selected for biological relevance before outcomes are inspected, rather than inferred from the largest observed fold changes.

---

## Stage 2: dataset eligibility

A discovery dataset is eligible only if it has:

1. raw sequencing reads for every analyzed sample;
2. at least two independent biological units in each estimable condition, or at least two independent pairs for a paired contrast;
3. sample-level condition labels and sufficient technical metadata;
4. an estimable design in which condition is not perfectly confounded with batch or another required covariate;
5. gene-level count generation that can be reconstructed from the raw reads;
6. a consistent biological system and sampling time for the primary contrast;
7. permission to reserve or acquire a genuinely independent validation cohort.

Two replicates per group are an operational minimum for an estimable comparison, not a claim that they are generally adequate. Simulation should determine whether the available design has useful power for \(\delta\).

Technical replicates do not count as independent biological replicates. If they represent repeated sequencing of the same biological library, combine them at an explicitly documented stage or model their dependence; do not treat them as independent evidence.

### Exclusion conditions

Exclude the dataset from the primary biological question if:

- raw reads or essential sample identities are unavailable;
- condition and technical batch are inseparable;
- biological replication is absent;
- the primary contrast was selected after inspecting gene-level outcomes;
- most samples fail prespecified, condition-blind technical criteria.

Excluding an individual sample after observing its effect on the condition result is not permitted. Any post hoc exclusion must be shown only as a labeled sensitivity analysis.

---

## Stage 3: raw-read provenance and reproducibility record

Create an immutable manifest containing, for every sample:

- sample and biological-unit identifiers;
- raw-read file names and checksums;
- source location or accession;
- collection condition and biological replicate;
- technical replicate, lane and batch identifiers;
- library preparation and strandedness, if known;
- sequencing platform, read layout and read length, if known;
- acquisition date and any transfer or renaming steps.

Record for the raw-to-count pipeline:

- reference sequence and gene annotation versions;
- read preprocessing rules;
- alignment or quantification method and complete parameters;
- handling of multimapping and ambiguous reads;
- gene-count aggregation rules;
- software and environment versions;
- all logs, intermediate file identifiers and checksums.

These parameters are not supplied and therefore cannot be filled in here. They must be frozen before differential-expression results are examined.

---

## Stage 4: raw-read processing and condition-blind quality control

1. Verify raw-file checksums.
2. Inspect read quality, adapter content and library structure.
3. Apply a single prespecified preprocessing policy to all samples.
4. Align or quantify against the fixed reference and annotation.
5. generate integer gene-level counts under the fixed assignment policy.
6. Produce sample-level metrics such as total assigned counts, assignment rate and expression-profile similarity.
7. Apply only preregistered, condition-blind failure rules.
8. Check sample identity and the correspondence between metadata and count profiles where possible.
9. Lock the count matrix and analysis manifest.

Genes with zero counts in every sample are non-estimable and should be labeled as such. A condition-independent minimal-count filter may be used to remove genes carrying essentially no likelihood information, but its rule must be frozen and its consequences reported. Filtering must not depend on observed fold-change direction.

---

## Stage 5: discovery and validation separation

The preferred design uses:

- a **discovery cohort** to estimate the dispersion-sharing relationship and Normal-prior scale; and
- an **independent validation cohort** consisting of newly sampled biological units.

Do not estimate discovery hyperparameters using validation data. If only one cohort initially exists, a held-out subset can test computational reproducibility, but it is weaker than new biological sampling and must not be described as fully independent validation.

Validation sample size should be chosen by the simulation procedure below to provide prespecified power for effects of magnitude \(\delta\). A numerical sample size cannot be supplied without the mean counts, dispersions, design and acceptable error rates.

---

## Stage 6: primary estimation model

### Proposed model and assumptions

For gene \(g\) and sample \(i\), use a count regression model. One operational implementation is:

\[
Y_{gi} \sim \text{Negative Binomial}(\mu_{gi},\alpha_g)
\]

\[
\log(\mu_{gi}) = \log(s_i) + X_i\gamma_g + C_i\beta_g
\]

where:

- \(Y_{gi}\) is the gene count;
- \(s_i\) is a library-size or normalization offset;
- \(X_i\) contains prespecified nuisance or blocking variables;
- \(C_i\) encodes the biological contrast;
- \(\beta_g\) is the gene-specific log fold change;
- \(\alpha_g\) is the gene-specific dispersion.

The negative-binomial form is a **proposed operational assumption**, not a result supplied by the packet. Diagnostics and simulation must assess its adequacy.

### Dispersion sharing

1. Obtain initial gene-wise dispersion estimates.
2. estimate a cross-gene mean–dispersion relationship.
3. shrink noisy gene-wise dispersions toward that relationship, with the amount of shrinkage reflecting gene-level information.
4. Preserve both raw and shrunken dispersion estimates for audit and figures.

### Effect sharing

Use the stipulated effect prior:

\[
\beta_g \sim N(0,\tau^2)
\]

Estimate \(\tau\) using discovery genes under a frozen empirical-Bayes procedure. Nuisance coefficients should not automatically receive the same prior unless separately justified.

Report for each gene:

- unshrunken effect estimate;
- shrunken effect estimate;
- unshrunken standard error or likelihood interval;
- posterior or penalized-model uncertainty;
- posterior probability of each direction and of exceeding \(\delta\);
- abundance, dispersion and an information measure;
- the degree of shrinkage.

### Information measure

Define gene information independently of the prior, for example as the inverse variance of the unshrunken condition-effect estimate:

\[
I_g = 1/\operatorname{Var}(\hat{\beta}^{\,\text{unshrunk}}_g).
\]

Genes can then be stratified into prespecified information bins. Information bins are descriptive; they must not be selected after seeing which bin gives the desired result.

---

## Stage 7: decision rule that rejects unstable extremes

A gene should be called a supported biological change only when all of the following hold:

1. its shrunken absolute effect is at least the preregistered biological threshold \(\delta\);
2. its posterior probability of exceeding \(\delta\) in the reported direction exceeds a preregistered level, provisionally 0.95;
3. the simulation-calibrated information gate is passed;
4. its expected error rate under the applicable simulation scenario is within the preregistered tolerance;
5. its direction is confirmed in the independent validation cohort.

The information gate should be selected from discovery-design simulations, not from observed gene labels. Choose the smallest information level at which the false-sign rate for null or near-null effects remains at or below the target, provisionally 5%.

A low-information gene with a large shrunken estimate but inadequate directional evidence is **unresolved**, not proven unchanged. This distinction prevents rejection of potentially real low-count biology while also preventing acceptance of unstable extremes.

---

## Stage 8: simulation evaluation

Simulation is part of the primary evaluation, not an optional illustration.

### 8.1 Parameter basis

Using the discovery design, estimate representative:

- library-size offsets;
- mean-count distribution;
- dispersion relationship and residual dispersion variation;
- sample allocation and model matrix.

Generate new count matrices preserving these design characteristics. Re-estimate all model hyperparameters within each simulated dataset; do not supply the analysis method with the true simulation parameters.

Because simulation from the fitted model may favor that model, include deliberately misspecified effect distributions.

### 8.2 Effect scenarios

At minimum, simulate:

1. **Global null:** all true condition effects are zero.
2. **Normal effects:** nonzero effects follow the proposed Normal prior.
3. **Sparse effects:** most effects are zero and a minority are nonzero.
4. **Rare strong effects:** a small fraction have effects well above \(\delta\).
5. **Heavy-tailed effects:** more extreme effects than a Normal prior predicts.
6. **Asymmetric effects:** up- and down-regulation are not balanced.
7. **Multimodal effects:** effects arise from more than one nonzero mode.
8. **Abundance-dependent effects:** nonzero effects occur at low, medium and high mean counts.
9. **Dispersion-dependent effects:** the same true effects occur across low and high variability.

Repeat scenarios across the actual replicate number and plausible larger replicate numbers. This distinguishes a method failure from a fundamentally underpowered design.

### 8.3 Methods compared

Use identical normalization and design matrices while comparing:

- unshrunken gene-wise dispersion and unshrunken effects;
- dispersion shrinkage only;
- Normal effect shrinkage only;
- combined dispersion and Normal effect shrinkage;
- as a sensitivity analysis, a less strongly contracting or heavy-tailed effect model if the Normal prior fails.

The last option is an alternative direction, not something supported as superior by the evidence packet.

### 8.4 Metrics

For each method, report overall and within abundance, dispersion and information strata:

- effect bias;
- root-mean-square error;
- median absolute error;
- confidence or posterior interval coverage;
- sign-error rate;
- false-positive or false-discovery rate;
- power for \(|\beta_g| \geq \delta\);
- rank stability across repeated simulations;
- calibration of posterior directional probabilities.

### 8.5 Explicit strong-effect preservation test

Define a simulated gene as a **strong, informative effect** when:

- its true \(|\beta_g|\) exceeds a preregistered strong-effect threshold, \(\delta_{\text{strong}}\), at least as large as \(\delta\); and
- its likelihood-based information exceeds the simulation-calibrated gate.

For these genes, calculate the attenuation ratio:

\[
A_g = \frac{|\hat{\beta}^{\,\text{shrunk}}_g|}{|\beta^{\,\text{true}}_g|}.
\]

A provisional success criterion is:

- median \(A_g\) between 0.8 and 1.2;
- at least 90% correct effect direction;
- no material loss of detection relative to the best competing method at the calibrated error rate.

These numerical margins are proposed analysis criteria and may be tightened before registration. They are not observed results.

### 8.6 Explicit unstable-extreme rejection test

Among null and near-null genes in the lowest-information strata:

- identify genes with extreme unshrunken fold changes;
- measure how often each method reports them as exceeding \(\delta\);
- require a false-sign rate of no more than the preregistered target, provisionally 5%;
- compare the upper tail of raw and shrunken estimated magnitudes;
- confirm that stabilization does not merely replace large uncertain estimates with overconfident smaller ones.

The desired pattern is selective: strong informative effects are retained, while low-information extremes lose magnitude or fail the evidence gate.

---

## Stage 9: independent validation

### 9.1 Validation cohort

Acquire newly sampled biological units under the same biological contrast. Ideally, process them in a separate experimental batch while avoiding perfect confounding. Use the frozen raw-to-count pipeline and record a separate provenance manifest.

Before viewing validation outcomes, freeze:

- the discovery gene list;
- expected direction for every listed gene;
- \(\delta\);
- the validation model;
- primary replication metrics.

Include a representative set of discovery-positive, discovery-uncertain and discovery-null genes. Validating only the most favorable genes would inflate apparent replication.

### 9.2 Validation analyses

For each discovery gene:

1. estimate its validation effect without using discovery outcomes to reselect or change direction;
2. test directional agreement;
3. test whether the validation estimate exceeds \(\delta\), when sufficiently powered;
4. compare discovery and validation magnitudes with uncertainty intervals;
5. record genes that are directionally concordant but too imprecise for a magnitude conclusion.

Primary cohort-level measures should include:

- proportion of prespecified genes with matching directions;
- replication rate for effects above \(\delta\);
- discovery–validation effect association;
- calibration of discovery uncertainty against validation outcomes;
- replication stratified by discovery information and degree of shrinkage.

A targeted independent expression assay may provide additional validation for selected genes, but it does not replace independent biological sampling. Any such assay, platform and gene-selection rule are currently unreported.

---

## Stage 10: sensitivity analyses

Perform and label the following without replacing the primary analysis:

- removal of each biological replicate in turn;
- alternative reasonable gene-filtering thresholds;
- analyses with and without estimable nuisance covariates;
- dispersion-only and no-effect-shrinkage analyses;
- alternative prior scales;
- a heavier-tailed or mixture prior if the Normal prior fails the heavy-tail simulations;
- stratification by batch or other recorded technical variables;
- comparison of results before and after any post hoc sample exclusion.

A gene whose conclusion changes repeatedly under reasonable analyses should be labeled unstable.

---

## 4. Figure-generation plan

All figures should be generated by versioned scripts directly from locked analysis tables.

### Figure 1: dataset and provenance flow

Show:

- biological units and technical replicates;
- raw-read files;
- exclusions with preregistered reasons;
- discovery and validation separation;
- raw-read-to-count processing versions.

### Figure 2: dispersion stabilization

Plot initial gene-wise dispersion against mean count, with:

- estimated cross-gene relationship;
- shrunken dispersions;
- points colored by information.

This diagnoses where sharing has the greatest influence.

### Figure 3: raw versus shrunken effects

Use an abundance–effect plot and a direct raw-versus-shrunken comparison:

- point size or color indicates information;
- horizontal lines show \(\pm\delta\);
- low-information raw extremes are visibly distinguished from supported effects;
- strong informative genes are labeled only according to preregistered rules.

### Figure 4: simulation calibration

Display, by information stratum and true effect category:

- bias and root-mean-square error;
- sign-error rate;
- power;
- interval coverage;
- strong-effect attenuation ratio.

Show all four primary method variants on the same scale.

### Figure 5: strong-effect preservation versus extreme suppression

Two linked panels:

- attenuation for known strong simulated effects;
- call rate for extreme unshrunken estimates among null low-information genes.

This is the central falsification figure.

### Figure 6: independent validation

Plot discovery shrunken effects against independent validation effects with:

- uncertainty intervals;
- quadrants for directional agreement;
- lines at zero and \(\pm\delta\);
- symbols identifying genes that passed or failed the information gate.

Do not use only confirmed genes in this plot.

### Figure 7: stability summary

Show gene classifications across:

- primary analysis;
- leave-one-replicate-out analyses;
- alternative prior assumptions;
- independent validation.

Every figure should state sample counts, units, transformations, filtering rules and whether estimates are raw or shrunken.

---

## 5. Conditional interpretation

### Positive outcome

A favorable conclusion requires that:

- combined shrinkage lowers error and false signs in simulation;
- low-information null extremes are usually not called;
- strong informative effects show limited attenuation;
- performance remains acceptable under at least the major non-Normal scenarios;
- prespecified effects reproduce directionally and, where powered, in magnitude in the independent cohort.

**Permitted conclusion:**  
“In this dataset and design, shared dispersion and Normal-effect shrinkage improved recovery of reproducible gene-expression changes while reducing unsupported low-information extremes.”

This would not prove that every selected gene is causally regulated by the perturbation, nor that the method is optimal for all effect distributions.

### Negative outcome

A negative methodological result occurs if:

- strong informative effects are substantially compressed;
- false signs remain common in low-information genes;
- uncertainty is poorly calibrated;
- results fail under modest prior misspecification; or
- discovery effects do not replicate.

**Permitted conclusion:**  
“The proposed shrinkage method did not reliably separate reproducible effects from sampling-driven extremes under this design.”

Failure to validate does not by itself prove absence of biological regulation. It could also reflect inadequate validation power, biological heterogeneity, technical differences or confounding.

### Ambiguous outcome

Examples include:

- direction replicates but magnitude does not;
- the method performs well under Normal simulations but poorly with heavy tails;
- strong effects replicate but are consistently over-shrunk;
- only high-count genes are resolved, while low-count genes remain uncertain;
- discovery–validation agreement is positive but validation intervals are broad.

**Permitted conclusion:**  
“Evidence supports some reproducible regulation, but the Normal-prior model or available replication is insufficient to estimate the complete effect distribution.”

The next action would be more biological replication or a preregistered alternative prior, not post hoc acceptance of low-information extremes.

---

## 6. Alternatives and limits

### Alternatives

- **No effect shrinkage:** preserves raw magnitude but is expected to retain unstable extremes.
- **Dispersion shrinkage only:** tests whether dispersion stabilization is sufficient.
- **Normal effect shrinkage only:** isolates the contribution of effect regularization.
- **Heavy-tailed or mixture effect prior:** a candidate if strong-effect attenuation or non-Normal simulations falsify the Normal-prior approach.
- **More biological replication:** may be preferable to increasingly strong modeling assumptions when low information is the dominant limitation.

### Limits

The evidence packet does not establish:

- the correct count distribution for a particular dataset;
- the true distribution of biological effects;
- an appropriate biological effect threshold;
- valid normalization under extreme composition changes;
- the absence of batch effects or hidden biological heterogeneity;
- causal regulation from expression association;
- that shrinkage can recover information absent from the data.

Shrinkage can stabilize estimation, but it cannot transform a confounded or non-replicated experiment into an identifiable biological comparison.

---

## 7. Unreported parameters required before implementation

The following remain unknown and must not be invented:

- organism, tissue or cell type;
- perturbation and comparator;
- timing and pairing structure;
- discovery and validation sample sizes;
- raw-read identifiers;
- library and sequencing details;
- reference and annotation versions;
- quality-control thresholds;
- normalization method;
- nuisance covariates;
- \(\delta\) and \(\delta_{\text{strong}}\);
- target error rates;
- validation assay and replication criterion.

Accordingly, this plan forecasts how the supplied shrinkage rationale could be tested. It does **not** reproduce any published biological result or claim that any expression change has been observed.
