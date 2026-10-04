# Claude Opus 4.8 / neu-d02

Original final answer, shared by both scoring rounds.

# Proposed Calibration and Validation Protocol for a GECI as a Spike-Inference Reporter

**All experiments described below are proposed, not performed.** Exact indicator identity, expression level, spike counts, imaging frame rates, and analysis thresholds are treated as unknown and are *calibrated empirically* rather than assumed.

---

## Bottom line (recommended approach)

Build the validation as a layered chain in which **each known artefact in the evidence packet is matched to a specific control and a quantitative acceptance criterion**. The core is simultaneous cell-attached/juxtacellular electrophysiology (ground truth) paired with two-photon imaging of the same identified neuron, acquired with a **structural reference channel** and **3D motion tracking**, under both visual stimulation and quiet/baseline epochs. From this you derive a per-cell-type transfer function (fluorescence → calcium → spike probability/rate) with reported detection sensitivity and false-positive rate, and you explicitly bound the conditions under which that transfer function may be extrapolated.

The single most consequential design decision is that **the fluorescence-to-spike mapping must be reported as a cell-type- and expression-conditioned distribution with uncertainty, not a fixed scalar gain**, because the evidence states the same fluorescence amplitude can correspond to different firing depending on kinetics, saturation, and expression level.

---

## Concepts and their relationships

- **Ground truth (electrophysiology)** defines true spike times/counts. Everything else is inferred.
- **GECI fluorescence** is a *filtered, nonlinear, saturating* report of intracellular calcium, which is itself an indirect report of spiking. The chain is: spikes → calcium transient → indicator binding/kinetics → photon emission → detector counts → ΔF/F → inferred spikes. Each arrow adds distortion the protocol must quantify.
- **Structural reference channel** (a calcium-insensitive fluorophore, e.g. a co-expressed static marker or a second spectral channel) provides a motion/expression denominator independent of activity, so that activity-related ΔF/F can be separated from motion- and focus-related fluorescence changes.
- **3D motion estimation** addresses the "movement, focus drift" artefact: lateral (x,y) and axial (z) displacement of the cell relative to the focal volume changes fluorescence without any change in calcium.
- **Neuropil contamination** addresses the "background and neuropil" artefact: surrounding neuropil signal leaks into the somatic/spine region of interest (ROI), carrying behaviour- and stimulus-correlated signal that is not that cell's spiking.
- **Expression-level / kinetics / saturation** addresses why the transfer function is conditional and non-extrapolable.
- **Visual-response tracking** is the functional read-out used to show the indicator reports stimulus-driven somatic and dendritic-spine signals, and simultaneously a setting where false signals (behaviour-correlated motion) are most dangerous.

Relationship summary: the **ground truth constrains** the transfer function; the **reference channel, 3D motion, and neuropil controls remove confounds** before fitting that function; **expression checks define the validity domain**; and **visual responses test real-world inference** including false positives.

---

## Evidence → inference → conclusion chain

1. **Evidence:** fluorescence reflects calcium dynamics shaped by indicator and imaging system, not error-free instantaneous spikes. **Inference:** a deterministic 1:1 spike readout is invalid; a probabilistic/rate transfer function with confidence bounds is required. **Conclusion:** report spike *inference* with detection probability and temporal uncertainty, calibrated against paired ephys.

2. **Evidence:** calibration in one cell type cannot be unconditionally extrapolated. **Inference:** the transfer function is a function of cell type (and by the same logic, expression and imaging conditions). **Conclusion:** calibrate *in the target cell type* and explicitly state the validity domain; treat cross-type use as a separate, flagged inference.

3. **Evidence:** movement, focus drift, background, and neuropil produce behaviour-related *false* signals. **Inference:** stimulus/behaviour correlation of a signal is not sufficient evidence of spiking. **Conclusion:** require that candidate signals survive reference-channel regression, 3D motion correction, and neuropil subtraction before being counted, and quantify residual false-positive rate against ephys.

