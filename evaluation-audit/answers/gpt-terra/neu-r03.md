# GPT-5.6 Terra / neu-r03

Original final answer, shared by both scoring rounds.

# Recommended next biological question

**Does dopamine-neuron activity during the interval between a predictive cue and a fixed possible reward time encode uncertainty about whether reward will occur, independently of expected reward value and temporal expectation?**

This is the most valuable next question because the supplied evidence establishes outcome-time prediction-error-like responses, but explicitly leaves unresolved whether dopamine neurons carry additional information **while the animal waits** for a variable outcome.

---

# 1. Evidence → inference → conclusion

## Supplied evidence

**E1.** “During learning, dopamine-neuron responses to rewards diminish as rewards become predicted.”

**E2.** “Unexpected timing produces activation, while omission at an expected time produces a depression.”

**E3.** These observations “connect neural activity with violations of reward prediction.”

**E4.** The packet states that these observations “do not establish whether activity during the waiting period carries additional information about variable outcomes.”

**E5.** “No later probability-manipulation experiment or result is included.”

## Inference

E1–E3 support the proposition that dopamine-neuron activity at, or near, an outcome can reflect whether the outcome is better, worse, or differently timed than predicted. They do **not** determine whether activity between cue and outcome time is merely baseline/temporal anticipation, or whether it represents a property of the pending outcome such as its probability, expected value, or uncertainty.

Because E4–E5 identify the missing manipulation, a controlled probability experiment is required.

## Conclusion

The appropriate next experiment is a **probability-by-value-by-time design** in which the time of possible reward is held fixed while reward probability is varied, expected value is independently controlled, and dopamine-neuron activity is measured specifically in the cue-to-outcome waiting interval.

---

# 2. Unresolved biological question and definitions

## Primary unresolved question

When a cue predicts that reward may occur at a known future time, does dopamine-neuron activity during the waiting period encode:

1. **uncertainty** about whether reward will occur,
2. **expected reward value/probability**,
3. **temporal anticipation or hazard** of the expected event,
4. or no additional variable-outcome information beyond cue and outcome responses?

## Operational definitions for the proposed study

These are proposed definitions, not reported findings.

- **Waiting period:** the interval after the cue-related transient has ended and before the possible reward time. In a proposed 4-s delay task, the primary window would be 0.75–3.75 s after cue onset.
- **Reward probability, \(p\):** programmed probability that reward is delivered at the fixed outcome time.
- **Expected value (EV):** probability multiplied by the behaviorally calibrated value of reward magnitude.
- **Uncertainty:** maximal at intermediate probabilities and low at probabilities near 0 or 1. A simple preregistered uncertainty regressor is \(U = 4p(1-p)\), which is 0 at \(p=0\) or 1 and 1 at \(p=0.5\).
- **Temporal expectation/hazard:** expectation related to when an event may occur, rather than whether it will occur.

The experiment should not assume that objective reward volume equals subjective reward value. That relation is an unreported parameter and must be measured or treated as an explicit assumption.

---

# 3. Competing mechanisms and discriminating predictions

## Mechanism 1: Outcome-only prediction-error signaling

### Account
Dopamine neurons respond mainly when reward arrives unexpectedly, arrives at an unexpected time, or is omitted at an expected time. There is no meaningful variable-outcome signal during the delay.

### Predictions
- After excluding the immediate cue response and outcome response, average waiting-period activity does not differ reliably among reward probabilities.
- Reward-delivery responses are larger when reward is less predicted.
- Omission-related depressions are larger when reward was more expected.
- Any apparent delay-period difference disappears after accounting for cue transients, movement, recording drift, or time within trial.

### Discriminating result
A well-powered null result with narrow confidence intervals around a preregistered smallest biologically relevant effect would favor this mechanism for the tested task.

---

## Mechanism 2: Uncertainty coding during the waiting period

### Account
Dopamine-neuron activity during the delay represents uncertainty about whether reward will occur.

