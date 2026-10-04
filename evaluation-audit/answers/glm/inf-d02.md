# GLM 5.3 FlashX / inf-d02

Original final answer, shared by both scoring rounds.

# Proposed Bulk RNA-seq Differential-Expression Analysis Plan (Design Only; No Execution Claimed)

## Conclusion and recommended next action

What follows is a **proposed, pre-registered analysis plan** for a two-condition bulk RNA-seq study with possible donor and processing-batch structure. It is designed so that every input is immutable, every transformation is scripted, and every output is regenerable from a frozen input set by a single command — i.e., auditable without hidden state. **No files were supplied with this question; therefore nothing here has been executed, and all paths, versions, thresholds, and numeric settings below are placeholders to be recorded at run time, not established values.** The recommended next action is to instantiate the manifest and sample-sheet templates (Steps 1–3) before sequencing data arrive, so that the design matrix is fixed before counts are seen.

## Evidence–inference–conclusion chain

**Evidence (from the supplied packet).** The DESeq2 record describes negative-binomial generalized linear models with information sharing for dispersion and effect-size estimation, and inference and diagnostics. It explicitly states that modelling does not create missing independent treatment replication; the experimental unit is defined by independent treatment allocation; donor and well are distinct inference targets; and a single donor cannot identify across-donor heterogeneity merely by adding a donor random effect. The read record is partial; no count matrices, sample sheets, or file versions are supplied.

**Inference.** (i) Statistical modelling choices (NB GLM, shrinkage, covariate terms) operate *within* a replication structure that must exist in the physical experiment; a model term cannot substitute for independently allocated replicates. (ii) Because donor-level and well-level variation differ in scope, the design matrix must encode the level at which treatment was randomized — if treatment was assigned per donor, donor is the experimental unit and the analysis unit; if per well within donor, wells are subsamples and must be aggregated or modeled with donor-level blocking such that the effective n is the number of donors. (iii) Absent supplied files, the plan must specify *procedures for recording and checking* inputs rather than assume their contents.

**Conclusion.** A defensible plan must (a) pin the experimental unit at independent treatment allocation before model specification, (b) freeze all inputs with checksums and recorded versions, (c) use a count model whose assumptions match the design (NB GLM with the design implied by the allocation), (d) pre-specify contrasts and FDR control, (e) regenerate all figures from code and frozen inputs, and (f) include a source-difference audit that detects any change between the documented and actual inputs. Each element is specified below.

---

## Ordered operational protocol (all steps proposed)

### Phase A — Preparation and quality checks (pre-data and at data receipt)

**A1. Input immutability.** Create a project root with two directories: `inputs/` (write-once, never edited) and `analysis/` (all scripts and generated outputs). At instantiation, record for every input file: relative path (placeholder: `inputs/counts/raw_counts.tsv`), SHA-256 checksum, byte size, and acquisition timestamp, in a `MANIFEST.sha256`. Make `inputs/` read-only at the filesystem level where possible. *Placeholder values only; no manifest exists at design time.*

**A2. Reference and annotation versions.** Record in `config.yaml` (proposed fields, values to be filled at run time):
- Genome assembly and source (e.g., placeholder `GRCh38`, download URL, accession).
- Annotation release (e.g., placeholder gene annotation version, GTF/GFF checksum) and its genome build compatibility.
- Transcriptome reference if alignment-free quantification is used (e.g., placeholder transcript FASTA checksum).
- Salmon/Kallisto or STAR/HISAT2 version strings; DESeq2 and R versions (`sessionInfo()` output captured at run).
- rRNA/ERCC spike-in set identity if used.

*Calibration procedure for unknowns:* when the annotation version is unrecorded, recover it from the provider's release notes for the stated download date, or re-download from the named repository and compare checksums; if the source is untraceable, flag the analysis as "annotation provenance unverified" rather than inventing a version. Verify genome/annotation build compatibility by checking that a random sample of gene coordinates in the GTF lies within chromosome lengths of the FASTA.

**A3. Sample sheet.** A single CSV with one row per sequencing library and columns (all entries placeholders until data receipt): `sample_id` (unique, machine-safe), `donor_id`, `well_id` (if applicable), `treatment` (levels: `control`, `treated`), `batch` (library-prep batch), `sequencing_run`, `library_prep_date`, `read_pair` layout, `expected_total_reads`, and any covariates (sex, age, passage). The sample sheet is frozen under checksum before unblinding of treatment labels to the analyst (A4). Any post-hoc change requires a new versioned file and a logged reason — never an edit in place.

**A4. Allocation and blinding records.** Record who randomized treatments, the allocation mechanism (e.g., block randomization at donor level — placeholder), and whether treatment labels were withheld from library prep and analysis staff. *Proposed standard:* randomized assignment at the level declared to be the experimental unit, performed by a person not performing library prep; labels released to the analyst only after QC pass/fail is determined on blinded data.

