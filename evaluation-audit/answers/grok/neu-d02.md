# Grok 4.7 / neu-d02

Original final answer, shared by both scoring rounds.

All experiments below are proposed. Do not treat fluorescence amplitude, detected events, or visual-related transients as spike counts until a held-out paired calibration in the target cell type meets the gates in this protocol. Exact indicator identity, expression level, spike numbers, imaging rates, and analysis thresholds are unreported and must be estimated here; they are not filled in from the source.

## Recommended next action

Run a de novo, simultaneous imaging–electrophysiology calibration in the same cell type and behavioural state as the planned inference, with a calcium-insensitive structural channel driving three-dimensional motion correction, an explicit neuropil-sensitivity analysis, expression stratification, and pre-registered detection and false-positive gates. Use the validation partition only after those procedures are locked. If pairing, structural-channel registration, or the expression band cannot be secured, stop and do not infer spikes from fluorescence.

## Evidence → inference → conclusion

**Evidence (fixed packet only).** The indicator is described as improving activity detection and as reporting somatic and dendritic-spine visual-related signals. Figure captions are described as stating simultaneous imaging and electrophysiology calibration. Stated limits: fluorescence reflects calcium dynamics shaped by the indicator and the imaging system, not error-free instantaneous spikes; calibration in one cell type cannot be unconditionally extrapolated. Named artefacts: movement, focus drift, background and neuropil contamination can produce behaviour-related false signals; kinetics, saturation, or expression level can make the same fluorescence amplitude correspond to different firing. Available resources for this design: a genetically encoded calcium indicator, simultaneous electrophysiology, a structural reference channel, visual stimulation, and movement or neuropil controls. Unavailable and therefore not used as inputs: indicator identity, expression level, spike numbers, imaging rates, and analysis thresholds.

**Inference.** Because the measured signal is filtered calcium, not spikes, spike inference is a calibrated inverse problem. Because the source already identifies movement, focus, background, and neuropil as routes to behaviour-locked false signals, visual-response tracking without those controls can confirm an artefact. Because expression, kinetics, and saturation change the amplitude-to-firing map, a single threshold or a single gain is not an estimator. Because cell-type transfer is disallowed by the stated limit, somatic calibration does not validate another type, and somatic pairing does not by itself validate spine spike counts. The source’s mention of simultaneous calibration shows that paired ground truth is the appropriate standard; it does not supply the parameters, so those parameters are experimental outputs, not assumptions.

**Conclusion.** The valid use of this indicator for neural-activity inference is restricted to the cell type, expression band, imaging rate, integration window, and artefact regime in which paired error has been measured. Outside that regime the supported claim is at most “a calcium-dependent optical signal was observed,” not a spike count or a confirmed visual spike response.

## Concept relationships

Ground truth is the electrophysiological spike train of the imaged cell, not the fluorescence trace and not the structural channel. The structural channel estimates motion, focus, ROI identity, and a denominator for expression; it is not an activity reporter. Fluorescence is a function of spikes only after calcium influx, buffering, indicator binding, saturation, and the imaging measurement. Neuropil and background are additive contaminants that can correlate with behaviour and with visual stimulation. A visual-related label requires stimulus locking that survives those contaminants and, for somata, a concurrent change in the paired spike train. Detection metrics and spike-count error are different claims: an event can be detectable when its amplitude still maps to more than one spike count. Spine signals are anatomically downstream of the soma; parent-soma spikes are only a partial reference for spines.

## Assumptions and unreported parameters

**Assumptions (proposed design depends on these; if any fails, the corresponding claim is unsupported).** A spectrally separable structural reference is present in or on the recorded cell. The electrode and the imaged soma can be identified as the same cell. Electrophysiological spike times can be recovered with an error small enough to serve as ground truth. Visual stimuli can be time-locked to both recording streams. The behavioural state of calibration matches the state in which inference will be used (anaesthetised versus awake is not interchangeable for movement artefacts).

