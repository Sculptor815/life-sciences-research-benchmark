# Claude Fable 5 / inf-d02

Original final answer, shared by both scoring rounds.

# Proposed, Audit-Ready Bulk RNA-seq Differential-Expression Plan (Design Only — Nothing Executed)

**Status declaration (applies to every section below):** All experiments, analyses, file paths, versions, thresholds and numeric settings in this document are **proposed placeholders to be recorded at execution time**. No files, count matrices, sample sheets or reference versions were supplied, so **no analysis has been run and no results exist or are claimed**. The plan is written so that, once populated, every step can be audited from immutable artefacts with no hidden state.

---

## 1. Lead recommendation

Adopt a design in which (a) the **experimental unit is the independent treatment allocation** (the smallest entity independently randomised to treatment or control), (b) all inputs are **content-addressed and frozen before model fitting**, (c) the count model is a **DESeq2-style negative-binomial GLM with shared dispersion estimation**, with a single pre-registered contrast and Benjamini–Hochberg FDR, and (d) every figure and table is **regenerated from code plus frozen inputs**, with a scripted **source-difference audit** comparing any externally supplied summaries against the pipeline's own outputs. If the study ends up with a **single donor**, the plan must explicitly scope all inference to that donor: adding a donor random effect cannot manufacture across-donor replication, and treating wells as replicates when allocation occurred at a coarser level (e.g., per flask or per donor-treatment) would be pseudoreplication.

---

## 2. Evidence → inference → conclusion chain

**Evidence (from the supplied packet only):**

1. The DESeq2 record describes negative-binomial GLMs with information sharing (shrinkage) for dispersion and effect-size estimation, plus inference and diagnostics.
2. The record states that **modelling does not create missing independent treatment replication**.
3. The experimental unit **depends on independent treatment allocation**; donor-level and well-level inference are **distinct inferential targets**; a **single donor cannot identify across-donor heterogeneity** merely by adding a donor random effect.
4. The read record is **partial**: no count matrices, sample sheets or file versions are supplied.

**Inferences:**

- From (1): a NB GLM with moderated dispersion is an appropriate default count model for bulk RNA-seq with modest replication; its validity still depends on the design matrix reflecting the true allocation structure.
- From (2) and (3): the design document — not the statistical software — must fix the experimental unit. If treatment was allocated per donor-culture, wells within that culture are **technical/subsampling replicates** and must be collapsed (e.g., summed counts per allocation unit) or modelled as nested, never counted as independent n.
- From (3): with one donor, the population of inference is that donor; the plan must either recruit ≥2 donors with treatment allocated independently within each, or pre-register the single-donor scope limitation.
- From (4): because no files exist, the deliverable can only be a **protocol with placeholders and calibration procedures**, and must say so. Any claim of executed results would be fabrication.

**Conclusion:** Deliver the protocol below, with immutability, unit-of-analysis, and audit mechanisms specified in advance, and with every unknown parameter paired with a calibration procedure rather than an invented value.

---

## 3. Operational protocol (proposed; ordered)

### Step 0 — Pre-registration and repository scaffold (before any data arrive)

- Create a version-controlled repository (placeholder: `repo@tag v0.1-design`) containing: this protocol, an empty `inputs/` manifest, analysis scripts, an environment lockfile, and a `CHANGELOG`.
- Pre-register: the experimental unit definition, the design formula, the single primary contrast, the FDR threshold, and acceptance/stopping criteria (Sections 3.2–3.9). Record the pre-registration hash/date.
- **Environment capture:** pin the full software stack (container image digest, e.g., `sha256:<placeholder>`; R/Bioconductor or equivalent versions; DESeq2 version; aligner/quantifier version; all set as placeholders to be filled and hashed at execution). The environment lockfile is itself an immutable input.

### Step 1 — Immutable inputs and manifest

At execution time (not now), record in `inputs/MANIFEST.tsv`:

| Field | Placeholder |
|---|---|
| Raw FASTQ files | per-file SHA-256, size, run/lane IDs |
| Reference genome | source, assembly name, release number, file checksum |
| Annotation (GTF/GFF) | source, release number, checksum; must be version-matched to the genome |
| Index files | builder version, build command, checksum |
| Sample sheet | checksum; see Step 2 |
| Environment lockfile / container digest | checksum |
| Random seeds | all seeds recorded explicitly |

