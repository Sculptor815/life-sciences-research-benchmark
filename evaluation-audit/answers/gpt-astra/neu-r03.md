# GPT-6 Astra / neu-r03

Original final answer, shared by both scoring rounds.

## 1. Recommended next question

**Test whether dopamine-neuron activity during the waiting period reflects uncertainty about whether a reward will occur, beyond responses to predicted value, reward delivery, omission, or timing errors.**

The highest-value next experiment is to manipulate reward probability while keeping reward timing fixed, record independently identified dopamine neurons throughout the delay, and include reward-magnitude controls that help separate uncertainty from expected reward.

### Evidence → inference → unresolved question

| Supplied evidence | Justified inference | What remains unresolved |
|---|---|---|
| Reward responses diminish as rewards become predicted. | Reward responses depend on prediction, not simply reward receipt. | Whether waiting-period activity contains information beyond these event responses. |
| Unexpected reward timing produces activation. | Timing expectations influence dopamine-neuron activity. | Whether apparent delay activity could arise from temporal expectation or timing errors. |
| Omission at an expected time produces depression. | Activity distinguishes an expected reward from its absence. | Whether uncertainty before that outcome is represented independently. |

**Reported conclusion:** the observations connect dopamine-neuron activity with violations of reward prediction.

**Proposed extension:** determine whether a stable, probabilistic reward contingency produces an additional waiting-period signal. The packet contains no probability-manipulation result, so neither such a signal nor its mechanism is established.

---

## 2. Competing mechanisms and discriminating predictions

Let a cue predict reward amount \(R\) at a fixed time \(T\), delivered with probability \(p\). For this proposed binary-outcome task:

\[
E[\text{reward}]=pR,\qquad
\operatorname{Var}(\text{reward})=p(1-p)R^2.
\]

These are task definitions, not claims about the neurons’ computations. The animal’s learned probability and subjective reward value may differ from scheduled probability and physical amount.

| Mechanism | Distinct predictions | Important qualification |
|---|---|---|
| **Persistent outcome-uncertainty signal** | At fixed amount, waiting activity has an interior maximum near intermediate probabilities rather than increasing monotonically with \(p\). It persists after learning stabilizes. | A maximum at exactly \(p=0.5\) requires appropriate learning and a particular uncertainty measure. |
| **Expected-value or anticipation signal** | At fixed amount, activity generally increases with probability. Conditions matched for subjective expected value should have similar waiting activity. | Matching \(pR\) matches objective, not necessarily subjective, expected value. |
| **Event-transient-only prediction-error account** | Probability affects cue, reward, and omission transients, but no independent delay component remains after excluding those events and avoiding temporal smoothing artifacts. | More general prediction-error models with uncertain internal states can generate delay activity; this experiment cannot reject every such model. |
| **Temporal expectation/internal timing uncertainty** | Modulation concentrates near the expected outcome time and shifts or stretches when the trained delay changes. A probability effect may weaken after accounting for timing-related activity. | Uncertainty and timing signals can coexist. A ramp is not uniquely diagnostic. |
| **Uncertainty about learning the contingency, rather than irreducible outcome uncertainty** | Delay modulation declines with additional stable training or tracks recent contingency changes. | Both types of uncertainty may be present early in learning. |
| **Movement, arousal, attention, or sensory confounding** | Apparent uncertainty effects track measured behavior, cue identity, recording artifacts, or reward-delivery precursors. | A genuine uncertainty-dependent attention signal could remain; behavioral adjustment alone cannot identify the underlying computation. |

### Distinguishing kinds of uncertainty

Two candidate uncertainty variables are:

- **Reward variance:** \(p(1-p)R^2\).
- **Binary outcome entropy:** \(-p\log p-(1-p)\log(1-p)\), which does not depend on reward amount.

Both peak at intermediate probability, but they predict different magnitude dependence **if neural encoding is proportional to the proposed variable**. Failure of proportional scaling would not, by itself, disprove uncertainty coding.

The primary hypothesis below concerns increased activity with uncertainty. A consistently signed decrease or heterogeneous neuronal coding would be a separately assessed outcome, not grounds to declare that all uncertainty information is absent.

