# GLM 5.3 FlashX / neu-r03

Original final answer, shared by both scoring rounds.

# Proposed Next Question, Competing Mechanisms, and Full Research Plan

## 1. Bottom line first (recommended next action)

The most valuable next biological question, given only the supplied packet, is:

**Does dopamine-neuron activity during the waiting period between a predictive cue and a possible reward carry information about the *probability or magnitude* of the upcoming outcome (prospective value), or are dopamine neurons restricted to signaling violations of prediction at the moment the outcome does or does not arrive (retrospective reward-prediction-error, RPE, coding)?**

The packet establishes the RPE phenomena (diminishing responses to predicted rewards, activation at unexpected timing, depression at omission) but explicitly contains no probability-manipulation experiment and no result on waiting-period information content. Testing this requires a new experiment manipulating reward probability with timing held constant — proposed below. Nothing in this answer should be read as a reported result; all experiments are proposals.

---

## 2. Evidence → inference → conclusion chain from the packet

| Evidence (reported in packet) | Justified inference | Inference NOT licensed |
|---|---|---|
| Reward responses diminish as rewards become predicted | Dopamine responses are shaped by prediction, consistent with RPE coding | That dopamine carries no prospective signal before outcome |
| Unexpected timing → activation | Timing prediction errors drive activation | That the same neurons code outcome value during the wait |
| Omission at expected time → depression | Omission is coded as a negative error | That waiting-period activity exists at all, or is informative |
| Packet contains no probability manipulation | Whether waiting-period activity scales with outcome probability is untested and open | Any claim about what such an experiment would show |

**Gap:** The RPE observations tie dopamine to *violations* of prediction. They are silent on whether sustained or phasic activity *during the interval* of expectation encodes the *content* of the prediction (probability/magnitude of reward). These are logically separable: a system could compute RPEs at outcome time without maintaining any value representation during the wait, or it could maintain such a representation that also produces RPEs at outcome.

---

## 3. Competing mechanisms and discriminating predictions

**Hypothesis A — Pure retrospective RPE coding.** Dopamine neurons are activated only by deviations from prediction at the time the outcome is or is not delivered. Waiting-period activity, if present, reflects timing estimation (e.g., a ramp tied to expected reward time) or nonspecific arousal, not outcome value.

**Hypothesis B — Prospective value coding.** During the waiting period, dopamine activity scales monotonically with the expected probability (and/or magnitude) of reward. The outcome response then reflects the discrepancy between this maintained value and the delivered outcome.

**Hypothesis C — Confound account (behavioral/state).** Waiting-period activity tracks licking, movement preparation, or arousal that happen to correlate with expectation in the chosen design, but is not a value signal per se.

**Discriminating predictions** (in an experiment where reward probability p is varied blockwise across {0, 0.25, 0.5, 0.75, 1} with cue identity counterbalanced, cue-to-reward interval held constant, and reward magnitude fixed):

- **A:** Waiting-period firing is identical across p conditions; outcome responses follow RPE (large for p=0 rewarded "lucky" trials, deep depression for unrewarded trials at p=1).
- **B:** Waiting-period firing increases monotonically with p within the fixed interval; outcome responses still follow RPE (i.e., outcome responses anti-correlate with p on rewarded and unrewarded trials respectively).
- **C:** Apparent waiting-period probability modulation disappears or reverses once licking/movement/time-in-trial are included as covariates, or does not survive a design in which behavior and probability are decorrelated.

Critically, A and B make *opposite* predictions for the waiting window but can both accommodate standard RPE outcome responses — which is exactly why the packet's evidence cannot decide between them.

---

## 4. Proposed research plan (detailed, ordered, auditable)

### Phase 0 — Prerequisites and feasibility (proposed, not reported)