Rules: inputs are written once to a read-only location; any change requires a new manifest entry and a new analysis tag. No analysis script may read a file absent from the manifest ("no hidden state" rule). Checksums are re-verified by the pipeline at startup and the verification log is retained.

### Step 2 — Sample sheet schema (the unit-of-analysis ledger)

One row per **sequenced library**, with explicit columns linking each library to its allocation unit:

- `library_id`, `fastq_files`
- `allocation_unit_id` — the independent treatment allocation (the experimental unit)
- `donor_id`, `well_id`, `passage`, `harvest_date`
- `treatment` (treatment/control), `dose` (placeholder), `allocation_timestamp`, `randomisation_block`
- `processing_batch` (RNA extraction batch, library-prep batch, sequencing run/lane)
- `blinding_code` (sample labels used during processing)

Critical rule, derived directly from the evidence packet: **n for inference = number of distinct `allocation_unit_id` values per arm**, not number of libraries or wells. If multiple wells share one allocation (e.g., treatment applied to a flask then split), those wells share one `allocation_unit_id` and will be collapsed (counts summed) before model fitting, or modelled as nested technical replicates — never as independent replicates.

### Step 3 — Independent units, allocation and blinding (proposed experimental design)

- **Target design (preferred):** ≥2 donors (placeholder: 3–6, to be set by the power calibration in Section 5), with treatment vs control **allocated independently to separate cultures within each donor**, so each donor contributes independent allocation units to both arms. This makes donor a blocking factor and permits across-donor generalisation.
- **Fallback (single donor available):** pre-register that inference is **within-donor only**. Do not add a donor random effect and claim donor-generalisable results — per the evidence packet, a single donor cannot identify across-donor heterogeneity.
- **Randomisation:** allocate units to arms with a seeded random sequence (seed recorded in the manifest); block by donor and by planned processing batch.
- **Confound avoidance:** ensure `treatment` is not aliased with `processing_batch` — distribute both arms across every extraction batch, library-prep batch and sequencing lane. Record the allocation table before processing begins.
- **Blinding:** relabel samples with `blinding_code` before RNA extraction; the key is stored separately and merged only at the statistical-analysis step. Bench and sequencing staff remain blinded.

### Step 4 — Intervention and sampling (placeholders)

- Intervention: treatment vs vehicle control; dose, duration and medium are placeholders to be recorded with timestamps per allocation unit.
- Sampling: harvest all units within a pre-specified time window; record exact harvest time per unit (circadian/handling-time drift is a known nuisance); snap-freeze or stabilise per a fixed SOP; record RIN or equivalent RNA-quality metric per sample.

### Step 5 — Measurements and quantification

- Sequencing: platform, read length, strandedness, target depth are placeholders; **depth calibration** in Section 5.
- Quantification: aligner/pseudo-aligner version and exact command lines recorded; gene-level counts generated against the pinned genome+annotation pair from Step 1. The counting command, parameters and tool version are part of the manifest.
- QC gates (thresholds are placeholders with calibration in Section 5): per-sample read totals, mapping/assignment rate, rRNA fraction, gene-body coverage, duplication; sample-identity checks (sex-marker or SNP concordance with `donor_id`); PCA/distance heatmap on transformed counts to flag outliers and batch structure. All QC outputs written to `qc/` and hashed.
- **Outlier policy pre-registered:** samples may be excluded only on QC grounds defined before unblinding (e.g., identity mismatch, assignment rate below the calibrated floor), with every exclusion logged with reason and hash of the pre/post sample sheets.

### Step 6 — Count model, design formula, contrast and FDR

