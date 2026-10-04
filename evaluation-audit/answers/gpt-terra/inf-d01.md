# GPT-5.6 Terra / inf-d01

Original final answer, shared by both scoring rounds.

# Objective and primary recommendation

Use the 30-patient paired cohort as a **development set** to derive a treatment-associated, multi-omic program defined primarily by **within-patient pre/post changes**, then lock the program and test it once in the untouched second cohort. The most defensible program will be one supported by:

1. reproducible paired changes in RNA and/or protein,
2. coherent pathway-level enrichment rather than isolated features,
3. metabolite changes consistent with the same biology, but interpreted cautiously because post-treatment metabolomics is largely batch-associated, and
4. external replication of a pre-specified program score and direction of change.

The patient—not an RNA sample, protein sample, metabolite sample, gene, or technical replicate—is the independent biological unit. The treatment-associated estimand is the average or patient-specific **post-treatment minus pretreatment change**. This supports a temporal association with treatment; it does not by itself establish that treatment caused the observed changes, because other time-varying factors may co-occur with treatment.

---

# Evidence-to-inference-to-conclusion chain

| Evidence | Inference | Design consequence |
|---|---|---|
| **M1. Thirty patients have pretreatment and post-treatment samples.** | Each patient supplies a matched baseline control. Between-patient heterogeneity can be removed or modeled. | Analyze paired within-patient differences or mixed models with patient effects; do not treat 60 samples as independent. |
| **M2. RNA and protein were run in different batches.** | RNA and protein measurements cannot be assumed to be on a common technical scale; cross-platform correlation can reflect modality-specific processing. | Perform QC and differential analysis within each modality first. Integrate biologically at feature/pathway/network levels, not by pooling raw RNA and protein values. Record any within-modality batch structure and treatment balance. |
| **M2. Most post-treatment metabolomics samples share a batch.** | Metabolomics batch and treatment time are substantially confounded. A post/pre metabolite difference may be a batch artifact. | Do not call a metabolite treatment-associated unless the result survives pre-specified batch-confounding checks or is supported by bridging/QC samples and sensitivity analyses. Use metabolomics primarily as corroborative evidence until this issue is resolved. |
| **M3. Some assays are missing.** | Complete-case analysis can waste data and can bias results if missingness relates to sample quality, time point, or outcome. | Preserve modality-specific paired analyses; characterize missingness; use integration approaches that tolerate missing blocks rather than imputing unmeasured biology as if observed. |
| **M4. A second small cohort is available but must remain untouched during development.** | It is the only unbiased estimate of reproducibility. | Freeze feature lists, weights, preprocessing rules, directionality, and pass/fail criteria before access. Do not use it for feature selection, tuning, threshold choice, or troubleshooting. |

**Conclusion:** The core discovery should be based on robust paired RNA and protein evidence, summarized as a locked pathway/program score. Metabolomics can strengthen mechanistic interpretation only after its batch limitation is addressed. External validation should test the locked program rather than repeat unrestricted discovery.

---

# Operational ordered protocol

## 1. Preparation, governance, and pre-specification

### 1.1 Define the scientific estimand
Pre-specify:

- **Primary estimand:** within-patient change from pretreatment to post-treatment in a multi-omic program score.
- **Secondary estimands:** feature-level RNA, protein, and metabolite changes; concordance between RNA and protein; association of program change with any available treatment-response or clinical variables.
- **Direction convention:** for every assay, define positive change as post-treatment minus pretreatment.
- **Minimum evidence standard for a “program”:** for example, a program must have:
  - statistically controlled evidence in at least one primary molecular layer (RNA or protein),
  - directional support in a second layer or robust pathway-level evidence,
  - stability under resampling,
  - and confirmation in the external cohort.
  
Exact numerical thresholds should be calibrated from the development data using resampling and false-discovery control, not selected after inspection of the external cohort.

### 1.2 Create an analysis manifest
Before examining differential results, create a sample-level manifest containing:

- patient identifier;
- time point;
- assay availability;
- extraction, library/preparation, acquisition, plate/run, operator, instrument, and processing batch;
- RNA/protein/metabolite QC metrics;
- specimen attributes, tissue composition estimates if available, and clinically relevant covariates;
- reason for missing assay or failed sample;
- sample swaps, duplicates, and re-runs.

