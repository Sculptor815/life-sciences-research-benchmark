# Kimi K3 / neu-d01

Original final answer, shared by both scoring rounds.

## Recommended design

Test necessity by inhibiting **P axon terminals in Q**, not P cell bodies, specifically during a movement-free cue-retrieval interval. Because P also projects elsewhere, somatic inhibition would not isolate the P→Q pathway.

The strongest design is:

1. Express an inhibitory opsin in P neurons that project to Q.
2. Illuminate their terminals in Q during the cue/retrieval window.
3. Compare opsin and reporter-control animals receiving identical illumination.
4. Randomize light and no-light trials within animals.
5. Separate cue retrieval from the locomotor response with a hold/delay interval.
6. Include intertrial and locomotion-epoch illumination controls.
7. Make the animal—not the trial—the independent biological unit.

A necessity conclusion is justified only if cue-epoch inhibition reduces correct choices more in opsin than reporter animals while visible-light effects, response completion, movement initiation, and locomotion are adequately controlled.

---

## 1. Causal relationships and evidence-to-inference chain

### Causal model

```text
Learned cue
   → cue processing and retrieval of the learned choice rule
   → P→Q activity during the retrieval window
   → choice selection
   → locomotion
   → observed correct/incorrect outcome
```

Important alternatives:

```text
P→Q inhibition → impaired cue sensory processing → wrong choice
P→Q inhibition → impaired locomotion → omission, slowing or wrong choice
Visible light → orienting/distraction/arousal → altered behavior
P soma inhibition → altered output to Q and another region
```

### Evidence, inference and design consequence

| Evidence | Inference | Design consequence |
|---|---|---|
| **O1: P projects to Q and another region.** | P manipulation is not automatically projection-specific. | Illuminate P terminals in Q rather than P somata. Quantify collateral targeting and illumination spread. |
| **O2: Inhibitory opsin expression can be targeted to P neurons projecting to Q.** | Projection-defined inhibition is feasible. | Verify expression, Q-terminal coverage and reversible functional suppression. |
| **O3: Correct choices are the proposed outcome, but the task requires locomotion.** | Lower accuracy alone cannot distinguish failed retrieval from failed movement. | Use a pre-movement retrieval window, continuous movement measurements and locomotion-control illumination. |
| **O4: Delivered light can be visible to the animal.** | Light can act as a sensory stimulus independent of opsin. | Shield light, match visible stimulation across conditions, and include reporter animals receiving identical light. |

### Required inference chain

1. O1 and O2 establish that a projection-targeted manipulation is feasible.
2. Terminal illumination in Q is therefore the appropriate manipulation; illumination over P somata would also implicate the other projection.
3. If randomized cue-window inhibition produces an opsin-specific reduction in subsequent correct choices, P→Q activity is necessary for normal performance during that window.
4. That inference becomes specific to cue retrieval only if:
   - visible light does not explain the effect,
   - response availability and locomotion remain intact,
   - the effect is stronger during the retrieval window than during control epochs, and
   - cue sensory processing is not comparably impaired.
5. A null result supports non-necessity only if inhibition is functionally validated, pathway coverage is adequate, and the experiment is powered to detect the prespecified effect.

This is an operational necessity test: it asks whether normal P→Q activity is required under this task and manipulation. It does not establish that P→Q carries the retrieved information, that the role is exclusive, or that the pathway is necessary in every behavioral context.

---

## 2. Operational protocol

The packet does not report the opsin identity, wavelength, light power, pulse pattern, cue duration, delay length, sample size, learning criterion or movement threshold. These must be calibrated empirically and prespecified rather than assigned arbitrary values.

### Step 1 — Define the retrieval window and endpoints

Operationally define cue retrieval as the interval:

- beginning at learned-cue onset, and
- ending before the go signal or before reliably detectable movement onset.

Prefer a task version with:

1. a fixed starting position,
2. cue presentation,
3. a short hold or delay during which locomotion is not permitted,
4. a go signal,
5. locomotion to the selected choice.

If the existing task has no movement-free interval, estimate cue-to-movement latency from baseline data. If no reliable window exists, modify the task or limit the conclusion to “activity around cue presentation,” not retrieval independent of movement.

