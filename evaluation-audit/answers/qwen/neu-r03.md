# Qwen3.8 Max (0902) / neu-r03

Original final answer, shared by both scoring rounds.

## 1. Lead conclusion and next biological question

**Most valuable next question:**  
**Does dopamine-neuron activity during the waiting period between a predictive cue and a possible reward carry information about the probability or uncertainty of the future reward, independently of event-triggered prediction errors, elapsed time, temporal expectation, licking/movement, and arousal?**

This is the most valuable next question because the supplied packet establishes that dopamine-neuron responses behave like signals related to **reward-prediction violations**:

- reward responses diminish as rewards become predicted;
- unexpected reward timing produces activation;
- omission at an expected time produces depression.

However, the packet explicitly states that these observations **do not establish whether activity during the waiting period carries additional information about variable outcomes**, and that **no later probability-manipulation experiment or result is included**. Therefore, the key unresolved issue is whether dopamine activity is limited to discrete event-related prediction errors or whether it also maintains or computes information about probabilistic future outcomes during the delay.

**No new results are claimed below. Everything following is a proposed question, mechanisms, and experimental plan.**

---

## 2. Evidence-to-inference-to-conclusion chain

### Evidence supplied by the packet

1. **Reward responses diminish as rewards become predicted.**  
   This indicates that dopamine responses to reward delivery are not fixed sensory responses but depend on learned expectation.

2. **Unexpected reward timing produces activation.**  
   This indicates that dopamine neurons respond when reward timing violates expectation.

3. **Omission at an expected time produces depression.**  
   This indicates that absence of an expected reward is also represented as a negative violation of expectation.

4. **The packet explicitly says the observations do not establish whether waiting-period activity carries additional information about variable outcomes.**  
   Therefore, delay activity cannot yet be interpreted as encoding probability, uncertainty, expected value, or motivational state.

5. **No probability-manipulation experiment or result is included.**  
   Therefore, no conclusion can be drawn about how dopamine neurons respond to explicit changes in reward probability.

### Permitted inference

The supplied evidence supports the inference that dopamine-neuron activity is linked to **violations of reward prediction** at or near salient events: reward delivery, unexpected timing, and expected omission.

### Not permitted

The evidence does **not** permit the inference that:

- dopamine neurons encode reward probability during the delay;
- dopamine neurons encode uncertainty;
- dopamine neurons maintain expected value between cue and outcome;
- delay activity is behaviorally meaningful;
- delay activity is distinct from motor preparation, elapsed time, arousal, or temporal expectation.

### Conclusion

The strongest justified conclusion from the packet alone is:

> Dopamine-neuron activity is event-related and sensitive to reward-prediction violations, but whether it carries additional probabilistic outcome information during the waiting period remains unresolved.

The appropriate next step is therefore a controlled experiment that manipulates **reward probability** while separating probability coding from temporal expectation, movement, arousal, and event-related prediction errors.

---

## 3. Unresolved biological question

### Primary question

**Do dopamine neurons carry information about future reward probability during the cue–reward waiting period, or is their activity during that interval fully explained by time, temporal expectation, motor preparation, arousal, or event-based reward prediction errors?**

A more operational version:

> After learning that different cues predict different probabilities of reward at a fixed or controlled time, does dopamine activity in the delay before reward differ systematically across probability conditions when reward delivery, timing structure, movement, licking, and arousal-related variables are controlled?

### Why this question matters

If dopamine neurons only generate brief event-related prediction-error signals, then waiting-period activity may be irrelevant or merely preparatory. If, however, dopamine neurons carry probability or uncertainty information during the waiting period, then dopamine signaling may contribute not only to learning from outcomes but also to representing the current probabilistic structure of the environment.

This distinction matters for interpreting dopamine in learning, motivation, decision-making, and disorders involving abnormal expectation signaling.

---

## 4. Competing mechanisms and discriminating predictions

The proposed experiment should distinguish among several mechanisms. These are not claimed to be established; they are candidate explanations to be tested.

