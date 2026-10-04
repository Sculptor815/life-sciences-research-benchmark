# Kimi K3 / neu-d02

Original final answer, shared by both scoring rounds.

## Recommended next action

Run a **proposed, paired within-subject calibration**: in the **same target cell type, same trials, same clock**, record high-bandwidth electrophysiology for spike times/counts while imaging the calcium indicator and a static structural channel during controlled visual stimuli and motion/neuropil challenges. Estimate 3D motion from the structural reference, model neuropil/background as explicit nuisance terms, titrate expression and laser power, and build a spike-count-to-fluorescence calibration only from calibration cells. Validate detectors and deconvolution on held-out neurons/animals with electrophysiology labels hidden, then report sensitivity, precision/F1 or AUPRC, false positives per minute under motion/behavior, lead/lag, minimum detectable spike count, saturation limits, and confidence intervals by hierarchical bootstrap. Do **not** interpret ΔF/F amplitude as “spikes” outside the calibrated target type and operating range.

All experiments, thresholds, spike numbers, imaging rates, expression levels, and analysis settings below are **proposed and must be calibrated**; none are reported results.

---

## Evidence → inference → conclusion chain

**Evidence packet, as summarized:** the indicator improves activity detection and reports somatic and dendritic-spine visual-related signals; figure captions state simultaneous imaging and electrophysiology calibration. The stated limits are that fluorescence reflects calcium dynamics shaped by indicator and imaging system, not error-free instantaneous spikes; movement, focus drift, background and neuropil can create behaviour-related false signals; kinetics, saturation and expression can make the same fluorescence amplitude correspond to different firing; and calibration in one cell type cannot be unconditionally extrapolated.

**Inference:** because visual soma/spine signals exist and paired imaging–electrophysiology is feasible, a ground-truth calibration is possible. But because the mapping is filtered, nonlinear, expression-dependent and contamination-prone, fluorescence must be treated as a noisy, convolutionally distorted, motion-corrupted measurement of spiking, not as spike identity.

**Conclusion:** the protocol must estimate the transfer function and error modes directly in the target cell type, using paired spike times, structural motion tracking, neuropil sensitivity analysis, expression/saturation checks, and held-out validation with explicit false-positive reporting. Any extrapolation to other cell types, brain states, indicators, imaging rates, or expression levels requires recalibration or a formal transportability test.

---

## Signal model and concept relationships

Model each region of interest as:

\[
F(t)=F_0 + a\,[k * S](t)+ c\,N(t)+ d\,B(t)+ M(x,y,z,t)+ \epsilon(t)
\]

where \(S\) is the spike train, \(k\) is the indicator calcium kernel, \(N\) is neuropil/out-of-focus fluorescence, \(B\) is background/hemodynamic/vascular shading where relevant, \(M\) is 3D motion/focus artifact, and \(\epsilon\) is photon/electronic noise.  
Observed ΔF/F is not \(S\); it is \(S\) after indicator kinetics, sampling, saturation, motion, segmentation and contamination. Structural reference estimates \(M\); electrophysiology supplies \(S\); visual stimulation supplies repeatable, graded drive; controls estimate \(N,B,M\).

---

# Operational ordered protocol — all proposed

## 1. Preparation and quality checks

**[P1.1 Target cell definition and pairing plan]**  
Define the target cell type genetically/anatomically before calibration. Use cell-attached/juxtacellular recording for in vivo spike times when minimal perturbation is required; use whole-cell only when current injection, voltage control or morphology is essential and after quantifying how dialysis changes calcium/ephys properties. Simultaneously image the indicator and a spectrally separated structural reference channel. Use a common clock/TTL for stimulus, imaging frames, piezo/z position, ephys, behavior and movement sensors; measure synchronization jitter and correct timestamps.

**[P1.2 Optical/channel calibration]**  
Before animals, calibrate: pixel size, stage/piezo z scale, field flatness, laser power stability, detector linearity, spectral bleedthrough/unmixing matrix using single-fluorophore controls, chromatic shift between functional and structural channels, and 3D point-spread function using beads or subresolution objects. Establish a dark-noise and background map. Record objective immersion, wavelength, power at sample, dwell time/frame rate, gain/offset and filters for every session.

