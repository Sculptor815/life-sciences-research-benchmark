# GPT-5.6 Sol / neu-r03

Original final answer, shared by both scoring rounds.

# Recommended next biological question

**Do identified dopamine neurons carry a sustained signal during the cue-to-outcome waiting period that represents reward-probability uncertainty, independently of expected reward value, outcome timing, and behavioral state?**

This is the highest-value next question because the packet establishes dopamine responses to prediction violations at reward or omission, but explicitly leaves waiting-period information unresolved. The appropriate next step is therefore a controlled probability manipulation with fixed outcome timing, direct dopamine-neuron recording, and separable tests of uncertainty, expected value, and temporal expectation.

**Important status:** Everything below is a proposed experiment and proposed interpretation. The packet contains no probability-manipulation experiment or result.

---

# 1. Evidence-to-inference-to-conclusion chain

## Packet evidence

- **E1:** During learning, dopamine-neuron responses to rewards diminish as rewards become predicted.
- **E2:** Reward at an unexpected time produces activation.
- **E3:** Reward omission at the expected time produces a depression.
- **E4:** These findings link dopamine activity to reward-prediction violations but do not establish whether waiting-period activity carries information about variable outcomes.
- **E5:** No later probability-manipulation experiment or result is supplied.

## Inference

E1–E3 show that dopamine activity is sensitive to learned reward expectations and their violation. They therefore provide:

1. A rationale for manipulating reward probability.
2. Positive-control signatures showing that the animal learned the contingencies.
3. A way to separate event-related prediction errors from activity arising before an outcome is delivered or omitted.

However, event-time responses do not imply a sustained uncertainty signal. Waiting-period activity could instead be absent, encode expected value, reflect uncertainty about timing, or arise from movement, arousal, or cue identity.

## Conclusion

A probability task with a fixed cue-to-outcome interval is needed. The critical measurement is activity after the cue response has ended but before the expected outcome time. A genuine probability-uncertainty signal should be maximal at intermediate reward probabilities and should survive controls for expected value, timing, cue identity, and behavior.

---

# 2. Operational definition of the unresolved question

A waiting-period signal will count as carrying **additional information about reward uncertainty** if:

1. It occurs after the transient cue response and before the outcome or omission.
2. It changes systematically with learned reward probability.
3. Its probability dependence cannot be explained adequately by expected reward value alone.
4. It remains under fixed outcome timing.
5. It replicates across animals and counterbalanced cue identities.
6. It is not attributable solely to measured movement, reward-seeking behavior, recording drift, or local reward history.

“Information” here means a reproducible condition-related neural signal. It does not by itself imply that the animal consciously experiences uncertainty or that dopamine activity causally controls behavior.

---

# 3. Competing mechanisms and discriminating predictions

| Mechanism | Waiting-period prediction | Cue and outcome predictions | Key discriminator |
|---|---|---|---|
| **M1. Event-locked prediction-error mechanism only** | After the cue transient, activity returns to baseline and does not systematically encode probability. | Cue response may reflect learned prediction; delivered reward response is larger when reward was less probable; omission depression is larger when reward was more probable. | Intact cue/outcome signatures but no probability-dependent middle-delay signal. |
| **M2. Probability-uncertainty signal** | Activity is lowest for certain outcomes, rises for intermediate probabilities, and is maximal near probability 0.5. | Outcome responses can still follow prediction violation. | Inverted-U probability dependence under fixed timing, beyond expected value and behavior. |
| **M3. Expected-value or reward-anticipation signal** | Activity changes monotonically with probability when reward magnitude is fixed, or with probability × reward magnitude when magnitude varies. | Larger predictions produce larger anticipatory signals; surprise still affects outcomes. | Monotonic rather than inverted-U dependence; approximately equal activity for value-matched conditions. |
| **M4. Outcome-variance signal** | Signal follows approximately \(p(1-p)m^2\), where \(p\) is reward probability and \(m\) is reward magnitude. | Stronger for larger possible rewards even at the same probability. | Probability effect scales strongly with reward magnitude. |
| **M5. Probability-entropy-like signal** | Peaks near \(p=0.5\) and is principally determined by probability, not reward magnitude. | Amount can affect event responses without proportionally changing the waiting signal. | Similar uncertainty-shaped signal across calibrated reward magnitudes. |
| **M6. Temporal-hazard or timing-prediction signal** | Activity tracks possible outcome times or the changing likelihood of an outcome as time passes. It may occur even when reward is certain but its timing is uncertain. | Unexpected timing produces activation, consistent with E2. | Signal shifts when the timing distribution shifts and appears with timing uncertainty at probability 1. |
| **M7. Cue salience, movement, arousal, or motivational confound** | Activity follows a particular cue, anticipatory movement, or engagement rather than probability itself. | May superficially resemble uncertainty. | Fails cue remapping, counterbalancing, behavioral matching, or covariate controls. |

