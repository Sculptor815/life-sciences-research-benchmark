# GPT-5.6 Sol / neu-d01

Original final answer, shared by both scoring rounds.

# Recommended design

Use **projection-targeted inhibitory opsin expression in P neurons that project to Q, but illuminate their axon terminals locally in Q during a cue-sampling/retrieval epoch that ends before locomotion begins**. Randomize light delivery trial by trial and compare with an identically targeted opsin-negative control group receiving the same light.

This is preferable to illuminating P somata: because P also projects elsewhere (O1), somatic inhibition of P→Q-projecting neurons could suppress collateral outputs and would test the cell population, not specifically the P→Q projection. A claim that P→Q is necessary is warranted only if validated Q-terminal inhibition selectively reduces correct choices during the retrieval window, while task-matched movement and visible-light controls exclude material motor or sensory effects.

---

## 1. Question, estimand, and interpretation

### Primary causal question

Does transient suppression of transmission from projection-defined P neurons at their terminals in Q during cue retrieval reduce the probability of a correct choice?

### Primary comparison

The planned effect is the interaction:

> **[cue-window light effect in opsin animals] − [cue-window light effect in opsin-negative controls]**

Light-off trials within each animal provide baseline performance; the control group estimates effects of visible light, illumination-associated heating, tethering, and other light-delivery artifacts.

### Scope of a positive conclusion

A positive result would support:

> Normal activity/transmission in the experimentally reached P→Q axons is necessary for normal choice performance during the tested cue-related interval and task conditions.

It would not by itself prove that P→Q stores the learned association, or distinguish retrieval from cue perception or short-term maintenance unless those alternatives are addressed with additional task controls.

---

## 2. Explicit evidence-to-inference-to-conclusion chain

1. **Evidence O1:** P projects to Q and to another region.  
   **Inference:** Inhibiting P→Q-projecting somata may also suppress their collateral output to the other target.  
   **Design consequence:** Illuminate projection-defined axons locally in Q rather than P somata. Validate that Q illumination does not materially suppress output at the other P target.  
   **Conclusion enabled:** A pathway-level interpretation is more credible than with somatic illumination, although local terminal illumination still requires physiological specificity checks.

2. **Evidence O2:** Inhibitory opsin expression can be targeted to P neurons projecting to Q.  
   **Inference:** The relevant neuronal population can be accessed.  
   **Design consequence:** Use that targeting method, with inhibitory opsin in the experimental group and a matched non-inhibitory reporter/control construct in controls.  
   **Conclusion enabled:** Differences caused specifically by activating the inhibitory construct can be estimated.

3. **Evidence O3:** Correct choice is the proposed outcome, but the task requires locomotion.  
   **Inference:** Reduced correct choices could result from impaired initiation, speed, trajectory, or completion rather than impaired retrieval.  
   **Design consequence:** Temporally separate cue sampling from movement when possible, measure detailed kinematics and omissions, and include response-window and task-matched motor controls.  
   **Conclusion enabled:** Necessity for cue-guided choice can be claimed only if the accuracy effect is not explained by a material motor deficit.

4. **Evidence O4:** Light may be visible to the animal.  
   **Inference:** Light could distract, startle, obscure a cue, or become an additional predictive cue.  
   **Design consequence:** Shield and mask light, make it nonpredictive, and give the identical light pattern to opsin-negative controls. Directly assay orienting and cue detection under illumination.  
   **Conclusion enabled:** An opsin-specific effect can be separated from a visible-light effect.

---

# 3. Operational ordered protocol

## Step 1 — Define the behavioral epoch and stabilize performance

1. Train animals to stable performance on the learned choice task before intervention.
2. Operationally define:
   - cue onset and offset;
   - the interval in which the animal must sample the cue;
   - earliest movement onset;
   - choice commitment;
   - reward or outcome delivery.
3. Preferably impose a stationary start position or hold period:
   - present the cue while the animal must remain stationary;
   - apply inhibition during cue presentation/retrieval;
   - stop light before the release/go event;
   - allow a calibrated recovery interval before locomotion.
