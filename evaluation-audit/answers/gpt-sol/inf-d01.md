# GPT-5.6 Sol / inf-d01

Original final answer, shared by both scoring rounds.

# Recommended design

Use a **paired, modality-specific analysis followed by pathway-level late integration**, and reserve the second cohort for one locked confirmatory test. The primary independent unit is the patient, not an assay feature or specimen aliquot.

The major decision gate is batch identifiability. In particular, metabolomics should contribute to the primary program **only if treatment time and metabolomics batch can be separated statistically or by a balanced bridge-rerun experiment**. If most or all post-treatment samples occupy a batch with little pretreatment representation, no integration method can recover an unconfounded treatment effect. In that case, metabolomics should remain exploratory.

Define the program as a frozen set of signed pathways/modules and, where possible, representative RNA, protein, and metabolite features. Enrichment identifies coherent biology within each modality; integration assesses whether that biology is supported across layers without treating correlated evidence as independent; external validation tests whether the frozen program transports to new patients. None of these steps turns an uncontrolled pre/post comparison into a causal treatment effect.

---

# Evidence-to-inference-to-conclusion chain

| Evidence | Inference | Consequence |
|---|---|---|
| **M1:** 30 patients have pretreatment and post-treatment samples. | Pairing can remove stable between-patient heterogeneity, but 30 independent patients is small relative to the number of molecular features. | Fit paired models, preserve patient pairs in every resampling step, use shrinkage and pathway-level summaries, and avoid treating features as replicates. |
| **M2:** RNA and protein were run in different batches; most post-treatment metabolomics samples share a batch. | Batch must be handled separately within each modality. The metabolomics treatment contrast may be weakly identifiable or nonidentifiable. | Audit the time-by-batch table and design-matrix rank before differential analysis. Do not use generic batch correction to “solve” treatment-batch confounding. Bridge-rerun or exclude metabolomics from primary inference if needed. |
| **M3:** Some assays are missing. | Complete-case analysis may waste patients and become biased; whole missing assay blocks cannot be reliably reconstructed from 30 patients. | Use all valid pairs within each modality, record reasons for missingness, avoid imputing entirely missing omic blocks for primary inference, and conduct missingness sensitivity analyses. |
| **M4:** A second small cohort is available but must remain untouched during development. | It can provide genuinely independent validation only if no feature, threshold, normalization choice, or troubleshooting decision is based on it. | Lock and timestamp the complete analysis specification before accessing cohort 2. Use one parsimonious primary program score because the validation cohort is small. |

**Conclusion:** The strongest defensible claim will be a **reproducible treatment-associated, paired molecular program**, supported by batch-adjusted RNA/protein changes and eligible metabolomics evidence, then confirmed in the untouched cohort. Causation, pathway flux, and treatment specificity require additional controls.

---

# Operational, ordered protocol

## 1. Preparation and quality checks

### 1.1 Define the estimand before examining associations

Primary estimand:

> The average within-patient post-minus-pre change in a prespecified multi-omic program among patients receiving the studied treatment.

The program should ultimately contain:

1. signed pathway or module scores;
2. the molecular features contributing to each score;
3. fixed feature and omic-block weights;
4. a patient-level paired program score;
5. a fixed missing-feature and missing-block rule.

Record whether the intended population includes all 30 patients or a clinically defined subgroup. Subgroup discovery is not supportable unless prespecified and adequately represented.

### 1.2 Construct a sample and assay manifest

For every specimen, record and reconcile:

- patient identifier and pre/post pairing;
- treatment regimen, dose, dates, and post-treatment sampling interval;
- anatomical site and tumor sampling procedure;
- assay availability and reasons for missingness;
- assay batch, plate, run order, operator, and instrument;
- specimen handling times and storage history;
- RNA/protein/metabolite quality metrics;
- tumor content or purity estimates, if available;
- technical replicates, pooled controls, blanks, and reference samples.

Treatment, sampling interval, tumor purity, and batch overlap are **unreported parameters** in the evidence packet. They must be retrieved rather than assumed.

### 1.3 Detect identity and pairing errors

Use available molecular identity checks within and across modalities, such as concordance of invariant sample-level markers, to detect swaps. Investigate rather than automatically discard discrepancies.

### 1.4 Perform QC without treatment labels where possible

In a first blinded stage:

- inspect intensity distributions, missingness, detection rates, library or peptide counts, and run-order trends;
- assess technical replicate and pooled-control variation;
- examine unsupervised sample structure colored only by technical variables;
- identify contamination, saturation, failed samples, and duplicated records.

QC thresholds are not reported. Calibrate them from the distributions of technical controls, replicates, dilution series, and assay blanks, with a prespecified false-rejection tolerance. Do not select thresholds because they strengthen the pre/post result.

