# Qwen3.8 Max (0902) / neu-d02

Original final answer, shared by both scoring rounds.

## Recommended next action

**Implement a paired, target-cell-type calibration and validation workflow in which simultaneous electrophysiology provides the spike-count ground truth while the genetically encoded calcium indicator is imaged together with a structural reference channel.** The indicator should not be used as a direct spike readout until the mapping from fluorescence dynamics to electrophysiologically verified spikes has been calibrated, validated on held-out data, and tested for motion, neuropil contamination, expression-level variation, saturation, and false-positive rate. **All experiments described below are proposed, not completed.**

The key operational conclusion is: **do not infer neural activity from a fixed fluorescence amplitude threshold.** Instead, use simultaneous electrophysiology to build and validate a cell-type-specific, expression-aware, motion-corrected, neuropil-controlled calibration model, and report detection performance and false positives explicitly.

---

## Evidence-to-inference-to-conclusion chain

| Supplied evidence | Inference | Protocol consequence |
|---|---|---|
| The indicator improves activity detection and reports somatic and dendritic-spine visual-related signals; figure captions state simultaneous imaging and electrophysiology calibration. | The signal can be related to neural activity, but the relationship must be anchored to direct electrical measurements. | Use simultaneous electrophysiology as ground truth for calibration and validation. |
| Fluorescence reflects calcium dynamics influenced by the indicator and imaging system, not error-free instantaneous spikes. | Fluorescence is an indirect, filtered, potentially nonlinear measure of spiking. | Calibrate using known spike counts and spike-history models, not raw amplitude alone. |
| Movement, focus drift, background, and neuropil contamination can produce behaviour-related false signals. | Apparent activity may arise from non-neural or non-target fluorescence changes. | Include a structural reference channel, 3D motion estimation, neuropil masks, movement controls, and false-positive reporting. |
| Indicator kinetics, saturation, or expression level can make the same fluorescence amplitude correspond to different firing. | A universal fluorescence-to-spike conversion is unsafe. | Calibrate per target cell type and expression stratum; test saturation and expression-level effects. |
| Calibration in one cell type cannot be unconditionally extrapolated. | Cell-type-specific calcium dynamics, morphology, and expression can change the signal. | Perform calibration and validation separately in each target cell type and report limits of generalization. |

---

## Assumptions and unreported parameters

These are assumptions or parameters not supplied in the evidence packet. They must be measured or calibrated, not assumed.

1. **Indicator identity, affinity, kinetics, and dynamic range are unknown.**  
   Calibrate empirically from simultaneous electrophysiology.

2. **Expression level is unknown and variable.**  
   Measure baseline indicator fluorescence, structural-channel fluorescence, indicator-to-structural ratio, and saturation behaviour.

3. **Imaging rate, exposure, laser power, and signal-to-noise are unknown.**  
   Determine by pilot calibration balancing temporal resolution, phototoxicity, bleaching, and detection performance.

4. **Spike counts during visual responses are unknown before recording.**  
   Use simultaneous electrophysiology to count spikes and define ground-truth labels.

5. **Analysis thresholds are unknown.**  
   Derive thresholds from calibration data using receiver-operating-characteristic or precision-recall procedures and validate on independent data.

6. **Neuropil contamination and motion artefact magnitudes are unknown.**  
   Estimate from no-spike epochs, movement-only epochs, neuropil masks, and structural-channel motion correction.

7. **Dendritic-spine spikes or local calcium events may not have direct electrophysiological ground truth.**  
   For spines, propose response-level validation rather than exact spike-count inference unless direct ground truth is available.

---

# Proposed calibration and validation protocol

**All experiments below are proposed.**

---

## 1. Preparation and quality checks

### 1.1 Define target cell type and expression criteria

1. Define the target cell type using available genetic, anatomical, or physiological markers.  
2. Confirm that indicator expression is present in the target cell type.  
3. Confirm that a structural reference channel is available and spectrally separable from the indicator channel.  
4. Verify that the structural channel is stable and not itself activity-dependent.  
5. Record expression-level metrics for each cell:
   - baseline indicator fluorescence;
   - baseline structural-channel fluorescence;
   - indicator-to-structural fluorescence ratio;
   - visible morphology quality;
   - saturation status during test flashes or test spike trains.

**Proposed expression-level check:** classify cells into low, medium, and high expression strata using the measured indicator-to-structural ratio, then test whether calibration parameters differ across strata.

