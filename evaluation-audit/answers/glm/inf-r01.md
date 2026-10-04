# GLM 5.3 FlashX / inf-r01

Original final answer, shared by both scoring rounds.

# Recovering True Expression Changes from Noisy RNA-seq Data: A Shrinkage-Based Proposal with a Falsifiable Evaluation Plan

---

## 1. The Unresolved Biological Question

**Biological question (stated as falsifiable):** *When biological replicates are few (n = 2–5 per condition), can a shrinkage estimator that shares information across genes — stabilizing dispersion and log-fold-change (LFC) estimates via a Normal prior on effects — recover the direction and approximate magnitude of real, treatment-induced expression changes better than an unpenalized count-model estimator, without erasing genuinely large effects and without producing confident calls for genes supported only by low counts?*

**Why this question is unresolved:** The supplied evidence packet establishes the *rationale* for shrinkage — that with few biological replicates, low or variable counts yield unstable fold-change estimates, and that a Normal prior on effects plus cross-gene information sharing stabilizes dispersion and LFC estimates. The packet explicitly does **not** supply evidence about the underlying distribution of true biological effects. This matters because shrinkage estimators are only as good as their fit to that distribution:

- If real effects are **sparse** (most genes unchanged, a minority changed) and the true effect distribution is unimodal and concentrated near zero, shrinkage should improve ranking and magnitude estimation.
- If real effects are **polymodal or heavy-tailed** (e.g., a transcription-factor pulse moving hundreds of genes by large amounts), a Normal prior is misspecified and could bias large true effects toward zero — the classic failure mode the proposed evaluation must detect.

**Competing mechanisms generating expression changes (and their distinct predictions):**

| Mechanism | Expected effect distribution | Distinct prediction under shrinkage |
|---|---|---|
| **Sparse, targeted regulation** (e.g., a ligand activating a specific receptor pathway) | Most genes ≈ 0 LFC; a small set of moderate-to-large effects | Shrinkage improves ranking precision; strong effects mostly preserved; false positives from low-count genes reduced |
| **Global transcriptional shift** (e.g., stress response, media change) | Effect distribution shifted; many moderate effects, heavier tails | Shrinkage may compress the upper tail; ranking may still improve but magnitude estimates systematically biased downward |
| **Technical/batch noise masquerading as biology** | Effects concentrated at low-count genes; no coherent biology | Shrinkage should suppress these; the unpenalized estimator should show excess of extreme LFCs among low-count genes |

The evaluation plan below is designed so these mechanisms lead to **distinct, observable outcomes** (Section 6), which is what makes the enterprise falsifiable.

---

## 2. Evidence → Inference → Conclusion Chain

**Evidence (from packet):**
1. The method uses a count model (gene-level expression differences).
2. Few biological replicates make low/variable counts yield unstable fold-change estimates.
3. Stabilization is achieved by sharing information across genes plus a Normal prior on effects.
4. No evidence is supplied about the underlying distribution of biological effects.

**Inferences licensed by that evidence:**
- (E1+E2 → I1) The unsupervised penalty target is variance of LFC estimates driven by low information (low counts, high dispersion, small n).
- (E3 → I2) The method is a form of empirical-Bayes-style moderation: cross-gene information sharing estimates the prior; the Normal prior defines how strongly extreme observed LFCs are pulled toward the prior center.
- (E4 → I3) The *benefit* of the method is conditional on the true effect distribution; this is the central empirical uncertainty and must be tested, not assumed.

**Conclusion (defensible now):** It is *justified to propose* this method as a candidate improvement for small-n differential expression, and *necessary to evaluate* whether it (a) improves recovery of reproducible effects, (b) preserves strong effects, and (c) does not lend false confidence to low-information genes. It is **not** justified to claim it does so in any particular biological dataset until the evaluation in Sections 4–6 is run.

---

## 3. Method Direction (Forecast, Not Result)

**What is being forecast:** A *methods-direction* claim — that a Normal-prior, cross-gene-sharing shrinkage layer on top of a standard negative-binomial count model will, in expectation, improve precision of effect estimates and ranking under small n, with the principal risk being tail compression of genuinely large effects and prior misspecification under polymodal biology.

