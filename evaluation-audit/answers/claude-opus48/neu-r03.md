# Claude Opus 4.8 / neu-r03

Original final answer, shared by both scoring rounds.

# Next Biological Question and Research Plan for Dopamine Reward-Prediction Signaling

## Lead Conclusion / Recommended Next Action

**The most valuable next biological question is:** *During the delay between a predictive cue and an uncertain reward, does tonic/sustained dopamine-neuron activity encode the statistical uncertainty of the upcoming outcome (e.g., reward variance or entropy), as distinct from, and in addition to, the phasic signals that encode prediction errors at cue and outcome?*

This question is directly licensed by the packet's explicit open gap: the supplied evidence establishes that phasic dopamine responses track **violations of reward prediction** (diminished responses to predicted reward, activation for unexpected timing, depression for omission at expected time), but **"do not establish whether activity during the waiting period carries additional information about variable outcomes."** The recommended next step is a controlled electrophysiological experiment that manipulates outcome *predictability/uncertainty* while holding expected value and timing fixed, and that reads out **sustained inter-cue-outcome firing** separately from the phasic cue and outcome transients.

I am explicitly flagging that the packet contains **no probability-manipulation experiment or result**. Everything below describing uncertainty manipulations and sustained-activity readouts is a **proposed design**, not a reported finding.

---

## Evidence → Inference → Conclusion Chain (from the packet only)

**Evidence (supplied, reported):**
1. Dopamine-neuron responses to rewards diminish as rewards become predicted.
2. Unexpected timing of reward produces activation.
3. Omission of reward at an expected time produces a depression (below-baseline dip).
4. These findings link neural activity to reward-prediction violations.

**Inference (licensed):**
- Items 1–3 are jointly consistent with a **phasic prediction-error** account: the signal reports the difference between received and expected reward (positive error → activation; fully predicted → no response; negative error/omission → depression). Timing sensitivity (item 2) implies the prediction is temporally specific.

**Conclusion / gap (stated in packet):**
- The reported data concern **event-locked (phasic) responses to prediction violations**. They are silent on whether the **waiting period** (cue-to-outcome delay) carries information about **variable outcomes** (i.e., about the distribution, not just the point expectation). This is the unresolved biological question.

**Why this gap is the highest-value target:** Prediction-error coding (established) explains how expectations are *updated*; it does not reveal whether the same neurons also *represent the uncertainty* of what is expected. Uncertainty representation is a logically separate computation with distinct downstream consequences (exploration, learning-rate control, risk sensitivity). Resolving it determines whether dopamine is a pure error channel or a richer carrier of distributional information. The packet itself nominates "activity during the waiting period" and "variable outcomes" as the unexamined axes, so this is the minimal, directly-motivated extension.

---

## Competing Mechanisms and Discriminating Predictions

I frame three mechanistic hypotheses. All are consistent with the reported phasic findings; they differ in what the **sustained delay-period activity** should do as outcome uncertainty varies at fixed expected value and timing.

### Mechanism A — Pure phasic prediction-error channel (null for sustained uncertainty coding)
Dopamine neurons encode only event-locked reward-prediction errors. Delay-period firing returns to baseline after the cue transient and carries no systematic dependence on outcome variance.
- **Prediction A:** Mean sustained firing during the delay is flat across uncertainty conditions (no monotonic relation to variance/entropy). Cue-evoked phasic response scales with cue value but not with cue-signaled uncertainty per se. Outcome-evoked response scales with prediction-error magnitude (larger for surprising outcomes), which will trivially be larger under higher uncertainty — but this is an *outcome-locked* effect, not a *delay-period* effect.

### Mechanism B — Sustained uncertainty (variance/entropy) coding during the delay
A component of dopamine activity ramps or sustains during the delay in proportion to the uncertainty of the predicted outcome, peaking for maximally uncertain predictions (e.g., p≈0.5 for binary reward) and minimal for certain predictions (p≈0 or p≈1).
- **Prediction B:** Mean sustained delay firing is an **inverted-U** function of reward probability (maximal at p=0.5), i.e., monotonic in variance/entropy, while expected value is held constant or dissociated. This sustained signal is largest just before the expected outcome time and is dissociable from the phasic cue response.