4. **Evidence:** indicator kinetics, saturation, and expression level make the same fluorescence amplitude correspond to different firing. **Inference:** amplitude alone is ambiguous. **Conclusion:** calibrate the full nonlinear amplitude–rate relation including the saturating regime, and measure expression as a covariate.

---

## Operational, ordered protocol

### Stage 0 — Preparation and quality checks

**Targets to define before data collection (each is a calibrated unknown):**
- *Indicator identity / variant:* unknown in the packet. Record the actual construct, promoter, and delivery method used. Because kinetics are variant-specific, **do not assume literature kinetics**; measure them (Stage 5).
- *Expression level:* unknown. Define a **structural-channel-normalized expression metric** (see Stage 1) and pre-register inclusion windows *after* the pilot establishes the distribution.
- *Imaging rate:* unknown. Determine by a **Nyquist-for-kinetics calibration**: in a pilot, image single evoked transients at the fastest feasible frame rate, fit the rise time, and set the operating frame rate to oversample the measured rise by ≥3–5×. State the measured rise time and the chosen rate; do not invent a number.
- *Analysis thresholds* (event-detection threshold, neuropil coefficient, motion rejection bounds): all set by calibration procedures in Stages 6–7, not assumed.

**QC gates:**
- Structural channel present, in focus, and bright enough to serve as a motion/expression denominator (define minimum SNR in pilot).
- Electrode seal quality (for cell-attached: stable seal resistance; for juxtacellular: clear, sortable spike waveforms) meeting a pre-registered threshold.
- Confirmed spatial correspondence: the recorded neuron is the same neuron as the imaged ROI (e.g., electrode-tip dye or targeted patch under visual guidance).
- Photobleaching/phototoxicity budget: measure baseline fluorescence decay over a test epoch; set a maximum tolerable baseline drift per session.

### Stage 1 — Structural reference channel and expression-level check

- Co-image a **calcium-insensitive structural fluorophore** in a spectrally separated channel, simultaneously with the GECI.
- **Expression metric:** compute GECI resting brightness normalized to structural-channel brightness per ROI. This controls for how much indicator is present. Record this metric for every calibrated cell; it becomes a **covariate** in the transfer-function fit and a basis for the validity domain.
- **Saturation flag:** cells with resting GECI/structural ratio in the top of the distribution are flagged as candidate over-expressors (potential buffering of calcium, altered kinetics, baseline saturation). Do not exclude a priori; analyze expression as a graded covariate and report sensitivity of the transfer function to it.

### Stage 2 — Independent units and sampling design

- **Independent unit = individual calibrated neuron** with paired ephys, nested within animal. Treat animal as a random effect; do not pseudoreplicate across cells from one animal as if independent.
- **Target sample (proposed, to be fixed by a pilot power analysis):** enough cells per target cell type to estimate the amplitude–rate relation across the firing-rate range *and* to estimate false-positive rate with a usefully narrow confidence interval. Because the spike-count distribution is unknown, run a pilot (Stage 4) to obtain the variance of inferred-vs-true spike counts, then compute n to achieve a pre-set precision on detection sensitivity and on the amplitude–rate slope. **State the target n only after the pilot; do not invent it now.**
- **Cell-type coverage:** calibrate the specific target cell type. If the study will later image a second cell type, that requires its own calibration block (per the non-extrapolation constraint).

### Stage 3 — Allocation and blinding

- **Allocation:** cells are not "assigned to conditions"; instead each cell passes through all epoch types (baseline, evoked, motion-challenge). Randomize the *order* of visual-stimulus blocks and motion-challenge blocks within a session to decorrelate them from bleaching/drift trends.
- **Blinding:** the analyst performing spike inference from fluorescence is **blinded to the simultaneous ephys** during inference. Spike sorting of the ephys ground truth is performed independently (separate operator or automated, with blinded manual curation). Only after both are finalized are they aligned for scoring. This prevents tuning the fluorescence inference to match known spikes.
- Pre-register the analysis pipeline and all thresholds (or the calibration rule that sets them) before unblinding.

