# Qwen3.8 Max (0902) / inf-d02

Original final answer, shared by both scoring rounds.

**Conclusion and recommended next action — all analyses are proposed, not executed**  
The safest next action is to freeze an audit-ready protocol before any wet-lab or computational work is done: define the independent treatment-allocation unit, record an immutable input manifest, specify a sample sheet, fix reference/annotation versions as placeholders, define a DESeq2-style negative-binomial count model, pre-specify the treatment-versus-control contrast and FDR rule, require deterministic plot regeneration, and require a source-difference audit. No differential-expression claim should be made until actual files exist, hashes are recorded, and the independent replication required for the chosen inferential scope is verified. Because no count matrices, sample sheets, FASTQ files, reference files, or versions are supplied, every path, version, numeric setting, and threshold below is a placeholder to be recorded later; nothing described here has been run.

---

## 1. Evidence-to-inference-to-conclusion chain

| Evidence location in supplied packet | Inference | Proposed design consequence |
|---|---|---|
| DESeq2 record: negative-binomial generalized linear models; information sharing for dispersion and effect estimation; inference and diagnostics | Bulk RNA-seq read counts can be modeled as overdispersed counts, with borrowing of information across genes and diagnostic checks | Use a DESeq2-style negative-binomial GLM as the proposed count model, with mandatory diagnostics and immutable count inputs |
| DESeq2 record / curator interpretation: modelling does not create missing independent treatment replication | Statistical models cannot replace absent independent biological replication | The analysis must count independent treatment-allocation units, not technical wells or lanes, as the replicates for treatment inference |
| Experimental-unit interpretation: experimental unit depends on independent treatment allocation; donor and well inference are distinct; a single donor cannot identify across-donor heterogeneity merely by adding a donor random effect | The unit of inference is determined by where treatment was independently assigned; donor-level and well-level conclusions are different; one donor cannot support donor-population heterogeneity | The sample sheet must record `allocation_level`, `allocation_unit_id`, `donor_id`, `well_id`, and `inferential_scope`; models must not use random effects or blocking to manufacture donor-level generalization |
| Read record is partial; no count matrices, sample sheets, or file versions supplied | The analysis cannot be executed or validated now | All paths, checksums, versions, thresholds, and numeric settings are placeholders; the plan is proposed only and must pass a source-difference audit before execution |

---

## 2. Ordered proposed protocol

### 2.1 Preparation and quality checks — proposed

1. **Define the causal question.**  
   Specify:  
   - treatment definition;  
   - control definition;  
   - sampling time;  
   - tissue/cell type;  
   - biological population to which conclusions should apply;  
   - whether inference is at donor level, well/aliquot level, or another allocation level.

2. **Draw a minimal causal diagram.**  
   Include treatment, outcome, donor, batch, processing date, lane, library preparation, and any known biological covariates. The diagram determines which variables are confounders, blockers, or colliders. Do not adjust for variables affected by treatment unless the causal question explicitly requires it.

3. **Create a placeholder configuration file.**  
   The configuration must contain no hidden state. Every parameter must be written in a tracked text file. Example placeholder fields:

   ```yaml
   project_id: [PROJECT_ID_PLACEHOLDER]
   analysis_mode: proposed_not_executed
   raw_data_dir: [RAW_DATA_DIR_PLACEHOLDER]
   output_dir: [OUTPUT_DIR_PLACEHOLDER]
   genome_fasta: [GENOME_FASTA_PATH_PLACEHOLDER]
   genome_build: [GENOME_BUILD_PLACEHOLDER]
   genome_sha256: [GENOME_SHA256_PLACEHOLDER]
   annotation_gtf: [ANNOTATION_GTF_PATH_PLACEHOLDER]
   annotation_version: [ANNOTATION_VERSION_PLACEHOLDER]
   annotation_sha256: [ANNOTATION_SHA256_PLACEHOLDER]
   gene_id_type: [GENE_ID_TYPE_PLACEHOLDER]
   seed: [SEED_PLACEHOLDER]
   threads: [THREADS_PLACEHOLDER]
   fdr_alpha: [FDR_ALPHA_PLACEHOLDER]
   lfc_threshold: [LFC_THRESHOLD_PLACEHOLDER]
   cooks_cutoff: [COOKS_CUTOFF_PLACEHOLDER]
   min_replicates_for_replace: [MIN_REPLICATES_FOR_REPLACE_PLACEHOLDER]
   ```