---

## 3. Proposed research plan

**Everything in this section is proposed, not reported.** The packet does not specify species, preparation, recording technology, cell-identification method, reward type, timings, sample size, or analysis methods.

### Step 1 — Establish prerequisites and lock the protocol

Before definitive data collection, document:

1. A preparation permitting repeatable reward learning and stable single-neuron recording during a sufficiently long waiting interval.
2. An independently validated means of identifying dopamine neurons. **Do not define dopamine neurons by the reward-response pattern being tested.**
3. A reward that can be delivered accurately at two tolerable amounts, \(R\) and \(2R\).
4. Observable measures of anticipation, movement, and reward consumption.
5. Ethical approval, welfare limits, and predefined session-termination criteria.

Use a separate feasibility pilot to determine, then freeze:

- Reward amounts, cue duration, primary delay \(T\), baseline duration, post-outcome observation interval, and intertrial-interval distribution.
- Recording and dopamine-identity acceptance criteria.
- Delivery timing and amount tolerances.
- Learning/stability criteria and maximum training duration.
- Cue- and outcome-exclusion buffers for the waiting-period analysis.
- Minimum useful effect \(\Delta\), expressed in interpretable firing-rate units.
- Animal number, session requirements, and maximum acquisition limits.

**Unreported parameters:** their numerical values cannot be supplied from this packet. The definitive protocol is not ready to launch until these are filled in. Pilot observations used to choose the design should not be counted as confirmatory evidence.

### Step 2 — Calibrate delivery, event timing, and recording

Perform and archive the following checks before training and periodically thereafter:

- Measure actual reward amounts across repeated deliveries at both settings.
- Measure command-to-delivery latency and its variability.
- Verify synchronization among neural recording, cue onset, delivery detection, and behavioral measurements.
- Check whether delivery hardware generates sound, vibration, light, or other cues **before** reward arrival.
- Verify that future rewarded and omitted trials have identical hardware states throughout the waiting interval.
- Test spike-detection reliability, recording stability, and event-related electrical artifacts.

Use actual detected delivery time when analyzing rewarded outcomes. On omission trials, use the programmed expected time \(T\).

**Calibration gate:** pause acquisition if delivery amount, latency, synchronization, or precursor-cue performance falls outside frozen tolerances. Retain records of failed checks and affected trials.

### Step 3 — Train a fixed-time probabilistic task

#### Primary condition set

Use probabilities:

\[
p\in\{0,\ 0.25,\ 0.5,\ 0.75,\ 1\}.
\]

For each nonzero probability, use amounts \(R\) and \(2R\). Include one zero-reward condition; reward amount is undefined when reward never occurs. This gives **nine conditions**.

Each condition receives a distinct, discriminable cue. Match presentation frequency across conditions.

#### Proposed trial sequence

1. A neutral pre-cue baseline.
2. A brief cue identifying the condition.
3. A blank waiting interval.
4. Reward at fixed time \(T\), or omission without an additional omission signal.
5. An identical-duration post-outcome observation period.
6. An intertrial interval sampled independently of condition and outcome.

Reward should not require an action in the primary task. This reduces, but does not eliminate, movement-related interpretations.

Keep trial duration the same after reward and omission. Ensure that the post-outcome interval accommodates the larger reward without truncating consumption measurements.

#### Randomization

- Randomize cue order with approximately balanced condition counts.
- Generate outcomes independently with the specified probability; do not enforce short alternating or fixed win–loss patterns.
- Log the randomization seed and scheduled outcome.
- Counterbalance cue-to-condition mappings across animals.
- Avoid making reward probability predictable from recent outcomes beyond the designated cue.

The actual number of rewards will fluctuate around the programmed expectation. Report both programmed and realized probabilities.

### Step 4 — Demonstrate learning without using the neural hypothesis as a criterion

Use preregistered behavioral measures to assess whether cues produce differentiated expectations and whether behavior has stabilized across successive training blocks.

For example, measure anticipatory responses and their timing, using a response appropriate to the selected preparation. Specify the exact measure before definitive recording.

