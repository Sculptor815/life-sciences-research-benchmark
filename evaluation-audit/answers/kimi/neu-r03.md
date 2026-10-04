# Kimi K3 / neu-r03

Original final answer, shared by both scoring rounds.

## 1. Recommended next biological question

**Do dopamine signals during the learned cue-to-reward waiting period encode reward uncertainty or another feature of the outcome distribution, independently of expected reward value, elapsed time, sensory cue identity, arousal and movement?**

The most valuable next experiment is a **preregistered, within-animal Pavlovian probability and outcome-distribution study** with:

1. A fixed cue-to-reward interval;
2. Cues spanning reward probabilities from certain omission to certain reward;
3. Certain and risky outcomes matched as closely as possible for expected value;
4. Trial-resolved recording of dopamine, licking, movement and other state variables; and
5. Animal, not trial, as the independent experimental unit.

A causal manipulation should wait until an anticipatory uncertainty signal has been demonstrated and separated from behavior. Otherwise, a null or positive perturbation result would be difficult to interpret.

---

## 2. Evidence-to-inference-to-conclusion chain

| Supplied evidence | Justified inference | What is not yet established | Experimental implication |
|---|---|---|---|
| “During learning, dopamine-neuron responses to rewards diminish as rewards become predicted.” | Outcome-period dopamine activity changes with reward expectation. | Whether the signal represents only scalar expectation or also the spread of possible outcomes. | Parametrically vary reward probability while recording before outcome. |
| “Unexpected timing produces activation.” | Dopamine can respond to a violation of temporal expectation. | Whether waiting-period activity represents elapsed time, temporal hazard, reward uncertainty, or some combination. | Hold cue-to-outcome timing fixed in the primary experiment; test temporal uncertainty separately. |
| “Omission at an expected time produces a depression.” | Absence of an expected reward can be represented at the scheduled outcome time. | Whether anticipatory activity differentiates certain from uncertain omission/reward. | Include certain-no-reward and probabilistic cues. |
| “These observations connect neural activity with violations of reward prediction.” | The observations are compatible with prediction-error-like outcome coding. | They do not by themselves prove a complete reward-prediction-error code or an uncertainty code. | Outcome-period responses should be internal positive controls, while the waiting period is the new inferential target. |
| “They do not establish whether activity during the waiting period carries additional information about variable outcomes.” | The central missing biological variable is anticipatory information about outcome variability. | The direction, form and function of any uncertainty representation are unknown. | Dissociate expected value, variance/entropy, timing and behavioral state. |
| “No later probability-manipulation experiment or result is included.” | No probability effect can be treated as reported. | The packet cannot support a conclusion that anticipatory dopamine does or does not encode probability. | The following probability experiment is proposed, not an author result. |

**Conclusion from the packet:** outcome and timing manipulations establish prediction-dependent dopamine responses, but the unresolved next step is to determine what learned dopamine activity represents **before** the outcome.

---

## 3. Reported observations versus proposed work

### Reported by the packet

- Reward responses diminish as rewards become predicted.
- Unexpected reward timing activates dopamine neurons.
- Omission at an expected time depresses dopamine activity.

### Not reported

- The species, recording method, brain region, behavioral task, reward type, sample size or analysis.
- A probability-manipulation experiment.
- Evidence that waiting-period dopamine tracks uncertainty.
- Evidence that such activity causes risk-sensitive behavior.

### Proposed here

The task, recording preparation, sample-size procedure, analyses and controls below are **new proposals**, not reconstructed author methods.

---

## 4. Competing mechanisms and discriminating predictions

### Mechanism A: Scalar expected value or utility

Waiting-period dopamine primarily represents the expected value of the future reward.

**Predictions**

- Across cues predicting reward with probability \(p\), activity should increase monotonically with \(p\), allowing for nonlinear subjective utility.
- After expected value is included, there should be no residual maximum or minimum at \(p=0.5\).
- Certain and risky cues with matched expected value should evoke similar waiting-period activity.

### Mechanism B: Outcome-variance coding

Dopamine carries the statistical spread of possible rewards in addition to expected value.

For a binary reward of fixed size,

\[
\mathrm{Variance} \propto p(1-p).
\]