**Unreported, to be calibrated rather than invented.** Indicator on- and off-kinetics, affinity, and cooperativity; expression level and the width of an acceptable expression band; true spike counts and the smallest resolvable spike packet; frame rate and the longest integration window that still meets the claim; event threshold, neuropil coefficient, baseline window, and motion-rejection cutoff; whether current-evoked and sensory-evoked spikes share one fluorescence gain.

## Proposed protocol

### 1. Preparation and quality checks

1. Define the target cell type by pre-specified genetic, anatomical, or physiological criteria before any recording. Cells that fail that definition are not calibration data and are not an extrapolation set.
2. Confirm optical access, indicator expression, and a usable structural channel in the same field. Reject fields in which the two channels cannot be separated or the structural signal is too dim for registration (dimness cutoff set in the pilot in step 6, not by a fixed published value).
3. Proposed expression screen, before visual stimulation: in a standardised somatic ROI, record baseline indicator fluorescence and structural-channel fluorescence under the same laser power and dwell. Define an expression index as their ratio, or as indicator photons per dwell if a structural denominator is locally unusable. This index is the covariate for later stratification. Exclude, by pilot-derived bounds, cells that saturate the detector at rest or during the brightest expected response, and cells whose indicator signal is within the noise floor of a blank optical recording.
4. Proposed pairing check: position the electrode on the imaged soma. Accept the pair only if spatial coincidence is unambiguous and at least one of the following is true: spontaneous spikes in the electrode match the imaged cell’s identity criteria, or a brief current injection evokes spikes only in that cell while neighbouring somata do not show the same electrophysiological waveform. If identity is ambiguous, discard the cell. Do not use fluorescence to decide which cell was patched.
5. Proposed electrophysiology quality check: require a stable recording mode (cell-attached or whole-cell; see alternatives). Have spike times marked by a pre-specified detector plus a second independent mark on a subset of traces. If the two marks disagree above a pre-registered mismatch rate, the trace is not ground truth; stop that cell. Whole-cell recordings must document series resistance and holding current over time, because dialysis can change calcium handling and thus the very map being calibrated.
6. Proposed pilot, separate from the validation partition: a small number of paired cells is used only to lock imaging rate, expression bounds, motion cutoff, neuropil procedure, and the event operating point. Those choices are frozen before the validation animals are analysed.

### 2. Independent units

The independent unit for a cell-type claim is the animal or independent preparation. Cells are nested in animals; trials and frames are repeated measures within a cell. Report cell-level and animal-level summaries. Do not treat thousands of frames as thousands of independent calibrations. Spine observations are nested in the parent cell and do not count as additional independent ground-truth cells unless each spine has its own electrical recording, which this protocol does not assume is available.

Split, before analysis, into a training/pilot partition (lock parameters) and a validation partition (report detection, false positives, and count error). A further leave-one-animal-out check is proposed so that one preparation cannot dominate the accepted gain.

### 3. Allocation and blinding

Allocate animals to pilot versus validation before recordings from the validation set are scored. Within each session, randomise visual stimulus identity and interleave blank epochs of matched duration. If current-evoked spike packets are used, interleave them with sensory epochs rather than blocking all electrical calibration at the end, when expression, bleach, or seal may have drifted.

Blinding rules: motion estimation and ROI placement use only the structural channel and a pre-acquired structural z-stack, not the electrophysiological trace and not an activity-triggered average of the indicator. The event detector’s threshold and any spike-inference hyperparameters are locked on the pilot partition. Fluorescence-only labels (“visual response” versus “no response”) are assigned before the analyst opens the paired spike train for that validation cell. Exclusions (lost seal, ambiguous pairing, saturation, uncorrectable motion) follow the written rules and are logged with the channel that justified them.

### 4. Intervention and sampling

Proposed session structure, in order, after pairing is accepted:

1. Structural z-stack and expression-index measurement at the working power.
2. Quiet epoch: no visual stimulus, for baseline, noise, and neuropil estimation during electrophysiologically silent periods.
3. Randomised visual stimuli and matched blanks, with simultaneous imaging, electrophysiology, and an independent movement or focus monitor (structural-channel motion metrics at minimum; a behavioural sensor if the animal can move).
4. Proposed known-count intervention: current injection delivering pre-specified spike packets (isolated spikes and short bursts at several counts). The counts are known because they are commanded and then verified on the electrode, not because a fluorescence model predicted them. Packets that the electrode does not confirm are not used as labels.
5. Repeat a short expression and z-stack check at the end to document bleach and focus drift.