These mechanisms are not mutually exclusive. For example, different dopamine neurons could carry event-related, value-related, and uncertainty-related components.

---

# 4. Proposed research plan

## 4.1 Unreported parameters and assumptions

The packet does not specify:

- Species or target population.
- Brain region or dopamine-neuron subtype.
- Reward type or magnitude.
- Cue modality.
- Cue-to-outcome delay.
- Recording method or cell-identification method.
- Behavioral readout.
- Sample size, variability, or attrition.
- Whether individual neurons can be followed across conditions.

These must not be inferred from the packet. Before confirmatory work, select an experimentally tractable preparation in which dopamine neurons can be identified independently of their reward responses.

**Proposed implementation:** record single-neuron activity with a method that provides precise cue and outcome timing. Dopamine-neuron identity should use a preregistered anatomical, genetic, molecular, or other independently validated criterion. Reward responsiveness must not be used as the identity criterion because that would make the test circular.

---

## 4.2 Stage 1 — Preregistration and analysis preparation

Before collecting confirmatory data:

1. Register the primary question, primary waiting window, hypotheses, exclusion rules, statistical model, multiplicity control, and interpretation criteria.
2. Define the target biological population and the animal as the primary independent biological unit.
3. Write and test acquisition and analysis code on simulated or calibration data.
4. Freeze code for:
   - Event alignment.
   - Spike or activity quantification.
   - Baseline subtraction.
   - Trial-history variables.
   - Behavioral covariates.
   - Hierarchical statistical analysis.
5. Keep pilot data separate from confirmatory data unless a rule for combining them was registered before viewing condition effects.
6. Do not stop confirmatory acquisition early merely because a significance threshold is crossed.

---

## 4.3 Stage 2 — Technical and biological calibration

### A. Event-timing calibration

1. Measure actual cue onset, reward delivery, and any delivery-device signal using hardware timestamps.
2. Quantify latency and jitter.
3. Set an acceptable timing tolerance before confirmatory collection.
4. Use the actual measured delivery time, rather than only the command time, for neural alignment.
5. Include sham activation of the delivery apparatus on omission trials if the apparatus itself creates sound, vibration, or another sensory event.

### B. Recording calibration

1. Establish preregistered minimum criteria for unit isolation, recording stability, missing data, and artifacts.
2. Determine whether the delay is long enough to separate:
   - Baseline.
   - Cue-evoked response.
   - Middle waiting period.
   - Pre-outcome period.
   - Outcome or omission response.
3. Select the delay during pilot work only. It should be long enough to isolate waiting activity but short enough for animals to learn and remain engaged.
4. Do not change analysis windows after inspecting probability effects.

### C. Reward calibration

1. Select a reward magnitude that is detectable and motivating but not saturating.
2. Confirm that behavior remains stable across a session and is not dominated by rapid satiety.
3. If two reward magnitudes will be used in the secondary variance-versus-entropy test, confirm behaviorally that they are discriminable.
4. Treat equal expected physical amounts as only an approximate value match; subjective value may be nonlinear.

### D. Cue calibration

1. Use cues with comparable duration and physical intensity.
2. Verify that animals can discriminate the cues.
3. Assign cue identity to probability condition differently across animals so that no sensory cue is permanently associated with a particular probability across the study.

### E. Positive-control calibration

Before the probability test, verify at the preparation level that the task can produce the packet’s relevant signatures:

- Smaller reward response when reward is well predicted than when it is unexpected.
- Activation to an unexpectedly timed reward.
- Depression at an expected time when a learned reward is omitted.

These controls validate the preparation. Individual neurons must not be included or excluded according to whether they show the expected effect.

---

## 4.4 Stage 3 — Primary task design

### Primary fixed-magnitude probability task

Use five cues predicting the same reward magnitude at probabilities:

- \(p=0\)
- \(p=0.25\)
- \(p=0.50\)
- \(p=0.75\)
- \(p=1.00\)

For every condition:

1. Cue duration is matched.
2. The nominal cue-to-outcome interval is identical.
3. Reward, when delivered, occurs at the same fixed time.
4. Trials are interleaved so that satiety, recording drift, or time in session is not confounded with probability.
5. Intertrial intervals may be jittered, but their distribution must be identical across probability conditions.
6. Reward sequences are generated before the session using a documented randomization algorithm.
7. Sequence generation should avoid accidental condition-specific temporal structure. Recent reward history will also be included in analysis.