**Predictions**

- After the expected-value term is removed, the uncertainty component is greatest at \(p=0.5\), intermediate and approximately equal at \(p=0.25\) and \(p=0.75\), and lowest at \(p=0\) and \(p=1\).
- The sign could be positive or negative:
  - Positive: uncertainty increases waiting dopamine.
  - Negative: uncertainty decreases it, potentially representing precision or certainty.
- In a matched-expected-value module, a high-variance distribution should differ from a low-variance or certain distribution.
- With appropriately constructed distributions, a variance code predicts:

\[
\text{all-or-none risk} > \text{magnitude risk} > \text{certain reward}.
\]

### Mechanism C: Outcome entropy or number-of-alternatives coding

Dopamine represents how many distinguishable outcomes are possible, rather than their numerical spread.

**Predictions**

- A two-outcome all-or-none cue and a two-outcome variable-magnitude cue should produce similar waiting activity because both have two alternatives.
- Both should differ from a one-outcome certain cue:

\[
\text{all-or-none} = \text{magnitude risk} > \text{certain}.
\]

This differs from variance coding, which predicts a larger response for the all-or-none distribution when its reward spread is greater.

### Mechanism D: Temporal prediction or hazard coding

Waiting dopamine reflects elapsed time or the changing probability that reward is now due, rather than uncertainty about the reward itself.

**Predictions**

- Activity should show a reproducible time course across the fixed delay.
- Probability may scale the ramp, but it should not produce a distributional residual after expected value and time are modeled.
- In a separate manipulation, changing the distribution of cue-to-reward delays while holding reward probability and magnitude fixed should alter the waiting-period time course.

### Mechanism E: Arousal, attention or movement preparation

The apparent waiting signal is generated by anticipatory licking, posture, pupil state, orienting or general arousal.

**Predictions**

- Trial-by-trial dopamine activity is strongly associated with behavioral/state measurements.
- Condition differences disappear or reverse in behavior-matched trial subsets.
- Matched-expected-value risky and certain cues do not differ once behavior is equated.

A correlation with behavior would not by itself prove that dopamine is epiphenomenal, because dopamine could be upstream of behavior. This mechanism therefore requires converging behavioral matching and, eventually, causal tests.

### Mechanism F: Sensory or associative-history artifact

The response is tied to the physical cue or the order in which contingencies were learned, not probability.

**Predictions**

- Responses cluster by cue identity rather than assigned probability.
- Across animals with counterbalanced cue assignments, the same physical cue does not consistently produce the same neural pattern.
- After cue-contingency remapping and relearning, the neural pattern should follow the old cue rather than the new probability if this mechanism is correct. A genuine learned probability signal should follow the remapped contingency.

---

## 5. Proposed experimental protocol

The following is an auditable exemplar using adult mice and a validated dopamine recording signal. Because the packet does not specify the original preparation, the same design could be implemented with another established dopamine-neuron assay. If dopamine-release photometry is used, it should not be described as direct single-neuron firing.

### 5.1 Primary biological unit and preparation

1. **Independent unit:** one animal.
2. Use both sexes, with randomized and stratified assignment of cue mappings.
3. Record from one prespecified dopamine source or terminal field per animal.
4. If using photometry:
   - Include an activity-independent reference channel where technically supported.
   - Verify probe placement after the experiment.
5. If using electrophysiology:
   - Use prespecified waveform stability and neuron-identification criteria.
   - Nest neurons within animals in analysis; do not treat neurons as independent replicates.
6. An optional independent cohort can use a complementary method, but replication should retain animal as the unit.

### 5.2 Prerequisites

Before data collection:

1. Obtain ethical and animal-care approval.
2. Preregister:
   - Primary question;
   - Conditions and windows;
   - Minimum effect of interest;
   - Exclusion criteria;
   - Primary model;
   - Replication criteria;
   - Stop rules.
3. Select and calibrate a reward magnitude \(M\) that is behaviorally detectable but not saturating.
4. Build and validate automated delivery of:
   - At least \(0\), \(0.5M\), \(M\), \(1.5M\) and \(2M\);
   - Reward probabilities \(0, 0.25, 0.50, 0.75, 1\).