**A5. Blinded QC at data receipt.** Run FastQC/MultiQC (versions recorded) and alignment/quantification summary metrics with treatment labels masked. Checks (proposed thresholds, to be confirmed against the platform's historical distributions — these are calibration targets, not invented constants): per-sample total reads, duplication rate, adapter content, per-base quality, mapping rate, rRNA fraction, gene-body coverage uniformity, and number of detected genes (counts per million > 1, placeholder threshold). Flag — do not delete — outlier samples; exclusion criteria must be pre-specified and objective (see Phase E).

### Phase B — Independent units

**B1. Declare the experimental unit.** Before analysis, the plan records: *"The experimental unit is the independently allocated treatment unit."* If treatment was allocated per donor, n = number of donors and the donor is both the blocking factor and the unit of inference; wells are technical subsamples. If treatment was allocated per well within donors, wells are the units but treatment effects are estimated within the donor structure, and donor-to-donor generalization is limited to the donors actually studied. **If only one donor exists, the plan records that across-donor heterogeneity is unidentifiable; adding a donor term does not create replication, and conclusions are restricted to that donor.** This is recorded in the analysis report verbatim from the design declaration, per the curator's inference.

**B2. Aggregation rule (pre-specified).** If multiple wells per donor×treatment exist, pre-specify the aggregation: collapse well-level counts to the donor×treatment level by summation (for raw counts feeding a NB GLM), or model wells with donor as a fixed blocking factor and report the donor-consistent effect. The choice is made once, in the plan, before seeing count distributions. Do not choose post hoc whichever yields smaller p-values.

### Phase C — Intervention, sampling, and measurements (design-time documentation)

These steps are documented from the protocol record; where the record is partial (as it is here — the read record is partial), the plan requires that missing details be obtained from the experimenter or marked unknown, never filled by assumption:

- **Intervention:** compound/dose/duration (placeholders to record), vehicle control identity, and treatment timing relative to harvest.
- **Sampling:** time point, cell number or tissue mass targets, harvest method, RNA extraction kit and lot, DNase treatment, QC of input RNA (RIN or equivalent; proposed acceptance: RIN ≥ 7 for standard poly-A libraries, to be confirmed — calibration procedure: compare to the core facility's historical RIN–library-quality relationship, not to a literature constant).
- **Library prep:** kit and version, strandedness (must be recorded and verified empirically — proposed calibration: infer strandedness from a pilot alignment using read-through statistics with RSeQC and reconcile with the stated protocol; a mismatch triggers protocol review).
- **Sequencing:** platform, read length, depth targets, single vs paired end, randomization of samples across lanes/batches.
- **Controls:** include ERCC or similar spike-ins if absolute-change inference is intended (proposed); negative-control samples (untreated) distributed across batches; if batch effects are unavoidable, ensure treatment is balanced *within* each batch — this is a design constraint to verify before sequencing, because post hoc batch correction cannot rescue confounding.

### Phase D — Analysis (all proposed; executed only when inputs exist)

**D1. Count generation.** Align (or pseudoalign) with the recorded tool/version/reference; generate a gene-level raw count matrix. Counts, not normalized values, enter the model.

**D2. Count model.** Negative-binomial GLM as implemented in DESeq2 (per the source record): sample-specific size factors (median-of-ratios default), dispersion estimation with information sharing across genes, and Wald or likelihood-ratio tests. Record the design formula *in the frozen config* before unblinding. **Design decision tree (proposed, resolved by B1):**
- Treatment allocated per donor, multiple donors, randomized within donor: `~ donor + treatment` (donor as fixed blocking factor; the default recommendation because donor strata are typically few).
- Treatment and batch crossed with adequate replication: `~ batch + treatment` or `~ batch + donor + treatment` as applicable; never include a factor with as many levels as samples.
- Single donor: `~ treatment` with an explicit written limitation that donor heterogeneity is unestimable; no donor random effect is added for appearance's sake (it would be unidentifiable and would not create replication).
- Well-level data with donor-level allocation: aggregate to donor level (B2) so the residual degrees of freedom reflect independent units.

*Proposed alternative to pre-specify:* if size-factor assumptions fail (many genes with treatment-induced global shifts or extreme compositional bias), switch to spike-in-based or control-gene-based size factors, with the switch condition and procedure written in the plan (calibration: compare size-factor distributions with and without the alternative on the actual data and choose per the pre-specified criterion, not by outcome of DE tests).

**D3. QC of the fitted model.** Proposed checks before inference is accepted: PCA or distance heatmaps on variance-stabilized counts (blinded first pass already done in A5; now labeled, to confirm treatment separates as expected and batch effects are not confounded with treatment), residual mean–variance trend inspection, dispersion shrinkage diagnostics, and Cook's-distance flagging of influential samples.

**D4. Contrast and FDR.** Pre-specify in the frozen config: the primary contrast (placeholder: `treated vs control`), secondary contrasts if any, and the multiple-testing rule: Benjamini–Hochberg FDR at a pre-stated level (placeholder α = 0.05) applied genome-wide to the primary contrast; report the number of tests, the alpha, and independent-filtering behavior as run. State the minimum effect size of interest (placeholder: |log2 fold change| ≥ 1 with shrinkage applied for reporting, unshrunken for the test) *before* running. Sensitivity analyses (proposed): (i) re-run excluding each batch in turn; (ii) re-run with the alternative design formula from D2; report concordance rather than selecting the "better" result.

**D5. Diagnostics of unit integrity (audit step).** Verify computationally that the residual degrees of freedom equal the number of independent units minus model parameters; if the design matrix implies more replication than the allocation record supports, the analysis is stopped and returned to Phase B. This operationalizes the record's constraint that modelling cannot create missing replication.

### Phase E — Acceptance, stopping criteria, and troubleshooting (all proposed)

**Accept (analysis proceeds to reporting) when, all proposed:** manifest checksums verified; sample sheet complete with no ambiguous treatment labels; blinded QC thresholds met or outliers excluded only per pre-specified criteria; strandedness verified; design matrix matches the declared allocation; DESeq2 convergence without errors; diagnostic plots show no uncorrected confounding.

**Pre-specified exclusion criteria (objective only):** library failure (e.g., total reads below a recorded floor), sample swap detected by genotype/sex markers or PCA clustering with the wrong group, or documented technical error. **Non-criteria:** a sample that weakens the expected result is not excludable.

**Stopping/troubleshooting rules:**
- *Confounded batch × treatment:* stop and report as uninterpretable for treatment; do not "correct" it.
- *Excessive dropouts/zero inflation or outlier dispersion:* investigate per-sample library metrics; if a technical cause is documented, exclude with logged evidence; otherwise retain and report sensitivity analyses.
- *DESeq2 dispersion fitting failure:* inspect count distributions for low-count genes; apply pre-specified filtering (placeholder: keep genes with ≥ 10 reads total across samples), recorded as a parameter, not tuned to results.
- *Single donor limitation realized:* stop treatment-effect generalization; report within-donor inference only, with the limitation stated using the record's language.

### Phase F — Plot regeneration and reproducibility mechanics

- All figures produced by scripts (R/DESeq2 + ggplot2 or equivalent; versions recorded) reading only `inputs/` and `config.yaml`. Proposed figure set: QC metrics dashboard, PCA of variance-stabilized counts (pre- and post-labeling), sample distance heatmap, dispersion plot, size-factor plot, MA/volcano with FDR threshold annotated, count plots for top genes, and the sensitivity-concordance plot.
- A single entry-point (proposed: `make all` or a driver R script) rebuilds every figure and table from the frozen inputs. Verify by running twice into clean directories and diffing outputs (checksums may differ for figures with timestamps; normalize or exclude timestamps).
- Environment pinned via a container image or lockfile (placeholder: Docker image digest or renv lockfile checksum), recorded in the manifest.

### Phase G — Source-difference audit

Because the read record is partial, the plan includes an audit that compares documented vs actual inputs at run time:
1. Recompute SHA-256 of every file; compare against `MANIFEST.sha256`. Any mismatch halts the pipeline with a logged diff.
2. Reconcile the sample sheet against sequencing facility reports (sample IDs, indexes, run IDs); log any discrepancy.
3. Re-verify reference/annotation checksums against the provider's published checksums where available.
4. Diff the executed design formula and contrast list against the pre-registered frozen config; any deviation must be a new, versioned, logged amendment — never a silent change.
5. Emit an audit report (proposed template) listing: inputs + checksums, versions, config hash, session info, all parameter values used, all deviations, and the git commit hash of the analysis code.

---

## Alternatives considered and limits

- **limma-voom** is a valid alternative count model; proposed as the pre-specified sensitivity model in D4 to check robustness of calls across NB and linear-model frameworks. Chosen second to DESeq2 because the supplied record specifies DESeq2's NB GLM with shared dispersion.
- **Mixed models with donor random effects** are attractive in appearance but, per the record, do not identify across-donor heterogeneity from a single donor; the plan restricts random effects to settings with adequate donor numbers (placeholder: ≥ 5 donors proposed as a calibration to confirm against power simulation on pilot variance estimates).
- **edgeR** is a near-equivalent alternative; including it as a third sensitivity check is optional and should be pre-specified, not added after seeing results.
- **Limits.** (1) No files were supplied, so no parameter values, QC outcomes, or results exist here; every numeric setting is a placeholder pending calibration against the actual platform and tissue. (2) The intervention, sampling, and library-prep details are partially unknown (the read record is partial) and must be completed from experimenter records or flagged unknown. (3) If batch and treatment turn out to be confounded in the realized data, no analysis plan can recover the treatment effect; the plan's response is honest stopping, not correction. (4) All statements in this document are proposed designs; none constitutes an executed analysis or a result.