Important safeguards:

- Do not use an observed neural uncertainty effect to decide that learning is complete.
- Do not assume behavior provides an exact probability estimate.
- If fitting behavioral estimates of subjective probability, estimate them without the neural outcome and propagate their uncertainty.
- Track behavior across additional stable training to distinguish persistent outcome uncertainty from ongoing contingency acquisition.

For expected-value comparisons, add a separate, predefined behavioral valuation procedure if the preparation supports it. This can constrain subjective values of \(R\) and \(2R\), but should not be treated as perfect measurement.

**Learning gate:** if an animal does not meet frozen behavioral criteria within the training limit, report this and do not treat its neural null result as a clean test of learned uncertainty.

### Step 5 — Define independent units and acquisition targets

**The primary independent biological unit is the animal.** Trials, neurons, and sessions within an animal are repeated or nested observations.

- Enroll animals according to a prospective sampling plan.
- Counterbalance cue mappings across animals; balance other known enrollment factors where feasible.
- Record all neurons meeting independent identity and quality criteria, not only reward-responsive neurons.
- If the same neuron is followed across sessions, retain its identity as a repeated unit.
- If cross-session identity is uncertain, do not count recordings as demonstrably independent neurons.

Determine animal number using pilot estimates of between-animal variation, within-animal correlation, and anticipated recording yield. Simulate the planned clustered analysis for the minimum useful effect \(\Delta\).

Set minimum information requirements per animal, including coverage of all conditions and adequate reward/omission observations. These must depend on counts and quality, not the direction of neural effects.

**No defensible numerical sample size follows from the packet alone.** More trials in one animal cannot substitute for biological replication.

### Step 6 — Allocation concealment and blinding

- Automate condition presentation and outcome assignment.
- Keep routine recording staff unaware of hypotheses attached to particular cue identities where practical.
- Have spike sorting, cell-identity adjudication, and quality-control decisions performed with condition labels masked.
- Freeze trial and neuron inclusion before revealing probability labels for confirmatory analysis.
- Record every manual exclusion, its reason, and who made it.
- Separate exploratory findings from locked confirmatory tests.

Full operator blinding may be impossible because rewards are observable. Automated delivery and label-blinded neural processing remain valuable safeguards.

### Step 7 — Record synchronized measurements

Retain trial-level records of:

- Raw neural signals and spike times.
- Dopamine-cell identification evidence.
- Cue identity and actual onset/offset.
- Programmed probability and amount.
- Scheduled outcome and expected outcome time.
- Actual reward arrival and delivered amount where measurable.
- Anticipatory and consummatory behavior.
- Movement and any available arousal proxy.
- Trial number, recent reward history, session time, and quality flags.

Arousal measures are proxies, not comprehensive measurements of attention.

**Useful negative control:** within a given probabilistic cue condition, waiting activity should not systematically predict the independently randomized future reward assignment. Replicable prediction would trigger investigation of delivery precursors, scheduling dependencies, timestamp leakage, or other violations—not an immediate biological interpretation.

### Step 8 — Prespecify neural epochs and prevent event contamination

Define separate epochs:

1. Pre-cue baseline.
2. Cue response.
3. Waiting interval.
4. Expected outcome response.
5. Later consumption/post-outcome period.

Set the waiting interval using the independent pilot: begin after the cue transient and end before the outcome buffer. Use the same boundaries across primary conditions.

Primary measurements:

- Waiting-period spike count divided by its duration.
- Baseline firing, retained as a measurement rather than silently subtracted without inspection.
- Waiting activity in three prespecified subintervals.
- Cue, reward, and omission response magnitudes in separate windows.
- Trial-to-trial behavioral and firing variability.

For the main waiting analysis, use unsmoothed spike counts. Display smoothing must not move outcome spikes backward into the delay; state kernel type and support.

A mean delay effect does not automatically establish sustained single-neuron firing. Report whether modulation spans multiple waiting subintervals, occurs only near an edge, or arises from differently timed brief responses across neurons.

### Step 9 — Include discriminating controls

#### A. Probability endpoints

