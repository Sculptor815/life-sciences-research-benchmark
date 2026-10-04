# GPT-5.6 Terra / neu-d01

Original final answer, shared by both scoring rounds.

## Conclusion and recommended design

Use **projection-terminal inhibition in Q during a temporally isolated cue-retrieval interval**, not inhibition of P cell bodies. Express the inhibitory opsin selectively in P neurons that project to Q, illuminate their terminals locally in Q, and compare randomized light-on versus light-off trials within animals. Structure the task so that cue sampling/retrieval occurs while the animal is required to remain still, followed by a separate go signal permitting locomotion.

This design can support the conclusion that **P-to-Q signaling is necessary for normal learned-choice retrieval** only if: (i) Q illumination demonstrably suppresses P-derived signaling in Q, (ii) the behavioral impairment is opsin-dependent and retrieval-window-specific, and (iii) sensory/light and locomotor explanations are excluded or bounded by controls.

A P-cell-body inhibition experiment alone would not adequately test P-to-Q necessity, because P also projects elsewhere.

---

# 1. Evidence-to-inference-to-conclusion chain

| Fixed evidence | Inference | Design consequence |
|---|---|---|
| **O1. P projects to Q and to another region.** | Inhibiting P somata could suppress P output to Q and to the other target. A resulting behavioral effect would not identify P-to-Q signaling as the causal pathway. | Express in P-to-Q neurons if possible, but deliver light in **Q**, at P-derived terminals, rather than at P cell bodies. |
| **O2. Inhibitory opsin expression can be targeted to P neurons projecting to Q.** | The relevant P-to-Q neuronal population can be optogenetically manipulated. This does not by itself establish that local Q illumination suppresses transmitter release from those axons. | Validate expression, fiber placement, and functional inhibition of P-derived terminals in Q before interpreting behavior. |
| **O3. Correct choices require locomotion.** | Reduced correct choice could arise from impaired retrieval, sensory processing, movement initiation, directional movement, general vigor, or failure to complete trials. | Separate cue/retrieval from movement in time; measure locomotion directly; include movement-window perturbations and analyze omissions separately from incorrect choices. |
| **O4. Light delivery can be visible to the animal.** | Light can act as an unintended cue or distractor, potentially changing choice or movement without neural inhibition. | Shield the implant, measure light leakage, use masked lighting, and include opsin-negative animals receiving the same light schedule. |

**Primary causal conclusion, if criteria are met:** acute signaling from P-derived terminals in Q is necessary during the tested retrieval interval for normal learned-choice performance.

**What the experiment would not establish by itself:** that P-to-Q signaling is the only pathway supporting retrieval; that the effect is permanent or required during learning; or that the effect is specifically “memory retrieval” rather than cue processing or decision formation unless the task epochs distinguish those processes.

---

# 2. Critical assumptions and unreported parameters

## Assumptions to test rather than assume

1. **Terminal efficacy assumption:** inhibitory-opsin activation in Q suppresses P-derived signaling in Q.
2. **Spatial specificity assumption:** light is sufficiently confined to Q that the intended manipulation is predominantly local to P terminals in Q.
3. **No substantial non-Q effect assumption:** Q illumination does not materially alter P somatic activity or P output to the other projection target.
4. **Temporal separation assumption:** the task can separate cue/retrieval from locomotor execution.
5. **Sensory-control assumption:** external light leakage can either be eliminated or matched across control conditions.

If terminal inhibition cannot be validated, the experiment should be reported as manipulation of **P-to-Q-projecting neurons**, not a definitive test of the **P-to-Q projection**.

## Parameters not provided

The evidence packet does not specify opsin identity, illumination wavelength, light power, pulse structure, expression method, task cue modality, cue duration, retention interval, locomotor distance, sample size, or behavioral criterion.

These should be chosen by **calibration**, not assumed:

- determine the lowest local Q illumination that produces verified terminal inhibition;
- determine the behavioral timing at which cue information is acquired but locomotion has not begun;
- determine a stable-baseline training criterion from pilot behavior;
- determine animal-level sample size from pilot estimates of within-animal light effects and the smallest behaviorally meaningful effect.

---

# 3. Operational ordered protocol

## A. Preparation and quality checks

### A1. Pre-register the causal question and primary estimand

Pre-specify:

- **Question:** Is P-to-Q signaling necessary during the cue-retrieval interval of a learned choice task?
- **Primary comparison:** change in correct-choice probability caused by Q light during the retrieval interval in opsin-positive animals, relative to the same light effect in opsin-negative controls.
- **Primary unit of biological inference:** animal, not trial, cell, hemisphere, or session.
- **Primary outcome:** trial outcome classified as correct, incorrect, omission/failure to respond, or aborted trial.
- **Primary retrieval window:** a post-cue, pre-movement interval, if the task supports one.
- **Confound criteria:** thresholds for meaningful changes in sensory detection, movement initiation, movement trajectory, or visible-light effects.

The primary analysis should be intention-to-treat: all randomized trials are included, with omissions analyzed explicitly rather than discarded.

### A2. Use a task structure that separates retrieval from movement

Where feasible, modify the learned choice task into the following ordered epochs:

1. **Trial initiation/central hold.**
2. **Cue presentation.**
3. **Post-cue retrieval or delay interval:** animal must maintain a central hold and cannot yet initiate the locomotor choice.
4. **Go signal.**
5. **Locomotor choice period.**
6. **Outcome period.**

The key feature is that the animal must remain stationary during the retrieval interval. If the existing task lacks such a delay, add and validate one before the causal experiment.

This permits three conceptually different perturbation windows:

- **Retrieval-window light:** after the cue has been sampled and before the go signal. This is the primary test.
- **Cue-presentation light:** tests the broader cue-triggered process but is more vulnerable to sensory-processing interpretations.
- **Movement-window light:** after the go signal, during locomotion. This tests whether P-to-Q inhibition primarily disrupts motor execution.
- **Intertrial or outcome-window light:** a temporal control for nonspecific light exposure and state changes.

Do not describe a cue-period effect alone as selective evidence for retrieval: it could reflect altered perception or attentional processing of the cue.

### A3. Expression and implantation

Use the available projection-targeting strategy to express the inhibitory opsin in P neurons that project to Q.

For the primary experiment:

- implant the illumination device over **Q**;
- avoid illuminating P cell bodies in the main projection-specific test;
- use the same surgical and implant procedures in opsin-negative control animals, except that they express a non-inhibitory control construct.

### A4. Anatomical quality checks

After the experiment, assess:

- opsin expression in P neurons identified as projecting to Q;
- P-derived labeled axons/terminals in Q;
- illumination-device placement relative to Q;
- unintended expression or implant placement outside the planned structures;
- whether the experimental and control cohorts differ systematically in placement quality.

Define exclusion rules before outcome unblinding. Examples of acceptable exclusion categories are failed expression, missed implant placement, or technical malfunction—not poor behavioral performance or an undesired behavioral result.

### A5. Functional quality checks

Before interpreting behavioral effects, establish that the intended local manipulation works.

**Proposed validation experiment:**

- record a Q-level physiological readout of P-derived input while illuminating in Q;
- test whether the planned illumination suppresses that P-derived signal;
- test whether the effect is present only in opsin-positive preparations;
- test whether the selected dose produces evidence of nonspecific effects in opsin-negative preparations.

Because the evidence packet does not establish terminal efficacy, this validation is essential.

**Additional projection-specificity check, if feasible:**

During Q illumination, measure whether P somatic activity or signaling in P’s other target changes detectably. If local Q illumination measurably alters P-wide activity or output to the other target, the conclusion must be weakened to: “Q illumination of P-to-Q-projecting neurons affected behavior,” rather than “P-to-Q terminal signaling in Q was necessary.”

### A6. Light calibration and visible-light check

Determine illumination settings empirically:

1. Begin with low light exposure.
2. Increase only until terminal inhibition is verified.
3. Select the minimum setting that produces reliable inhibition.
4. Test the selected setting in opsin-negative preparations for nonspecific physiological or behavioral effects.

For the visible-light issue:

- use opaque shielding around the implant and optical connector;
- inspect or measure leakage from the animal’s viewpoint or eye position;
- use stable background/masking illumination where compatible with the task;
- verify that light-on versus light-off trials cannot be identified from external leakage by an observer or camera procedure.

If visible light cannot be reduced below a pre-specified practical limit, the opsin-negative light control becomes indispensable, and any residual sensory ambiguity should remain explicit in interpretation.

---

## B. Independent units, allocation, and blinding

### B1. Independent units

- **Animal:** independent biological replicate.
- **Session and trial:** repeated observations nested within animal.
- **Hemisphere:** not an independent replicate if both hemispheres are studied in one animal.
- **Cells or histological fields:** validation observations, not independent behavioral replicates.

### B2. Allocation

Allocate animals before behavioral testing to:

1. **Opsin-positive, Q-terminal-light group.**
2. **Opsin-negative, identical Q-light control group.**

If relevant biological variables exist, balance them across groups before training or surgery. The evidence packet does not specify such variables, so they should be documented rather than assumed irrelevant.

Within each animal, randomly interleave trial types while balancing:

- light on versus light off;
- cue identity;
- correct choice direction;
- retrieval, movement, and control light epochs;
- trial position within session.

Avoid predictable long blocks of light-on trials, because animals could learn light contingencies.

### B3. Blinding

- Code animals and viral conditions so the experimenter scoring behavior is blind to group.
- Automate trial delivery and outcome scoring where possible.
- Blind histological placement scoring to behavioral condition.
- Lock the analysis plan before decoding group identities.

---

## C. Intervention and sampling

### C1. Main intervention

On randomized trials, illuminate P-derived terminals in Q only during the predefined **post-cue, pre-go retrieval window**.

Use a light-off trial as the within-animal baseline. Deliver the same temporal pattern in opsin-negative animals.

### C2. Epoch controls

In the same animals, on separate randomized and balanced trials, deliver identical Q light during:

- cue presentation;
- movement/choice execution;
- intertrial or outcome interval.

These controls distinguish a retrieval-specific deficit from a general effect of light, task state, or movement.

### C3. Sampling plan

Collect enough sessions and animals to estimate the animal-level light effect with a confidence interval narrow enough to distinguish the smallest meaningful retrieval impairment from no meaningful effect.

Use a pilot dataset to estimate:

- baseline accuracy;
- omission rate;
- within-animal trial-to-trial variance;
- between-animal variance in light effect;
- effect of trial number, session number, cue identity, and side.

Use those estimates for a simulation- or model-based power calculation. Do not stop because a nominal significance threshold is crossed early.

---

# 4. Measurements

## Behavioral outcome measures

For every initiated trial, record:

- cue identity;
- required choice direction;
- light condition and epoch;
- correct versus incorrect choice;
- omission or failure to respond;
- trial aborts or broken holds;
- reaction time from go signal;
- choice commitment time, if measurable;
- reward outcome.

Analyze omissions separately. A fall in “correct choices” can result from more incorrect choices, more omissions, or both; these imply different possible mechanisms.

## Movement measurements

Because locomotion is required, measure:

- movement onset relative to cue and go signal;
- premature movements during the hold/retrieval interval;
- path trajectory;
- speed;
- distance traveled;
- directional commitment;
- endpoint accuracy;
- movement duration.

A camera- or sensor-based measure is preferable to a single endpoint measure because an animal can reach the correct endpoint with altered movement vigor or trajectory.

## Sensory measurements

Use at least one control that asks whether light or the cue has become behaviorally altered independent of learned retrieval.

**Proposed sensory controls:**

1. **Opsin-negative light control:** same Q illumination and task schedule.
2. **Cue-detection/discrimination control:** use the same sensory cues in a task where the required response depends on the currently present cue rather than recall of a learned cue-to-choice association, if such a control is compatible with the task.
3. **External-light visibility check:** quantify leakage and confirm shielding/masking performance.
4. **Temporal light control:** light outside the retrieval interval, with identical physical illumination.

A light-induced change in the opsin-negative group is evidence against a clean neural interpretation.

---

# 5. Analysis plan

## Primary analysis

Model trial outcome with a hierarchical analysis that accounts for trials nested in sessions nested in animals. The main test is the interaction:

\[
\text{opsin status} \times \text{retrieval-window light}
\]

The critical question is whether retrieval-window light changes correct-choice probability more in opsin-positive animals than in opsin-negative animals.

Include pre-specified task variables such as cue identity, correct side, session, and trial position. Estimate animal-level effects and their population uncertainty.

Use a multinomial or separate pre-specified model for:

- correct choice;
- incorrect choice;
- omission/aborted response.

Do not analyze only completed trials as the sole primary analysis, because excluding omissions can conceal a strong impairment in movement initiation or task engagement.

## Movement analysis

Analyze movement outcomes separately from the primary choice analysis:

- premature movement and hold breaks during the retrieval interval;
- movement latency after the go signal;
- speed, trajectory, and directional accuracy during locomotion.

Do **not** simply include post-light movement variables as covariates in the primary correctness model. Movement may itself be affected by the intervention and may be part of the causal pathway; conditioning on it could distort the estimated total behavioral effect.

Instead, ask whether the retrieval-window intervention:

1. impairs correct choices while leaving pre-go holding and post-go movement measures practically unchanged; or
2. produces a pattern consistent with motor impairment, such as more hold breaks, delayed movement, reduced speed, or path distortion.

## Sensory-confound analysis

Test whether light changes behavior in the opsin-negative group. Also compare retrieval-window light with non-retrieval light in opsin-positive animals.

A credible retrieval interpretation requires the active-group retrieval effect to exceed:

- the light effect in controls;
- the effect of intertrial/outcome light;
- and, ideally, effects attributable to movement disruption.

---

# 6. Acceptance and stopping criteria

## Criteria supporting the intended conclusion

Conclude that P-to-Q signaling is necessary during the tested retrieval interval only when all of the following are satisfied:

1. **Anatomical QC passes:** expression is in P-to-Q-targeted neurons and illumination is centered in Q.
2. **Functional QC passes:** Q illumination inhibits the intended P-derived signal in Q at the selected dose.
3. **Behavioral effect is opsin-dependent:** retrieval-window light impairs learned-choice performance more in opsin-positive than opsin-negative animals.
4. **Temporal specificity is supported:** the effect is larger during retrieval than during intertrial/outcome illumination.
5. **Movement explanation is not sufficient:** retrieval-window light does not produce a practically consequential impairment in stationary holding, locomotor initiation, trajectory, speed, or endpoint execution that could explain the choice deficit.
6. **Sensory explanation is not sufficient:** visible-light controls and opsin-negative controls show no effect large enough to account for the active-group effect.

“Not sufficient” should be evaluated with pre-specified practical-effect bounds and confidence intervals, not only with failure to reach a significance threshold.

## Stopping criteria

Stop planned enrollment when:

- the pre-registered animal-level precision or power target is met;
- all included animals have completed the same pre-specified sampling schedule;
- predefined QC criteria have been evaluated.

Do not stop early solely because the result appears positive or negative.

---

# 7. Interpretation of possible outcomes

| Result pattern | Interpretation |
|---|---|
| Opsin-positive animals show a retrieval-window-specific accuracy deficit; controls do not; movement and sensory measures remain within pre-specified practical bounds. | Strongest evidence that P-to-Q signaling is necessary during the tested retrieval interval. |
| Effect occurs during cue light but not post-cue delay light. | P-to-Q may contribute to cue processing, cue-triggered retrieval, or attention. This does not isolate memory retrieval from sensory processing. |
| Effect occurs during movement-window light, with altered speed/trajectory or increased failure to execute movement. | A motor or action-execution contribution is likely; do not claim a retrieval-specific requirement. |
| Light affects opsin-negative animals. | Visible light, heating, or another nonspecific light effect is plausible. Do not attribute the behavioral result uniquely to P-to-Q inhibition. |
| Retrieval light increases omissions or broken holds without increasing incorrect committed choices. | Could reflect arousal, engagement, movement initiation, or task-state disruption rather than incorrect retrieval. |
| No effect despite verified terminal inhibition. | P-to-Q signaling may be unnecessary under these task conditions, redundant with another pathway, required in another time window, or the behavioral assay may lack sensitivity. |
| No verified terminal inhibition. | The negative behavioral result is uninterpretable as evidence against P-to-Q necessity. |

---

# 8. Troubleshooting and limits

## If no behavioral effect is found

Check, in order:

1. Was P-derived signaling in Q actually inhibited?
2. Was the implant correctly located in Q?
3. Did the light dose meet functional inhibition criteria without nonspecific effects?
4. Was the retrieval interval sufficiently separated from movement?
5. Was baseline performance stable but not at an uninformative ceiling or floor?
6. Was the chosen retrieval window correct, or was relevant processing earlier or later?
7. Could another P output or another circuit compensate?

Do not increase light intensity indefinitely. Recalibrate against terminal inhibition and opsin-negative nonspecific effects.

## If movement is altered

If retrieval-window light changes speed, trajectory, movement initiation, or central holding, move the perturbation earlier in a stationary enforced-hold interval and repeat. If motor effects remain, the experiment cannot cleanly distinguish retrieval from motor control.

## If visible light is detected or control animals change behavior

Improve shielding and masking, then repeat validation. If matched light still affects opsin-negative animals, retain that effect in the interpretation and do not make a projection-specific causal claim.

## Fundamental limitation

Even with successful terminal inhibition in Q, the strongest justified statement is about the necessity of **acute P-derived signaling in Q under the tested task and time window**. The experiment does not establish that P-to-Q is the sole retrieval route, nor does it establish a general requirement outside this learned-choice context.
