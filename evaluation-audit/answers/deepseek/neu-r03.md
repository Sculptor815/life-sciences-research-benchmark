# DeepSeek V4.1 Flash / neu-r03

Original final answer, shared by both scoring rounds.

## Recommended next action

Run a preregistered, fixed-timing probability/variance manipulation while recording dopamine-neuron activity, with a factorial design that varies reward probability and reward magnitude so that expected value (EV) and outcome variance can be partially orthogonalized. The primary question is:

**During the waiting period before an expected reward, does dopamine-neuron activity encode the variance/uncertainty of the upcoming outcome independently of expected value, elapsed time/hazard, and motor/salience covariates, or is waiting-period activity explained by outcome-time signed reward prediction error (RPE), expected value, timing, or behavioral confounds?**

All protocol elements below are **proposed**, not reported results. The packet does not report species, brain region, recording modality, neuron-identification method, reward identity, delay duration, trial counts, timing distribution, behavioral measurements, or analysis methods. Those are **unreported parameters** and must be fixed before the experiment is interpretable.

---

## 1. Evidence-to-inference-to-conclusion chain from the packet

**Evidence reported in the packet**
1. Dopamine-neuron responses to rewards diminish as rewards become predicted.
2. Unexpected timing produces activation.
3. Omission at an expected time produces a depression.

**Inference supported by the packet**
- Outcome-time dopamine activity is consistent with a signed reward prediction error: better-than-expected outcomes activate; worse-than-expected outcomes depress; predicted outcomes produce smaller responses.

**Limit explicitly stated in the packet**
- These observations do **not** establish whether activity during the waiting period carries additional information about variable outcomes.
- No later probability-manipulation experiment or result is included.

**Unresolved biological question**
- Does waiting-period dopamine activity represent only anticipation, elapsed time, or expected value, or does it also carry information about outcome variance/probability that is separable from outcome-time RPE?

**Conclusion from the packet alone**
- The packet supports an outcome-time RPE-like signal under prediction, timing, and omission manipulations, but it leaves open whether dopamine neurons transmit distributional information about upcoming outcomes during the waiting period. The most valuable next question is therefore whether waiting-period activity encodes outcome variance/uncertainty beyond EV and timing.

---

## 2. Competing mechanisms and discriminating predictions

| Mechanism | Waiting-period prediction | Outcome-time prediction | Key discriminating test |
|---|---|---|---|
| M1: RPE-only | Waiting activity flat or reflects only time/anticipation; no modulation by outcome variance after controls | Signed RPE: unexpected reward activates, expected reward small, omission at expected time depresses | Delay activity should not track variance when EV and timing are matched |
| M2: EV-only | Delay activity scales with expected reward value, not variance | RPE remains | Delay activity should follow EV, not variance, across matched-EV/different-variance conditions |
| M3: Variance/uncertainty | Delay activity scales with outcome variance or entropy, even at matched EV | RPE may remain separate | Delay activity should be higher when variance is higher at matched EV; should peak near p = 0.5 if variance drives it |
| M4: Timing/hazard | Delay activity ramps with elapsed time or hazard rate; probability effects are secondary to timing | RPE intact | Holding reward timing fixed while varying outcome probability/variance should abolish or reduce delay modulation if timing-driven |
| M5: Motor/salience/arousal | Delay activity correlates with licking, pupil, movement, cue salience | RPE may be confounded | Including behavioral covariates should remove variance/EV effects if motor/salience explains them |
| M6: Mixed population | Some neurons encode RPE, some EV, some variance | Heterogeneous | Population decoding and single-neuron clustering should reveal separable components |

Strongest early discriminator: compare M2 and M3 by matching EV while changing variance. If delay activity tracks variance at matched EV, M3 is favored. If it tracks EV only, M2 is favored. If it does neither after controlling timing and movement, M1 or M4 is favored.

---

## 3. Proposed research plan

### 3.1 Prerequisites

1. **Neuron identification.** Record from neurons identified as dopaminergic by the preparation’s validated criterion. The packet does not report how this was done; this must be specified before the experiment. If identification is unavailable, the conclusion must be limited to “putative dopamine neurons.”
2. **Stable recording.** Use a preparation allowing repeated trials and within-session block manipulations. Stability criteria must be preregistered.
3. **Precise reward delivery and omission control.** The system must log cue onset, reward delivery, omission, reward magnitude, and consumption with high temporal resolution.
4. **Fixed cue-reward delay for the primary test.** The packet shows unexpected timing produces activation, so timing must be held constant in the main variance test unless timing is explicitly modeled.
5. **Sufficient power.** The packet reports no effect sizes or trial counts. A pilot or prior estimate is required to set trial numbers. As a proposed assumption, plan at least several animals, multiple sessions per animal, and enough trials per condition for hierarchical modeling.
6. **Behavioral monitoring.** Record licking, movement, pupil/arousal if available, and reward consumption to test motor/salience confounds.
7. **Preregistration.** Define primary endpoints, exclusion criteria, model structure, and stop rules before data collection.