| Mechanism | Core claim | Prediction for waiting-period dopamine activity | Discriminating test |
|---|---|---|---|
| **M1. Event-only reward prediction error** | Dopamine neurons primarily signal prediction errors at events; delay activity carries no independent probability information | No reliable effect of reward probability during the waiting period after controlling for elapsed time, licking, movement, and arousal | If probability cues produce different behavioral expectation but no delay neural effect, M1 is favored |
| **M2. Expected value / probability maintenance** | Dopamine neurons maintain information about the probability or expected value of future reward during the delay | Delay activity increases monotonically with reward probability, even before reward delivery and after controlling for movement and time | A linear positive effect of probability on delay activity, preserved on unrewarded probe trials, supports M2 |
| **M3. Uncertainty / salience coding** | Dopamine neurons encode uncertainty, variance, entropy, or arousal associated with probabilistic outcomes | Delay activity is maximal at intermediate probability, for example near 50%, producing an inverted-U or entropy-like pattern | A quadratic probability effect or entropy model outperforming a linear model supports M3 |
| **M4. Temporal hazard / urgency** | Delay activity reflects time-varying expectation of reward occurrence, not abstract probability | Delay activity tracks elapsed time and conditional hazard: the probability that reward will occur now given it has not yet occurred | Changing delay distribution while holding overall reward probability constant should change delay activity if M4 is correct |
| **M5. Motor / arousal confound** | Apparent delay activity reflects licking, movement, pupil dilation, or general arousal rather than outcome information | Probability effects disappear after controlling for licking, movement, pupil size, or trial initiation | If neural delay activity is explained by behavioral covariates, M5 must be considered |

### Key predictions summarized

#### If M1 is correct

- Waiting-period activity should not differ across probability levels after controlling for time and behavior.
- Cue and outcome responses may still vary with prediction.
- Omission at the expected time should still produce depression.
- Unexpected timing should still produce activation.

#### If M2 is correct

- Waiting-period activity should be graded by reward probability:  
  P0 < P25 < P50 < P75 < P100.
- The effect should be present before outcome delivery.
- The effect should remain when licking, movement, and pupil are included as covariates.
- The effect should be detectable even on rare omission probe trials before the time of expected outcome.

#### If M3 is correct

- Waiting-period activity should not be simply monotonic.
- Activity should be highest at intermediate probabilities or high entropy.
- An uncertainty regressor such as `p(1-p)` or entropy should fit delay activity better than linear probability.
- The effect may correlate with arousal measures, requiring careful covariate control.

#### If M4 is correct

- Delay activity should depend strongly on time within the delay and on conditional hazard.
- If reward probability is held constant but the temporal distribution of possible reward changes, delay activity should change.
- Probability may appear significant only because it is correlated with hazard or timing expectation.

#### If M5 is correct

- Probability effects should be explained by anticipatory licking, movement, pupil dilation, or other state variables.
- After adding behavioral covariates, neural probability effects should weaken or disappear.

---

## 5. Proposed research plan

This is a proposed protocol only. It does not reconstruct any author methods, because the packet provides no methods. It is designed to be ordered, auditable, and falsifiable.

---

## 5.1. Prerequisites and assumptions

### Required prerequisites

Before testing the main hypothesis, the following should be in place:

1. **A preparation in which dopamine neurons can be identified and recorded.**  
   The specific preparation is an unreported parameter in the packet and must be chosen prospectively. Possible approaches include electrophysiology of identified dopamine neurons or optical recording from genetically or anatomically defined dopamine cells. The choice must be justified and validated.

2. **A behavioral preparation capable of learning cue–outcome associations.**  
   The animal must be able to learn that discrete cues predict different probabilities of reward.

3. **Stable reward delivery.**  
   Reward magnitude, timing, and delivery probability must be controllable and measurable.

4. **Behavioral monitoring.**  
   At minimum, the setup should record licking or another measure of anticipatory behavior. If possible, movement and pupil size should also be recorded.

5. **Timing synchronization.**  
   Cue onset, reward delivery, omission, neural recording, and behavior must be aligned on a common clock.

6. **Validation of dopamine-neuron identity.**  
   If electrophysiology is used, dopamine identity should be established by validated criteria. If optical recording is used, cell-type specificity and signal quality must be validated.

