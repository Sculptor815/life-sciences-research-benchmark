# GLM 5.3 FlashX / neu-d01

Original final answer, shared by both scoring rounds.

# Optogenetic Test of Necessity of the P→Q Projection During Cue Retrieval

## 1. Bottom-line recommendation

Test necessity **within-subject, trial-by-trial**: inhibit P neurons projecting to Q (projection-targeted inhibitory opsin, per O2) **only during the cue-retrieval epoch** of well-learned trials, randomized against interleaved light-off trials in the same animals, with a **projection-matched control group** (opsin in P neurons projecting to the *other* region, per O1) and an **opsin-negative control** absorbing the visible-light artifact (per O4). Movement (per O3) is handled by (a) restricting illumination to the retrieval epoch so locomotion demands before cue onset are unaffected, (b) measuring and statistically controlling locomotion within the epoch, and (c) a locomotion-matched control task in which light is delivered but no cue is presented. If correct-choice rates fall selectively on light-on retrieval trials in the P→Q group — but not in the P→other group, not in opsin-negative animals receiving identical light, and not in a no-cue locomotion control — the inference that P→Q is necessary for cue retrieval (not for seeing the cue, moving, or consuming reward) is supported.

**Do not rely on between-subject comparisons alone**: the visible-light confound (O4) and baseline performance variability make within-subject randomization essential.

---

## 2. Evidence-to-inference-to-conclusion chain

| Evidence | Inference it licenses | Inference it does **not** license |
|---|---|---|
| O1: P projects to Q and to another region | An anatomical pathway exists that could carry retrieval signals; the "other" projection provides a projection-matched control target | That the pathway is functionally active or behaviorally relevant |
| O2: Inhibitory opsin can be targeted to P→Q neurons | Causal suppression of specifically the P→Q projection is technically feasible, without suppressing P→other | That suppression is complete, spatially restricted, or behaviorally silent — these need calibration |
| O3: The outcome is correct choice, but the task requires locomotion | Correct choice could fail because retrieval fails *or* because locomotion/arousal fails; any deficit must be dissociated from movement | — |
| O4: Light delivery is visible | The animal may detect illumination; light itself (novelty, retinal activation, avoidance) could alter behavior independent of P→Q | — |

**Chain of inference:** If P→Q is necessary for cue retrieval, suppressing it during retrieval should reduce correct choices on illuminated trials relative to interleaved non-illuminated trials in the same trained animals. For this drop to be attributed to retrieval rather than confounds, it must disappear or attenuate under conditions holding constant (i) visual stimulation (opsin-negative + light), (ii) generic P suppression with spared Q-projecting fibers (P→other control — note this control suppresses a *different* P population, so it controls for P-related motor/arousal effects, not for all alternative mechanisms), (iii) locomotion demands (locomotion epoch not illuminated; speed matched or covaried), and (iv) cue detection (task version requiring only cue detection without choice). **Conclusion rule:** necessity is concluded only when the light-on deficit is specific to the P→Q group × retrieval-epoch × correct-choice measure conjunction.

---

## 3. Concepts in their correct relationships

- **Structure:** P cell bodies; axonal projection P→Q; collateral projection P→other (O1).
- **Intervention:** cell-body-located inhibitory opsin in P→Q neurons — suppressing at somata silences the projection's output while sparing other P populations only because targeting is projection-specific (O2). *Do not* place the opsin/illumination in Q axons as the primary test: axonal inhibition would test the projection, but somatic targeting (O2) additionally guarantees the animal's P→other projection is untouched, which is critical given O1.
- **Behavior:** learned choice task = cue presentation → retrieval epoch → choice → outcome; locomotion is required for execution but is not the dependent variable (O3).
- **Necessity claim:** P→Q activity *during retrieval* is necessary for correct choice — a claim about a time-locked causal contribution, established by epoch-specific suppression with epoch-independent performance intact.

---

## 4. Operational protocol (ordered)

### Phase A — Preparation and quality checks

**A1. Task training to asymptote before surgery.** Train animals to a pre-defined stable criterion (e.g., ≥ some pre-set % correct across 3 consecutive sessions — set the numeric threshold from pilot data; do not assume a value here). Record per-trial: cue latency, choice, correct/incorrect, intertrial interval (ITI) length, movement speed trajectories, port approach/reward-collection latencies. These pre-surgical baselines power the within-subject design.

**A2. Characterize the retrieval epoch.** From pilot sessions, define the retrieval window operationally (cue onset to choice commit, or cue offset). All illumination timing in later phases is derived from these measured distributions — a calibration, not an assumption.

**A3. Viral targeting (P→Q group).** Inject retrograde vector into Q delivering Cre (or Flp) to Q-projecting neurons; inject Cre/Flp-dependent inhibitory opsin (e.g., a validated anion-pump or chloride-conducting opsin — choose the opsin from current validated reagent list; do not cite performance numbers as fact) into P. Per O1, the **P→other control group** gets the identical construct scheme with the retrograde vector placed in the other projection target instead.

