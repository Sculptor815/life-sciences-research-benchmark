# Claude Opus 4.8 / inf-d02

Original final answer, shared by both scoring rounds.

# Proposed Reproducible Bulk RNA-seq Differential-Expression Analysis Plan

**Status: fully proposed. No files were supplied; nothing below has been executed. Every path, version string, numeric threshold and parameter is a placeholder to be recorded at run time, not an invented result.**

---

## 1. Lead conclusion and recommended design

The audit-safe plan centres on one non-negotiable rule drawn directly from the evidence packet: **the experimental unit is the level of independent treatment allocation, not the sequenced library or the well.** DESeq2's negative-binomial GLM with dispersion/effect shrinkage is an appropriate count model, but the curator interpretation is explicit that *statistical modelling does not manufacture independent replication*. Therefore the plan's validity hinges on correctly declaring the unit before any model is fit, and on making every input immutable and every transformation re-derivable from recorded state.

Recommended action: construct a pipeline in which (a) raw inputs are content-addressed (hashed) and read-only, (b) a sample sheet encodes the allocation structure and blocking factors, (c) reference/annotation versions are pinned, (d) the count model and contrast are specified a priori, (e) all plots regenerate from a single deterministic script, and (f) a "source-difference audit" compares recorded inputs against the curator's source summary to flag any claim that exceeds the evidence. If donors number one, or if donor is confounded with batch, the plan must downgrade its inferential claim rather than add a random effect to rescue it.

---

## 2. Concepts and their relationships

**Experimental unit vs. observational unit.** The experimental unit is whatever received an independent, separately randomised application of treatment. Replicate libraries, multiple wells from one culture, or multiple aliquots from one donor are *observational/technical* subunits nested within that unit. Pseudoreplication occurs when subunits are counted as independent degrees of freedom.

**Donor inference vs. well inference (distinct, per evidence).** Well-level variation estimates technical/processing dispersion within a biological source. Donor-level variation estimates biological heterogeneity across sources. These answer different questions. The evidence states a single donor cannot identify across-donor heterogeneity: with one donor, a "donor random effect" has no between-donor variance to estimate and cannot license population-level conclusions. The design must therefore record donor count and scope conclusions accordingly.

**Count model (DESeq2).** Gene counts are modelled as negative-binomial with a gene-wise mean linked to a design matrix; dispersions are estimated with information sharing (shrinkage toward a trend), and log fold-changes may be shrunk for stable ranking. This is the measurement-to-effect engine, but it inherits whatever (in)dependence the design declares.

**Contrast and FDR.** A contrast is a specified linear combination of model coefficients (e.g., treatment vs. control). Multiplicity across genes is controlled by a false-discovery-rate procedure at a pre-registered threshold.

**Immutability and auditability.** "No hidden state" means every output is a pure function of recorded, hashed inputs plus a recorded environment. Nothing depends on interactive memory, ad hoc edits, or unversioned files.

---

## 3. Evidence → inference → conclusion chain

- **Evidence:** DESeq2 uses NB-GLM with dispersion/effect information sharing, inference and diagnostics. → **Inference:** it is a defensible count model for bulk RNA-seq with modest replication because shrinkage stabilises per-gene estimates. → **Conclusion:** adopt DESeq2 (or an equivalent NB-GLM) as the proposed count model, with parameters recorded not invented.

- **Evidence:** "modelling does not create missing independent treatment replication." → **Inference:** adding terms (including random effects) cannot substitute for having independently allocated units. → **Conclusion:** fix the experimental unit at allocation level; set n from independent allocations; refuse to inflate n with technical replicates.

- **Evidence:** "donor and well inference are distinct; a single donor cannot identify across-donor heterogeneity merely by adding a donor random effect." → **Inference:** the admissible inferential scope depends on how many independent donors exist and whether donor is confounded with treatment/batch. → **Conclusion:** the sample sheet must capture donor and batch; the analysis must branch on donor count; conclusions must be scoped (within-donor vs. across-donor).

- **Evidence:** "the read record is partial, and no actual count matrices, sample sheets or file versions are supplied." → **Inference:** no numeric result can be asserted. → **Conclusion:** everything is a proposed protocol with calibration procedures and placeholders.

---

## 4. Immutable inputs (content-addressed)

Record, for every input, a cryptographic hash (e.g., SHA-256 placeholder `<hash>`), a path, and a byte size, in a manifest file `inputs.manifest.tsv`. Inputs are stored read-only.