### 3.2 Experimental design

**Core idea:** manipulate outcome probability and reward magnitude so that EV and variance are not perfectly confounded.

For a binary outcome with reward magnitude \(m\) delivered with probability \(p\):
- \(EV = p \cdot m\)
- \(Var = p(1-p)m^2\)

If only \(p\) is varied with fixed \(m\), EV and variance are correlated but not identical. To dissociate them, vary both \(p\) and \(m\).

**Proposed conditions (example, to be calibrated to the preparation):**
1. \(p = 1.0, m = 0.5\): EV = 0.5, Var = 0
2. \(p = 0.5, m = 1.0\): EV = 0.5, Var = 0.25
3. \(p = 0.25, m = 2.0\): EV = 0.5, Var = 0.75
4. \(p = 0.0, m = 0\): EV = 0, Var = 0
5. Optional: \(p = 0.75, m = 1.0\): EV = 0.75, Var = 0.1875
6. Optional: \(p = 0.5, m = 0.5\): EV = 0.25, Var = 0.0625

Conditions 1–3 match EV while differing in variance. This is the strongest proposed test for M2 vs M3. If reward magnitude cannot be varied, the experiment can still manipulate probability, but EV and variance will be collinear; the conclusion will be weaker and limited to “probability-related modulation” rather than variance-specific coding.

**Trial structure (proposed):**
- Baseline/ITI
- Cue predicting the block’s outcome distribution
- Fixed delay
- Reward delivery or omission
- Post-outcome period
- ITI

**Control conditions:**
- Cue with no reward probability (\(p = 0\)).
- Uncued reward (US alone) to verify unexpected reward activation.
- Expected reward at \(p = 1\).
- Omission at expected time.
- Unexpected reward timing, used only as a calibration positive control.
- Decoy cue predicting nothing.
- Blocks with matched timing but different variance.

**Allocation and blinding:**
- Randomize block order within animal and counterbalance across animals.
- Automate reward delivery and omission so the experimenter does not manually decide outcomes.
- Code condition labels during preprocessing; analysis is blind to condition until primary preprocessing is complete.
- If histology or neuron identification is used, score it blind to condition.

**Independent units:**
- Animal is the top-level independent unit.
- Session is nested within animal.
- Neuron is nested within session/animal.
- Trials are repeated measures.
- Inference should use hierarchical/mixed models with animal as a random effect, not treat neurons or trials as independent.

### 3.3 Calibration and positive controls

Before testing the primary question, verify that the preparation reproduces the packet’s core phenomena:
1. **Prediction suppression:** reward response at \(p = 1\) should be smaller than uncued reward.
2. **Unexpected reward activation:** uncued or unexpectedly timed reward should activate.
3. **Omission depression:** omission at an expected time should produce a depression relative to expected reward.
4. **Timing precision:** cue and reward times must be stable within the fixed-delay condition.
5. **Behavioral calibration:** measure baseline licking and movement; verify that reward and omission produce detectable behavioral differences that can be used as covariates.

If these calibration criteria fail, the RPE assay is not working, and primary variance results would be uninterpretable.

### 3.4 Measurements

**Neural measurements:**
- Same modality as the packet, if specified; otherwise preregister one modality.
- Analyze firing rate or calcium signal in predefined windows:
  - baseline pre-cue
  - cue response
  - early delay
  - late delay
  - reward response
  - omission response
- For delay activity, measure mean activity, slope/ramp, and population decoding.

**Behavioral measurements:**
- Licking, movement, pupil/arousal if available, reward consumption.
- These are covariates to test M5.

**Timing measurements:**
- Cue onset, delay duration, reward delivery, omission confirmation, ITI.

### 3.5 Analysis

**Primary analysis:**
- Mixed-effects model for delay activity:
  \[
  DelayActivity \sim EV + Var + Time + Behavior + (1|Animal) + (1|Session) + (1|Neuron)
  \]
- Include orthogonalized EV and variance regressors when possible.
- Test whether the variance coefficient is nonzero after controlling EV, time, and behavior.

**Secondary analysis:**
- Outcome-time model:
  \[
  OutcomeResponse \sim RPE + Var + (1|Animal) + (1|Session) + (1|Neuron)
  \]
