# GPT-6 Astra / neu-d01

Original final answer, shared by both scoring rounds.

## Recommendation

**Use projection-targeted inhibition delivered locally in Q during a prespecified cue-associated retrieval window, with interleaved light/no-light trials, an opsin-negative light-control group, and explicit sensory and movement controls.** Do not rely on correct choices alone.

Inhibiting the somata of Q-projecting P neurons would test the necessity of that **neuronal population**, not specifically its output to Q. Local inhibition of their terminals in Q is the better pathway-level test—but only if terminal inhibition is effective, temporally appropriate, and sufficiently localized.

**All procedures below are proposed experiments, not reported results.** The packet does not specify the species, task timing, opsin, targeting method, optical parameters, laterality, effect size, or sample size. These require calibration.

## Evidence → inference → conclusion

| Evidence location | Supported inference | Consequence for the experiment |
|---|---|---|
| **O1:** P projects to Q and another region. | Perturbing P could affect more than P→Q transmission. O1 does **not** establish whether individual Q-projecting neurons collateralize to the other region. | Prefer illumination of P terminals within Q. Examine collateral anatomy and test for effects outside Q where feasible. |
| **O2:** Inhibitory opsin expression can target Q-projecting P neurons. | Projection-defined expression is feasible, but effective inhibition at terminals is not established. | Validate expression specificity and light-induced suppression of P→Q transmission before interpreting behavior. |
| **O3:** The outcome is correct choices, and the task requires locomotion. | Fewer correct choices could reflect impaired movement, failure to initiate, or altered choice execution rather than retrieval failure. | Separate retrieval from locomotion where possible; measure accuracy, omissions, movement initiation, and movement execution separately. |
| **O4:** Light can be visible. | Light could distract, mask the cue, become an additional cue, or alter behavior independently of neural inhibition. | Match illumination in opsin-negative animals, reduce and test light leakage, and include perceptual controls. |

**Conditional conclusion:** A selective, validated P→Q perturbation that reduces choice accuracy during the cue window, without meaningful sensory or motor impairment, would support a requirement for P→Q transmission for **normal cue-associated task performance**. Calling the effect specifically a retrieval deficit requires additional evidence separating retrieval from cue perception, attention, and response selection.

---

# Ordered operational protocol

## 1. Preparation and quality checks

### Define the causal question and task epochs

Prespecify the target contrast:

> Does reducing P→Q transmission during the cue-associated retrieval epoch impair expression of a previously learned cue–choice association?

Identify cue onset/offset, movement onset, choice commitment, and outcome delivery from recorded task events and video or equivalent movement tracking. Do not assume that cue presentation precisely brackets retrieval.

**Preferred task arrangement:** Present the retrieval cue while the animal is stationary, followed by a delayed “go” event permitting locomotion. End inhibition sufficiently before movement to allow physiological recovery.

- If the existing task already separates these events, retain it.
- If it does not, a delayed-response version is a **proposed task modification** requiring training and baseline validation. Its results apply directly to that modified task, not automatically to the original.
- If retrieval and locomotion cannot be separated, retain the original task but acknowledge that timing alone cannot establish a retrieval-specific effect.

Establish stable learned performance under the planned task and masking conditions before perturbation. Define stability and acceptable omission rates in advance using baseline data.

### Anatomical preparation

Use a validated targeting implementation consistent with **O2**, expressing the inhibitory opsin in Q-projecting P neurons. Place illumination to cover their terminal field in Q.

Measure:

- Expression location and specificity in P.
- Terminal distribution in Q.
- Optical implant location and expected illuminated volume.
- Expression or illumination outside the intended structures.
- Whether the targeted population has detectable collateral projections, especially to the other region identified in **O1**.

Choose unilateral or bilateral coverage from anatomical and task mapping; this parameter is **unreported**. Incomplete coverage must constrain interpretation of a negative result.

Complete final anatomical verification after testing, using criteria assessed without access to behavioral treatment effects.

### Physiological and optical calibration

Do not assume that an inhibitory opsin effective at somata effectively suppresses terminals.

In a validation cohort or suitable experimental subset:

1. Identify a P-driven response in Q and establish that the assay measures P→Q transmission rather than nonspecific Q activity.
2. Measure suppression across a range of light intensities and durations.
3. Measure onset, offset, recovery, and any post-light disturbance.
4. Select the lowest exposure that achieves a prespecified, reproducible suppression criterion with acceptable localization and recovery.
5. Where feasible, measure P activity and P-driven responses in the other output region during Q illumination. Effects there would weaken pathway specificity.

Calibrate illumination spread, delivered power, hardware timing, and visible leakage. Check matched illumination in opsin-negative preparations for nonspecific effects.