### Predictions
- Delay-period activity follows an inverted-U relation with probability: greatest near \(p=0.5\), lower near \(p=0.25\) and \(0.75\), and lowest near certainty.
- Conditions with similar uncertainty but different expected values—for example \(p=0.25\) versus \(p=0.75\) at the same reward magnitude—produce similar uncertainty-related delay activity.
- The intermediate-probability effect remains when expected value is behaviorally matched across conditions.
- The effect follows a reversal of cue–probability contingencies: it changes with the learned probability, not with the sensory identity of a cue.
- The effect remains after controlling for time in trial, anticipatory behavior, locomotion, and other measured state variables.

### Discriminating result
A reproducible, contingency-dependent inverted-U delay signal that survives expected-value and timing controls would support uncertainty-related information in dopamine-neuron activity.

---

## Mechanism 3: Expected-value or reward-probability coding

### Account
Delay activity represents how much reward is expected, rather than uncertainty.

### Predictions
- Delay-period activity changes monotonically with expected value or reward probability.
- With constant reward magnitude, activity is greatest for high-probability cues and least for low-probability cues.
- The relation is reduced or eliminated when expected value is behaviorally matched across probability conditions.
- \(p=0.75\) and \(p=0.25\), which have equal simple uncertainty but different expected values, differ substantially.

### Discriminating result
A monotonic effect of expected value with no residual inverted-U uncertainty component after expected-value matching would favor this mechanism.

---

## Mechanism 4: Temporal anticipation, temporal hazard, or serial timing-related prediction errors

### Account
Delay activity reflects passage of time toward a possible outcome or the changing conditional likelihood of an event at each moment, rather than uncertainty about reward identity or probability.

### Predictions
- Activity changes systematically as the expected time approaches.
- Altering the cue-to-outcome interval or its temporal distribution shifts the activity profile in time.
- At a fixed time point, probability-dependent effects are absent or are fully captured by an explicit temporal-hazard model.
- A common ramp or decline occurs across probabilities when timing is identical.

### Discriminating result
A signal that changes with reward timing but not with reward probability once timing is controlled would favor a temporal account.

### Important limit
Temporal expectation and uncertainty need not be mutually exclusive. A result may reveal both a probability-related component and a time-dependent component. The experiment should therefore estimate both rather than force a single-mechanism interpretation.

---

## Mechanism 5: Non-specific arousal, movement, sensory, or recording artifact

### Account
Probability cues alter licking, orienting, locomotion, pupil-linked state, cue salience, or recording stability; neural differences are secondary to these factors.

### Predictions
- Apparent delay effects covary with movement or anticipatory behavior.
- Effects are tied to one cue identity rather than its learned contingency.
- Effects fail to reverse after cue–probability reassignment.
- Effects disappear under movement/state covariates or are inconsistent across recording modalities.

### Discriminating result
A probability effect that follows cue contingencies across counterbalanced cues and reversals, and survives measured behavioral-state adjustment, is less consistent with this explanation. It would not eliminate all unmeasured-state explanations.

---

# 4. Proposed research plan

## Overview

The study should proceed in ordered stages. The primary experiment is observational: it asks what information is present in dopamine-neuron activity during waiting. A causal intervention should be considered only after an interpretable observational signal has been established.

## Unreported parameters that must be fixed before execution

The packet does not report the following. They must be specified prospectively rather than inferred:

- species, strain, sex balance, age, housing, and reward type;
- dopamine-neuron identification method;
- recording modality;
- cue modality;
- reward magnitudes and delay duration;
- required sample size;
- behavioral criterion for learned cue contingencies;
- smallest biologically relevant neural effect;
- welfare limits and technical exclusion criteria.

None of these are claims about the original observations.

---

## Stage 0: Prerequisites and assay qualification

### 0.1 Define the biological unit and neural identity

**Primary biological replication unit:** animal.

**Nested observational units:** sessions, trials, and recorded neurons within animals.

Neurons and trials must not be treated as independent biological replicates. They increase precision but do not replace animal-level replication.

**Requirement:** use a prospectively specified dopamine-neuron identification criterion. If the method identifies neurons only provisionally, results must be described as arising from *putative dopamine neurons*, not definitively from dopamine neurons.

A robust design would use:

1. a primary method capable of resolving individual neuronal activity, and  
2. an orthogonal measure, where feasible, of dopamine-population activity or dopamine release.

