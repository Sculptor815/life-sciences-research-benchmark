# Claude Opus 4.6 / inf-d02

Original final answer, shared by both scoring rounds.

# Proposed Reproducible Bulk RNA-seq Differential-Expression Analysis Plan

## Lead Conclusion and Recommended Action

**All analyses described below are proposed; no files are supplied and no execution has occurred.** The plan specifies every input, parameter and decision rule needed so that an independent auditor can regenerate every output from immutable inputs alone, with no hidden state. The single most consequential design requirement is that the experimental unit must be the independent treatment allocation (typically the biological donor or independent culture assigned to treatment), not the sequencing lane, well, or technical replicate. Violating this inflates degrees of freedom and produces false positives that no statistical correction can rescue, because—as stated in the evidence—"modelling does not create missing independent treatment replication."

---

## 1. Immutable Inputs and Version Pinning

All items below are placeholders to be recorded at execution time; none are executed here.

| Element | Placeholder | Audit requirement |
|---|---|---|
| Raw FASTQ files | `data/raw/{sampleID}_{R1,R2}.fastq.gz` | SHA-256 checksums recorded in `checksums.sha256` |
| Reference genome | e.g., GRCh38 primary assembly, Ensembl release `{VER}` | Exact URL, file name, download date, SHA-256 |
| Gene annotation | GTF from same Ensembl release `{VER}` | Same provenance record |
| Software versions | STAR `{x.y.z}`, Salmon `{x.y.z}`, DESeq2 `{x.y.z}`, R `{x.y.z}` | Recorded in `environment.yaml` or `renv.lock` |
| Analysis code | Git-tracked; tagged release hash at run time | Repository URL + commit SHA |
| Sample sheet | `metadata/sample_sheet.tsv` (see §2) | SHA-256; versioned in same repository |

**Source-difference audit.** Any change to any input (FASTQ, reference, annotation, sample sheet, code) is detectable by comparing SHA-256 digests. The proposed pipeline stores all digests in a manifest file committed before analysis begins. Re-running from the manifest must reproduce bit-identical count matrices and, given identical random seeds, identical statistical outputs.

---

## 2. Sample Sheet Specification

The sample sheet is the sole bridge between raw files and statistical model. Proposed required columns:

| Column | Definition | Why required |
|---|---|---|
| `sample_id` | Unique sequencing-library identifier | Links to FASTQ filenames |
| `donor_id` | Independent biological unit identifier | Defines the experimental unit (§3) |
| `treatment` | Factor: `treatment` or `control` | Primary contrast variable |
| `batch` | Processing/library-prep batch label | Potential confound to model or block |
| `lane` | Sequencing lane | Technical covariate; never an experimental unit |
| `sex`, `age_bin` | Known biological covariates (if available) | Candidate covariates; inclusion decided by design, not data |

No column may be derived post-hoc from expression data; all must be determined before counts are generated.

---

## 3. Experimental Unit, Replication, and Allocation

### 3.1 Definition of the Experimental Unit

The experimental unit is the entity independently assigned to a treatment condition. Per the evidence: "The experimental unit depends on independent treatment allocation; donor and well inference are distinct." If treatment is applied per donor, then donor is the experimental unit. If treatment is applied per well from the same donor, those wells are technical (or at best pseudo-) replicates of that donor and must not be treated as independent units.

**Operational rule.** Count the number of distinct values of `donor_id` per level of `treatment`. The residual degrees of freedom for the treatment contrast derive from this count, not from the number of FASTQ files or wells.

### 3.2 Allocation and Blinding

- **Proposed randomisation:** Donors are randomised to treatment and control via a reproducible pseudo-random assignment (seed recorded).
- **Proposed blinding:** Sample IDs used during library preparation and sequencing are non-informative regarding treatment; the key linking `sample_id` to `treatment` is recorded in the sealed sample sheet.

### 3.3 Handling Multiple Wells or Lanes per Donor

If a single donor contributes multiple libraries (wells, lanes), two valid proposed approaches exist:

1. **Collapse before modelling:** Sum raw counts across technical replicates of the same donor×treatment combination to produce one count vector per experimental unit. This is the default proposed approach.
2. **Model technical replicates explicitly:** Fit a model with donor as the unit and a within-donor correlation structure, but this does not create additional independent replication. As stated: "a single donor cannot identify across-donor heterogeneity merely by adding a donor random effect."

Approach 1 is proposed as the primary analysis because it keeps the matrix dimensions honest and avoids pseudo-replication.

---

## 4. Proposed Ordered Protocol

