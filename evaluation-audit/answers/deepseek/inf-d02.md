# DeepSeek V4.1 Flash / inf-d02

Original final answer, shared by both scoring rounds.

Recommended next action: do **not** run differential expression yet. First instantiate a locked, read-only input manifest and sample sheet that define the experimental unit as the independent treatment allocation unit. If treatment is allocated at donor/animal level, the donor/animal is the unit; if treatment is allocated only to wells within one donor, inference is limited to that donor’s wells and cannot be generalized across donors. The following is a **proposed, unexecuted** protocol. No count matrices, sample sheets, file versions, or results were supplied.

## 1. Evidence-to-inference-to-conclusion chain

**Evidence**
- E1: The DESeq2 record describes negative-binomial generalised linear models with information sharing for dispersion and effect estimation, inference, diagnostics, and states that modelling does not create missing independent treatment replication.
- E2: The experimental unit depends on independent treatment allocation; donor and well inference are distinct; a single donor cannot identify across-donor heterogeneity merely by adding a donor random effect.
- E3: The read record is partial; no actual count matrices, sample sheets, or file versions are supplied. Hypothetical constraints: treatment/control, possible donors, processing batches, no files at design time.

**Inference**
- I1: Any DE plan must first define and record the independent allocation unit before model fitting.
- I2: Donor and batch covariates must be justified by the design; they cannot manufacture replication or repair confounding.
- I3: Because no files are supplied, all paths, versions, numeric settings, and thresholds must be placeholders to be recorded, not executed.

**Conclusion**
- C: A reproducible bulk RNA-seq DE protocol can be specified as a locked pipeline with immutable inputs, a sample sheet, pinned reference/annotation versions, a count model, an explicit contrast and FDR rule, plot regeneration, and a source-difference audit. It cannot be executed or validated until the actual files and design are supplied. If the independent allocation unit is not identifiable, the analysis should stop rather than claim DE.

## 2. Design assumptions and estimand

**Proposed estimand:** the treatment effect on gene expression in independent treatment allocation units, reported as log2 fold change (Treatment vs Control) with uncertainty and FDR.

**Unknowns to calibrate, not invent:** number of independent units per group, donor structure, batch balance, library depth, dispersion, effect size, RNA quality, strandedness, species/tissue, and whether donors are paired or between-group. For each unknown, use a calibration procedure:
- Pilot or public data: estimate size factors, dispersion, mean-variance trend, and depth.
- Simulation: simulate negative-binomial counts under the proposed design across dispersion, effect-size, and depth grids; fit the same model; choose sample size/depth for target power at the pre-specified FDR.
- Batch effect: estimate from a balanced pilot or simulate; record as assumption if no data.
- Outlier thresholds: derive from pilot QC distributions, not post hoc.
- FDR and LFC thresholds: pre-register based on false-positive control and biological relevance; calibrate by simulation if needed.

## 3. Immutable inputs and version pinning

All inputs must be read-only and checksummed. A manifest should record SHA256 checksums, file sizes, and source paths. No manual editing of counts or sample sheets after lock.

**Inputs**
- Raw FASTQ files, or a precomputed gene-level count matrix if raw reads are unavailable.
- Sample sheet (CSV/TSV) with locked columns.
- Reference genome FASTA: source, release, checksum, URL.
- Annotation GTF/GFF: source, release, checksum, gene ID version, biotype.
- Transcriptome/index files, if used.
- Software versions: R, Bioconductor, DESeq2, aligner/quantifier, featureCounts, trimming tools, container digests, renv/conda lock, OS.
- Decision log: every parameter, exclusion, and change, with timestamp and reason.

**Sample sheet: minimum columns**

| Column | Requirement | Example/placeholder | Purpose |
|---|---|---|---|
| sample_id | required | S001 | unique sample |
| allocation_unit_id | required | A001 | independent treatment allocation unit |
| unit_type | required | donor/animal/well | defines experimental unit |
| donor_id | if applicable | D001 | pairing/blocking |
| condition | required | Treatment/Control | primary contrast |
| treatment | required | drug/vehicle | intervention |
| dose | if applicable | `<DOSE>` | intervention |
| batch_id | required | B01 | processing batch |
| biological_replicate | required | 1..n | within-group replicate |
| technical_replicate | if applicable | T1/T2 | not an experimental unit |
| fastq_1/fastq_2 | if raw | path | input |
| library_id | required | L001 | library |
| lane/index | if applicable | L1/i7 | sequencing |
| RIN | if applicable | numeric | RNA quality |
| sex/age | if applicable | M/F/numeric | covariates |
| tissue | required | liver | sample type |
| strandedness | required | yes/no/reverse | quantification |
| read_length | required | 100 | quantification |
| notes | optional | | audit trail |

**Reference and annotation versions** must be placeholders until supplied, e.g. `<GENOME_ASSEMBLY_VERSION>`, `<ANNOTATION_RELEASE>`, `<GTF_CHECKSUM>`. The same annotation must be used for quantification and gene-level summarisation unless a source-difference audit explicitly compares versions.

## 4. Experimental unit, allocation, and blinding