- **Model:** DESeq2-style NB GLM, consistent with the supplied record: per-gene NB likelihood, median-of-ratios size factors, dispersion estimation with information sharing (shrinkage toward the mean–dispersion trend), Wald test for the primary contrast; effect sizes reported with shrinkage for ranking/visualisation and unshrunk estimates retained in the full table.
- **Design formula (multi-donor case):** `~ donor + batch + treatment` with donor as a fixed blocking factor at the allocation-unit level (after technical-replicate collapsing). If `batch` is confounded with `donor`, drop the redundant term and document the aliasing check.
- **Design formula (single-donor case):** `~ batch + treatment`, with the pre-registered scope statement that results apply to this donor only. **Do not** use a donor random effect to simulate replication — the evidence packet is explicit that this cannot identify across-donor heterogeneity.
- **Primary contrast (single, pre-registered):** treatment vs control log2 fold change. Any additional contrasts are labelled exploratory.
- **Multiplicity:** Benjamini–Hochberg FDR at a pre-registered threshold (placeholder 0.05); independent filtering / low-count handling done by the documented default of the pinned software version, with the filtering threshold recorded in the output log. If a minimum-effect criterion is desired, pre-register a fold-change null (e.g., |LFC| > placeholder threshold tested directly, not post-hoc filtering), because post-hoc fold-change cutoffs invalidate FDR control.
- **Reported outputs:** full per-gene table (baseMean, LFC, SE, statistic, p, adjusted p), written as a hashed artefact; no gene list is reported without its generating command.

### Step 7 — Plot regeneration (no hand-made figures)

- Every figure (MA plot, PCA, dispersion fit, p-value histogram, heatmaps, volcano) is produced by a script in `figures/` that reads **only** manifest-listed inputs and the pipeline's own result tables.
- A single orchestration command (placeholder: `make all` or a workflow-manager run) regenerates all tables and figures end-to-end from raw inputs; the run log, seeds and output checksums are archived.
- **Reproducibility check:** two independent executions (same container, same seeds, ideally different machines) must yield byte-identical or numerically-tolerance-identical outputs (tolerance pre-specified for any nondeterministic steps, e.g., multithreaded quantification). Discrepancies trigger Section 7 troubleshooting.

### Step 8 — Source-difference audit

Purpose: detect divergence between what the pipeline produces and any externally supplied numbers (collaborator spreadsheets, prior reports, manuscript drafts).

- Script `audit/source_diff.(R|py)` ingests (i) pipeline outputs and (ii) any external summary, and reports: row/column count mismatches, gene-ID set differences, checksum comparison of claimed-identical files, numeric deltas on shared fields (LFC, adjusted p) with a pre-set tolerance, and annotation-version mismatches (gene IDs present in one annotation release but not the other).
- The audit also compares the **manifest-recorded** genome/annotation/software versions against any versions claimed in external documents.
- Output: a signed, hashed audit report. Rule: **no external figure or table may be cited as equivalent to pipeline output unless the audit report shows agreement within tolerance.**
- Because the current evidence record is explicitly partial, the audit's first run must flag that no external sources exist yet; this is recorded, not assumed resolved.

### Step 9 — Acceptance and stopping criteria (pre-registered placeholders)

Proceed to interpretation only if **all** hold:

1. Manifest verification passes (all checksums match).
2. Each arm contains ≥ the calibrated minimum number of **independent allocation units** (placeholder floor: 3 per arm in the multi-donor design; calibration in Section 5).
3. No treatment–batch aliasing in the realised design matrix (rank check logged).
4. QC gates passed or exclusions documented per the pre-registered policy.
5. P-value histogram and dispersion-fit diagnostics show no gross model misfit (criteria below).
6. Reproducibility check (Step 7) passes.
7. Source-difference audit shows no unresolved discrepancies.

**Stopping rules:** stop and redesign (do not analyse for inference) if treatment is fully confounded with batch or donor, if fewer than the floor of independent units survives QC in either arm, or if sample-identity checks reveal label swaps that cannot be resolved from primary records.

### Step 10 — Troubleshooting map