### Phase A — Preparation and Quality Checks

| Step | Tool (placeholder) | Proposed action |
|---|---|---|
| A1 | `FastQC {ver}` | Per-FASTQ quality metrics; flag samples with >30 % adapter or mean Q < 25 |
| A2 | `MultiQC {ver}` | Aggregate QC; archive HTML report with SHA-256 |
| A3 | `Trim Galore {ver}` or `fastp {ver}` | Adapter and quality trimming; parameters recorded (e.g., `--quality 20 --length 36`) |
| A4 | Re-run FastQC | Confirm trimming efficacy |

**Acceptance criterion A:** No sample excluded without documented, pre-registered reason (e.g., < `{MIN_READS}` total reads; exact threshold recorded before inspection of expression data).

### Phase B — Alignment and Quantification

| Step | Proposed tool | Key parameters (placeholders) |
|---|---|---|
| B1 | `STAR {ver}` two-pass or `Salmon {ver}` quasi-mapping | Genome index built from pinned reference + GTF |
| B2 | `featureCounts` (Subread `{ver}`) or Salmon quant | Strand setting verified by `infer_experiment.py`; gene-level counts |
| B3 | Collapse technical replicates | Sum counts by `donor_id × treatment` as described in §3.3 |

Output: a single integer count matrix `counts.tsv` with columns = experimental units, rows = genes. SHA-256 recorded.

### Phase C — Exploratory Diagnostics (Proposed)

These plots are regenerated deterministically from `counts.tsv` and `sample_sheet.tsv`.

1. **Library-size bar plot** — total counts per experimental unit.
2. **PCA / MDS of variance-stabilised counts** — colour by `treatment`, shape by `batch`; inspect for batch-driven clustering.
3. **Hierarchical clustering dendrogram** — same transformed counts; Euclidean distance, Ward linkage.
4. **Sample-to-sample correlation heatmap.**
5. **Cook's distance box plots per sample** (after model fit, §Phase D).

**Decision rule:** If PCA shows batch dominates treatment, the model in Phase D must include `batch`. If a sample is a clear outlier on ≥ 2 diagnostics and an independent wet-lab explanation exists, it may be excluded; the exclusion and reason are recorded in the sample sheet (new column `excluded`, with `reason`), and the full analysis is re-run. Both included and excluded results are reported.

### Phase D — Statistical Model (Proposed)

#### D1. Count Model

Per the evidence, DESeq2 fits "negative-binomial generalised linear models with information sharing for dispersion and effect estimation." The proposed model:

```
design: ~ batch + treatment
```
- **Family:** Negative binomial (NB).
- **Dispersion estimation:** DESeq2 shrinkage (empirical Bayes, sharing information across genes).
- **Effect-size estimation:** Proposed use of `lfcShrink()` with `type = "apeglm"` (or `"ashr"`); exact type recorded.
- **Size-factor normalisation:** Median-of-ratios (DESeq2 default).

If `batch` is fully confounded with `treatment` (determinable from the sample sheet), it cannot be included and this must be reported as a limitation.

#### D2. Contrast

Primary contrast (proposed):

```
contrast: treatment vs. control (treatment as numerator)
```
Encoded as `results(dds, contrast = c("treatment", "treatment", "control"))` or equivalent.

Secondary contrasts, if any, are pre-registered in the analysis plan before data inspection.

#### D3. FDR Control

- **Method:** Benjamini–Hochberg (BH) adjusted p-values (DESeq2 default).
- **Threshold:** Proposed α_adj = 0.05. Genes with `padj < 0.05` are called differentially expressed.
- **Independent filtering:** DESeq2 automatic independent filtering on mean of normalised counts (threshold chosen to maximise discoveries at the specified α).
- **Log2 fold-change threshold (optional):** If a minimum effect size is scientifically meaningful, propose `lfcThreshold = log2(1.5)` with a likelihood-ratio or Wald test against that threshold, clearly distinguished from post-hoc fold-change filtering.

#### D4. Diagnostics of Model Fit

| Diagnostic | What it checks |
|---|---|
| Dispersion plot (`plotDispEsts`) | Shrinkage behaviour; no genes with dispersion orders of magnitude above trend |
| MA plot | Symmetry of fold changes; no abundance-dependent bias |
| P-value histogram (raw) | Should be uniform under null with a spike near 0; anti-conservative shapes indicate model mis-specification or unmodelled confounds |
| Cook's distance | Influential observations; DESeq2 flags genes with high Cook's for individual samples |

### Phase E — Result Outputs and Plot Regeneration