### Explicit assumptions

These assumptions are not supplied by the packet and must be treated as protocol assumptions:

- The chosen preparation can learn probabilistic cue–reward associations.
- Dopamine neurons are accessible and stable enough to compare activity across probability conditions.
- Reward probability can be manipulated without unintentionally changing cue salience, reward magnitude, timing, or motor demands.
- Licking, movement, and pupil measures are sufficient to capture major behavioral confounds.
- The waiting period can be isolated from cue-evoked and outcome-evoked activity.

### Unreported parameters that must be defined before the experiment

The packet does not provide these. They should be preregistered or set by pilot work:

- species and preparation;
- dopamine neuron identification method;
- recording modality;
- reward type and volume;
- cue modalities;
- delay duration;
- intertrial interval;
- number of trials per probability;
- number of animals and neurons;
- learning criterion;
- probe-trial fraction;
- inclusion/exclusion criteria for neural units;
- statistical power target.

These should not be invented post hoc.

---

## 5.2. Overall experimental design

### Core design

Use a within-subject Pavlovian cue–reward task with several cues predicting different probabilities of the same reward.

### Proposed probability levels

Five cue conditions are recommended:

- **P0:** 0% reward;
- **P25:** 25% reward;
- **P50:** 50% reward;
- **P75:** 75% reward;
- **P100:** 100% reward.

This design allows testing for:

- linear probability coding;
- nonlinear uncertainty coding;
- baseline activity in the absence of reward expectation;
- omission-related depression.

### Reward

Use one fixed reward magnitude across all rewarded trials. Reward magnitude should not vary with probability, because varying magnitude would confound probability with expected value magnitude.

### Waiting period

Define the waiting period as the interval after cue offset and before the earliest possible outcome.

For analysis, avoid contamination by event responses by excluding small buffers around cue and outcome, for example:

- exclude the first portion after cue onset;
- exclude the last portion immediately before expected reward time;
- analyze both early-delay and late-delay epochs separately.

Exact epoch boundaries are parameters to be preregistered.

---

## 5.3. Calibration

Calibration is essential for auditability.

### 5.3.1. Reward calibration

Before behavioral training:

1. Measure delivered reward volume repeatedly across the range used.
2. Confirm that reward delivery timing is accurate.
3. Confirm that reward delivery does not produce unintended cues that differ by probability condition.
4. Confirm that reward lines are clean and delivery failures are rare.
5. Record any missed or partial deliveries as trial defects.

### 5.3.2. Cue calibration

1. Confirm that cue intensity is stable across sessions.
2. Confirm that cues do not differ in unintended salience.
3. Counterbalance cue identity across probability conditions across animals.
4. Avoid cues that predict timing differently unless timing is explicitly manipulated.

### 5.3.3. Timing calibration

1. Synchronize stimulus delivery, reward delivery, behavior acquisition, and neural recording.
2. Verify actual delay durations against intended delay durations.
3. Log all trial events with high temporal resolution.
4. Identify and exclude trials with hardware timing errors.

### 5.3.4. Neural calibration

Depending on the recording method:

1. Define signal-quality criteria.
2. Define baseline period for normalization.
3. If electrophysiology is used, define spike-sorting quality thresholds and unit stability criteria.
4. If optical recording is used, define motion correction, bleaching correction, and reference-signal controls.
5. Confirm that artifacts from reward delivery or movement do not contaminate the delay window.

### 5.3.5. Behavioral calibration

1. Set lick detection thresholds.
2. Validate movement tracking if used.
3. Validate pupil tracking if used.
4. Confirm that behavioral measures are sampled at sufficient rate to resolve delay-period changes.

---

## 5.4. Training and experimental phases

The experiment should proceed in ordered phases with explicit go/no-go criteria.

### Phase 0: Habituation and shaping

Goal: animal becomes comfortable with the setup and learns that rewards can be obtained.

Procedure:

- expose animal to apparatus;
- deliver rewards non-contingently if needed;
- establish stable reward consumption;
- confirm that the animal can perform the basic task structure.

Go criterion:

- animal reliably consumes delivered reward;
- animal shows stable engagement without excessive stress or inactivity.