0.1 **Species/preparation choice.** Choose an awake, head-fixed behaving preparation compatible with single-unit recording (e.g., mice or rats with chronic multielectrode drives or high-density probes). *Rationale:* single-unit resolution is needed to separate dopamine-neuron responses from population averages; the packet does not specify the species or method used for the quoted observations, so this is a design choice, not an inherited parameter.

0.2 **Dopamine-neuron identification.** Pre-specify identification criteria: putative dopamine neurons identified by waveform criteria and/or (preferred, if available) optogenetic-tag identification in a TH-Cre line. *Assumption to declare:* whether identification is post hoc (histological verification of track location in substantia nigra pars compacta / ventral tegmental area) or online (opto-tagging). This affects analysis exclusions and must be registered before data collection.

0.3 **Ethics, power, and preregistration.** Pre-register hypotheses, primary endpoints, exclusion rules, and sample size. Power analysis based on a pilot effect size for the key contrast (waiting-period firing at p=0.25 vs p=0.75); if no pilot data exist, state that n is set by convention (e.g., ≥ 8 animals per preparation, ≥ 30–50 well-isolated dopamine neurons total) and flagged as an assumption.

### Phase 1 — Behavioral training (proposed)

1.1 **Task.** Pavlovian conditioning: trial starts (fixation/entry), cue (500 ms–1 s), then a fixed waiting period (e.g., 1.5–2.5 s), then reward, no reward, or (in one control condition) reward with unexpectedly shifted timing, mirroring the packet's timing-shift phenomenon as an internal replication.

1.2 **Probability blocks.** Within each session, run blocks of trials at p = 0, 0.25, 0.5, 0.75, 1 (blocked or mixed-with-cues-disambiguating; mixed designs prevent block-level satiety confounds but require distinct cues — see 1.4).

