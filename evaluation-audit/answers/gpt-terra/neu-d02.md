# GPT-5.6 Terra / neu-d02

Original final answer, shared by both scoring rounds.

# Proposed calibration and validation protocol for a genetically encoded calcium indicator (GECI)

## Conclusion and recommended next action

**Proposed conclusion:** infer neural activity from the GECI only after a **target-cell-type-specific, simultaneously acquired electrophysiology–imaging calibration** has established (i) the relationship between known spike counts and fluorescence under defined imaging conditions, (ii) detection and false-positive performance in held-out cells and trials, and (iii) robustness to three-dimensional motion, neuropil contamination, expression level, and visual/behavioural confounds. The final validated output should be described as a **probabilistic or calibrated estimate of spiking/activity state**, not as error-free instantaneous spike timing.

The immediate proposed next step is to establish a preregistered analysis plan and acquire a pilot set of **paired imaging–electrophysiology recordings in the intended target cell type**, including visual stimulation, structural-reference imaging, behavioural/motion measurement, and deliberate or naturally occurring motion/neuropil control conditions. The pilot should be used to set—not assume—the imaging rate, temporal windows, motion criteria, neuropil-correction range, event-detection thresholds, spike-count bins, and expression-quality bounds.

**All experiments, analyses, criteria, and controls below are proposed. No completed experimental results are claimed.**

---

# 1. Evidence → inference → conclusion

| Fixed evidence | Inference for the proposed protocol | Operational conclusion |
|---|---|---|
| The indicator improves activity detection and reports somatic and dendritic-spine visual-related signals. | Both somatic activity detection and visual-response tracking are plausible intended outputs, but they require measurement-specific validation. Spine and soma signals should not be assumed to have identical spike relationships. | Calibrate somatic spike inference separately from any dendritic/spine analysis; report spine results as local calcium signals unless independently calibrated. |
| Figure captions state simultaneous imaging and electrophysiology calibration. | Electrophysiology can provide temporally aligned ground truth for fluorescence calibration. | Use simultaneous, time-synchronized imaging and electrophysiology for calibration and independent validation. |
| Fluorescence reflects calcium dynamics influenced by the indicator and imaging system, not error-free instantaneous spikes. | Fluorescence-to-spike conversion is conditional on kinetics, signal-to-noise ratio, imaging rate, expression, and firing pattern. | Estimate activity in specified temporal bins or with an explicitly fitted probabilistic model; do not claim universally exact spike times. |
| Calibration in one cell type cannot be unconditionally extrapolated. | Spike-to-fluorescence transfer functions can differ across cell types and compartments. | Perform calibration and validation in the intended target cell type, brain region, compartment, and preparation. Do not transfer a calibration without a new paired test. |
| Movement, focus drift, background, and neuropil contamination can generate behaviour-related false signals. | Apparent visual or behavioural responses may arise from optical artefacts rather than cellular activity. | Include a structural reference channel, 3D motion estimation, focus/quality metrics, neuropil sensitivity analyses, and no-spike/behavioural false-positive tests. |
| Indicator kinetics, saturation, and expression level can cause the same fluorescence amplitude to represent different firing. | A single amplitude threshold cannot be assumed valid across cells or firing regimes. | Measure expression-related brightness and dynamic-range proxies; evaluate saturation, stratify performance by expression level, and calibrate multiple spike-count/firing-pattern conditions. |
| Exact indicator identity, expression level, spike numbers, imaging rates, and thresholds are unavailable. | Critical parameters cannot be supplied as fixed values. | Determine each parameter empirically in a pilot calibration and lock values before confirmatory validation. |

**Overall conclusion:** a valid neural-activity inference pipeline must be a paired, cell-type-specific measurement model with explicit uncertainty and artefact controls, rather than a fluorescence-thresholding procedure alone.

---

# 2. Scope, assumptions, and unreported parameters

## 2.1 Proposed scientific objective

To determine how accurately GECI fluorescence from the target cell type reports:

1. **Spike occurrence/activity detection** in predefined time windows;
2. **Known spike count or firing-rate category** over calibrated windows;
3. **Visual-response presence, timing, and selectivity**, relative to electrophysiological ground truth;
4. **Response estimates after accounting for motion, focus, background, neuropil, and expression-related variability.**

