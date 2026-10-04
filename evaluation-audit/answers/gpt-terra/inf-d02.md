# GPT-5.6 Terra / inf-d02

Original final answer, shared by both scoring rounds.

# Proposed auditable bulk RNA-seq differential-expression plan  
**Status: proposed only. No files, sample sheet, count matrix, reference version, or software environment has been supplied; therefore nothing in this plan has been executed and no result is claimed.** All paths, versions, thresholds, sample numbers, and parameters below are placeholders to be fixed prospectively, recorded, and versioned before analysis.

## 1. Conclusion and governing principle

The proposed primary analysis is a gene-level negative-binomial differential-expression model with a pre-specified treatment-versus-control contrast, using DESeq2 or an equivalently specified negative-binomial GLM implementation. The analysis must preserve replication at the level of **independent treatment allocation**, not at the level of reads, sequencing lanes, libraries, aliquots, cells, or technical wells.

For an effect intended to generalize across donors, the design must include multiple independently sampled donors. Multiple wells from one donor can support inference about treatment allocation within that donor, but cannot establish across-donor heterogeneity or a donor-population treatment effect. Adding a donor random effect to data from one donor would not create missing donor replication.

The proposed workflow is auditable because every input, reference, parameter, program, intermediate, result, and plot will be immutable or content-addressed, and every difference between source materials and analysis materials will be reported.

---

## 2. Evidence → inference → conclusion chain

| Evidence location | Evidence | Inference | Proposed design consequence |
|---|---|---|---|
| Fixed evidence packet, source summary | The DESeq2 record describes negative-binomial generalized linear models, information sharing for dispersion and effect estimation, inference, and diagnostics. | A negative-binomial count model is appropriate for proposed gene-level count analysis, with dispersion estimation and shrinkage performed according to a versioned implementation. | Use a specified DESeq2 negative-binomial GLM for the primary analysis, subject to count and design checks. |
| Fixed evidence packet, curator interpretation | Statistical modelling does not create missing independent treatment replication. | Technical replication, extra sequencing depth, or a more complex model cannot replace independently allocated biological units. | Define replication from the allocation scheme before sequencing; do not count reads, lanes, or technical libraries as biological replicates. |
| Fixed evidence packet, curator interpretation | Donor and well inference are distinct; a single donor cannot identify across-donor heterogeneity merely by adding a donor random effect. | A within-donor result and an across-donor result have different estimands and valid sample sizes. | Require multiple donors for donor-generalizable conclusions; label any one-donor analysis as donor-specific. |
| Fixed evidence packet, source summary | The read record is partial and no actual count matrices, sample sheets, or file versions are supplied. | Existing inputs and provenance cannot currently be verified. | Do not execute. Create a manifest, sample sheet, source-difference audit, and reproducible workflow before any computation. |

**Conclusion:** the proposed analysis is feasible only after the allocation hierarchy, sample metadata, immutable raw-data inventory, and reference resources are supplied and pass the pre-specified audit.

---

## 3. Proposed estimand and independent-unit rules

### 3.1 Primary estimand

The primary estimand will be declared before allocation:

> The adjusted average difference in gene expression between treatment and control in the defined biological population, under the specified intervention duration, tissue/cell source, sampling procedure, and reference annotation.

The exact population, treatment dose, duration, tissue, and timepoint are currently **unreported parameters** and must be added to the protocol.

### 3.2 Unit hierarchy

The protocol will explicitly distinguish:

1. **Treatment-allocation unit** — the unit independently randomized or assigned to treatment/control, for example an animal, donor-derived culture well, organoid, or experimental vessel.
2. **Biological sampling unit** — the donor, animal, or source specimen from which material is obtained.
3. **Library unit** — one RNA-seq library from an RNA preparation.
4. **Technical sequencing unit** — lane, run, read pair, or re-sequenced library.

Only independently allocated biological units contribute treatment replication. Reads and technical units contribute measurement precision, not independent treatment replication.

### 3.3 Required design branches

**A. Treatment allocated to whole animals or whole donors**  
The animal/donor is the experimental unit. One RNA-seq observation per eligible animal/donor is the default. Technical replicate libraries or lanes are merged according to the pre-specified technical-replicate rule.

