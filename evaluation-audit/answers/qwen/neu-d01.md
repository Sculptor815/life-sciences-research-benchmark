# Qwen3.8 Max (0902) / neu-d01

Original final answer, shared by both scoring rounds.

## Recommendation

Use a **projection-specific, epoch-specific optogenetic inhibition test**: express an inhibitory opsin selectively in **P neurons that project to Q** and deliver light **locally in Q during the cue-retrieval epoch only**. Compare correct choices to no-light trials and to control illumination epochs, in both opsin-bearing and control animals. This design can support the conclusion that **P-to-Q activity is necessary for cue retrieval** only if the behavioral deficit is specific to the retrieval epoch, absent or smaller in light-only/control animals, and not explained by changes in locomotion, motivation, cue detection, or visibility/aversion of the light itself.

Because the evidence states that **P projects to Q and to another region** (O1), the cleanest manipulation is **terminal inhibition in Q**, not broad inhibition of P. Because correct choice requires locomotion (O3), the protocol must separate mnemonic choice from movement execution. Because the light can be visible to the animal (O4), the protocol must include sensory and behavioral light controls and automated blinded scoring.

---

## Evidence-to-inference-to-conclusion chain

| Evidence | Inference | Design consequence |
|---|---|---|
| **O1: P projects to Q and to another region.** | Inhibiting all P neurons would not isolate the P-to-Q pathway. Even inhibiting P neurons that project to Q at the soma could affect collateral outputs if the same neurons project elsewhere. | Use **projection-targeted expression** plus **local illumination of Q terminals** to preferentially test the P-to-Q synapse/output during behavior. |
| **O2: Inhibitory opsin expression can be targeted to P neurons projecting to Q.** | The required genetic access exists in principle. | Use a projection-targeted inhibitory opsin preparation, with validation of expression specificity and terminal localization. |
| **O3: The proposed outcome is correct choices, but the task also requires locomotion.** | A reduction in correct choices could reflect impaired retrieval, but could also reflect impaired movement initiation, speed, motivation, or action execution. | Add delayed/hold trial structure if possible; measure locomotion precisely; include movement-only control epochs and separate locomotion assays. |
| **O4: Light delivery can be visible to the animal.** | Light could serve as an extra sensory cue, distractor, aversive stimulus, or arousal stimulus, independently of opsin activation. | Include control animals receiving light without opsin, light-alone catch trials, non-retrieval light controls, intensity calibration, and blinded automated scoring. |

**Conclusion supported by the design:**  
If retrieval-epoch light suppresses correct choices in opsin animals but not in control animals, and does not produce equivalent effects during movement-only or non-retrieval epochs, and does not impair basic locomotion or cue detection, then the evidence supports the conclusion that **P-to-Q transmission is necessary during cue retrieval**. If light impairs movement generally or affects control animals similarly, the result is not interpretable as a retrieval-specific necessity.

---

## Explicit causal assumptions

Label these as assumptions, not established facts.

1. **A1: Retrieval can be bounded in time.**  
   Cue retrieval is assumed to occur after cue onset and before the animal commits to a locomotor response. If retrieval overlaps movement, the epoch must be redesigned or the inference weakened.

2. **A2: Local light delivery to Q can inhibit P-to-Q terminals sufficiently.**  
   The opsin must be expressed in P-to-Q axons and capable of suppressing neurotransmission or terminal excitability when illuminated in Q.

3. **A3: Local illumination of Q does not primarily manipulate fibers of passage or unrelated circuits.**  
   Light spread must be limited and histologically/behaviorally controlled.

4. **A4: The visible light used for optogenetics can be made approximately behaviorally neutral, or its non-specific effects can be estimated with controls.**  
   If light is unavoidably salient or aversive, inference depends on differential effects in opsin versus control animals and on epoch controls.

If any of these assumptions fails, the recommendation changes: use a different task epoch, validate terminal inhibition directly, reduce light intensity, change opsin/wavelength, or accept that the test is inconclusive.

---

# Operational protocol

## 1. Preparation and quality checks

### 1.1 Define the learned choice task and retrieval epoch

Use a learned cue-guided two-choice task in which the animal must choose one of two locomotor targets based on a cue.

Preferred structure:

1. Animal starts in a center zone.
2. Cue is presented.
3. Optional delay/hold period is imposed before locomotion is permitted.
4. Go signal permits locomotion.
5. Animal moves to left or right choice port.
6. Correct choice is rewarded.

