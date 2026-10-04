# GLM 5.3 FlashX / inf-r02

Original final answer, shared by both scoring rounds.

# Proposed Next Question and Research Plan: Separating Genuine Post‑Transcriptional Cell States from Measurement Artifacts in Joint RNA–Protein Single‑Cell Data

---

## 1. Lead conclusion (the recommended next question)

**The most valuable next biological question is:** *Do the RNA–protein discordances observable in joint oligonucleotide-tagged-antibody single-cell measurements reflect genuine, reproducible, functionally coherent post-transcriptional cell states — or are they dominated by the differing noise and detection properties of the two modalities?* Phrased operationally: for each measured gene/epitope pair, is the cell-to-cell residual disagreement between transcript abundance and surface-protein abundance (after correcting each modality's known error structure) reproducible across independent biological units, structured across cells, and confirmable by an orthogonal protein assay — or does it track technical covariates and fail to replicate?

This question is the highest-value next step because, per the supplied packet, joint measurement is already established but (a) no optimal integrated representation is specified and (b) it is explicitly unresolved whether apparent RNA–protein disagreements define real cell states. Every downstream integration decision — whether to average modalities, privilege one, or model discordance as signal — depends on this answer. Resolving it converts an ambiguous dataset property into a decision rule for representation design.

**Status labeling used throughout:** everything in the "Fixed result" category below was reported; every protocol element, threshold, and expected result below is a *proposal* and has not been observed or performed.

---

## 2. Evidence, inference, and conclusion chain

**Evidence (reported, packet only):**
- E1. Oligonucleotide-tagged antibodies permit selected surface-protein measurements and transcript measurements to be linked to the same single cells.
- E2. The two measurement types are complementary and have *different noise and detection properties*.
- E3. Joint measurement is established (the supplied result).
- E4. The packet does not specify an optimal integrated representation of the two modalities.
- E5. The packet does not establish that apparent RNA–protein disagreements define real cell states.

**Inference (mine, from E1–E5):**
- I1. Because detection properties differ (E2), a raw observed difference between RNA and protein levels for the same gene is a *mixture* of biological signal and modality-specific error; it cannot be interpreted as biology without an explicit error model.
- I2. Because integration strategy is unspecified (E4), the field-relevant deliverable is a decision rule: under what conditions should discordance be treated as signal (state) versus noise (artifact) in an integrated representation.
- I3. Because state-defining status is unestablished (E5), the discriminating test must include reproducibility across independent biological units, independence from technical covariates, perturbation responsiveness, and orthogonal confirmation — no single test suffices.

**Conclusion (proposed, conditional on the study below):** the answer to the lead question will determine the integrated representation: if discordances are largely artifact, integration should denoise (shared-latent-factor shrinkage); if a reproducible subset exists, integration must additionally preserve a discordance axis as a bona fide state variable. The study is designed so that any of these outcomes yields a defensible representation recommendation.

---

## 3. Competing mechanisms and discriminating predictions

### Mechanism A — Genuine post-transcriptional regulation (biological discordance)
Differences arise from regulated translation, differential protein half-life, secretion or shedding of surface proteins, or epitope exposure changes — processes that decouple protein abundance from mRNA while leaving RNA measurements intact.

*Predictions:*
- A1. Discordance (standardized RNA–protein residual) replicates across independent donors/samples and across independent library preparations of the same cells.
- A2. Discordance is **gene-specific and direction-consistent**: the same genes are discordant in the same direction across units; it is not diffuse genome/panel-wide.
- A3. Discordant cells form coherent subpopulations that differ in other transcripts and respond in a coordinated way to perturbations expected to act post-transcriptionally (rapid protein change without transcript change).
- A4. Orthogonal protein assays (flow cytometry on matched aliquots; imaging) confirm the protein side of the discordance.

### Mechanism B — Modality-specific technical artifact
Differences arise from the differing noise/detection properties (E2): antibody non-specific binding, ambient/free antibody-oligo carryover, protein-tag dropout or saturation, differing dynamic range and count statistics between UMI-based RNA and antibody-derived tag counts.

*Predictions:*
- B1. Discordance does not replicate across independent units or replicate libraries, or replicates only as a batch effect.
- B2. Discordance correlates with technical covariates: total antibody-derived counts, background level in negative-control features, sequencing depth, antibody lot/batch, cell size/auto-fluorescence proxies.
- B3. Discordance magnitude falls when measurement quality improves (higher antibody specificity, better washing, calibrated titration), without changing the cells.
- B4. Orthogonal assays fail to confirm the protein signal implied by the antibody tag.

### Mechanism C — Sampling/identity artifacts masquerading as discordance
Doublets (two cells sharing one barcode) and ambient RNA/oligo admixture.

*Predictions:*
- C1. Discordant cells show doublet signatures (co-expression of mutually exclusive markers, elevated total content).
- C2. Discordant cells show ambient-signature enrichment; discordance diminishes after ambient-correction and doublet removal.

**Discriminating logic:** A predicts reproducible, structured, perturbation-responsive, orthogonally confirmed discordance; B predicts instability and technical covariate association; C predicts marker-based artifact signatures. The three are separable by the factorial design below.

---

## 4. Proposed research plan (ordered, auditable)

> All of Section 4 is a proposal. No step has been performed; no result below has been observed.

### Phase 0 — Prerequisites and calibration (pilot; no biological claim)

**0.1 Reagent inventory and documentation.** List every antibody-tag conjugate, lot, clone, target epitope, and fluorochrome-conjugated twin (for orthogonal validation). Record which surface proteins have paired RNA targets in the measurement panel. *Prerequisite:* unconjugated and oligo-conjugated versions of each antibody clone available or synthesizable.

**0.2 Antibody titration.** For each antibody-tag, titrate on a positive/negative cell mixture (two cell lines known — by prior fluorochrome cytometry, not assumed from the packet — to be positive and negative for the epitope). Select the concentration at the plateau of positive separation before background rise. *Auditable output:* titration curves per antibody; chosen concentration.

**0.3 Spike-in and background standards.** Introduce (i) synthetic oligonucleotide spike-ins at known concentrations for antibody-tag sequencing; (ii) a fixed proportion of a reference cell type with stable, previously characterized protein levels per feature. *Calibration targets (pre-registered):* per-feature background rate in negative cells; per-feature dynamic range; limit of detection per tag.

**0.4 Noise-model construction.** Using pilot data only, fit per-modality noise models: for RNA, a count model capturing dropout and mean–dispersion; for protein tags, a background-plus-saturation model calibrated against negative/positive standards. This model defines the *technical expectation* against which discordance is later tested. **Stop rule (Phase 0):** abort and troubleshoot if >20% of antibodies fail to separate positive from negative cells at any concentration, or if spike-in recovery deviates from nominal by more than a pre-set factor, or if reference-cell protein measurements vary more across replicate wells than across antibody lots (indicating dominant handling noise).

**Troubleshooting 0:** non-specific binding → add blocking reagent, switch tag barcode, test an alternate clone; high ambient oligo → additional post-stain washes, carrier oligo competition; low RNA complexity → assess cell viability and capture efficiency before proceeding.

### Phase 1 — Primary observational study: does discordance replicate and is it structured?

**1.1 Independent units and design.** *Independent unit = biological donor/sample*, not cell. Proposal: ≥6 independent units (e.g., donors), each split into two matched aliquots processed as **separate library preparations on different days** (technical-replicate stratum). Cells from different units are randomized across processing batches and sequencing lanes so that unit is not confounded with batch. *Allocation:* randomization performed by a third party using a pre-registered scheme; sample identifiers coded.

**1.2 Blinding.** Analysts performing discordance quantification are blinded to unit identity and batch assignment until the primary reproducibility statistic is locked.

**1.3 Controls per batch.** (a) Negative-stain control (no antibody tags) to quantify ambient/background per feature; (b) single-fluorophore-analog "missing tag" controls (all tags except one) per panel to quantify spillover of tag barcodes; (c) the reference-cell spike-in from 0.3 in each batch; (d) isotype-control tags for a subset of antibodies to estimate non-specific binding.

**1.4 Measurements.** Per cell: transcript count vector (selected genes incl. all genes whose proteins are tagged), antibody-tag counts for all panel features, QC metrics (total counts per modality, mitochondrial fraction, doublet scores from both modalities).

**1.5 Pre-specified analysis.**
1. QC: remove low-quality cells by modality-specific pre-registered thresholds; detect doublets by combined-modality criteria.
2. Normalize each modality with its calibrated noise model (Phase 0).
3. Compute per cell and per feature a **discordance statistic**: the residual of protein-tag level regressed on RNA level, standardized by the pooled technical variance from the noise model and replicate aliquots (so "discordant" means exceeding what replicate variability explains).
4. **Primary test of Mechanism A vs B:** intraclass correlation of per-feature discordance across the two independent library preparations within each unit, and across units. Pre-registered success criterion for genuine signal: per-feature discordance ICC exceeding a threshold set from the pilot noise model (proposal: ICC > 0.4 across preparations), with gene-level consistency of direction across ≥5 of 6 units.
5. **Test of Mechanism B:** regression of discordance on technical covariates (batch, tag background, total antibody counts, sequencing depth). A genuine biological discordance should be substantially unexplained by these after correction.
6. **Test of Mechanism C:** re-run analyses after ambient correction and doublet removal; report how much discordance survives.
7. Secondary: clustering on the discordance residual matrix alone — do discordant cells form coherent groups that are also coherent in transcript space (supporting A3)?

**Stop rules (Phase 1):** halt if replicate-aliquot concordance of the *raw* measurements is below the noise model's expectation for either modality (measurement instability invalidates all downstream inference); halt if >50% of high-discrepancy cells are classified as doublets or ambient-driven (mechanism C dominates; redirect to sample handling).

**Troubleshooting 1:** batch-driven discordance → rebalance design, add a second randomization round; discordance confined to low-count cells → add a detection-sensitivity covariate to the noise model; saturation-driven artifacts → re-titrate and repeat the affected antibody.

### Phase 2 — Perturbation discrimination (does discordance behave like biology?)

**2.1 Design.** Using the same unit structure (≥4 independent units), expose matched aliquots to a candidate stimulus proposed — on biological grounds to be validated in Phase 2a pilot — to alter a panel protein *post-transcriptionally* (rapid protein-level change with minimal expected transcript change), alongside vehicle controls. Processing randomized; condition labels coded; analysts blinded. Time points chosen to bracket the expected protein-response window, with an early time point where transcript change should still be absent if the mechanism is genuinely post-transcriptional.

**2.2 Predictions.** Mechanism A: perturbation shifts the discordance residual of the targeted feature in the expected direction, at the protein measurement, without a parallel RNA shift, reproducibly across units; the perturbation response *depends on* baseline discordance state (cells already discordant respond differently), implying the discordant state is functional. Mechanism B: perturbation produces no structured residual shift, or shifts RNA and protein equally (technical gain change), or the shift fails to replicate.

**2.3 Controls.** Vehicle controls per unit; unstained/background controls; the same batch-level controls as 1.3; a non-targeting feature as a negative-control readout.

**2.4 Stop rule.** If the pilot (2a) shows the chosen stimulus alters both modalities or neither, select a different candidate stimulus or proceed only with the observational criteria; do not interpret a null perturbation as evidence against Mechanism A without confirming stimulus activity via its known transcriptomic response.

### Phase 3 — Orthogonal protein validation

**3.1** On aliquots from the same units processed in Phase 1/2, perform an independent protein measurement of the top discordant features by a modality-independent method (e.g., fluorochrome flow cytometry with the matched clone, sorted-subpopulation immunoblotting, or imaging). Analysts blinded to discordance status.

**3.2 Prediction split.** Mechanism A: the orthogonal assay confirms the protein levels implied by the tag measurement in the discordant cells. Mechanism B: orthogonal assay disagrees with the tag measurement (artifact in the tag modality). This phase is what licenses the word "genuine."

**Stop rule.** If orthogonal assays disagree with *both* modalities for the same cells, the discordance metric or cell-handling is flawed; return to Phase 0.

### Phase 4 — Integration decision (the deliverable)

Using the accumulated evidence, compare pre-specified integrated representations on pre-registered criteria: (i) shared-latent-factor denoising (treats discordance as noise), (ii) protein-prioritized representation, (iii) representations that carry an explicit discordance axis. Evaluate: preservation of validated states, robustness to batch, and recovery of the perturbation effect. The output is a *representation recommendation conditioned on the discordance category of each feature*, not a universal algorithm claim.

---

## 5. Outcomes, interpretation, and limits

**Positive outcome (Mechanism A supported):** a defined gene set shows discordance that replicates across units and preparations (A1), is gene-specific and direction-consistent (A2), forms coherent, perturbation-responsive subpopulations (A3), and is orthogonally confirmed (A4), while technical-covariate dependence is low (negating B2) and surviving doublet/ambient correction (negating C). **Strongest justified conclusion:** for those features, RNA–protein discordance defines reproducible cell states consistent with post-transcriptional regulation, and the integrated representation should preserve a discordance axis for them. **Not justified:** naming the specific molecular mechanism (translation vs half-life vs secretion) — that requires experiments outside this plan.

**Negative outcome (Mechanism B supported):** discordance fails to replicate, tracks batch/background/depth covariates, and disappears on orthogonal assay or improved calibration. **Strongest justified conclusion:** apparent disagreements in this system are dominated by modality-specific measurement error; the optimal integrated representation is denoising-based, and prior reports of state-like disagreement in comparable data should be re-examined against error models. **Not justified:** the claim that no genuine post-transcriptional states exist anywhere — only that none were demonstrated here for these features under these conditions.

**Ambiguous outcome (most likely):** a reproducible, orthogonally confirmed subset of features, with the remainder artifact-like. **Strongest justified conclusion:** a feature-level classification; integration should be hybrid (denoise artifact-dominated features, preserve validated discordance axes). If reproducibility is intermediate (e.g., replicates across preparations but not across donors), the honest conclusion is that discordance is real but partly unit-specific — still signal, but not a universal state definition; this outcome would motivate a larger donor cohort before any representation is locked.

**Key uncertainties and what would change the recommendation:** (i) the noise model's adequacy — if replicate-aliquot variance is larger than modeled, some "biology" is really unmodeled noise, shrinking the positive set; (ii) stimulus choice in Phase 2 — a wrong candidate could falsely favor Mechanism B, which is why the pilot and activity check are mandatory; (iii) epitope biology — genuine epitope masking would look like artifact to an orthogonal antibody; using a non-overlapping epitope or modality-independent assay mitigates but does not eliminate this; (iv) sample size — the proposed unit counts are minimums; if donor-to-donor variability in discordance is high, formal power depends on pilot variance estimates not available in this packet.

**Explicit limits of the packet:** the packet establishes only joint measurement (E3) and differential noise (E2). It supplies no dataset, no noise parameters, no antibody panel composition, no donor material, no benchmark, and no prior integration algorithm. Consequently, all thresholds above are placeholders to be pre-registered from Phase 0 calibration, not values reported anywhere.

---

## 6. Summary chain (auditable one-paragraph restatement)

Reported: joint RNA+protein measurement exists; noise properties differ; integration is unspecified; state-defining status of discordance is unestablished. Inferred: discordance is currently uninterpretable without an error-calibrated, replication-based test. Proposed question: which discordances are real states? Competing mechanisms: post-transcriptional regulation vs modality-specific artifact vs doublet/ambient confounds, discriminated by replication across independent units, technical-covariate dependence, perturbation behavior, and orthogonal protein confirmation. Proposed plan: calibrate (Phase 0) → observational replication with randomized, blinded, controlled, multi-unit design (Phase 1) → perturbation discrimination (Phase 2) → orthogonal validation (Phase 3) → conditional integration recommendation (Phase 4), each with stop rules and troubleshooting. Conditional conclusions: positive → preserve discordance as state; negative → denoise; ambiguous → hybrid feature-level decision. No result described above has been observed; all are pre-specified proposals from a single, feedback-free attempt.