- RPE defined as outcome minus EV.
- Check whether reward activation and omission depression follow signed RPE.

**Population decoding:**
- Train a classifier/decoder on delay activity to predict condition (\(p\), EV, or variance).
- Cross-validate across trials and, ideally, across sessions/animals.
- Compare against shuffled-label controls.

**Model comparison:**
- Compare RPE-only, EV-only, variance, and timing/hazard models using preregistered criteria.
- Use FDR or hierarchical Bayesian posterior probabilities for multiple comparisons.

**Behavioral confound analysis:**
- Add licking, movement, and pupil as covariates.
- If variance effects disappear when these are included, M5 is favored.

### 3.6 Stop rules

**Calibration failure stop rule:**
- If the positive controls fail in more than a prespecified fraction of sessions (e.g., unexpected reward not greater than expected reward, or omission not depressing relative to expected reward), stop and troubleshoot before primary analysis.

**Data-quality stop rule:**
- Exclude sessions with unstable recording, reward-delivery errors above a prespecified threshold, or insufficient trials per condition.
- If too few stable neurons/sessions remain, stop and redesign.

**Futility stop rule:**
- After a prespecified interim fraction of planned animals, if the variance effect is estimated with high precision around zero and is below the minimal effect of interest, stop for futility.

**Success stop rule:**
- If the variance effect excludes zero and exceeds the minimal effect of interest after controlling EV, timing, and behavior, continue to the planned sample and then report.

### 3.7 Troubleshooting

- **No RPE signal:** verify reward delivery, neuron identification, recording stability, and timing logs. Without positive controls, do not interpret delay activity.
- **Motor/licking confound:** include behavior as covariate; if variance effect vanishes, reclassify as motor/salience. Consider adding a no-reward cue condition.
- **Timing confound:** if delay activity tracks hazard, hold delay fixed in the primary test and model timing separately.
- **Drift:** randomize block order within session; z-score neural activity per session; include session as random effect.
- **Sparse data:** increase trials per condition or animals; do not over-interpret single-neuron effects.
- **Saturation/clipping:** if using calcium imaging, check dynamic range; consider electrophysiology if available.

---

## 4. Positive, negative, and ambiguous outcomes

### Positive outcome
**Pattern:** Delay activity scales with outcome variance at matched EV, remains after controlling timing and behavior, and outcome-time RPE is intact.
**Interpretation:** Waiting-period dopamine activity carries additional information about variable outcomes, consistent with M3 or a mixed population containing variance-coding neurons.
**Strongest justified conclusion:** In this preparation and under these conditions, dopamine-neuron population activity during the waiting period encodes outcome variance/uncertainty beyond signed outcome-time RPE.

### Negative outcome
**Pattern:** Delay activity is not modulated by variance after controlling EV, timing, and behavior. Outcome-time RPE remains.
**Interpretation:** The RPE account is sufficient for this paradigm; waiting-period activity does not carry separable variance information.
**Strongest justified conclusion:** Under these conditions, dopamine-neuron waiting-period activity is explained by expected value, timing, or motor/salience covariates, not by outcome variance.

### Ambiguous outcome
**Pattern A:** Delay activity tracks probability but EV and variance are confounded because magnitude was not varied.
**Conclusion:** Cannot distinguish EV from variance. Need the factorial EV/variance design.

**Pattern B:** Delay activity tracks variance but only in a subset of neurons or sessions.
**Conclusion:** Possible mixed population; need preregistered population-level decoding and replication.

**Pattern C:** Variance effect is confounded with timing, licking, or arousal.
**Conclusion:** Cannot assign the effect to variance without stronger controls.

**Pattern D:** Positive controls fail.
**Conclusion:** Calibration failure; no biological conclusion about variance is justified.

---

## 5. Limits and what would change the recommendation

- The packet reports only outcome-time prediction effects. It does not report a probability manipulation, waiting-period analysis, neuron identity, species, or recording method. All proposed methods above are inferences from the question, not reported author methods.
- Correlation is not causation. Even a positive result would show that waiting-period activity carries variance information; it would not prove that dopamine neurons compute variance or use it causally.
- The strongest test requires reward-magnitude variation to dissociate EV from variance. If magnitude cannot be varied, a probability-only experiment can still ask whether waiting activity carries probability-related information, but it cannot cleanly separate expected value from uncertainty.
- If timing is not fixed, hazard/timing coding remains a strong alternative. Fixed-delay primary conditions are therefore recommended.
- The most valuable next question is not simply “does dopamine signal RPE at outcome?” The packet already supports that. The unresolved and higher-value question is whether waiting-period dopamine activity carries additional distributional information about variable outcomes.