**Rule:** The experimental unit is the smallest unit independently assigned to treatment/control. 
- If whole animals/donors are allocated, `allocation_unit_id = donor_id`; n is the number of donors per group.
- If wells/dishes are allocated independently, the well is the allocation unit only if allocation is genuinely independent. Donor is a blocking factor if multiple donors contribute.
- Technical replicates, repeat libraries, or multiple sequencing lanes of the same library are not independent units.
- A single donor cannot support across-donor heterogeneity inference. Adding a donor random effect does not create replication or identify between-donor variance from one donor.

**Allocation and blinding:** pre-specify randomisation, allocation concealment, vehicle/control, and sample processing blinded to treatment where possible. Lock the analysis plan before unblinding treatment labels. Record any unblinding.

## 5. Preparation and quality checks

**Ordered proposed steps**
1. Verify checksums and sample sheet completeness; confirm no duplicate sample IDs, no missing condition, and correct allocation-unit coding.
2. Read QC: FastQC/MultiQC, adapter content, per-base quality, duplication, rRNA, overrepresented sequences. Trim with a pinned tool and parameters; record before/after QC.
3. Quantification: primary route, e.g. align with `<ALIGNER_VERSION>` to `<REFERENCE_VERSION>` and count with featureCounts against `<ANNOTATION_VERSION>`; secondary route, e.g. Salmon/tximport, for source-difference audit. Record strandedness and read length.
4. Count-matrix QC: library sizes, zero counts, gene biotypes, mitochondrial/ribosomal fractions. Pre-specify a low-count filter, e.g. genes with counts above `<MIN_COUNT>` in at least `<MIN_SAMPLES>` samples; DESeq2 independent filtering may additionally be used.
5. Sample-level QC: PCA, sample-to-sample correlation, hierarchical clustering, outlier metrics. Pre-specify outlier rules and report sensitivity with and without exclusions; do not remove samples silently.
6. Batch/donor balance: check cross-tabulations and variance inflation/estimability. If treatment is perfectly confounded with batch or donor, stop; the treatment effect is not separable.

## 6. Intervention and sampling

Record treatment dose, duration, vehicle, randomisation, and sampling time. Record tissue, preservation, RNA extraction, library prep, and sequencing batches. Controls should include untreated/vehicle controls, and where feasible positive/negative technical controls or spike-ins. All interventions and sampling are proposed placeholders until design is supplied.

## 7. Measurements

Primary measurement: gene-level counts. Secondary measurement: transcript-level estimates for audit. Record metadata including RIN, library concentration, index, lane, extraction batch, library prep batch, and sequencing batch. Measurements are not executed here.

## 8. Count model, contrast, and FDR

**Primary proposed model:** DESeq2 negative-binomial GLM. For gene i and sample j:
`K_ij ~ NB(mu_ij, alpha_i)`,
`log(mu_ij) = beta_i0 + beta_i1 * condition + ...`,
with dispersion `alpha_i` and effect estimates sharing information across genes. Inference is proposed via Wald test for the primary contrast, with diagnostics.

**Design formula depends on the independent allocation unit**
- Between-donor/animal groups, one treatment per unit: `~ batch_id + condition` if batch is not confounded. Do not include donor as a fixed effect if donor is nested within treatment and each donor receives only one condition; donor is the replicate.
- Paired within-donor design, each donor receives both conditions: `~ donor_id + condition`.
- Multiple donors with repeated wells: `~ donor_id + condition` if donor is a fixed block; if inference to a donor population is required, a mixed-model framework with multiple donors may be considered as a sensitivity analysis, but a single donor cannot identify across-donor heterogeneity.
- If batch is imbalanced, include batch only if estimable; otherwise revise the design or restrict inference.

**Proposed DESeq2 steps**
1. Construct `DESeqDataSet` from counts and sample sheet, or from tximport.
2. Set factor levels explicitly: `Control` as reference, `Treatment` as comparison.
3. Estimate size factors.
4. Estimate dispersions; inspect dispersion fit.
5. Fit GLM.
6. Extract contrast: `results(dds, contrast=c("condition","Treatment","Control"), alpha=<FDR_ALPHA>, independentFiltering=TRUE)`.
7. Optional LFC shrinkage for ranking/plots: `lfcShrink(..., type="<SHRINK_TYPE>")` as a placeholder.
8. Report `baseMean`, `log2FoldChange`, `lfcSE`, `stat`, `pvalue`, `padj`, number tested, and model formula.

**FDR and contrast rules**
- Primary FDR: Benjamini-Hochberg at `<FDR_ALPHA>` (placeholder, e.g. 0.05 only after pre-registration).
- Multiple testing is within the pre-specified gene set and primary contrast. If multiple contrasts are tested, pre-specify whether BH is across all genes within each contrast or across all contrasts; do not change post hoc.
- LFC threshold: `<LFC_THRESHOLD>` placeholder; report unthresholded and thresholded results. Do not lower FDR to force discoveries.

**Diagnostics**
- MA plot, p-value histogram, dispersion plot, Cook’s distance, residual patterns, size-factor vs library-size plot, sample clustering. Check convergence and outlier influence. Pre-specify acceptance limits.