| Symptom | Likely cause | Pre-registered response |
|---|---|---|
| Treatment aliased with batch | Allocation error | Stop; no causal DE inference; report as design failure |
| p-value histogram with inflation near 0 **and** structure elsewhere (e.g., hill shape) | Unmodelled variation / batch | Add recorded batch covariate or estimate latent factors (e.g., surrogate-variable approach), pre-registering the number of factors via the calibration in Section 5; label as sensitivity analysis |
| Severe outlier sample on PCA + failing QC | Technical failure | Exclude per policy, log, rerun full pipeline from manifest |
| Non-identical reruns | Nondeterminism/thread race | Pin threads/seeds; if persistent, record tolerance band and investigate the offending step |
| External table disagrees in audit | Different annotation/software version or manual edits | Re-map IDs across annotation versions; if still discrepant, treat external source as non-equivalent and say so |
| Wells mistaken for units | Sample-sheet error | Re-collapse by `allocation_unit_id`; refit; document correction in CHANGELOG |

---

## 4. Alternatives and limits

- **Alternative count frameworks:** quasi-likelihood NB pipelines (edgeR-QL) or precision-weighted linear models (limma-voom) are defensible substitutes; voom's weighting is attractive when library sizes vary widely, and QL tests can be more conservative with small n. The choice must be pinned **before** data arrive; switching after seeing results is prohibited. None of these changes the experimental-unit logic — the evidence packet's point that modelling cannot create missing replication applies to all of them.
- **Random-effects / duplicate-correlation approaches:** useful when multiple libraries per allocation unit must be retained rather than summed, but — per the evidence — they adjust within-donor correlation; they do **not** convert a single-donor study into a donor-generalisable one.
- **Limits of this plan:** (i) with the minimal-replication floor (e.g., 3 units/arm), dispersion shrinkage is doing heavy lifting and power for small effects is low; (ii) FDR control is over genes within the single pre-registered contrast, not over exploratory analyses; (iii) the source-difference audit can detect divergence, not adjudicate which source is correct without primary records; (iv) single-donor results carry no claim about donor-to-donor effect variability — this is a hard identifiability limit, not a software setting.
- **What would change the recommendation:** if supplied files later reveal that allocation actually occurred at a different level (e.g., per sequencing run), the unit definition, design formula and n must be redefined accordingly before any fitting; if donors ≥2 with within-donor allocation are confirmed, the fixed-donor blocking design in Step 6 stands; if arms are confounded with batch, the plan mandates stopping, not statistical rescue.

---

## 5. Calibration procedures for unknown parameters (no invented values)

Because no data or author methods exist, each placeholder gets a **procedure**, not a number:

1. **Replicates per arm / number of donors:** simulation-based power calibration — simulate NB counts over a grid of (n units/arm, dispersion, LFC) using dispersion–mean trends estimated from a pilot or a comparable public dataset recorded in the manifest; choose the smallest n achieving pre-registered power (placeholder target: 0.8) at the chosen FDR for the minimum effect of interest, which itself must be set from biological reasoning documented in the pre-registration.
2. **Sequencing depth:** saturation analysis on pilot libraries (subsample reads, track detected genes and DE power proxy); set depth at the plateau knee.
3. **QC thresholds (mapping rate, assignment rate, rRNA fraction):** set empirically as robust lower bounds from the pilot batch distribution (e.g., median − k·MAD with k pre-registered), not from literature defaults asserted as authoritative.
4. **Low-count filter:** use the pinned software's automatic independent-filtering optimisation; log the realised threshold rather than hand-picking one.
5. **LFC threshold for a minimum-effect test (if used):** elicited from the biological question before unblinding; document the elicitation.
6. **Numeric reproducibility tolerance:** derived from repeated pilot runs of the pinned container; set tolerance just above observed nondeterministic jitter.
7. **Number of latent factors (if surrogate-variable rescue is triggered):** choose by a pre-specified estimator (e.g., permutation-based parallel analysis) on the pilot or realised data, recorded before DE refitting.

---

## 6. Closing statement

Everything above is a **proposed** protocol. No data were supplied, no pipeline was run, and no results, figures or gene lists exist. The design's integrity rests on three commitments drawn directly from the evidence packet: the experimental unit is fixed by independent treatment allocation and cannot be repaired by modelling; a single donor bounds the inferential scope regardless of random-effect specification; and because the record is partial, every input must be made immutable and every external claim must pass the source-difference audit before it is treated as part of the study's evidentiary base.