4. **Calibrate unknown parameters, do not invent them.**  
   For every placeholder, record the calibration procedure:
   - `fdr_alpha`: chosen from decision context, validation capacity, and acceptable false-discovery burden.
   - `lfc_threshold`: chosen from biological relevance and measurement error estimated from controls, pilot data, or published comparable data.
   - `cooks_cutoff` and outlier rules: chosen from model diagnostics and control behavior.
   - minimum independent replicates: chosen from power or precision considerations using pilot or external dispersion/effect-size information; if no information exists, state that inference is not supported.

5. **Verify that no execution is claimed.**  
   Because no files are supplied, all file paths, hashes, versions, and thresholds remain placeholders. The protocol is a design and acceptance specification, not a completed analysis.

---

### 2.2 Independent experimental units — proposed rules

The experimental unit is the smallest entity to which treatment is independently allocated. This determines the replication used for differential-expression inference.

| Treatment allocation situation | Independent unit for primary DE inference | Count handling | Allowed inferential scope |
|---|---|---|---|
| Treatment allocated to whole donor/animal/person | Donor/animal | Sum or collapse technical subsamples to one count profile per donor, or use one representative library per donor by pre-specified rule | Across donors only if multiple independently allocated donors exist |
| Treatment allocated to wells/aliquots from each donor | Well/aliquot, if truly independently treated | One count profile per treated well/aliquot; donor may be included as a blocking factor if estimable | Conditional on the donors used; if only one donor, no across-donor heterogeneity or population claim |
| Treatment allocated to batch/plate, not to individual biological units | Batch/plate is not a valid biological treatment replicate unless treatment was independently allocated at that level | Do not treat wells/lanes within one allocated unit as independent | Claims limited to the allocated unit; usually insufficient for treatment inference |
| One donor only, with treated and control wells | Treated/control wells may support a within-preparation contrast | Model wells as observations, but label inference as within that preparation only | Cannot estimate donor-to-donor heterogeneity; cannot generalize to donors |

Required rule: **technical replication does not create independent treatment replication.** If several libraries, wells, lanes, or sequencing runs belong to the same independent treatment-allocation unit, they must either be collapsed into one count profile for that unit or analyzed only as a sensitivity check, not as independent replicates.

---

### 2.3 Allocation, randomization, and blinding — proposed

1. **Record the allocation log.**  
   For every sample, record what entity received treatment, when, by whom, and under which batch. The allocation log is the primary evidence for the experimental unit.

2. **Randomize or block where possible.**  
   If treatment can be randomized, record:
   - randomization seed: `[RANDOMIZATION_SEED_PLACEHOLDER]`;
   - blocking variables: donor, plate, extraction batch, library batch, lane;
   - balance constraints.

3. **Prevent confounding.**  
   Treatment must not be perfectly confounded with batch, donor, lane, extraction date, or library preparation date. If all treated samples are in one batch and all controls in another, the treatment effect is not separately estimable from batch. The correct response is to stop or limit the claim, not to adjust it away.

4. **Blinding.**  
   Where feasible, sample identifiers shown to laboratory and analysis staff should not reveal treatment. Record:
   - blinding code;
   - time of unblinding;
   - person authorizing unblinding.

---

### 2.4 Intervention and sampling — proposed

1. **Define intervention precisely.**  
   Record treatment dose, duration, vehicle, route, environmental conditions, and control condition. Use placeholders if not yet known.