4. If the existing task cannot temporally separate cue retrieval from movement, retain it but acknowledge weaker causal localization. Use high-resolution movement tracking and temporally matched response-window inhibition.

**Unreported parameters:** retrieval-window duration, required hold duration, and recovery interval.  
**Calibration:** derive them from task-event timing, observed movement-onset distributions, and physiological measurements of inhibition onset and recovery. Do not select them after examining the main behavioral outcome.

## Step 2 — Prepare experimental and control groups

### Experimental group

- Target the inhibitory opsin to P neurons projecting to Q, using the available projection-targeting approach.
- Place light delivery over Q to illuminate the targeted axons/terminals locally.

### Primary control group

- Apply the same targeting and surgical procedures with a matched non-inhibitory reporter/control construct.
- Deliver the identical light patterns over Q.

### Optional anatomical light-site control

- In a separate group or counterbalanced preparation, place light adjacent to but outside Q while retaining the inhibitory construct. This can help identify effects caused by light spread or nonspecific tissue perturbation, but it is supplementary to the opsin-negative control.

### Laterality

Whether inhibition must be unilateral or bilateral is unreported. Determine this from the anatomy and task structure before the main study. If both hemispheres may independently support the behavior, bilateral intervention is the more direct necessity test; unilateral intervention may instead test lateralized contribution.

## Step 3 — Calibrate light and validate inhibition

### Proposed physiology experiment

Before the main behavioral test, determine whether Q illumination:

1. suppresses a measurable P-derived response or transmission in Q;
2. acts rapidly enough for the intended cue window;
3. recovers before the motor period;
4. does not produce comparable changes in opsin-negative controls;
5. does not materially suppress P output at the other projection target.

Use the lowest illumination that reaches a prespecified, reproducible level of pathway suppression while avoiding detectable control-group effects. The required suppression level, illumination intensity, pulse structure, and recovery period are unreported and must be established in pilot physiology rather than assumed.

If direct terminal illumination fails to suppress P→Q transmission reliably, the behavioral experiment cannot support a negative conclusion about necessity.

### Anatomical quality checks

Conduct checks blind to behavioral outcome:

- targeted expression in P neurons associated with the Q projection;
- axonal expression in Q;
- light-delivery placement and estimated coverage of Q;
- absence of gross expression or illumination outside intended bounds;
- assessment of whether illuminated axons pass through Q without terminating there;
- implant integrity and tissue quality.

Set quantitative inclusion boundaries before outcome unblinding, using the distribution from calibration animals rather than choosing boundaries based on behavioral effects.

## Step 4 — Control visible light

1. Use opaque ferrules, patch-cable coverings, and head-mounted shielding.
2. Maintain constant, noninformative background illumination if compatible with cue perception.
3. Quantify light leakage around the head under the exact experimental configuration.
4. Acclimate both groups equally to cables, shielding, and randomized light delivery.
5. Ensure light condition is balanced across:
   - cue identity;
   - correct choice side;
   - reward history;
   - trial number and session;
   - preceding trial condition.
6. Never allow light to predict the correct action or reward.
7. Record orienting, startle-like movement, head turning, or interruption of cue sampling at light onset.

If the task cue is visual, include a separate cue-detection or cue-discrimination calibration under identical visible-light conditions. The purpose is to test whether illumination degrades access to the sensory cue independently of mnemonic retrieval.

## Step 5 — Define independent units and sample size

- The **animal** is the biological independent unit.
- Trials are repeated observations nested within animal; they are not independent biological replicates.
- Sessions may form an additional nested level if substantial session-to-session variation exists.

Determine animal number prospectively using a pilot-informed or simulation-based power analysis for the planned mixed-effects model. Specify:

- the smallest scientifically meaningful decrease in correct-choice probability;
- expected between-animal variability;
- within-animal trial correlation;
- expected exclusions and missing trials.

Increasing trial count cannot substitute indefinitely for increasing the number of animals.