**A4. Opsin-negative control group.** Same surgery, opsin replaced with fluorescent reporter only; identical fiber implants and illumination.

**A5. Optical calibration (required for every unknown parameter — do not import literature values as guarantees):**
- Measure power output of every fiber in air with a power meter before implantation and after explant; recalibrate any drift > ~10%.
- Estimate illuminated volume: in a subset of animals or with an optical phantom/slide-mounted fluorescent dye, measure the light spread at the working power to confirm coverage of the opsin-expressing P population and estimate spillover. Where direct measurement is impossible, record power, fiber diameter, and tip-to-soma distance so spread can be modeled and reported.
- Determine suppression onset/offset timing *empirically* for the chosen opsin: brief light pulses delivered while recording light-evoked changes (electrophysiology, or a behavioral probe such as light-induced interruption of an ongoing action), sweeping intensity and pulse protocol until suppression is reliable within the retrieval-epoch duration from A2. Report the intensity–latency curve achieved; do not assume instantaneous or sustained suppression.
- Verify the laser/LED cannot heat tissue at the working duty cycle: use the lowest power meeting the suppression criterion, pulsed at the lowest duty cycle that spans the epoch.

**A6. Histological quality check (exclusion criterion applied before analysis).** After behavior, section brains: confirm retrograde label confined to Q (or other target), opsin expression in P restricted to the intended projection-defined population, fiber track terminating over the expression field, and no gross tissue damage at the tip. Pre-register exclusion criteria: off-target retrograde label, expression in non-intended P neurons, fiber misplacement, or tissue damage → exclude before unblinding.

### Phase B — Independent units, allocation, blinding

- **Unit of analysis:** the individual animal for group-level inference; the individual *trial* within animal for within-subject contrast (with animal as a random effect — trials are not independent units for confirmatory inference).
- **Allocation:** randomized assignment of animals to P→Q, P→other, or opsin-negative groups, balanced for pre-surgical performance (stratified block randomization using A1 baselines). Balanced sexes where available.
- **Blinding:** the experimenter running sessions is blind to group (opsin vs. reporter identity masked by coding); the analysis script written and frozen before unblinding. Light-on vs. light-off trials are randomized by the acquisition software, invisible to the experimenter.

### Phase C — Intervention and sampling

**C1. Re-training with hardware.** Post-surgically re-establish baseline performance with fibers attached; require return to A1 criterion.

**C2. Randomized illumination schedule.** Within each session, ~50% of retrieval epochs are illuminated (light-on), interleaved with light-off trials, order randomized and pre-programmed; ITIs jittered so illumination is unpredictable. Intensity and timing per A5 calibration.

**C3. Epoch restriction.** Light delivered only during the retrieval window (A2). Critically for O3: **no illumination during the ITI, the pre-cue travel period, or reward collection.** This isolates retrieval from locomotion-to-cue and consummatory behavior.

**C4. Visible-light mitigation (O4).** Because light is visible: (i) shield the delivery path/enclose the fiber patch cord where feasible so retinal illumination is minimized or diffuse; (ii) opsin-negative animals receive the *identical* illumination schedule — any residual behavioral effect of visible light appears as a group-level difference and can be subtracted; (iii) run an explicit detectability probe: in opsin-negative animals, compare light-on vs. light-off trials for omissions, speed changes, or orienting. If light-on alters these, strengthen shielding/randomize a wavelength-matched counter-balanced configuration, or add a pre-session habituation epoch with visible light until detectability measures are null.

**C5. Locomotion controls (O3).**
- **Primary:** measure speed and path continuously; require that light-on and light-off trials within each animal be compared with locomotion as a time-varying covariate, and additionally perform a matched-pairs analysis comparing light-on and light-off trials with equivalent speed profiles at cue onset.
- **Locomotion-only probe:** sessions in which light is delivered on a matched random schedule but **no cue is presented** (animals locomote to ports for reward on an uncued schedule). If P→Q inhibition impairs locomotion or reward collection here, the retrieval deficit interpretation fails and movement is a confound.
- **Projection specificity:** because P→other neurons are unopsined in the P→Q group, any global locomotor effect of suppressing *all* P output is not present by design; the P→other control group tests whether suppressing *a* P projection (a different one) produces any locomotor or choice effect.

**C6. Sampling target.** Power the within-subject contrast on the number of light-on vs. light-off trials per animal needed to detect the effect size observed in pilot data or a pre-set minimal effect of scientific interest; run until each animal reaches that trial count across sessions, with per-session trials capped to avoid fatigue effects (record session order and analyze with session as a factor).

### Phase D — Measurements

Per trial, logged automatically: cue time, illumination time and parameters, choice, correct/incorrect, omission, choice latency, reward-collection latency; continuous speed and position; continuous light log. Post-hoc: histology (A6).

### Phase E — Controls (summary table)