Sampling continues across animals until stopping rules in section 8 are met. Do not stop early because a few cells “look calibrated.”

**Unreported spike numbers.** No spike count is imported from the source. Labels are the verified electrode counts in each analysis bin. If single spikes do not produce a fluorescence deflection above noise in the pilot, the protocol does not invent a single-spike sensitivity; it restricts the claim to the coarsest packet size that is actually resolved and says so.

**Unreported imaging rate.** In the pilot, record at the fastest rate that is stable on the rig without unacceptable bleaching over the session length. Then downsample the paired pilot data and recompute count error and detection. Adopt the slowest rate that still meets the pre-registered error tolerance if the claim is integrated count; keep a faster rate if the claim is timing. The numerical rate is an output of that comparison.

### 5. Measurements

Record, time-aligned: indicator images, structural images, electrode voltage, stimulus identity and onset, commanded current, expression index at start and end, and the 3D motion traces derived from the structural channel.

Proposed measurements per cell:

- Electrode spike times and binned spike counts.
- Indicator fluorescence in the soma ROI and, where in focus, in dendritic spines whose parent soma is the paired cell, with ROI borders taken from the structural channel.
- Local background and a neuropil annulus that does not include other somata, defined on the structural image.
- Residual motion in x, y, and z after correction, in units of pixels and of ROI radius.
- Expression index and a saturation flag (fraction of pixels at the detector ceiling).
- Stimulus-locked averages of fluorescence and of spike rate, plus the same averages on blank epochs and on high-residual-motion epochs.

### 6. Controls

**Structural reference and three-dimensional motion.** Estimate x–y motion by registering the structural channel (rigid, then non-rigid only if a pre-specified residual criterion requires it). Estimate z by correlating each structural frame to the pre-acquired z-stack, or by true multiplane sampling if that mode is used. Apply the same transforms to the indicator channel. Do not register on the indicator channel; activity would be partly removed or partly turned into false motion. Proposed positive control: in a subset of pilot sessions, impose small known focus steps and quantify false indicator transients before and after correction. The motion-rejection threshold is not a fixed micron value. On the pilot set, find the residual-motion level at which the fluorescence event rate during electrode-silent epochs exceeds the pre-registered false-positive bound; reject validation trials above that empirical cutoff.

**Neuropil and background.** Estimate a contamination coefficient from the regression of somatic indicator fluorescence on the neuropil time course, preferentially using electrode-silent epochs so that true spikes do not set the coefficient. Subtract or jointly model that component. Proposed sensitivity analysis: recompute detection, false-positive rate, and count error across a grid of coefficients centred on the per-cell estimate, with the grid width equal to the spread of estimates across pilot cells, not a universal constant. A cell fails this control if the scientific metric moves outside its pre-registered tolerance across that grid. Background-only ROIs outside the tissue, if the preparation allows, separate detector offset from neuropil.

**Behaviour-related false signals.** Independently mark movement and focus-drift epochs from the structural channel and any behavioural sensor. The false-positive contribution of artefacts is the indicator event rate in those epochs when the electrode shows no spikes, after the locked correction. Stimulus-locked fluorescence that is explained by stimulus-locked motion or neuropil is not a visual spike response.

**Expression, kinetics, and saturation.** These are controls on the meaning of amplitude, not only quality filters. Proposed: at fixed verified spike count, test whether fluorescence amplitude still depends on the expression index. Conversely, at fixed fluorescence amplitude, test whether verified spike count depends on expression. Fit indicator kinetics from the paired pilot data by aligning fluorescence to isolated verified spike packets and estimating a causal kernel and a static nonlinearity with cross-validation. Do not insert literature time constants for a named indicator; identity is unreported. Saturation is present if the slope of fluorescence versus spike count declines at high counts; the inverse used for inference must be that nonlinearity, and linear conversion is then out of scope above the bend.

