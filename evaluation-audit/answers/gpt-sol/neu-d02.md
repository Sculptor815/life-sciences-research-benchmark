# GPT-5.6 Sol / neu-d02

Original final answer, shared by both scoring rounds.

# Proposed calibration and validation protocol

## Recommended approach

**All experiments, analyses, criteria, and controls below are proposed; no results are asserted.**

Calibrate the indicator in the **intended target cell type** using fluorescence and electrophysiology recorded simultaneously from the same cell. Use electrophysiologically verified spike counts—including zero-spike periods and experimentally evoked known-count trains—to estimate indicator kinetics, count dependence, saturation, and an event detector. Then lock the acquisition settings and analysis pipeline and test them in separate, held-out animals with natural and visually evoked activity.

A simultaneous activity-independent structural channel should be used to estimate three-dimensional motion, but not as a substitute for electrophysiological ground truth. Validation should report sensitivity, precision, false-positive rates, spike-count error, and visual-response concordance as functions of motion, neuropil contamination, expression level, and firing pattern. If performance is not robust to plausible neuropil corrections or expression strata, the conclusion should be restricted to the validated conditions rather than generalized.

---

## 1. Evidence-to-inference-to-conclusion chain

| Evidence location in the supplied packet | Inference | Protocol consequence |
|---|---|---|
| Source summary: the indicator improves activity detection and reports somatic and dendritic-spine visual-related signals. | Visual-response performance is relevant, but reported fluorescence must be compared with actual firing. | Include synchronized visual stimulation, trial-by-trial electrophysiology, and optical response tracking. Treat somatic and spine claims separately. |
| Figure-caption summary: simultaneous imaging and electrophysiology calibration was reported. | Same-cell paired recordings are an appropriate calibration design. | Pair every primary fluorescence trace with simultaneous electrophysiological spikes from the same cell. |
| Stated limit: fluorescence reflects calcium dynamics shaped by the indicator and imaging system, not instantaneous error-free spikes. | A fixed amplitude-to-spike rule cannot be assumed. | Empirically measure the impulse response, kinetics, history dependence, count response, saturation, and timing uncertainty. |
| Stated limit: calibration in one cell type cannot be unconditionally extrapolated. | Calibration must be cell-type specific. | Perform known-spike calibration and independent validation in the intended target cell type; limit conclusions to that type and preparation. |
| Artefact summary: movement, focus drift, background, and neuropil can produce behavior-related false signals. | Apparent visual or behavioral responses may not originate from target-cell firing. | Add a structural reference channel, three-dimensional registration, movement tracking, neuropil-only ROIs, blank visual trials, and zero-spike false-positive analyses. |
| Artefact summary: kinetics, saturation, and expression can cause the same fluorescence amplitude to correspond to different firing. | Performance may vary across firing patterns and expression levels. | Calibrate multiple spike counts and intervals, test for saturation, quantify expression proxies, and report stratified performance. |
| Hypothetical constraints: indicator, electrophysiology, structural channel, visual stimulation, and controls are available, but identity, expression, rates, spike numbers, and thresholds are unknown. | Numerical acquisition and analysis settings cannot be imported or invented. | Determine them in a designated calibration phase and lock them before held-out validation. |

**Conclusion:** the indicator should be accepted for spike or visual-response inference only over the cell type, expression range, firing range, imaging conditions, and motion/neuropil conditions directly supported by paired held-out validation.

---

# 2. Objectives and estimands

## Proposed primary objectives

1. Estimate the relationship between fluorescence and electrophysiologically verified spike count in the target cell type.
2. Measure detection sensitivity and false-positive rates for optical activity events.
3. Determine whether fluorescence preserves trial-by-trial and condition-dependent visual responses measured electrophysiologically.
4. Quantify sensitivity to three-dimensional motion, neuropil contamination, expression level, indicator kinetics, and saturation.

## Proposed primary unit and ground truth

- **Biological independent unit:** animal.
- **Nested units:** recorded cells within animal and repeated trials within cell.
- **Primary paired unit:** a time interval from one imaged cell with simultaneous electrophysiological spike count from that same cell.
- Trials should not be treated as independent biological replicates.
- Electrophysiology is the spike ground truth; the structural channel is a motion and morphology reference only.