**[P1.3 Health/expression baseline]**  
Before imaging, screen cells for resting fluorescence, morphology in structural channel, membrane/access properties where patched, spontaneous spike rate in cell-attached mode, visual responsiveness, bleb formation, and photodamage. Exclude or flag unhealthy cells using pre-specified criteria set from pilots; do not let exclusion depend on final calibration outcome.

**[P1.4 Pilot calibration of unknowns]**  
Because exact indicator identity, expression, spike numbers, imaging rates and thresholds are unavailable, run pilots to estimate: resting F0 distribution; indicator rise/decay after confirmed single spikes and brief bursts; linear range and saturation using increasing confirmed spike counts; frame-rate aliasing by acquiring the same cells at multiple rates or using interleaved high-rate snippets; motion amplitude during behavior; neuropil gradients around somata/spines; and achievable signal-to-noise. Use pilots only to set operating ranges and sample-size precision targets, not to tune final claims.

## 2. Independent units and experimental design

**[P2.1 Units of inference]**  
Primary unit: individual neuron. Hierarchical levels: trial/event < ROI/spine/soma < neuron < field of view < session < animal. Do not treat repeated trials or multiple ROIs from one cell as independent biological replicates. For spines, treat parent dendrite/cell as a clustering variable.

**[P2.2 Calibration/validation split]**  
Split by held-out neurons and held-out animals, and where possible held-out sessions/days: e.g., calibration set for kernel/threshold/neuropil coefficients; validation set untouched until final evaluation. Use nested cross-validation for model selection and a final locked evaluation. Report performance with leave-one-animal-out to test generalization across animals.

**[P2.3 Allocation, randomization and blinding]**  
Randomize stimulus order, motion/behavior blocks, laser-power/expression conditions where feasible, and cell selection among eligible cells. Balance visual stimulus parameters across expression and motion strata. Analysts optimizing segmentation/detection must be blind to ephys spike times except in a labeled training subset; final evaluators run a frozen pipeline on held-out data. Unblind only after acceptance criteria are applied.

## 3. Intervention and sampling

**[P3.1 Visual-response tracking]**  
Deliver controlled visual stimuli spanning the relevant feature space: oriented/direction-selective gratings or appropriate naturalistic stimuli, multiple contrasts/luminances, spatial/temporal frequencies, sizes, blank/gray periods, and repeats. Track pupil/eye position, locomotion, whisking/body movement and relevant behavior. Include stimulus-triggered, spontaneous, running-vs-stationary and eye-movement-stratified analyses. Measure response latency, reliability, receptive-field/tuning estimates and trial-to-trial variability alongside fluorescence.

**[P3.2 Known spike-count calibration in the target type]**  
Obtain paired ground truth from the same neurons. Use cell-attached recordings to count spikes without changing intracellular calcium where possible; add whole-cell current injection in slice or in vivo only as a perturbation-checked complement. Deliver or elicit confirmed patterns: single spikes, isolated spike doublets/triplets, short bursts, and sustained trains across physiologic firing ranges, interleaved with blanks. Randomize timing relative to visual stimuli. Ensure every fluorescence event candidate has synchronized ephys labels; reject epochs with ambiguous spike sorting/seal instability.

**[P3.3 Motion and neuropil challenge blocks]**  
Induce or sample controlled 3D motion: passive z displacement via piezo, small x/y translations, natural locomotion/air-puff/startle if ethically approved, and focus ramp. Include bead-phantom or tissue-phantom motion to validate registration before animal interpretation. For neuropil, image somata, dendritic segments, spines and nearby neuropil annuli, blood vessels and background regions during blank and stimulated conditions.

**[P3.4 Expression and dose/sampling checks]**  
Across cells or controlled expression cohorts, quantify indicator expression by resting indicator fluorescence normalized to structural marker, brightness/lifetime if available, and post hoc confirmation where feasible. Vary acquisition power/frame rate in calibrated steps to estimate photobleaching, phototoxicity and detector/indicator saturation. Keep exposure within a pre-set photodamage budget defined by stable ephys and morphology.

## 4. Measurements