2. **Define sampling hierarchy.**  
   Example hierarchy:

   ```text
   donor
     treatment allocation unit
       tissue/cell aliquot
         RNA extraction
           library
             sequencing lane/read group
   ```

3. **Sampling must map to the allocation unit.**  
   If the donor is the independent unit, all subsamples from that donor under the same treatment are downstream observations of the same allocation unit. If wells are independently allocated, each well may be an allocation unit.

4. **Pooling rule.**  
   If samples are pooled, pooling must occur only within a defined allocation unit or according to a pre-scribed rule. Record pool composition and count it as one measurement of the pooled allocation unit.

---

### 2.5 Measurements — proposed

1. **RNA quality control.**  
   Record concentration, integrity, extraction batch, and any sample-quality thresholds. Thresholds should be calibrated from controls or pilot data, not invented.

2. **Library preparation.**  
   Record library kit, input amount, PCR cycles, index sequences, library batch, and any unique molecular identifier scheme if used.

3. **Sequencing.**  
   Record instrument, flow cell, lane, read length, paired/end status, demultiplexing software, and version placeholders.

4. **Raw data products.**  
   The immutable raw measurement is the FASTQ set, or an equivalently raw demultiplexed read set. Proposed manifest fields:

   ```text
   sample_id
   library_id
   lane_id
   fastq_r1_path
   fastq_r2_path
   fastq_r1_sha256
   fastq_r2_sha256
   read_count
   instrument_id
   ```

5. **Gene-count generation.**  
   The count matrix must be generated from the frozen reference and annotation. Proposed fields:

   ```text
   genome_build: [GENOME_BUILD_PLACEHOLDER]
   annotation_version: [ANNOTATION_VERSION_PLACEHOLDER]
   aligner_or_quantifier: [QUANTIFICATION_TOOL_PLACEHOLDER]
   quantifier_version: [QUANTIFICATION_VERSION_PLACEHOLDER]
   count_type: raw_unstranded_or_stranded_integer_counts
   gene_id_type: [GENE_ID_TYPE_PLACEHOLDER]
   ```

   The primary DE model should use raw integer gene counts, not normalized counts or transformed counts.

---

### 2.6 Controls — proposed

Controls are for calibration and audit, not for post-hoc rescue.

1. **Negative controls**
   - blank extraction or no-template controls;
   - low-input or no-RNA controls;
   - intergenic or non-target regions, if appropriate.

2. **Positive controls**
   - spike-in RNAs if used: `[SPIKE_IN_NAME_PLACEHOLDER]`;
   - reference RNA samples;
   - known expected-difference controls, if available.

3. **Process controls**
   - the same reference sample run across batches;
   - repeated library controls;
   - sample identity checks using genotype, sex, or known marker genes where ethically and scientifically appropriate.

4. **Use of controls**
   - establish acceptable mapping, contamination, and library-quality ranges;
   - detect sample swaps;
   - calibrate outlier thresholds;
   - audit batch effects.

---

## 3. Proposed reproducible analysis plan

All analyses in this section are proposed. No files have been supplied, so no analysis has been executed.

### 3.1 Immutable inputs

Before execution, the following inputs must be frozen by checksum and version.

| Input class | Required record | Placeholder |
|---|---|---|
| Raw reads | FASTQ paths and SHA-256 hashes | `[FASTQ_SHA256_PLACEHOLDER]` |
| Sample sheet | TSV/CSV file hash | `[SAMPLE_SHEET_SHA256_PLACEHOLDER]` |
| Configuration | YAML/JSON file hash | `[CONFIG_SHA256_PLACEHOLDER]` |
| Genome FASTA | path, build, SHA-256 | `[GENOME_SHA256_PLACEHOLDER]` |
| Annotation GTF/GFF | path, release, SHA-256 | `[ANNOTATION_SHA256_PLACEHOLDER]` |
| Transcript-to-gene map | path and hash, if used | `[TX2GENE_SHA256_PLACEHOLDER]` |
| Analysis code | Git commit or archive hash | `[CODE_COMMIT_PLACEHOLDER]` |
| Software environment | container digest or lockfile hash | `[ENV_DIGEST_PLACEHOLDER]` |
| Randomization seed | recorded in config | `[SEED_PLACEHOLDER]` |