5. Timestamp cue onset, reward command, measured reward delivery, licks, movement and neural samples on a common clock.
6. Create the outcome sequences in advance using independently sampled Bernoulli draws for probabilistic cues. Save seeds and realized reward fractions.
7. Run a small technical pilot—approximately four to six animals, subject to local feasibility—to estimate recording and behavioral variance. Do not use the pilot to support or reject the biological hypothesis.

### 5.3 Core cue conditions

Use seven perceptually distinct cues. Randomly assign cue identities to conditions across animals.

| Condition | Probability of any reward | Outcome distribution | Nominal expected amount |
|---|---:|---|---:|
| P0 | 0 | Always 0 | 0 |
| P25 | 0.25 | \(M\) or 0 | \(0.25M\) |
| P50 | 0.50 | \(M\) or 0 | \(0.50M\) |
| P75 | 0.75 | \(M\) or 0 | \(0.75M\) |
| SURE | 1.00 | Always \(M\) | \(M\) |
| AON | 0.50 | \(2M\) or 0, each with probability 0.5 | \(M\) |
| MAG | 1.00 | \(0.5M\) or \(1.5M\), each with probability 0.5 | \(M\) |

The P0–SURE ladder separates expected value from \(p(1-p)\).

The SURE/AON/MAG trio gives stronger distributional discrimination:

- **Linear expected value:** all three are nominally matched.
- **Variance:** AON \(>\) MAG \(>\) SURE.
- **Outcome-number entropy:** AON \(=\) MAG \(>\) SURE.
- **Reward-presence uncertainty:** AON should differ from both reward-certain conditions.

Nominal expected value is not necessarily subjective expected utility. This limitation is addressed through magnitude calibration and sensitivity analyses rather than assumed away.

### 5.4 Trial structure

Proposed defaults, to be adjusted only during pilot testing and locked before confirmatory data collection:

1. Cue duration: 0.5 s.
2. Fixed scheduled outcome time: 2.0 s after cue onset.
3. Intertrial interval: randomly drawn from the same distribution for every condition, approximately 6–10 s.
4. No operant response is required; outcomes are delivered according to the cue contingency.
5. Interleave all conditions within every session.
6. Use approximately 40 trials per cue per session.
7. After learning, collect three confirmatory sessions, yielding roughly 120 cue presentations per condition per animal.

Independent Bernoulli outcome sequences are preferable to overbalanced schedules because overbalancing creates learnable local dependencies. Realized probabilities should nevertheless be logged and included in quality checks.

### 5.5 Learning phase

Train animals on the interleaved seven-cue task.

A proposed learning criterion is:

1. At least three consecutive sessions;
2. A positive relationship between anticipatory licking or another stable approach measure and reward probability;
3. Higher anticipatory behavior for P75/SURE than P0/P25;
4. No strong improving or declining trend across the final three sessions;
5. Realized reward fractions within prespecified tolerance of programmed probabilities.

Animals that fail a prespecified maximum training duration should be reported as nonlearners and excluded from the learned-contingency analysis without reference to their neural effect direction.

Once criterion is reached, begin confirmatory recording promptly. Prolonged overtraining may change anticipatory representations and should not be added opportunistically.

### 5.6 Calibration

#### Reward calibration

Before each session:

1. Deliver at least 20 pulses at each reward magnitude.
2. Weigh or otherwise measure delivered volume.
3. Confirm that magnitude ordering is correct and within a prespecified coefficient-of-variation threshold, such as 5%.
4. Verify the actual interval between cue onset and reward.
5. Abort or repair a session if pump or timing calibration fails.

#### Neural calibration

1. Confirm adequate baseline stability and reward-evoked responsiveness before using an animal.
2. Apply the same preprocessing pipeline to every condition.
3. Use an independent motion/reference signal where available.
4. Align all trials to measured cue and outcome timestamps.
5. Verify anatomical placement without knowledge of condition effects.
6. Predefine the minimum signal-to-noise and artifact thresholds before unblinding condition assignments.

#### Behavioral calibration

1. Calibrate lick sensors or pose tracking.
2. Record video, whole-body movement and, if available, pupil size.
3. Verify that cue intensities and durations are matched as closely as possible.
4. Record satiety-related variables such as session duration and reward count.