### Stage 4 — Intervention and sampling (data acquisition epochs)

Each calibrated neuron is recorded through the following epochs in randomized block order:

1. **Quiet baseline epoch** (no stimulus, animal still): characterizes spontaneous firing and baseline fluorescence noise; anchors the false-positive estimate in the absence of evoked drive.
2. **Known-spike-count calibration epoch:** drive or capture a graded range of spike counts in the target cell type. Because exact spike numbers are unavailable and are a calibrated unknown, obtain the range by whichever method is feasible and least perturbing:
   - naturally occurring spontaneous spikes/bursts sorted from the ephys (preferred: no perturbation), and/or
   - controlled current injection / minimal optogenetic or sensory drive to populate the high-count tail if spontaneous activity under-samples it.
   The **ground truth is the ephys-counted spikes**, not an assumed count. Bin to produce single-spike, few-spike, and high-count/burst exemplars so the saturating regime is sampled.
3. **Visual-stimulation epoch:** present a battery of visual stimuli to evoke somatic and (where resolvable) dendritic-spine responses, with simultaneous ephys. This is the functional read-out and the primary false-positive test bed.
4. **Motion-challenge epoch:** deliberately introduce the behaviour-related motion the packet warns about (e.g., locomotion bouts, or small controlled axial/lateral stage perturbations as a surrogate), while recording ephys, structural channel, and 3D position. This provides the data to measure how much "behaviour-correlated false signal" survives correction.

### Stage 5 — Measurements

Collected simultaneously and time-synchronized to a common clock (record the synchronization latency; measure it, do not assume zero):

- **Ephys:** spike times and counts (ground truth), with sortable waveform quality.
- **GECI channel:** ΔF/F from the somatic ROI and, where resolvable, spine ROIs.
- **Structural channel:** per-ROI brightness for motion/expression normalization.
- **3D motion estimate:** lateral displacement from image registration and **axial (z) displacement** estimated from the structural channel (e.g., via an axial point-spread-function model, a reference z-stack, or a dedicated axial-tracking readout). Axial drift is explicitly logged because it changes fluorescence without calcium change and is invisible to purely 2D registration.
- **Indicator kinetics (per cell):** from isolated single-spike-triggered fluorescence transients, fit rise time, decay time, and peak amplitude. These per-cell kinetics feed the transfer-function model and the saturation assessment.
- **Expression metric** (Stage 1) per cell.
- **Visual tuning:** stimulus-locked response amplitude for both fluorescence and ephys.

### Stage 6 — Controls (one per named artefact)

| Artefact (from evidence) | Control / measurement | Quantity produced |
|---|---|---|
| Movement, focus drift | 3D motion estimation + structural-channel regression; reject or correct frames beyond motion bounds | Residual motion-correlated fluorescence after correction |
| Axial drift specifically | Independent z-tracking from structural channel | Fraction of ΔF/F explained by z-displacement |
| Background / neuropil contamination | Neuropil-subtraction with a calibrated coefficient; **neuropil sensitivity sweep** (see below) | False-positive rate vs neuropil coefficient |
| Indicator kinetics | Per-cell kinetic fit (Stage 5) | Rise/decay constants used in deconvolution |
| Saturation | Amplitude–rate fit across high-count epoch; expression covariate | Onset of nonlinearity / saturation point |
| Expression-dependent gain | Expression metric as covariate | Transfer-function shift vs expression |
| Behaviour-related false signals | Motion-challenge epoch with ephys | Behaviour-correlated signals that are NOT real spikes |

**Neuropil contamination sensitivity (explicit):** rather than fixing a single neuropil subtraction coefficient, **sweep** the coefficient across a plausible range and measure how detection sensitivity and false-positive rate (both scored against ephys) change. Report the coefficient value, the rule used to choose it (e.g., the value that minimizes false positives in the quiet baseline epoch while retaining ephys-confirmed single-spike events), and the sensitivity of all downstream conclusions to that choice. This directly operationalizes "neuropil contamination sensitivity."