Acquire: functional indicator channel; static structural reference channel; synchronized ephys voltage/current with spike times and waveform quality; stimulus identity/timing; eye/pupil/locomotion/body motion; piezo/z position; laser power and detector settings; dark/background frames; and post hoc anatomy/cell identity. For spines, record parent dendrite and local neuropil. Save raw data before registration/subtraction plus all transforms.

Minimum metadata: animal/cell ID, target-type evidence, depth, coordinates, expression proxy, F0, laser power, frame/volume rate, z-step, motion estimates, neuropil coefficient, saturation flags, ephys mode/quality, exclusion reason.

## 5. Controls

- **Paired positive control:** confirmed spike/burst produces fluorescence transient within kernel latency in same cell.  
- **Blank/negative control:** gray/no-stimulus and no-spike epochs estimate false event rate.  
- **Motion control:** structural-channel motion intentionally induced with ephys-confirmed no-spike epochs; functional false transients quantify artifact.  
- **Neuropil control:** annulus/local neuropil, blood-vessel and off-cell background measured simultaneously; sensitivity to subtraction coefficient reported.  
- **Bleedthrough/unmixing control:** single-color samples or expression-negative tissue.  
- **Saturation control:** increasing confirmed spike counts or strong visual drive to find plateau/nonlinearity.  
- **Expression control:** low/medium/high expression proxy strata; overexpression toxicity flagged by ephys/morphology.  
- **Indicator-independent control where feasible:** membrane voltage or extracellular spike signal remains stable across imaging exposure.  
- **Order/carryover control:** randomized blocks and washout/blank intervals test adaptation, bleaching and state drift.

## 6. Analysis

**[P6.1 Preprocessing with provenance]**  
Work on raw functional and structural stacks. Estimate 3D motion from the structural channel using rigid/affine plus nonrigid registration to a session reference volume; include z drift and through-plane motion, correct chromatic/spatial offset using the optical calibration, and propagate uncertainty. Apply transforms to the functional channel only after validating that structural and functional motion are colocalized; reserve epochs where channels disagree as high-risk. Interpolate missing frames transparently; never silently delete motion epochs from false-positive estimates.

**[P6.2 Segmentation and contamination model]**  
Segment somata/spines primarily from the structural channel or time-averaged functional data with motion-corrected references. For each ROI define matched neuropil annulus/local background excluding adjacent cells. Estimate contamination coefficient \(c\) by robust regression of ROI signal on neuropil during ephys-confirmed low-spike/blank periods and stimulus-orthogonal components, then test stability across states. Report ΔF/F under multiple plausible \(c\) values and coefficients from global versus local neuropil as a sensitivity analysis. For spines, separate parent-dendrite and axonal/bouton contributions using morphology and stimulus tuning.

**[P6.3 Ground-truth labeling]**  
Detect spikes from ephys with quality metrics: waveform SNR, refractory violations, seal stability, spike amplitude drift, sorting confidence if extracellular. Align spikes to imaging frames using measured clock jitter. Define evaluation windows with pre-specified tolerance for event timing and an explicit lead/lag estimate from cross-correlation between confirmed spikes and fluorescence.

**[P6.4 Calibration model]**  
In calibration cells only, fit models relating confirmed spike counts/times to fluorescence: kernel/deconvolution models, nonlinear saturation function, baseline drift term, motion regressors from structural channel, neuropil term, expression proxy interaction, and random effects for cell/animal/session. Prefer hierarchical models so cell-specific kernels pool toward target-type distributions. Estimate minimum detectable spike count as a function of SNR, frame rate, motion and expression. Calibrate amplitude-to-count mapping only within observed spike-count, firing-rate, expression and motion ranges.

**[P6.5 Detection benchmarking and false-positive reporting]**  
Compare candidate detectors—threshold on ΔF/F, matched filter/template, constrained deconvolution, supervised model trained only on labeled calibration cells—using identical preprocessing and splits. Metrics: sensitivity/recall at fixed precision, precision–recall AUC as primary for sparse events plus ROC for context, F1 at an operating point chosen from downstream cost, false positives per minute in no-spike and motion-challenge epochs, timing error/lead-lag, count error for bursts, calibration-in-the-large, and confidence intervals by hierarchical bootstrap over trials/cells/animals. Report failure enrichments: high motion, z drift, neuropil coefficient extremes, low/high expression, saturation, high firing, bleaching, specific visual features or behaviors.