No-go criterion:

- animal fails to consume reward or cannot tolerate the setup.

### Phase 1: Simple cue–reward learning

Goal: establish that cues can predict reward.

Procedure:

- initially use only P100 and P0 cues;
- P100 cue followed by reward after fixed delay;
- P0 cue not followed by reward;
- interleave trials pseudorandomly.

Measurements:

- anticipatory licking;
- reward responses;
- omission responses;
- neural activity if recording is already stable.

Go criterion:

- animal distinguishes P100 from P0 behaviorally;
- anticipatory behavior is higher for P100 than P0;
- neural event responses, if recorded, are stable.

No-go criterion:

- animal cannot discriminate the simplest rewarded and unrewarded cues.

### Phase 2: Probability learning

Goal: train all probability cues.

Procedure:

- introduce P25, P50, and P75;
- keep reward magnitude constant;
- keep delay structure initially fixed to simplify learning;
- interleave all five cue types pseudorandomly;
- ensure enough trials per probability condition.

Behavioral criterion:

- anticipatory behavior should show ordered sensitivity to probability, at least distinguishing high from low probability.

Important point:

- behavioral probability discrimination is a prerequisite for interpreting neural probability effects as cognitive or predictive rather than nonspecific.

### Phase 3: Timing-control training

Goal: prevent the animal from using a single fixed temporal expectation as the only explanatory variable.

Procedure:

- in some sessions, keep delay fixed;
- in other sessions, use variable delays;
- keep probability cues the same;
- randomly sample delay durations from a predefined distribution.

Purpose:

- dissociate reward probability from elapsed time and hazard.

Go criterion:

- animal remains engaged and shows probability-sensitive behavior despite variable delays.

No-go criterion:

- variable delays abolish task engagement or make behavior uninterpretable.

### Phase 4: Probe trials

Goal: test waiting-period activity without contamination from actual reward delivery.

Probe types:

1. **Omission probes**  
   On some nonzero-probability trials, omit reward at the expected time.  
   Purpose: examine delay activity before outcome and outcome depression after omission.

2. **Unexpected timing probes**  
   On rare trials, deliver reward earlier or later than expected.  
   Purpose: validate temporal prediction-error responses and separate time from probability.

3. **Unexpected reward probes**  
   On rare trials, deliver reward when probability was low or zero.  
   Purpose: validate activation to unexpected reward timing or occurrence.

Probe frequency:

- probe trials should be rare enough to avoid rapid extinction but frequent enough for analysis.
- exact fraction is a protocol parameter to be set by pilot data.

---

## 5.5. Trial structure

A proposed single trial:

1. **Baseline / intertrial interval**  
   Variable duration to reduce temporal conditioning.

2. **Cue onset**  
   One of the probability cues is presented.

3. **Waiting period / delay**  
   Fixed or variable duration depending on session type.

4. **Outcome window**  
   Reward delivered or omitted according to trial type.

5. **Post-outcome period**  
   Record neural and behavioral responses.

### Trial exclusion criteria

Predefine exclusion rules, for example:

- hardware failure;
- missed reward delivery;
- movement artifact exceeding threshold;
- premature behavior before cue if the task requires quiescence;
- incomplete neural recording;
- timing error.

These exclusions should be applied identically across probability conditions.

---

## 5.6. Independent units, allocation, and blinding

### Independent units

The primary independent biological unit should be the **animal**, not the trial.

Neurons or recording units are nested within animals. Trials are nested within neurons and animals. Statistical inference about biological generality should respect this hierarchy.

Recommended hierarchy:

- animal: independent biological replicate;
- session: nested within animal;
- neuron or recording unit: nested within session/animal;
- trial: repeated measurement.

Trial-level effects can be modeled, but group-level conclusions should not treat trials as independent biological replicates.

### Allocation

Where possible:

1. Randomize trial order within session.
2. Counterbalance cue identity across probability conditions across animals.
3. Counterbalance the order of fixed-delay and variable-delay sessions.
4. Randomize probe-trial placement subject to behavioral constraints.
5. If multiple recording sites or sessions are used, balance probability conditions across recording order.