Compare intermediate probabilities with both:

- \(p=0\): no outcome uncertainty and no reward.
- \(p=1\): no outcome uncertainty but substantial expected reward.

An interior maximum is more informative than a difference between uncertain reward and no reward alone.

#### B. Expected-reward matching

The proposed condition set includes:

- \(p=0.5,\ 2R\) versus \(p=1,\ R\): same objective expected reward, different uncertainty.
- \(p=0.25,\ 2R\) versus \(p=0.5,\ R\): same objective expected reward, different variance and entropy.

Interpret these with the behavioral valuation calibration. Without credible subjective-value matching, residual value explanations remain.

#### C. Timing generalization

After primary learning, test a preregistered subset—\(p=0,\ 0.5,\ 1\) at amount \(R\)—at two trained fixed delays.

Counterbalance delay order and complete behavioral stabilization at each delay. Do not introduce an unsignaled delay change during the confirmatory waiting-period comparison.

Analyze activity in both cue-aligned and expected-outcome-aligned time. Ask whether the probability effect remains away from event boundaries or is confined to a narrow outcome-anticipatory period.

Because changing delay can also change subjective value, this is a temporal-discrimination control, not a perfectly isolated manipulation of timing.

#### D. Event-response sensitivity control

In separate sessions after the primary experiment, introduce prespecified unexpected timing changes and unexpected omissions of a previously reliable reward.

These proposed probes assess whether the preparation detects the kinds of responses described in the packet. Keep them separate from primary acquisition because repeated probes would change timing and probability expectations.

#### E. Behavioral and training controls

Examine:

- Comparable low-movement periods with overlap across conditions.
- Early versus late stable-training blocks.
- Cue-mapping dependence.
- Recent reward history and within-session drift.

Do not claim that statistically adjusting for behavior proves a direct neural uncertainty computation. Behavior may itself be downstream of uncertainty.

### Step 10 — Perform the locked analysis

#### Primary test: interior waiting-period enhancement

At amount \(R\), estimate animal-level marginal waiting rates and the contrasts:

\[
C_1=r_{0.5}-r_0,\qquad
C_2=r_{0.5}-r_1.
\]

Require both contrasts to support an interior enhancement, with simultaneous confidence intervals and the prespecified meaningful-effect criterion. Then examine the complete five-probability curve: a single elevated intermediate point is weaker evidence than a reproducible probability-dependent profile.

Analyze the \(2R\) series as a prespecified extension, with multiplicity handled across confirmatory claims.

#### Hierarchical estimation

Use a count model appropriate to observed dispersion, with waiting duration as exposure, and account for:

- Animal.
- Session.
- Neuron within animal, including repeated recordings where identifiable.
- Baseline activity.
- Prespecified history and session-drift terms.

Treat probability initially as categorical so that the principal result does not depend on assuming a quadratic shape.

Check model fit. Provide an animal-level summary analysis or cluster-respecting sensitivity analysis so a large neuronal yield from one animal cannot dominate the conclusion.

#### Mechanistic model comparison

Compare predefined candidate models containing:

1. Expected value alone.
2. Outcome uncertainty alone.
3. Expected value plus uncertainty.
4. Event-locked transient and temporal-expectation components.
5. Those components plus an independent waiting-period uncertainty term.

Compare reward variance and entropy separately. Avoid interpreting unstable coefficients from highly correlated predictors.

Assess predictive improvement on held-out animals, not merely held-out trials from the same recording. If the animal sample is too small for credible held-out comparison, label model ranking exploratory.

#### Secondary coding analyses

Predefine analyses for:

- Negative uncertainty coefficients.
- Heterogeneous neuronal subpopulations.
- Cross-validated information about uncertainty beyond expected value.

An average near zero can conceal opposing neuronal effects. Conversely, selecting “uncertainty neurons” and testing them on the same trials produces circular evidence; use independent data splits.

#### Temporal and behavioral sensitivity

Repeat the analysis with wider event-exclusion buffers and on behaviorally comparable subsets. Report both unadjusted task effects and behavior-adjusted associations.

