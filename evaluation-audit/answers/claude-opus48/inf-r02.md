# Claude Opus 4.8 / inf-r02

Original final answer, shared by both scoring rounds.

## Recommended next question

**Do single-cell disagreements between a marker's transcript and its surface-protein measurement identify genuine, reproducible cell states (driven by post-transcriptional/temporal regulation), or are they dominated by measurement artifacts (dropout, ambient contamination, nonspecific antibody binding)?**

This is the highest-value next step because the supplied packet explicitly establishes only that joint RNA+protein measurement is *possible* on the same cells, while flagging two open issues: (1) no optimal integrated representation is defined, and (2) it is *not* established that apparent RNA–protein disagreements define real cell states. Answering the disagreement-validity question is logically prior to building any integration algorithm: an integration method can only be benchmarked once we know which cross-modal signals are biology and which are noise. Everything downstream (representation choice, denoising, cell-state calling) inherits the answer.

---

## Evidence → inference → conclusion chain

- **Evidence (packet):** Oligo-tagged antibodies link surface-protein and transcript measurements in the same cell; the two modalities carry *complementary information* and have *different noise and detection properties*.
- **Inference:** Because the modalities differ in noise and detection, per-cell disagreement for the same gene product (e.g., RNA detected, protein not, or vice versa) can arise from either biology or technical error. The two are confounded in any single measurement.
- **Inference:** The packet states no result establishes that disagreements are real states, so the field currently cannot attribute a given disagreement to a mechanism.
- **Conclusion:** The decisive experiment is one that *partitions* observed disagreement into technical vs. biological sources using orthogonal validation and designed controls, rather than one that assumes either interpretation.

I am not claiming any disagreement is real or artifactual — the packet supplies no such result. The plan below is a proposal to discriminate.

---

## Competing mechanisms and discriminating predictions

**Mechanism A — Technical artifact dominates.**
Sub-mechanisms: (A1) transcript dropout from low mRNA capture; (A2) ambient/free antibody-oligo contamination inflating protein counts; (A3) nonspecific or cross-reactive antibody binding; (A4) index hopping / barcode spillover.
Predictions:
- A-i: Disagreement rate scales with technical covariates (low total UMIs → more RNA⁻; high ambient ADT background → more protein⁺).
- A-ii: Protein⁺ signal on cells genetically lacking the target (knockout, or a cell type that cannot express it) is comparable to isotype control → specificity failure.
- A-iii: Disagreements are *not reproducible* across donors, library preps, or platforms.
- A-iv: Disagreements do **not** co-vary with any independent functional cell-state marker.
- A-v: Orthogonal single-molecule validation (smFISH for RNA, flow/imaging for protein) fails to confirm the discordant quadrant.

**Mechanism B — Real biology dominates (post-transcriptional / temporal decoupling / trafficking).**
Sub-mechanisms: (B1) transcription-then-translation lag (RNA⁺/protein⁻ transient early); (B2) long protein half-life after transcription ceases (RNA⁻/protein⁺ late); (B3) surface internalization/trafficking or trogocytosis (protein present without local transcription); (B4) translational/post-transcriptional repression.
Predictions:
- B-i: Disagreement is reproducible across donors and platforms for the *same* cell type/state.
- B-ii: Disagreement is cell-type/state specific and co-varies with independent functional markers (e.g., activation, cell-cycle, differentiation genes).
- B-iii: In a controlled time course, disagreement shows the predicted temporal order (RNA rises before protein; protein persists after RNA falls).
- B-iv: Orthogonal methods (smFISH + intracellular/surface protein imaging on the same cells) confirm the discordant quadrant at matched prevalence.
- B-v: Disagreement is robust to removing technical confounders (persists after ambient subtraction, within high-quality cells, and above knockout/isotype floor).

The mechanisms are not mutually exclusive; the realistic question is the *fraction* of disagreement explained by each, and whether any marker/state shows B-type signal surviving all A-controls.

---

## Proposed research plan (ordered, auditable)

> All items below are **proposed methods**, not reported results. Unreported parameters are flagged as assumptions to be fixed during calibration.

### 0. Design overview

A factorial validation study on a defined, perturbable cell system, measuring the same markers by (i) joint RNA+ADT (the assay in the packet), (ii) orthogonal protein (flow cytometry/CyTOF), and (iii) orthogonal RNA (smFISH/imaging), plus engineered negative controls (target-knockout cells) and a controlled induction time course. The primary endpoint is the decomposition of per-marker disagreement into technical vs. biological variance and its orthogonal confirmation.

### 1. Model system and marker panel (prerequisites)