### Blinding

Complete blinding may be difficult because probability conditions are part of the task design, but partial blinding is possible:

1. Use automated trial delivery and automated data acquisition.
2. Use automated preprocessing where possible.
3. Mask condition labels during manual curation of neural units if feasible.
4. Preregister the analysis plan before unblinding condition labels.
5. Use coded condition labels during exploratory model selection, with final hypotheses tested after code release.

---

## 5.7. Controls

### Positive controls

These test whether the preparation reproduces the basic phenomena described in the packet.

1. **Reward prediction control**  
   Reward responses should be smaller when reward is more predicted.

2. **Omission control**  
   Omission at an expected time should produce depression relative to expected reward.

3. **Unexpected timing control**  
   Unexpected reward timing should produce activation relative to expected timing.

If these controls fail, the assay may not be valid for testing dopamine prediction-related activity.

### Negative controls

1. **P0 cue**  
   Provides a no-reward expectation baseline.

2. **No-cue baseline periods**  
   Help define spontaneous or baseline activity.

3. **Omitted reward trials**  
   Help distinguish delay expectation from reward consumption.

### Specificity controls

1. **Movement control**  
   Include movement or licking as covariates.

2. **Arousal control**  
   Include pupil size or other arousal measures if available.

3. **Temporal control**  
   Compare fixed-delay and variable-delay sessions.

4. **Sensory control**  
   Ensure cue effects are not due to physical differences among cues.

5. **Motor-preparation control**  
   Compare delay activity before any observable preparatory behavior.

---

## 5.8. Measurements

### Neural measurements

For each trial and each validated dopamine unit, measure:

1. **Baseline activity**  
   Pre-cue period.

2. **Cue-evoked activity**  
   Window after cue onset.

3. **Waiting-period activity**  
   Delay period between cue and outcome.

4. **Outcome-evoked activity**  
   Window after reward delivery or omission.

5. **Post-outcome activity**  
   Window after outcome to capture depression or activation.

Depending on recording modality, activity may be spike rate, spike probability, fluorescence change, or another validated neural signal.

### Behavioral measurements

Measure at minimum:

1. **Anticipatory licking**  
   Lick rate during delay or before reward.

2. **Reward consumption**  
   Whether delivered reward is consumed.

3. **Movement**  
   Body or head movement if measurable.

4. **Pupil diameter**  
   If available, as an arousal proxy.

5. **Reaction or approach latency**  
   If the preparation allows.

### Trial metadata

Record:

- cue identity;
- assigned probability;
- actual outcome;
- delay duration;
- reward delivery time;
- omission status;
- probe type;
- session identifier;
- animal identifier;
- neural unit identifier;
- quality metrics.

---

## 5.9. Data preprocessing

Preprocessing should be preregistered and applied identically across conditions.

### Neural preprocessing

Depending on method:

1. Remove trials with artifacts.
2. Correct baseline drift.
3. Normalize activity within session or unit, for example z-score relative to pre-cue baseline.
4. Exclude unstable units.
5. Confirm that outcome-period activity does not leak into delay-period estimates.

### Behavioral preprocessing

1. Detect licks and movement events.
2. Compute licking rate in defined epochs.
3. Compute pupil metrics if available.
4. Exclude trials with excessive movement if predefined.

### Epoch definition

Define epochs before analysis. A possible scheme:

- baseline: pre-cue interval;
- cue window: cue onset to early delay;
- early delay: after cue-evoked response;
- late delay: before expected outcome;
- outcome window: around reward or omission;
- post-outcome window: after outcome.

The exact durations must be set prospectively.

---

## 5.10. Analysis plan

The analysis should be ordered to prevent circularity.

### Step 1: Verify behavior

Before analyzing delay neural activity, confirm that the animal learned the probability structure.

Model anticipatory behavior:

`behavior ~ probability + trial type + movement + session + random effects`

Expected behavioral pattern if learning occurred:

- higher anticipatory behavior for higher reward probability;
- appropriate suppression or modification on P0 trials;
- sensitivity to omission and timing probes.

If behavior does not distinguish probabilities, neural probability effects cannot be interpreted as learned probability coding.