A formal linkage check is essential: paired RNA, protein, and metabolite aliquots must map to the same patient and time point. Where genotype, sex markers, or other identity markers are available, use them to check pairing and detect swaps.

### 1.3 Allocation and blinding
There is no stated randomization of treatment in the evidence packet; therefore this is an analysis of samples collected before and after treatment, not a new intervention trial.

For analytic protection against bias:

- assign pseudonymous patient/sample identifiers;
- keep the external cohort inaccessible to analysts developing the signature;
- mask time point during initial sample QC where feasible;
- retain time point for checks that specifically require it, notably assessment of batch/time confounding;
- have a separate data custodian apply the frozen model to the external cohort;
- version-control all code, manifests, filtering decisions, and outputs.

## 2. Intervention and sampling documentation

The treatment regimen, timing between treatment and post-treatment biopsy, biopsy site, tumor cellularity, concurrent medications, fasting status, ischemia time, and storage conditions are **unreported parameters**. They may determine the biological meaning and reproducibility of the signal.

Document and evaluate:

- exact treatment exposure, dose, schedule, and adherence;
- interval from treatment initiation to post-treatment sampling;
- whether pre/post specimens come from the same lesion or anatomical site;
- tumor purity/cell composition and pathology review;
- specimen handling differences by time point;
- whether treatment response changes tissue composition, which could produce apparent expression changes without tumor-cell-intrinsic reprogramming.

If post-treatment samples differ systematically in site or cellular composition, characterize the result as a **tumor-specimen program**, unless orthogonal deconvolution or pathology supports a tumor-cell-specific interpretation.

## 3. Measurement and quality control

### 3.1 RNA
Use standard modality-appropriate QC, selected according to the assay platform:

- read/library yield, mapping or alignment rate, rRNA/mitochondrial fraction where applicable, duplication, transcript coverage, contamination, and outlier libraries;
- gene filtering based on detectable expression before multiple-testing analysis;
- inspection of principal components, sample correlations, and QC-metric associations.

Normalize RNA using an approach appropriate to count or abundance data and retain the raw data and normalization parameters.

### 3.2 Protein
Assess:

- peptide/protein identification and quantification rates;
- missingness by sample and protein;
- peptide-to-protein consistency;
- intensity distributions, retention-time/instrument drift, internal standards, and technical replicate agreement where available;
- contamination and outliers.

For proteins quantified from multiple peptides, define in advance how peptide evidence will be summarized and how discordant peptides will be handled.

### 3.3 Metabolites
Assess:

- internal-standard behavior, pooled QC performance, blank contamination, peak shape/integration, retention-time and mass-accuracy drift, and feature annotation confidence;
- missingness, detection limits, and censored values;
- technical replicate precision;
- batch structure in PCA or other unsupervised displays.

Metabolites should be reported at their actual identification confidence. An unconfirmed mass feature is not equivalent to an identified metabolite, and pathway claims based on ambiguous annotations should be downgraded.

### 3.4 Controls
Use, if available:

- pooled quality-control samples distributed across runs;
- blanks;
- reference materials;
- technical replicates;
- bridge samples run across batches;
- randomized injection order.

These controls are particularly important for metabolomics. If they were not included, the ability to separate treatment effects from batch effects is reduced and must be reported as such.

### 3.5 Outlier policy
Pre-specify that samples are excluded only for documented technical failure, identity mismatch, or pre-defined QC failure—not because they weaken a biological result. Reanalyze with and without borderline samples as a sensitivity analysis. Do not remove outliers separately by time point unless the technical reason is clear.

---

# 4. Independent units, missingness, and batch assessment

## 4.1 Independent units
- **Primary independent unit:** patient.
- **Paired observation:** pre/post samples from the same patient.
- **Technical replicates:** not independent; collapse after QC or model as technical repeats.
- **Molecular features:** correlated measurements, not independent biological replicates.

## 4.2 Missing assays
First, tabulate missingness by modality, patient, time point, batch, and QC status.

Classify likely mechanisms:

- **technical missingness** (instrument failure, insufficient material);
- **structural missingness** (assay was not attempted);
- **below-detection missingness**;
- potentially informative missingness (for example, low tumor content causing assay failure).

Do not impute absent RNA, protein, or metabolite blocks merely to create a rectangular multi-omic matrix. For feature-level analyses, use all valid pairs within each modality. For integrated models, use methods designed for missing views, or perform sensitivity analyses on complete cases while recognizing the reduced and possibly selected sample set.

## 4.3 Batch/time confounding diagnosis
For each modality, make tables and plots of:

- batch versus time point;
- batch versus patient and paired status;
- QC metrics versus batch and time point;
- sample processing date versus time point;
- missingness versus batch and time point.

### Critical metabolomics limitation
Because most post-treatment metabolomics samples share a batch, batch may be nearly indistinguishable from treatment time. If no adequate pretreatment samples occur in that batch, no post-treatment samples occur in other batches, and no bridge/QC strategy supports correction, a treatment effect is not statistically identifiable from batch effect.

**Recommended action:** seek or generate, if material and resources permit, a bridging experiment: re-run a balanced subset of matched pre/post samples across relevant metabolomics batches, including pooled QC and standards. Select the subset using blinded, pre-specified sampling across patients and signal range, not according to apparent biological results.

If a bridging experiment is impossible, label metabolite findings as **batch-confounded exploratory observations**, not as independent proof of treatment-associated metabolic reprogramming.

---

# 5. Primary paired analyses within each modality

## 5.1 Preferred model
For each feature, estimate the post-versus-pre change using either:

\[
\Delta_{if} = y_{i,\mathrm{post},f} - y_{i,\mathrm{pre},f}
\]

or a repeated-measures model such as:

\[
y_{itf} = \alpha_f + b_{if} + \beta_f \mathrm{Post}_{t} + \gamma_f^\top X_{it} + \epsilon_{itf},
\]

where \(b_{if}\) captures patient-specific baseline level and \(X\) includes only justified, non-collinear technical or biological covariates.

For RNA count data, use a count-based paired model with a patient blocking factor and appropriate library-size normalization. For continuous normalized protein and metabolite data, use paired linear models with robust variance estimation where appropriate.

### Batch adjustment rule
Adjust for batch only if the design supports estimating batch separately from time. If batch and time are completely or near-completely confounded, automated batch correction can erase a real treatment effect or manufacture one. Report both unadjusted paired contrasts and justified adjusted/sensitivity analyses.

## 5.2 Feature selection
For each modality report:

- effect size and confidence interval;
- nominal and multiplicity-adjusted significance;
- number of paired observations contributing to each estimate;
- direction of change;
- missingness and batch sensitivity;
- annotation confidence.

Use false-discovery-rate control within modality, but do not rely on adjusted \(P\)-values alone. A small cohort may yield biologically coherent moderate effects that are not individually significant; this is why pathway-level testing and validation are central.

## 5.3 RNA–protein concordance
Map RNA genes to corresponding proteins using a documented identifier map. Evaluate:

- concordance of paired effect directions;
- correlation of patient-level RNA and protein changes for matched features;
- pathway-level concordance, which is generally more realistic than one-to-one gene/protein agreement.

Lack of feature-level correlation does not necessarily invalidate a program because protein turnover and post-transcriptional regulation differ from RNA dynamics. However, any claim of transcriptionally driven protein change requires direct concordance evidence.

---

# 6. Integration: role, approach, and limits

## 6.1 Role of integration
Integration should answer a biological question that separate analyses cannot: whether multiple molecular layers support a common treatment-associated process and whether patients share coordinated response patterns.

Integration is **not** a substitute for valid within-modality QC or for resolving batch confounding. Combining biased metabolite data with RNA/protein data does not make the metabolite result valid.

## 6.2 Recommended two-level integration strategy

### Level 1: Evidence integration at pathways/networks
This is the primary approach because it is interpretable and robust for approximately 30 paired patients.

