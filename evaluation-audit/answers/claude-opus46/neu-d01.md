# Claude Opus 4.6 / neu-d01

Original final answer, shared by both scoring rounds.

# Optogenetic Test of Projection P→Q Necessity During Cue Retrieval

---

## 1. CONCLUSION AND RECOMMENDED DESIGN

**Lead conclusion:** A pathway-specific inhibitory opsin strategy, combined with epoch-restricted illumination locked to cue presentation and multiple control conditions, can isolate the contribution of the P→Q projection to cue-guided choice while ruling out motor, sensory, and nonspecific light confounds. The critical design features are: (i) retrograde targeting of the opsin to P neurons that project to Q (addressing O1/O2), (ii) restricting photoinhibition to a defined cue-retrieval epoch rather than the full trial (dissociating choice from locomotion, addressing O3), (iii) a masked-light control to neutralise visible-light artefacts (addressing O4), and (iv) an opsin-negative illuminated control to distinguish photothermal/photochemical effects from opsin-mediated silencing.

---

## 2. SCIENTIFIC ARGUMENT

### 2.1 Rationale and evidence-to-inference chain

| Evidence | Inference | Design consequence |
|---|---|---|
| O1: P projects to Q **and** to another region | Whole-cell silencing of P would disrupt both pathways; necessity of P→Q cannot be isolated without projection-specific targeting | Use retrograde viral strategy to restrict opsin to P→Q neurons only |
| O2: Inhibitory opsin can be targeted to P→Q neurons | Projection-specific loss-of-function is technically feasible | Inject retrograde-Cre virus in Q, Cre-dependent opsin AAV in P |
| O3: Task requires locomotion as well as correct choice | Any performance deficit could reflect a motor rather than a cognitive (cue-retrieval) impairment | Restrict illumination to cue epoch; measure locomotor metrics independently; include a locomotion-only control epoch |
| O4: Light delivery is visible to the animal | Animal may use light onset as a secondary cue or show startle/avoidance, confounding choice behaviour | Provide constant masking illumination on every trial; use opsin-negative illuminated controls |

### 2.2 Core logic

* **Necessity claim:** If photoinhibition of P→Q during cue presentation impairs choice accuracy but not locomotion, and this impairment is absent in opsin-negative controls receiving identical light, then the P→Q projection is necessary for cue retrieval.
* **Alternative explanations to exclude:**
  1. *Motor confound*: Deficit is locomotor, not cognitive → addressed by epoch restriction and locomotor assays.
  2. *Sensory confound (visible light)*: Animal detects laser onset → addressed by ambient masking light and opsin-negative group.
  3. *Off-pathway confound*: Silencing P neurons disrupts P→other-region pathway → addressed by projection-specific opsin expression (O1, O2).
  4. *Photothermal tissue damage*: Heat from fibre impairs local tissue → addressed by opsin-negative illuminated control and power calibration.
  5. *State/arousal confound*: Inhibiting P→Q changes global arousal → partially addressed by comparing performance on non-cue epochs and by reaction-time distributions.

---

## 3. OPERATIONAL PROTOCOL

### Phase A — Preparation and Quality Checks

**A1. Viral strategy**

1. Inject a retrograde-transport virus encoding Cre recombinase (e.g., AAVretro-Cre) into region Q.
2. Inject a Cre-dependent inhibitory opsin virus (e.g., AAV-DIO-eNpHR3.0-eYFP or AAV-DIO-GtACR1-FusionRed) into region P.
3. For the **opsin-negative control group**, inject AAVretro-Cre into Q and AAV-DIO-eYFP (fluorophore only, no opsin) into P.
4. Allow ≥4 weeks for anterograde expression; exact duration should be calibrated by a pilot cohort killed at 3, 4, 5, and 6 weeks and assessed for terminal fluorescence in Q and soma fluorescence in P.

**A2. Fibre-optic implant**

* Implant optical fibre (200 µm core, 0.39 NA) with tip aimed at P, dorsal to the labelled somata.
* Rationale: Illuminating somata in P silences their output to Q. Illuminating terminals in Q is an alternative but risks backpropagating effects and inconsistent silencing efficacy; somatic inhibition is preferred given O2.

**A3. Expression verification plan (pre-experiment)**

* In a subset of pilot animals (not used behaviourally), verify:
  - Opsin-expressing somata are restricted to P.
  - Fluorescent terminals are present in Q.
  - No detectable opsin expression in neurons that do not project to Q (sample ≥100 labelled neurons per animal; co-label with retrograde tracer from the other region P projects to; expect <5% overlap to confirm specificity; if overlap exceeds 5%, interpret results with the caveat of partial off-target silencing).