**B. Treatment allocated independently to wells within each donor**  
The well is the treatment-allocation unit for a within-donor causal comparison. However, if the scientific claim is intended to generalize across donors, the number of independently sampled donors—not merely the number of wells—determines evidence about donor-to-donor variation.

- With multiple donors and one eligible independently allocated well per condition per donor, a paired/block analysis can use donor as a fixed blocking factor.
- With multiple treatment wells per donor, a simple sample-level model that treats all wells as independent across donors may underestimate uncertainty if wells from the same donor remain correlated. The protocol must pre-specify either:
  - a donor-level aggregation/summary strategy for the donor-generalizable estimand, or
  - a cluster-aware/hierarchical sensitivity analysis with sufficient donors.
- With one donor only, analysis may estimate a result conditional on that donor and experimental context, but must not claim across-donor generalizability or donor heterogeneity.

**C. Technical replicate libraries from one allocation unit**  
Technical libraries, split aliquots, and multiple sequencing lanes from the same allocation unit are not additional biological replicates. The default proposed rule is to merge lane-level reads for the same library and, where justified by laboratory identity and QC, combine technical-library counts before the differential-expression model. All merges must remain reversible and recorded.

---

## 4. Immutable inputs and no-hidden-state architecture

### 4.1 Proposed immutable input register

Before execution, create a read-only `input_manifest.tsv` or equivalent versioned table. Each file or object will have:

- `asset_id`
- role: raw FASTQ, sample metadata, reference FASTA, annotation GTF/GFF, index, count file, script, parameter file, container, or result
- original URI/path and storage version/object identifier
- file size
- cryptographic checksum, proposed: SHA-256
- creation/receipt date and source organization
- source-document or repository accession
- parent asset(s), if derived
- access status
- notes on consent or restricted access, if applicable.

Raw FASTQ files and original metadata will never be overwritten. Derived assets will be written to new immutable locations with their own hashes.

### 4.2 Proposed reproducible execution record

The workflow will use a declared workflow engine or scripted directed acyclic graph, with:

- repository URL and immutable commit identifier;
- workflow release tag;
- parameter file checksum;
- container image digest or package-lock/environment-lock checksum;
- operating-system and architecture record;
- reference/index checksums;
- complete command log;
- standard output/error logs;
- random seed where an algorithm uses randomness;
- timestamped run manifest;
- output checksums.

Manual editing of count matrices, sample labels, annotation files, or results is prohibited. If correction is needed, it will be a new versioned input with a documented rationale and source-difference report.

---

## 5. Proposed sample sheet

No actual sample sheet exists in the evidence packet. The following are proposed schemas, not records.

### 5.1 Biological-analysis sample sheet: one row per modeled biological observation

`analysis_samples.tsv` must include at least:

| Field | Purpose |
|---|---|
| `analysis_sample_id` | Immutable identifier used in count matrix columns |
| `allocation_unit_id` | Unit independently assigned to treatment/control |
| `biological_source_id` | Animal, donor, colony, or source specimen identifier |
| `donor_id` | Required when donor-derived material is used |
| `treatment` | Pre-specified level, e.g., control/treatment; analyst-blinded code until QC lock where feasible |
| `treatment_dose`, `duration`, `sampling_time` | Intervention definition |
| `allocation_date`, `sampling_date` | Temporal provenance |
| `processing_batch`, `extraction_batch`, `library_batch`, `sequencing_run`, `lane` | Technical factors |
| `paired_set_id` | Donor/animal pairing or matched set, if applicable |
| `allocation_sequence` | Randomization order or allocation record |
| `eligibility_status` | Pre-specified inclusion status |
| `qc_status` | Pass/fail/flag after blinded QC review |
| `exclusion_reason` | Controlled vocabulary; never blank for excluded samples |
| `count_file_asset_id` | Manifest link to the final count source |
| `notes` | Non-identifying deviations |

### 5.2 Library/lane sheet: one row per technical asset

`libraries.tsv` will link each `analysis_sample_id` to:

- `library_id`, `lane_id`, `fastq_r1_asset_id`, `fastq_r2_asset_id`;
- library-preparation kit and version;
- RNA input amount and extraction method;
- strandedness declaration;
- read layout and read length;
- sequencing platform and run;
- technical-replicate relationship;
- proposed merge decision and justification.