The packet does not specify a method; thus this is a proposed safeguard, not a reported author method.

### 0.2 Establish stable learned behavior

Before neural testing, animals must demonstrate that cues alter reward expectation. Suitable prespecified behavioral measures include anticipatory approach, licking, lever contact, or another task-relevant response.

The behavioral analysis should test whether the response during the waiting period changes systematically with programmed reward probability and/or calibrated expected value.

**Interpretation rule:** if animals do not behaviorally distinguish cue contingencies, absence of a neural probability effect is not interpretable as evidence against neural coding. Such sessions should be classified as failed task acquisition, retained in reporting, and not silently discarded.

### 0.3 Calibrate reward magnitude to subjective value

The central uncertainty-versus-value comparison requires expected value to be held approximately constant while probability changes. Objective reward volume alone may not achieve this.

Proposed calibration:

1. Present choices between alternatives differing in reward probability and reward magnitude.
2. Estimate, for each animal, reward magnitudes that produce approximate behavioral indifference at selected probabilities.
3. Use those animal-specific values to create approximately equal-expected-value conditions.

For example, if subjective value were linear, reward magnitudes of 4, 2, and 1.33 units at probabilities 0.25, 0.5, and 0.75 would have equal objective expected value. **This linearity is only an example and must not be assumed.** The actual values should be selected from the behavioral calibration.

### 0.4 Establish timing behavior

Use limited, preplanned probe trials to assess whether animals anticipate the possible outcome time. These probes should be separated from the main analysis because omission trials themselves can alter learning and motivation.

The goal is not to eliminate temporal expectation—timing is part of the question—but to measure it and model it.

---

## Stage 1: Main fixed-time probability experiment

### 1.1 Core task structure

A proposed trial structure:

1. **Baseline:** 1 s before cue.
2. **Cue:** 0.5 s sensory cue indicating a reward contingency.
3. **Fixed delay:** 4 s from cue onset to possible outcome.
4. **Outcome time:** reward delivered or omitted according to the cue-specific probability.
5. **Intertrial interval:** variable, for example 6–10 s, to reduce predictable trial onset.

The exact durations are proposed parameters. The key requirement is that all main probability conditions have the **same cue-to-possible-outcome interval**.

At the outcome time, a common neutral event marker should occur on all trials if technically possible, while reward delivery differs according to contingency. This makes the temporal event explicit and reduces ambiguity about whether the animal experienced a distinct time point on omission trials.

### 1.2 Core probability conditions

Use at least three intermediate probabilities:

- \(p=0.25\)
- \(p=0.50\)
- \(p=0.75\)

Optional near-certain reference conditions:

- \(p=0.90\) or 1.00
- \(p=0.10\) or 0.00

Near-zero and near-one conditions are informative about certainty but may require special handling because a never-rewarded cue can become behaviorally irrelevant. They should therefore be treated as reference conditions, not the sole test.

### 1.3 Two complementary condition sets

#### Set A: Same reward magnitude, varying probability

All rewarded trials deliver the same amount.

Purpose:
- measures the natural relation between probability and waiting activity;
- distinguishes monotonic probability/expected-value effects from inverted-U uncertainty effects;
- enables comparison of \(p=0.25\) and \(p=0.75\), which have the same simple uncertainty but different expected values.

Limitation:
- expected value necessarily covaries with probability.

#### Set B: Behaviorally matched expected value, varying probability

Reward magnitude varies inversely with probability using the calibration in Stage 0.

Purpose:
- tests whether an uncertainty effect remains when expected value is approximately matched;
- separates a probability/uncertainty signal from a simple expected-value signal.

Limitation:
- varying reward magnitude introduces differences in the future sensory and consummatory consequences of reward. This is acceptable for the waiting-period question if outcome-time analyses are kept separate, but it remains a possible source of learned cue differences.

### 1.4 Cue controls and contingency reversal

Each condition should be represented by at least two cue exemplars where feasible. Cue identity, modality, and assignment to probability/value condition should be counterbalanced across animals using a prespecified Latin-square or equivalent balanced allocation.