The preferred task includes a **delay or hold period** because it separates cue retrieval from locomotion. If the animal cannot be trained with a delay, then use a free-response version but define epochs behaviorally.

**Operational epoch definitions:**

- **Cue epoch:** cue onset to cue offset.
- **Retrieval/decision epoch:** cue onset to response commitment.  
  If a delay is used: cue onset to go signal or cue onset to first sustained movement toward a choice port, whichever is appropriate.
- **Movement-execution epoch:** response commitment or go signal to choice-port entry.
- **Outcome epoch:** port entry to reward consumption.

**Quality check:** Calibrate epoch boundaries using video tracking and event timestamps. Define response commitment from baseline movement distributions, for example the time at which sustained trajectory deviation toward one port begins. Do not invent fixed latency thresholds without pilot calibration.

---

### 1.2 Choose the projection-specific inhibition strategy

Because P projects to Q and another region (O1), the primary manipulation should be:

1. Target inhibitory opsin expression to P neurons that project to Q (O2).
2. Implant optic fiber over Q.
3. Illuminate Q during selected epochs to inhibit P-to-Q terminals locally.

This tests the necessity of the **P-to-Q output in Q**, rather than the necessity of P broadly.

**Assumption to verify:** the chosen inhibitory opsin must be suitable for axon-terminal suppression. If expression is soma-restricted or terminal expression is poor, the test is invalid. Verify terminal expression in pilot animals.

---

### 1.3 Calibration of surgical and expression parameters

Coordinates, viral volume, titer, promoter suitability, expression time, and fiber size are not specified in the evidence. Treat them as unknown and calibrate rather than assume.

**Calibration procedure:**

1. Use a small pilot cohort to map P and Q placement with tracer injections or other standard anatomical verification approved by the facility.
2. Adjust injection location and volume until expression is detectable in P neurons retrogradely labeled from Q, with minimal spread into adjacent structures.
3. Verify expression timecourse in pilot animals before behavioral testing.
4. Proceed only when pilot histology shows:
   - opsin expression in P,
   - projection labeling consistent with P-to-Q targeting,
   - no gross off-target expression affecting nearby regions,
   - fiber placement over Q.

Do not infer from animals with misplaced fibers or clear off-target expression.

---

### 1.4 Optical hardware calibration

Because light may be visible to the animal (O4), optical calibration is essential.

**Calibration procedure:**

1. Measure light output at the fiber tip with a power meter before each test phase.
2. Check fiber integrity and connector cleanliness.
3. Measure or estimate light leakage around the implant if feasible.
4. Use the lowest light intensity and shortest duration compatible with effective inhibition.
5. If the opsin permits, consider longer-wavelength variants that may reduce visual salience, but only if this is compatible with the inhibitory opsin being used.
6. Calibrate light intensity in pilot animals by testing a range of powers and durations while monitoring:
   - behavior in control animals,
   - movement metrics,
   - orienting or aversive responses,
   - task performance.

The chosen light parameters should be the lowest that produce a putative inhibition-related behavioral effect in opsin animals without producing comparable changes in control animals.

---

### 1.5 Baseline behavioral quality checks

Before optogenetic testing, animals must reach stable learned performance.

**Required checks:**

1. Stable correct-choice performance across sessions without light.
2. Stable locomotion metrics across sessions.
3. No signs of pain, infection, weight loss, or impaired motivation.
4. If reward restriction is used, monitor body weight and health according to institutional standards.
5. Confirm that cue detection is intact by ensuring animals respond to both cue types at comparable baseline rates.

If baseline performance is unstable, do not proceed to optogenetic testing.

---

## 2. Independent units, allocation, and blinding

### 2.1 Independent experimental unit

The **animal** is the primary independent unit for inference. Trials and sessions are nested within animals and must not be treated as independent replicates.

If both hemispheres are used, hemisphere should be modeled or counterbalanced, but the animal remains the primary unit unless a pre-registered split-animal design is justified.

---

### 2.2 Allocation

Use at least two main groups:

1. **Projection-inhibition group:** P-to-Q-targeted inhibitory opsin, fiber over Q.
2. **Light-control group:** same surgical and light procedure but without functional inhibitory opsin, for example fluorescent-protein-only or no opsin, depending on what is ethically and technically appropriate.

Allocation procedure:

1. Stratify animals by baseline task performance, sex if used, age or weight if relevant.
2. Randomize within strata to opsin or control group.
3. Counterbalance cue-response mappings, testing time of day, and order of light conditions where possible.

If using a within-subject light comparison, the light-on versus light-off contrast is within animal, but the causal interpretation still requires between-animal control for visible-light effects.

---

### 2.3 Blinding

The animal cannot be blinded because light may be visible (O4). Therefore, blinding must be applied to data collection and analysis.

**Required blinding procedures:**

1. Use automated trial control and automated behavioral scoring wherever possible.
2. Hide light-condition labels from the experimenter during handling and scoring if manual scoring is required.
3. Use coded group labels during analysis.
4. Pre-register analysis before unblinding group identities.
5. If manual intervention is required during sessions, use standardized scripts so the experimenter cannot influence trial timing based on expected condition.

---

## 3. Intervention and sampling

## 3.1 Primary intervention

The primary intervention is light delivery to Q during the cue-retrieval epoch in animals expressing the projection-targeted inhibitory opsin.

**Primary trial type:**

- **Retrieval-light trial:** light begins at cue onset and ends at response commitment, go signal, or the pre-registered end of the retrieval epoch.

This tests whether P-to-Q activity is needed during retrieval.

---

### 3.2 Control light epochs

Because retrieval and movement can overlap (O3), include several within-session light conditions.

1. **No-light trials**  
   Baseline cue-retrieval and choice performance without light.

2. **Retrieval-light trials**  
   Light during cue retrieval/decision epoch.

3. **Movement-light trials**  
   Light begins at response commitment or go signal and ends at choice-port entry.  
   Purpose: test whether the effect is due to movement execution rather than retrieval.

4. **Non-retrieval light trials**  
   Light during intertrial interval or after trial completion, not paired with cue retrieval.  
   Purpose: test general arousal, distraction, or aversive effects of visible light.

5. **Light-alone catch trials**  
   Light delivered without task cue or during a neutral period.  
   Purpose: test whether light itself evokes orienting, freezing, locomotion changes, or side bias.

6. **Optional delay-light trials**  
   If a delayed task is used, deliver light only during the delay after cue offset and before go signal. This provides a cleaner retrieval/maintenance epoch than cue-onset-only stimulation.

---

### 3.3 Trial sampling and randomization

Trial types should be randomized within session.

Recommended sampling logic:

1. No-light and retrieval-light trials should be numerous enough to support the primary comparison.
2. Movement-light and non-retrieval-light trials can be fewer but sufficient for epoch specificity.
3. Light-alone catch trials should be rare enough not to retrain the animal, but frequent enough to estimate light-evoked behavior.

Because optimal trial numbers are unknown, calibrate them.

**Calibration procedure for trial numbers:**

1. Run pilot sessions and estimate within-animal variability in correct choice and locomotion metrics.
2. Increase trials per condition until the standard error of the within-animal light effect reaches a pre-registered precision threshold.
3. If sessions become too long and fatigue or motivation changes occur, split testing across days rather than increasing trial density within a day.

Do not treat repeated trials as independent animals.

---

### 3.4 Light delivery calibration for unknown inhibition parameters

The exact light power, duration, frequency, and opsin efficacy are not specified. Calibrate rather than assume.

**Calibration procedure:**

1. Start with low light power and short epoch duration.
2. Test a small number of sessions across a range of powers/durations.
3. Look for a dissociation:
   - opsin animals show a retrieval-specific change,
   - control animals do not show the same change,
   - movement and sensory metrics remain stable.
4. Select the lowest intensity/duration that produces a reproducible dissociation.
5. If no dissociation appears at tolerable intensities, do not escalate indefinitely. Instead, verify expression, terminal localization, opsin function, and task sensitivity.

If electrophysiological or optical neural recordings are available, use them as an independent calibration check: light should reduce Q activity evoked by P activity or cue-related activity in opsin animals but not controls. This is optional but strengthens inference.

---

## 4. Measurements

### 4.1 Primary outcome

**Correct choice**  
Binary outcome: chosen port matches the cue-associated rule.

---

### 4.2 Movement-related measurements

Because locomotion is required (O3), collect the following on every trial:

1. Latency from cue onset to first movement.
2. Latency from cue onset to response commitment.
3. Latency from go signal or response commitment to port entry.
4. Mean and peak locomotion speed.
5. Path length and path efficiency.
6. Trajectory curvature or deviation toward one port.
7. Number and duration of movement pauses.
8. Omission rate, defined as failure to initiate or complete a response.
9. Reward port dwell time and reward consumption latency.

These measurements are necessary to distinguish retrieval failure from motor impairment, reduced motivation, or altered vigor.

---

### 4.3 Sensory and arousal measurements

Because light may be visible (O4), collect:

1. Orienting toward light source or fiber.
2. Freezing or abrupt locomotor arrest after light onset.
3. Changes in locomotion speed after light onset in light-alone trials.
4. Side bias relative to light delivery side.
5. Changes in cue-response latency when light is present versus absent.
6. If available, pupil response or video-based arousal indices.

These measurements do not eliminate the confound but allow it to be quantified.

---

### 4.4 Anatomical and expression measurements

After experiments:

1. Verify fiber placement over Q.
2. Verify opsin expression in P.
3. Verify projection-targeting strategy using retrograde or other appropriate labeling.
4. Assess spread into adjacent regions.
5. If possible, assess terminal expression in Q.
6. Record any tissue damage, inflammation, or infection.

Animals failing placement or expression criteria are excluded according to pre-registered rules.

---

## 5. Controls for movement and sensory confounds

## 5.1 Movement confound controls

### Delay or hold control

If possible, train animals to withhold locomotion after cue presentation. Then light can be delivered during cue retrieval before movement begins.

This is the strongest control because it separates retrieval from movement.

### Movement-epoch control

If delay training is not possible, compare retrieval-light trials with movement-light trials.

Interpretation:

- Retrieval-light impairs correct choice but movement-light does not: supports retrieval-specific necessity.
- Both retrieval-light and movement-light impair choice or locomotion: motor or performance confound likely.
- Retrieval-light effect disappears after accounting for speed or initiation latency: likely movement-related.

### Separate locomotion assay

Test animals in a simple movement task not requiring cue-guided choice:

1. Linear track or open field.
2. Reward approach from start zone to known reward location.
3. Light delivered during movement.

Measure speed, initiation, turning, pausing, and reward approach.

Interpretation:

- Light in opsin animals impairs basic locomotion: not a clean retrieval effect.
- Light does not impair basic locomotion: strengthens retrieval interpretation.

---

## 5.2 Sensory/light confound controls

### Control-animal light exposure

Control animals without functional inhibitory opsin receive the same light schedule.

Interpretation:

- Control animals show reduced correct choice or altered movement during retrieval-light: light has non-specific sensory or behavioral effects.
- Opsin animals show a larger retrieval-specific deficit than controls: supports inhibition-specific effect.

### Light-alone catch trials

Deliver light without task cues.

If light alone causes orienting, freezing, avoidance, or locomotion changes, then light is behaviorally salient. This does not automatically invalidate the experiment, but it requires stronger controls and cautious interpretation.

### Non-retrieval light trials

Deliver light during intertrial intervals.

If non-retrieval light produces the same deficit as retrieval light, the effect is not retrieval-specific.

### Intensity calibration

Use the lowest effective light intensity. If high-intensity light produces effects in control animals, reduce intensity or change wavelength if compatible with the opsin.

### Blinded scoring

Because the animal cannot be blinded to visible light, the scoring pipeline must be blinded and automated.

---

## 6. Analysis

Pre-register the analysis before unblinding group assignments.

### 6.1 Primary model

Use a mixed-effects model because trials are nested within animals and sessions.

Primary outcome: correct/incorrect.

A suitable model structure is:

- correct choice ~ light condition × group + movement covariates + session-level covariates + random effects for animal and session.

The primary contrast is:

**Retrieval-light effect in opsin animals minus retrieval-light effect in control animals.**

This difference controls for general effects of visible light, handling, surgery, and trial structure.

---

### 6.2 Movement-adjusted analysis

Run two complementary analyses.

1. **Total behavioral effect:**  
   correct choice ~ light × group, without movement covariates.  
   This estimates the overall effect of inhibition on task success.

2. **Movement-adjusted effect:**  
   correct choice ~ light × group + speed/latency/path metrics.  
   This helps determine whether the effect is explained by locomotion changes.

Be careful: movement may be downstream of the manipulation. If movement impairment is caused by inhibition, controlling for it may remove part of the true behavioral effect. Therefore, movement-adjusted models are interpretive aids, not the sole basis for inference.