A count-matrix column must map unambiguously to one `analysis_sample_id`. Technical lanes must not appear as separate biological columns unless they are genuinely separate independently allocated biological units.

---

## 6. Ordered proposed operational protocol

## 6.1 Preparation and quality-system setup

1. **Freeze the protocol before enrollment/allocation.** Register the biological question, estimand, primary contrast, allocation unit, donor population, planned covariates, QC rules, stopping rules, and FDR family.
2. **Create the immutable input register and source register.**
3. **Calibrate sample size before intervention.** Use pilot data, historical validated assay data, or simulations based on plausible dispersion, library depth, effect-size, donor variability, and dropout ranges. The calibration must vary the number of independent donors/allocation units, not just reads or technical replicates.
4. **Lock the software/reference environment.** Placeholder versions must be replaced with actual version strings, release dates, checksums, and container/package-lock hashes before execution.
5. **Train and document blinding procedures.** The data analyst should receive blinded treatment labels during initial QC when operationally feasible.

**Unreported parameters requiring calibration:** required independent-unit number; acceptable dropout rate; sequencing-depth target; RNA-input requirement; RNA-quality threshold; acceptable mapping/count-assignment ranges; and FDR threshold.

## 6.2 Allocation and blinding

1. Randomize treatment allocation at the declared allocation-unit level.
2. Use blocked or stratified randomization across donor, processing day, sex or other pre-treatment factor only when those factors are scientifically relevant and known before treatment.
3. Balance treatment/control across extraction batch, library-preparation batch, sequencing run, lane, and processing order as far as feasible.
4. Do not process all controls before all treated samples.
5. Retain the randomization list, allocation seed or procedure, responsible person, and deviations in an immutable allocation log.
6. Blind sample identifiers to treatment during extraction, library preparation, and initial QC where feasible; preserve a secure treatment key.

## 6.3 Intervention and sampling

1. Apply treatment/control according to the locked intervention specification.
2. Record deviations, deaths, contamination, failed cultures, delayed sampling, and all exclusions contemporaneously.
3. Sample all groups at the pre-specified timepoint using the same collection protocol.
4. Do not replace failed allocation units silently. Any replacement requires a documented allocation-consistent procedure and must appear in the sample sheet.

## 6.4 RNA and sequencing measurements

1. Measure RNA quantity and integrity using a laboratory-qualified procedure.
2. Set RNA acceptance thresholds from a pre-treatment assay-validation or blinded pilot distribution; record the rationale and threshold in the parameter file. Do not select a threshold after inspecting treatment-associated expression results.
3. Randomize/balance extraction, library preparation, and sequencing order across treatment and donor.
4. Record strandedness, chemistry, read configuration, platform, run, lane, and library indexes.
5. Include appropriate process controls:
   - extraction blanks and library blanks to detect contamination;
   - an external or standardized RNA control where the laboratory has validated its use;
   - a pre-specified positive process control, if available.
   
Controls are QC tools, not biological replicates. Spike-ins will not automatically replace standard library-size normalization; their intended scaling role must be justified and declared prospectively.

## 6.5 Read and count quality checks

The following are proposed checks, with acceptance ranges calibrated from qualified pilot/control data and fixed before unblinding:

- FASTQ integrity and checksum verification;
- adapter/quality-content assessment;
- read-pair and read-count consistency;
- alignment or quantification rate;
- rRNA, mitochondrial, intergenic, intronic, and exonic fractions as relevant to the protocol;
- duplicate/library-complexity metrics where interpretable;
- strandedness confirmation;
- gene-body coverage or analogous RNA-degradation metric;
- sample identity checks where genotype, sex markers, or other lawful identifiers are available;
- contamination checks using blanks and expected controls;
- library-size and detected-gene distributions;
- PCA/sample-distance plots of transformed counts, initially with masked treatment labels;
- batch and donor association checks.

QC thresholds must not be tuned to improve treatment separation. A sample failing a hard pre-specified assay criterion is excluded only with a recorded technical reason. Statistical “outlier” status alone is a flag requiring investigation, not an automatic deletion rule.

---

## 7. Proposed reference, alignment, and counting specification