## 2.2 Proposed primary estimands

For each recorded target neuron:

- Probability of at least one electrophysiological spike in a prespecified imaging-compatible time bin, conditional on fluorescence and quality covariates;
- Estimated spike count or count category over prespecified windows;
- Visual-response probability and response time course from imaging versus electrophysiology;
- False-positive rate in electrophysiologically silent windows, including windows associated with movement or visual stimulation;
- Sensitivity of conclusions to plausible neuropil-subtraction choices.

## 2.3 Assumptions

The protocol assumes availability of:

- A GECI;
- Simultaneous electrophysiology;
- A structural reference channel;
- Visual stimulation;
- Movement and/or neuropil controls.

It does **not** assume the identity or kinetics of the indicator, the cell type, imaging frame/volume rate, expression range, stimulus set, electrophysiological configuration, spike-count range, or detection threshold. These are unreported parameters and must be calibrated.

---

# 3. Experimental design and independent units

## 3.1 Independent units

The proposed hierarchy is:

1. **Animal/preparation**: biological independent unit;
2. **Cell**: measurement unit nested within animal;
3. **Trial/stimulus presentation**: repeated observation nested within cell;
4. **Imaging frame/volume**: time sample, not an independent replicate.

Inference should account for the nesting of cells within animals. A large number of trials from one cell cannot replace paired recordings from multiple target cells and multiple animals.

## 3.2 Calibration and validation separation

The protocol proposes three non-overlapping datasets:

1. **Pilot dataset**  
   Used to characterize image quality, achievable signal-to-noise ratio, motion distribution, candidate bin widths, spike-count ranges, and feasible quality-control thresholds.

2. **Calibration/training dataset**  
   Used to fit motion correction, neuropil handling, fluorescence normalization, kinetic/deconvolution or classification models, and decision thresholds.

3. **Locked validation dataset**  
   Used only once the analysis pipeline is frozen. It must contain paired electrophysiology and imaging from new cells, preferably from new animals or at minimum animals not used to tune thresholds.

A further **transportability dataset** may test another expression range, day, behavioural state, or imaging depth. This is not a substitute for the primary target-cell-type validation.

## 3.3 Allocation and blinding

**Proposed allocation:**

- Randomize or counterbalance visual stimulus order across trials.
- Counterbalance recording order across planned expression levels, depths, and animals where feasible.
- Predefine inclusion before examining visual-response conclusions.
- Randomly assign cells/animals, rather than trials, to calibration versus held-out validation partitions.

**Proposed blinding:**

- The analyst performing initial ROI selection, structural-channel registration, and quality-control labeling should be blinded to electrophysiological spike trains and stimulus labels where feasible.
- The analyst scoring electrophysiological spikes should be blinded to calcium-event calls.
- The final joint analysis may occur only after these intermediate outputs are time-stamped and locked.

Complete blinding may be impractical during simultaneous recordings because physiology guides electrode stability. Any necessary unblinding should be logged.

---

# 4. Ordered operational protocol

## Stage 1 — Preparation and pre-recording quality checks

### 4.1 Define the target population and intended claim

Before recording, specify:

- Target cell type, brain region, layer/depth, and compartment (soma; spine analyses separate);
- Preparation and behavioural state;
- Whether the intended output is binary activity, spike count, firing-rate class, visual responsiveness, or another calcium-derived measure;
- The temporal scale at which claims will be made.

**Proposed rule:** do not make millisecond spike-timing claims if the empirically measured indicator kinetics and volume rate do not support them.

### 4.2 Establish expression and optical quality measures

For each cell and session, record:

- GECI baseline fluorescence in a standardized imaging configuration;
- Structural-channel intensity and image contrast;
- Depth, laser/excitation power, detector settings, and acquisition rate;
- Soma size/ROI geometry;
- Background fluorescence;
- A standardized proxy for expression level, such as baseline GECI brightness normalized to acquisition settings and, where appropriate, structural-channel brightness.

**Important limitation:** fluorescence brightness is not necessarily a direct measure of molecular expression because it also depends on optical depth, illumination, detector settings, and tissue properties. It should therefore be treated as an operational expression/visibility proxy unless independently quantified.