After QC rules are locked, unblind pre/post labels to assess confounding.

### 1.5 Conduct an explicit batch-identifiability audit

For each modality:

1. Tabulate pre/post samples across batches.
2. Determine whether both time points occur in enough batches to estimate separate time and batch terms.
3. calculate the rank and condition of the proposed model matrix;
4. inspect whether the estimated time effect is driven by one batch;
5. assess leave-one-batch-out stability where there are enough batches.

A full-rank model does not guarantee adequate precision: sparse overlap can produce unstable estimates. Calibrate acceptable precision by simulation using blinded technical variance and the observed batch allocation.

---

## 2. Independent units

- **Independent biological units:** the 30 patients.
- **Repeated observations:** pre- and post-treatment specimens within each patient.
- **Not independent:** molecular features, technical replicates, multiple peptides from one protein, or multiple aliquots from one tumor.
- If multiple tumor cores or technical replicates exist, combine them using a prespecified rule or model them hierarchically; they must not inflate the patient count.

All bootstraps, cross-validation folds, and permutations must move the patient and their paired samples together. Cross-omic measurements from the same patient are also correlated and cannot be combined as independent studies.

---

## 3. Allocation and blinding

### 3.1 Development versus validation

- Use cohort 1 for all discovery, model selection, weighting, troubleshooting, and internal resampling.
- Keep cohort 2 inaccessible until the analysis specification, software versions, feature mapping, and acceptance criteria are frozen and timestamped.
- Do not use cohort 2 to decide which pathways “replicate,” adjust a threshold, or replace failed features.

Because cohort 1 contains only 30 patients, a fixed internal holdout would likely be inefficient. Use all of cohort 1 for final estimation, with nested patient-level resampling to quantify selection stability and optimism.

### 3.2 Laboratory allocation for any new runs

For reruns or supplementary measurements:

- balance pre- and post-treatment aliquots within every batch;
- randomize run position within technical constraints;
- include common reference material across batches;
- keep laboratory personnel blinded to time point and preliminary program status.

Do not deliberately put all members of a biological class into one technical batch.

---

## 4. Intervention and sampling

The evidence supports a paired treatment study but does not report random treatment allocation or an untreated control. Therefore:

- describe treatment exactly rather than assuming a uniform intervention;
- model major regimen or timing differences only if prespecified and adequately represented;
- record the treatment-to-biopsy interval;
- assess whether pre/post specimens differ systematically in sampling site, ischemia time, storage, or tumor content.

Changes in tumor-cell fraction or immune/stromal composition may be part of treatment response, a sampling artifact, or both. The primary analysis can estimate the total specimen-level program. A sensitivity analysis may adjust for independently measured purity or composition, but adjustment for a post-treatment variable can remove genuine treatment-associated biology and should not replace the primary result.

Without an untreated or alternative-treatment group, the pre/post contrast can also include time, repeated-biopsy, disease-progression, and sampling effects. Thus use “treatment-associated,” not “treatment-induced.”

---

## 5. Measurements and preprocessing

Process each modality separately before integration.

### 5.1 RNA

- Filter features using a label-blind expression/detection rule.
- Normalize using a method appropriate to the measurement scale.
- retain normalized expression and QC uncertainty;
- map features to a frozen gene identifier and pathway database version.

### 5.2 Protein

- Resolve peptides to proteins using a frozen mapping rule.
- Flag proteins supported by ambiguous peptides.
- normalize and assess run-order or batch drift within protein data only;
- map proteins to the same gene-level identifier system where biologically justified.

RNA and protein absolute values should not be directly compared. Concordance concerns the direction and relative strength of paired changes or pathway enrichment.

### 5.3 Metabolites

- Remove blank-associated contaminants and poorly identified features according to calibrated QC rules.
- use pooled controls and internal standards to assess drift;
- preserve metabolite identification confidence and one-to-many pathway mappings;
- distinguish measured concentration changes from pathway flux: metabolite accumulation does not by itself establish increased pathway activity.

### 5.4 Missing measurements

Separate:

1. an entirely missing assay or omic block;
2. a missing paired specimen;
3. feature-level values below detection;
4. sporadic technical missingness.

Primary rules:

- do not impute an entirely missing omic block from the other modalities;
- analyze each modality using all patients with valid information for that modality;
- for feature-level censoring, use a censoring-aware method only if dilution or detection data support that interpretation;
- otherwise perform complete-pair and model-based sensitivity analyses;
- report missingness by time, batch, clinical factors, and QC status.