| Input | Placeholder identifier | Immutability control |
|---|---|---|
| Raw FASTQ (per library) | `fastq/<lib>_{R1,R2}.fastq.gz`, hash `<h>` | read-only; hashed |
| Reference genome FASTA | `GENOME=<assembly>:<release>` | pinned release + hash |
| Gene annotation GTF/GFF | `ANNOT=<source>:<version>` | pinned version + hash |
| Transcriptome index (if pseudo-alignment) | built from above; record builder version | hash of index |
| Sample sheet | `samplesheet.tsv`, hash `<h>` | version-controlled |
| Environment lockfile | container digest / package lock, hash `<h>` | pinned |

**Rationale:** auditability requires that re-running the pipeline on the same hashed inputs with the same environment reproduces identical counts and statistics. Any input change changes a hash, which the audit surfaces.

---

## 5. Sample sheet schema

A single machine-readable `samplesheet.tsv`. One **row per sequenced library**, with an explicit column distinguishing library from experimental unit so pseudoreplication cannot be hidden.

Required columns (placeholders):
- `library_id` — unique per FASTQ pair.
- `experimental_unit_id` — the independent allocation unit; **this is the level of n.**
- `donor_id` — biological source (may equal `experimental_unit_id` or be coarser/finer).
- `condition` — `treatment` / `control`.
- `batch` — processing/library-prep batch.
- `lane`/`run` — sequencing technical factor.
- `allocation_time`/`allocation_seed` — when/how treatment was assigned.
- `tech_replicate_of` — null unless this library is a technical replicate of another.
- `rin`/`qc_flag` — RNA integrity and QC placeholders.

**Key integrity constraint:** the number of distinct `experimental_unit_id` values **per condition** is the replication count. Multiple `library_id` rows sharing one `experimental_unit_id` are subunits and must be aggregated (Section 9) before unit-level inference.

---

## 6. Reference and annotation versioning

- Pin genome assembly and release (`<assembly>:<release>`) and annotation (`<source>:<version>`). Record both the human-readable version and the file hash.
- Record the exact tools and versions used to build any index (aligner/quantifier version placeholder `<tool>@<ver>`).
- Record whether quantification is at gene or transcript level and whether `tximport`-style summarisation to gene level is applied.
- **Calibration, not invention:** if the correct annotation version is unknown, do not guess. Calibrate by (i) checking chromosome naming and gene-id scheme match between FASTA, GTF and any downstream ID maps, and (ii) confirming a high assignment rate in QC (Section 8). Record the chosen version once fixed.

---

## 7. Preparation and quality checks (ordered)

1. **Verify inputs.** Recompute hashes; confirm they match `inputs.manifest.tsv`. Abort if any mismatch.
2. **Per-library read QC.** Run a read-QC tool (version pinned). Record per-library: total reads, duplication, adapter content, per-base quality, GC. Thresholds are **calibrated from the batch's own distribution** (e.g., flag libraries beyond a pre-declared robust cutoff such as median ± k·MAD, with k recorded), not from invented absolute values.
3. **Trimming/filtering (optional, recorded).** If applied, pin the tool and parameters; re-QC after.
4. **Quantification.** Align/pseudo-align to the pinned reference; produce per-library counts. Record assignment/mapping rate.
5. **Post-quant QC.** Record library size, fraction assigned to features, rRNA/mito fraction, and gene-detection count per library.

**Gate:** proceed only if QC metrics are within pre-declared calibrated bounds. Any excluded library is logged with reason in an exclusions file (no silent drops).

---

## 8. Independent units, allocation and blinding

**Independent units.** Declare before analysis: `n_treatment` and `n_control` counted as distinct `experimental_unit_id`s. If a unit contributes multiple libraries (lanes/wells/aliquots), these are technical subunits.

**Allocation.** Record the randomisation that assigned treatment to units (seed/scheme placeholder). If allocation was not random, record it as observational and scope conclusions accordingly — the count model cannot repair non-random allocation.

**Blocking against confounding.** The decisive audit check: cross-tabulate `condition × batch` and `condition × donor`. If treatment is perfectly confounded with batch or donor, the treatment effect is **not identifiable** separately from that nuisance factor; record this and either (a) restrict inference, or (b) declare the design inadequate. No modelling term fixes full confounding.

**Blinding (proposed).** Where feasible, blind sample-prep and QC-exclusion decisions to condition by using de-identified `library_id`s; record who was blinded and at which steps. Analysis code is condition-agnostic until the contrast step.

---

## 9. Handling technical subunits (anti-pseudoreplication)

Before fitting the unit-level model:
- **Aggregate technical replicates** sharing one `experimental_unit_id` by summing raw counts (recorded as the collapse step). Summation preserves the NB count structure; this yields one count column per experimental unit.
- Alternatively, if subunit structure is itself of interest, fit a mixed NB model with a random intercept for `experimental_unit_id` — but **only** when there are enough independent units to estimate between-unit variance. Per the evidence, a single donor/unit cannot support across-unit heterogeneity estimation, so default to aggregation when units are few.