**[P6.6 Validation and transportability]**  
Run frozen pipeline on held-out neurons/animals. If applying to another cell type, indicator variant, microscope, expression level, anesthesia/behavior state, frame rate or brain region, treat as new domain: first test whether motion/neuropil coefficients, kernels and expression interactions transfer; if not, perform a recalibration with paired ephys in that domain. Report domain-shift metrics before any biological claim.

## 7. Acceptance and stopping criteria — set from downstream cost, not universal constants

Before data collection, define required precision and error tolerance from the biological question, e.g., maximum tolerable false positives per minute and minimum detectable burst size. A proposed indicator/session is acceptable only if all are met: stable health/ephys under imaging; synchronized timing within tolerance; 3D motion residual small relative to ROI and not correlated with detected events; neuropil sensitivity bounded across plausible coefficients; confirmed single spikes/bursts produce monotonic fluorescence within calibrated range before saturation; expression effect is modeled or excluded by range; held-out performance meets pre-set sensitivity/precision and FP limits with intervals excluding unacceptable values; visual responses replicate across repeats and are not explained by motion/eye/locomotion regressors.

Stop or exclude: ephys instability, seal loss, ambiguous spikes, morphological damage, expression toxicity, uncorrectable z/through-plane motion, channel registration disagreement, saturation in the relevant firing range, laser-power drift beyond calibrated tolerance, or contamination so strong that ROI and neuropil are statistically inseparable. Any stopping/exclusion must be logged with reason and included in attrition reporting.

## 8. Troubleshooting

- **Focus/z drift:** increase structural-volume reference frequency, add piezo/z logging, restrict to co-registered z slices, model focus as nuisance; if through-plane motion dominates, treat affected frames as missing and report FP impact.  
- **Behaviour-correlated false signals:** add motion sensors, eye tracking, structural-channel motion regressors and no-spike motion challenges; compare event rates in stationary versus moving epochs; do not subtract behavior blindly because neural activity may be behavior-linked.  
- **Neuropil contamination:** improve optical sectioning/resolution, use smaller/local neuropil estimators, soma-targeted indicator or sparse labeling, estimate contamination under blanks, and present sensitivity rather than a single corrected trace.  
- **Low SNR/small transients:** verify expression, objective/collection path, power within damage budget, frame rate versus kernel, ROI placement; average across repeats only after trial-level alignment and motion control.  
- **Saturation/nonlinearity:** reduce expression/exposure, choose operating point below plateau, fit nonlinear calibration, avoid inference for high-burst regimes outside calibration.  
- **Bleedthrough:** re-estimate unmixing with single-color controls; validate structural channel does not respond to activity.  
- **Ephys perturbation:** prefer cell-attached for calibration; if whole-cell necessary, quantify time-dependent changes in spike shape, resting potential, calcium transient amplitude and visual response.  
- **Overfit detector:** lock preprocessing, enlarge held-out animals, use leave-animal-out, penalize complexity, and require stable performance across days.

---

## Alternatives and limits

Alternatives: cell-attached versus whole-cell ground truth trades minimal perturbation against inability to inject known currents; in vivo versus slice trades ecological validity against control of spike counts and motion; soma-targeted versus cytosolic indicator trades neuropil resistance against different kinetics; supervised detectors can improve sensitivity but may inherit labels and fail under domain shift; widefield is higher throughput but more background/hemodynamic contamination than two-photon.

Hard limits: fluorescence cannot prove instantaneous spike timing finer than sampling plus kernel uncertainty; dendritic spine signals may mix local calcium, backpropagating spikes and synaptic inputs; equal ΔF/F amplitudes need not equal equal firing across expression, saturation, depth, state or cell type. A calibration valid here becomes invalid if indicator variant, expression, imaging physics, target cell type, behavior state, or contamination regime changes; in those cases repeat paired ground truth or formally demonstrate transportability.