Where feasible, add a post hoc expression assessment using a predefined method. This can test whether imaging brightness reflects expression rather than optical variation.

### 4.3 Test acquisition stability

Before each paired recording:

- Verify hardware time synchronization using recorded timing pulses in both imaging and electrophysiology streams.
- Acquire a short baseline with the structural channel to characterize drift, z-motion, and background.
- Confirm that the electrophysiological recording has stable spike detectability.
- Confirm that neither the electrophysiology setup nor visual stimulus introduces periodic optical/electrical artefacts.
- Record behavioural/motion signals available in the preparation, such as locomotion, pupil, body movement, or trial-wise motion estimates.

**Proposed exclusion before analysis:** recordings with failed synchronization, unstable electrophysiological spike identification, irrecoverable imaging corruption, or absent structural reference data should not enter paired calibration. Exclusion reasons must be reported by animal and cell.

---

## Stage 2 — Simultaneous intervention and sampling

### 4.4 Paired ground-truth recording

For each target cell, acquire simultaneous:

- GECI imaging;
- Structural-reference-channel imaging;
- Electrophysiology;
- Visual-stimulus timestamps;
- Behavioural/motion data;
- Acquisition-clock or synchronization pulses.

### 4.5 Electrophysiological ground-truth strategy

Use a recording configuration that provides identifiable action potentials from the imaged target cell. Candidate proposed approaches include:

- **Cell-attached recording:** minimizes intracellular perturbation and provides spike timing, but does not directly impose a programmed spike pattern.
- **Whole-cell current clamp:** allows known current-evoked spike trains and subthreshold characterization, but may alter intracellular conditions over time.
- **Juxtacellular or other validated extracellular single-cell methods:** may provide spike timing with different stability or identification trade-offs.

The choice should be reported and treated as a possible source of measurement influence. If whole-cell recording is used, test for time-dependent changes in calcium signal or excitability and include recording duration as a covariate or stopping criterion.

### 4.6 Known spike-count calibration in the target cell type

The calibration must include **known spike counts**, not only spontaneous or visually evoked activity.

For each recorded target cell, sample a prespecified range of experimentally feasible spike patterns, including:

- Zero-spike control windows;
- Single-spike or lowest reliably elicited-count windows;
- Increasing spike-count bins;
- Different interspike intervals/burst patterns where feasible;
- Repeated examples of the same count;
- Counts near the expected physiological range under visual stimulation.

If whole-cell current injection is used, deliver randomized and interleaved current protocols designed to evoke these patterns. Actual electrophysiological spike counts—not commanded current amplitudes—are the calibration labels.

If imposing spikes is not appropriate, use naturally occurring electrophysiological spike counts and enrich underrepresented count bins through stimulus design or sampling. This is a weaker design for separating count from firing pattern and should be stated as such.

**Critical proposed test:** compare fluorescence responses for equal spike counts delivered with different temporal patterns. If they differ materially, spike count alone is insufficient; the final model should include recent firing history or use activity categories/windows that the indicator can distinguish.

### 4.7 Visual stimulation and response tracking

Present repeated, randomized visual stimuli sufficient to test the intended visual feature or response metric. The exact stimuli are unreported and must be selected for the scientific question.

For every trial, retain:

- Stimulus identity and onset/offset;
- Electrophysiological spike train;
- GECI and structural-channel time series;
- Motion/focus estimates;
- Neuropil and background traces.

Track visual responses independently in both modalities:

1. **Electrophysiology:** stimulus-aligned spike rate/count, latency, reliability, and selectivity metric;
2. **Imaging:** corrected fluorescence, inferred activity, latency, reliability, and analogous selectivity metric.

The imaging result should be judged against electrophysiology for the same cell and trial set. A population-average match alone is insufficient because it can conceal cell-specific misclassification.

### 4.8 Sampling of movement and focus conditions

To test artefact susceptibility, ensure the dataset contains:

- Low-motion baseline periods;
- Naturally occurring movement periods, if available;
- Visual trials with and without measurable movement;
- Trials with stable versus reduced structural-channel focus/quality, when safely observable;
- No-spike periods across the range of movement.