If post-treatment assay failure is related to response, missing-at-random models can be biased. Explore inverse-probability weighting or pattern-mixture sensitivity analyses using pretreatment and technical variables, without presenting unverifiable imputation assumptions as fact.

---

## 6. Controls

Use available controls and add them for any reruns:

- blanks and contamination controls;
- pooled sample controls across run order;
- internal standards or spike-ins where assay-appropriate;
- technical replicates;
- shared bridge samples across batches;
- negative-control features or pathway sets chosen before outcome analysis;
- null analyses based on valid patient-level resampling.

Technical controls reveal drift and precision but do not substitute for biological controls. In particular, pooled metabolomics controls cannot distinguish treatment from batch if treatment time is perfectly confounded with batch.

### Proposed experiment: metabolomics bridge-rerun

If stored aliquots are available, rerun a balanced set of pre- and post-treatment specimens together in one or more new batches, with randomized positions and common reference samples. Select the number of bridges through a variance/precision calculation based on blinded technical replicates.

The bridge must create actual overlap between treatment times and batches. If this cannot be achieved, keep metabolomics out of the primary treatment program.

---

## 7. Analysis

### 7.1 Modality-specific paired effects

For each feature, fit a paired model of the form

\[
Y_{ift}=\alpha_f+u_{if}+\beta_f\,Post_{it}+\gamma_f^\top Batch_{it}+\theta_f^\top Z_{it}+\epsilon_{ift},
\]

where:

- \(i\) is patient;
- \(t\) is pre or post;
- \(u_{if}\) represents the patient-specific baseline;
- \(\beta_f\) is the treatment-associated paired change;
- \(Z\) contains only prespecified, interpretable covariates.

Use moderated or partially pooled variance estimates appropriate for many features and few patients. Report effect sizes and confidence intervals, not only multiplicity-adjusted significance.

Do not apply batch correction without retaining the post-treatment contrast in the design. If batch and post status are collinear, empirical batch correction may erase the biological contrast or mislabel technical effects as biology.

### 7.2 Internal robustness

For each modality:

- bootstrap patients, preserving their paired and cross-omic records;
- calculate sign, rank, and selection stability;
- conduct leave-one-patient-out diagnostics;
- perform leave-one-batch-out analyses where possible;
- repeat analyses with robust regression or downweighting of verified technical outliers;
- compare analyses including and excluding questionable samples, reporting both.

Use label swaps or residual permutations only when exchangeability conditional on batch is defensible. If treatment time is tied to batch, unrestricted pre/post permutation is not a valid null.

### 7.3 Enrichment

Enrichment should follow feature-level modeling, not replace it.

1. Freeze pathway libraries and identifier mappings before testing.
2. Rank features by signed paired effect statistics.
3. test pathways within each modality using methods that account for correlated features;
4. correct for testing the selected pathway collection;
5. retain pathway direction, effect size, uncertainty, feature coverage, and leading contributors;
6. assess pathway stability across patient bootstraps.

**Role of enrichment:** it reduces reliance on single noisy features and asks whether coordinated biology changes within an omic layer. It does not remove batch effects, establish causality, or prove metabolic flux. Large or densely measured pathways should not receive automatic preference.

### 7.4 Primary integration strategy: pathway-level late integration

Do not concatenate raw RNA, protein, and metabolite matrices as the primary analysis. Their scales, coverage, missingness, and batch structures differ.

Instead:

1. estimate paired effects separately in each modality;
2. calculate signed pathway evidence separately;
3. align pathways using a frozen cross-modality mapping;
4. combine signed pathway evidence with equal or prespecified reliability-based omic weights;
5. calibrate the combined statistic by patient-level resampling that preserves cross-omic dependence;
6. require a candidate program to have coherent support from a prespecified number of identifiable modalities.

Give each omic block comparable influence so that RNA does not dominate merely because it has more features. Reliability weights must be based on QC or technical precision, not on which weighting produces the strongest treatment signal.

RNA and protein measurements of the same gene are biologically related and are not independent replications. Agreement strengthens interpretation; disagreement can reflect regulation, timing, cell composition, or technical error and should not be forced away.

**Role of integration:** it identifies a coherent program spanning molecular layers and creates a transportable summary. Integration cannot rescue confounding or turn missing data into observed evidence.

### 7.5 Secondary integration alternatives

As sensitivity analyses, consider:

- gene-centric RNA/protein concordance;
- sparse multi-block latent-factor models;
- supervised multi-block scores predicting pre versus post status;
- network-based modules.

With 30 patients, these methods are vulnerable to overfitting. All feature selection, normalization, and tuning must occur inside patient-level resampling. They should not replace the simpler pathway-level primary analysis unless they show strong stability and are fully frozen before validation.

### 7.6 Construct the locked patient-level score

