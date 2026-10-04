# GPT-5.6 Sol / inf-d02

Original final answer, shared by both scoring rounds.

# Proposed auditable bulk RNA-seq differential-expression plan

## 1. Recommended design decision

**The proposed primary analysis should use one observation per independent treatment-allocation unit, not one observation per well, lane, or library unless that entity was independently allocated to treatment.** Technical lanes should be combined, and subsamples nested within one allocation should either be combined according to a predeclared rule or retained only for measurement-QC purposes.

The proposed primary model is a DESeq2 negative-binomial generalized linear model comparing **treatment minus control**, with donor blocking only when the allocation structure makes that term identifiable and with processing batch included only when it is estimable rather than confounded with treatment. Benjamini–Hochberg FDR control should use a prospectively selected threshold `<alpha_FDR>`.

**No analysis has been run.** No count matrix, sample sheet, allocation log, raw reads, reference files, or software versions were supplied. Every experiment, path, version, parameter, threshold, command, and analysis below is therefore **proposed** and must be replaced by recorded values before execution.

---

## 2. Evidence → inference → conclusion

| Supplied evidence | Inference | Proposed conclusion |
|---|---|---|
| DESeq2 uses negative-binomial GLMs and shares information for dispersion and effect estimation. | DESeq2 is appropriate for gene-level integer counts with biological replication and an estimable design. | Propose a DESeq2 negative-binomial GLM with a frozen design matrix and contrast. |
| Modeling does not create missing independent treatment replication. | Wells, lanes, or repeated measurements cannot be counted as independent treatment replicates merely because they produce separate files. | Define `allocation_unit_id` before analysis and conduct treatment inference at that level. Stop confirmatory DE analysis if the calibrated replication requirement is not met. |
| The experimental unit depends on independent treatment allocation. | Unit identity cannot be inferred safely from filenames or the count matrix. | Require an allocation log and sample sheet linking every library to an independent allocation unit. |
| Donor and well inference are distinct. | Within-donor replication can support a within-donor treatment estimand but does not by itself establish across-donor generality. | State the estimand explicitly and include multiple independent donors if across-donor inference is intended. |
| A single donor cannot identify across-donor heterogeneity by adding a donor random effect. | A random-effect model cannot rescue absent donor replication. | With one donor, restrict claims to that donor and the represented allocation units; do not claim a population-of-donors effect. |
| The record is partial and files and versions are absent. | Author settings and results cannot be reconstructed or attributed. | Freeze immutable inputs, software, references, settings, and provenance before execution; maintain a source-difference audit. |

The recommendation would change if the future allocation log shows a different experimental unit, if treatment is confounded with donor or batch, or if the intended estimand is explicitly limited to a single donor.

---

# 3. Proposed ordered protocol

## 3.1 Preparation, estimand, and prospective calibration

1. **Define the primary estimand before unblinding expression data.** Proposed default:

   > Difference in expected gene expression between treatment and control at `<sampling_time>`, for the population represented by the independent allocation units and donors in the design.

2. Record:
   - organism, tissue/cell type, intervention, dose, duration, sampling time;
   - primary treatment and control labels;
   - target population of donors;
   - whether inference is donor-population, donor-conditional, or limited to a single donor;
   - primary assay and gene universe;
   - one primary contrast: `treatment - control`;
   - `<alpha_FDR>`, chosen before analysis;
   - any minimum effect size used for interpretation.

3. **Calibrate sample size rather than inventing it.** The proposed calibration should simulate negative-binomial counts over plausible grids of:
   - mean abundance and dispersion;
   - biologically meaningful fold changes;
   - library sizes;
   - donor and allocation-unit variation;
   - donor intraclass correlation where relevant;
   - attrition rates.

   Inputs should come from a blinded pilot, validated historical data, or a documented plausible range. The selected number of independent allocation units and donors should be frozen before outcome-dependent analysis. If no defensible calibration input becomes available, report that power is unknown rather than supplying a nominal replicate number.

4. Pre-register primary and sensitivity analyses in a dated, immutable analysis-plan file.

## 3.2 Independent units and allocation structure

Create an `allocation_unit_id` that identifies the smallest entity independently assigned to treatment or control.

Proposed decision rules:

- **Donor-level parallel allocation:** if each donor is assigned wholly to one arm, the donor is the treatment-allocation unit. Wells and libraries from that donor are nested measurements.
- **Split-donor allocation:** if independently prepared donor-derived cultures are assigned within each donor, each independently assigned culture is an allocation unit and donor is a blocking factor. Multiple donors are still needed for across-donor generalization.
- **Multiple wells after one allocation:** wells produced after a single treatment assignment are not independent treatment units.
- **Independently randomized wells:** they may be allocation units for a well-level, donor-conditional response, but wells from one donor do not establish across-donor heterogeneity.
- **Technical lanes or resequencing of one library:** these are measurement replicates and should be merged, not treated as biological observations.