## Proposed performance outputs

- Sensitivity/recall by verified spike count and firing pattern.
- Precision or positive predictive value.
- False-positive events per unit time during verified zero-spike periods.
- False-positive probability per zero-spike analysis window.
- Spike-count bias and absolute error.
- Timing error relative to the measured calcium response, not an assumption of instantaneous reporting.
- Calibration curve: inferred versus observed spike count, with uncertainty.
- Visual-response concordance, including optical false visual responses when electrophysiology shows no response.
- Performance stratified by animal, cell, expression level, depth, motion, neuropil signal, and visual/behavioral state.

---

# 3. Ordered proposed protocol

## Phase A — Preparation and quality checks

### A1. Define the intended claim

Before collecting validation data, specify whether the indicator is intended to support:

- binary detection of one or more spikes;
- approximate spike-count inference;
- trial-by-trial visual-response detection;
- visual tuning or response-amplitude estimation; or
- only detection of broad activity epochs.

The acceptance metrics should match this claim. Failure of spike-count calibration would not necessarily preclude broad activity detection, but the claim must then be narrowed.

### A2. Confirm target-cell identity

Use the available targeting strategy and proposed post-recording morphology or cell-type marker confirmation. Prespecify how ambiguous cells will be handled. Exclude or separately report cells whose identity cannot be confirmed.

Because cell-type extrapolation is unsupported, do not pool other cell types into the primary analysis.

### A3. Establish the structural reference channel

The proposed structural reference should be activity-independent over the measurement period. Before use:

1. Acquire indicator-only and structural-channel-only controls to measure spectral bleed-through.
2. Test whether visual stimulation or known spikes alter the structural signal.
3. Measure structural-channel bleaching and shot/background noise.
4. Verify that the structural signal provides enough stable landmarks for lateral and axial registration.

If the structural channel is activity-modulated or contaminated by indicator fluorescence, use it only after quantified correction or replace it with an alternative structural label.

### A4. Synchronization

Record imaging frame or volume times, electrophysiology, current-command timing, visual stimulus identity and onset, and available movement signals on a common clock. Use proposed synchronization pulses to measure and correct fixed offsets and drift.

### A5. Electrophysiology quality

Prespecify session-level criteria for:

- reliable spike discrimination above noise;
- stable recording configuration;
- acceptable access or seal stability, as applicable;
- lack of progressive changes suggesting cell damage;
- verified delivery of commanded spike counts.

Thresholds are unreported and should be set from instrument noise and an independent pilot, then locked. Periods failing electrophysiology criteria should not be used as ground truth.

### A6. Imaging-setting calibration

Because imaging rate, power, and indicator identity are unreported, test proposed candidate settings in calibration animals:

- Select frame or volume rates that recover the measured rise and decay dynamics while preserving adequate signal quality.
- Increase illumination only within a range that does not produce unacceptable bleaching, saturation, or evidence of damage.
- Record detector gain, optical power, depth, field size, and sampling rate for every session.
- Acquire dark/background measurements and pre/post-session reference images.

Do not choose settings by performance in validation animals.

---

## Phase B — Independent units, allocation, and blinding

### B1. Dataset allocation

Prospectively allocate entire animals to:

1. **Calibration/training set:** selection of imaging settings, neuropil correction, kinetic model, detector, thresholds, and analysis windows.
2. **Held-out validation set:** unchanged application of the locked pipeline.

Holding out whole animals is preferred because cells from the same animal are not fully independent. If animal numbers prevent this, leave-one-animal-out analysis may be proposed but should be identified as weaker validation.

### B2. Sample size

Use calibration data to estimate between-animal and between-cell variability. Select the validation sample size to achieve prespecified precision for the principal sensitivity and false-positive estimates, accounting for cells nested within animals. Do not stop when favorable performance is reached.

### B3. Randomization

Within calibration and validation sessions, randomize or counterbalance:

- visual stimulus order, including blank trials;
- known spike-count and spike-interval conditions;
- spontaneous, visual, and stimulation blocks where technically feasible;
- acquisition settings if more than one locked setting is being compared.

### B4. Blinding