From stable development-cohort results, define one primary score:

1. select the final pathways and representative features according to prespecified stability and multiplicity rules;
2. orient every component so that a higher score denotes the same post-treatment direction;
3. standardize paired changes using development-cohort parameters;
4. summarize features within each omic, then combine omic blocks with fixed weights;
5. specify minimum feature coverage and the handling of a missing block;
6. freeze all coefficients, mappings, and scaling values.

A fixed reduced-block score may be prespecified for patients missing an assay, but it is a distinct estimand and should not silently replace the full score.

### 7.7 External validation

Only after the lock:

1. open cohort 2 and apply the frozen QC and mapping rules;
2. assess whether its treatment, sampling time, assay platforms, and paired structure match the target setting;
3. compute the frozen score without refitting or reselection;
4. test whether the paired post-minus-pre score changes in the predicted direction;
5. report the effect size, confidence interval, and individual paired changes;
6. test pathway and feature replication only as secondary outcomes.

Because cohort 2 is small, the primary external test should be the single composite score rather than hundreds of individual features. If a feature is absent on the external platform, follow the locked coverage rule; do not replace it after seeing outcomes.

**Role of external validation:** it tests transportability and guards against development-cohort overfitting. It does not repair bias shared by both cohorts, such as the same time-batch confounding or absence of untreated controls.

---

## 8. Acceptance and stopping criteria

Numerical thresholds are unreported and must be chosen before outcome analysis. Calibrate them as follows:

- **Technical QC thresholds:** from blinded control, replicate, blank, and dilution data.
- **Minimum analyzable sample count:** from simulations using blinded variance, a scientifically meaningful minimum effect, and the desired confidence-interval width.
- **Multiplicity and stability thresholds:** by null resampling under valid exchangeability and simulations targeting a prespecified false-program rate.
- **External minimum effect:** based on scientific relevance and technical precision, not the development effect alone.

### Accept a development program only if

- the paired time effect is estimable separately from batch;
- its direction and pathway enrichment are stable to patient resampling and reasonable QC choices;
- it is not driven by one patient or one technical batch;
- it has coherent support from the prespecified number of eligible modalities;
- all score components and validation rules can be frozen.

### Accept external reproduction only if

- the frozen primary score changes in the predicted direction;
- its prespecified confidence test excludes no effect and, if required, effects below the prespecified minimum;
- assay coverage meets the locked criterion;
- no refitting or post hoc pathway substitution was used.

### Stop or downgrade the analysis if

- sample identities or pairings cannot be resolved;
- the post-treatment term is rank-deficient with batch;
- bridge reruns fail to create usable treatment-by-batch overlap;
- effective paired sample size is below the calibrated precision requirement;
- QC failure is strongly differential by time point and cannot be repaired;
- the validation cohort is technically incompatible with the locked score.

If external validation fails, label the program unreplicated. Do not revise it using cohort 2 and retest in the same cohort.

---

## 9. Troubleshooting

| Problem | Response |
|---|---|
| Metabolomics time and batch are confounded | Perform the balanced bridge-rerun; otherwise exclude metabolites from primary inference and report them descriptively. |
| RNA or protein batch overlap is sparse | Fit explicit batch terms, quantify variance inflation, use leave-one-batch-out checks, and downgrade unsupported results. |
| One patient drives a pathway | Verify identity/QC, use robust models, and report analyses with and without the patient; exclusion requires a technical reason. |
| Many missing assays | Analyze modality-specific pairs, avoid whole-block imputation, model observation probability, and report sensitivity to missing-not-at-random assumptions. |
| RNA and protein disagree | Check feature mapping, isoforms, tumor composition, and timing; retain disagreement rather than selecting the favorable layer. |
| Metabolite annotations are ambiguous | Carry identification confidence and alternative mappings through enrichment; avoid mechanistic claims based on one uncertain metabolite. |
| External platform lacks features | Apply the frozen coverage rule. If coverage fails, call validation technically unevaluable rather than biologically negative. |
| Program changes under small analysis choices | Report instability and simplify to more robust pathways; do not claim a reproducible program. |

---

# Alternatives and limits

A raw early-integration or supervised classifier could be more sensitive if all assays were complete, well balanced, and much larger in sample size. Under M1–M3, it is more likely to learn batch, platform scale, and missingness. Late pathway integration is therefore the preferred primary strategy.

The analysis can identify reproducible association, not mechanism or causality. Stronger causal interpretation would require a **proposed future experiment** with randomized treatment or a suitable untreated/time-matched control, standardized sampling, and balanced assay batches. Orthogonal targeted assays of locked representative markers could confirm measurement accuracy, but they would not replace independent patient-level validation.