1. Produce ranked paired-change statistics separately for RNA and protein.
2. Perform directional pathway enrichment separately in each modality.
3. Identify pathways with concordant direction and acceptable stability.
4. Overlay high-confidence metabolite changes only where batch sensitivity supports interpretation.
5. Construct a program composed of:
   - a biologically coherent pathway or small collection of pathways;
   - named RNA/protein members;
   - metabolite support when defensible;
   - a pre-specified sign for each component.

This avoids forcing incompatible raw scales into one model.

### Level 2: Patient-level latent-factor integration
As a secondary discovery and heterogeneity analysis, create patient-by-feature matrices of paired changes and use a sparse multi-view latent-factor method that can accommodate missing assay blocks. The model should:

- operate on within-patient changes, not raw pre/post values;
- standardize features within modality using development-set parameters;
- permit missing views without biological-value imputation;
- use regularization and cross-validation;
- include only metabolite data passing the batch-identifiability screen, or analyze it in a separate sensitivity model.

Assess factor stability by repeatedly resampling patients and refitting the model. A factor is not a reproducible program merely because it explains variance once; its selected features, signs, and patient scores should recur across resamples.

## 6.3 Avoiding overfitting
With 30 patients, high-dimensional supervised integration is especially vulnerable to optimistic results. Therefore:

- reduce dimensionality using predefined biological sets or feature filtering independent of post/pre outcome where possible;
- tune model complexity using only the development cohort, ideally nested resampling;
- quantify stability of selected features and pathway scores;
- avoid choosing the “best” among many algorithms using the external cohort;
- prefer a small, interpretable locked signature to a large flexible model.

---

# 7. Enrichment: role, implementation, and limits

## 7.1 Role of enrichment
Enrichment converts noisy feature-level changes into interpretable biological hypotheses. It increases power when many modest changes occur in a coordinated pathway and provides the natural common language for RNA, protein, and metabolites.

Enrichment is not independent validation if it is performed on the same discovery data used to identify the features. It is a discovery-level synthesis that must be externally tested.

## 7.2 Implementation
Use curated, versioned pathway/gene-set databases selected before testing. For RNA and protein:

- rank all adequately measured features by signed paired-change statistic;
- use a ranked, directional gene-set test rather than only a thresholded “significant gene” list;
- account for gene-set overlap and multiple testing;
- inspect leading-edge molecules and whether they have consistent direction.

For metabolites:

- conduct metabolite-set or pathway analysis only for high-confidence metabolite annotations;
- account for ambiguous compound mapping;
- treat pathway enrichment as exploratory if the underlying metabolite data remain batch-confounded.

## 7.3 Directional program definition
A credible program should specify:

- pathway identity;
- direction after treatment;
- component RNA/protein features and signs;
- any metabolite evidence and its annotation/batch status;
- scoring formula;
- expected relation between layers.

For example, a score can be the mean or weighted mean of standardized signed paired changes for a locked set of RNA/protein members. Weights should be fixed from development data using a pre-specified rule, such as stability-weighted effect sizes, and not revised after external validation.

---

# 8. Internal robustness checks and acceptance/stopping criteria

## 8.1 Internal checks
Within the development cohort, require:

1. **Pair integrity:** no unresolved identity mismatch.
2. **Technical robustness:** conclusion is not driven by a small number of failed-QC or high-leverage samples.
3. **Batch robustness:** RNA/protein results remain directionally consistent under justified batch adjustments; metabolite results survive only if batch is estimable.
4. **Resampling stability:** repeat patient-level bootstrap or subsampling. Calibrate a stability threshold from the observed distribution and planned signature complexity; report selection frequencies rather than a single fit.
5. **Cross-modal coherence:** RNA/protein pathway direction is consistent, where both layers measure the process.
6. **Biological specificity:** enrichment is not solely attributable to generic low-quality, stress, or tissue-composition signatures, unless that is the intended biological finding.

## 8.2 Development stopping rule
Stop discovery and lock the program when:

- a single pre-specified or transparently selected program has passed QC, paired-effect, enrichment, and stability criteria;
- its score and all preprocessing rules are frozen;
- all sensitivity analyses are documented;
- the analysis code can be executed without manual decisions.

Do **not** continue adding/removing features after this point because doing so uses the external cohort as a tuning set.

If no program meets the criteria, the correct outcome is that the development cohort did not identify a sufficiently robust multi-omic program. The external cohort should not be used to rescue discovery.