All outputs are regenerated by running the version-controlled script on the immutable inputs:

1. **Results table:** `results/de_genes.tsv` — all genes, with baseMean, log2FoldChange, lfcSE, stat, pvalue, padj. SHA-256 recorded.
2. **Volcano plot:** x = shrunken log2FC, y = −log10(padj), with α and FC thresholds marked.
3. **Heatmap of top DE genes** (e.g., top 50 by padj) using variance-stabilised counts, clustered by row and column.
4. **PCA coloured by treatment** (repeat from Phase C for the final sample set).

**Plot regeneration guarantee.** Because all random seeds, software versions, inputs and parameters are recorded, re-executing the pipeline from the manifest must produce identical plots. Any discrepancy indicates hidden state or an unrecorded dependency—this is the source-difference audit.

---

## 5. Source-Difference Audit Procedure (Proposed)

1. An auditor receives: (a) the git repository at the tagged commit, (b) the checksum manifest, (c) the archived FASTQ files and reference files.
2. The auditor verifies all SHA-256 digests.
3. The auditor rebuilds the software environment from `environment.yaml` / `renv.lock`.
4. The auditor executes the pipeline end-to-end.
5. Output checksums are compared to the original output manifest. Bit-identical results confirm no hidden state. Any difference triggers investigation of unrecorded parameters (e.g., thread-order non-determinism in alignment—mitigated by fixing `--outBAMsortingBinsN` or by using deterministic quantification with Salmon).

---

## 6. Acceptance / Stopping Criteria and Troubleshooting

| Issue | Proposed criterion / remedy |
|---|---|
| Too few DE genes (0 at padj < 0.05) | Check p-value histogram; if uniform, the study may be underpowered. Report as negative result; do not lower α. |
| Anti-conservative p-value histogram | Investigate unmodelled covariates (batch, sex); add to design if justified a priori. |
| Batch dominates PCA | Include batch in model; if confounded with treatment, the experiment cannot separate effects—report limitation. |
| One treatment group has n = 1 donor | No valid inference on treatment effect is possible. "Modelling does not create missing independent treatment replication." Halt analysis; recommend additional biological replication. |
| High Cook's distance for a sample | Inspect wet-lab records. If an independent reason exists, exclude and re-run; report both analyses. |

### Calibration of Unknown Parameters

- **Minimum read-depth threshold for sample inclusion:** Propose calibrating by examining the distribution of total counts; a common starting point is `{MIN_READS}` = 5 × 10⁶, but this must be fixed before inspecting per-gene counts.
- **Gene-level filtering (minimum count):** DESeq2's independent filtering handles this internally; no manual pre-filter is proposed unless computational constraints require one, in which case the rule (e.g., ≥ 10 counts in ≥ n samples, where n = smallest group size) is recorded before execution.
- **Number of biological replicates needed:** A power analysis (e.g., via `RNASeqPower` or simulation) should be performed before the experiment using pilot dispersion estimates. This is a proposed pre-experimental step; no data are available to execute it here.

---

## 7. Alternatives and Limits

- **Alternative models:** edgeR (NB with different dispersion estimator), limma-voom (transforms counts to log-CPM with precision weights, uses linear models). These provide complementary sensitivity/specificity profiles and could be run as sensitivity analyses on the same count matrix.
- **Donor as random effect (e.g., via dream/variancePartition or DESeq2 with ~batch + donor + treatment where donor is nested):** Only valid if there are repeated measures within donors across treatment conditions. Does not rescue a design with a single donor per condition.
- **Limits of this plan:** (i) No files are supplied; all paths and thresholds are placeholders. (ii) Bit-identical reproducibility may require containerisation (Docker/Singularity with fixed image digest) to control system-library versions. (iii) Floating-point non-determinism across CPU architectures can cause minor numerical differences in p-values; the plan should record architecture and, for critical audits, provide the container image.

---

## Evidence-to-Inference Chain (Summary)

1. **Evidence:** DESeq2 uses NB GLMs with empirical-Bayes dispersion shrinkage; it does not create independent replication.
2. **Inference:** The statistical model must receive one column per independent experimental unit (donor assigned to treatment), not per well or lane. Technical replicates must be collapsed or explicitly accounted for.
3. **Conclusion:** A reproducible plan must (a) define the experimental unit from the allocation design, (b) pin every input and version, (c) pre-register the model, contrast, and FDR threshold, and (d) provide a checksum-based audit trail so that any analyst can regenerate all outputs and verify no hidden state exists.

**All elements above are proposed. No execution has occurred and no results are claimed.**