### 5.7 Allocation and blinding

- Randomize each animal’s physical cue-to-probability mapping.
- Balance mapping across sex and cohort.
- Interleave trial conditions within session.
- Lock randomized outcome sequences before the session.
- Experimenters cannot practically be blinded while operating the apparatus, but:
  - Behavioral videos should receive coded labels;
  - Preprocessing should run without condition labels;
  - The primary analyst should receive a shuffled condition key until quality-control and model-fitting scripts are complete;
  - Histology and recording-quality exclusions should be made blind to the primary result.
- Use an independent replication cohort with cue mappings swapped.

### 5.8 Measurements

For every trial, preserve raw and processed data:

1. Cue identity and assigned condition;
2. Programmed and delivered reward;
3. Actual cue and outcome times;
4. Trial number and session;
5. Previous-trial outcome;
6. Dopamine signal;
7. Anticipatory licks;
8. Post-reward consumption;
9. Movement and pupil measures where available;
10. Artifact and exclusion flags.

Proposed windows:

- **Baseline:** 1.0 to 0 s before cue;
- **Early cue response:** 0 to 0.5 s;
- **Primary waiting window:** 0.75 to 1.75 s after cue onset, ending before the scheduled outcome;
- **Outcome window:** 2.0 to 2.5 s after cue onset;
- A time-resolved analysis should cover the full delay.

The waiting window is primary because the packet specifically leaves unresolved whether information is present during this period.

---

## 6. Internal positive controls

Before interpreting the new waiting-period result, test whether the preparation reproduces the qualitative patterns described in the packet.

### Rewarded trials

Fit outcome-window activity as a function of \(p\). The expected pattern is a smaller reward response as probability increases.

### Unrewarded probabilistic trials

Compare activity after the scheduled outcome time across P25, P50 and P75. Omission-related depression should generally become stronger where reward was more probable.

### Certain controls

- SURE validates reward delivery and predicted-reward responses.
- P0 establishes activity after a cue for which reward is never predicted.

Failure of these controls does not prove the packet’s observations are wrong; it may reflect a different preparation. It does mean that a new null uncertainty result should not be interpreted as a well-validated absence until the assay problem is resolved.

---

## 7. Analysis plan

### 7.1 Preprocessing

1. Keep the raw signal immutable.
2. Correct recording drift and motion according to the preregistered pipeline.
3. Normalize within session using a prespecified baseline.
4. Exclude artifact-contaminated trials by condition-blind rules.
5. Calculate the mean or area under the curve for each window.
6. Retain both trial-level data and animal-level summaries.

### 7.2 Primary probability analysis

For each animal, model waiting-period activity \(D\) as:

\[
D =
\beta_0 +
\beta_V p +
\beta_U p(1-p) +
\beta_T t +
\beta_S s +
\beta_R r_{t-1} +
\beta_B b_t +
\epsilon,
\]

where:

- \(p\) is assigned reward probability;
- \(p(1-p)\) is binary outcome variance;
- \(t\) is trial number;
- \(s\) is session;
- \(r_{t-1}\) is the previous outcome;
- \(b_t\) contains baseline, movement or other nuisance measures;
- \(\beta_V\) is the expected-value component;
- \(\beta_U\) is the uncertainty component.

Fit the model separately within each animal and test the distribution of \(\beta_U\) across animals. Use a hierarchical mixed-effects model as a secondary analysis with animal as a random effect and cue mapping accounted for.

**Primary inferential test:** whether \(\beta_U\) differs from zero across animals.

Because the packet provides no basis for assuming a direction, use a two-sided test. A positive coefficient supports uncertainty-related activation; a negative coefficient supports uncertainty-related suppression, not absence of coding.

### 7.3 Matched-outcome-distribution analysis

For each animal, calculate:

1. AON − SURE;
2. MAG − SURE;
3. AON − MAG.

Expected patterns:

- Variance code: AON \(>\) MAG \(>\) SURE;
- Entropy code: AON \(=\) MAG \(>\) SURE;
- Presence-only uncertainty: AON \(>\) MAG \(=\) SURE;
- Scalar expected value: AON \(=\) MAG \(=\) SURE.