After stable learning and baseline recording, conduct a **contingency-reversal phase**:

- the cue previously associated with one probability is reassigned to another probability;
- reward magnitudes are adjusted according to the same predeclared mapping;
- recordings continue through relearning.

**Key test:** does waiting-period neural activity follow the newly learned probability/expected value, or remain attached to the cue’s sensory identity?

A cue-specific effect that does not reverse is not strong evidence for probability coding.

### 1.5 Trial scheduling and randomization

- Trial types should be interleaved rather than presented in long condition blocks.
- Cue order should be generated in advance with balanced presentation counts.
- For each probability condition, reward outcomes should be generated from an archived random-number sequence consistent with the programmed probability.
- Avoid post hoc removal of “streaks.” Streaks are part of probabilistic experience.
- The realized outcome sequence, seed, and actual reward frequency should be retained and reported.

---

## Stage 2: Temporal control experiment

The main experiment controls timing by holding it fixed. A second experiment should determine whether an observed delay signal is better explained by timing.

### 2.1 Design

Cross reward probability with temporal structure:

- **Fixed-time condition:** reward, when delivered, occurs at one known delay.
- **Variable-time condition:** reward, when delivered, occurs according to a cue-signaled distribution of possible delays.

Keep probability and calibrated expected value matched across temporal structures.

### 2.2 Predictions

- A primarily temporal signal should shift or reshape when the outcome-time distribution changes.
- A probability/uncertainty signal should retain a probability-dependent component at comparable stages of the waiting period, even after temporal-hazard regressors are included.
- A mixed result would indicate that delay activity contains both temporal and outcome-probability information.

### 2.3 Limit

This control cannot prove that all timing-related computations are absent. It can only determine whether a simple common temporal profile explains the observed probability effect.

---

## Stage 3: Measurements

## 3.1 Neural measurements

### Primary measurement
Time-resolved activity of identified dopamine neurons, aligned to:

- cue onset,
- onset of the primary waiting window,
- possible reward time,
- reward delivery,
- reward omission.

### Secondary neural measurements
Where feasible, use an orthogonal dopamine-population or dopamine-release readout. This can test whether a single-neuron result generalizes to a population-level signal.

### Predefined neural end points

1. **Mean baseline-corrected activity** in the primary waiting window.
2. **Time-resolved activity** in fixed bins across the delay.
3. **Delay slope**, estimated per trial or condition.
4. **Cue response**, analyzed separately.
5. **Reward-delivery response** at outcome time.
6. **Omission response** at the expected outcome time.

Cue and outcome responses must not be combined with the waiting-period measure.

## 3.2 Behavioral and state measurements

Record on every trial, as available:

- anticipatory licking or approach;
- movement or locomotion;
- trial initiation and reaction measures;
- reward consumption;
- session number and time within session;
- any available arousal-related measure.

These variables are controls and mechanistic measurements, not grounds for selectively excluding inconvenient trials.

---

# 5. Allocation, blinding, quality control, and exclusions

## Allocation

- Assign cue identities to probabilities and reward magnitudes by balanced randomization across animals.
- Randomize session order for fixed-time and variable-time tasks where learning history permits.
- Balance sex and other relevant biological variables if both are included; the packet does not state whether these variables are relevant, so this should be declared prospectively.

## Blinding

Full blinding of the animal is impossible because cues intentionally signal contingencies. However:

- reward delivery should be computer-controlled;
- the experimenter should not manually select outcomes;
- neural preprocessing should be performed with condition labels masked or relabeled;
- the primary analysis code should be finalized before condition labels are unmasked;
- histological or identity validation, if used, should be scored blind to behavioral condition.

## Predefined technical exclusions

Examples of legitimate exclusions include:

- failure of neural recording quality according to a predefined criterion;
- loss of synchronization between behavior and neural recording;
- failure of reward delivery hardware;
- missing required behavioral or state recordings;
- failure to meet predeclared dopamine-neuron identity criteria.

All exclusions must be logged by animal, session, neuron, and reason. No unit should be excluded because its response contradicts the expected hypothesis.

---

# 6. Analysis plan

## 6.1 Primary confirmatory analysis