No raw input may be edited. If a file must be excluded, it remains in the manifest with an `inclusion=false` flag and a reason.

---

### 3.2 Sample sheet

The sample sheet is the single tabular source of truth for sample metadata and experimental design. Proposed columns:

```text
sample_id
library_id
donor_id
well_id
allocation_unit_id
allocation_level
parent_allocation_unit_id
condition
batch
processing_date
lane_id
index_sequence
fastq_r1_sha256
fastq_r2_sha256
count_file_sha256
inclusion
inferential_scope
notes
```

Required controlled values:

```text
condition: control | treatment
allocation_level: donor | well | aliquot | animal | other_predefined_level
inclusion: true | false
inferential_scope: donor_population | within_donor_only | well_level_only | allocation_unit_only
```

Rules:

1. `sample_id` must be unique.
2. `allocation_unit_id` must identify the independent treatment-allocation unit.
3. If multiple rows share the same `allocation_unit_id`, they are subsamples or technical replicates and must be collapsed for the primary analysis unless a pre-specified sensitivity analysis says otherwise.
4. `donor_id` and `well_id` must not be conflated. Donor is the biological source; well is a possible treatment-allocation or measurement unit.
5. If `inferential_scope=donor_population`, the design must contain multiple independent donors or equivalent biological units, unless the claim is explicitly restricted.

---

### 3.3 Reference and annotation versions

The count matrix is only interpretable relative to a fixed reference and annotation. Record:

```text
species: [SPECIES_PLACEHOLDER]
genome_build: [GENOME_BUILD_PLACEHOLDER]
genome_fasta_path: [GENOME_FASTA_PATH_PLACEHOLDER]
genome_fasta_sha256: [GENOME_SHA256_PLACEHOLDER]
annotation_source: [ANNOTATION_SOURCE_PLACEHOLDER]
annotation_release: [ANNOTATION_RELEASE_PLACEHOLDER]
annotation_gtf_path: [ANNOTATION_GTF_PATH_PLACEHOLDER]
annotation_gtf_sha256: [ANNOTATION_SHA256_PLACEHOLDER]
gene_id_type: [GENE_ID_TYPE_PLACEHOLDER]
gene_id_version: [GENE_ID_VERSION_PLACEHOLDER]
```

If annotation changes after counts are generated, counts are not directly comparable. The audit rule is: any annotation change requires a new count-generation run and a new manifest.

---

### 3.4 Count model

The proposed primary count model is a DESeq2-style negative-binomial generalized linear model. This is consistent with the supplied evidence packet describing DESeq2 as using negative-binomial GLMs with information sharing for dispersion and effect estimation.

General model form:

```text
gene_count ~ offset(library_size) + design_terms
```

The design formula depends on the experimental unit and inferential scope.

#### Case A: Donor-level treatment allocation, independent donors

Use when each donor or animal is independently assigned to treatment or control.

```text
design = ~ batch + condition
```

Required conditions:

- one count profile per independent donor/allocation unit, or technical subsamples collapsed to donor level;
- at least `[MIN_INDEPENDENT_UNITS_PER_GROUP_PLACEHOLDER]` independent units per condition;
- batch not confounded with condition.

#### Case B: Well/aliquot-level treatment allocation within donors

Use when treatment is independently allocated to wells or aliquots from donors.

```text
design = ~ batch + donor_id + condition
```

Interpretation:

- estimates the treatment contrast within donors, averaged over the included donors;
- donor is treated as a blocking factor, not as a source of donor-population heterogeneity unless the design and number of donors support that claim;
- if only one donor exists, the result is a within-preparation contrast only; it does not identify across-donor heterogeneity.

#### Case C: Paired donor design with donor-level summary