**Visual-response tracking.** A somatic transient may be called visual-related only if it is larger in stimulus epochs than in matched blanks, the difference remains after regression of residual motion and neuropil, and the paired spike rate changes in the same window. Spine transients may be called visually associated calcium signals only if the same stimulus and artefact tests pass and the event is interpreted relative to the parent soma. They are not called spine spike counts. Absence of a somatic spike change with a surviving spine signal is reported as a dendritic calcium event, not forced into a spike count.

**Negative and transfer controls.** Blank stimuli estimate the false-positive rate per unit time. A neighbouring soma that is imaged but not the patched cell, if its spikes are unknown, is not a second ground-truth cell; it can only illustrate field contamination. No other cell type is accepted as a transfer test. If the experiment will later include another type, that type needs its own paired calibration.

### 7. Analysis

Pre-register the claim level before the validation partition is opened. Allowed claim levels, from weak to strong: calcium signal present; calcium event detection with a stated false-positive rate; spike-count estimation inside a stated count range and integration window; spike timing to within a stated lag. Each level has its own gate. Passing detection does not pass count or timing.

Proposed analysis order:

1. Apply locked 3D correction and neuropil procedure. Define baseline from electrode-silent or pre-stimulus frames whose residual motion passed the cutoff. The baseline window length is chosen in the pilot as the window that minimises count error without eating into the stimulus response; it is not copied from an unreported source method.
2. Forward description, training partition only: spikes convolved with the estimated kernel, passed through the estimated nonlinearity, compared with measured fluorescence. Retain the model class (linear kernel versus nonlinear saturation) that wins on training likelihood or count error under the pre-registered rule. Alternatives are reported, not silently discarded.
3. Inverse description: map fluorescence features in a time bin to spike count or to spike probability. The bin width is the integration window under test. Cross-validate within the training partition by leaving out cells and, separately, animals.
4. Lock the operating point. For detection, choose the threshold on training data to meet a pre-registered false-positive bound on blank, electrode-silent time, then read sensitivity at that point. For counting, choose the inverse model that minimises training count error inside the non-saturated range. Do not retune on validation cells.
5. On the validation partition, report sensitivity, precision, false-positive rate per unit time, timing error (lag between spike packet and fluorescence event), and count error (correlation and root-mean-square error, or the equivalent pre-registered score), with animal-level confidence intervals. Also report the neuropil-sensitivity span and the expression-interaction test.
6. Visual responses: stimulus versus blank contrast for fluorescence and for spike rate; partial association after motion and neuropil covariates; fraction of fluorescence “responses” that lack a spike-rate change (false visual labels) and the fraction of spike-rate changes that lack a fluorescence event (missed visual spikes).

Hierarchical structure is respected: summarise within cell, then across cells within animal, then across animals. A single highly expressing cell must not set the gain for the type.

### 8. Acceptance and stopping criteria

Numerical bounds are pre-registered by the investigator as decision tolerances for the claim they intend to publish. This protocol does not supply those numbers, because no such thresholds were in the evidence. It does fix the logical gates.

Accept a validation cell only if all of the following hold: pairing identity confirmed; electrode spike-mark mismatch within the pre-registered ground-truth bound; expression index inside the pilot-defined band, or expression entered as a covariate in a model that was locked before validation; no detector saturation; residual 3D motion below the pilot-derived cutoff for the analysed frames; neuropil sensitivity within tolerance.

Accept a claim for the target cell type only if, on the validation partition, the metric for that claim level meets its pre-registered bound and the animal-level interval is no wider than the pre-registered precision. Scope of acceptance is exactly the tested cell type, behavioural state, expression band, frame rate, and count range. Extrapolation is a failure, not a minor caveat.

Stop a cell if the seal or access is lost, pairing becomes ambiguous, the detector saturates, structural registration fails, or end-of-session expression has left the accepted band. Stop the study as adequate when validation precision is reached. Stop the study as inadequate when a pre-registered maximum number of animals is reached and the gates still fail or the intervals remain too wide. In that case the conclusion is that this indicator and imaging configuration are not validated for the intended inference. Do not loosen a gate after seeing the validation partition.