Prespecify:

- **Primary cognitive endpoint:** probability of a correct choice among trials with an emitted choice.
- **Co-primary interpretation endpoints:** completion/omission rate, movement latency and movement kinematics.
- **Secondary endpoint:** correct-choice probability with omissions counted as failures, to avoid silently excluding treatment-induced aborts.
- The smallest behavioral effect considered meaningful.
- Statistical thresholds and stopping rules before unblinding.

Do not treat a drop in accuracy as sufficient if omissions or abnormal movement increase substantially.

### Step 2 — Instrument the behavior

Measure, with timestamps aligned to cue and light onset:

- cue identity and duration;
- go-signal time;
- position, velocity and trajectory;
- movement onset;
- choice-entry time;
- correct, incorrect, omitted and aborted trials;
- premature movement and hold violations;
- orienting, startle or other immediate reactions to illumination.

Calibrate the movement-onset detector using baseline sensor-noise distributions and independent blinded video scoring. Do not assume a universal velocity threshold.

Counterbalance or randomize cue-action and cue-location mappings across animals so a deficit is not attributable to one sensory cue or one movement direction.

### Step 3 — Establish stable learned performance

Train animals until choice accuracy is stable according to a prespecified rule based on absence of session-to-session trend and acceptable within-animal variability.

Record baseline:

- accuracy by cue and choice direction;
- omissions and aborts;
- cue-to-movement latency;
- movement speed and path;
- spontaneous orienting.

Use these data to calibrate the hold duration and retrieval-window light duration. The duration should cover the defined retrieval process while ending before the earliest reliable movement. Validate that animals can perform the hold without excessive aborts before adding opsin manipulation.

### Step 4 — Define independent units and allocate animals

The **animal** is the independent unit for comparisons involving viral group. Sessions are nested within animals, and trials are nested within sessions. Trials are not independent replicates merely because light is randomized trial by trial.

After baseline training:

1. Randomly allocate animals to:
   - inhibitory opsin in Q-projecting P neurons, or
   - a non-opsin reporter control in the same population.
2. Stratify randomization by baseline performance and relevant cohort variables, such as batch or sex if used.
3. Conceal allocation from behavioral scorers and analysts.
4. Automate light scheduling and scoring where possible.
5. Keep histology scorers blind to behavioral results.

Estimate final animal number from a pilot or calibration cohort using animal-level variability and the prespecified smallest meaningful effect. Do not derive statistical power from the number of trials alone.

### Step 5 — Surgery and anatomical quality checks

Use the projection-targeting strategy established by O2 and place the optical interface over Q to inhibit P terminals locally.

Quality checks:

1. Confirm opsin expression in P neurons labeled as Q-projecting.
2. Estimate the proportion of Q-projecting P neurons expressing the opsin.
3. Determine whether the same cells project to the other region described in O1, using an appropriate projection label.
4. Confirm terminal labeling and optical placement in Q.
5. Measure likely light spread and exclude animals in which illumination is likely to reach P somata or unintended structures.
6. Compare baseline behavior after recovery but before light testing to detect expression- or surgery-related effects.

Perform pilot histology before the full experiment and final blinded histology for every animal. Animals failing prespecified targeting or placement criteria should be excluded from the primary causal analysis but reported.

### Step 6 — Functional light calibration

Histological expression alone is insufficient.

In calibration sessions independent of the primary behavioral estimate:

1. Use an available physiological or molecular readout to verify that Q illumination reversibly suppresses P-terminal output or the predicted Q response.
2. Titrate light power, duration and duty cycle to the lowest exposure producing reliable reversible suppression.
3. Confirm recovery after light offset and absence of cumulative suppression across repeated trials.
4. Where feasible, assess whether illumination alters P somatic activity or output to the other projection. If this cannot be tested, retain collateral effects as a limitation.
5. Freeze the final parameters before behavioral randomization.

Do not infer non-necessity from a behavioral null unless this functional validation passed.

### Step 7 — Calibrate and control visible light

Because light can be visible, use layered controls:

- Enclose exposed fiber connections and implanted hardware in opaque shielding.
- Keep room illumination and visual background constant.
- Measure stray light around the implant and testing chamber during calibration.
- If residual visibility cannot be eliminated, deliver a matched external visual masker across both light and sham-light epochs so visibility is not treatment-correlated.
- Match shutter, trigger and other equipment events on no-light trials where technically possible.
- Most importantly, give reporter-control animals the same illumination schedule and calibrated light exposure as opsin animals.

Compare light versus no-light behavior in reporter animals to estimate the direct sensory effect. If reporter light causes floor-level disruption, improve shielding before testing the main hypothesis.

### Step 8 — Intervention conditions

Use a two-factor core design:

| Factor | Levels |
|---|---|
| Virus | Inhibitory opsin or non-opsin reporter |
| Light | Calibrated light or no light |

Randomize light condition within animal and session. Balance it across cue identity, choice direction and baseline movement characteristics. Light must not predict cue identity, rewarded side or reward probability.

Within each virus group, include the following light epochs:

1. **Cue/retrieval epoch:** light from the defined cue-retrieval onset until before the go signal or movement onset.
2. **No-light epoch:** identical task events without terminal illumination.
3. **Intertrial epoch:** the same light exposure during a period with no cue or required choice; controls for persistent arousal, illumination artifacts and nonspecific suppression.
4. **Locomotion-control epoch:** the same inhibition during comparable movement that does not require retrieval of the learned cue-choice rule. This may be a separate movement probe or carefully designated post-go probe trials.
5. **Optional post-cue epoch:** if the cue ends before the delay, illuminate after cue offset but before movement. This helps separate retrieval/maintenance from direct sensory encoding.

Use the same calibrated light parameters across all illuminated epochs unless calibration demonstrates that a different duration is required and that change is prespecified.

### Step 9 — Sampling schedule

Interleave conditions within sessions to control for motivation, learning, fatigue and slow drift.

For each session:

- balance light condition across every cue and choice direction;
- avoid predictable sequences;
- include enough no-light trials to estimate concurrent baseline performance;
- repeat the manipulation across multiple sessions and preferably independent cohorts;
- record calibration and experimental light exposures separately.

Do not stop or add animals based on unblinded interim significance testing unless a formal prespecified sequential design is used.

---

## 3. Measurements and control interpretation

### Primary behavioral measurements

For every randomized trial:

- correct or incorrect among emitted choices;
- omission, timeout and abort;
- movement latency and path;
- maximum and mean speed;
- premature movement;
- time and spatial accuracy of choice entry;
- immediate orienting or startle after light onset.

Report both:

1. accuracy conditional on an emitted choice, and
2. all-randomized-trials performance with omissions counted as failures.

The first isolates choice accuracy more directly; the second protects against differential exclusion.

### Control logic

| Observation | Interpretation |
|---|---|
| Reporter light has no behavioral effect, but opsin cue light reduces accuracy. | Supports opsin-specific P→Q effect. |
| Reporter and opsin light both change behavior, with a larger cue-epoch deficit in opsin animals. | The difference-in-differences may support an opsin effect, but visible-light interaction remains a limitation. |
| Cue inhibition reduces accuracy but also delays, slows or prevents locomotion. | Retrieval and motor explanations cannot be separated. |
| Locomotion-control inhibition reproduces the movement phenotype. | The cue effect may reflect motor necessity. |
| Intertrial light produces similar later performance changes. | The effect is not temporally specific to retrieval. |
| Cue inhibition also impairs immediate detection of the same cue. | The result may reflect sensory encoding rather than retrieval. |
| Only post-cue/delay inhibition disrupts later choice. | Supports a mnemonic or maintenance role more strongly than direct cue perception. |

For sensory processing, use a probe in which the same physical cue is detected or discriminated without requiring retrieval of the learned choice mapping, or use a physically matched neutral cue in a separate probe. If such a probe is not possible, the post-cue temporal arm becomes especially important.

---

## 4. Analysis plan

### Primary estimand

For each animal, calculate or model:

```text
Cue-light effect =
accuracy during cue-window light
− accuracy during no-light cue trials
```

Compare this animal-level effect between opsin and reporter groups. Equivalently, estimate the virus × light interaction in a hierarchical model.

### Main model

Model choice outcome among emitted-choice trials as binary, with:

- virus group;
- light condition;
- virus × light interaction;
- cue identity and choice direction;
- baseline performance;
- pre-light movement or baseline velocity;
- random effects for animal and session.

Do not treat post-light movement as an ordinary confounder if it may mediate the circuit effect. Instead:

- adjust only for pre-light movement and baseline variables;
- analyze post-light movement as an outcome;
- provide matched or stratified analyses as supportive evidence.

### Secondary analyses

1. Analyze omission/abort probability with the same group × light structure.
2. Analyze movement latency, velocity, path and premature responding.
3. Test whether the cue-epoch interaction exceeds effects during:
   - intertrial illumination, and
   - locomotion-control illumination.
4. Test direct visible-light effects in reporter animals.
5. Test sensory-probe performance separately.
6. Examine persistence by comparing post-light no-light trials with baseline trials.
7. Use prespecified multiplicity control for secondary epoch contrasts.

Report effect sizes and confidence intervals, not only significance. Present animal-level data rather than pooled-trial summaries alone.

---

## 5. Acceptance and stopping criteria

### Positive necessity claim requires all of the following

1. Anatomical targeting and Q optical placement meet prespecified criteria.
2. Functional calibration demonstrates reversible suppression at the final light parameters.
3. Opsin animals show a prespecified detrimental cue-window effect relative to their no-light trials.
4. That effect is significantly or credibly larger than the corresponding reporter-light effect.
5. Completion, movement initiation and locomotion do not show a comparable treatment-induced deficit.
6. The cue-window effect is larger than effects from intertrial and locomotion-control epochs.
7. Visible light is either nondetectable behaviorally in reporter animals or adequately removed by the double-difference comparison.
8. Findings replicate across sessions and, preferably, independent cohorts.
9. Cue sensory-probe results do not show a comparable impairment; otherwise the conclusion must be broadened to “cue processing/retrieval.”

### Stop or do not make the causal claim if

- functional suppression cannot be demonstrated;
- expression or optical placement fails prespecified quality control;
- stable task performance cannot be restored after surgery;
- no reliable movement-free retrieval window can be created;
- visible-light exposure cannot be matched or adequately controlled;
- the manipulation causes major omissions or locomotor disruption;
- manipulation coverage is too limited for a negative result to be informative.

For a negative conclusion, also require adequate animal-level precision and verified pathway coverage. Otherwise report “no detected effect,” not “P→Q is unnecessary.”

---

## 6. Troubleshooting

| Problem | Recommended action |
|---|---|
| No behavioral effect | Verify expression, terminal placement, functional suppression, illumination timing and bilateral/relevant pathway coverage. Adjust only through a new calibration plan; do not infer non-necessity from an unvalidated manipulation. |
| Reporter animals respond to light | Improve opaque shielding, use matched external visual masking and repeat sensory calibration. If the effect persists, rely on the virus × light interaction and state the residual visual limitation. |
| Cue light reduces response completion or speed | Shorten the window to end earlier, introduce or lengthen a pre-go hold, and compare against a locomotion-control epoch. Do not claim selective retrieval necessity. |
| High premature-movement or abort rates | Recalibrate hold duration and movement thresholds using baseline data. Analyze aborts as outcomes rather than deleting them. |
| Effect occurs during both cue and intertrial epochs | Suspect persistent suppression, arousal or sensory effects. Reduce cumulative exposure and increase washout after calibration. |
| Effect is accompanied by impaired cue detection | Classify the pathway as necessary for cue processing or cue-guided behavior, not selective retrieval. |
| Expression reaches P neurons with collaterals to the other region | Use terminal illumination in Q, quantify collateral overlap and, if possible, test whether the other projection is affected. |
| Large behavioral variability | Increase the number of animals and repeated sessions based on animal-level variance; do not treat additional trials as independent animals. |

## Principal limitation

Even with these controls, a positive result demonstrates that P→Q activity during the defined window is necessary for normal cue-guided choice in this task. It does not by itself prove that P→Q represents the retrieved rule, excludes contributions from other pathways, or generalizes to other task timings. Conversely, a negative result may reflect incomplete inhibition, pathway compensation or insufficient coverage rather than true non-necessity.