### Stage 7 — Analysis

1. **Motion/structural correction first.** Apply 3D motion correction; regress structural-channel fluctuations out of the GECI trace. Flag and exclude epochs where residual motion correlation with the GECI signal exceeds a pre-set bound. Report the fraction of data excluded.

2. **Neuropil subtraction** with the swept-and-selected coefficient (Stage 6).

3. **Event detection / spike inference**, blinded to ephys. Use a deconvolution or event-detection model parameterized by the **per-cell measured kinetics**. The detection threshold is set by a calibration rule tied to the quiet-baseline noise and false-positive target, not an arbitrary constant.

4. **Transfer-function fit (core deliverable):** relate inferred/true quantities using the paired ephys:
   - Fluorescence amplitude (and integrated transient) vs ephys spike count, fit as a **nonlinear, saturating** function, with **expression metric and cell type as covariates**. Report the slope in the linear regime, the saturation onset, and how both shift with expression.
   - Report this as a distribution with confidence intervals, not a single gain.

5. **Detection and false-positive scoring (against ephys):**
   - **Detection sensitivity:** fraction of ephys spikes/events correctly detected, as a function of true spike count (expect low single-spike sensitivity, rising with count — report the curve).
   - **Temporal precision:** distribution of detected-event timing error relative to ephys spikes.
   - **False-positive rate:** rate of detected "events" with no corresponding ephys spike, reported separately for quiet baseline, visual, and motion-challenge epochs. The motion-challenge false-positive rate is the key number demonstrating control of behaviour-related false signals.
   - Provide ROC-style curves (sensitivity vs false-positive rate) across detection thresholds so users can pick an operating point.

6. **Visual-response validation:** compare stimulus tuning derived from inferred spikes vs from ephys spikes for the same cells (agreement of preferred stimulus, response reliability). For dendritic-spine signals, because no spine-level ephys ground truth exists, validate indirectly: show spine responses survive all corrections and report that spine-level claims rest on somatic calibration plus correction controls, **explicitly flagged as not independently ground-truthed at the spine**.

7. **Uncertainty propagation:** carry the transfer-function confidence intervals into any downstream firing-rate estimate, so inferred rates come with error bars reflecting kinetics, saturation, and expression ambiguity.

### Stage 8 — Acceptance / stopping criteria

Pre-register these (illustrative structure; **numeric thresholds set from the pilot, not invented**):

- **Minimum ground-truth quality:** only cells meeting the pre-set seal/waveform and same-cell-correspondence criteria enter calibration.
- **Motion acceptance:** after correction, residual fraction of ΔF/F variance explained by 3D motion must be below a pre-registered bound; otherwise the epoch is excluded and reported.
- **False-positive ceiling:** define the maximum acceptable false-positive rate at the chosen operating point (e.g., set so that visual-tuning conclusions are not driven by motion artefact; justify with the motion-challenge data).
- **Calibration precision:** stop collecting once the amplitude–rate slope and the single-spike detection sensitivity are estimated to the pre-set confidence-interval width (this defines n, from Stage 2 pilot).
- **Validity-domain statement (mandatory output):** the transfer function is reported together with the range of cell type, expression metric, firing rate, and imaging rate over which it was calibrated. Use outside that range is flagged as extrapolation.
- **Go/no-go:** if, after correction, behaviour-correlated false signals cannot be reduced below the ceiling, the conclusion is that the indicator/pipeline cannot reliably support single-cell spike inference under motion in this cell type — report that honestly rather than loosening thresholds.

### Stage 9 — Troubleshooting