**Unreported parameters:** wavelength, intensity, pulse pattern, exposure duration, expression interval, implant geometry, and recovery interval. Determine them from these calibration measurements; do not substitute generic settings.

## 2. Independent units and sample planning

- **Biological independent unit:** the animal—not the trial, neuron, fiber, hemisphere, or session.
- Repeated trials improve each animal’s effect estimate but do not replace independent animals.
- Account for shared batch, litter, or other clustering if present and relevant.

Use pilot or baseline data to estimate between-animal variation, within-animal trial dependence, expected omissions, and technical attrition. Plan the sample size around:

1. A prespecified minimum meaningful accuracy deficit.
2. Precision needed to assess meaningful motor and sensory effects.
3. Expected losses from prospectively defined targeting failures.

Pilot work used to tune the intervention should be distinguished from the confirmatory dataset.

## 3. Allocation and blinding

Randomly allocate animals to:

- **Projection-targeted inhibitory opsin.**
- **Matched opsin-negative control**, with otherwise comparable targeting procedures, surgery, handling, and illumination.

Balance allocation on important measured baseline characteristics, including task performance. Specify any balancing variables before assignment.

Within animals, use concealed, computer-generated allocation of light/no-light trials and intervention windows, balanced across cue identity, required choice, session progression, and other known task conditions.

Blind behavioral scoring, anatomical inclusion decisions, and primary analysis to group identity. If the operator can see light delivery, automate trial control and retain objective recordings. Document any unavoidable unblinding.

## 4. Intervention and sampling

Use the following conditions:

1. **No-light baseline trials.**
2. **Cue-window inhibition:** the primary test.
3. **Movement-window inhibition:** a control for sensitivity of choice execution or locomotion to perturbation.
4. **Non-retrieval timing control:** a justified task epoch outside cue processing, movement, and outcome processing.

Match optical exposure across timing conditions when feasible without crossing functional boundaries. If matching requires inappropriate overlap, retain the valid windows and report the exposure difference.

For cue-window trials:

- Assign the condition before illumination and before any treatment-induced behavior.
- Trigger light from a recorded task event.
- Verify actual delivery timestamps.
- End light according to measured recovery kinetics, not merely the nominal cue offset.

Determine intertrial recovery empirically. Check whether effects carry into the following trial; lengthen recovery or change the randomization scheme if necessary. Keep illumination unrelated to the correct answer or reward contingency so it cannot serve as an informative task cue.

If the retrieval epoch is uncertain, conduct a **separate timing-calibration experiment** using prespecified adjacent windows. A temporal profile can localize vulnerability, but timing alone does not identify the cognitive process.

## 5. Measurements

### Primary behavioral endpoint

Measure the probability of a correct choice across **all eligible trials defined before intervention**. Report errors and omissions separately.

Also report accuracy among completed choices, but only as a secondary endpoint: excluding animals’ failures to move after treatment could conceal a motor deficit.

### Movement and execution endpoints

Record:

- Movement initiation and failure to initiate.
- Cue-to-movement and movement-to-choice latencies.
- Speed, acceleration, path length, and trajectory.
- Pauses, premature departures, and failures to reach a choice location.
- Choice-side bias and, where relevant, side-specific movement effects.

Separate movements before commitment from movements after an incorrect choice; the latter may be consequences rather than causes of the error.

### Sensory and task-engagement endpoints

Measure cue detection/discrimination, trial engagement, and outcome collection where the task allows. Include task-relevant orienting or other observable sensory responses if validated.

Synchronize these measurements with cue events, illumination, and choice events.

## 6. Controls addressing alternative explanations

| Control | Question addressed | Interpretation limit |
|---|---|---|
| Opsin-negative animals receiving identical Q illumination | Does light, heating, hardware, or handling alter behavior without the opsin? | A null result requires adequate precision; it does not establish every aspect of neural specificity. |
| No-light trials in both groups | Are baseline performance and expression-related effects comparable? | Baseline differences can complicate treatment comparisons and create floor/ceiling effects. |
| Light shielding plus constant, noninformative masking illumination, if compatible with the cue | Can visibility of experimental light be reduced? | Masking itself must not impair the task cue. |
| Matched visible-light control without inhibitory illumination in Q, calibrated to reproduce the animal’s visual exposure | Could visible light distract or function as an extra cue? | Matching must be measured or behaviorally validated, not assumed. |
| Cue-detection/discrimination control with matched sensory conditions and minimal retrieval demands | Is the effect attributable to impaired perception of the cue? | No control is perfectly free of attention, learning, or decision demands. |
| Instructed/forced-choice movement trials with similar timing, routes, and movement demands but reduced associative-choice demand | Does the same cue-window perturbation compromise subsequent movement? | Easier or poorly matched movement controls may miss relevant impairment. |
| Movement-window and non-retrieval-window illumination | Is vulnerability concentrated in the proposed retrieval epoch? | Different windows may differ in circuit engagement; this is not proof of mnemonic specificity. |