**What is explicitly not being claimed:** No reproduction of any published biological result is claimed or attempted here. The packet contains no dataset, no counts, no published signature. Everything below is a *protocol* — the experiment has not been run, no results exist, and any language about expected outcomes is conditional.

---

## 4. Proposed Protocol (Detailed)

### 4.1 Dataset eligibility criteria

Use **publicly available, paired-design RNA-seq data** where an independent ground-truth anchor exists. Eligibility requires all of:

1. **Raw reads available** at a public archive (SRA/ENA/GEO with FASTQ files), not only normalized matrices — this is non-negotiable because raw-read provenance (below) is part of the falsification chain.
2. **≥ 2 biological replicates per condition** (to exercise the small-n regime the method targets) **and ≥ 6 replicates per condition for at least one public dataset** of the same biological system, so a high-n version of the same contrast can serve as a quasi-reference.
3. **A declared, mechanistically interpretable contrast** (e.g., drug-treated vs. vehicle; knockout vs. wild-type) with a known target pathway, enabling an external sanity anchor.
4. **Controlled confounders reported**: batch, sex, age, sequencing lane, library prep, or explicit acknowledgment that they are unmodeled.
5. **Two contrast classes**: (a) a sparse-regulation contrast and (b) a global-shift contrast (Section 1), if available; if only one class exists, state that the evaluation covers one mechanism only.

**Candidate archetypes (to be confirmed against actual archive metadata before use; not asserted to exist as described):** bulk RNA-seq of a cell line with drug/time-course perturbation where a companion high-replicate study or independent qPCR/proteomics validation exists.

### 4.2 Raw-read provenance

For every dataset, record before any analysis:

- Archive accession, run accessions, sequencing platform, read length, single/paired-end, strandedness.
- Contributor, organism, strain, tissue/cell line, passage, treatment, time, dose.
- Batch variables as declared in metadata; **do not impute** undeclared batches.
- MD5/SHA checksums of downloaded FASTQs.
- Version numbers of every tool and every reference (genome build, annotation release, transcriptome index).

### 4.3 Preprocessing (fixed in advance, applied identically to all methods)

- QC with a standard tool (e.g., FastQC/MultiQC); adapter and quality trimming only if indicated by QC; document parameters.
- Alignment or quasi-mapping to a single, pinned reference (e.g., STAR to a named genome build, or Salmon to a pinned transcriptome); document index and parameters.
- Gene-level quantification against a single annotation release; summarize to gene counts.
- Filter: retain genes with a minimum cumulative count (e.g., ≥ 10 counts across all samples — this threshold is an **assumption** to be declared and, ideally, sensitivity-tested at 0×, 1×, and 10× this level).
- Sample-level QC: PCA / sample-distance clustering; outliers removed only by a pre-registered rule (e.g., PCA distance > X with a documented technical cause); never remove outliers *after* seeing DE results.

### 4.4 Estimation — the method under test and its comparators

For each dataset, run the following estimators on the *identical* count matrix:

- **M1 (method under test):** the packet's count model with cross-gene dispersion shrinkage and a Normal prior on LFCs; report shrunken LFCs, standard errors, and unshrunken LFCs for later tail-preservation analysis.
- **M2 (unpenalized comparator):** the same count model with the shrinkage layer disabled (MLE LFCs), the natural ablation isolating the prior's contribution.
- **M3 (optional external benchmark, if reproducibly runnable):** a different shrinkage family (e.g., a mixture/adaptive-shrinkage approach) to test whether *any* reasonable shrinkage beats M2 or whether benefits are specific to the Normal prior.

**Small-n protocol:** subsample replicates from high-n datasets down to n = 2, 3, 5 per condition (all subsamples, or a pre-registered random sample of ≥ 20 subsamples per n), estimate effects, and compare against the full-n estimate treated as a reference. This is the core "recoverability" test.

### 4.5 Simulation layer (mechanism-level falsification)

Because real data lack true effect sizes, simulate count data with known parameters, calibrated to the observed data (fit dispersion–mean trend and effect distribution from each real dataset, then resample):