### Mechanism C — Value/anticipation ramp (expected-value, not uncertainty)
Delay-period activity reflects a growing expectation of imminent reward (temporal-discounting-driven value ramp) that scales with **expected value**, not with variance.
- **Prediction C:** Sustained delay firing increases monotonically with expected reward magnitude/probability (largest at p=1), i.e., a value ramp, with **no inverted-U** and no special status for p=0.5.

### Discriminating table (sustained delay-period firing as a function of cue-signaled reward probability, expected value controlled)

| Reward probability | Mechanism A (error only) | Mechanism B (uncertainty) | Mechanism C (value ramp) |
|---|---|---|---|
| p = 0 (certain no-reward) | baseline | low | low |
| p = 0.25 | baseline | intermediate | low–intermediate |
| p = 0.5 | baseline | **maximal (peak)** | intermediate |
| p = 0.75 | baseline | intermediate | intermediate–high |
| p = 1 (certain reward) | baseline | low | **maximal** |

The three hypotheses make **qualitatively distinct shapes** (flat vs. inverted-U vs. monotonic increasing), which is the core identifiability of the design. A fourth composite outcome (value ramp *plus* an inverted-U uncertainty component) is possible and is handled analytically below.

---

## Proposed Research Plan (Detailed, Ordered, Auditable)

> **Status label:** This is a *proposed* protocol. No results here are observed. Any methods attributed to prior work are only the four reported phasic phenomena in the packet; all manipulations below (probability conditions, sustained-activity analysis) are new proposals, not author methods.

### 0. Overarching design logic
Manipulate the **uncertainty** of a predicted reward via cue-signaled probability while (i) holding **expected timing** fixed and (ii) dissociating **expected value** from **variance** across blocks, then read out **cue-locked phasic**, **delay-period sustained**, and **outcome-locked phasic** dopamine activity separately. The design is built so that the three hypotheses' predictions about the *delay-period* component cannot be mimicked by each other.

### 1. Prerequisites and assumptions (explicit)
- **Model system (assumption):** A behaving animal trained on Pavlovian/operant cue-reward associations with single-unit or fiber-based dopamine readout. I do not assume a specific species; the packet does not specify one. The design is species-agnostic but requires reliable isolation of dopaminergic signals.
- **Dopamine identification (prerequisite):** Independent identification of recorded units/signal as dopaminergic (e.g., optogenetic tagging in a dopamine-promoter line, or well-validated electrophysiological criteria combined with pharmacological verification). This is a prerequisite I am proposing; the packet does not supply an identification method.
- **Stable baseline behavior (prerequisite):** Animals must show asymptotic, stable anticipatory behavior (e.g., conditioned licking/approach) before recording, so that learning-related prediction-error dynamics (which the packet shows change with learning) are not confounded with uncertainty coding. We study the **asymptotic** regime where predictions are stable.
- **Fixed delay (assumption):** A single, fixed cue-to-outcome interval long enough to resolve sustained activity (proposed 2–3 s) and long enough to separate cue and outcome transients.
- **Caloric/volume controls (prerequisite):** Reward identity and physical delivery held constant; only probability of delivery varies.

### 2. Independent experimental units and sample size
- **Independent unit = animal** for behavioral and population-level inference; **secondary unit = identified neuron** for within-animal response-shape analysis, with animal as a random effect to avoid pseudoreplication.
- **Proposed n (assumption, to be justified by pilot power analysis):** ≥6 animals; within each, as many optogenetically tagged dopamine units as can be isolated (target ≥20 tagged units/animal across sessions). Final n set by a pilot-based power calculation (see §9 stop rules). State clearly: these numbers are proposed, not derived from supplied data.

### 3. Stimulus/condition set (the core manipulation)
Two interleaved sub-designs run in separate blocks:

**Sub-design 1 — Probability sweep at matched expected timing (primary inverted-U test).**
Five distinct cues map to reward probabilities p ∈ {0, 0.25, 0.5, 0.75, 1.0}, reward magnitude fixed at a constant M. Outcome time fixed. This sweep makes expected value (p·M) covary with probability but lets variance (p(1−p)M²) peak at p=0.5. This alone cannot separate B from C, hence Sub-design 2.

**Sub-design 2 — Value/variance dissociation (critical discriminator).**
Add cues that **hold expected value constant while varying variance**, and others that **hold variance constant while varying expected value**:
- Iso-EV set: combinations of (p, magnitude) chosen so expected value is equal across ≥3 cues but variance differs (e.g., certain small reward vs. risky larger reward with the same mean). 
- Iso-variance set: cues with similar variance but different means.

Mechanism C predicts delay firing tracks EV regardless of variance; Mechanism B predicts delay firing tracks variance at matched EV. This crossed design is the linchpin for identifiability.

**Timing-probe trials (embedded control, ties to reported phenomena).**
On a minority (~10%) of p=1 and p=0.5 trials, deliver reward at an **unexpected early/late time**, and on a minority of expected-reward trials **omit** reward. These reproduce the packet's established phenomena (unexpected-timing activation; omission depression) and serve as **internal positive controls** verifying that the recording captures known phasic signatures.

### 4. Trial structure and randomization
- **Trial:** inter-trial interval (jittered, mean ~several s) → cue onset (fixed duration) → fixed delay → outcome (reward or nothing per p) → ITI.
- **Randomization/allocation:** Cue-to-probability assignment counterbalanced across animals to prevent sensory confounds (which physical cue maps to which probability is permuted). Trial order pseudorandomized within session with no more than 3 identical-cue repeats to prevent sequential prediction.
- **Blinding:** Analysts blinded to cue-probability identity during spike sorting and sustained-window extraction (condition labels replaced with codes; unblinded only at the group-analysis stage). Stimulus delivery automated; experimenter not in the loop during trials.

### 5. Calibration and controls (pre-recording and within-session)
**Pre-recording calibration:**
1. **Behavioral calibration of learned predictions:** Confirm anticipatory responses are graded by probability (e.g., anticipatory licking monotonic in p) before neural recording, establishing that animals have learned the cue-probability map. If behavior does not discriminate cues, the uncertainty manipulation is not internalized → do not proceed (stop rule, §9).
2. **Dopamine-signal calibration:** Optogenetic-tag latency/waveform criteria fixed and documented before analysis. For fiber photometry (if used instead of/with units), calibrate sensor to known pharmacological dopamine challenges and isoperturbation controls (isosbestic channel for motion artifact).
3. **Reward-delivery calibration:** Verify reward volume/latency identical across conditions with a flow meter; any mechanical cue that leaks probability information (pump sound) masked or randomized.

**Within-session controls:**
- **Isosbestic/motion control** (photometry) recorded continuously.
- **Timing-probe and omission trials** (above) as positive controls for phasic PE signatures.
- **No-cue "free-reward" trials** sparse, to confirm unpredicted reward still elicits phasic activation (reproducing packet item on unexpected reward).
- **Non-reward-predictive neutral cue** to estimate sensory-evoked phasic response independent of value.

### 6. Measurements and analysis windows (pre-registered)
Define three non-overlapping windows per trial, fixed before unblinding:
- **W_cue:** 0–300 ms after cue onset (phasic cue response).
- **W_delay:** a sustained window spanning the middle of the delay through ~200 ms before expected outcome (the *waiting-period* signal the packet flags as unexamined). To separate a *ramp* (Mechanism C) from a *sustained plateau* (Mechanism B), further subdivide W_delay into early/mid/late thirds.
- **W_outcome:** 0–600 ms after outcome time (phasic outcome response / omission dip).

**Primary dependent variable:** mean firing rate (or ΔF/F) in W_delay, baseline-subtracted (ITI baseline).