Before counting, the following placeholders will be replaced by immutable identifiers:

- genome assembly: `${ASSEMBLY_ACCESSION_AND_VERSION}`;
- reference FASTA URI, SHA-256, and release date;
- annotation provider and release: `${ANNOTATION_PROVIDER_RELEASE}`;
- GTF/GFF URI and SHA-256;
- gene identifier namespace and version;
- aligner or quantifier name/version/container digest;
- index-generation command and index checksum;
- read filtering, multimapping, overlap, and strandedness policy;
- gene-level counting tool/version and command;
- treatment of overlapping genes and non-unique mappings.

The proposed primary endpoint is **gene-level integer counts** generated against one locked genome/annotation pair. The count matrix will retain raw counts; normalized/transformed matrices are derived objects used only for specified purposes.

A proposed annotation-change audit will report:

- genes added, removed, split, merged, or renamed relative to any earlier annotation;
- changes in gene identifier mapping;
- count-matrix differences attributable to annotation or counting-policy changes;
- whether the primary analysis was rerun under a new annotation, rather than mixed with old results.

---

## 8. Proposed differential-expression analysis

## 8.1 Count model

For gene \(g\) and modeled biological sample \(i\), the proposed model is:

\[
K_{gi} \sim \mathrm{NB}(\mu_{gi}, \alpha_g)
\]

\[
\mu_{gi} = s_i q_{gi}, \qquad \log(q_{gi}) = X_i\beta_g
\]

where \(K_{gi}\) is the raw gene count, \(s_i\) is a library-size normalization factor, \(\alpha_g\) is gene-specific dispersion estimated with information sharing, and \(X_i\) is the pre-specified design matrix.

The proposed implementation is DESeq2 at locked `${DESEQ2_VERSION}`, with its recorded normalization, dispersion estimation, and inference settings. Any effect-size shrinkage method and version will be reported separately; shrinkage for ranking/display must not silently replace the primary hypothesis-test specification.

## 8.2 Design and primary contrast

The exact design depends on the allocation structure:

- **Unpaired independently allocated biological units:**  
  `~ processing_batch + treatment`

- **Paired or matched donor design with treatment/control within donor:**  
  `~ donor_id + processing_batch + treatment`

- **Additional pre-treatment covariates:**  
  Include only covariates defined before outcome inspection, scientifically justified, sufficiently represented, and not collinear with treatment.

The proposed primary contrast is:

> `treatment` versus `control`, adjusted for the locked design terms.

The reference treatment level, coefficient name, and contrast vector will be stored in the parameter file and result manifest.

No model can estimate a treatment effect separately from batch if treatment is completely confounded with batch. If the design matrix is rank-deficient or treatment is fully confounded with donor, processing batch, or another covariate, the proposed action is to stop that confirmatory analysis, report non-identifiability, and redesign or restrict the claim rather than remove terms opportunistically.

## 8.3 Filtering, FDR, and reporting

1. Apply a pre-specified, treatment-blind expression filter based on total or minimally required count evidence across samples. Record the exact rule and resulting tested-gene universe.
2. Fit the negative-binomial model to retained genes.
3. Obtain the treatment-control test statistic and raw \(p\)-value for every tested gene.
4. Control false discovery rate across the complete primary tested-gene family using Benjamini-Hochberg, with `${FDR_ALPHA}` fixed before unblinding.
5. Report, for every tested gene:
   - stable gene ID and annotation release;
   - gene symbol if available, labeled as annotation-dependent;
   - base mean/count summary;
   - estimated log2 fold change;
   - standard error;
   - raw \(p\)-value;
   - adjusted \(p\)-value;
   - shrinkage method/status if used;
   - filter status;
   - model and contrast identifiers.

An effect-size threshold, if used for biological prioritization, will be an additional pre-specified criterion and will not be substituted for FDR control.

## 8.4 Planned sensitivity analyses

These are proposed, not executed:

- alternate valid count-model implementation under the same design and tested-gene universe;
- analysis excluding documented technical failures only;
- analysis with/without a justified pre-treatment covariate;
- donor-level or cluster-aware analysis when repeated wells are nested within donors;
- influence diagnostics identifying whether a result is dominated by one donor or allocation unit;
- assessment of treatment-by-donor heterogeneity only when multiple donors and an identifiable design support it.