For light visibility, use a separate behavioral detection assay if necessary. Failure to detect illumination supports only the tested detection limit—not absolute invisibility.

The motor control should include **the same cue-window illumination followed by matched movement**, not just illumination during movement. This tests delayed consequences of the primary perturbation.

## 7. Analysis

Prespecify a primary opsin-specific light contrast:

\[
(\text{cue-light} - \text{no-light})_{\text{opsin}}
-
(\text{cue-light} - \text{no-light})_{\text{control}}.
\]

Estimate this contrast with an animal-level paired analysis or a hierarchical binary-outcome model accounting for trials and sessions nested within animals. Report marginal probability differences, uncertainty intervals, and individual-animal effects.

Include prespecified cue, choice-side, session, and treatment-order terms where justified. Evaluate carryover using prior-trial condition. Avoid selecting covariates based on which analysis produces significance.

Analyze omissions, wrong choices, and movement endpoints separately. Do **not** simply adjust accuracy for post-treatment speed or analyze only successful movers as the primary causal test: movement may itself be affected by inhibition.

For sensory and motor controls, define equivalence bounds representing the smallest confound large enough to threaten interpretation. “Not statistically significant” is insufficient evidence of preservation. Report when intervals remain too wide to exclude meaningful impairment.

Prespecify timing comparisons and multiplicity handling. Label additional windows, subgroup analyses, or revised endpoints exploratory.

## 8. Acceptance and stopping criteria

### Technical acceptance gates

Require, before the confirmatory interpretation:

- Acceptable targeting and Q coverage.
- Demonstrated P→Q suppression at the selected exposure.
- Recovery appropriate to the intended window.
- Adequate optical localization.
- Stable baseline performance.
- Light visibility addressed to a stated evidential bound.

Specify thresholds from calibration before confirmatory analysis. Exclude animals or sessions only under documented, outcome-independent technical or welfare rules. Report all exclusions and reasons.

### Criteria for a positive necessity interpretation

Require an opsin-specific cue-window accuracy deficit of meaningful magnitude, together with:

- Verified target engagement.
- No sensory or motor effect large enough to plausibly explain the deficit within the prespecified bounds.
- Timing and localization evidence consistent with the proposed claim.

These observations would support—not logically prove—a retrieval-specific interpretation.

### Stopping rules

Stop or pause for welfare concerns, tissue or implant problems, unreliable delivery, major baseline deterioration, unanticipated persistent effects, or failed physiological specificity.

Use a fixed confirmatory sample or a prespecified sequential rule. Do not stop at the first significant behavioral result or increase light until a deficit appears.

## 9. Troubleshooting

- **No behavioral effect:** Check coverage, inhibition strength, recovery timing, task sensitivity, and compensation opportunities. A null under weak inhibition is not evidence of dispensability.
- **Errors accompanied by slower movement or more omissions:** Treat the result as mixed performance impairment. Improve temporal separation and matched-movement controls before attributing it to retrieval.
- **Light affects control animals:** Repair shielding or masking, reassess visibility and cue interference, then validate the revised setup before confirmation.
- **Cue discrimination is impaired:** The experiment cannot isolate retrieval from sensory processing. Add appropriately matched perceptual controls or use a separate task version, acknowledging changed generalization.
- **Q illumination alters P or another P output:** Restrict the claim to perturbation of Q-projecting P neurons/axons with possible extra-Q effects. Improve localization or explicitly retain that limitation.
- **Post-light effects overlap movement:** Recalibrate exposure and recovery, or use a validated intervention with more suitable kinetics. Do not describe the manipulation as retrieval-only.

## Alternatives and limits

**Somatic inhibition in P** is a useful complementary experiment testing Q-projecting P neurons, but it cannot substitute for a localized P→Q test. **Inhibiting Q generally** tests Q’s involvement, not specifically the P input. **Recording during cues** can inform timing but cannot establish necessity.

A clean positive result supports a contribution necessary for **normal performance**, not necessarily an absolute requirement for every correct choice. A clean null constrains the importance of the inhibited transmission under the achieved suppression, timing, and task conditions; it does not establish universal dispensability.

The decisive uncertainties are terminal efficacy, extra-Q effects, the actual retrieval window, and sensory/motor preservation. Failure to resolve any of these should narrow the conclusion to **cue-period task-performance involvement**, rather than a specific mnemonic necessity claim.