- The fluorescence-event analyst should be blinded to electrophysiological spikes and, where possible, stimulus identity until optical calls are locked.
- Electrophysiology quality and spike detection should be assessed without viewing the fluorescence trace.
- Manual ROI or cell-quality adjudication should be blinded to performance outcomes.
- After independent processing, pair the optical and electrophysiological records by synchronized time.

---

## Phase C — Expression-level and baseline checks

For each proposed cell:

1. Measure background-subtracted baseline indicator fluorescence under standardized acquisition settings.
2. Record depth, illumination, detector settings, ROI size, and local background.
3. Measure structural-channel intensity separately; do not assume that it is a stoichiometric expression measure unless that relationship is independently established.
4. Quantify bleaching and baseline drift during the session.
5. Inspect morphology and baseline fluorescence for aggregation, compartmental abnormalities, or saturation.
6. Measure electrophysiological health and firing properties consistently across expression strata.
7. If feasible, propose post hoc indicator quantification as an independent expression measure.

Define low, intermediate, and high expression strata from a prespecified assay or the calibration distribution, without using validation performance to choose boundaries. If expression cannot be measured directly, label baseline fluorescence as an optical expression proxy and retain the confounding by depth and optics as a limitation.

A proposed matched comparison with non-indicator-expressing target cells may be used to assess whether expression is associated with altered electrophysiological properties, although those cells cannot contribute to optical detection validation.

---

## Phase D — Paired interventions and sampling

### D1. Known spike-count calibration in the target cell type

In calibration animals, propose simultaneous imaging and current-clamp or other suitable electrophysiological stimulation of the imaged target cell.

1. Begin with verified zero-spike commands.
2. Test isolated spikes to estimate the single-spike fluorescence response where detectable.
3. Adaptively add larger spike counts and multiple interspike intervals.
4. Randomize conditions and repeat each sufficiently to estimate variability.
5. Continue only through a physiologically and technically acceptable firing range.
6. Count actual spikes from electrophysiology rather than assuming that a command generated the intended count.
7. Label failures to evoke the commanded count and analyze them according to observed count.
8. Stop increasing count when fluorescence or detector saturation is detected, the cell becomes unstable, or the predefined physiological range is reached.

No particular spike counts or frequencies should be invented in advance; calibration should identify a range spanning zero, the detection boundary, the approximately count-sensitive region, and the onset of saturation.

### D2. Natural spontaneous and visually evoked validation

In both phases, and especially held-out validation, propose blocks of:

- spontaneous activity;
- randomized visual stimuli;
- interleaved blank or no-stimulus trials;
- repeated presentations of each visual condition;
- available movement conditions or naturally occurring movement states.

Track stimulus identity, onset, duration, and each available movement variable, such as locomotor or ocular measurements if those are the supplied movement controls. The exact movement modality is unreported and should be documented rather than assumed.

Natural visually evoked validation should preferentially use a minimally perturbative paired electrophysiological mode where feasible. This avoids making all validation depend on current injection.

### D3. Behavior-related false-signal sampling

Deliberately retain epochs with:

- movement but no electrophysiological spikes;
- visual presentation but no electrophysiological response;
- large structural-channel displacement;
- elevated neuropil signal with absent target-cell spikes;
- blank visual trials.

These epochs are necessary for estimating behavior-related false positives and should not all be removed as artefact before analysis.

---

## Phase E — Three-dimensional motion measurement

### E1. Reference data

Acquire a proposed three-dimensional structural reference stack around the imaging plane before each recording and again afterward. If simultaneous volumetric structural acquisition is feasible, use it; otherwise compare each time point with the reference stack.

### E2. Motion estimation

Estimate, for every frame or volume:

- lateral displacement in \(x\) and \(y\);
- axial displacement in \(z\);
- registration confidence or residual landmark error.

Use the structural rather than activity channel for the primary registration transform. Apply the same spatial transform to the indicator data.

### E3. Registration validation

Propose known computational or stage-displacement tests to determine the range over which \(x,y,z\) shifts can be recovered. Choose residual-motion exclusion limits from these calibration tests and lock them before validation.

Report performance both:

- after the locked motion correction; and
- stratified by residual motion magnitude.

Do not interpolate missing optical events and count them as detected spikes. Frames outside the validated registration range should be marked unavailable, and the amount of unavailable time reported.

---

## Phase F — Neuropil and background controls