The \(p=0.25, 0.50,\) and \(0.75\) conditions are particularly useful because all retain a possibility of reward. The \(p=0\) and \(p=1\) conditions anchor certainty.

### Learning criterion

Before confirmatory recording, require a preregistered behavioral indication that the cues have acquired different predictions. The exact behavior depends on the preparation and is unreported in the packet. A suitable measure could be anticipatory reward-seeking behavior.

The criterion must:

1. Be defined without reference to waiting-period neural activity.
2. Be assessed on independent or preceding trials.
3. Have a maximum permitted training duration.
4. Be reported for all animals, including those failing to learn.

Failure to meet this criterion is a learning failure, not evidence against neural uncertainty coding.

---

## 4.5 Stage 4 — Secondary discriminating task modules

These modules should be separately powered or explicitly labeled exploratory.

### Module A: Expected-value challenge

Compare conditions with approximately matched expected physical reward but different probabilities, for example:

- Certain smaller reward.
- A larger reward delivered with probability 0.5.

Prediction:

- An uncertainty mechanism gives greater waiting activity for the probabilistic condition.
- A pure expected-value mechanism gives similar activity if the values are genuinely matched.

**Limitation:** matching expected physical amount does not guarantee matching subjective value. Behavioral preference or indifference data should therefore accompany this comparison.

### Module B: Probability entropy versus outcome variance

Cross several reward probabilities with at least two calibrated reward magnitudes.

Predictions:

- A probability-entropy-like signal depends mainly on probability and remains similarly shaped across magnitudes.
- A variance-like signal grows with reward magnitude.
- An expected-value signal follows probability × magnitude.

This module is necessary before claiming that a signal represents “uncertainty” in a specific computational sense.

### Module C: Temporal uncertainty

In separate blocks, compare:

1. Fixed reward timing.
2. Distributed or jittered reward timing.

Include a condition in which reward is eventually certain but its time is uncertain.

Predictions:

- A temporal-hazard mechanism produces activity aligned to possible reward times and can appear despite certain eventual reward.
- A probability-uncertainty effect should remain present in the fixed-timing probability task and should not be fully reproduced by timing uncertainty alone.

Do not mix this module into the primary fixed-timing analysis.

---

## 4.6 Independent units, sample size, and allocation

### Independent units

- **Primary biological unit:** animal.
- **Nested observations:** neurons within animal, sessions within animal, and trials within neuron/session.
- Neurons and trials increase measurement precision but must not be counted as independent biological replicates.

### Sample-size determination

Because the packet supplies no variance or effect size:

1. Use calibration or pilot data to estimate animal-to-animal variance, usable neuron yield, within-neuron variability, and attrition.
2. Define a minimum biologically meaningful waiting-period effect before confirmatory collection.
3. Determine the number of animals by simulation of the planned hierarchical model, targeting prespecified power, such as 90%, at the chosen familywise error rate.
4. Inflate for preregistered technical attrition.
5. Fix the confirmatory sample size before unblinding probability effects.
6. If variance is re-estimated during collection, do so while condition labels remain blinded and use a registered blinded sample-size adjustment rule.

### Allocation

Because the primary manipulation is within animal:

1. Randomize animals to cue-to-probability mappings.
2. Balance mapping assignments so each sensory cue represents each probability across animals.
3. Randomize or counterbalance the order of timing and magnitude modules.
4. Interleave primary probability conditions within sessions.
5. Use automated reward scheduling so operator decisions cannot change trial allocation.

---

## 4.7 Blinding

Full operator blinding may be impossible because rewards are observable, but several components can remain blinded:

1. Label cues and conditions with arbitrary codes during spike sorting, artifact rejection, and primary analysis.
2. Blind histological or molecular identity assessment to neural effects.
3. Freeze technical exclusion decisions before decoding probability labels.
4. Automate trial generation and reward delivery.
5. Unblind only after the registered dataset, exclusions, and primary analysis are locked.

---

## 4.8 Measurements

### Primary neural measurement

For every accepted neuron and trial, quantify baseline-adjusted activity in preregistered epochs:

1. **Baseline:** immediately before cue onset.
2. **Cue epoch:** captures the cue-evoked transient.
3. **Early delay:** after cue onset.
4. **Middle delay:** the primary waiting-period window, separated from cue and outcome by guard intervals.
5. **Late delay:** tests whether activity emerges only near the outcome.
6. **Outcome epoch:** centered on actual reward delivery or the expected time of omission.