## Step 6 — Allocation and blinding

1. Randomly allocate animals to inhibitory-opsin or control construct.
2. Stratify allocation by baseline accuracy and, where relevant, cue or side bias.
3. Conceal construct identity from:
   - behavioral testers;
   - trial-quality scorers;
   - movement-video scorers;
   - primary analysts until exclusions and the analysis dataset are locked.
4. Generate trial-condition schedules by computer or another prespecified random procedure.
5. Apply anatomical and physiological inclusion criteria without access to behavioral group effects.

## Step 7 — Intervention and trial sampling

Within each animal, sample the following conditions in randomized, balanced order:

1. **Cue/retrieval-window light:** principal test.
2. **No-light trials:** within-animal baseline.
3. **Pre-cue light:** controls for nonspecific state changes and anticipatory effects.
4. **Response/movement-window light:** tests whether pathway inhibition directly impairs locomotor execution.
5. **Post-choice light:** controls for nonspecific illumination effects; it cannot causally alter a choice already committed.

Use the same photon exposure or the closest physiologically appropriate match across timing-control conditions. Ensure the intertrial interval exceeds the calibrated recovery time. If effects persist across trials, use counterbalanced blocks or sessions with a validated washout period rather than trial-wise randomization.

Include all eligible trials after trial initiation. Do not discard trials merely because the animal omitted a choice or moved slowly; these outcomes may be caused by the intervention.

---

# 4. Measurements

## Primary outcome

Probability of a correct choice per eligible trial.

Prespecify how omissions are handled. A robust approach is:

- primary: correct versus not correct, with omissions counted as not correct;
- secondary: multinomial decomposition into correct, incorrect, and omission;
- supportive: accuracy among completed choices.

This prevents an apparent accuracy change caused solely by selectively excluding omitted trials.

## Movement outcomes

Measure at minimum:

- maintenance or breaking of the stationary hold;
- latency to initiate movement;
- movement speed and acceleration;
- path length and trajectory;
- time to reach the choice location;
- choice completion and omission rate;
- left/right or other directional bias;
- head or body orientation at light onset.

Use automated tracking where possible, with blinded manual review of uncertain trials.

## Sensory and light-related outcomes

Measure:

- cue-sampling duration;
- orientation or startle at light onset;
- failure to attend to the cue;
- cue-detection or discrimination performance under identical light;
- any control-group change in accuracy, latency, or trajectory caused by light.

## Quality and state variables

Record implant connection, trial number, session, cue identity, correct side, prior outcome, and any prespecified signs of equipment failure. These variables can improve precision but should not be used for post hoc exclusion.

---

# 5. Controls needed for interpretation

## Essential controls

1. Opsin-negative animals receiving identical Q light.
2. Light-off trials in both groups.
3. Retrieval-window versus response-window inhibition.
4. Movement tracking on every main-task trial.
5. Anatomical verification of expression and light placement.
6. Physiological verification that Q illumination suppresses P→Q transmission.

## Strongly recommended controls

### Task-matched motor control

Use trials with the same locomotor route and reward collection but with the choice removed or directly instructed. Apply the same cue-window and response-window light. Impairment here would indicate a motor, motivational, or action-execution contribution.

### Sensory control

Use a task version in which the same cue modality directly instructs a response and minimizes retrieval of the learned choice association. If illumination disrupts this performance in both groups, cue-window results in the main task are sensory-confounded.

### Collateral-output check

Because P has another target (O1), measure whether Q-local light changes P-derived activity or transmission at that other target. A material effect would weaken projection specificity and could make the result resemble somatic inhibition of a collateralized cell population.

---

# 6. Prespecified analysis

## Primary model

Use a mixed-effects logistic model for correct choice, with:

- fixed effects for construct group, light condition, timing window, and their interactions;
- relevant prespecified task factors such as cue identity, correct side, and session;
- animal random intercepts and, if supported by the data, random slopes for light condition.

The main planned contrast is the group-by-cue-light interaction. Report effect size as an absolute change in correct-choice probability and/or odds ratio with uncertainty intervals, not only a significance value.