### Step 2: Replicate event-related controls

Test whether the neural data show the basic packet-consistent event effects:

1. Reward responses diminish as reward becomes more predicted.
2. Unexpected timing produces activation.
3. Omission at an expected time produces depression.

Example model for outcome activity:

`outcome_activity ~ outcome_type + probability + timing_expectedness + interaction + covariates + random effects`

This step validates the assay but does not test the main waiting-period question.

### Step 3: Primary waiting-period analysis

Primary outcome variable:

- neural activity during the waiting period before outcome.

Primary candidate regressors:

1. `probability` as linear term;
2. `probability^2` or entropy for uncertainty;
3. `elapsed_time` or time-in-trial;
4. `hazard`, if variable delays are used;
5. `lick_rate`;
6. `movement`;
7. `pupil`;
8. `previous_trial_outcome`;
9. `session` and `animal` random effects.

Primary model:

`waiting_activity ~ probability + probability^2 + time_in_delay + licking + movement + pupil + previous_outcome + (1|animal) + (1|neuron)`

For trial-resolved data, use an appropriate generalized linear mixed model or hierarchical model.

### Step 4: Model comparison

Compare predefined models:

- **M0:** time and behavioral covariates only;
- **M1:** M0 + linear probability;
- **M2:** M0 + linear probability + quadratic probability or entropy;
- **M3:** M0 + hazard/time-varying temporal expectation;
- **M4:** M0 + motor/arousal interactions.

Use cross-validation or information criteria to compare models.

Decision logic:

- M1 outperforms M0 and M2: supports monotonic probability coding.
- M2 outperforms M1 with peak near intermediate probability: supports uncertainty coding.
- M3 outperforms probability-only models: supports temporal hazard coding.
- Probability effects vanish after behavioral covariates: supports motor/arousal confound.
- No model outperforms M0: no evidence for additional waiting-period information.

### Step 5: Decoding analysis

As a secondary analysis, test whether probability can be decoded from waiting-period activity.

Procedure:

1. Use waiting-period neural activity as features.
2. Train a classifier or regressor to predict probability condition.
3. Cross-validate across trials, sessions, and preferably animals.
4. Compare against shuffled-label controls.

Important caution:

- decoding should not be treated as independent biological replication if trials come from the same animals.
- cross-validation should include animal-level or session-level splits to avoid pseudoreplication.

### Step 6: Sensitivity analyses

Perform preplanned sensitivity analyses:

1. Exclude trials with high movement.
2. Exclude trials with licking in the delay.
3. Analyze early delay and late delay separately.
4. Analyze omission probe trials separately.
5. Exclude first and last trials of blocks.
6. Exclude unstable neural units.
7. Test whether effects survive removal of arousal covariates.
8. Test whether results differ across fixed-delay and variable-delay sessions.

### Step 7: Population heterogeneity

Do not assume all dopamine neurons behave identically.

Test whether:

- a single population effect explains the data;
- distinct subpopulations show different patterns;
- probability effects depend on recording site, cell type marker, or session type.

If heterogeneity is found, report it as a result rather than averaging it away without explanation.

---

## 5.11. Sample size and power

The packet provides no sample size information. Therefore, sample size should be determined prospectively.

Recommended approach:

1. Run pilot data collection sufficient to estimate variability in waiting-period activity.
2. Define a minimum effect size of biological interest before main data collection.
3. Perform power analysis or simulation-based power analysis using the hierarchical structure: trials nested in neurons nested in animals.
4. Set minimum numbers of animals, sessions, and usable neural units.
5. Do not treat trials as independent biological replicates.

A stopping rule can be:

- continue until the predefined power target is reached or until a maximum ethical and practical sample size is reached;
- if the minimum number of usable neural units or animals cannot be reached, declare the result underpowered rather than interpreting a null effect as strong evidence of absence.

---

## 5.12. Stop rules

Stop rules should be defined before testing the main hypothesis.

### Stop data collection for a neural unit if:

- signal quality falls below predefined threshold;
- unit identity is unstable;
- there are too few usable trials per probability condition;
- movement or reward-delivery artifacts contaminate the delay window.