If the inferential target is donor-level response, a separate donor-summary analysis may be proposed:

1. estimate a within-donor treatment-control contrast for each donor, where possible;
2. test donor-level contrasts across donors using a pre-specified model;
3. keep this analysis separate from well-level DESeq2 inference.

This secondary analysis is proposed only if multiple donors with paired treatment/control observations exist.

#### Model settings

Proposed placeholders:

```text
count_distribution: negative_binomial
normalization: DESeq2_median_of_ratios
dispersion_estimation: DESeq2_information_sharing
test: Wald_or_LRT_placeholder
cooks_cutoff: [COOKS_CUTOFF_PLACEHOLDER]
min_replicates_for_replace: [MIN_REPLICATES_FOR_REPLACE_PLACEHOLDER]
beta_prior_or_shrinkage_method: [SHRINKAGE_METHOD_PLACEHOLDER]
```

No transformed expression values are used as the primary test input. Transformations such as variance-stabilizing or regularized-log transformations may be used only for diagnostic plots, and their parameters must be recorded.

---

### 3.5 Contrast and FDR

Primary contrast:

```text
contrast = condition: treatment versus control
```

Formal placeholder:

```text
contrast_variable: condition
numerator_level: treatment
denominator_level: control
```

Testing and multiple-testing correction:

```text
null_log2_fold_change: [LFC_NULL_PLACEHOLDER]
alternative: two_sided_or_directional_placeholder
p_value_adjustment: Benjamini-Hochberg
fdr_alpha: [FDR_ALPHA_PLACEHOLDER]
independent_filtering: [TRUE_FALSE_PLACEHOLDER]
```

Rules:

1. If `null_log2_fold_change` is zero, the null hypothesis is no treatment effect on log2 fold change.
2. If a nonzero log2 fold-change threshold is used, the alternative hypothesis and threshold must be pre-specified.
3. FDR control is applied across genes within each declared contrast.
4. Results should include effect size, standard error, base mean, p-value, adjusted p-value, outlier flags, and model diagnostics, not only significance calls.
5. A lack of discoveries is not evidence of no biological effect; it may reflect low power, high dispersion, or restrictive thresholds.

---

### 3.6 Plot regeneration

All figures must be regenerable from immutable inputs and tracked code. No manual point-and-click editing should be required.

Required plots:

1. **Library-size and size-factor plot**  
   Purpose: detect extreme library composition differences.

2. **Sample-distance heatmap**  
   Purpose: identify outliers and major batch or donor structure.

3. **PCA or ordination plot**  
   Purpose: visualize major variance sources. Use transformed counts only for visualization. Record transformation parameters.

4. **MA plot**  
   Purpose: show mean expression versus log2 fold change and highlight significant or flagged genes.

5. **Volcano plot**  
   Purpose: display effect size versus evidence; must be derived from the same results table used for reporting.

6. **Dispersion plot**  
   Purpose: inspect DESeq2 dispersion fit and information sharing.

7. **Cook’s distance or outlier plot**  
   Purpose: identify genes/samples with disproportionate influence.

8. **P-value histogram**  
   Purpose: check test behavior and possible confounding.

9. **FDR diagnostic plot**  
   Purpose: show adjusted p-value distribution or discoveries versus threshold.

10. **QC metric plot**  
   Purpose: mapping rate, read quality, contamination indicators, and control behavior.

Plot reproducibility requirements:

```text
plot_script: [PLOT_SCRIPT_PATH_PLACEHOLDER]
plot_script_sha256: [PLOT_SCRIPT_SHA256_PLACEHOLDER]
input_count_matrix_sha256: [COUNT_MATRIX_SHA256_PLACEHOLDER]
input_sample_sheet_sha256: [SAMPLE_SHEET_SHA256_PLACEHOLDER]
config_sha256: [CONFIG_SHA256_PLACEHOLDER]
seed: [SEED_PLACEHOLDER]
palette: [PALETTE_PLACEHOLDER]
deterministic_order: sample_id, gene_id
```