Use animal-level confidence intervals and control the three comparisons with a preregistered multiple-comparison procedure.

### 7.4 Utility sensitivity analysis

Reward magnitude may have nonlinear subjective value. Therefore:

1. Measure post-reward consumption and/or behavior under deterministic cues spanning the relevant magnitudes;
2. Fit a monotonic magnitude-response curve where behavior permits;
3. Recompute expected value under a range of plausible utility transformations;
4. Repeat the variance, entropy and expected-value comparisons.

A distributional conclusion is strongest when its ordering survives physical-value and utility-sensitivity analyses. A separate choice-preference assay can estimate a sure equivalent, but that is a proposed secondary calibration rather than evidence already in the packet.

### 7.5 Behavioral-state analyses

Run the primary model without behavioral covariates first, because anticipatory behavior may be downstream of dopamine.

Then conduct secondary models that:

1. Add trial-wise licking, movement and pupil state;
2. Compare condition effects in behavior-matched subsets;
3. Examine trials with no detectable anticipatory lick;
4. Test whether neural condition differences remain when behavior distributions overlap.

If behavioral adjustment removes the effect, this is ambiguous: it may indicate an arousal artifact or that dopamine and behavior are linked parts of the same biological process.

### 7.6 Temporal analysis

1. Compare the full waiting-period time course across probabilities.
2. Test probability-by-time and uncertainty-by-time interactions.
3. Fit expected-value-only and expected-value-plus-uncertainty models at each time point.
4. Use animal-level summaries or hierarchical models rather than treating time bins as independent.

After the primary experiment, use a separate timing module:

- Fixed-delay risky cue;
- Variable-delay risky cue with the same reward probabilities and magnitudes;
- Matched certain cues.

Temporal coding predicts a changed time course under variable delay. Outcome-distribution coding predicts that the risky-versus-certain contrast persists when temporal parameters are accounted for.

### 7.7 Model comparison and decoding

As secondary analyses, compare:

1. Expected-value-only model;
2. Expected-value plus variance;
3. Expected-value plus entropy;
4. Expected-value plus elapsed-time terms;
5. Full model.

Use cross-validation separated by animal. A decoder may be used to ask whether waiting activity predicts the outcome distribution beyond expected value and behavior, but decoding should supplement—not replace—the interpretable coefficient tests.

---

## 8. Sample size, replication and independence

The packet contains no effect size, so a defensible fixed sample size cannot be supplied.

Recommended procedure:

1. Use the pilot only to estimate behavioral and neural variance.
2. Define the smallest meaningful uncertainty effect before confirmatory analysis, for example:
   - 20% of the waiting-period dynamic range between SURE and P0; or
   - If that range is near zero, 0.25 within-animal residual standard deviations.
3. Simulate the exact seven-condition schedule, planned trial count and animal-level model.
4. Choose \(N\) for approximately 90% power at the preregistered alpha level.
5. Conduct an independent replication cohort.
6. Treat sex as a prespecified stratification or exploratory factor unless the sample is explicitly powered for sex interactions.

Trials, time bins, neurons and sessions are nested measurements. They improve precision but are not independent biological replicates.

---

## 9. Stop rules

### Technical stop

Pause data collection if:

- Reward-volume calibration exceeds its prespecified error threshold;
- Outcome timing exceeds the accepted timestamp tolerance;
- More than a prespecified fraction of trials contain recording artifacts;
- Actual outcome probabilities diverge materially from programmed probabilities;
- The recording no longer passes signal-quality criteria.

Repair the apparatus and restart the affected session. Do not remove animals because their biological effect is in the “wrong” direction.

### Assay-validity stop

Do not draw a biological conclusion from a cohort in which:

- Animals fail the learning criterion;
- Rewarded and certain-omission controls are indistinguishable;
- Recording placement fails;
- Positive-control outcome responses cannot be detected.

### Futility stop

Avoid repeated informal looks at the data. If one blinded interim analysis is planned in advance, stop for futility only if the confidence interval for the uncertainty coefficient lies entirely within the prespecified equivalence interval around zero. Otherwise complete the planned sample.

### Welfare stop

