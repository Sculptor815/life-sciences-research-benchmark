# GLM 5.3 FlashX / neu-d02

Original final answer, shared by both scoring rounds.

# Proposed Calibration and Validation Protocol for a Genetically Encoded Calcium Indicator (GECI) with Simultaneous Electrophysiology

**Status: All experiments below are proposed. No data exist yet; every numeric target is a parameter to be calibrated, not a known value.**

---

## 1. Framing: Evidence → Inference → Conclusion Chain

**Evidence (from the fixed packet):**
1. The indicator is reported to improve activity detection and to report somatic and dendritic-spine visual-related signals, with simultaneous imaging and electrophysiology calibration described.
2. The stated limits are explicit: fluorescence reflects calcium dynamics influenced by both the indicator and the imaging system, *not* error-free instantaneous spikes.
3. Calibration in one cell type cannot be unconditionally extrapolated to other cell types.
4. Artefacts are enumerated: movement, focus drift, background, and neuropil contamination producing behaviour-related false signals; indicator kinetics, saturation, or expression level can make identical fluorescence amplitudes correspond to different firing rates.
5. Hypothetical constraints: the indicator identity, expression level, spike counts, imaging rates, and analysis thresholds are all unknown and must be calibrated.

**Inference:** Because the causal chain from spikes → calcium → fluorescence → image → extracted ΔF/F is multi-stage and each stage is condition-dependent, a single correlation coefficient is insufficient. Validation must be (a) *paired* (same cell, same time, spikes and fluorescence from the same trial), (b) *calibrated per cell type and per expression regime*, and (c) *artefact-controlled*, because movement and neuropil signals are themselves correlated with behaviour and visual stimuli and can therefore masquerade as true activity.

**Conclusion:** A valid protocol must deliver four calibrated outputs before the indicator is used for inference: (1) a spike-to-fluorescence transfer function for the target cell type; (2) a motion and neuropil artefact budget; (3) a detection operating characteristic (sensitivity vs. false-positive rate) on held-out paired data; and (4) an expression-level validity window. The protocol below is ordered to produce these.

---

## 2. Protocol at a Glance (Ordered Phases)

| Phase | Purpose |
|---|---|
| A. Preparation and quality checks | Animal, indicator expression, rig, electrophysiology readiness |
| B. Independent units and allocation/blinding | Define analysis units, prevent analyst bias |
| C. Calibration experiments | Spike transfer function, imaging rate, expression window |
| D. Intervention and sampling | Visual stimulation with paired recording |
| E. Measurements | Two-channel imaging (indicator + structural), 3D motion, electrophysiology |
| F. Controls | Neuropil, movement, no-stimulus, dead/anesthetized tissue |
| G. Analysis | Pre-registered pipeline, held-out validation |
| H. Acceptance/stopping criteria and troubleshooting | Go/no-go gates |

---

## 3. Phase A — Preparation and Quality Checks (all proposed)

**A1. Animals and expression.** Express the indicator in the target cell type using the planned genetic strategy (proposed: cell-type-specific promoter or viral delivery). Because expression level is an unreported parameter:
- *Calibration procedure:* For each recorded cell, measure baseline fluorescence in the indicator channel, normalize to the co-acquired structural reference channel (Section 5, M2) to obtain an expression proxy, E = F_indicator / F_structural. Record the distribution of E across the cohort. Stratify all downstream calibration results by E-tertile (low/mid/high) and test whether the spike-to-fluorescence relationship varies with E. If it does, define an acceptable E window outside which fluorescence amplitudes are flagged as non-interpretable.
- Do not assume a saturation-free regime. *Calibration:* present high-frequency spike events (see C3) and check whether peak ΔF/F plateaus with increasing spike counts; if it plateaus, define the saturating spike count and exclude amplitudes above it from quantitative inference.