Every plot file should be listed in an output manifest with its generating command and input hashes.

---

### 3.7 Source-difference audit

The audit must show that the analysis contains no hidden state and that the executed objects match the declared objects. Because no files are supplied, this audit is proposed, not performed.

#### 3.7.1 Source manifest

Create a manifest with one row per source object:

```text
object_type
object_path
object_version
sha256
recorded_by
recorded_at
status
```

Object types include:

```text
fastq
sample_sheet
config
genome_fasta
annotation_gtf
tx2gene
code
container
count_matrix
results_table
plot
log
```

#### 3.7.2 Source-difference checks

The audit script should compare planned versus observed state and report:

```text
missing_input
unexpected_input
hash_changed
version_changed
sample_sheet_mismatch
reference_mismatch
annotation_mismatch
code_commit_mismatch
environment_mismatch
output_not_reproducible_from_manifest
```

Required checks:

1. Every FASTQ referenced in the sample sheet exists and has the declared hash.
2. Every sample row has a matching count file or a documented exclusion.
3. The annotation version used for counting matches the annotation version declared in the config.
4. The gene identifiers in the count matrix match the annotation version.
5. The design formula uses only columns present in the sample sheet.
6. The contrast levels exist in the sample sheet.
7. The analysis container or environment digest matches the recorded digest.
8. All outputs are generated by tracked code at the recorded commit.
9. No raw count, FASTQ, or metadata file has been edited after freezing.

#### 3.7.3 Curated-source difference

The supplied packet includes a source summary and curator interpretation, not a quotation. Therefore, if the original source record becomes available, the audit should compare:

- curator interpretation;
- original source record;
- version of the source record;
- any semantic differences.

Any difference must be recorded before the source record is used to justify analytical choices.

---

## 4. Acceptance and stopping criteria — proposed

### 4.1 Acceptance gates

| Gate | Criterion | Proposed action if passed |
|---|---|---|
| G0 | Independent allocation unit is defined and documented | Proceed to sample-sheet freeze |
| G1 | Sample sheet validates: unique IDs, controlled vocabularies, no missing required fields | Proceed to input manifest |
| G2 | All input hashes and versions are recorded | Proceed to wet-lab or data-generation stage |
| G3 | Treatment is not confounded with batch, donor, lane, or processing date | Proceed to count generation |
| G4 | Count matrix is integer-valued, gene IDs match annotation, samples match sample sheet | Proceed to model fitting |
| G5 | Design matrix is full rank and contrast is estimable | Proceed to differential testing |
| G6 | Diagnostic plots and control metrics fall within calibrated acceptance ranges | Proceed to results reporting |
| G7 | Source-difference audit reports no unresolved mismatches | Release proposed results |

### 4.2 Stopping criteria

Stop differential-expression inference if any of the following occur:

1. The independent treatment-allocation unit cannot be identified.
2. There are no independent treatment replicates at the required allocation level.
3. A single donor is used to claim across-donor heterogeneity or donor-population inference.
4. Treatment is fully confounded with batch, donor, lane, or processing date.
5. Sample identity cannot be verified.
6. Reference or annotation versions are not frozen.
7. Count files are not raw integer counts or do not match the declared annotation.
8. The source-difference audit detects unexplained changes.
9. Model diagnostics indicate severe misspecification that cannot be corrected by a pre-specified rule.

### 4.3 Calibration procedures for unknown thresholds

For any unknown numeric threshold, use a calibration procedure rather than an invented value.