Apply prespecified institutional criteria for distress, excessive weight loss, injury or failure to recover. Welfare exclusions should be documented and reported separately from biological exclusions.

---

## 10. Troubleshooting

| Problem | Likely interpretation | Corrective action |
|---|---|---|
| Animals do not show probability-graded anticipation | Cues insufficiently discriminable, weak motivation or too many conditions | Verify cue calibration and reward delivery; simplify the probability ladder in a redesigned pilot |
| SURE outcome response is absent | Pump, timing or recording failure | Check measured delivery, timestamps and signal; do not interpret waiting data |
| Omission response is absent | Failure to learn expected timing, insensitive assay or misaligned outcome window | Check behavior, timing and preprocessing; extend training only under a preregistered rule |
| Waiting signal predicts the future rewarded/unrewarded outcome on AON trials | Sensory leakage, software bug, systematic behavior or analysis contamination | Audit randomization, apparatus signals and trial labels; analyze behavior-matched subsets |
| Probability effect reverses when cue assignments are swapped | Physical-cue or learning-history artifact | Do not interpret as probability coding; redesign cue set |
| Effect disappears after adjustment for licking or movement | Behavioral-state confound or dopamine-behavior coupling | Analyze no-lick and matched trials; use a noncontingent task and consider later causal perturbation |
| AON and SURE differ but MAG does not | Presence uncertainty, utility nonlinearity or entropy explanation | Use utility sensitivity and entropy/variance contrasts before accepting a variance account |
| Effects weaken with prolonged training | Overtraining or changing subjective uncertainty | Begin confirmatory recording immediately after criterion and model session number |
| Results differ between recording methods | Firing and release may not be interchangeable | Treat methods as separate biological measurements; do not pool without testing method-by-condition interaction |

---

## 11. Conditional conclusions

### Positive outcome

A positive result requires all of the following:

1. Animals learn the cue contingencies;
2. Outcome-period controls reproduce the qualitative packet patterns;
3. The waiting-period uncertainty coefficient differs reliably from zero across animals;
4. The effect follows assigned probability rather than physical cue identity;
5. The matched-distribution module gives a coherent variance, entropy or presence-uncertainty ordering;
6. The effect survives utility sensitivity analysis and is not wholly explained by measured behavior;
7. It replicates in an independent cohort.

**Strongest justified conclusion:** dopamine activity during the waiting period contains information about outcome variability beyond scalar expected value in the recorded preparation. The exact result may support variance, entropy, presence uncertainty or inverse certainty coding, depending on the observed ordering.

This would still be **correlational**. It would not prove that dopamine causes risk-sensitive choice or learning.

### Negative outcome

A negative result requires valid learning and positive controls, adequate power and confidence intervals that exclude the prespecified meaningful effect.

**Strongest justified conclusion:** under this fixed-delay Pavlovian preparation, the measured dopamine signal does not detectably encode outcome uncertainty during waiting beyond expected value.

This would not rule out:

- Uncertainty coding in other dopamine populations or regions;
- Single-cell heterogeneity hidden by a population signal;
- Coding at a different delay time;
- Codes that appear only during active choice;
- Uncertainty representations below the achievable detection threshold.

### Ambiguous outcome

The result should remain ambiguous if:

- The probability ladder suggests uncertainty but matched distributions do not;
- Utility nonlinearities can explain the apparent risk effect;
- Behavior matching removes the neural difference;
- Cue remapping fails;
- Outcome positive controls fail;
- Confidence intervals include both zero and the minimum meaningful effect;
- The probability and replication cohorts disagree.

The appropriate conclusion is that waiting-period dopamine may contain a distribution-related correlate, but its identity and independence from value or behavior remain unresolved.

---

## 12. Recommended subsequent causal question

Only if the encoding result is positive should the next experiment ask:

**Does the uncertainty component of waiting-period dopamine causally alter risk-sensitive choice or learning?**

That experiment should use randomized, delay-restricted perturbation in a separate properly powered cohort, with stimulation or suppression outside the delay as temporal controls and unbiased choice or learning as the endpoint. A positive result would support a functional role; a null result would indicate that an uncertainty-correlated signal need not be causal. No such causal result is reported in the supplied packet.