The exact durations must be chosen during calibration and then frozen.

### Behavioral and nuisance measurements

Record, where feasible:

- Anticipatory reward-seeking behavior.
- Gross movement and posture.
- Task engagement.
- Trial number and time in session.
- Recent reward and omission history.
- Actual reward-delivery timing.
- Any apparatus-generated sensory event.

Behavior is both evidence that probabilities were learned and a potential mediator or confound. Analyses with and without behavioral covariates should both be reported; covariate adjustment alone cannot prove that movement is irrelevant.

---

## 4.9 Primary statistical analysis

Use a hierarchical model appropriate for the recorded activity distribution, with:

- Animal-level random effects.
- Neurons nested within animal.
- Session effects where needed.
- Repeated trials nested within neuron/session.
- Baseline activity and recording drift.
- Recent outcome history.
- Prespecified behavioral covariates.

For the fixed-magnitude task, model separate terms for:

1. A monotonic probability or expected-value component.
2. An uncertainty-shaped component, such as \(4p(1-p)\), which equals zero at certainty and peaks at \(p=0.5\).

The **primary test** is whether the uncertainty-shaped coefficient in the middle-delay window differs from zero in the predicted positive direction after accounting for the monotonic component.

Planned supporting contrasts should include:

- Activity at \(p=0.5\) versus the average at \(p=0.25\) and \(p=0.75\).
- Intermediate-probability conditions versus certainty conditions.
- Equal-expected-amount probabilistic versus certain conditions.
- Fixed versus temporally jittered conditions.

The local contrast around \(p=0.5\) is useful because the average probability of the \(0.25\) and \(0.75\) conditions is also \(0.5\), reducing sensitivity to a simple linear expected-value effect.

### Time-resolved analysis

A time-resolved analysis can determine whether the effect is sustained, ramps, or appears only near outcome time. It should be secondary unless fully preregistered. Correct for multiple temporal comparisons.

### Outcome-response validation

Separately test whether:

- Delivered reward responses become larger as reward probability decreases.
- Omission-related depression becomes stronger as reward probability increases.

These are manipulation checks for learned prediction. They should not be used to select individual neurons.

### Heterogeneity

Estimate neuron-specific probability and uncertainty slopes in the hierarchical model. Report heterogeneity, but do not create post hoc “uncertainty neuron” classes without independent replication.

---

# 5. Controls

Essential controls are:

1. **Cue-identity control:** counterbalance and, if feasible, remap cue identities.
2. **Fixed-timing control:** all primary rewards occur at the same delay.
3. **Certainty anchors:** include both certain reward and certain no-reward cues.
4. **Outcome-surprise checks:** confirm probability-dependent reward and omission responses.
5. **Unexpected-timing control:** confirm sensitivity to timing violations in a separate probe.
6. **Apparatus control:** equalize delivery-device sensory events where possible.
7. **Behavioral control:** monitor movement and anticipatory behavior.
8. **History control:** model recent rewards, omissions, and random streaks.
9. **Session-time control:** interleave conditions to avoid satiety and drift confounds.
10. **Identity control:** identify dopamine neurons independently of response profile.
11. **Technical replication:** require effects across animals, not merely many trials from one animal.
12. **Timing-uncertainty control:** test certain reward with uncertain timing separately.

---

# 6. Stop rules and exclusions

## Animal and session stop rules

Stop a session for:

- Prespecified welfare criteria.
- Loss of task engagement according to a behavioral criterion independent of neural condition effects.
- Reward-delivery failure or timing jitter beyond the calibrated tolerance.
- Recording instability or artifact beyond the preregistered QC threshold.

## Training stop rule

Set a maximum training duration. Animals failing the behavioral learning criterion by that point are classified as nonlearners. Their number and data disposition must be reported. They should not be silently replaced.

## Data exclusions

Allow exclusions only for rules defined before unblinding, such as:

- Failure of independent dopamine-neuron identification.
- Technical recording failure.
- Event-timing failure.
- Prespecified unit-isolation failure.
- Missing behavioral or event records needed for alignment.

Do not exclude neurons because they lack the predicted reward response or uncertainty effect.

## Study-level stopping

- Stop after the fixed number of usable animals determined by the power analysis.
- Do not stop early for statistical significance unless a formal sequential design with alpha spending was registered.
- Technical replacements should follow fixed rules.
- If pilot-based parameters are changed, begin a newly registered confirmatory cohort rather than silently modifying the ongoing study.

---

# 7. Troubleshooting