**A2. Imaging rig.** Two simultaneous channels, proposed configuration:
- Channel 1 (functional): indicator excitation/emission.
- Channel 2 (structural/reference): a co-acquired morphological channel (e.g., a second fluorophore or the indicator's own structural signal, per available hardware) used for focus tracking, motion estimation, and expression normalization. Confirm both channels are co-registered and co-temporal before any data collection (acquire a static calibration target; report channel alignment offset and inter-channel timing skew; correct if non-zero).

**A3. Electrophysiology.** Whole-cell or juxtasomal recording of the imaged neuron in the target cell type, with spike times timestamped to the imaging clock. *Calibration:* record the imaging frame sync and the acquisition system sync simultaneously at session start; estimate clock drift over a 30–60 min session and correct; discard sessions with uncorrectable drift.

**A4. Visual stimulation.** Structured visual stimuli (drifting gratings, sparse noise, or naturalistic movie — chosen to drive the target cell type) presented under reproducible timing locked to the combined imaging/recording clock.

**A5. Health checks before each session.** Confirmed indicator expression in the target region; stable baseline fluorescence; stable spiking in response to a standard probe stimulus; respiration/eye movement monitoring if the animal is awake.

---

## 4. Phase B — Independent Units, Allocation, and Blinding

**B1. Independent units.** The primary independent unit is the *cell–session* (one neuron, one paired imaging/recording session). Secondary units: *trials* (stimulus repeats) and *time bins*. For cell-type-level conclusions, the unit is the cell; trials and time bins are repeated measures and must not be treated as independent for statistical inference. Record the number of animals, cells, and sessions and report clustering.

**B2. Allocation.** Proposed: order conditions (stimulus types, movement states) in a randomized, counterbalanced sequence within each session to prevent time-dependent drift (photobleaching, recording degradation) from confounding condition effects.

**B3. Blinding.** The analyst running the fluorescence extraction and spike-inference pipeline should be blinded to the electrophysiological results until the analysis pipeline is frozen and pre-registered. Spike sorting and quality-metric assignment should be performed by an analyst blinded to the fluorescence traces. Only after both pipelines are locked are the paired datasets joined.

---

## 5. Phase C — Calibration Experiments (proposed; all parameters to be measured, not assumed)

**C1. Imaging rate calibration.**
- Unknown: required frame rate relative to indicator decay kinetics.
- *Procedure:* Record spikes and fluorescence while presenting transient spike-evoking probes. Estimate the indicator decay time constant τ from the fluorescence decay following isolated spike events (spike-triggered averaging). Compare ΔF/F amplitude and spike-detection performance at the candidate frame rates achievable by the rig (propose sweeping at least a slow and a fast rate). Choose the fastest practical rate; report τ and the Nyquist margin. If frame rate < ~2/τ, flag single-event resolution as unreliable and target population-rate inference instead.

**C2. Spike-count / amplitude calibration in the target cell type (the core transfer function).**
- Unknown: how many spikes produce what ΔF/F, and whether the relation is linear.
- *Procedure:* In paired recordings, identify isolated fluorescence transients with simultaneous spike counts of 1, 2, 3, … events. Construct a spike-count → peak-ΔF/F curve (spike-triggered averages and event-triggered averages). Fit and report: (i) single-spike ΔF/F amplitude and variability; (ii) the linearity range; (iii) the half-decay time per spike count; (iv) the spike count at which saturation begins. Repeat in a *second* cell type if any cross-cell-type inference is intended — per the stated limit, one cell type's calibration cannot be extrapolated unconditionally.

**C3. Kinetics check.** Measure the rise time and decay time of fluorescence evoked by single spikes vs. spike bursts; verify the indicator does not distort fast stimulus-locked timing beyond what the analysis model assumes.

**C4. Noise floor.** Record in a "silent" condition (no stimulus, quiescent animal, verified by electrophysiology) to measure baseline noise of the fluorescence trace — required for false-positive calibration (Section 9, G3).

---

## 6. Phase D — Intervention and Sampling

**D1. Main session structure (per cell–session).**
1. Baseline block: no stimulus, spontaneous activity (≥ a pre-registered minimum duration, e.g., several minutes — exact duration to be set from C4 noise-stability analysis).
2. Visual-response block: repeated presentations of each stimulus type, randomized order, sufficient trials to estimate per-condition response distributions (trial count determined by pilot variance; proposed target ≥20 trials/condition, adjusted).
3. Movement/neuropil control block: stimulus-free epochs with induced or naturally occurring movement (locomotion, whisking, eye movements), recorded but without expected specific spiking responses — used to quantify artefact-driven fluorescence.
4. Optional drift probe: slow structural-only imaging to quantify focus drift over session duration.

**D2. Sampling plan.** Propose N ≥ 3 animals, ≥ 15–30 target cells total (final N from power analysis on the C2 calibration variance; do not fix N in advance of that measurement). Stop recruitment when the confidence interval on the primary metric (Section 8) is narrower than a pre-set criterion, or when the stopping rule in Section 10 triggers.

---

## 7. Phase E — Measurements

**M1. Functional channel.** Indicator fluorescence, full-frame, at the calibrated rate.

**M2. Structural reference channel.** Simultaneously acquired morphological image used for:
- Focus-drift estimation (axial: compare structural channel intensity/contrast signature against a pre-acquired z-stack; propose acquiring a reference z-stack at session start).
- Lateral motion estimation (template matching / registration of the structural channel; report translation estimates per frame).
- Expression proxy E = F_indicator/F_structural (A1).
- Cell-boundary verification (confirm the ROI still encloses the same soma/spine throughout the session).

**M3. Three-dimensional motion estimation.**
- Combine lateral registration offsets (M2) with axial focus estimates (structural intensity vs. z-stack lookup). Output per-frame (dx, dy, dz).
- Flag frames with motion exceeding a pre-registered tolerance (to be calibrated: determine the Δz at which measured ΔF/F changes without any concurrent spike activity, using silent epochs; set tolerance below that).
- *Calibration procedure for motion sensitivity:* during silent epochs, artificially introduce known focus offsets (z-stepper steps) and measure the induced ΔF/F; this yields a motion-to-artefact transfer curve used to set thresholds and to correct or reject contaminated frames.

**M4. Neuropil measurement.**
- Define per-cell neuropil annuli around each ROI (annulus geometry to be calibrated: sweep annulus inner/outer radius and verify the neuropil signal is not contaminated by soma pixels; choose the geometry that minimizes structural-channel somatic signal inside the annulus).
- Record raw neuropil fluorescence per frame, plus its response to visual stimuli and movement.

**M5. Electrophysiology.** Continuous wideband recording; spike times extracted with quality metrics (amplitude, SNR, stability over session, ISI violations). Exclude cells with unstable recordings.

---

## 8. Phase F — Controls (all proposed)

| Control | Purpose | Readout |
|---|---|---|
| No-stimulus, quiescent epoch | Noise floor, false-positive baseline | Spontaneous ΔF/F events vs. verified spikes |
| Movement block without stimulus | Movement-induced fluorescence artefact independent of neural signal | ΔF/F vs. (dx,dy,dz) regression; residual after regression |
| Structural-channel-only check | Confirms visual stimuli and movement do not alter the structural channel (ruling out haemodynamic/scattering confounds attributed wrongly to indicator) | ΔF/F_structural during stimuli; should be negligible; if not, quantify and regress it out |
| Neuropil-rich regions of interest (ROI in neuropil, no soma) | Direct false-positive test: do ROI extraction methods report "activity" in acellular neuropil during behaviour/stimulus? | Event rate in neuropil-only ROIs |
| Second cell type (if extrapolation is intended) | Tests the stated non-extrapolation limit | Repeat C2 transfer function |
| Expression-low/high strata | Tests expression-level dependence (A1) | Transfer function by E-tertile |

**Neuropil contamination sensitivity (explicit requirement).** Calibrate the sensitivity of spike inference and event detection to neuropil correction:
- Vary the neuropil correction coefficient over a range (proposed sweep: e.g., 0 to a high fraction of raw neuropil signal subtracted; exact coefficient range determined from measured soma–neuropil fluorescence ratios).
- For each coefficient value, recompute (i) detected event rate, (ii) spike-inference accuracy against paired spikes, (iii) false-positive rate in silent/movement epochs.
- Report the *sensitivity curve*: how conclusions change as a function of neuropil correction. If spike-inference accuracy is flat across a plausible coefficient range, the result is robust; if it swings, the coefficient must be fitted per cell (proposed: fit it by minimizing the fluorescence residual during verified silent epochs) and the fitted value reported per cell.

---

## 9. Phase G — Analysis (pre-registered, blinded, then validated on held-out data)

**G1. Preprocessing.** Motion correction using 3D estimates (M3); neuropil subtraction (per F); ΔF/F computation; expression-window flagging (A1); frame rejection by motion tolerance; sync-alignment of spikes and frames (A3).

**G2. Spike inference / event detection.** Apply a candidate spike-inference or event-detection method. Because thresholds are unknown:
- *Calibration:* on a **training split** (e.g., 50–70% of cell–sessions, chosen before analysis), fit the detection threshold and any model parameters against paired spikes.

**G3. Detection and false-positive reporting (primary validation).**
- On the **held-out test split** (untouched during fitting), compute against electrophysiological ground truth:
  - **Sensitivity** (detected events / true spike events or true spike epochs);
  - **False-positive rate** (detected events with no concurrent spikes / time, and per-session);
  - **Precision/recall, F1**, and a confusion-style report at the single-event and per-trial levels;
  - **Spike-count fidelity:** predicted vs. true spike count per transient (slope, R², and bias vs. spike count);
  - **Timing fidelity:** lag between detected events and spikes (should reflect calibrated indicator kinetics, C3).
- Also report the *no-ground-truth* false-positive proxies: event rates in silent epochs and neuropil-only ROIs (F).
- Report a full **receiver-operating or precision-recall curve** across thresholds, not a single threshold's numbers, so end users can select an operating point.

**G4. Visual-response tracking validation.** For each stimulus condition, compute the fluorescence-derived tuning/response curve and the spike-derived curve from paired data; report the correlation between them, per condition and per cell. Any visual-response claim (including the reported dendritic-spine signals, if spine imaging is added) must be validated with the same paired logic at the spine ROI level, with spine motion handled by the same 3D pipeline (spines require more stringent motion tolerance; flag as a separate validation tier).

**G5. Artefact attribution.** Regress the fluorescence trace against motion traces (M3), neuropil trace (M4), and structural-channel fluctuations (M2); report variance explained by each. Any "neural" conclusion requires that the spike-locked component survives these regressions and matches paired spikes.

---

## 10. Acceptance Criteria, Stopping Rules, and Troubleshooting (proposed thresholds; exact values set from pilot data)

**Acceptance (all must hold on the held-out split):**
1. Single-spike or event sensitivity and false-positive rates meet pre-registered targets (targets set from C2/C4 variability; typical aim: detectable sensitivity with false-positive rate in silent epochs near the statistical noise floor — final numbers to be fixed after pilot power analysis).
2. Spike-count transfer function is stable within the expression window and non-saturated over the spike range used.
3. Motion- and neuropil-explained variance in the validated detection is below a pre-set fraction; conclusions are insensitive to the neuropil coefficient over the plausible range (F).
4. Structural channel confirms stable focus, ROI containment, and no stimulus-locked structural artefact.
5. Calibration performed in the target cell type (and in any additional cell type for which inference is claimed).

**Stopping rules:**
- Stop recording a cell–session if: sync drift uncorrectable; spike quality metrics fail; motion exceeds correctable tolerance for a sustained period; or photobleaching/indicator expression falls outside the calibrated E window.
- Stop cohort recruitment when acceptance-metric confidence intervals meet the pre-registered width.

**Troubleshooting (proposed responses):**
- *Movement artefacts dominate:* increase motion tolerance enforcement, improve stabilization, restrict analysis to low-motion frames; re-derive the motion-to-artefact curve.
- *Neuropil contamination high:* refit annulus geometry, fit coefficient per cell, or restrict claims to high-SNR cells; re-run the sensitivity sweep.
- *Saturation:* lower expression (A1) or restrict inference to spike counts below the saturating count.
- *Poor spike-fluorescence correspondence:* verify sync (A3), verify ROI contains a healthy cell, check indicator expression level, re-check kinetics vs. frame rate (C1).

---

## 11. Alternatives and Limits

**Alternatives considered:** (i) Population-level validation without paired recordings — rejected: it cannot separate indicator kinetics/saturation from detection errors, and it cannot produce spike-count calibration. (ii) Post-hoc neuropil correction only — rejected: without the sensitivity sweep, the dependence of conclusions on the correction coefficient is unknown. (iii) Calibrating in a surrogate cell type — explicitly disallowed by the stated limit unless a second cell type is separately calibrated.

**Limits and consequential uncertainties:**
- The calcium signal fundamentally reflects indicator kinetics and the imaging system, not instantaneous spikes; single-spike resolution is bounded by τ and frame rate and may be unachievable — the protocol then degrades gracefully to burst/population-rate inference.
- Expression-level dependence may not be fully captured by the structural-normalized proxy E; direct measures of indicator abundance would strengthen the window definition.
- Movement artefacts correlated with behaviour may never be fully separable from genuine movement-related neural activity; the movement-block control bounds, but does not eliminate, this residual.
- Dendritic-spine validation requires its own motion and neuropil treatment and should not inherit somatic calibration values.
- Cross-session stability of calibration (days/weeks, expression changes) is untested here and would require a longitudinal follow-up.

**What would change the recommendation:** measured τ relative to achievable frame rates (changes single-event vs. rate inference); measured motion-to-artefact magnitude (changes required stabilization); dependence of the transfer function on expression (changes whether a single calibration suffices); and any intended extension to additional cell types or spine-level claims (each requiring its own calibration arm).