| Parameter | Calibration procedure |
|---|---|
| `fdr_alpha` | Decide based on confirmatory versus exploratory use, validation budget, and consequences of false discoveries |
| `lfc_threshold` | Use biological effect-size justification plus measurement error from controls or pilot data |
| Minimum independent replicates | Use power or precision calculation based on plausible dispersion and effect sizes; if unavailable, declare insufficient replication |
| Mapping-rate threshold | Use distribution of positive-control libraries and known acceptable ranges from the sequencing platform |
| Count-filter threshold | Use independent filtering principles and library-size distribution; preserve enough genes for inference while removing uninformative genes |
| Outlier threshold | Use Cook’s distance behavior, positive/negative controls, and pre-specified sensitivity analyses |
| Batch adjustment set | Use causal diagram and observed association with treatment and expression; exclude colliders and treatment consequences |

---

## 5. Troubleshooting — proposed

| Problem | Likely interpretation | Proposed response |
|---|---|---|
| Treatment and batch are confounded | Treatment effect is not separable from batch | Stop primary DE inference; redesign, reprocess balanced samples, or restrict claim |
| Only one donor per condition | No independent biological replication for donor-population inference | Do not claim donor-level DE; report descriptive results only or collect more donors |
| Many wells but one treated donor | Well-level contrast may exist but donor generalization does not | Label inference as within-preparation only |
| Samples cluster by batch rather than treatment | Strong technical or biological batch effect | Check randomization; include batch if estimable; verify no confounding |
| One sample has extreme library size or distance | Possible library failure, contamination, or outlier | Verify wet-lab metrics; use pre-specified exclusion or sensitivity analysis; document |
| Poor mapping rate | Wrong reference, contamination, degraded RNA, or species mismatch | Re-check reference version, contamination controls, and RNA QC |
| Gene IDs do not match annotation | Count matrix was generated against a different annotation | Rebuild counts using frozen annotation or create new manifest |
| P-value histogram shows strong inflation | Possible unmodeled confounding, relatedness, or batch effect | Re-examine design formula, sample sheet, and allocation unit; do not only adjust threshold |
| No genes pass FDR | Low power, small effect, high variability, or stringent threshold | Report negative result with uncertainty; do not claim no effect without power assessment |
| Source-difference audit fails | Hidden state or changed input | Rebuild from immutable manifest; do not release results until resolved |

---

## 6. Alternatives and limits

### 6.1 Alternatives

The supplied evidence specifically supports a DESeq2-style negative-binomial GLM, but the same audit principles could be applied to other count-based or precision-weighted frameworks if they are fully versioned and documented. Any alternative must still:

1. use raw count or equivalent count-scale input;
2. record the experimental unit correctly;
3. avoid treating technical replicates as independent;
4. pre-specify contrasts and FDR;
5. regenerate plots deterministically;
6. pass the same source-difference audit.

If donor-level random effects are scientifically required, a mixed-model framework may be proposed separately. However, a random donor effect does not create information about donor heterogeneity when only one donor exists, and it does not replace missing independent treatment replication.

### 6.2 Limits

1. **No execution has occurred.** No files, counts, sample sheets, references, or versions were supplied.
2. **All numeric values are placeholders.** Thresholds must be calibrated and recorded before execution.
3. **The experimental unit controls inference.** Adding wells, lanes, or technical libraries cannot create independent biological replication.
4. **Donor and well inference are distinct.** A well-level result is not automatically a donor-population result.
5. **A single donor cannot support across-donor heterogeneity.** A donor random effect or blocking term does not solve this.
6. **Annotation changes alter counts.** A new annotation version requires new counting and a new manifest.
7. **Batch confounding can make treatment effects inestimable.** Statistical adjustment cannot rescue a fully confounded design.

---

## 7. Final proposed statement

This is a proposed, reproducible, audit-ready bulk RNA-seq differential-expression plan. It keeps the experimental unit at the independent treatment-allocation level, uses a DESeq2-style negative-binomial count model, pre-specifies the treatment-versus-control contrast and Benjamini-Hochberg FDR control, requires deterministic plot regeneration, and requires a source-difference audit. No analysis has been executed because no count matrices, sample sheets, sequence files, reference files, or versions have been supplied. All paths, versions, numeric settings, and thresholds are placeholders to be calibrated, recorded, and audited before any execution or biological claim.