**A4. Light-power calibration**

* Measure irradiance at fibre tip in free space with an optical power meter before each surgical implantation.
* Target irradiance at the deepest labelled somata should be ≥1 mW/mm² for eNpHR3.0 (or the empirically determined EC₅₀ for the chosen opsin), but <15 mW/mm² to minimise photothermal effects. If the chosen opsin is GtACR1, lower powers suffice (~0.1–1 mW/mm²); calibration curve should be generated in a pilot electrophysiology experiment (see A5).
* Unknown parameter: exact power needed in this preparation. **Calibration procedure**: in 2–3 animals with opsin + an acutely inserted electrode near P somata, titrate laser power (0.1, 0.5, 1, 2, 5, 10 mW at fibre tip) and measure suppression of evoked or spontaneous firing. Choose the minimum power yielding ≥80% spike suppression sustained over the intended epoch duration.

**A5. Functional validation (acute electrophysiology pilot)**

* In ≥3 opsin-expressing animals, perform acute recordings in P during light delivery.
* Confirm: (a) rapid onset of firing suppression within 50 ms, (b) recovery within 500 ms of light offset, (c) no rebound excitation that outlasts the illumination epoch by >1 s.
* Confirm in opsin-negative animals that the same light produces no significant firing-rate change.

---

### Phase B — Independent Units and Allocation

**B1. Subjects**

