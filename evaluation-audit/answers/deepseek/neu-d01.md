# DeepSeek V4.1 Flash / neu-d01

Original final answer, shared by both scoring rounds.

## Recommended next action

Do not treat a reduction in correct choices as sufficient evidence that P→Q is necessary for cue retrieval. Use a **delayed-choice task** with a defined cue-retrieval epoch, inhibit **P→Q projection terminals locally in Q** during that epoch, randomize light-on/off trials within animal, include **opsin-negative lit controls**, and make **movement and sensory measures co-primary**. Accept a necessity claim only if the correct-choice deficit is retrieval-epoch-specific and cannot be explained by impaired locomotion or by the animal seeing/detecting the light.

If the existing learned-choice task cannot temporally separate cue retrieval from locomotion, add a delay between cue and go signal, or use closed-loop inhibition that ends before movement onset. If that is impossible, the experiment can still be run, but the conclusion will be weaker and should be framed as “P→Q manipulation during cue presentation/delay impairs performance,” not as a clean retrieval-specific necessity claim.

---

## Evidence-to-inference chain

| Evidence | Inference | Consequence for design |
|---|---|---|
| **O1:** P projects to Q and to another region. | Inhibiting all P neurons cannot isolate P→Q. A behavioral effect could reflect the other projection. | Target P→Q specifically. Prefer **terminal inhibition in Q** rather than somatic inhibition of all P neurons, especially if P→Q neurons may collateralize. |
| **O2:** Inhibitory opsin expression can be targeted to P neurons projecting to Q. | The intervention is feasible in principle. | Use projection-specific targeting. Verify expression and function; do not assume targeting worked. |
| **O3:** The proposed outcome is correct choices, but the task also requires locomotion. | A correct-choice deficit may be motor, motivational, or locomotor, not retrieval. | Measure movement independently; separate retrieval and movement epochs; include movement-only inhibition controls. |
| **O4:** Light delivery can be visible to the animal. | Light itself may act as a sensory cue, distractor, or aversive stimulus. | Include opsin-negative lit controls, make light non-predictive, and calibrate for sensory/behavioral effects of light alone. |

**Core inference:** If inhibition of P→Q during the cue-retrieval epoch reduces correct choices, while (i) opsin-negative lit controls show no equivalent deficit, (ii) movement metrics are unchanged or cannot account for the choice deficit, and (iii) inhibition during movement alone does not produce the same pattern, then P→Q is necessary for cue retrieval in this task. If any of those controls fail, the result is inconclusive.

---

## Operational protocol

### 1. Preparation and quality checks

**1.1 Define the task and epochs operationally.**
Use or create a learned choice task with a discrete cue, a retrieval/delay period, and a movement/response period. Define:
- **Cue-retrieval epoch:** cue onset through the end of the delay or the go signal. Inhibit P→Q only here.
- **Movement epoch:** go signal through response completion. Inhibit P→Q here only in movement-control sessions/trials.
- **Inter-trial interval:** no light.

If the existing task has no delay, add one, because otherwise cue retrieval and movement overlap and the confound cannot be resolved cleanly.

**1.2 Targeting and expression.**
Use a projection-specific strategy consistent with O2. For example, a retrograde Cre approach from Q combined with a Cre-dependent inhibitory opsin in P, or another validated projection-targeting method.  
**Unreported parameters:** opsin type, promoter, viral vector, titer, injection coordinates, light wavelength, power, and pulse protocol. Do not invent these. Calibrate them.

**1.3 Histological and functional quality checks.**
- Verify opsin expression in P neurons that project to Q using retrograde tracing plus opsin immunostaining or reporter expression.
- Check for off-target expression in P neurons that do not project to Q or in nearby regions.
- If P→Q neurons may collateralize to the other region named in O1, use **terminal inhibition in Q** rather than somatic inhibition in P. This isolates release at Q.
- Functionally validate inhibition in vitro or in vivo. In vitro: light should reduce firing of P→Q neurons or reduce terminal release. In vivo: if possible, measure downstream Q activity or a known P→Q-dependent physiological signal.  
**Calibration procedure:** vary light power and duration to find the minimum that produces reliable inhibition without tissue damage or spreading excitation. Use the same calibration for all animals.

**1.4 Implants and light delivery.**
Implant fiber optics aimed at Q terminals or P somata, depending on strategy. Verify placement histologically. Measure light power at the fiber tip before and after behavior.  
Because **O4** states light can be visible, assume it is visible unless you have independently validated otherwise. Use opaque shielding around the fiber and animal head where possible, but do not rely on invisibility.