### 1.2 Imaging system checks

1. Verify spectral separation between indicator and structural channels.  
2. Check for channel bleed-through using control fields or single-channel expression if available.  
3. Acquire a high-resolution structural reference volume.  
4. Confirm that the structural channel can support three-dimensional registration:
   - x-y translation;
   - z drift;
   - optional rotation or nonrigid deformation if measurable.  
5. Test illumination intensity and exposure using short pilot recordings.  
6. Select the lowest illumination and exposure that provide acceptable signal, because phototoxicity, bleaching, and saturation are possible confounds.

**Unknown parameter:** imaging frame rate.  
**Calibration procedure:** acquire short test sequences at several candidate frame rates while recording electrically evoked single spikes and bursts. Choose the frame rate at which spike-related transients are resolved sufficiently for detection, without excessive phototoxicity or bleaching. Do not assume a universal frame rate.

### 1.3 Electrophysiology checks

1. Establish simultaneous electrophysiological recording from the imaged target cell.  
2. Preferred ground truth: whole-cell current clamp with known injected current and observed spike times.  
3. If whole-cell recording is not possible, propose cell-attached or loose-patch recording, but limit claims to detected action potentials rather than subthreshold state.  
4. Verify electrophysiological health:
   - resting membrane potential where available;
   - spike amplitude and shape;
   - input or access resistance where measurable;
   - stability over time.  
5. Synchronize electrophysiology, imaging frames, visual stimulation, and behavioural tracking using hardware timestamps or shared trigger pulses.  
6. Validate synchronization by delivering test pulses and confirming aligned timestamps.

### 1.4 Visual stimulation and behavioural tracking checks

1. Calibrate visual stimulus timing using a photodiode or equivalent timing signal.  
2. Record stimulus identity, contrast, position, timing, and trial order.  
3. If movement tracking is available, record locomotion, eye position, pupil, or other behaviour-related signals.  
4. Include blank trials and movement-only control trials.  
5. Ensure that visual-response tracking is time-locked to both imaging and electrophysiology.

---

## 2. Independent units, allocation, and blinding

### 2.1 Independent experimental units

1. Treat the **cell** as the primary calibration unit for within-cell spike calibration.  
2. Treat the **animal or session** as the higher-level independent unit for population generalization.  
3. Do not treat repeated trials from the same cell as independent cells.  
4. Use hierarchical or mixed-effects analysis if multiple trials are nested within cells and cells are nested within animals.

### 2.2 Allocation

1. Allocate cells or animals to at least two analysis roles:
   - **calibration set:** used to estimate fluorescence-to-spike mapping and detection thresholds;
   - **validation set:** used only to test performance after calibration.  
2. Prefer validation across different cells or animals rather than only new trials from the same cell.  
3. If sample size permits, use leave-one-cell-out or leave-one-animal-out cross-validation.

### 2.3 Blinding and circularity control

1. Define regions of interest using the structural reference channel before examining the functional calcium trace or electrophysiological spike labels where practical.  
2. Predefine analysis pipelines and threshold-selection rules.  
3. Use calibration data only to choose thresholds or model parameters.  
4. Keep validation spike labels concealed until performance metrics are computed.  
5. Report any case where manual intervention was required after unblinding.

---

## 3. Intervention and sampling design

The proposed design contains three major blocks: known spike-count calibration, visual-response validation, and artefact-sensitivity testing.

---

## Block A: Known spike-count calibration in the target cell type

### 3.1 Purpose

To relate known spike times and spike counts to indicator fluorescence in the target cell type.

### 3.2 Proposed spike-count calibration trials

1. Obtain simultaneous electrophysiology and imaging.  
2. Deliver current-clamp commands designed to evoke predefined spike trains.  
3. Include the following proposed spike-count conditions:
   - zero spikes;
   - single isolated spikes;
   - two-spike pairs;
   - small bursts;
   - intermediate trains;
   - high-frequency trains within the physiological range expected for the cell type.  
4. Randomize the order of spike-train conditions.  
5. Vary interspike intervals to sample the temporal dynamics of the indicator.  
6. Record the actual electrophysiological spike times and compare them with the intended command.  
7. Exclude or relabel trials in which the observed spike count differs from the commanded count.

### 3.3 Saturation check

1. Deliver progressively higher spike counts or higher-frequency bursts.  
2. Test whether fluorescence amplitude stops increasing despite additional spikes.  
3. Mark saturated trials.  
4. Use saturated trials only to define the saturation boundary, not to estimate linear spike counts.