Sensitivity analyses will not be used to select the most favorable result. Their full result tables and rationale will be released.

---

## 9. Proposed plot regeneration

Every plot will be generated from immutable inputs by a versioned script, not manually edited. The plot manifest will contain source data hashes, script commit, parameter hash, software environment hash, and output image hash.

Proposed plots include:

1. sample-flow diagram: enrolled, allocated, sampled, sequenced, QC-passed, modeled;
2. sequencing/count QC distributions;
3. mapping/assignment metrics by batch and masked treatment;
4. PCA or multidimensional scaling of transformed counts, labeled by batch, donor, and treatment after QC lock;
5. sample-to-sample distance heatmap;
6. dispersion-versus-mean diagnostic;
7. MA plot for the primary contrast;
8. volcano plot, clearly marked as descriptive and not a substitute for FDR table;
9. \(p\)-value distribution and independent-filtering diagnostic;
10. donor- or allocation-unit-level effect display for selected pre-specified genes or pathways;
11. model-design and batch-balance plots.

The transformed-count plots are diagnostic only; the primary inference remains based on raw counts in the negative-binomial model.

---

## 10. Proposed source-difference audit

A `source_difference_audit.tsv` will be produced before analysis and at release. It will compare:

1. declared study materials and repository/LIMS assets;
2. raw-file manifest and files actually consumed;
3. sample sheet and count-matrix columns;
4. allocation log and treatment labels;
5. reference/annotation declarations and files actually used;
6. prior versus current scripts, parameters, environments, and output tables.

Required checks include:

- set differences in sample IDs, library IDs, and FASTQ assets;
- duplicate or missing files;
- checksum mismatches;
- changed treatment, donor, batch, or exclusion fields;
- count columns without sample-sheet rows or vice versa;
- changed reference or annotation identifiers;
- changed gene mappings and tested-gene universe;
- changed software/container/parameter versions;
- old-versus-regenerated result-table and plot hashes.

Every difference will be categorized as **expected**, **approved correction**, **unresolved discrepancy**, or **analysis-blocking**. The current evidence packet permits no completed source-difference audit because the underlying files and versions are absent. Its current status is therefore **not assessable**, not “passed.”

---

## 11. Acceptance, stopping, and troubleshooting criteria

### Acceptance before confirmatory analysis

Proceed only if all of the following are met:

- immutable raw-data and metadata manifest is complete;
- allocation unit and target population are documented;
- biological replication supports the intended claim;
- treatment is not fully confounded with batch/donor/covariates;
- sample sheet and count matrix reconcile exactly;
- reference and annotation versions are locked and hashed;
- QC exclusions have documented pre-specified or technically verified reasons;
- workflow regenerates counts, models, tables, and plots from declared inputs.

### Stop or replan if

- independent treatment allocation was not achieved;
- only one donor is available for an intended across-donor claim;
- treatment is fully confounded with a technical factor;
- treatment labels, input checksums, or sample identities cannot be reconciled;
- reference/index provenance is missing;
- failures leave insufficient independently allocated units according to the prospective calibration;
- a required batch/process control indicates unresolved assay contamination or failure.

No study will stop because a desired FDR result has or has not appeared.

### Troubleshooting principles

- **Low mapping/assignment:** verify reference version, strandedness, read orientation, adapter trimming, contamination, and RNA quality before excluding samples.
- **Batch-separated PCA:** inspect allocation/balance and batch metadata; include identifiable pre-specified technical factors in the design; do not batch-correct counts and then treat corrected values as primary DE counts.
- **Unexpected donor clustering:** confirm donor IDs and pairing; preserve donor structure; revise the estimand or use a cluster-aware analysis rather than declaring wells independent across donors.
- **Low replication:** report descriptive results only within the support of the allocation design; obtain additional independent units for confirmatory inference.
- **Annotation mismatch:** rerun from raw/count-generation stage using one locked annotation; do not merge results across annotation releases without a mapping audit.

This proposed plan provides a reproducible analysis framework, but execution and scientific conclusions must await the missing raw inputs, sample metadata, reference versions, allocation records, and pre-specified calibration decisions.