**Primary analyses:**
1. **Shape test (A vs B vs C):** Fit W_delay activity as a function of probability with competing regressors: (i) constant (A), (ii) variance/entropy term p(1−p) (B), (iii) linear EV term (C), plus their combination. Compare models by cross-validated likelihood / information criterion with animal as random effect. The *qualitative* signature—flat vs inverted-U vs monotonic—is read directly, with model comparison quantifying it.
2. **Dissociation test:** Within the iso-EV set, test whether W_delay activity still varies with variance (supports B); within the iso-variance set, test whether it varies with EV (supports C). This is the decisive contrast because it breaks the EV-variance correlation present in Sub-design 1.
3. **Ramp vs plateau:** Compare early/mid/late W_delay thirds; a monotonic rise toward outcome favors value-ramp (C); a symmetric sustained elevation across the delay favors uncertainty coding (B). (Proposed heuristic, not a hard rule.)
4. **Positive-control validation:** Confirm (a) diminished phasic outcome response for predicted (p=1) vs unpredicted reward, (b) activation for unexpectedly-timed reward, (c) depression for omission. These must replicate the packet's reported phenomena; if they do not, the preparation is suspect (ambiguous-result handling, §10).
5. **Separation of phasic outcome PE from delay signal:** Because higher-uncertainty cues produce larger outcome prediction errors by construction, verify that any W_delay effect is not a spillover of the outcome transient (window separation plus trial-shuffled control where outcome-locked activity is regressed out before analyzing W_delay).

**Statistics:** Mixed-effects models (neuron nested in animal); pre-registered primary contrasts; multiple-comparison control across windows; effect sizes with confidence intervals reported alongside p-values. All analysis code and window definitions registered before unblinding.

### 7. Allocation/blinding summary
- Cue-probability mapping counterbalanced and coded.
- Analyst blind to condition identity through spike sorting and window extraction.
- Automated stimulus/reward delivery; isosbestic motion control; counterbalanced cue physical features.

### 8. Troubleshooting (anticipated failure modes → fixes)
- **Behavior doesn't discriminate probabilities:** extend training; verify cue discriminability; increase magnitude contrast. If still absent, animals lack the internal predictions needed—report as inconclusive for the biological question, not as evidence against B.
- **Cue and outcome transients bleed into W_delay:** shorten W_cue/W_outcome, lengthen delay, apply regression-based removal of event-locked kernels.
- **Motion/licking artifacts correlate with probability (more anticipatory licking at high p):** include lick rate as a nuisance covariate; use iso-EV set where anticipatory behavior is matched; photometry isosbestic regression.
- **Few tagged units:** pool across sessions within animal; supplement with photometry population signal; treat unit-level results as secondary to population/animal-level inference.
- **Sequential/history effects:** enforce repeat limits; include previous-trial outcome as covariate.
- **Expected-value confound in Sub-design 1:** rely on Sub-design 2 dissociation as the decisive test; treat Sub-design 1 alone as insufficient.
- **Tonic drift in baseline:** frequent interleaved baseline estimation; normalize per-block.

### 9. Stop rules
- **Go/no-go gate:** If pre-recording behavioral calibration fails (no probability discrimination) after a pre-set training ceiling, stop and remediate before any neural recording.
- **Positive-control gate:** If the three reported phasic signatures (diminution with prediction, unexpected-timing activation, omission depression) are **not** reproduced in a session, exclude that session from primary analysis (preparation not validated).
- **Sample-size stop:** Pre-registered sequential analysis with a planned maximum n; stop when the pre-specified precision (CI width on the variance-term coefficient) is reached or the max n is hit, whichever first. No peeking-driven early stop outside the registered plan.
- **Safety/welfare stops** per institutional protocol (not detailed here).

### 10. Outcome interpretation (conditional conclusions)