A conclusion should not depend exclusively on one smoothing choice, one buffer, or exclusion of most trials from a particular condition.

### Step 11 — Stop rules and troubleshooting

| Trigger | Required action | Consequence for inference |
|---|---|---|
| Welfare threshold reached | End session or participation according to approved rules. | Report attrition; never extend acquisition to obtain a desired result. |
| Delivery or synchronization fails calibration | Pause, repair, recalibrate; flag affected data. | Timing or uncertainty claims from affected trials are unreliable. |
| Learning criteria fail by training limit | Stop definitive testing or enter a separately labeled retraining phase. | A neural null is not evidence against learned uncertainty coding. |
| Dopamine identity or recording stability fails | Exclude by blinded, predefined criteria. | Restrict conclusions to valid identified recordings. |
| Future outcome is predictably signaled during waiting | Investigate hardware and schedule; repeat after correction. | Cannot interpret the contaminated delay as uncertainty-only. |
| High probability is confounded with movement without common support | Improve measurement or redesign a new experiment. | Regression alone cannot resolve the confound. |
| Delay effect disappears with larger event buffers | Report edge dependence and test event-transient accounts. | Do not call it a sustained waiting signal. |
| Feasibility is inadequate at a predefined review | Stop or amend transparently before confirmatory continuation. | Treat amended work as a revised study. |

Do not stop early because a significance threshold is crossed. If sequential monitoring is desired, specify its statistical rule in advance.

---

## 4. Conditional outcomes and strongest justified conclusions

### Positive, well-discriminated outcome

**Hypothetical observations:** intermediate probabilities produce reproducible waiting-period enhancement after learning; the effect survives event buffers, appears across animals and cue mappings, differs between appropriate value-matched conditions, and improves held-out prediction beyond value and event-transient models.

**Strongest justified conclusion:** dopamine-neuron activity contains waiting-period information associated with reward-outcome uncertainty in this task, beyond the specific value and transient explanations tested.

Further distinctions would depend on magnitude scaling and timing generalization. This would **not** prove that these neurons calculate uncertainty, that uncertainty is their exclusive signal, or that the activity causes learning. Those require additional experiments.

### Negative outcome with adequate sensitivity

**Hypothetical observations:** learned expectations and event responses are demonstrable, but waiting-period uncertainty effects have confidence bounds smaller than \(\Delta\); secondary analyses also find no reliable alternative coding.

**Strongest justified conclusion:** the study places a quantitative upper bound on uncertainty-related waiting activity in the recorded population, task, and temporal resolution.

It would not show that dopamine never represents uncertainty. A null population mean alone is insufficient to exclude heterogeneous coding.

### Ambiguous outcomes

- **Probability hump only near outcome time:** compatible with uncertainty-dependent anticipation, timing effects, or contaminated event responses; not a clear sustained signal.
- **Effect disappears as training stabilizes:** favors contingency-learning uncertainty over persistent outcome uncertainty.
- **Monotonic probability dependence:** favors value or anticipation under this design, although mixed coding remains possible.
- **Objective-value-matched conditions differ, but subjective values are unresolved:** uncertainty remains plausible, not isolated.
- **Effect tracks movement:** may reflect motor confounding or a genuine uncertainty-to-behavior pathway; the recording alone cannot distinguish them.
- **Only a post hoc neuronal subset shows an effect:** exploratory until independently validated.
- **Poor learning, failed identity, or imprecise estimates:** inconclusive, not evidence of absence.

---

## 5. Audit trail and final inference boundary

Archive the preregistration, pilot/design separation, cue mappings, randomization seeds, calibration logs, all exclusions, animal/session/neuron identifiers, raw timestamps, preprocessing versions, and analysis code. Report the flow from enrolled animals to analyzed recordings and display animal-level effects.

**Bottom line:** the packet supports a prediction-violation interpretation of event responses but leaves waiting-period information unresolved. A probability-by-magnitude experiment with fixed outcome timing is the most direct next step. Its strongest attainable result is evidence for an additional uncertainty-associated neural signal—not, by itself, proof of an uncertainty-computing mechanism or a causal role in learning.