If allocation history cannot distinguish these cases, stop confirmatory treatment inference until it is resolved.

## 3.3 Allocation and blinding

The proposed experiment should:

1. Generate the allocation sequence independently of sample processing.
2. Randomize allocation units, with stratification or blocking by donor where a split-donor design is intended.
3. Balance treatment across extraction batches, library-preparation plates, operators, and sequencing lanes.
4. Avoid placing all treatment samples in one processing batch.
5. Preserve a signed allocation log containing unit, stratum, assigned condition, allocation time, and deviations.
6. Use masked sample IDs for extraction, library preparation, sequencing QC, and pre-model exclusions where feasible.
7. Reveal treatment labels only after sample identity and technical-QC decisions are frozen.

Randomization method, software version, seed, and any constrained-allocation criteria should be recorded. Seeds are reproducibility metadata, not substitutes for saving the realized allocation.

## 3.4 Intervention and sampling

Record prospectively for each allocation unit:

- intervention identity, lot, concentration/dose, vehicle and duration;
- control intervention;
- culture or husbandry conditions;
- sampling time and collection order;
- donor and source material;
- viability or other prespecified phenotypic acceptance measure;
- time to stabilization/freezing;
- extraction date, operator, plate, and position;
- deviations, losses, and reasons.

Sampling order should be randomized or balanced across condition. Replacements should follow a predeclared rule and should not be selected using expression outcomes.

## 3.5 Measurements and controls

The proposed measurement process should record:

- RNA extraction protocol and kit lot;
- RNA quantity, purity, and integrity metrics;
- library protocol, strandedness, selection method, insert-size target, and unique molecular identifier use if any;
- sequencer model, run, lane, read configuration, and target depth;
- positive, negative, extraction, and library controls;
- sample identity checks where informative.

Spike-ins may be proposed if absolute RNA output or global transcriptional shifts are central to the estimand. Their use and normalization role must be specified in advance; they should not be added post hoc to rescue an unexpected result. Controls and spike-ins are not biological replicates.

Unknown QC thresholds should be calibrated from instrument specifications, validated historical performance, or a blinded pilot. The calibration source and finalized thresholds must be recorded before condition-aware analysis.

---

# 4. Immutable inputs and computational record

## 4.1 Proposed repository layout

```text
project/
  README.md
  protocol/
    estimand.yaml
    analysis_plan.md
    acceptance_rules.yaml
  metadata/
    samples.tsv
    allocation_log.tsv
    data_dictionary.tsv
  manifests/
    inputs.sha256
    references.sha256
    outputs.sha256
  config/
    workflow.yaml
    contrasts.tsv
    software.lock
  reference/
    genome.fa
    annotation.gtf
  workflow/
    Snakefile_or_Nextflow_files
    scripts/
  containers/
    image_digest.txt
  results/
    qc/
    counts/
    de/
    figures/
    tables/
  audit/
    source_differences.tsv
    exclusions.tsv
    deviations.tsv
  logs/
  report/
```

These are placeholder paths. The final paths and filenames should be frozen in configuration.

## 4.2 Immutable-input manifest

For each raw FASTQ, imported count file, sample sheet, allocation log, reference, annotation, and configuration file, record:

- relative path and immutable storage URI;
- file role;
- byte size;
- SHA-256 checksum;
- creation or acquisition date;
- source accession or provider;
- compression format;
- read-only or object-version identifier.

Raw inputs should be retained read-only. Any corrected metadata file should receive a new checksum and version; it should not overwrite the previous file.

## 4.3 Proposed sample-sheet schema

Use one row per sequenced library, with at least:

```text
sample_id
library_id
allocation_unit_id
donor_id
well_or_subsample_id
condition
condition_code
allocation_block
batch_extraction
batch_library
batch_sequencing
plate
lane
collection_time
intervention_time
sex_or_other_prespecified_covariates
fastq_r1
fastq_r2
strandedness
paired_end
technical_replicate_group
include_primary
exclusion_reason
```

Requirements:

- identifiers must be unique and nonblank where applicable;
- `condition` must agree with the signed allocation log;
- every library must map to exactly one allocation unit;
- technical replicates must share a declared replicate-group ID;
- exclusions must cite a frozen rule and must never be silently deleted;
- no covariate should be inferred from a sample name.

## 4.4 Reference and annotation freeze

Before execution, record:

- organism and assembly accession/release;
- exact genome FASTA source, filename, checksum, and contig naming convention;
- exact GTF/GFF provider, release, filename, and checksum;
- gene biotype inclusion rules;
- transcript-to-gene mapping version if transcript quantification is used;
- aligner or quantifier name, version, parameters, and index checksum;
- counting software, version, strandedness, paired-read rules, multimapping policy, and overlap policy.

Genome and annotation compatibility should be checked by contig names, coordinate conventions, and representative feature IDs. An annotation release label without a file checksum is insufficient.

## 4.5 Software and hidden-state control

The proposed workflow should run from a version-controlled workflow at a recorded commit inside a container identified by immutable digest. Record:

- workflow engine and version;
- R, Bioconductor, DESeq2, plotting, alignment and counting versions;
- operating-system/container digest;
- all command lines, configuration files, stdout/stderr and exit codes;
- locale, time zone, thread count, and random seeds;
- whether any tool is nondeterministic under multithreading;
- session information in the generated report.

The workflow should fail if input hashes, sample-sheet schema, reference hashes, or configuration differ from the frozen manifest. No manual spreadsheet editing or manual figure adjustment should occur after workflow execution.

---

# 5. Proposed data processing and quality checks

1. Verify all hashes and metadata relationships.
2. Inspect raw-read quality, adapter content, base composition, duplication, read length, and unexpected sequence.
3. Apply trimming only under a predeclared or calibrated rule; save both settings and reports.
4. Align or quantify against the frozen reference.
5. Assess mapping/assignment rate, strandedness, insert size, rRNA or other unwanted content, coverage bias, and sample identity.
6. Merge lanes from the same library by a deterministic rule.
7. Generate integer gene counts using the frozen annotation.
8. Reconcile read totals through stages: raw → retained → aligned/quantified → assigned.
9. Combine nested technical measurements before treatment modeling:
   - lanes from one library: sum counts;
   - resequenced copies: sum only if they represent the same library and compatible processing;
   - multiple libraries or wells from one allocation unit: use a prospectively chosen aggregation or representative-library rule. They must not increase treatment replicate count.
10. Freeze exclusions before primary DE testing whenever possible.

PCA or clustering may identify possible swaps or failures, but treatment-aware removal should not be based merely on appearing unusual or weakening a desired result.

---

# 6. Proposed statistical analysis

## 6.1 Model

For gene \(g\) and independent allocation unit \(i\), propose:

\[
K_{gi} \sim \mathrm{NB}(\mu_{gi}, \alpha_g)
\]

\[
\log(\mu_{gi}) =
\log(s_i) + \beta_{0g} + \beta_{Tg}T_i
+ \sum_j \gamma_{jg}X_{ij}
\]

where:

- \(K_{gi}\) is the integer gene count;
- \(s_i\) is the DESeq2 size factor;
- \(\alpha_g\) is the shared/estimated dispersion;
- \(T_i\) encodes treatment;
- \(X_{ij}\) contains only prespecified, identifiable blocking covariates.

Proposed formulas:

- balanced parallel donor allocation: `~ batch + condition`;
- split-donor design: `~ donor + batch + condition`;
- no relevant batch: omit it rather than inserting an unnecessary term.

Batch should be included only if it varies independently enough from treatment to be estimable. If treatment is perfectly confounded with batch or donor, the primary treatment effect is not identifiable and confirmatory DE analysis should stop.

A donor random effect is not proposed as a remedy for one donor. If a mixed-model alternative is scientifically needed, it requires enough independent donors and a separately specified method; it does not manufacture donor replication.

## 6.2 Primary contrast and testing

The proposed primary contrast is explicitly:

```text
treatment - control
```

Positive log2 fold change should mean higher expression in treatment.

A proposed two-group primary test is the DESeq2 Wald test for the condition coefficient. The workflow should save:

- gene identifier and annotation;
- base mean;
- unshrunken log2 fold change;
- standard error;
- test statistic;
- raw p-value;
- adjusted p-value;
- filtering and outlier status.

If effect-size shrinkage is used for ranking or plotting, the estimator and version should be frozen and the shrunken estimate should be labeled separately from the coefficient used for the primary test.

## 6.3 Filtering, outliers, and multiplicity

Before execution, record:

- low-count or prevalence filter, or the exact DESeq2 independent-filtering behavior;
- treatment-independent filter statistic;
- Cook’s-distance and replacement behavior;
- minimum replicate conditions required for any automatic replacement;
- genes excluded by annotation or QC.

The multiple-testing universe is all genes passing the frozen eligibility/filtering rules. Apply the Benjamini–Hochberg procedure to the primary gene-level p-values and call significance at:

```text
adjusted p-value < <alpha_FDR>
```

`<alpha_FDR>` must be selected before testing and may not be chosen after viewing results. Report effect sizes and uncertainty even when genes do not cross the FDR threshold.