**Positive for Mechanism B (uncertainty coding):**
If W_delay activity shows a reproducible **inverted-U in probability (peak at p=0.5)** *and* survives the iso-EV dissociation (varies with variance at matched expected value) *and* is not an artifact of outcome-transient spillover *and* phasic positive controls replicate — then the strongest justified conclusion is: **dopamine-neuron waiting-period activity carries additional information about variable outcomes, specifically encoding outcome uncertainty (variance/entropy), beyond the phasic prediction-error signal.** This directly answers the packet's open question in the affirmative. Scope limit: established at asymptotic learning, fixed timing, for the tested reward type and species; generalization requires further study.

**Negative (supports Mechanism A):**
If W_delay activity is **flat across conditions** (no variance or EV dependence) while phasic controls replicate, the justified conclusion is: **within this design's sensitivity, waiting-period dopamine activity does not carry additional information about outcome variability; the signal is consistent with a phasic prediction-error channel.** State the detectable effect size floor (power) so "no effect" is bounded, not absolute.

**Mechanism C outcome (value ramp, not uncertainty):**
If W_delay activity increases **monotonically with expected value** (peak at p=1), tracks EV in the iso-variance set, and shows no variance dependence in the iso-EV set, conclude: **waiting-period activity reflects anticipatory expected-value ramping, not uncertainty.** This still answers the packet's question partially ("waiting-period activity does carry outcome-related information, but of value not uncertainty").

**Composite outcome (B + C):**
If both a variance term and an EV term are needed (e.g., an inverted-U superimposed on a rising ramp), conclude that **waiting-period activity multiplexes expected value and uncertainty**; report the partitioned variance each term explains. The iso-EV / iso-variance dissociation is what licenses this decomposition.

**Ambiguous outcomes and handling:**
- *Positive controls fail:* results on the delay window are uninterpretable for the biological question; treat as a preparation/identification failure, not evidence about B/A/C.
- *Effect present but confounded by licking/motion that cannot be regressed out:* label as ambiguous; propose follow-up with behavior matched (iso-EV set) or quiescence-enforced paradigms.
- *Inverted-U present in Sub-design 1 but collapses under iso-EV dissociation:* this indicates the apparent uncertainty effect was an EV artifact → favors C, not B. Explicitly do **not** claim uncertainty coding in this case.
- *Underpowered (CI spans both flat and inverted-U):* declare inconclusive; do not over-interpret; report precision achieved and the n needed for resolution.

---

## Relationship of Conclusions Back to the Packet
The packet establishes the **phasic prediction-error** framework (diminution with prediction, timing-activation, omission-depression) and explicitly leaves open whether **waiting-period activity encodes variable outcomes**. The proposed experiment is the minimal, directly-motivated test of that exact gap: it reuses the packet's established phasic phenomena as **internal positive controls** and adds the one manipulation (outcome uncertainty with value dissociated) needed to adjudicate among a pure-error channel (A), an uncertainty code (B), and a value ramp (C). No probability-manipulation result is assumed or imported; the packet contains none, and none is claimed here as observed.

## Key Limits and What Would Change the Recommendation
- **Species/preparation not specified in packet:** if the available system cannot isolate dopaminergic signals or sustain the required delay, the design must adapt (photometry vs units) and sensitivity to a modest sustained signal may drop—this is the most consequential uncertainty.
- **Asymptotic-learning scope:** the design deliberately studies stable predictions; it cannot speak to uncertainty dynamics *during* learning. If the higher-value interest is learning-rate control, a separate longitudinal design would be warranted.
- **Expected-value/variance correlation** in a naive probability sweep is the chief confound; the iso-EV/iso-variance dissociation (Sub-design 2) is therefore non-optional—if it cannot be implemented, conclusions must be downgraded from "uncertainty coding" to "outcome-related delay activity of undetermined form."
- **Window artifacts:** the credibility of any delay-period claim rests on clean separation from cue/outcome transients; failure here converts positive findings to ambiguous.

If a reader's priority were instead *downstream causal consequences* of any uncertainty signal (e.g., effects on behavior), the next question would shift to a causal perturbation design; given the packet's framing ("carries additional information"), the correlational-identification experiment above is the correct first step.