Deliberate physical perturbations should only be used if compatible with animal welfare and imaging stability. Natural variation is preferable where adequate.

---

# 5. Measurements and preprocessing

## 5.1 Structural reference channel and 3D motion estimation

Use the structural channel as the primary basis for motion estimation because it is intended to report anatomy rather than activity-dependent fluorescence.

**Proposed procedure:**

1. Construct a high-quality reference volume or reference plane/stack from stable structural images.
2. Estimate x–y displacement by frame/volume registration to the structural reference.
3. Estimate z displacement using one of the following proposed strategies:
   - fast structural z-stacks or interleaved reference volumes;
   - multiplane imaging;
   - comparison of current structural images to a reference z-stack;
   - another validated 3D registration method.
4. Apply the estimated 3D transform to the GECI channel.
5. Record residual registration error and a focus-quality metric for each frame/volume.

The analysis should distinguish:

- **Correctable displacement:** structurally registered data with acceptable residual error;
- **Uncertain displacement/focus loss:** frames flagged, censored, or modeled as low-confidence;
- **Uncorrectable periods:** excluded according to prespecified rules.

**Do not infer absence of motion artefact merely from acceptable x–y correction.** Axial displacement and focus changes can alter fluorescence even when lateral registration appears good.

## 5.2 ROI, background, and neuropil measurements

For each soma:

- Define a soma ROI using anatomy and structural information, not calcium transients alone;
- Define a local neuropil annulus or surrounding region, excluding neighboring somata, blood vessels, and obvious nonrepresentative structures;
- Extract soma, neuropil, background, and structural traces;
- Preserve raw traces and masks for reanalysis.

### Neuropil-contamination sensitivity analysis

Because the correct neuropil correction coefficient is unreported and may vary across cells, do not assume a universal subtraction factor. Instead:

1. Analyze uncorrected soma signals;
2. Analyze a set of prespecified plausible correction coefficients or a coefficient estimated from independent low-somatic-activity segments;
3. If fitting a cell-specific coefficient, fit it only in calibration data or independent segments, not by optimizing against held-out spike labels;
4. Quantify how detection, spike-count calibration, and visual-response conclusions change across correction choices.

A result is robust if its principal conclusion survives the prespecified plausible correction range. If a visual response or inferred event appears only after one aggressive correction choice, report it as neuropil-sensitive rather than as confirmed somatic activity.

**Additional proposed control:** test whether the neuropil trace itself predicts movement, stimulus condition, or electrophysiologically silent apparent soma events. Such prediction would indicate possible contamination or shared optical artefact.

## 5.3 Fluorescence normalization and saturation checks

Evaluate several transparently defined representations, such as baseline-normalized fluorescence and model-based fluorescence features. Select the final representation in training data only.

Assess possible saturation by examining whether fluorescence response ceases to increase, or increases nonlinearly, over verified increasing spike counts. Test this separately across expression-brightness strata.

If saturation is detected:

- Limit quantitative count inference to the empirically monotonic range;
- Report higher activity as a censored category (for example, “at or above validated high-activity range”) rather than an exact count;
- Do not extrapolate beyond the highest calibrated spike count.

---

# 6. Analysis plan

## 6.1 Temporal alignment

Align all streams using recorded synchronization signals. Estimate any residual fixed lag between electrophysiology and imaging, but avoid selecting lag separately for each validation trial to maximize apparent performance. Lock the alignment model from calibration data.

## 6.2 Calibration model

Fit one or more candidate models in the calibration dataset:

- Feature-based classifier for spike/no-spike within a predefined time bin;
- Regression or ordinal model for spike-count bins;
- Kinetic/deconvolution model informed by empirical impulse responses;
- Hierarchical model with cell- and animal-level variation;
- Model including fluorescence, recent fluorescence history, structural quality, z-motion, neuropil signal, and expression proxy.

The chosen model should be selected based on held-out calibration cells, not its fit to the same cells used for fitting.

**Recommended output:** calibrated probability of activity and, where supported, a count estimate with uncertainty interval or posterior distribution. This more directly reflects the evidence than an unqualified binary event call.

## 6.3 Detection and false-positive reporting

For a locked validation dataset, compare inferred activity against electrophysiological ground truth at the preregistered temporal resolution.