This step is where pseudoreplication is mechanically prevented: the design matrix will have one row per experimental unit, not per library.

---

## 10. Count model specification (a priori)

- **Model:** negative-binomial GLM (DESeq2-style). Counts ~ NB(mean, dispersion); mean linked to design matrix.
- **Design formula (placeholder):** `~ batch + condition`, where `batch` is included **only if** it is not confounded with `condition` and has ≥2 levels with units in each cell. If donors are multiple and crossed with condition, use `~ donor + condition` or a mixed model; if donor is nested/confounded, see Section 12.
- **Normalisation:** size-factor / median-of-ratios estimation (recorded). 
- **Dispersion:** gene-wise estimates shrunk toward a fitted trend (information sharing), per the DESeq2 record.
- **Reference level:** `condition` reference set to `control` (recorded) so the coefficient sign is interpretable.
- **Independent filtering:** apply the method's standard low-count filtering; record the rule.

All of formula, reference level, filtering and shrinkage choices are fixed **before** seeing p-values.

---

## 11. Contrast, effect shrinkage and FDR

- **Contrast:** `treatment − control` on the `condition` coefficient. Record the exact contrast specification.
- **LFC shrinkage:** apply shrinkage (e.g., apeglm-style) for ranking/visualisation; report both shrunken and unshrunken LFC so the audit can see the transformation. Record the shrinkage method and version.
- **FDR:** control at a **pre-registered** threshold (placeholder `alpha = <q>`, e.g. 0.05) using Benjamini–Hochberg (or the method's adjusted p-value). Record both nominal p and adjusted p per gene.
- **Effect-size floor (optional, pre-registered):** if a minimum biologically meaningful |LFC| is set, declare it a priori; do not choose it after inspecting results.

**Output:** a results table with gene id, baseMean, LFC (shrunk and raw), SE, stat, p, p-adj, and a significance flag at `alpha`. Written to `results/de_table.tsv` with its own hash.

---

## 12. Branching on donor/batch structure (the evidence-driven core)

The analysis **must** take one of these recorded branches:

1. **Multiple donors, crossed with condition (ideal).** Donor enters the design as a blocking factor (fixed) or random intercept (if enough donors). Conclusions may be scoped to *across-donor* (population-level) within the sampled donor range.

2. **Single donor, multiple independent treatment allocations within it.** Inference is *within-donor only*. Explicitly state that across-donor heterogeneity is not estimable and population generalisation is unsupported — adding a donor random effect is impossible/ill-posed with one donor, per the evidence.

3. **Donor confounded with condition or batch.** Treatment effect not separable from the confounder. Report non-identifiability; do not present a treatment p-value as if it were clean. Recommend redesign.

The branch chosen, and why, is written to the audit log.

---

## 13. Plot regeneration

All figures regenerate deterministically from `results/de_table.tsv` plus the normalised count object, via one script `make_plots.R|py` (version pinned, random seed fixed where applicable):
- **Library/unit QC:** size factors, detected-gene counts.
- **Sample relationships:** PCA / sample-distance heatmap on variance-stabilised counts, coloured by condition, donor and batch — this visually exposes batch/donor dominance and confounding.
- **Dispersion plot:** gene-wise vs. fitted dispersion trend (model diagnostic).
- **MA plot** and **volcano plot** at the pre-registered `alpha`.
- **Top-gene count plots** at the experimental-unit level.

Each plot file is hashed. Because inputs and script are pinned, re-running reproduces byte-stable or numerically identical figures. No manual post-editing.

---

## 14. Source-difference audit

Purpose: guarantee no conclusion exceeds the supplied evidence and no hidden state crept in. Produce `audit_report.md` that mechanically checks:

1. **Input integrity:** recomputed hashes == manifest. Pass/fail.
2. **Environment:** recorded container/lockfile digest == the one used. Pass/fail.
3. **Unit integrity:** `n` used in the model == count of distinct `experimental_unit_id` per condition; technical replicates collapsed. Flag any library-level inflation.
4. **Confounding matrix:** `condition × batch` and `condition × donor` tables; flag empty cells / perfect confounding.
5. **Design vs. evidence:** assert that the design formula and claim scope match the donor branch (Section 12); flag if a single-donor dataset asserts across-donor conclusions, or if a random effect was added without sufficient units (the specific failure the evidence warns against).
6. **Source consistency:** compare each stated claim to the curator source summary; flag any statement about DESeq2 or replication that is not supported by, or contradicts, the summary. Flag any numeric *result* claim (forbidden: no files).
7. **Plot provenance:** every figure traces to a hashed results file + script commit.

The audit output is itself versioned and hashed.

---

## 15. Acceptance and stopping criteria

**Pre-analysis acceptance (must all pass to proceed to inference):**
- All input hashes verified.
- Each condition has ≥ the pre-declared minimum independent units (placeholder `n_min`, justified by a calibration in Section 17, not invented).
- No perfect confounding of `condition` with `batch` or `donor`.
- QC metrics within calibrated bounds; exclusions logged.

**Analysis acceptance:**
- Dispersion trend fit is sensible (diagnostic plot shows gene-wise estimates scattered around the trend, not pathological).
- PCA does not show condition effect wholly explained by batch.
- Model converges; no coefficient aliasing warnings unaddressed.

**Stopping / do-not-report criteria:**
- Confounding non-identifiable → stop, recommend redesign.
- Single-donor data where the question requires across-donor inference → report only within-donor, or stop for population claims.
- Inputs or environment unverifiable → stop (audit fails).

---

## 16. Alternatives and limits

**Model alternatives:** edgeR (NB-GLM with quasi-likelihood) or limma-voom (precision-weighted linear models) are defensible substitutes; limma-voom is often more robust with larger n, DESeq2/edgeR with small n. Choice is recorded; it does not change the unit rule.

**Replication alternatives:** with very few units, consider that no method yields trustworthy population inference; the honest alternative is to report effect sizes with wide uncertainty and label them exploratory.

**Confounding alternatives:** surrogate-variable or RUV-style latent-factor correction can remove unwanted variation *only when* treatment is not confounded with the unwanted factor; record and justify, and treat as sensitivity analysis, not primary.

**Limits (explicit):**
- No files supplied → no results, effect sizes, or gene lists can be claimed; all numbers are placeholders.
- The read record is partial; the plan cannot assert anything the source summary does not support.
- DESeq2's shrinkage improves stability but cannot create replication or identify confounded effects.
- A single donor caps inferential scope at within-donor regardless of modelling.

---

## 17. Calibration procedures for unknown parameters

Because author methods are not supplied, unknown settings are **calibrated and recorded**, never invented:

- **QC thresholds:** derive from the dataset's own metric distributions (robust central tendency ± recorded multiplier); pre-register the rule, then apply.
- **Minimum replication `n_min`:** set by a proposed power/feasibility calibration — e.g., simulate NB counts across a plausible dispersion range (estimated from pilot or public data of matched tissue) to find the n giving acceptable detection at the pre-registered `alpha` and effect floor. Record assumptions as assumptions.
- **FDR `alpha` and LFC floor:** pre-registered conventional values, recorded with justification; sensitivity re-run at a second threshold to show robustness.
- **Annotation version:** fixed by compatibility checks (Section 6), then recorded.
- **Shrinkage/filtering settings:** method defaults recorded explicitly, with any deviation justified.

Each calibration writes its inputs, procedure and chosen value to the audit log so a reviewer can reproduce the choice.

---

## 18. Troubleshooting (proposed)

- **PCA separates by batch not condition:** check confounding table; if separable, ensure `batch` is in the formula; if confounded, stop.
- **Dispersion plot pathological / few genes pass filtering:** revisit low-count filtering and library QC; check for failed libraries.
- **Inflated significance / implausibly many hits:** audit for pseudoreplication (libraries counted as units); recollapse technical replicates.
- **No significant genes despite expected effect:** check n vs. calibrated `n_min`, RNA quality, and whether shrinkage/effect floor is too strict; report as underpowered rather than tuning thresholds post hoc.
- **Hash mismatch:** input or environment changed; halt and reconcile before any inference.
- **Model aliasing error:** a factor is collinear with condition (confounding); resolve by design review, not by dropping the diagnostic.

---

## 19. Ordered execution summary (proposed, not executed)

1. Freeze and hash inputs; record environment lock.
2. Build/verify sample sheet; declare experimental units and blocking.
3. Verify hashes; run read QC against calibrated bounds; log exclusions.
4. Quantify against pinned reference/annotation; post-quant QC.
5. Collapse technical subunits to one column per experimental unit.
6. Check confounding tables; select donor/batch branch.
7. Fit NB-GLM with pre-registered formula; estimate size factors and shrunk dispersions.
8. Apply contrast `treatment − control`; shrink LFC; control FDR at pre-registered `alpha`.
9. Regenerate all plots deterministically.
10. Run source-difference audit; emit audit report.
11. Apply acceptance/stopping criteria; scope conclusions to the donor branch.

**Every step above is proposed. No count matrices, sample sheets, versions, or results exist in this packet; all identifiers and numbers are placeholders to be recorded at run time. The plan's inferential claims remain bounded by the independent-treatment-allocation unit and by the donor structure, exactly as the fixed evidence requires.**