The cleanest evidence for retrieval specificity comes from **epoch controls**, not statistical adjustment alone.

---

### 6.3 Epoch specificity

Compare the light effect across epochs:

1. Retrieval-light.
2. Movement-light.
3. Non-retrieval-light.
4. Light-alone trials.

A retrieval-specific necessity claim requires:

- retrieval-light reduces correct choices in opsin animals,
- movement-light does not produce the same pattern unless movement is genuinely impaired,
- non-retrieval-light does not reproduce the effect,
- control animals do not show the same retrieval-specific deficit.

---

### 6.4 Locomotion and sensory diagnostics

Analyze:

1. Speed and initiation latency by light condition and group.
2. Omission rate.
3. Side bias.
4. Light-alone response probability.
5. Cue-response latency.

If opsin animals show slower movement, increased omissions, or failure to initiate, the correct-choice deficit may be motoric.

If light-alone trials produce orienting or avoidance, the visible-light confound is present. The inference then depends on whether the opsin-specific retrieval effect remains after control subtraction and whether the effect is absent in non-retrieval epochs.

---

### 6.5 Inclusion/exclusion criteria for analysis

Predefine criteria such as:

1. Minimum valid trials per condition, determined by pilot precision calibration.
2. Stable baseline performance before light sessions.
3. Fiber placement within Q.
4. Acceptable projection-targeted expression.
5. Absence of severe health or welfare issues.
6. Absence of hardware failure during trial delivery.

Do not exclude animals after seeing the outcome unless they violate pre-registered quality criteria.

---

## 7. Acceptance and stopping criteria

### 7.1 Acceptance criteria for a valid necessity inference

The experiment supports the conclusion that P-to-Q is necessary during cue retrieval if all of the following hold:

1. Retrieval-light trials reduce correct choices in the projection-inhibition group relative to no-light trials.
2. This reduction is larger than any reduction seen in control animals receiving the same light.
3. The effect is stronger during retrieval than during movement or non-retrieval light epochs.
4. Locomotion metrics do not show a general impairment that fully accounts for the choice deficit.
5. Light-alone and non-retrieval-light controls do not reproduce the same effect.
6. Histology confirms appropriate expression and fiber placement.

If some but not all criteria hold, the result is suggestive but not conclusive.

---

### 7.2 Inconclusive outcomes

The result is inconclusive if:

1. Control animals also show retrieval-light deficits.
2. Opsin animals show general locomotor impairment.
3. Light-alone trials produce strong orienting, freezing, or avoidance.
4. Expression is weak, off-target, or not terminal-localized.
5. Retrieval and movement epochs cannot be separated.
6. The number of valid trials is too low to estimate effects precisely.

In these cases, do not claim retrieval-specific necessity.

---

### 7.3 Stopping criteria

Stop or pause the experiment if:

1. Animals show distress, weight loss, infection, or other welfare concerns.
2. Light delivery causes persistent freezing or avoidance in control animals.
3. Fibers repeatedly fail or light output drifts outside calibrated range.
4. Baseline task performance collapses across sessions.
5. Interim analysis shows strong non-specific light effects that cannot be controlled.
6. Interim analysis shows futility under pre-registered sequential rules.

If the problem is sensory, revise light parameters or controls. If the problem is motor, redesign epochs or reduce light intensity/duration.

---

## 8. Troubleshooting

### Problem 1: No effect of retrieval-light in opsin animals

Possible causes and responses:

1. Insufficient opsin expression in P-to-Q terminals.  
   Verify expression histologically; adjust targeting strategy or expression time in a new calibration cohort.

2. Light intensity too low.  
   Increase intensity only within pre-registered safety limits and only after control animals show no non-specific effects.

3. Retrieval epoch incorrectly defined.  
   Re-calibrate epoch boundaries using behavior and, if available, neural activity.

4. Task insensitive.  
   Use a more difficult cue discrimination, a delay period, or a trial structure that places greater demand on retrieval.

5. Inhibitory opsin not effective at terminals.  
   Use a different terminal-compatible inhibitory opsin if available and validated.

---

### Problem 2: Retrieval-light reduces correct choices but also slows movement

Possible interpretations:

1. Inhibition impairs movement initiation or vigor.
2. Retrieval failure delays movement secondarily.
3. Light affects arousal or motivation.

Responses:

1. Add or strengthen delayed-hold trials.
2. Compare retrieval-light with movement-light.
3. Run separate locomotion assays.
4. Reduce light duration so it ends before movement initiation if ethically and technically feasible.
5. Analyze trials where movement initiation occurs within the normal baseline range. If the choice deficit persists, retrieval impairment is more plausible.

---

### Problem 3: Control animals also show light effects

This indicates visible-light or procedural confounds (O4).

Responses:

1. Lower light intensity.
2. Change wavelength if compatible with opsin.
3. Add more light-alone and non-retrieval controls.
4. Increase habituation to light delivery.
5. Use background illumination or masking if it does not alter cue perception.
6. If effects persist, the experiment cannot cleanly isolate optogenetic inhibition.

---

### Problem 4: Expression spreads outside P-to-Q pathway

Responses:

1. Reduce injection volume or titer in calibration cohorts.
2. Refine targeting coordinates.
3. Use more selective projection-targeting approaches if available.
4. Exclude animals with clear off-target expression from inference.

---

### Problem 5: P-to-Q neurons may collateralize to another region

This is a key limit given O1.

Terminal inhibition in Q is still the best primary test of whether the P-to-Q output in Q is necessary. However, if P-to-Q neurons also project elsewhere, the manipulation does not rule out all functions of those neurons. It tests the necessity of their output in Q during the illuminated epoch.

If collateralization is a major concern, optional additional controls include:

1. Targeting the same projection strategy to the other projection, if feasible, and testing whether light there affects retrieval.
2. Comparing terminal inhibition in Q with terminal inhibition in the other target region.
3. Using anatomical tracing to estimate collateralization.

These are proposed controls, not established from the supplied evidence.

---

# Alternatives and limitations

## Alternative designs

### 1. Projection-targeted somatic inhibition in P

Instead of illuminating Q terminals, express inhibitory opsin in P neurons projecting to Q and illuminate P.

Advantage: may be easier if terminal inhibition is weak.  
Limitation: if P-to-Q neurons also project to another region, inhibiting their somata may affect multiple outputs. This weakens projection specificity.

### 2. Inhibit Q cell bodies

Inhibiting Q itself during retrieval would test whether Q is necessary, but not whether the P-to-Q projection specifically is necessary. It is a useful complementary control but not a projection-specific test.

### 3. Temporal mapping

Use brief light pulses at different latencies after cue onset to identify the sensitive window. This can help distinguish early cue processing from later retrieval or decision processes.

### 4. Behavioral pharmacology or lesion controls

If permitted and available, non-optogenetic inactivation can complement optogenetics, but it usually lacks the temporal precision needed to isolate cue retrieval.

---

## Major limitations

1. **Visible light confound.**  
   Because light delivery can be visible (O4), the animal cannot be blinded. Control subtraction can estimate but not eliminate all sensory effects.

2. **Movement overlap.**  
   If retrieval and locomotion cannot be separated temporally, a retrieval-specific necessity claim is weakened (O3). Delayed-response design is strongly preferred.

3. **Projection ambiguity.**  
   Because P projects to more than one region (O1), somatic manipulation would be ambiguous. Terminal illumination in Q is better but still requires validation.

4. **Incomplete inhibition.**  
   Failure to observe an effect may reflect inadequate inhibition rather than true non-necessity.

5. **Off-target light or expression.**  
   Light spread and expression outside the intended pathway can produce false positives or false negatives.

6. **Acute compensation or behavioral strategy change.**  
   Animals may adapt to light or inhibition across trials. Randomized within-session controls help but do not fully eliminate this issue.

7. **Unknown biological parameters.**  
   Expression level, opsin kinetics, terminal density, light spread, and behavioral sensitivity are not specified. All must be calibrated before definitive testing.

---

## Final decision rule

Accept the hypothesis that P-to-Q is necessary during cue retrieval only if:

1. Projection-targeted inhibition in Q during cue retrieval reduces correct choices.
2. The effect is greater than any effect of the same visible light in control animals.
3. The effect is absent or substantially smaller when light is delivered outside retrieval or during movement execution alone.
4. Locomotion, motivation, and cue detection controls do not explain the deficit.
5. Anatomical and optical quality checks pass.

If the effect is present but accompanied by general movement impairment, visible-light aversion, control-animal effects, or poor expression specificity, the result should be interpreted as inconclusive and the protocol should be revised before any necessity claim is made.