### 3.4 Expression-level calibration

1. Repeat known spike-count calibration across cells with different expression levels.  
2. Test whether the same fluorescence amplitude corresponds to different spike counts in low-expression versus high-expression cells.  
3. Include expression level as a covariate or stratification factor in the calibration model.

### 3.5 Compartment-specific calibration

1. Perform somatic calibration using somatic regions of interest.  
2. If dendritic spines are imaged, treat spines as a separate compartment.  
3. For spines, use somatic electrophysiology to identify somatic spikes, but acknowledge that local spine calcium events may not correspond one-to-one to somatic spikes.  
4. For spine signals, report:
   - visual-response reliability;
   - motion sensitivity;
   - neuropil contamination;
   - relationship to somatic spikes;
   - not necessarily absolute spike count unless direct ground truth exists.

---

## Block B: Visual-response validation with paired ground truth

### 4.1 Purpose

To test whether calibrated imaging signals infer visually evoked activity accurately when the cell is responding to natural or controlled visual stimuli.

### 4.2 Proposed visual stimulation protocol

1. Present a set of visual stimuli expected to drive the target cell type.  
2. Include repeated trials to estimate reliability.  
3. Include blank or null stimuli to measure stimulus-locked false positives.  
4. Include movement-only or behaviour-only control epochs where possible.  
5. Record simultaneous electrophysiology throughout.

### 4.3 Visual-response tracking

For each trial, record:

1. stimulus onset and offset;  
2. stimulus parameters;  
3. behavioural state if tracked;  
4. electrophysiological spike times;  
5. imaging fluorescence trace;  
6. structural-channel motion estimate;  
7. neuropil trace.

### 4.4 Validation logic

1. Use electrophysiology to define true visually evoked spikes.  
2. Apply the calibrated imaging model to infer spikes or spike probability.  
3. Compare inferred events against electrophysiology on held-out visual trials.  
4. Report performance separately for:
   - strong visual responses;
   - weak visual responses;
   - blank trials;
   - movement epochs;
   - high-neuropil epochs.

---

## Block C: Motion, focus drift, and neuropil contamination sensitivity

### 5.1 Three-dimensional motion estimation using the structural reference channel

1. Acquire a reference structural volume before functional recording.  
2. Acquire structural-channel frames or volumes during imaging.  
3. Estimate three-dimensional motion relative to the reference:
   - x shift;
   - y shift;
   - z drift;
   - optional local deformation if supported by data quality.  
4. Apply the estimated transform to the indicator channel or to region-of-interest coordinates.  
5. Quantify residual motion by comparing corrected structural frames with the reference.

### 5.2 Motion controls

1. Record epochs with no electrophysiological spikes but with animal movement, if available.  
2. Record epochs with visual stimulation and movement.  
3. Record epochs with induced or naturally occurring focus drift.  
4. Test whether motion correction reduces false calcium events during no-spike epochs.  
5. Report residual false-positive rate after motion correction.

### 5.3 Neuropil contamination sensitivity

1. Define target regions of interest using the structural channel.  
2. Define surrounding neuropil masks that exclude the target soma or spine.  
3. Extract neuropil fluorescence traces from each mask.  
4. Compute contamination metrics:
   - correlation between target trace and neuropil trace;
   - shared variance;
   - spatial overlap or mask proximity;
   - change in target trace after neuropil regression or subtraction.  
5. Use electrophysiologically verified no-spike epochs to estimate neuropil-driven false signals.  
6. Test sensitivity by varying the neuropil correction strength over a plausible range and reporting how inferred events change.  
7. Do not select the neuropil correction strength using validation labels; choose it from calibration or no-spike control data.

### 5.4 Behaviour-related false signals

Because neuropil contamination can produce behaviour-related false signals:

1. Compare blank visual trials with movement-only trials.  
2. Identify imaging events that occur without electrophysiological spikes but coincide with movement or neuropil activation.  
3. Report these separately as behaviour-associated false positives.

---

## 4. Measurements

For each recording unit, collect the following.

### 4.1 Raw measurements

1. Indicator-channel fluorescence time series.  
2. Structural-channel fluorescence time series.  
3. Electrophysiological voltage or current trace.  
4. Detected electrophysiological spike times.  
5. Injected current or command signal, if available.  
6. Visual stimulus log.  
7. Behavioural tracking signals, if available.  
8. Hardware synchronization markers.