The primary model should test whether waiting-period activity contains an uncertainty term after accounting for expected value, time, and measured behavior.

A conceptual mixed-effects model is:

\[
\text{Delay activity} =
\beta_0 +
\beta_U U +
\beta_{EV} EV +
\beta_T \text{time} +
\beta_{U\times T}(U \times \text{time}) +
\beta_B \text{behavior/state} +
\text{random effects}.
\]

Where:

- \(U = 4p(1-p)\);
- \(EV\) is behaviorally calibrated expected value;
- time is elapsed time in the delay;
- behavior/state includes measured anticipatory responses and movement;
- random effects include animal, neuron nested within animal, and session.

Cue identity should be included as a controlled factor or random effect, and the reversal phase should test whether effects follow the new contingency.

## 6.2 Primary hypothesis tests

1. **Uncertainty test:** is \(\beta_U\) different from zero in the predicted positive direction?
2. **Expected-value test:** is \(\beta_{EV}\) different from zero?
3. **Timing test:** are time and probability-by-time terms needed to explain the signal?
4. **Reversal test:** does the condition effect move with learned contingency rather than cue identity?

The primary biological inference should be based on the animal-level distribution of effect estimates or a hierarchical model that appropriately clusters data by animal. It should not be based solely on a large number of neurons or trials.

## 6.3 Outcome-time analyses

These are secondary but important assay checks.

At reward delivery:
- test whether responses are larger for less predicted rewards.

At omission:
- test whether depressions are larger when reward was more expected.

These expected patterns are motivated by E1–E3. Their presence would indicate that the task engages the kind of prediction-related outcome responses described in the packet. Their absence would not automatically invalidate the study, but it would weaken interpretation that the task successfully reproduced the relevant expectation structure.

## 6.4 Effect size and power

The packet provides no effect size, variance, or sample size. Therefore an exact defensible sample size cannot be calculated from supplied evidence.

Before confirmatory data collection:

1. obtain a nonconfirmatory technical pilot or use pre-existing laboratory variance estimates;
2. define the smallest biologically relevant waiting-period effect;
3. simulate power for the planned hierarchical analysis at the **animal** level;
4. preregister the required number of valid animals and the maximum number to enroll to account for technical attrition.

The pilot must be used for feasibility and variance estimation, not for unmasked hypothesis confirmation.

---

# 7. Stop rules and troubleshooting

## Stop rules

### Scientific stopping
- Do not stop early for apparent significance.
- Complete the preregistered number of valid animals unless a predefined safety, welfare, or technical futility criterion is reached.
- If behavioral learning does not reach the predeclared criterion after a specified training limit, classify the case as nonlearned and report it. Do not reinterpret neural null results from such cases as evidence against coding.

### Technical stopping
Pause or terminate acquisition for:
- persistent failure of neural identification or recording stability;
- unrecoverable reward-delivery timing error;
- inability to collect synchronized neural, behavioral, and event-timing data;
- animal welfare criteria specified before the experiment.

## Troubleshooting table

| Problem | Likely consequence | Corrective action |
|---|---|---|
| Animals do not distinguish probabilities behaviorally | Neural probability null is uninterpretable | Revise training only before confirmatory recording; document all failures |
| Reward magnitude does not produce matched subjective value | “Uncertainty” may actually reflect expected value | Recalibrate using choice/indifference data |
| Cue identity predicts neural activity independent of contingency | Sensory confound | Use counterbalancing, multiple exemplars, and contingency reversal |
| Probability effects covary with licking or movement | State/motor confound | Include state variables in model; test whether effect survives; do not simply delete active trials |
| Neural signal drifts over session | False condition effect if trial order is imbalanced | Interleave conditions and model session/time-within-session |
| Rare-probability outcomes are undersampled | Imprecise outcome responses | Increase planned trial counts or focus primary inference on waiting activity |
| Fixed-delay effect resembles a ramp | Could be timing rather than uncertainty | Run Stage 2 temporal-distribution control |
| Effect appears in only one modality | Interpretation uncertain | Inspect measurement-specific artifacts; replicate in independent animals and assay |

---

# 8. Conditional outcomes and justified conclusions