| Problem | Interpretation | Corrective action |
|---|---|---|
| Cues do not produce behavioral discrimination | Probabilities may not have been learned. | Improve cue discriminability, adjust delay or training duration during a new pilot, and restart confirmation with frozen parameters. |
| Outcome responses do not scale with surprise | Manipulation or learning may be inadequate, or the sampled population may not show the packet’s signatures. | Check timing, reward delivery, learning, and identification. Treat waiting-period results as ambiguous rather than negative. |
| Apparent effect follows one cue identity | Sensory confound. | Use counterbalanced mappings and a remapped replication. |
| Effect appears only immediately after cue | Could be cue-value or salience response, not waiting activity. | Preserve guard interval; analyze middle delay separately. |
| Effect occurs only immediately before outcome | Could be temporal anticipation or hazard. | Run timing-jitter module and test whether the signal shifts with possible outcome times. |
| Movement parallels neural activity | Motor or engagement explanation remains viable. | Improve movement measurement, compare movement-matched trials, and replicate under conditions reducing movement differences. |
| Random reward streaks alter behavior | Animals may track local probability rather than nominal probability. | Model recent history, use long training, and verify that results are not driven by rare runs. |
| Signal drifts across the session | Recording instability, satiety, or changing belief. | Interleave conditions, include drift terms, shorten sessions prospectively, and apply registered QC. |
| Population mean is null but neurons are heterogeneous | Opposing subpopulations may cancel. | Report hierarchical slope distribution; test subtypes only with independent identity markers or a new replication. |
| Too few usable neurons | Insufficient precision, not biological absence. | Improve technical yield without relaxing identity or QC criteria; revise sample size in a new registered cohort. |

---

# 8. Interpretation of possible outcomes

## A. Positive uncertainty result

Criteria:

- Animals behaviorally learn the probabilities.
- Reward and omission responses show the expected surprise dependence.
- Middle-delay activity has a reproducible inverted-U probability relationship.
- The effect survives monotonic expected-value, local-history, cue, and behavioral controls.
- It replicates across animals and cue mappings.
- It remains under fixed timing and is stronger in probabilistic than approximately value-matched certain conditions.

**Strongest justified conclusion:** In the sampled identified dopamine neurons and task, waiting-period activity carries a signal associated with learned reward-probability uncertainty in addition to event-time prediction-violation responses.

This would not establish that the signal is causal, consciously experienced, universal across dopamine neurons, or exactly equivalent to entropy rather than another nonlinear variable.

## B. Monotonic waiting-period result

If activity increases or decreases monotonically with probability or expected reward amount, with no independent inverted-U component:

**Conclusion:** The results support expected-value or reward-anticipation coding more strongly than probability-uncertainty coding.

A nonlinear subjective-value function would remain a possible complication.

## C. Reward-magnitude-dependent inverted-U result

If the uncertainty-shaped signal grows strongly with possible reward magnitude:

**Conclusion:** Outcome variance or risk magnitude is more plausible than a magnitude-independent probability-entropy signal.

## D. Timing-dependent result

If activity shifts with possible reward times and appears when reward is certain but timing is uncertain:

**Conclusion:** Temporal hazard or timing prediction is the better explanation. The data would not support a probability-specific uncertainty signal.

## E. Negative waiting-period result with valid controls

If learning is demonstrated, event-time prediction-error signatures are intact, timing and recording are adequate, and confidence intervals exclude the preregistered minimum meaningful effect:

**Conclusion:** There is no detectable population-level waiting-period uncertainty signal of that size in the sampled neurons and task. This supports an event-locked or value-only account within the tested conditions.

It would not prove that no dopamine neuron ever carries uncertainty information, especially if rare or opposing subpopulations exist.

## F. Ambiguous result

The result is ambiguous if:

- Behavioral learning is absent.
- Outcome-surprise signatures are absent.
- Recording precision is insufficient.
- The effect is confined to cue or outcome boundaries.
- Cue identity and probability are not adequately counterbalanced.
- Movement or arousal fully tracks the neural effect.
- Expected value and uncertainty were not separable.
- Only nominal, not subjective, values were matched.
- Opposing neuron-level effects produce a population null without enough data to resolve heterogeneity.

In these cases, the strongest conclusion is that the experiment did not discriminate the mechanisms.

---

# 9. Overall limit

The supplied evidence supports only the existence of dopamine responses to prediction violations and identifies the waiting period as unresolved. It does not report probability coding, sustained activity, specific cell types, or any later experiment. The proposed study can establish an association between waiting-period dopamine activity and uncertainty under controlled conditions. A later causal intervention would be required to determine whether that activity is necessary or sufficient for uncertainty-dependent learning or behavior.