Interaction tests, pathway analyses, alternative contrasts, and subgroup analyses should be explicitly labeled secondary or exploratory and receive their own multiplicity plan.

---

# 7. Plot regeneration

All proposed plots should be generated from scripts, not interactively:

- per-sample read and assignment summaries;
- library sizes and size factors;
- dispersion-fit and diagnostic plots;
- transformed-count PCA and sample-distance plots;
- MA plot;
- volcano plot, if used;
- unit-level normalized count plots for selected genes;
- heatmap using a prospectively stated, outcome-independent selection rule where possible;
- Cook’s-distance and outlier summaries.

Transformations used for visualization should not replace the negative-binomial count model.

A single clean-build target should regenerate tables, figures, and report, for example:

```text
<workflow_command> --configfile config/workflow.yaml --use-container --rerun-incomplete
```

This is a placeholder, not an executed command. Each output should receive a checksum, and figure captions should identify the source table, transformation, filtering rule, unit of observation, and software version.

---

# 8. Source-difference audit

Create `audit/source_differences.tsv` with columns:

```text
item
source_A
source_B
observed_difference
expected_or_unexplained
potential_impact
resolution
reviewer
date
```

The proposed audit should compare:

1. allocation log versus analytical condition labels;
2. sample sheet versus FASTQ headers and sequencing records;
3. expected versus observed file hashes and sizes;
4. raw-read totals versus aligned, assigned, and counted totals;
5. genome contigs versus annotation contigs;
6. declared strandedness versus empirical strandedness evidence;
7. declared methods versus actual configuration, logs, and software lockfile;
8. imported source counts versus regenerated counts, if both later become available;
9. prior/source gene identifiers versus the frozen annotation;
10. primary results versus sensitivity analyses.

Differences should be classified as expected—for example, a documented annotation change—or unexplained. Unexplained differences affecting labels, allocation units, reference identity, or count values should block final inference until resolved.

Because the supplied record is partial, this protocol must not claim to reproduce undocumented author settings. Such fields should be recorded as `unknown`, followed by the proposed calibration or selection procedure.

---

# 9. Acceptance and stopping criteria

## Proposed acceptance criteria

Proceed to confirmatory modeling only if:

- allocation units and treatment assignments are verified;
- the prospective replication/power requirement is met;
- the design matrix is full rank;
- treatment is not perfectly confounded with donor or batch;
- input and reference hashes match;
- sample identity and technical QC pass frozen rules;
- count assignment and gene identifiers are internally consistent;
- all exclusions and deviations are documented.

## Proposed stopping or scope-restriction criteria

Stop confirmatory treatment inference, or restrict it to descriptive analysis, if:

- independent treatment replication is absent;
- unit identity cannot be recovered;
- treatment is inseparable from batch or donor;
- labels or file integrity remain unresolved;
- all observations come from one donor but the intended claim is across donors;
- QC failure is systematic by treatment and cannot be distinguished from biology;
- the model is rank-deficient or dispersion estimation is unsupported.

Stopping DE inference does not require discarding the data; descriptive QC and explicitly limited effect estimates may still be reported without confirmatory population claims.

---

# 10. Troubleshooting and proposed sensitivity analyses

- **Low mapping:** verify organism, contamination, read quality, reference release, and aligner settings; do not switch references based on which gives preferred DE results.
- **Low assignment:** check strandedness, gene-feature definitions, paired-read rules, and GTF/FASTA compatibility.
- **Sample swap:** compare barcodes, genotype or other identity evidence where available; correct only with documented independent evidence.
- **Batch imbalance:** inspect design rank and overlap. Statistical adjustment cannot resolve perfect confounding.
- **Outlier unit:** investigate processing records and identity; retain unless a frozen exclusion rule is met. Report analyses with and without any consequential exclusion.
- **Strong global RNA shift:** ordinary size-factor assumptions may be inappropriate; use prospectively included spike-ins or another independently justified normalization strategy.
- **One donor:** analyze only a donor-conditional response if allocation units permit; do not add a random donor effect or claim across-donor heterogeneity.
- **Alternative pipelines:** a frozen alternative such as transcript quantification followed by transcript-to-gene import may be used as a sensitivity analysis. It should not replace the primary pipeline after results are viewed.
- **Alternative statistical methods:** edgeR, limma-voom, or a mixed model may be prospectively specified as sensitivity analyses. Concordance and discrepancies should be reported rather than selecting the most favorable result.

## Principal unresolved parameters

The actual allocation level, donor count, sample count, batch structure, sequencing protocol, reference release, software versions, QC cutoffs, power target, and FDR threshold are unreported. They must be prospectively calibrated or supplied, frozen in the manifest and analysis plan, and audited before any proposed workflow is executed.