1.3 **Timing manipulation (internal replication control).** In a separate block, hold p constant but occasionally shift reward timing later. Prediction (from the packet's own phenomenon, which this experiment should reproduce as a sanity check): dopamine activation at the originally expected time, and responses to the delayed reward.

1.4 **Counterbalancing.** Cue identities (odor/tone) are assigned to probabilities and counterbalanced across animals, so cue identity is never confounded with probability.

1.5 **Behavioral criterion to proceed.** Animals must show reliable, cue-conditioned anticipatory licking that differs between high- and low-p cues (pre-specified criterion, e.g., anticipatory lick rate at p=1 cue > p=0 cue on ≥ 3 consecutive sessions). If not met, see troubleshooting (§7).

### Phase 2 — Calibration (proposed)

2.1 Reward delivery: volumetric calibration of the lick spout daily; verify reward timing jitter < 5 ms.
2.2 Recording: daily impedance checks, spike-sorting quality metrics pre-specified (isolation distance, L-ratio, refractory-period violations).
2.3 If using fiber photometry as a secondary modality: photobleaching check, bleaching correction, isosbestic/motion-control channel; however, photometry alone cannot resolve cell-type heterogeneity and is proposed only as a cross-check, with single units as the primary measurement.
2.4 Video-based motion tracking of the animal; motion regressors will be included in analysis.

### Phase 3 — Independent units, allocation, blinding

3.1 **Independent unit:** the *animal* for behavioral outcomes; the *neuron* is the unit for firing-rate analyses but is nested within animal — analyses must use mixed-effects models with animal as a random effect (see Phase 5), and the effective sample size for inference is animals, not trials or neurons.
3.2 **Allocation:** not a treatment experiment, so randomization applies to cue–probability assignment (counterbalanced across animals) and to block order (Latin-square/randomized, pre-specified).
3.3 **Blinding:** experimenters scoring behavior and performing spike sorting are blinded to probability condition where feasible (automatic spike sorting with pre-specified quality gates; analysis code run on condition-shuffled files before unblinding).

### Phase 4 — Recording session structure and controls

4.1 **Primary recording session set:** interleaved (or blocked, counterbalanced) trials at the five probability levels, fixed timing, fixed magnitude. Minimum pre-specified trials per condition per session (e.g., ≥ 20) to estimate firing rates.

4.2 **Controls, each with its purpose:**

- **C1 Random-reward control:** trials where reward occurs with no predictive cue at all (p effectively unconditioned); tests whether waiting-period activity requires an explicit prediction or merely reward context.
- **C2 Pseudo-timing control:** occasionally extend the interval on p=1 trials (the packet's own timing-shift phenomenon, used as an internal replication); prediction from the packet: activation at the expected time. Failure to replicate would trigger troubleshooting rather than proceeding to interpretation of the main result.
- **C3 Magnitude control (separate session/block):** vary magnitude at fixed p. If waiting activity scales with magnitude too, this strengthens the value interpretation over a "probability detector" interpretation.
- **C4 Non-rewarding cue control:** a cue predicting nothing; establishes baseline.
- **C5 Probability–behavior decorrelation control (addresses Hypothesis C):** a sub-condition where, on a subset of trials, a small reward is delivered after the p=0 cue ("surprise" reward) so that trial-by-trial licking and value are partially decoupled; waiting-period activity is then regressed on probability and on licking separately.
- **C6 Satiety/time-on-task control:** randomize block order and include session-half as a covariate, since satiety drifts can correlate with block position.

4.3 **Causal arm (Phase 4b, only after the correlational result):** If waiting-period activity scales with p, run an optogenetic perturbation (e.g., inhibiting dopamine neurons, or pathway-specific manipulation, during a narrow pre-specified waiting window on a random subset of trials, interleaved and counterbalanced). Prediction under B: perturbation selectively disrupts probability-dependent anticipatory behavior (licking/latency) without disrupting the timing-shift responses at outcome — i.e., tests whether the waiting signal is functionally engaged, not epiphenomenal. This arm is a *proposal contingent on Phase 4 outcome* and is explicitly labeled as such.

### Phase 5 — Measurements and analysis plan (pre-specified)

5.1 **Primary measurement:** per-neuron firing rate (spikes/s, 100 ms bins) averaged over a pre-registered waiting window (e.g., 300 ms after cue offset to 200 ms before expected reward, excluding movement-onset-aligned windows).

5.2 **Primary analysis:** linear mixed-effects model, per-neuron and across the population:
firing ~ p (continuous) + block order + time-in-session + lick rate + motion + (1 | animal).
Key test: the coefficient of p in the waiting window. Pre-register the direction: monotonic increase with p under Hypothesis B.

5.3 **Secondary analyses:**
- Outcome-window RPE analysis (replication of the packet's phenomena at each p; predicted depression scales with p on omission trials).
- Cross-validated decoding of p from waiting-period population activity (support-vector or logistic decoder; cross-validation at the animal level to avoid leakage; permutation testing for significance).
- Model comparison at the population level: RPE-only model (A) vs value-coding model (B) vs behavior-confound model (C), using AIC/BIC and held-out prediction.
- Timing-shift block: confirm activation at omitted expected time (internal replication).

5.4 **Correction and robustness:** FDR correction across neurons; sensitivity analyses excluding high-motion trials, first trials of blocks, and post-lick intervals; report effects with and without movement covariates (this is the explicit A/B/C discrimination).

### Phase 6 — Stop rules (pre-specified)

- **Behavioral stop:** if the anticipatory-licking criterion (1.5) is not reached by a pre-set session cap (e.g., 20 training sessions per animal), halt that animal; do not record and do not include.
- **Yield stop:** if well-isolated putative dopamine-neuron yield falls below the pre-specified minimum per animal across sessions, stop recruiting that animal and re-evaluate the preparation.
- **Replication stop:** if the timing-shift internal replication (C2) fails in the first cohort, stop and troubleshoot (see §7) before any interpretation of waiting-period data.
- **Interim look:** one pre-specified interim analysis after ~50% of animals, with a stopping rule only for harm/futility (e.g., zero neurons showing any task-locked modulation), not for significance — to avoid optional stopping bias.

### Phase 7 — Troubleshooting (anticipated problems and responses, all proposed)

- **No behavioral learning:** adjust cue salience, deprivation schedule, or trial count; verify reward palatability; check for a fixation-task confound.
- **Photometry/artifact concerns (if used):** rely on single units; enforce isosbestic-channel and motion regression; exclude high-motion trials pre-specified.
- **Confounding licking-driven movement artifacts in recordings:** include lick-locked regression and compare firing aligned to cue vs to lick onset.
- **Cue-identity confound:** verify counterbalance by testing the p effect *within* each counterbalance group before pooling.
- **Satiety drift:** shorten sessions, randomize block order, include session-half covariate.
- **Failure to replicate omission depression/timing activation:** suspect preparation differences from whatever produced the packet's observations (species/method unspecified in packet); do not proceed to the main question until replication succeeds, and report the discrepancy explicitly.

---

## 5. Conditional outcomes and the strongest justified conclusion in each case

**Positive outcome (supports Hypothesis B).** Waiting-period firing increases monotonically with p, survives lick/motion/time covariates, decodes p at above-chance levels with animal-level cross-validation, and outcome responses still follow RPE; the causal arm disrupts probability-dependent anticipatory behavior.
- *Strongest justified conclusion:* dopamine-neuron population activity during the waiting period carries prospective information about expected reward probability and is functionally engaged in expressing that expectation — provided the causal arm is completed. Without the causal arm, the strongest conclusion is *correlational only*: waiting-period activity carries outcome-probability information; its causal role remains untested.
- *What would weaken it:* the effect vanishing within the C5 decorrelation condition, or appearing only in counterbalance groups with one cue assignment.

**Negative outcome (supports Hypothesis A).** Waiting-period firing is flat across p; outcome responses scale with p in the RPE direction; timing-shift replication succeeds.
- *Strongest justified conclusion:* under these task conditions, dopamine neurons do not encode outcome probability during the waiting period; their information content is confined to prediction violations at outcome, consistent with pure RPE coding. Limit: this is task- and parameter-dependent; a different interval, magnitude range, or mixed vs blocked design could reveal value coding. Report the negative as conditional on the parameters used.

**Ambiguous outcome.** Waiting-period activity differs across p but does not survive behavioral covariates; or effects are present only in a neural subpopulation (e.g., some neurons track p, others track time); or photometry and single units disagree.
- *Strongest justified conclusion:* the evidence is insufficient to distinguish prospective value coding from behavior/state confounds. Declare the question unresolved. The appropriate next step is a redesigned decorrelation experiment (strengthening C5, e.g., within-cue trial-by-trial probability changes) rather than a forced interpretation.

---

## 6. Distinguishing proposals from reported results; limits

- **Reported (per the packet only):** diminishing responses to predicted rewards; activation at unexpected timing; depression at expected-time omission; absence of any probability-manipulation or waiting-period-information result.
- **Proposed here:** everything in §4–§5 — the probability-block experiment, all controls, the causal optogenetic arm, all analyses, and all three outcome scenarios. **No result from §4–§5 has been observed; all outcome descriptions are hypothetical conditionals.**
- **Assumptions not supplied by the packet and therefore declared as assumptions:** species, dopamine-identification method, recording modality, task parameters (interval length, cue modality), sample sizes, and the generalization that the preparation used will reproduce the packet's RPE phenomena (hence the internal replication control C2).
- **Key limits of the plan:** single-unit correlational results cannot establish causation without Phase 4b; a negative result is parameter-bound; and the packet's silence about the original methods means the internal replication is a prerequisite, not a guarantee.

**Final recommendation:** run the fixed-timing, variable-probability experiment with the controls and covariate strategy above as the single next step, because it is the minimal experiment that separates prospective value coding (B) from pure RPE coding (A) and from behavioral confounds (C) — three explanations the packet's existing evidence cannot distinguish.