### 9. Troubleshooting

If false positives cluster in high residual-motion frames, tighten the motion cutoff, improve z estimation, or drop awake epochs that cannot be stabilised. Do not subtract the indicator trace against itself to “remove motion.”

If false positives track the neuropil time course or the sensitivity grid moves the metric past tolerance, shrink ROIs to the structural soma core, exclude fields with dense overlapping processes, or abandon spike inference in that region. A more aggressive neuropil coefficient that was chosen because it improved validation scores is not allowed; the coefficient rule was locked on pilot data.

If the same fluorescence amplitude maps to different spike counts across expression strata, narrow the accepted band or include the expression index in the inverse model and re-lock on the training partition. Discarding the inconvenient stratum after validation is not a correction.

If isolated spikes are invisible and only bursts move fluorescence, downgrade the claim from single-spike detection to burst or rate estimation over the window that actually calibrates. Slow kinetics are a result, not a preprocessing failure.

If current-evoked and visually evoked packets of the same electrode count produce different fluorescence amplitudes, do not pool them into one gain. Report separate maps, and use the sensory map for visual-response inference. A mismatch can come from spike waveform, dendritic spikes, or calcium from sources other than the somatic sodium spike; the protocol does not decide among those causes without further experiments.

If somatic calibration succeeds but spine events diverge from parent-soma spikes after motion and local neuropil control, report spine-specific calcium signals and do not assign them somatic spike counts. Proposed follow-up, only if the scientific claim requires spine spikes: a method that electrically records the relevant compartment. Until then, spine spike counts stay unvalidated.

If ground-truth spike marking is itself unstable, stop. No optical refinement can repair a bad electrode label.

## Alternatives and limits

Cell-attached recordings avoid dialysis of calcium buffers and are the better default when the goal is the native spike-to-fluorescence map. Whole-cell recordings allow known-count current injection and cell identification but can change the map; if whole-cell is used, the limitation is explicit and a cell-attached subset is the proposed check on dialysis bias.

Volumetric imaging is the better z measurement when available. A z-stack correlation proxy is the proposed alternative on a single-plane rig; it fails if the structural image is axially ambiguous, in which case behaviour-related signals in that preparation are not acceptable.

A linear deconvolution is an acceptable inverse only inside the pilot-defined non-saturated, expression-matched range. A nonlinear generative inverse is the proposed alternative when the saturation check fails. The selection rule is training-set error, not flexibility.

Somatic pairing does not validate axons, other cell types, other indicators, other temperatures, or other imaging rates. The source limit on cell-type extrapolation is treated as binding. Spine visual-related signals in the source summary justify measuring spines, not equating them to spikes.

This protocol estimates association between verified spikes and fluorescence under controlled contamination. It does not identify the biophysical source of every photon, and it does not show that an unmeasured indicator variant would have performed similarly.

## What would change the recommendation

A full paired calibration remains necessary while indicator identity, expression, rates, and thresholds are unknown. If those parameters later become known for this exact indicator, cell type, expression band, and imaging system, the study could shrink to a verification set against that external map; it still could not skip motion, neuropil, and false-positive checks, because those depend on the preparation. If the only intended claim is detection of a calcium increase, count-error gates can be dropped, but silent-epoch false positives, 3D motion, and neuropil sensitivity cannot. If the experiment must be done in a cell type where simultaneous somatic electrophysiology is impossible, this protocol does not authorise a fluorescence-only substitute; the recommendation changes to “do not infer spikes,” not to a looser optical threshold. If animals are awake and residual motion cannot be held under the pilot cutoff, visual-response claims from this indicator are not accepted in that state, regardless of how clean anaesthetised pilot cells looked.

Uncertainties that dominate interpretation are the unmeasured kinetics and saturation, the expression dependence of gain, and the share of stimulus-locked fluorescence that is neuropil or motion. Any one of those, if large on the validation partition, is sufficient to reject spike-count inference even when average traces look visually responsive.