**1.5 Behavioral training and light habituation.**
Train animals to stable performance before surgery or before testing. Predefine stability (e.g., a performance criterion and a minimum number of sessions; the exact criterion is unreported and should be set from pilot data).  
Habituate animals to non-predictive light presentations before the main test so that novelty does not dominate. Calibrate cue timing, movement onset latency, and response duration for each animal.

**1.6 Sensory calibration.**
In opsin-negative animals with identical implants, deliver the same light schedule. Measure correct choices, latency, movement speed, trial initiation, licking, and any orienting response to light. If light alone changes behavior, adjust intensity, wavelength, shielding, or timing. If no adjustment removes the effect, the sensory confound remains and must be modeled or acknowledged.

---

### 2. Independent units, allocation, and blinding

**2.1 Independent units.**
- **Animal** is the independent unit for genotype/opsin allocation.
- **Session** and **trial** are nested within animal. Do not treat trials from the same animal as independent.
- If unilateral manipulation is used, a hemisphere may be an independent unit only if the two sides are independently allocated and do not interact. Otherwise use animal as the unit.
- Use mixed-effects models with animal and session as random effects.

**2.2 Allocation.**
Randomize animals to:
1. **Opsin group:** inhibitory opsin in P→Q neurons.
2. **Opsin-negative control group:** identical surgery, implants, and light exposure, but no inhibitory opsin (e.g., mCherry or empty vector).

Within each opsin animal, randomize light-on and light-off trials across the session, balanced by cue side, choice side, and reward outcome. Make light non-predictive of the correct choice.

**2.3 Blinding.**
Blind the surgeon, behavior experimenter, and analyst to genotype and condition where possible. Automated light delivery and automated behavioral scoring reduce bias. Pre-register the primary outcome, epochs, exclusion criteria, and analysis plan.

**2.4 Sample size.**
**Unreported:** expected effect size, variability, and task reliability. Do not guess. Run a pilot with the opsin group and opsin-negative controls to estimate effect size and variance. Then perform a power analysis for the primary mixed-effects test. Include enough animals to detect the pilot effect with the planned alpha and power, and enough trials per animal to estimate within-animal light effects.

---

### 3. Intervention and sampling

**3.1 Conditions.**
At minimum, include:
- **Opsin + retrieval light:** light during cue-retrieval epoch only.
- **Opsin + no light:** same animals, interleaved trials.
- **Opsin-negative + retrieval light:** sensory/opsin control.
- **Opsin + movement-only light:** light during movement epoch only, to test whether movement inhibition alone reproduces the deficit.
- If feasible, **opsin + light outside the task** or **opsin + light to a non-Q projection** to test specificity.

**3.2 Timing.**
Turn light on at cue onset and off before the go signal or before movement onset. If a delay exists, cover cue and delay. Confirm timing with a photodiode or light sensor and with behavioral timestamps. If inhibition persists into movement because of opsin kinetics, either shorten the light window or add a delay so that movement begins after light offset.

**3.3 Sampling.**
Interleave light-on and light-off trials pseudorandomly. Run multiple sessions per animal. Counterbalance light conditions across sessions. Collect trial-by-trial data:
- Correct/incorrect choice
- Omission
- Reaction time
- Movement onset time
- Movement speed or path length
- Trial initiation latency
- Licking or other consummatory measures
- Reward collection latency

Use video tracking and automated scoring where possible.

---

### 4. Measurements

**Primary outcome:** proportion of correct choices on retrieval-light trials versus no-light trials in the opsin group, compared with the opsin-negative lit control.

**Co-primary movement outcomes:** movement speed, movement onset latency, trial initiation latency, and omission rate. These are needed because of **O3**.

**Secondary outcomes:** choice latency, reward collection, licking, and any signs of aversion or orienting to light.

**Sensory-control outcome:** in opsin-negative animals, difference in correct choices, movement, and latency between light-on and light-off trials. A nonzero effect indicates a sensory/light confound.

**Quality-control outcomes:** histology, fiber placement, light power at tip, opsin expression, and functional inhibition.

---

### 5. Analysis

**5.1 Primary analysis.**
Use a mixed-effects logistic regression for correct choices, for example:
`correct ~ light * epoch * genotype + (1 | animal) + (1 | session)`  
or, within the opsin group:
`correct ~ light * epoch + (1 | animal) + (1 | session)`.