### 4.2 Derived measurements

1. Target soma or spine mask.  
2. Neuropil masks.  
3. Motion parameters in x, y, and z.  
4. Baseline fluorescence estimate.  
5. ΔF/F trace.  
6. Deconvolved or inferred spike-related trace.  
7. Neuropil contamination index.  
8. Expression-level metrics.  
9. Saturation index.  
10. Detection events and inferred spike counts.

### 4.3 Performance measurements

1. True positives.  
2. False positives.  
3. False negatives.  
4. Precision.  
5. Recall or sensitivity.  
6. False-positive rate per unit time.  
7. False-positive rate per trial.  
8. Area under receiver-operating-characteristic curve, if binary or probabilistic detection is used.  
9. Spike-count error, such as bias and root-mean-square error, if count inference is attempted.  
10. Latency error between electrophysiological spikes and inferred calcium events.

---

## 5. Controls

### 5.1 Positive controls

1. Current-injection trials with known spike counts.  
2. Visually evoked spikes confirmed by electrophysiology.  
3. Cells with clear structural outline and stable electrophysiological health.

### 5.2 Negative controls

1. No-spike epochs confirmed by electrophysiology.  
2. Blank visual trials.  
3. Movement-only epochs with no target-cell spikes.  
4. Neuropil-only regions.  
5. Background regions outside cells.  
6. If available, indicator-negative or structural-only control fields to estimate autofluorescence and bleed-through.

### 5.3 Artefact controls

1. Photobleaching control: repeated imaging during no-spike epochs.  
2. Focus-drift control: structural-channel z position over time.  
3. Motion control: structural-channel displacement and residual motion after correction.  
4. Neuropil control: high-neuropil epochs with no target spikes.  
5. Saturation control: high-frequency spike trains producing non-increasing fluorescence.

---

## 6. Analysis workflow

### 6.1 Preprocessing

1. Align all data streams using synchronization pulses.  
2. Detect electrophysiological spikes using voltage threshold, derivative threshold, or equivalent spike-detection rule.  
3. Correct indicator-channel data using the three-dimensional motion estimate from the structural channel.  
4. Reject or flag time segments with motion exceeding a pre-calibrated tolerance.  
5. Segment target regions using the structural channel:
   - soma;
   - dendritic shafts if included;
   - dendritic spines if included.  
6. Segment neuropil masks around each target region.  
7. Extract fluorescence traces for target and neuropil compartments.

### 6.2 Baseline and ΔF/F estimation

Because baseline fluorescence can be contaminated by neuropil and motion:

1. Identify candidate baseline epochs using electrophysiological silence and low-motion criteria.  
2. Estimate baseline fluorescence using a robust low percentile or equivalent robust statistic.  
3. Test baseline sensitivity by recomputing ΔF/F under alternative baseline windows.  
4. Report if baseline choice materially changes detection results.

### 6.3 Neuropil correction

1. Regress or subtract neuropil signal from target signal using correction parameters estimated from calibration or no-spike control epochs.  
2. Test a range of correction strengths.  
3. Report the sensitivity of inferred events to neuropil correction.  
4. Flag cells or spines whose apparent visual responses disappear or change substantially after plausible neuropil correction.

### 6.4 Calibration model

Use the known spike-count calibration data to estimate a mapping from imaging features to spike probability or spike count.

Possible model classes include:

1. **Event classifier:** detects calcium transients associated with spikes.  
2. **Spike-history convolution model:** relates past spikes to calcium fluorescence.  
3. **Deconvolution model:** estimates latent spikes from fluorescence dynamics.  
4. **Expression-stratified model:** fits separate parameters for low, medium, and high expression cells.  
5. **Covariate-adjusted model:** includes motion parameters, neuropil index, and expression level as nuisance or interaction terms.

The exact model should be chosen from calibration performance, not assumed.

### 6.5 Threshold selection

1. Use calibration data to generate candidate detection thresholds.  
2. Evaluate performance using receiver-operating-characteristic or precision-recall curves.  
3. Choose an operating point according to a pre-registered rule, such as:
   - limiting false-positive rate;
   - maximizing balanced accuracy;
   - maximizing precision under a minimum recall constraint.  
4. Do not choose the final threshold using validation ground truth.

### 6.6 Validation analysis