- **S1 — Sparse mechanism:** 5% of genes truly DE, effect magnitudes drawn from a distribution centered at |LFC| ≈ 1–2.
- **S2 — Heavy-tail mechanism:** same sparsity but with 10% of DE genes at |LFC| > 4 (deliberately testing Normal-prior misspecification).
- **S3 — Null mechanism:** 0% truly DE (calibrates false-positive behavior).
- **S4 — Low-count trap:** a stratum of genes with mean counts of 0–10, half truly DE, to test whether the method avoids confident calls on low-information genes.

For each simulation cell, sweep n ∈ {2, 3, 5} and vary the Normal prior width around its data-driven estimate (± 2×, ×0.5) to measure **prior sensitivity** — a declared robustness check, since the packet does not establish the true effect distribution.

### 4.6 Independent validation layer

- **Held-out replicates:** where n ≥ 4 per condition, estimate on a 2-vs-2 subsample and test recovery of the full-data calls (Section 5 criteria).
- **Orthogonal platform (if available in the chosen public resources):** compare estimated LFCs to qPCR fold-changes or matched proteomics log-ratios for a gene set spanning the effect-size range, not just top hits. Pre-register the correlation analysis across effect-size bins — the upper bins are where tail preservation is tested.
- **Cross-study replication:** the same biological contrast in an independent study; compare effect estimates (M1 vs. M2) by concordance and calibration, not by nominal significance overlap alone.

### 4.7 Figure generation plan (pre-specified)

1. **Fig 1 — Effect recovery vs. n:** scatter of estimated vs. reference LFC at n = 2, 3, 5, M1 vs. M2; annotate RMSE and rank correlation (all genes and DE-genes-only strata).
2. **Fig 2 — Tail preservation:** binned scatter of unshrunken vs. shrunken LFC restricted to genes with reference |LFC| > 2 and adequate counts; overlays of the shrinkage compression curve; quantified as median |shrunken − reference| per bin.
3. **Fig 3 — Low-information audit:** LFC shrinkage vs. base mean; highlight genes with tiny counts that receive large shrunken LFCs or large standard errors; this is where "confident calls on unstable extremes" would appear.
4. **Fig 4 — Simulation truth:** ROC/PRC per mechanism (S1–S4) and n; effect-magnitude bias by true |LFC| bin.
5. **Fig 5 — Validation:** M1 vs. M2 against qPCR/proteomics and cross-study estimates, stratified by effect size.
6. All figures: pinned code, pinned package versions, seeds recorded; every panel regenerable from a single script.

### 4.8 Interpretation rules

Interpretation proceeds only after the criteria in Section 5 are applied mechanically; the analyst does not get to reclassify ambiguous outcomes as positive. Any deviation from the protocol (e.g., a changed filter threshold) must be reported as a sensitivity analysis, not silently adopted.

---

## 5. Testing Preservation of Strong Effects Without Accepting Unstable Extremes

This is the crux, so it gets explicit, falsifiable criteria. The tension: shrinkage *should* dampen noise-driven extremes (which occur overwhelmingly at low counts), but *should not* erase true large effects (which occur at adequate counts). The discriminator is **information per gene**, not effect size alone.

**Decompose all calls into two strata:**

- **A. High-information strong effects:** reference |LFC| > 2 (or top-decile unshrunken |LFC|) **and** base mean above the pre-registered filter **and** estimated dispersion not in the top decile. Criterion: M1 must retain ≥ 80% of the sign and ≥ 70% of the magnitude relative to the reference (numbers pre-registered as thresholds; any reasonable pre-registered threshold serves — the point is that the criterion is fixed before looking).
- **B. Low-information extremes:** extreme unshrunken |LFC| arising from base mean below the filter threshold or top-decile dispersion. Criterion: M1 should *not* assign these confident calls; shrunken LFCs should contract toward zero and/or standard errors should remain large enough that these genes fall below the significance threshold.

**Combined success condition (both required):**

1. Stratum A preservation meets the thresholds above in both simulation S1/S2 and real small-n recovery against full-n references; *and*
2. Stratum B: the false-signature rate (fraction of low-information genes called DE in simulation S3) is no worse than M2, and materially better if M2 shows inflation.

**Failure modes, named in advance:**