The key test is whether light during the retrieval epoch reduces correct choices in the opsin group more than in opsin-negative controls and more than movement-only light.

**5.2 Movement analysis.**
Use linear mixed-effects models for speed and latency:
`speed ~ light * epoch * genotype + (1 | animal) + (1 | session)`.

A necessity claim requires that movement metrics do not show a comparable light-induced impairment. If movement is impaired, use equivalence testing or mediation analysis to assess whether the choice deficit can be explained by movement. Predefine what magnitude of movement change would invalidate the retrieval interpretation.

**5.3 Sensory analysis.**
Test whether opsin-negative lit animals show a light effect. If they do, the sensory confound is present. Model it, adjust the light protocol, or weaken the conclusion.

**5.4 Specificity.**
If P→Q neurons may collateralize, terminal inhibition in Q is the cleaner test. If somatic inhibition is used, compare with inhibition of the other projection named in O1, if technically possible. If not possible, acknowledge the limitation.

---

### 6. Acceptance and stopping criteria

**Accept the necessity claim only if all of the following hold:**
1. Opsin expression and functional inhibition are verified.
2. Retrieval-epoch inhibition significantly reduces correct choices in the opsin group.
3. The effect is absent or much smaller in opsin-negative lit controls.
4. Movement metrics are unchanged, or any change cannot explain the choice deficit.
5. Movement-only inhibition does not produce the same pattern.
6. The effect replicates across sessions or independent cohorts.
7. Sensory controls show no equivalent light-alone effect.

**Stop or reinterpret if:**
- No effect is observed after an adequately powered sample.
- Movement is impaired enough to explain the choice deficit.
- Opsin-negative lit controls show a light-induced choice or movement effect.
- Histology shows poor targeting or off-target expression.
- Light spread or tissue damage is evident.

**Stopping rules:** predefine a maximum sample size, futility boundary, and toxicity/health stopping criteria. Do not stop early based on a transient effect without pre-registration.

---

### 7. Troubleshooting

| Problem | Likely cause | Action |
|---|---|---|
| No opsin expression | Targeting failure, titer, injection | Verify histology; re-calibrate targeting; use positive control. |
| No behavioral effect | Light power too low, fiber misplacement, opsin ineffective | Calibrate power, verify placement, test opsin function in vitro. |
| Movement impairment | Inhibition spread to motor circuits or somatic P neurons | Use terminal inhibition in Q; reduce light duration/intensity; add delay. |
| Sensory/light effect | O4: light visible | Use opsin-negative lit controls; make light non-predictive; adjust shielding/wavelength; if unavoidable, model as confound. |
| Collateral projection effect | P→Q neurons also project elsewhere (O1) | Inhibit terminals in Q only; avoid somatic inhibition of all P. |
| Inconsistent effect | Trial variability, timing, state | Increase trials; randomize; measure state variables; use within-session comparisons. |
| Light spread | High power, large fiber | Use lower power, smaller fiber, local delivery; measure spread with immediate-early gene or electrophysiology if possible. |

---

## Alternatives and limits

**Alternative explanations to rule out:**
- **Sensory cue processing:** P→Q may be needed to perceive or attend to the cue, not to retrieve it. Inhibit after cue offset during a delay to isolate maintenance/retrieval.
- **Motivation/reward:** P→Q may affect reward value or motivation. Measure reward collection and include reward-only inhibition controls.
- **Movement:** O3 requires locomotion. Separate epochs and measure movement.
- **Light visibility:** O4 means light may be a cue or distractor. Opsin-negative lit controls and non-predictive light are essential.
- **Collateral projections:** O1 means P→Q may not be the only relevant P output. Terminal inhibition at Q is preferred.

**Limits:**
- Necessity is not sufficiency. This design tests whether P→Q is required, not whether it is enough.
- Projection-specific targeting may still have off-target expression.
- If light is visible and cannot be masked, a sensory confound may remain.
- The exact opsin, light parameters, task timing, effect size, and sample size are unreported. Use calibration and pilot data rather than assuming values.
- If the task cannot separate cue retrieval from movement, the conclusion should be limited accordingly.

**Bottom line:** The strongest feasible test is projection-specific terminal inhibition of P→Q in Q during a discrete cue-retrieval epoch, with randomized light-on/off trials, opsin-negative lit controls, movement-only inhibition controls, and co-primary movement/sensory measures. Claim necessity only if the choice deficit is retrieval-specific and movement and sensory confounds are excluded.