- **System:** Human PBMCs from ≥4 independent donors, plus one activation time course (anti-CD3/CD28 stimulation of purified T cells, timepoints 0, 2, 6, 24, 72 h). Rationale: activation markers give *a priori* temporal-decoupling predictions.
- **Spike-in / specificity controls:** (a) a cell line or primary population that cannot express a chosen marker; ideally (b) a **CRISPR knockout** of 1–2 target surface proteins (e.g., a lineage marker) to create a true protein-negative ground truth; (c) a human/mouse cell mixture ("barnyard") to quantify cross-cell contamination.
- **Marker panel (auditable choices):**
  - *Stable lineage markers* expected to largely agree: CD3, CD4, CD8, CD14, CD19, CD56.
  - *Temporally decoupled markers* (test B1/B2): CD69 (fast induction), CD25/IL2RA (delayed), a marker with long protein half-life.
  - *Trafficking-prone marker* (test B3): a receptor known to internalize.
  - Include transcript probes matched to every antibody target.
- **Assumption to fix in calibration:** final antibody concentrations, panel size, cell input per lane.

### 2. Calibration (must precede the main run)

1. **Antibody titration:** for each antibody-oligo, titrate to the staining index maximum; record signal-to-background on known-positive vs known-negative cells. Stop rule: any antibody failing to separate positive from negative populations is dropped or replaced.
2. **Ambient/background characterization:** sequence empty droplets to estimate per-ADT ambient profile; include **isotype-control antibody-oligos** matched to each host/isotype. Define the per-marker protein background floor as max(isotype signal, empty-droplet ambient).
3. **RNA detection limit:** from the data, estimate per-transcript dropout as a function of total UMIs using the agreeing lineage markers (e.g., CD3 mRNA vs protein in T cells) as internal references.
4. **Specificity floor:** stain the knockout / non-expressing population; the residual ADT signal defines the nonspecific-binding floor for that marker.
5. **Cross-contamination:** barnyard mixture quantifies fraction of ADT/UMI assignable to the wrong cell.

Record all calibration constants in a frozen parameter file *before* unblinding main analysis.

### 3. Independent units and replication

- **Biological units:** ≥4 donors (steady-state) + ≥3 independent cultures per time course point. Donors/cultures are the units of statistical inference.
- **Technical replication:** each biological sample split into ≥2 independent library preparations; ≥2 sequencing runs where feasible.
- **Platform replication:** repeat the core comparison on a second independent joint-assay chemistry/platform to test prediction A-iii/B-i reproducibility. (If a second platform is unavailable, substitute a second independent antibody clone per target as a partial orthogonal check.)

### 4. Allocation and blinding

- **Multiplexing:** use cell-hashing antibody-oligos to pool donors/conditions in each lane, so batch effects are shared across conditions (reduces confounding of condition with lane).
- **Randomization:** randomize donor→hash assignment and lane loading order.
- **Blinding:** the orthogonal-validation operators (flow/smFISH/imaging) and the analyst computing disagreement metrics are blinded to which cells the joint assay called discordant until after disagreement calls are frozen. Validation gating thresholds are set on control samples before looking at experimental discordant cells.

### 5. Controls (summary)

- Isotype-control antibodies (per-marker protein background).
- Empty-droplet ambient profile (ambient subtraction).
- Knockout / non-expressing population (specificity floor; true protein-negative).
- Barnyard mixture (cross-cell contamination).
- Agreeing lineage markers (internal positive controls for concordance).
- Unstimulated t=0 sample (baseline for the time course).
- Technical replicate libraries (reproducibility).

### 6. Measurements

Per cell, per marker:
- RNA UMI count for the target transcript.
- ADT count for the target protein (and matched isotype).
- Cell-quality covariates: total UMIs, total ADT, mito fraction, doublet score, hash identity.
Orthogonal, on matched aliquots:
- Flow/CyTOF protein distribution per population.
- smFISH transcript counts per cell for ≥2 discordant markers, imaged with the surface/intracellular protein stain on the *same* cells where possible (spatially matched RNA+protein ground truth).

### 7. Analysis pipeline (pre-registered)

1. **QC and cell typing** using the agreeing lineage markers (both modalities), independent of the markers under test.
2. **Normalization/denoising of ADT:** subtract ambient and isotype floor; normalize RNA by standard size-factor method. Record method; do not tune to produce discordance.
3. **Define disagreement calls** per marker per cell into four quadrants: RNA⁺/protein⁺, RNA⁺/protein⁻, RNA⁻/protein⁺, RNA⁻/protein⁻, using thresholds set *on controls* (RNA⁺ above dropout-adjusted detection; protein⁺ above specificity floor). Freeze calls.
4. **Variance partition (the core test):** fit a model of each discordant-quadrant indicator on (a) technical covariates (total UMIs, ambient ADT, doublet score, lane), and (b) cell-state covariates (cell type, activation score, cell-cycle phase, timepoint). Compare nested models (technical-only vs technical+biology) by cross-validated fit and variance explained. Report fraction of disagreement attributable to each block.
5. **Reproducibility test:** correlate per-cell-type disagreement rates across donors, library preps, and platforms/clones. Compute intraclass correlation.
6. **Temporal test:** in the activation series, test the ordered prediction that CD69 RNA⁺/protein⁻ precedes protein⁺, and that persistence markers show RNA⁻/protein⁺ late.
7. **Orthogonal confirmation:** compare joint-assay discordant-quadrant prevalence against smFISH+protein imaging prevalence per population; test agreement with a prespecified tolerance.
8. **Specificity subtraction:** recompute all protein⁺ discordant calls after setting the per-marker floor to the knockout/non-expressing signal; report how many survive.