1. Apply the calibrated model and threshold to validation data.  
2. Compare inferred events with simultaneous electrophysiology.  
3. Report performance separately for:
   - visual-response trials;
   - blank trials;
   - movement epochs;
   - high-neuropil epochs;
   - expression-level strata;
   - somatic versus spine compartments.  
4. Report both detection performance and false-positive burden.

### 6.7 False-positive reporting

Report false positives in at least the following categories:

1. False positives during electrophysiologically silent periods.  
2. False positives during blank visual trials.  
3. False positives during movement without target-cell spikes.  
4. False positives during high neuropil activity without target-cell spikes.  
5. False positives that are stimulus-locked.  
6. False positives that survive neuropil and motion correction.  
7. False positives introduced or removed by neuropil correction strength.

For each category, report:

- number of events;
- rate per minute or per trial;
- fraction of all detected events;
- confidence interval or variability across cells/animals.

---

## 7. Acceptance and stopping criteria

Because exact numerical thresholds are not supplied, the following are proposed calibration procedures for determining acceptance criteria.

### 7.1 Synchronization acceptance

1. Deliver test pulses to all acquisition streams.  
2. Measure timestamp offsets.  
3. Accept synchronization if offsets are small relative to the temporal resolution required for spike inference.  
4. If offsets exceed tolerance, correct timing or exclude the session.

### 7.2 Motion acceptance

1. Use no-spike motion epochs to determine how much residual motion produces false calcium events.  
2. Define a motion tolerance based on the residual motion level at which false-positive rate begins to rise.  
3. Accept data segments below that tolerance; flag or reject segments above it.

### 7.3 Neuropil acceptance

1. Use no-spike epochs with high neuropil activity.  
2. Determine whether neuropil fluctuations generate target-region events.  
3. Accept a cell or compartment only if neuropil correction reduces false positives to the pre-registered false-positive budget.  
4. If not, report the compartment as neuropil-contaminated and do not use it for spike inference.

### 7.4 Expression acceptance

1. Compare known spike-count responses across expression strata.  
2. If high-expression cells show saturation at low spike counts, restrict spike-count inference to the unsaturated range.  
3. If expression strata produce non-overlapping calibrations, do not pool them without an expression-level covariate.

### 7.5 Calibration acceptance

A calibration is acceptable only if it meets pre-registered criteria on held-out calibration or validation data, for example:

1. detection above chance;  
2. false-positive rate within the chosen budget;  
3. spike-count error small enough for the intended scientific question;  
4. stable performance across visual conditions, motion conditions, and neuropil conditions.  

Do not invent universal numerical criteria; define them from pilot calibration and the intended use of the indicator.

### 7.6 Stopping criteria

Stop or exclude a recording if any of the following occur:

1. electrophysiological ground truth becomes unreliable;  
2. cell health deteriorates;  
3. structural reference is lost;  
4. motion cannot be corrected below the calibrated tolerance;  
5. indicator saturation prevents distinct spike-count discrimination;  
6. neuropil contamination produces uncorrectable false events;  
7. photobleaching or phototoxicity alters baseline or physiology;  
8. synchronization fails.

---

## 8. Troubleshooting

| Problem | Possible cause | Proposed troubleshooting |
|---|---|---|
| Weak calcium transients despite electrophysiological spikes | Low expression, poor indicator function, low imaging sensitivity, excessive motion | Verify expression, increase structural signal quality, adjust imaging sensitivity within phototoxicity limits, improve motion correction, exclude unstable cells |
| Large fluorescence changes without spikes | Neuropil contamination, movement, focus drift, baseline drift | Strengthen neuropil masking, use no-spike controls, improve 3D motion correction, reject unstable epochs |
| Same fluorescence amplitude for different spike counts | Saturation, expression-level differences, slow kinetics | Restrict inference to unsaturated range, stratify by expression, use spike-history model, report non-identifiability |
| Poor visual-response validation despite good calibration with current injection | Visual state, behavioural modulation, neuropil or motion artefacts, cell-type-specific response properties | Add simultaneous electrophysiology during visual trials, include blank and movement controls, analyse behavioural covariates |
| Spine signals unreliable | Small compartment size, high neuropil contamination, lack of direct ground truth | Use structural-channel segmentation, stricter neuropil controls, limit conclusions to response presence rather than spike count |
| False positives locked to stimulus onset | Movement or pupil changes triggered by stimulus, neuropil activation, illumination artefact | Use blank trials, movement-only trials, neuropil regression, stimulus-locked false-positive reporting |
| Calibration fails across animals | Cell-type differences, expression differences, preparation differences | Calibrate separately by animal or session; use leave-one-animal-out validation |