## Outcome A: Strong uncertainty-related waiting signal

### Pattern
- Delay activity is highest near \(p=0.5\);
- the effect persists in expected-value-matched conditions;
- \(p=0.25\) and \(p=0.75\) are more similar to each other than predicted by their different expected values;
- the effect follows contingency reversal;
- it survives measured movement/state and temporal-hazard controls;
- outcome-time responses show prediction-related reward and omission responses.

### Strongest justified conclusion
In this task, dopamine-neuron activity during waiting carries information related to reward uncertainty beyond simple expected reward value and a common expected time of outcome.

### What this would not establish
It would not prove that dopamine neurons uniquely encode uncertainty, that every dopamine neuron does so, or that the signal causally controls learning or behavior.

---

## Outcome B: Monotonic expected-value/probability signal

### Pattern
- Delay activity increases or decreases monotonically with expected value;
- equal-expected-value conditions converge;
- no residual intermediate-probability peak remains.

### Strongest justified conclusion
Dopamine-neuron waiting activity carries information consistent with expected reward value or reward probability in this task. The data would not support a distinct uncertainty signal under the tested conditions.

---

## Outcome C: Timing-dependent but probability-independent signal

### Pattern
- Delay activity changes with elapsed time or outcome-time distribution;
- probability does not explain additional variance after time/hazard is modeled;
- activity shifts when expected reward timing changes.

### Strongest justified conclusion
The measured waiting activity is more consistent with temporal anticipation or timing-related expectation than with a distinct representation of reward uncertainty or probability.

---

## Outcome D: No detectable waiting-period signal

### Pattern
- No probability, expected-value, or uncertainty effect;
- narrow confidence intervals exclude the preregistered smallest biologically relevant effect;
- behavioral evidence confirms learned contingencies;
- recording and outcome-time assay checks are adequate.

### Strongest justified conclusion
Under the tested cues, reward types, timing structure, and measurement conditions, there is no detectable biologically meaningful dopamine-neuron representation of reward probability/uncertainty during the waiting interval.

### Limit
This is not a universal claim that dopamine neurons never encode uncertainty. It is limited to the tested task and detection sensitivity.

---

## Outcome E: Ambiguous mixed result

Examples:

- an intermediate-probability effect appears only with one cue identity;
- effects disappear after accounting for movement;
- a signal occurs in fixed-time but not variable-time tasks;
- single-neuron and population measurements disagree;
- expected value and uncertainty remain insufficiently separated because reward calibration failed.

### Strongest justified conclusion
The experiment would show that waiting activity differs across conditions, but would not yet identify whether the difference represents uncertainty, value, time, cue properties, or behavioral state. The next step would be to repair the specific failed discriminating control rather than claim uncertainty coding.

---

# 9. Optional follow-up only if Stage 1 is interpretable

A causal experiment should follow only if a reproducible waiting-period signal has been established.

## Proposed causal question

Is dopamine-neuron activity during the waiting interval required for learning or using reward probability/uncertainty?

## Proposed design

Compare temporally restricted perturbation during:

1. the waiting interval,
2. the outcome-time interval,
3. a matched control interval outside the trial.

Test effects on:

- subsequent behavioral estimates of reward probability;
- adaptation after contingency reversal;
- anticipatory behavior;
- outcome-time neural responses, if measurable.

## Critical control

A waiting-period manipulation must be temporally specific and must not alter sensory cue processing, reward delivery, movement, or general motivation. Otherwise a behavioral change cannot be attributed specifically to uncertainty-related waiting activity.

## Limit

The supplied packet contains no causal evidence. This stage is a proposal, not an inference from reported results.

---

# Final conclusion

The packet supports outcome-time dopamine prediction-error-like responses but leaves the waiting period untested. The highest-value next study is therefore a carefully controlled probability manipulation with fixed outcome timing, behaviorally matched expected value, cue counterbalancing and reversal, measured behavioral-state covariates, and a temporal-distribution control. A delay-period signal that peaks at intermediate probabilities, survives value and timing controls, and follows learned contingencies would justify the conclusion that dopamine-neuron activity carries uncertainty-related information while reward is pending.