---

# 9. External validation in the untouched cohort

## 9.1 Locked validation plan
Before unblinding the second cohort, freeze:

- the exact program members and identifiers;
- signs and weights;
- normalization and scaling rules;
- handling of missing program components;
- primary statistical test;
- acceptance criteria;
- planned sensitivity analyses.

Process the external cohort independently. Do not jointly normalize discovery and validation samples in a way that leaks validation distributions into development. If platform-specific normalization must be recalibrated within the validation cohort, use only technical controls or unsupervised cohort-internal normalization; do not change feature membership or weights.

## 9.2 Primary validation test
If the second cohort has matched pre/post samples, calculate each patient’s locked program change and test whether its direction and magnitude are consistent with the development cohort using a paired model.

Primary evidence of validation should include:

- concordant program-score direction;
- estimated effect size and confidence interval;
- an inferential test appropriate to cohort size;
- proportion of patients with expected-direction change;
- replication of leading RNA/protein pathway evidence where measured.

If the cohort is too small for decisive significance testing, report uncertainty explicitly. Directional concordance with an imprecise confidence interval is supportive but not definitive.

If the validation cohort is not paired, it cannot validate the paired treatment-change estimand directly. It may provide weaker support through cross-sectional associations, but should be labeled as such.

## 9.3 Validation outcomes
- **Pass:** locked program changes in the predicted direction with effect size compatible with development and no critical QC/batch contradiction.
- **Partial support:** pathway score replicates but individual components do not, or replication is directionally consistent but imprecise due to small sample size.
- **Fail:** opposite direction, no coherent effect despite adequate assay quality and comparable sampling, or dependence on features absent/unstable in validation.
- **Non-evaluable:** inadequate paired sampling, incompatible assay coverage, unresolved batch/QC problems, or missing key program components.

A failed validation is informative: it may indicate overfitting, biological heterogeneity, differences in treatment/sampling, or technical non-comparability. It should trigger a documented comparison of cohorts, not retrospective modification of the locked signature.

---

# 10. Troubleshooting and alternative analyses

## Problem: metabolite changes track batch
**Action:** use balanced re-runs/bridge samples if feasible; restrict to metabolites with strong technical QC; present metabolomics as exploratory if confounding persists.  
**Do not:** claim that integrated agreement proves a treatment-metabolite effect.

## Problem: RNA and protein disagree
**Possible explanations:** different temporal kinetics, post-transcriptional regulation, protein measurement coverage, tumor composition changes, or technical artifacts.  
**Action:** examine matched feature coverage, effect intervals, pathway rather than gene-level concordance, and sample identity. Retain a pathway-level program if biologically and statistically coherent; do not force agreement.

## Problem: extensive missing assays
**Action:** retain all valid modality-specific pairs; fit missing-view integration models; compare with complete-case results; report the number of informative patients per analysis.  
**Alternative:** define an RNA/protein core program and validate metabolite support separately.

## Problem: no individually significant molecules
**Action:** use ranked pathway enrichment and pre-specified module scores, then test stability and external replication.  
**Limit:** absence of individual discoveries should not be converted into a strong molecular claim without external support.

## Problem: treatment time is correlated with tissue composition
**Action:** incorporate pathology/tumor-purity information or deconvolution where justified, and report whether the program persists.  
**Limit:** without such information, call the result a specimen-level treatment-associated program.

---

# Final interpretation framework

The final claim should be calibrated to the strongest supported evidence:

- **Strongest claim:** “A paired, externally replicated RNA/protein program is associated with post-treatment tumor specimens; high-confidence metabolites provide concordant support after batch-sensitive analysis.”
- **More limited claim:** “RNA/protein data identify a reproducible treatment-associated pathway program; metabolite observations are exploratory because post-treatment batch is confounded with time.”
- **Not justified from the stated evidence alone:** “Treatment causes a tumor-cell-intrinsic metabolic program,” particularly if metabolomics batch confounding or tissue-composition differences remain unresolved.

This hierarchy preserves the advantage of paired multi-omics while preventing the most consequential technical limitation—metabolomics batch confounding—from being mistaken for biological integration.