All thresholds, models, and tolerances are fixed in a pre-registration before main-data analysis.

### 8. Stop rules

- **Stop/abort a marker** if its antibody fails titration separation or if knockout-floor protein signal is indistinguishable from positive signal (uninterpretable specificity).
- **Declare artifact for a marker** if the technical-only model explains disagreement within a prespecified margin of the full model AND discordant signal does not survive ambient/specificity subtraction AND orthogonal validation does not confirm.
- **Declare biology for a marker** if disagreement survives all technical controls, is reproducible (ICC above threshold) across donors/platforms, and is orthogonally confirmed.
- **Halt for quality** if doublet rate, ambient fraction, or hashing demultiplexing failure exceeds prespecified limits; re-run.

### 9. Troubleshooting

- *High ambient ADT:* improve washes, reduce antibody input, strengthen empty-droplet subtraction; re-estimate floor.
- *Excessive RNA dropout confounds RNA⁻ calls:* restrict analysis to high-UMI cells; use dropout-aware thresholds; report sensitivity to the cutoff.
- *Doublets mimicking protein⁺/RNA⁺ in wrong cells:* enforce doublet removal; use barnyard estimate to bound residual contamination.
- *Clone-dependent protein signal:* if two clones disagree, treat the marker as specificity-ambiguous and escalate orthogonal validation.
- *smFISH/flow prevalence mismatch:* check gating, fixation effects on epitopes, probe efficiency; reconcile before conclusions.

---

## Conditional outcomes and the strongest justified conclusion

**Positive (biology confirmed) outcome.** For ≥1 marker, disagreement survives ambient/isotype/knockout subtraction, is reproducible across donors and platforms, co-varies with independent cell-state covariates, follows the predicted temporal order in the activation series, and is confirmed by smFISH+imaging at matched prevalence. → **Justified conclusion:** these RNA–protein disagreements define real, post-transcriptionally/temporally regulated cell states, and an integration method must *preserve* (not erase) cross-modal discordance for these markers. This directly fills the packet's open gap and constrains future representation design.

**Negative (artifact) outcome.** Disagreement tracks technical covariates, collapses to the knockout/isotype floor after subtraction, is non-reproducible across donors/platforms, does not co-vary with any functional state, and is not orthogonally confirmed. → **Justified conclusion:** apparent disagreements for these markers are measurement noise; the optimal representation should *denoise toward concordance* for them, and disagreement should not be used to call new cell states without orthogonal support.

**Ambiguous / mixed outcome (most likely a priori).** Some markers show B-type (real) signal while others show A-type (artifact); or a marker is reproducible but not orthogonally confirmed, or confirmed but not clearly temporal. → **Justified conclusion:** disagreement validity is *marker- and context-specific*; no blanket interpretation is warranted. The deliverable becomes a per-marker, per-cell-type annotation of whether discordance is trustworthy, plus the quantitative technical-vs-biological partition — itself a necessary prerequisite and benchmark for any later integration algorithm (which the packet notes is not yet supplied).

---

## Limits and scope

- The plan discriminates *mechanism of disagreement*; it does not by itself deliver an optimal integrated representation (explicitly out of scope per the packet, which supplies no integration method or benchmark). It supplies the ground-truth labels such a benchmark needs.
- Conclusions are limited to the chosen markers, cell types, and platform(s); generalization requires replication beyond PBMCs.
- Knockout ground truth may be available for only a subset of markers; for the rest, specificity rests on non-expressing populations and multi-clone agreement, which is weaker.
- smFISH/flow use fixation/permeabilization that can alter epitopes or capture; prevalence comparisons carry this systematic uncertainty, mitigated but not eliminated by blinding and prespecified tolerances.
- All quantitative thresholds (titers, UMI floors, ICC cutoffs, prevalence tolerances) are **unreported parameters to be fixed in calibration/pre-registration**, not values claimed here.

This single, self-contained study converts the packet's acknowledged uncertainty ("not established that disagreements define real states") into a per-marker, auditable determination, and is the most valuable next biological question because every downstream integration and cell-state-discovery decision depends on its answer.