| Control | Confound addressed | Prediction if result is clean |
|---|---|---|
| Interleaved light-off trials (within-subject) | Session drift, light novelty | Deficit on light-on only |
| Opsin-negative + identical light | Visible light (O4), heat, handling | No light-on effect |
| P→other opsin group (O1) | Non-specific suppression of P output; projection-unspecific effects | No (or reduced) retrieval deficit |
| Retrieval-epoch-only illumination | Motor execution of choice, reward consumption, ITI locomotion (O3) | Deficit time-locked to retrieval |
| No-cue locomotion probe | Locomotion/arousal impairment (O3) | No impairment |
| Speed-matched/covariate analysis | Residual speed differences between trial types | Effect survives adjustment |
| Pre-surgical baseline stratification | Unequal learning ability across groups | Groups comparable |

### Phase F — Analysis

1. **Primary:** GLMM on correct/incorrect (logit link), fixed effects = light (on/off) × group (P→Q / P→other / opsin-negative) × epoch covariates; random intercepts (and light slopes) per animal; session as repeated factor. **Key test:** light×group interaction — light-on deficit present in P→Q and absent in controls.
2. **Secondary:** trial-level speed as covariate; sensitivity analysis restricted to light-on/light-off trial pairs with matched cue-onset speed; omission and latency analyses to detect motor slowing masquerading as retrieval impairment; mediation-style check: does the light effect on correctness reduce to zero after adjusting for speed?
3. **Time-lock check:** within-session analysis of whether the deficit is confined to illuminated trials (no carry-over onto subsequent light-off trials would indicate persistent motor disruption; carry-over would favor a motor/slowing account).

### Phase G — Acceptance, stopping, and troubleshooting

**Acceptance (all pre-registered):**
- ≥ pre-set % of animals per group pass histology (A6); excluded animals reported.
- Baseline (light-off) performance returns to A1 criterion in all groups.
- Opsin-negative group shows no significant light-on effect on correctness, omissions, or speed (visible-light confound controlled).
- No-cue locomotion probe shows no light effect in the P→Q group.
- Primary interaction significant with the deficit localized to retrieval-epoch illumination.

**Stopping/troubleshooting rules:**
- If light-on changes speed or omissions in opsin-negative animals → visible-light confound not controlled (O4): stop, improve shielding/habituation, repeat.
- If P→Q light-on trials show omissions or speed reduction without correctness change → motor confound (O3): narrow the epoch further, reduce power/duty cycle, or reconsider — a retrieval-specific claim is not supported.
- If P→other group shows the same deficit → effect is projection-unspecific; conclusion of P→Q necessity is **not** warranted.
- If suppression calibration (A5) fails to achieve reliable inhibition at tolerable power → the necessity test is underpowered; report as inconclusive rather than null.

---

## 5. Calibration of unknown parameters (nothing assumed)

| Unknown | Calibration procedure |
|---|---|
| Effective light spread / coverage | Pre-explant dye phantom or post-hoc estimate from recorded power, fiber NA/diameter, tip–soma distance; verify coverage against histology |
| Suppression latency, depth, duration | Empirical intensity/pulse sweep against a physiological or behavioral suppression readout; select lowest parameters meeting criterion within epoch duration |
| Retrieval epoch boundaries | Measured from pilot choice-latency distributions (A2) |
| Light detectability | Opsin-negative light-on/off probe for orienting, omission, speed changes (C4) |
| Photothermal safety | Power meter + lowest duty cycle; post-hoc tissue inspection at fiber tip |
| Trial/sample size | Powered from the variance of the within-subject light-on/light-off difference in pilot sessions; report the pre-set effect threshold |

## 6. Alternatives and limits

- **Alternative targeting:** axon-terminal illumination in Q would be a stronger *projection* test but risks off-target effects on afferents in Q and loses the O1-based projection-matched control; use as a confirmatory follow-up only.
- **Limit — incomplete suppression:** residual P→Q activity could produce a false negative; mitigate via A5 calibration and report achieved suppression magnitude.
- **Limit — P→other control is imperfect:** it suppresses a different population, so it does not control for every effect unique to the P→Q neurons themselves (e.g., their role in arousal); the no-cue probe partially covers this.
- **Limit — visible light (O4) can never be fully excluded**, only measured and subtracted via the opsin-negative group; residual detection asymmetries across groups remain the main unresolvable uncertainty.
- **Limit — timing resolution:** if retrieval processes extend beyond the illuminated epoch, the deficit may underestimate necessity; report epoch boundaries and treat the claim as epoch-scoped.

**Conclusion:** A within-subject, epoch-restricted, projection-targeted inhibition design — with projection-matched, opsin-negative, and locomotion controls plus empirical calibration of all optical and temporal parameters — provides a defensible test of whether P→Q is necessary for cue retrieval, with explicit decision rules separating a retrieval effect from movement (O3) and visible-light (O4) artifacts.