---

## 9. Calibration procedures for unknown parameters

| Unknown parameter | Proposed calibration procedure |
|---|---|
| Indicator kinetics | Estimate rise and decay from electrically evoked single spikes and bursts; fit spike-history or convolution model to paired data. |
| Imaging frame rate | Test several frame rates during paired electrophysiology; select rate that resolves evoked transients without excessive photodamage. |
| Baseline fluorescence | Estimate from electrophysiologically silent, low-motion epochs; test sensitivity to alternative baseline definitions. |
| Detection threshold | Derive from calibration-set receiver-operating-characteristic or precision-recall analysis; validate on held-out data. |
| Spike-count mapping | Fit model using known spike-count trials; validate against electrophysiology during visual responses. |
| Saturation boundary | Deliver increasing spike trains; identify spike counts beyond which fluorescence no longer increases reliably. |
| Expression-level effect | Measure indicator-to-structural ratio; stratify cells and compare calibration curves. |
| Neuropil correction strength | Estimate from no-spike epochs with active neuropil; select strength that minimizes false positives without eliminating true spikes in calibration data. |
| Motion tolerance | Use no-spike movement epochs; define tolerance based on residual motion associated with elevated false positives. |
| Sample size | Use pilot calibration data to estimate variability and perform a sample-size calculation for the desired precision of sensitivity, false-positive rate, and spike-count error. |

---

## 10. Alternatives

### 10.1 Alternative structural reference channels

Possible structural references include:

1. a spectrally distinct fluorescent protein;  
2. a structural or membrane-bound fluorophore;  
3. vasculature or tissue landmarks if stable;  
4. a separately expressed reference channel.  

The required property is stability, not calcium sensitivity.

### 10.2 Alternative electrophysiological ground truth

1. Whole-cell current clamp is preferred because spike count and membrane state can be observed.  
2. Cell-attached or loose-patch recording can provide spike timing with less intracellular perturbation.  
3. Extracellular recording may be used only if single-unit identity can be confidently matched to the imaged cell.

### 10.3 Alternative calibration stimuli

1. Current-injection spike trains provide controlled spike counts.  
2. Visual stimuli provide ecological validity but spike counts are only known through electrophysiology.  
3. Combined use is preferred: controlled calibration plus visual validation.

### 10.4 Alternative analysis strategies

1. Binary event detection.  
2. Probabilistic spike inference.  
3. Spike-count regression.  
4. Deconvolution.  
5. Mixed-effects population calibration.  

No single method should be assumed best; compare them using paired ground truth.

---

## 11. Limits and caveats

1. **Fluorescence is not a direct spike.** It is a calcium-dependent, indicator-dependent, imaging-system-dependent signal.  
2. **Calcium kinetics introduce delay and temporal summation.** Inferred spikes will have limited temporal precision.  
3. **Saturation can compress high-frequency firing.** Once saturated, fluorescence cannot distinguish additional spikes.  
4. **Expression level changes the fluorescence-to-spike relationship.** High expression may increase baseline, alter dynamic range, or saturate earlier.  
5. **Neuropil contamination can mimic visual or behavioural responses.** This is especially important for small compartments such as dendritic spines.  
6. **Motion correction cannot guarantee complete artefact removal.** Residual motion must be quantified and reported.  
7. **Cell-type specificity is required.** Calibration from one cell type cannot be assumed valid for another.  
8. **Spine calibration is limited.** Unless local electrical ground truth is available, spine signals should be interpreted as local activity-related fluorescence, not exact spike counts.  
9. **Behavioural state can modulate both neural activity and artefacts.** Movement, pupil changes, and neuropil activation must be tracked or controlled.  
10. **Validation performance may differ across preparations.** Leave-one-animal-out or leave-one-session-out validation is needed to assess generalization.

---

## Final conclusion

The safest proposed use of the genetically encoded calcium indicator is as a **calibrated, validated, probabilistic inferential signal**, not as an error-free spike counter. The proposed protocol requires simultaneous electrophysiology, known spike-count calibration in the target cell type, structural-channel-based three-dimensional motion correction, neuropil contamination sensitivity analysis, expression-level stratification, visual-response validation, and explicit false-positive reporting. All experiments described are proposed and should be implemented with pre-registered acceptance criteria, independent validation units, and blind or scripted analysis wherever possible.