Report, at minimum:

- True positives, false positives, true negatives, and false negatives;
- Sensitivity/recall;
- Specificity;
- Precision/positive predictive value;
- False-positive rate;
- False discovery rate;
- Receiver-operating-characteristic and precision–recall curves where applicable;
- Timing error or latency error if temporal event localization is claimed;
- Spike-count error, bias, and calibration curve if count inference is claimed;
- Metrics per cell and per animal, not only pooled frames/trials.

False positives should be broken down by context:

- Electrophysiologically silent, low-motion windows;
- Electrophysiologically silent, high-motion windows;
- Visual-stimulation periods with no evoked spikes;
- High-neuropil versus low-neuropil conditions;
- Expression-brightness strata;
- Different z-motion/focus-quality strata.

This breakdown is essential because a low pooled false-positive rate can mask behaviour-linked artefacts.

## 6.4 Visual-response validation

For each cell, compare electrophysiological and imaging-derived results for:

- Response presence versus absence;
- Stimulus-aligned response time course;
- Latency, using resolution compatible with the indicator;
- Trial-to-trial reliability;
- Stimulus preference/selectivity, if relevant;
- Response modulation by behavioural state.

Report disagreement categories, such as:

- Electrophysiology-positive/imaging-negative visual responses;
- Imaging-positive/electrophysiology-negative apparent responses;
- Agreement only before versus after neuropil correction;
- Responses restricted to high-motion or poor-focus trials.

A visual response should be called “validated by paired ground truth” only when the locked imaging analysis agrees with electrophysiology according to preregistered criteria and is not attributable to structural/motion or neuropil covariates.

## 6.5 Expression-level analysis

Stratify or model performance by standardized baseline brightness/expression proxy. Test whether detection sensitivity, false-positive rate, response amplitude per spike, kinetics, or saturation differs by stratum.

Possible interpretations:

- Lower brightness may reduce signal-to-noise ratio and sensitivity;
- Higher apparent expression may alter kinetics, dynamic range, or saturation;
- A brightness effect may instead reflect depth or optical quality.

Therefore, brightness should not automatically be treated as expression causality. The structural channel, depth, power, and image-quality measures should be included in interpretation.

---

# 7. Controls

## 7.1 Essential proposed controls

1. **Electrophysiologically verified no-spike windows**  
   Estimate baseline false positives.

2. **Structural-channel motion control**  
   Determine whether apparent calcium events covary with x–y/z displacement, residual registration error, or focus quality.

3. **Behaviour/movement control**  
   Test whether inferred events persist after matching or modeling movement and whether they occur in no-spike movement periods.

4. **Neuropil control**  
   Compare uncorrected, corrected, and sensitivity-range results; assess relation of soma signals to surrounding neuropil.

5. **Visual-stimulus control**  
   Evaluate stimulus periods without electrophysiological response to identify stimulus-locked optical or behavioural false signals.

6. **Repeated known-count control**  
   Determine repeatability of fluorescence responses to the same electrophysiologically verified spike count/pattern.

7. **Independent paired validation control**  
   Evaluate the frozen pipeline in new cells, rather than reusing fitted cells.

## 7.2 Useful alternatives when a control is infeasible

- If volumetric 3D imaging is unavailable, use interleaved structural z-references or rapid z-stacks, while explicitly limiting claims during possible axial motion.
- If controlled spike induction is not feasible, use dense sampling of naturally occurring electrophysiological count bins, but report weaker control over temporal pattern.
- If a separate structural fluorophore cannot be perfectly co-registered, document channel offset and validate registration with anatomical landmarks.
- If neuropil cannot be cleanly measured in dense tissue, report the analysis as contamination-sensitive rather than asserting cell-autonomous somatic signals.

---

# 8. Proposed acceptance, rejection, and stopping criteria

No universal numerical performance threshold can be justified from the supplied evidence. Therefore, numerical targets must be set prospectively after pilot characterization and before confirmatory validation.

## 8.1 Proposed acceptance criteria

The pipeline may be accepted for a **defined use case** only if the locked validation dataset shows:

1. Predefined detection and false-positive performance targets are met at the chosen temporal resolution;
2. Performance is reported and remains acceptable across animals, cells, and prespecified expression-quality strata;
3. Motion-associated no-spike windows do not show unacceptable excess false positives after 3D correction and quality filtering;
4. Main visual-response conclusions are robust across the prespecified neuropil-correction range;
5. The validated spike-count range is monotonic or otherwise adequately modeled, with saturation limits explicitly stated;
6. Imaging-derived visual-response calls show predefined agreement with paired electrophysiology;
7. Uncertainty is reported for individual estimates and population summaries.

## 8.2 Rejection or restricted-use criteria

Restrict or reject spike inference if any of the following occur:

- Detection threshold performs well only in training data;
- False positives increase strongly during movement, focus changes, or visual trials without spikes;
- Results depend qualitatively on one neuropil subtraction setting;
- Identical spike counts produce irreconcilably variable signals due to unmodeled expression, firing-pattern, or optical effects;
- Saturation prevents distinction among physiologically relevant higher spike counts;
- Performance is unacceptable in a substantial prespecified expression or image-quality subgroup;
- Electrophysiological and imaging visual-response conclusions disagree beyond the preset tolerance.

In such cases, retain only the lower-level claim supported by the data—for example, “motion-screened calcium transients” or “visual-related fluorescence modulation”—rather than “spike count” or “spike timing.”

## 8.3 Proposed stopping rules

Stop a recording session when:

- Electrophysiological spike identification becomes unstable;
- Structural-reference quality no longer supports reliable 3D registration;
- Photobleaching, focus drift, or physiological deterioration exceeds pilot-defined tolerances;
- The planned range of paired spike-count and visual-trial conditions has been obtained; or
- Animal-welfare or preparation-stability limits are reached.

Do not stop data collection merely because a desired detection metric has been reached. Sample-size completion should be based on a prospectively defined number of animals and paired cells, with sufficient representation of relevant expression and motion conditions.

---

# 9. Troubleshooting and interpretation limits

| Observed problem | Proposed diagnosis | Proposed action |
|---|---|---|
| Apparent calcium events align with movement but not spikes. | Residual x–y/z motion, focus change, or behaviour-linked background. | Reassess structural 3D registration; tighten residual-error filtering; test no-spike movement windows; do not count such events as neural detections. |
| Visual responses occur in imaging but not electrophysiology. | Neuropil contamination, stimulus-linked movement, timing error, or optical artefact. | Inspect neuropil and structural traces; repeat sensitivity analysis; verify synchronization; classify as unvalidated if unresolved. |
| Same spike count gives variable amplitudes. | Different spike patterns, expression/brightness differences, saturation, focus variation, or neuropil. | Include firing history and quality covariates; stratify by expression proxy; restrict range; avoid amplitude-only count mapping. |
| High fluorescence has weak incremental response to more spikes. | Saturation or nonlinearity. | Define a saturation boundary and report high activity categorically; do not extrapolate exact counts. |
| Poor detection in dim cells. | Low signal-to-noise, low expression, depth, or poor optical quality. | Improve acquisition if permissible; set a prospective quality threshold; report restricted applicability rather than silently excluding cells. |
| Good pooled accuracy but poor individual-cell performance. | Model may be driven by easy cells or repeated trials. | Report cell-level distributions; consider cell-specific calibration only if evaluated on independent trials and clearly labeled. |

---

# 10. Limits of the validated claim

Even a successful proposed protocol would support only a bounded claim:

> Under the validated indicator, target-cell-type, expression range, imaging configuration, behavioural/preparation state, motion-quality criteria, and spike-count range, corrected GECI signals provide calibrated estimates of electrophysiologically measured activity and visual responses with reported uncertainty.

It would **not** establish that:

- fluorescence equals instantaneous spikes;
- a calibration transfers unchanged to another cell type, compartment, expression regime, depth, imaging system, or indicator;
- dendritic-spine fluorescence directly reports somatic spike count;
- absence of a detected calcium event proves absence of neural activity;
- all visually or behaviourally aligned fluorescence changes are neural without paired artefact controls.

The decisive evidence for use is therefore the locked, paired ground-truth validation, with false-positive analyses explicitly conditioned on motion, focus, neuropil, expression proxy, and visual-stimulus context.