## Secondary analyses

1. Multinomial model for correct, incorrect, and omission outcomes.
2. Mixed models for initiation latency, speed, trajectory, and hold breaks.
3. Planned timing contrasts:
   - cue light versus pre-cue light;
   - cue light versus response light;
   - cue light versus post-choice light.
4. Control-group light effects to estimate visible-light and heating artifacts.
5. Cue-side and choice-side interactions to identify directional motor effects.

Do not make adjustment for post-intervention movement variables the primary analysis, because movement may be a mediator and conditioning on it can bias the estimate. Movement-matched or intact-hold analyses may be reported as sensitivity analyses.

## Equivalence rather than “no significant effect”

To argue that movement or visible-light effects are too small to explain an accuracy deficit, use prespecified equivalence bounds. Derive bounds during calibration from:

- baseline relationships between movement changes and accuracy;
- the smallest sensory or motor disturbance that could plausibly account for the target accuracy effect;
- precision achievable in the control group.

A nonsignificant motor or control-group result alone is not evidence that the confound is absent.

---

# 7. Acceptance and stopping criteria

## Criteria for a positive necessity result

All of the following should be met:

1. Valid anatomical targeting and light placement.
2. Validated suppression of P→Q transmission during the intended window.
3. Recovery before locomotion in the temporally separated design.
4. A prespecified reduction in correct choices specifically in opsin animals during cue-window light.
5. The group-by-light interaction excludes the smallest meaningful effect in the null direction.
6. No material visible-light effect in opsin-negative controls.
7. No movement change large enough to explain the choice effect.
8. No comparable impairment during post-choice light.
9. No evidence that Q illumination suppresses the collateral output sufficiently to account for the result.

## Interpretation of a null result

A null result supports “not necessary under these tested conditions” only if inhibition, targeting, statistical precision, and behavioral engagement all pass validation. Otherwise the result is inconclusive.

## Session and study stopping

Prespecify session stopping for:

- hardware or light-delivery failure;
- loss of stable task engagement across all conditions;
- excessive omissions relative to a bound derived from each animal’s stable baseline;
- inability to maintain the required stationary cue period;
- welfare concerns.

Stop enrollment at the preregistered sample size. Do not stop early after informal inspection of accuracy unless a formal sequential design was specified in advance.

---

# 8. Troubleshooting and decision rules

- **Accuracy falls and movement also changes materially:** Do not claim retrieval-specific necessity. Shorten or move inhibition earlier, increase cue–movement separation, and repeat after physiological recovery calibration.
- **Opsin-negative controls react to light:** Improve shielding or masking and habituation. If the cue is visual, redesign the sensory control or use a configuration with less leakage.
- **Cue-window and response-window inhibition produce similar deficits:** A motor/action contribution is likely; retrieval specificity is unsupported.
- **Only omissions increase:** Treat this as a possible engagement or motor effect, not automatically as incorrect retrieval.
- **No behavioral effect but weak physiological inhibition:** Inconclusive; improve targeting or light delivery before increasing behavioral sample size.
- **Q light also suppresses the other P target:** The projection-specific claim fails. Interpret as perturbation of a collateralized P→Q-defined population or redesign the local intervention.
- **Terminal suppression cannot be validated:** Somatic inhibition remains an alternative, but its conclusion must be restricted to “P neurons projecting to Q are necessary,” not “the P→Q projection is necessary.”
- **Visible-light effects remain despite masking:** Use the opsin-negative interaction as the principal estimator, but if the sensory effect is large or interacts with cue identity, the main retrieval test remains ambiguous.

---

## Main limitation

Even a clean, temporally selective result establishes necessity of normal P→Q signaling during a cue-related interval, not the exact computation performed by the pathway. Distinguishing retrieval from cue perception, attention, or maintenance requires the stationary timing design plus sensory and task-variant controls. The strongest conclusion should therefore remain tied to the tested interval, degree of inhibition, and learned-choice context.