* Species/strain matched to the task (e.g., mouse or rat, age- and sex-balanced).
* **Minimum sample**: power analysis based on expected effect size. If pilot data are unavailable, assume a medium effect (Cohen's d ≈ 0.8) for choice accuracy; for α = 0.05 (two-tailed) and power = 0.80, require n ≈ 26 per group. Adjust after interim look (see stopping rules).

**B2. Groups (between-subjects factor)**

| Group | Virus in Q | Virus in P | Light on cue epoch | Purpose |
|---|---|---|---|---|
| **Opsin + Light** | AAVretro-Cre | AAV-DIO-Opsin-FP | Yes | Test group |
| **FP + Light** | AAVretro-Cre | AAV-DIO-FP only | Yes | Controls for light/heat and surgical confound |
| **Opsin + No light** | AAVretro-Cre | AAV-DIO-Opsin-FP | No (fibre attached, masking light only) | Controls for opsin expression alone |

**B3. Within-subjects factor (epoch of illumination)**

For the Opsin + Light group, interleave three trial types in randomised blocks within a session:
* **Cue-epoch inhibition**: light ON during cue presentation only.
* **Movement-epoch inhibition**: light ON during the locomotion/response phase only (after cue offset, during approach/choice execution).
* **No-inhibition trials**: light OFF (masking light still present).

This within-subject comparison directly dissociates cue-retrieval from motor confounds (O3).

**B4. Blinding**

* Experimenter running behavioural sessions is blind to virus identity (opsin vs. FP). Virus aliquots are coded by a second person.
* Automated behavioural scoring (lick sensors, beam breaks, video tracking) removes scorer bias.
* Light delivery is automated and triggered by task events (TTL from behavioural system).

---

### Phase C — Behavioural Task

**C1. Task structure (learned choice with defined cue epoch)**

1. **Trial initiation**: animal occupies start position (detected by IR beam break).
2. **Cue presentation** (1–2 s): a sensory cue (e.g., auditory tone A vs. tone B, or visual cue left vs. right) indicates the correct choice port.
3. **Delay** (optional, 0–1 s): cue offset; animal must retain information.
4. **Go signal**: barrier opens or signal sounds; animal locomotes to one of two choice ports.
5. **Outcome**: correct choice → reward; incorrect → time-out.
6. Animals must reach a stable criterion (≥80% correct on 3 consecutive sessions) before entering the test phase, to ensure the behaviour is well learned and ceiling-level, making decrements detectable.

**C2. Masking-light solution (addressing O4)**

* A low-intensity LED of the same wavelength as the laser (or broad-spectrum ambient light that encompasses it) is mounted in the behavioural chamber and is **ON throughout every trial**, including inter-trial intervals.
* The laser light, delivered via the implanted fibre, is thus embedded in a background of the same wavelength. Because the fibre is implanted intracranially with minimal external light leakage, and the ambient masking light is always present, the onset of the laser cannot serve as a discriminative cue.
* Additionally, opaque dental cement and a ceramic ferrule sleeve should be used to minimise any light escaping from the fibre-ferrule junction.
* Verification: in a pilot cohort, compare lick latency and orientation behaviour on laser-ON vs. laser-OFF trials in opsin-negative animals. No significant difference confirms adequate masking.

---

### Phase D — Intervention and Sampling

**D1. Light delivery protocol**

* **Cue-epoch inhibition trials**: Laser turns ON 100 ms before cue onset (to ensure suppression is established by cue time) and turns OFF at cue offset (or at go signal if a delay is included).
* **Movement-epoch inhibition trials**: Laser turns ON at go signal and OFF when the animal reaches a choice port or after a maximum duration (e.g., 5 s).
* **No-inhibition trials**: Laser remains OFF; fibre is connected; masking light is on.
* Trial types are pseudo-randomly interleaved (no more than 3 consecutive trials of one type) within a session to prevent strategic adaptation.

**D2. Session structure**

* Each test session: ≥120 trials (≥40 per trial type).
* Conduct ≥3 test sessions per animal (total ≥360 trials/animal) to achieve stable estimates.
* Preceding each test session, run 20 warm-up trials with no inhibition (data excluded) to confirm baseline performance is at criterion.

---

### Phase E — Measurements

| Measure | Purpose | How recorded |
|---|---|---|
| **Choice accuracy** (% correct) | Primary outcome — cue retrieval | Beam-break/lick sensor at choice ports |
| **Reaction time** (cue onset → movement initiation) | Detect processing-speed vs. accuracy dissociation | Video tracking or beam-break latency |
| **Locomotion speed** (start → choice port) | Motor confound check | Video tracking (cm/s) |
| **Latency to initiate trial** | Motivation/arousal check | IR beam at start position |
| **Choice bias** (proportion left vs. right regardless of cue) | Detect side bias introduced by inhibition | Derived from choice data |
| **Omission rate** (trials without a response) | Detect gross motor or motivational deficit | Timeout counter |

---

### Phase F — Controls Summary

| Control | What it rules out |
|---|---|
| Opsin-negative + light (FP + Light group) | Photothermal/photochemical effects, visible-light artefact |
| Opsin-positive + no light (Opsin + No light group) | Viral toxicity, chronic opsin expression effects |
| Movement-epoch illumination (within-subject) | General motor/motivational impairment from P→Q silencing |
| Masking ambient light | Discriminative cue from laser onset (O4) |
| Retrograde specificity check (histology) | Off-target silencing of P→other-region neurons (O1) |

---

### Phase G — Analysis Plan

**G1. Primary analysis**

* Mixed-model logistic regression (or generalised linear mixed model, GLMM) with:
  - Fixed effects: Group (Opsin+Light, FP+Light, Opsin+NoLight) × Epoch (Cue, Movement, None).
  - Random effects: Animal (intercept and slope).
  - Dependent variable: trial-level binary choice (correct/incorrect).
* The critical contrast is: Opsin+Light during Cue epoch vs. all other conditions. A significant decrease in accuracy specifically in this cell supports necessity of P→Q for cue retrieval.

**G2. Motor confound analysis**

* Compare locomotion speed and reaction time across conditions using linear mixed models. If cue-epoch inhibition decreases accuracy but does **not** decrease locomotion speed or increase omissions, the motor-confound explanation is disfavoured.
* If movement-epoch inhibition impairs locomotion but not accuracy, this further dissociates motor from cognitive roles.

**G3. Sensory confound analysis**

* Compare FP+Light group accuracy across laser-ON vs. laser-OFF trials. No difference confirms light alone does not alter behaviour.

**G4. Effect-size estimation**

* Report odds ratios with 95% confidence intervals for the critical contrast, alongside Cohen's h for the accuracy difference.

**G5. Corrections**

* Adjust for multiple comparisons (e.g., Holm–Bonferroni) across the pre-specified contrasts.

---

### Phase H — Acceptance and Stopping Criteria

**H1. Inclusion criteria (per animal)**

* Histological confirmation of opsin expression in P somata and terminals in Q (post-hoc).
* Fibre tip within 300 µm of labelled somata (verified by histology).
* Baseline (no-inhibition) accuracy ≥75% during test sessions.
* Animals failing any criterion are excluded; exclusions are reported but data are also analysed with them included as a sensitivity check.

**H2. Interim analysis and stopping rule**

* After 50% of animals are tested, perform a pre-registered interim analysis with a Lan-DeMets (O'Brien–Fleming) spending function. Stop early for overwhelming efficacy (p < 0.005 at interim) or futility (conditional power < 10%).

**H3. Positive-result criterion**

* The P→Q projection is deemed necessary for cue retrieval if:
  1. Cue-epoch inhibition in the Opsin+Light group reduces accuracy significantly below both the FP+Light cue-epoch condition and the Opsin+Light no-inhibition condition (interaction p < 0.05 after correction).
  2. Movement-epoch inhibition does not produce a comparable accuracy deficit (ruling out a general behavioural disruption).
  3. Locomotion speed and omission rate are not significantly impaired during cue-epoch inhibition (ruling out motor confound).

**H4. Negative-result interpretation**

* No accuracy deficit → either P→Q is not necessary for cue retrieval, or the inhibition was insufficient. Distinguish by verifying (from pilot electrophysiology or post-hoc optrode recordings) that firing was indeed suppressed. If suppression was confirmed, accept the negative result. If not, the experiment is inconclusive.

---

### Phase I — Troubleshooting

| Problem | Diagnostic | Remedy |
|---|---|---|
| No behavioural deficit in any condition | Check expression (histology), check fibre placement, check laser output | Re-calibrate power; if expression/placement verified, accept negative result |
| Deficit in both cue and movement epochs | May indicate P→Q is needed for both processes, or a general arousal role | Add a free-locomotion assay (open field) with inhibition to test arousal; lengthen delay between cue and movement to better separate epochs |
| Deficit in FP+Light control | Light/heat artefact | Reduce power; increase fibre–tissue distance; switch to red-shifted opsin requiring lower power |
| Animal detects laser (bias shift in FP+Light group on light trials) | Masking light insufficient | Increase ambient masking-light intensity; add opaque shielding around ferrule; re-test |
| Low expression or retrograde labelling | Weak fluorescence in pilot cohort | Titrate viral titre upward; extend expression time; try alternative retrograde serotype |
| Rebound excitation after light offset contaminates choice epoch | Electrophysiology shows post-inhibition rebound | Use step-down ramp at light offset; or use chloride-conducting opsin (GtACR1/2) with confirmed absence of rebound |
| Fibre damage or degradation over sessions | Decreasing baseline performance across sessions | Monitor laser output before each session; replace patch cable if output drops >20% |

---

## 4. LIMITS AND UNCERTAINTIES

1. **Sufficiency is not tested.** This design tests necessity only. A complementary gain-of-function experiment (activating P→Q during an ambiguous cue) would address sufficiency.
2. **Temporal resolution of epoch dissociation.** If the cue and movement epochs partially overlap (e.g., the animal begins moving during the cue), the dissociation is weakened. A task design with an enforced delay between cue offset and go signal mitigates this but introduces a working-memory component, changing the cognitive demand.
3. **Incomplete silencing.** If only a fraction of P→Q neurons express the opsin, residual activity may sustain function, yielding a false negative. Quantifying the fraction of retrogradely labelled neurons that co-express opsin is essential for interpretation.
4. **Collateral branches (O1).** Even with retrograde Cre targeting, the opsin is expressed in the soma and all axon branches. If the P→Q neuron also sends a collateral to the "other region" mentioned in O1, somatic inhibition will silence that collateral too. This is an inherent limitation of somatic inhibition. Terminal illumination in Q would avoid this but introduces its own confounds (antidromic effects, incomplete silencing of en-passant fibres). The degree to which P→Q neurons also project elsewhere should be quantified histologically (dual retrograde tracing) and reported.
5. **Ecological validity of the masking-light solution.** Constant ambient light may itself alter arousal or visual processing. The opsin-negative illuminated control group accounts for this, but comparing behaviour before and after introduction of the masking light confirms it does not shift baseline performance.

---

## 5. EVIDENCE-TO-CONCLUSION MAP (Summary)

```
O2 (projection-specific opsin) ──► retrograde Cre strategy ──► silencing restricted to P→Q
O1 (P projects elsewhere too) ──► projection-specific targeting required ──► same strategy;
                                    acknowledge collateral caveat
O3 (task requires locomotion) ──► epoch-restricted inhibition + locomotor measures
                                    ──► cue-epoch deficit without motor deficit = cognitive necessity
O4 (light visible) ──► masking light + opsin-negative illuminated control
                       ──► no behavioural change in controls = artefact excluded

Combined: Accuracy deficit specific to (Opsin+Light × Cue epoch), absent in controls,
with intact locomotion ──► P→Q projection is necessary for cue retrieval.
```