- **Tail amputation:** Stratum A magnitude falls below threshold in S2 (heavy-tail simulation) → Normal prior too narrow / misspecified; the honest conclusion is that the method biases large true effects under heavy-tailed biology.
- **False confidence at the bottom:** Stratum B genes still called DE with large shrunken LFCs at tiny counts → shrinkage of the point estimate is insufficient without proper variance inflation; method overstates certainty exactly where it should not.
- **No benefit anywhere:** M1 ≈ M2 across all cells → the packet's rationale does not translate into recoverable gains at the tested n; report as a genuinely negative methods result.

---

## 6. Conditional Conclusions (Pre-Declared)

**Positive (conditional):** *If* M1 meets both criteria in Section 5 across S1–S4 and the real small-n recovery, *and* improves rank correlation with full-n references and with orthogonal validation, *then* the supported conclusion is: under effect distributions resembling those tested, the Normal-prior shrinkage layer improves recovery of real expression changes at small n, preserving strong effects while suppressing low-count artifacts. This conclusion is bounded to the tested organisms, tissues, effect distributions, and n values.

**Negative (conditional):** *If* Stratum A magnitude loss exceeds thresholds in S2, or M1 shows no gain over M2 at any n, *then* the supported conclusion is that the Normal prior is misfit to the relevant effect distribution or the gains claimed in principle do not materialize operationally; recommend prior recalibration (e.g., heavier-tailed or mixture prior) rather than abandonment of shrinkage per se, and state that the packet's rationale alone does not guarantee practice.

**Ambiguous (conditional):** *If* M1 improves ranking but fails one tail criterion, or results hold in the sparse mechanism but not the global-shift mechanism, *then* the supported conclusion is mechanism-dependence: the method is beneficial for targeted-regulation biology and risky for global-shift biology; recommendations must be scoped by contrast type. Distinguish this from noise by requiring the discrepancy to replicate across ≥ 2 datasets and ≥ 20 subsamples; a single-dataset discrepancy is treated as unresolved, not resolved negatively.

---

## 7. Alternatives Considered and Their Limits

- **No shrinkage (M2 alone):** unbiased for large effects when the model is correct but unstable at small n and low counts; the packet's stated motivation argues against relying on it alone, and the evaluation will quantify exactly how much instability costs.
- **Different prior families:** heavier-tailed or adaptive/mixture priors could fix tail amputation but may under-shrink noise at low counts; M3 tests the "any shrinkage vs. this shrinkage" question. The packet supplies no evidence comparing prior families; this is an explicitly unresolved parameter.
- **Filtering or count-flooring without shrinkage:** suppresses low-count artifacts but discards genuine low-abundance regulation and does nothing about small-n dispersion instability; could be added as an ablation but is not a substitute.
- **Independent-filtering on variance plus adjusted p-value ranking alone:** shifts the problem from effect estimation to call ranking; the evaluation's effect-recovery metrics (magnitude, not just significance) would still find it insufficient.

**Limits of the whole plan:** (1) Simulations are calibrated to real data but inherit the calibration model's assumptions, including the effect distribution — a simulation cannot fully rescue the missing knowledge flagged in the packet. (2) Full-n references are estimates, not truths; cross-study and orthogonal-platform validation partially mitigates this. (3) If only a sparse-mechanism public dataset is available, conclusions are scoped to that mechanism. (4) All thresholds (80%/70%, filter levels, subsample counts) are proposed conventions that should be pre-registered before data are examined; changing them post hoc converts a confirmatory evaluation into an exploratory one.

---

## 8. Methods Forecast vs. Biological Reproduction — Final Distinction

- **Forecast (what this document makes):** a *methods-direction* prediction — that the packet's shrinkage estimator will show the recovery improvements defined in Section 5, with named failure modes and pre-declared conditional conclusions. Nothing has been run; no numbers exist.
- **Reproduction (what this document does not do):** re-deriving any published biological result — a known signature, a published DE gene list, a reported fold-change. The evidence packet contains no published dataset or result; inventing one would be fabrication. Should the protocol in Section 4 be executed on a real contrast and independently replicate a published signature, that would constitute a *separate* biological claim requiring its own evidence, and it would validate the biological system rather than the estimator per se. The two claims — "the estimator recovers effects under conditions X" and "biology Y responds via mechanism Z" — require different evidence and must not be conflated.