- **High false positives in motion-challenge:** increase z-tracking resolution; verify the structural fluorophore is truly calcium-insensitive and co-localized; tighten motion rejection; re-examine neuropil coefficient. If false positives persist only during locomotion, restrict quantitative spike claims to quiescent epochs and report the restriction.
- **Poor single-spike detection:** likely frame rate too low relative to measured rise time (revisit Stage 0 Nyquist calibration) or low expression/SNR. Re-check expression metric; do not compensate by lowering threshold without re-measuring false positives.
- **Transfer function varies strongly with expression:** report the expression-conditioned family of functions and narrow the inclusion window; this is an expected finding given the evidence, not a failure.
- **Saturation reached at modest spike counts:** report the saturation onset explicitly; firing-rate inference is only valid below it. High-count epochs then yield only "≥ saturation" statements.
- **Ephys perturbs firing:** prefer spontaneous spikes for calibration; use evoked spikes only to populate the high-count tail and check that the transfer function derived from spontaneous vs evoked spikes agrees.
- **Structural channel bleeds into GECI channel or vice versa:** measure crosstalk with single-labeled controls and correct; unmeasured crosstalk would corrupt both expression and motion normalization.

---

## Alternatives considered

- **Population-level correlation with behaviour instead of paired single-cell ephys.** Rejected as the primary standard: the evidence explicitly warns that behaviour-correlated signals can be false, so behaviour correlation cannot validate spike inference. Paired ephys is necessary.
- **Fixed neuropil coefficient from literature.** Rejected: the coefficient interacts with the false-positive rate and depends on local tissue/expression; hence the sensitivity sweep.
- **Single scalar fluorescence-per-spike gain.** Rejected per the saturation/expression/kinetics evidence; replaced by a covariate-conditioned nonlinear function with uncertainty.
- **2D-only motion correction.** Rejected: axial drift changes fluorescence invisibly to 2D registration; hence explicit 3D/z tracking from the structural channel.
- **Cross-cell-type transfer-function reuse.** Rejected as default per the non-extrapolation constraint; allowed only as a separately validated, flagged inference.

---

## Limits of this protocol

- **Dendritic-spine calibration lacks direct ground truth.** No electrode measures spine-local calcium spikes directly in this design; spine claims inherit somatic calibration plus correction controls and must be reported as such.
- **Current injection / optogenetic drive to populate high spike counts is itself perturbing** and may not reproduce natural spike timing; cross-checking spontaneous vs evoked transfer functions partially mitigates this.
- **The structural fluorophore must be genuinely activity-independent and co-expressed**; if it reports anything calcium-related or has different bleaching, the motion/expression denominator is biased. This assumption should be independently verified.
- **Synchronization latency between ephys and imaging** must be measured, not assumed zero, or temporal-precision estimates are biased.
- **All numeric thresholds, sample sizes, frame rates, and spike-count ranges are deferred to pilot calibration**, consistent with the packet stating these are unavailable; the protocol specifies the *procedure* to fix each, not a fabricated value.
- **Validity domain is intrinsically narrow:** results license spike inference only within the calibrated cell type, expression range, firing-rate range (below saturation), and imaging configuration.

---

## What would change the recommendation

- If the structural reference channel proves not to be activity-independent, the entire motion/expression normalization strategy must be redesigned (e.g., using interleaved reference imaging or a different static marker).
- If motion-challenge false positives cannot be brought below the ceiling, the conclusion shifts from "calibrated spike inference" to "qualitative activity detection only," restricted to quiescent epochs.
- If the transfer function proves insensitive to expression within the achievable range, the expression inclusion window can be relaxed, improving yield.
- If the measured indicator kinetics are slow relative to achievable frame rates, single-spike inference may be abandoned in favor of calibrated firing-rate (multi-spike) inference, with the detection-sensitivity curve defining the smallest resolvable event.

This protocol operationalizes every artefact and limit named in the evidence packet into a specific proposed control, scores all inference against simultaneous electrophysiological ground truth, and reports the calibration as a conditional, uncertainty-bounded transfer function with an explicit validity domain — rather than as an error-free spike readout.