### Stop the session if:

- reward delivery fails repeatedly;
- timing synchronization fails;
- the animal stops consuming reward;
- behavioral engagement collapses;
- excessive movement prevents interpretable delay activity.

### Stop the experiment and revise the design if:

- animals cannot learn probability discrimination after sufficient training;
- positive controls described in the packet consistently fail;
- delay activity is completely explained by movement or licking;
- probability conditions are behaviorally indistinguishable;
- probe trials cause rapid extinction or severe behavioral disruption.

### Do not draw a definitive biological conclusion if:

- sample size is below the preregistered minimum;
- too few trials remain after exclusion;
- neural identity is uncertain;
- probability is confounded with timing or movement;
- model comparison is underpowered.

In such cases, the correct conclusion is “inconclusive,” not “negative.”

---

## 5.13. Troubleshooting

### Problem 1: Animals fail to learn probability differences

Possible remedies:

- increase reward value;
- reduce number of probability levels initially;
- use larger probability contrasts;
- increase training duration;
- use blockwise training before interleaving;
- simplify cues;
- verify cue detectability.

### Problem 2: Delay activity is contaminated by licking

Possible remedies:

- analyze only no-lick delay epochs;
- add licking as a time-varying covariate;
- shorten or lengthen delay to separate licking from neural signal;
- use a task requiring quiescence, if ethically and practically feasible.

### Problem 3: Timing expectation dominates

Possible remedies:

- use variable delays;
- model hazard explicitly;
- include timing probes;
- compare fixed-delay and variable-delay sessions;
- avoid making one cue always predict the same exact time unless timing is part of the hypothesis.

### Problem 4: Probe trials cause extinction

Possible remedies:

- reduce probe frequency;
- use separate probe sessions;
- return to high-rate reinforcement after probes;
- analyze early probe trials only;
- model trial-by-trial learning effects.

### Problem 5: Neural signal drifts

Possible remedies:

- restrict analysis to stable units;
- normalize within session;
- use drift correction if appropriate;
- exclude sessions with unstable baselines;
- increase recording stability.

### Problem 6: Positive controls fail

Possible interpretations:

- dopamine neurons are not correctly identified;
- the behavioral task does not generate appropriate predictions;
- timing structure is not learned;
- reward value is too low;
- recording modality lacks temporal resolution;
- the preparation differs biologically from the conditions under which the packet observations were made.

In this case, the main hypothesis should not be tested until assay validity is restored.

---

## 6. Conditional outcomes and their interpretation

### Outcome A: Positive evidence for probability coding

Pattern:

- waiting-period activity increases monotonically with reward probability;
- effect remains after controlling for time, licking, movement, and pupil;
- effect is present before outcome delivery;
- effect is detectable on omission probe trials before expected outcome;
- linear probability model outperforms null and uncertainty models;
- event-related positive controls are present.

Strongest justified conclusion:

> Dopamine neurons carry additional information about reward probability during the waiting period, beyond event-related prediction-error responses.

Limits:

- this would establish encoding, not causal necessity;
- it would not prove that downstream circuits use this information;
- it would not establish whether the signal is probability, expected value, motivation, or confidence unless those are separately dissociated;
- it would apply to the tested preparation, probabilities, delays, and reward conditions.

---

### Outcome B: Positive evidence for uncertainty coding

Pattern:

- waiting-period activity is maximal at intermediate probability;
- quadratic probability or entropy model outperforms linear probability;
- effect is not explained by movement, licking, or timing;
- effect persists after controlling for arousal, or arousal is measured and shown not to account for the neural pattern.

Strongest justified conclusion:

> Dopamine waiting-period activity reflects outcome uncertainty or probabilistic variance rather than simple monotonic reward probability.

Limits:

- uncertainty, salience, arousal, and engagement can be correlated;
- if pupil or movement correlates strongly with the inverted-U pattern, the conclusion becomes ambiguous;
- additional manipulations may be needed to separate informational uncertainty from motivational salience.

---

### Outcome C: Negative evidence for waiting-period outcome information

Pattern:

- no reliable effect of probability or uncertainty during waiting period after controlling for time and behavior;
- positive event-related controls are present;
- adequate power and sufficient trials;
- behavior shows probability learning;
- model comparison favors null or time-only model.

Strongest justified conclusion:

> Under the tested conditions, there is no evidence that dopamine waiting-period activity carries additional probability or uncertainty information beyond event-related prediction errors, elapsed time, and measured behavior.

Important limitation:

- this is not proof that dopamine neurons never carry such information;
- it may be absent in this preparation, task structure, recording method, or probability range;
- insufficient sensitivity would weaken the negative conclusion.

---

### Outcome D: Ambiguous outcome

Examples:

1. Probability effect appears only late in the delay.
2. Probability effect disappears when licking is controlled.
3. Probability effect appears only in fixed-delay sessions.
4. Probability and hazard are collinear and cannot be separated.
5. Different neurons show different patterns.
6. Probability effect appears only after reward omission.
7. Behavioral and neural probability effects are confounded by arousal.

Strongest justified conclusion:

> The data do not uniquely identify a mechanism. The observed waiting-period activity may reflect probability, uncertainty, temporal hazard, motor preparation, or arousal, and further orthogonal manipulations are required.

Next actions would include:

- better dissociation of probability and hazard;
- motor-free delay epochs;
- additional arousal measurements;
- larger probability contrasts;
- perturbation experiments if encoding is established.

---

## 7. Strongest overall justified conclusion from the supplied packet

From the supplied packet alone, the strongest justified conclusion is:

> Dopamine-neuron responses are linked to violations of reward prediction at events: predicted rewards evoke smaller responses, unexpected timing evokes activation, and expected omission evokes depression. The packet does not establish whether dopamine activity during the waiting period carries additional information about variable outcomes. Therefore, the most valuable next step is a controlled probability-manipulation experiment that tests whether delay activity encodes probability or uncertainty independently of timing, movement, arousal, and event-related prediction errors.

If the proposed experiment yields a robust, behavior-independent probability effect in the waiting period, the strongest conclusion would be:

> Dopamine neurons can carry additional probabilistic outcome information during the waiting period, not merely event-triggered reward prediction errors.

If the proposed experiment yields no such effect under adequately powered and controlled conditions, the strongest conclusion would be:

> There is no evidence, under those conditions, that dopamine waiting-period activity carries additional probabilistic outcome information; the observed phenomenon may remain event-based.

In neither case would the result establish causality, downstream use, or generality across brain regions, species, tasks, or motivational states.

---

## 8. What would change the recommendation

The recommendation would change if new information showed that:

1. **Waiting-period activity cannot be separated from movement.**  
   Then the priority would shift to developing a motor-free or strongly movement-controlled task before testing probability coding.

2. **Temporal expectation dominates the delay.**  
   Then the priority would shift to explicitly modeling and manipulating hazard rather than testing probability alone.

3. **Animals cannot learn probability cues.**  
   Then the priority would shift to simpler probability contrasts or block designs.

4. **Dopamine identity or recording sensitivity is inadequate.**  
   Then the priority would shift to improving cell-type identification or temporal resolution.

5. **Preliminary data show strong delay probability effects.**  
   Then the next question would shift from “does it exist?” to “what variables does it represent, and is it causally used by downstream circuits?”

6. **Preliminary data show no delay effects but strong event effects.**  
   Then the next question would be whether probability information appears only at cue or outcome events, not during the delay.

---

## 9. Final concise statement

The packet shows that dopamine neurons respond to reward-prediction violations at events but does not show what they do during the waiting period. The most valuable next biological question is therefore:

**Does dopamine-neuron waiting-period activity encode reward probability or uncertainty, or is it explained by event-related prediction errors, temporal expectation, motor preparation, and arousal?**

The proposed experiment is a controlled, preregistered probability-manipulation task with multiple probability cues, timing controls, omission and timing probes, behavioral covariates, hierarchical statistics, and explicit stop rules. A positive result would justify the conclusion that dopamine carries additional delay-period outcome information; a negative result would justify only that no such information was detected under the tested conditions; ambiguous results would require further dissociation of probability, hazard, movement, and arousal.