## 9. Plot regeneration

All plots must be regenerated from locked inputs and saved model objects, with no manual editing.

**Required regenerable outputs**
- Sample QC: read counts, alignment rate, rRNA, RIN, library size.
- PCA and sample-to-sample heatmap, coloured by condition/batch/donor.
- Dispersion estimates and mean-dispersion fit.
- MA plot, volcano plot, p-value histogram.
- Heatmap of top DE genes, per-gene normalised counts/boxplots.
- Batch/donor balance plots.
- Session information and package versions.

**Regeneration rules**
- Scripts in version control; parameters in a config file; seeds fixed for jitter/clustering.
- Outputs written to a new results directory with checksums and a manifest.
- A single command, e.g. `<MAKE_COMMAND>` or `<NEXTFLOW_COMMAND>`, regenerates all plots and tables.

## 10. Source-difference audit

Purpose: detect and document discrepancies between the supplied source materials, primary quantification, secondary quantification, and annotation versions.

**Proposed audit steps**
1. Verify that sample sheet IDs match raw file names, FASTQ read groups, and checksums.
2. Compare primary and secondary count sources at sample level: library sizes, detected genes, correlation, clustering.
3. Compare gene-level normalised counts: log2 differences, rank changes, MA plots. Flag genes above `<AUDIT_LOG2_DIFF>` or with rank change beyond `<AUDIT_RANK_DIFF>`.
4. Map discrepancies to annotation features: multi-transcript genes, overlapping genes, intronic reads, mitochondrial/rRNA, sex chromosomes, duplicated regions, gene ID version changes.
5. If annotation versions differ, quantify overlap and gene ID mapping; report genes lost or gained.
6. Decision rule: if discrepancies affect pre-specified genes or top DE results, investigate cause. If unresolved, report sensitivity using both sources. If only one source exists, state that the source-difference audit could not be performed.

**Output:** an audit report with discrepancy counts, examples, resolution, and effect on the DE list.

## 11. Acceptance and stopping criteria

**Before analysis**
- All inputs present, checksummed, and read-only.
- Sample sheet valid; experimental unit explicitly identified.
- Reference and annotation versions pinned.
- Design matrix full rank; treatment not perfectly confounded with batch/donor.
- Independent units per group sufficient by calibrated power/simulation.

**During QC**
- Pre-specified read, alignment, rRNA, and RIN thresholds met. If not, stop and resequence or document exclusion with sensitivity analysis.
- No sample outlier drives the primary result without sensitivity reporting.

**During modelling**
- Dispersion estimates converge; diagnostics acceptable.
- No severe model misspecification; p-value histogram and MA plot reviewed.
- Cook’s distance outliers handled by pre-specified rule.

**Analysis**
- Primary contrast and FDR rule pre-specified.
- If no genes pass FDR, report power/sensitivity; do not lower FDR post hoc.
- Stop if independent allocation cannot be verified, if only one donor is available for donor-level inference, or if confounding prevents separation.

## 12. Troubleshooting

| Problem | Proposed action |
|---|---|
| Low alignment | Check reference version, adapter contamination, rRNA, strandedness. |
| Batch confounding | Include batch if estimable; otherwise revise design or restrict inference. |
| Donor heterogeneity | Use donor as fixed block if paired; if between-donor, donor is the replicate. Single donor limits inference. |
| Zero counts | Pre-specified filter; use DESeq2 independent filtering. |
| Dispersion outliers | Inspect genes; consider robust/alternative model as sensitivity, not silent removal. |
| Odd p-value histogram | Check batch, outliers, model formula, normalisation. |
| Source discrepancies | Resolve annotation/strandedness/multimapping; report sensitivity. |
| Insufficient power | Use calibration/simulation; do not relax FDR post hoc. |

## 13. Alternatives, limits, and what would change the recommendation

**Alternatives**
- edgeR or limma-voom negative-binomial/linear modelling.
- Mixed-effects models for donor random effects when multiple donors exist and the estimand requires population-level donor inference.
- Transcript-level DE with tximport; gene-level summarisation as primary.
- Non-parametric or permutation approaches as sensitivity analyses.

**Limits**
- No files were supplied; no analysis can be executed or validated.
- Versions, paths, thresholds, sample size, and design are placeholders.
- DESeq2 modelling does not create missing independent treatment replication.
- A single donor cannot identify across-donor heterogeneity by adding a donor random effect.
- Source-difference audit is impossible without at least one second source or supplied original counts.
- The read record is partial; no claim about actual author methods or results is made.

**What would change the recommendation**
- Supplied FASTQ/counts, sample sheet, and design: instantiate the locked manifest, sample sheet, reference versions, and run the pipeline.
- If treatment allocation is well-level within one donor: redefine the estimand as within-donor and do not generalise.
- If multiple donors are paired: use `~ donor + condition`.
- If donors are between-group: donor is the independent unit; use `~ condition + batch` and do not include donor as a fixed effect unless estimable.
- If batch is confounded: redesign or stop.
- If pilot data exist: calibrate sample size, dispersion, depth, and thresholds before unblinding.