For each somatic ROI, define proposed surrounding neuropil ROIs that exclude the target soma, nearby somata, vessels, and structurally identified processes where possible. Also include matched neuropil-only and shifted-control ROIs.

Let the corrected trace be evaluated as a family of candidate corrections rather than assuming a subtraction coefficient:

\[
F_{\mathrm{corrected}} = F_{\mathrm{soma}}-\alpha F_{\mathrm{neuropil}}.
\]

Determine the primary \(\alpha\), if used, only in calibration data, using zero-spike and background epochs plus paired electrophysiology. Then lock it for validation.

Required sensitivity analyses should include:

- no neuropil subtraction;
- the locked correction;
- a prespecified range of plausible correction strengths;
- alternative neuropil ROI geometries;
- performance during high versus low neuropil activity;
- performance during movement with verified zero spikes.

Neuropil subtraction can remove genuine correlated signal as well as contamination. Therefore, robustness across plausible corrections is more informative than selecting the correction that maximizes agreement in the validation data.

---

# 4. Proposed analysis

## 4.1 Fluorescence processing

Apply a locked sequence:

1. background correction;
2. structural-channel three-dimensional registration;
3. ROI extraction;
4. bleaching or baseline-drift correction chosen in calibration;
5. neuropil correction;
6. conversion to the prespecified fluorescence measure;
7. event detection or spike-count inference.

Preserve raw and intermediate traces for audit. Avoid filters that use future electrophysiological or stimulus information.

## 4.2 Kinetic and spike-count model

Using calibration cells only:

- Estimate the rise, peak delay, and decay from isolated or sufficiently separated verified spikes.
- Test whether response amplitude or integrated signal varies with spike count.
- Test dependence on interspike interval and recent activity.
- Identify detector or indicator saturation.
- Compare candidate models, such as threshold detection versus kinetic deconvolution, using animal-level cross-validation.
- Select one primary model and lock all parameters.

If a unique spike count cannot be recovered because different firing patterns produce overlapping fluorescence, report probabilistic count intervals or binary activity detection rather than forced exact counts.

## 4.3 Event matching

Define optical event windows from the empirically measured kinetics, not from an assumed instantaneous response. Use a prespecified one-to-one matching rule so that one broad calcium transient cannot be credited as multiple correctly detected events without justification.

Zero-spike windows should be electrophysiologically confirmed and long enough to accommodate the measured response decay from earlier spikes.

## 4.4 Detection and false-positive reporting

For the held-out set, report:

- true positives, false positives, false negatives, and true negatives under the locked definitions;
- sensitivity by observed spike count;
- precision;
- false-positive events per recorded zero-spike time;
- false-positive probability per zero-spike window;
- count bias and absolute error;
- timing uncertainty;
- performance with and without high-motion epochs;
- performance across neuropil and expression strata.

Provide animal-level estimates and uncertainty that respects nesting. Do not report only pooled trial counts.

## 4.5 Visual-response tracking

Define electrophysiological visual responsiveness with a prespecified test comparing stimulus and baseline or blank trials. Apply an analogous locked optical analysis.

Compare:

- classification of responsive versus nonresponsive cells;
- trial-by-trial response detection;
- response amplitude across visual conditions;
- preferred-condition or tuning estimates, if that is an intended use;
- false optical visual responses in electrophysiologically nonresponsive trials or cells;
- response estimates after stratification by movement and neuropil signal.

Stimulus-locked fluorescence without paired spiking should be reported as an optical response, not automatically as neural firing.

## 4.6 Expression and artefact sensitivity

Model or stratify performance by:

- expression proxy;
- imaging depth and settings;
- baseline brightness;
- bleaching;
- \(x,y,z\) motion;
- registration residual;
- neuropil amplitude and correction strength;
- visual and movement state;
- firing rate and recent spike history.

If expression substantially changes the fluorescence-to-spike mapping, either restrict use to a validated expression range or lock an expression-aware model and validate it independently.

---

# 5. Proposed acceptance and stopping criteria

## Acceptance criteria

Numerical thresholds are unavailable in the evidence packet and should not be invented. Before held-out validation, investigators should specify application-relevant numerical minima or maxima for:

- sensitivity at the spike counts of interest;
- false positives per unit zero-spike time;
- precision;
- acceptable spike-count error;
- visual-response concordance;
- tolerated performance loss across expression strata;
- tolerated performance loss across the validated motion and neuropil ranges.

Acceptance should require that the relevant uncertainty bound, not just the point estimate, meets each primary criterion. The validation set must also show:

1. usable paired ground truth from the intended target cell type;
2. no unmodeled detector saturation in the claimed range;
3. acceptable registration within the declared motion range;
4. performance robust to the prespecified neuropil sensitivity analysis;
5. no unacceptable excess of optical events during movement-associated zero-spike periods;
6. expression levels within the validated range;
7. no retuning after validation labels are revealed.

If only binary activity detection meets criteria, do not claim validated spike-count inference.

## Session stopping criteria

A proposed session should stop or be marked invalid if:

- electrophysiological spike identification becomes unreliable;
- seal/access or cell health crosses its locked limit;
- synchronization fails;
- fluorescence or detector saturation prevents quantification;
- bleaching or focus drift exceeds calibrated correction limits;
- three-dimensional displacement leaves the validated registration range;
- structural-channel integrity fails;
- visual stimulus or movement timestamps are unavailable.

## Study stopping rules

Complete the prospectively planned sample unless stopping is required for safety, feasibility, or pervasive technical failure. Do not stop early for favorable accuracy. If widespread failure reveals that the imaging rate, expression range, or analysis is unsuitable, revise the method using calibration animals and start a new, independently held-out validation cohort.

---

# 6. Troubleshooting and decision paths

| Observation | Proposed diagnostic | Proposed response |
|---|---|---|
| Fluorescence events occur during movement but no spikes are present. | Examine structural \(x,y,z\) displacement, registration residuals, neuropil ROIs, and background. | Improve registration or restrict the validated motion range; revise neuropil handling in calibration and obtain a new validation set. |
| Same spike count gives different amplitudes across cells. | Stratify by expression proxy, depth, illumination, neuropil, and recent firing. | Standardize acquisition, restrict expression range, or validate an expression-aware probabilistic model. |
| Large responses stop increasing with spike count. | Check detector clipping and indicator saturation separately. | Reduce gain/power if detector-limited; otherwise limit count inference below the empirically identified saturation range. |
| Single spikes are often missed but bursts are reliable. | Inspect single-spike signal distribution and imaging rate. | Restrict the claim to multi-spike or activity-epoch detection unless settings can be recalibrated and independently revalidated. |
| Neuropil correction changes visual tuning. | Compare no correction, locked correction, alternative annuli, and electrophysiology. | Report sensitivity and avoid tuning claims if the conclusion is not robust. |
| Structural reference changes with neural activity. | Use single-channel controls and spike-triggered structural averages. | Correct quantified bleed-through or use another structural reference. |
| Calibration works but held-out performance falls. | Examine animal, expression, depth, motion, and firing-pattern shifts. | Treat calibration as non-generalizing; redesign and repeat independent validation rather than retuning on the failed set. |

---

# 7. Alternatives and important limits

- **Electrophysiology mode:** whole-cell current injection is useful for known-count calibration but may perturb the cell. A proposed minimally perturbative cell-attached or equivalent configuration is preferable for natural visual-response validation where feasible.
- **Motion reference:** simultaneous volumetric structural imaging is preferable for direct \(z\)-tracking. A reference stack with frame-to-stack registration is an alternative but may be less reliable during deformation.
- **Event model:** threshold detection is simpler and auditable; kinetic deconvolution may improve temporal and count estimates but requires stronger assumptions. Either should be selected only in calibration and then locked.
- **Dendrites and spines:** somatic electrophysiological spikes are not complete ground truth for local spine calcium or local synaptic events. If spine signals are included, the proposed analysis should report their association with somatic firing and visual stimulation, not claim validated local spike inference without an appropriate local ground truth.
- **Generalization:** validation applies only to the tested target cell type, expression range, firing patterns, imaging settings, preparation, and motion/neuropil range. A different cell type or substantially different acquisition system requires new calibration.
- **Intrinsic limitation:** even after successful validation, fluorescence remains a delayed and potentially nonlinear report of calcium dynamics. It should be presented as a calibrated probabilistic proxy for activity, not as error-free instantaneous spike measurement.
