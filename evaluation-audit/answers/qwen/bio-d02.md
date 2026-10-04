# Qwen3.8 Max (0902) / bio-d02

Original final answer, shared by both scoring rounds.

## Recommended next action and main conclusion

**Proceed with a proposed, calibrated fractionation–reconstitution assay whose decisive comparison is:**

> **Retentate + native heat-stable filtrate/boiled-extract factor pool**  
> versus  
> **Retentate + a processed, volume-, pH-, salt-, phosphate-, protein-, substrate- and dilution-matched inactive analog lacking the candidate heat-stable organic factor.**

If the native heat-stable fraction restores fermentative activity while the matched inactive analog does not, and if heat controls show that the complementing activity is retained in the heated filtrate/boiled extract but destroyed in the retentate, the result would support the conditional conclusion that **a heat-stable, separable functional factor is required for fermentative activity in these yeast-juice fractions**. This conclusion would remain strictly functional. It would **not** establish chemical structure, purity, stoichiometry, or identity as NAD or any other named molecule.

**All experiments below are proposed; no experimental results are being reported.**

---

## Evidence-to-inference-to-conclusion chain

### Evidence from the supplied packet

1. **Separation and recombination evidence**  
   The supplied historical summary states that yeast-juice filtrate and retentate were separated, individually inactive, and active when recombined.  
   *Inference:* fermentative activity may require two separable components, one in the filtrate and one in the retentate.

2. **Boiled-extract compensation**  
   The summary states that boiled extract could compensate for the missing activity.  
   *Inference:* the compensated component may be heat-stable, because boiling did not destroy its ability to support activity.

3. **Stated limitation**  
   The packet explicitly says compensation does not determine chemical structure and does not alone establish NAD identity.  
   *Inference:* any conclusion must be functional, not structural.

4. **Named artifact alternatives**  
   The packet lists pH, inorganic salt, phosphate changes, dilution, enzyme damage, and nonspecific stabilization as alternative explanations.  
   *Inference:* the proposed protocol must hold these variables constant or monitor them directly.

### Proposed inference logic

The protocol tests whether activity is restored by the candidate heat-stable fraction **after all measured non-candidate variables have been matched**. The logic is:

- If **retentate + filtrate** is active, but **retentate + matched inactive analog** is not active, then activity is not explained solely by pH, matched salts, phosphate, protein amount, volume, dilution, or generic stabilization by matched protein.
- If **filtrate or boiled extract remains active after heating**, while **heated retentate does not support activity**, then the active complementing component is operationally heat-stable and separable from a heat-labile retentate component.
- If **retentate enzyme integrity** is verified by rescue with boiled extract or by an independent enzyme-integrity assay, then failure of retentate alone is less likely to be caused merely by enzyme damage.
- If independent separations give the same pattern, the inference is less likely to be an artifact of one separation run.

### Conditional conclusion

If all acceptance criteria are met, the defensible conclusion is:

> The data support the presence of a heat-stable, separable functional factor in the filtrate/boiled-extract pool that is required for fermentative activity in the reconstituted yeast-juice system.

If key controls fail, the conclusion must be weakened or rejected. In no case should the protocol be interpreted as proving that the factor is NAD, a nucleotide, a coenzyme, or any specific chemical species.

---

## Operational definitions

All terms are proposed.

- **YJFP**: yeast-juice-derived fermenting preparation.
- **R**: retentate or high-molecular-mass/enzyme-containing fraction.
- **F**: filtrate or low-molecular-mass candidate heat-stable factor fraction.
- **BE**: boiled extract supernatant, used as an independent heat-stable factor source.
- **DRB**: defined reconstitution buffer, formulated during calibration.
- **SF**: synthetic filtrate, an inactive analog matched for measured pH, buffer, ions, phosphate, protein, volume, and, if measured, fermentable substrate, but lacking the candidate heat-stable organic factor.
- **SBE**: synthetic boiled-extract analog, matched to BE for measured non-candidate variables but lacking the candidate factor.
- **FD**: optional factor-depleted filtrate, if a depletion method can be calibrated.
- **IP**: inert protein or other inert macromolecular matcher, used only after calibration shows it does not restore activity.

---

## Assumptions and unreported parameters

The following are assumed from the fixed packet:

- A yeast-juice-derived fermenting preparation can be fractionated into filtrate and retentate.
- Boiled extract and candidate fractions are available.
- The active factor has not been structurally identified.
- Exact buffer, ion, phosphate, protein, volume, and dilution values are unavailable.

Therefore, the following parameters are **not invented** but must be calibrated before hypothesis testing:

- Fermentative assay readout, temperature, mixing, linear time window, and substrate condition.
- Buffer species and concentration.
- pH target and acceptable pH tolerance.
- Ion composition and concentration targets.
- Phosphate concentration target.
- Protein concentration targets and matching tolerances.
- Fractionation cutoff, method, time, temperature, and recovery criteria.
- Heat-treatment conditions for boiled extract and heated fractions.
- Acceptable activity-recovery window.
- Statistical thresholds and minimum biologically meaningful effect size.

All calibration decisions should be fixed before unblinded analysis of the primary contrast.

---

# Proposed ordered protocol

## 1. Preparation and calibration phase

### 1.1 Calibrate the fermentative activity assay

**Objective:** establish a quantitative, linear, reproducible assay for fermentative activity.

Proposed steps:

1. Choose one primary activity readout. Options include:
   - CO₂ production, preferred if continuous or frequent sampling is feasible;
   - ethanol formation;
   - fermentable sugar disappearance.
   
   The chosen readout should have a low blank and a linear initial-rate window.

2. Determine the linear range:
   - Test several YJFP protein or volume levels.
   - Test several time points.
   - Select a time window in which signal is linear with time and amount.

3. Calibrate substrate conditions:
   - Measure or estimate fermentable carbohydrate in whole preparation and fractions, if feasible.
   - Either add a defined fermentable substrate to all tubes at a saturating or near-saturating level, or match substrate across all treatments.
   - This prevents the filtrate from appearing active merely because it supplies fermentable substrate.

4. Define blank and background:
   - DRB plus substrate without yeast-juice material.
   - Heat-inactivated preparation, if compatible with the assay.
   - Substrate-only and fraction-only blanks.

5. Define assay acceptance:
   - Whole preparation positive control must produce a rate clearly above blank.
   - Technical variability should be low enough to detect the pre-specified effect size.
   - If no linear range can be found, stop and revise the assay before fractionation studies.

### 1.2 Calibrate defined buffer and ion add-back

**Objective:** remove pH, salt, phosphate, and buffer-composition artifacts.

Proposed steps:

1. Measure, at assay temperature where possible:
   - pH of whole YJFP, pilot R, pilot F, and BE.
   - Conductivity.
   - Phosphate, if measurable.
   - Major cations and anions, if measurable.
   - Osmolality or dry-mass estimate, if feasible.

2. Select a defined buffer system:
   - Test candidate buffer species for compatibility with whole YJFP activity.
   - Prefer a buffer that does not itself supply phosphate if phosphate is being tested as a possible confounder.
   - If phosphate is required for activity or the native system is phosphate-buffered, then phosphate must be treated as a matched variable and included in all relevant treatments.

3. Prepare DRB:
   - Fixed buffer species and concentration, selected by calibration.
   - pH adjusted to the calibrated target.
   - Ion add-back stocks added to match measured or conductivity-matched ionic composition.
   - Phosphate add-back, if required, matched across treatments.

4. Prepare explicit ion/phosphate controls:
   - DRB with matched ions but no phosphate.
   - DRB with matched phosphate but no other ion add-back, if meaningful.
   - DRB with full ion/phosphate add-back.
   - R plus ion/phosphate add-back but no candidate organic factor.

5. Acceptance:
   - pH after final mixing should be within the pre-defined tolerance.
   - Conductivity and phosphate should be matched across primary comparison tubes.
   - If exact ion matching is impossible, use conductivity and pH matching and record the limitation.

### 1.3 Calibrate protein, volume, and dilution matching

**Objective:** exclude dilution, protein concentration, and nonspecific protein-stabilizer artifacts.

Proposed steps:

1. Calibrate a protein assay for yeast-juice material.
2. Measure protein in:
   - Whole YJFP.
   - R.
   - F.
   - BE.
3. Define the amount of R protein to be used in each assay tube.
4. Keep final reaction volume identical in all tubes.
5. If F contributes non-negligible protein, prepare protein-matched inactive analogs:
   - Add an inert protein, IP, to SF or SBE at the same measured protein concentration.
   - Test IP alone and IP plus R.
   - Use at least two inert protein matchers if feasible, to reduce the chance that one nonspecific stabilizer explains the result.
6. Run dilution controls:
   - Whole YJFP diluted to the same total protein and volume as the reconstituted R+F mixture.
   - R alone at the same protein concentration as in reconstitution.
   - F alone at the same concentration as in reconstitution.
7. Acceptance:
   - Inert protein matchers should not restore activity by themselves.
   - Dilution of whole preparation should not create a false-positive or false-negative pattern within the selected working range.

### 1.4 Calibrate heat controls and boiled extract

**Objective:** define heat-stable and heat-labile behavior without allowing heat-induced pH/salt changes to confound interpretation.

Proposed steps:

1. Define a heat treatment for BE and heated F:
   - The treatment should abolish fermentative activity of whole extract or BE alone, if BE contains heat-labile enzymes.
   - The treatment should preserve the ability of BE or F to complement R, if the candidate factor is heat-stable.

2. After heating:
   - Clarify if precipitation occurs.
   - Re-measure pH, conductivity, and volume.
   - Adjust back to matched conditions if heating changed them.

3. Verify:
   - BE alone is inactive.
   - Heated F alone is inactive.
   - R + heated F is active if the factor is heat-stable.
   - Heated R + F is inactive, showing that the retentate component required for activity is heat-labile.

4. Acceptance:
   - If heating F destroys complementing activity, the protocol cannot support a heat-stable factor under those conditions.
   - If heated R plus F is active, heating may have released or preserved an activity that confounds the interpretation; stop or revise.

### 1.5 Calibrate enzyme-integrity monitoring

**Objective:** distinguish “missing factor” from “damaged retentate enzymes.”

Proposed monitoring strategy:

1. **Functional rescue control**:
   - R + BE should restore activity if R contains sufficient heat-labile enzymatic capacity and BE supplies the heat-stable factor.
   - If R + BE is inactive, R may be damaged, BE may lack factor, or matching may be inadequate.

2. **Independent enzyme-integrity assay**, if available:
   - Select a retentate-retained enzyme activity that can be assayed independently of the candidate factor.
   - Compare native R, heated R, and whole preparation.
   - This is optional but strengthens the inference.

3. **Preincubation stability check**:
   - Preincubate R with DRB, SF, or F for a short defined period.
   - Then add a saturating factor source, such as BE, to all tubes and measure activity.
   - If F or an inert stabilizer merely protects damaged enzymes, preincubation effects may differ from immediate complementation.

4. Acceptance:
   - R must be demonstrably capable of activity when supplied with a valid heat-stable factor source.
   - If no enzyme-integrity evidence can be obtained, the conclusion must be limited.

---

## 2. Independent separation and preparation of fractions

### 2.1 Independent experimental units

**Objective:** avoid dependence on one accidental separation artifact.

Proposed design:

1. Perform at least three independent fractionation runs.
   - These may be independent biological preparations, independent days, or independent operators.
   - Each independent separation is an experimental unit.

2. If feasible, include an orthogonal separation:
   - A second size-based method with a different retention principle or cutoff.
   - The purpose is to show that the complementing activity tracks the same operational fraction, not a device-specific artifact.

3. Record for each separation:
   - Starting volume and protein.
   - Retentate volume and protein.
   - Filtrate volume and protein.
   - Recovery of total material.
   - Any visible precipitation or color change.

### 2.2 Fractionation procedure, proposed

1. Clarify YJFP by gentle removal of particulate matter, using conditions calibrated not to remove activity.
2. Separate into:
   - R, the retentate or high-molecular-mass fraction.
   - F, the filtrate or low-molecular-mass fraction.
3. Keep all operations gentle and consistent:
   - Temperature, time, and handling should be fixed by calibration.
   - Avoid conditions known to damage enzymes unless specifically being tested.
4. Reserve aliquots of:
   - Unfractionated whole YJFP.
   - R.
   - F.
   - BE.
   - Flow-through or wash fractions, if useful for mass balance.

### 2.3 Buffer exchange and fraction adjustment

For R:

1. Exchange R into DRB if compatible with enzyme integrity.
2. Adjust pH, conductivity, phosphate, and ions to target values.
3. Adjust R protein concentration to the defined assay target.

For F:

1. Do not perform a buffer exchange that would lose the candidate factor unless pilot calibration shows acceptable recovery.
2. If needed, adjust F by adding concentrated DRB components, salts, phosphate, or buffer, rather than by dialysis that could remove a small factor.
3. If concentration is needed, use a method calibrated to retain complementing activity.

For BE:

1. Prepare BE using the calibrated heat treatment.
2. Clarify and adjust pH, conductivity, phosphate, ions, volume, and protein-related variables to match the corresponding native fraction.

---

## 3. Preparation of inactive analogs

### 3.1 Synthetic filtrate, SF

SF is proposed as the main inactive analog for F.

SF should contain:

- DRB at the same buffer concentration.
- Same pH.
- Same ion add-back profile.
- Same phosphate concentration.
- Same final volume contribution as F.
- Same fermentable substrate concentration, if substrate is being matched rather than universally added.
- Same inert protein concentration, if F contributes protein and protein matching is required.

SF should **not** contain yeast-juice low-molecular-mass organic material or the candidate heat-stable factor.

### 3.2 Synthetic boiled-extract analog, SBE

SBE should match BE for:

- pH.
- Buffer.
- Ions.
- Phosphate.
- Conductivity.
- Protein or inert protein content.
- Volume.
- Substrate, if relevant.

SBE should lack the boiled-extract heat-stable factor pool.

### 3.3 Optional factor-depleted filtrate, FD

If a depletion method can be calibrated, prepare FD by removing complementing activity from F while preserving measured pH, salt, phosphate, protein, and volume as closely as possible.

Possible approaches, all proposed and requiring calibration:

- Gentle adsorption.
- Ion-exchange or size-based subfractionation.
- Selective precipitation, if it does not destroy the system.

FD is useful only if:

- R + F is active.
- R + FD is inactive or strongly reduced.
- Adding back a small amount of active F restores activity.
- FD remains matched for pH, salt, phosphate, protein, substrate, and volume.

If depletion cannot be calibrated without changing these variables, do not use FD for the primary conclusion.

---

## 4. Allocation, blinding, and independent units

1. Assign each fractionation batch a code.
2. Randomize the order of assay treatments within each batch.
3. Use block allocation:
   - Each independent separation block should contain all key treatments.
4. Blind the analyst to treatment identity during measurement and initial data processing, if feasible.
5. Treat each independent separation, not each technical replicate, as the biological/experimental unit for the primary inference.

---

## 5. Reconstitution matrix and controls

The following treatment set is proposed. All tubes should have the same final volume and substrate condition.

| Code | Composition | Purpose |
|---|---|---|
| BLK | DRB + substrate only | Blank/background |
| W | Whole YJFP, matched dilution/protein | Positive system control |
| R | R alone | Test retentate alone |
| F | F alone | Test filtrate alone |
| R+F | R + native F | Main reconstitution test |
| R+SF | R + synthetic filtrate | Primary inactive-analog control |
| R+Fheat | R + heated F | Test heat stability of filtrate factor |
| Rheat+F | Heated R + F | Test heat lability of retentate component |
| R+BE | R + boiled extract | Historical heat-stable compensation control |
| R+SBE | R + synthetic boiled-extract analog | Inactive analog for boiled extract |
| BE | BE alone | Test boiled extract background |
| R+SF+IP | R + SF + inert protein matcher | Protein/stabilization control |
| R+ions/PO₄ | R + matched ions/phosphate, no organic factor | Salt/phosphate sufficiency control |
| W-dil | Whole YJFP diluted to reconstitution protein/volume | Dilution control |
| Optional: R+FD | R + factor-depleted F | Depletion test |
| Optional: R+FD+F add-back | R + FD + small active F add-back | Depletion/restoration test |

### Primary comparison

The primary quantitative contrast is:

> **R+F versus R+SF**

Both must be matched for pH, buffer, ions, phosphate, volume, total protein where feasible, dilution, and substrate.

### Secondary comparisons

- **R+BE versus R+SBE**: tests whether boiled extract contains a heat-stable complementing activity not explained by matched non-candidate variables.
- **R+Fheat versus R+F**: tests heat stability of the filtrate factor.
- **Rheat+F versus R+F**: tests heat lability of the retentate component.
- **R+ions/PO₄ versus R+SF**: tests whether matched salt/phosphate alone can account for activity.
- **R+SF+IP versus R+SF**: tests whether added inert protein or stabilization explains activity.

---

## 6. Intervention and sampling procedure

1. Pre-equilibrate all fractions and analogs to assay temperature.
2. Verify pH after mixing a representative set of tubes.
3. Assemble tubes in randomized order.
4. Start the reaction by adding substrate or by shifting to assay temperature, according to the calibrated assay design.
5. Sample at:
   - Time zero.
   - Multiple points within the calibrated linear range.
6. Stop or measure according to the chosen readout.
7. For destructive endpoints, use parallel tubes for each time point.
8. For continuous CO₂ measurement, record rate over the linear interval.
9. Reserve parallel tubes for post-assay checks:
   - pH.
   - Conductivity, if needed.
   - Protein, if needed.
   - Enzyme-integrity marker, if available.

---

## 7. Measurements

### 7.1 Primary fermentative measurement

Measure the pre-selected primary endpoint:

- CO₂ production, or
- ethanol formation, or
- substrate disappearance.

Use initial rates, not endpoint values alone, unless calibration shows endpoint values are equivalent.

### 7.2 Matching verification

For representative tubes or separate parallel mixtures, measure:

- pH.
- Conductivity.
- Phosphate, if feasible.
- Total protein.
- Final volume by construction and verification.
- Substrate concentration, if substrate matching is used instead of universal substrate addition.

### 7.3 Enzyme-integrity measurements

Measure:

- R + BE rescue activity.
- Optional independent retentate enzyme marker.
- Preincubation stability, if included.
- Comparison of native R and heated R in appropriate controls.

### 7.4 Fractionation quality measurements

Record:

- Protein recovery.
- Volume recovery.
- Activity recovery in reconstituted R+F relative to whole.
- Any loss of activity during buffer exchange or concentration.

---

## 8. Quantitative analysis and primary contrast

### 8.1 Rate calculation

For each tube:

1. Subtract blank signal where appropriate.
2. Fit the initial linear segment to obtain velocity, v.
3. Normalize as pre-specified:
   - per unit R protein, or
   - per fixed final volume, or
   - both, with the primary analysis fixed before unblinding.

### 8.2 Primary contrast

Define:

\[
C_{primary} = v(R+F) - v(R+SF)
\]

A normalized factor-dependence index may also be calculated:

\[
FDI = \frac{v(R+F) - v(R+SF)}{v(W) - v(BLK)}
\]

The primary conclusion depends on \(C_{primary}\), not on any single qualitative observation.

### 8.3 Secondary contrasts

Define:

\[
C_{BE} = v(R+BE) - v(R+SBE)
\]

Heat-stability ratio:

\[
H_F = \frac{v(R+F_{heat})}{v(R+F)}
\]

Heat-lability ratio:

\[
H_R = \frac{v(R_{heat}+F)}{v(R+F)}
\]

Inorganic/protein sufficiency checks:

\[
v(R+SF),\quad v(R+ions/PO_4),\quad v(R+SF+IP)
\]

should remain near background if the factor hypothesis is supported.

### 8.4 Statistical model

A proposed model:

- Treatment as fixed effect.
- Independent separation batch as random effect or blocking factor.
- Primary contrast estimated with confidence interval.
- Technical replicates used only to estimate within-tube measurement error, not to replace independent separations.

Predefine a minimum meaningful effect size during calibration, for example a value based on blank variability and whole-control rate. The threshold should be set before examining the primary contrast.

---

## 9. Acceptance and stopping criteria

### 9.1 Calibration acceptance

Proceed only if:

1. Whole YJFP gives a robust, linear fermentative rate.
2. Blank rates are low and stable.
3. pH, conductivity, phosphate, protein, and volume matching can be achieved within calibrated tolerances.
4. Inert protein matchers do not restore activity.
5. Heat treatment produces a BE that is inactive alone but capable of complementing R.
6. Fractionation yields acceptable recovery and does not grossly damage R.

### 9.2 Fractionation acceptance

Proceed only if:

1. R alone and F alone are individually low or inactive under matched conditions.
2. R+F restores activity relative to R alone.
3. The reconstituted activity is reproducible across independent separations.
4. R+BE rescue demonstrates that R retains enzymatic competence.

### 9.3 Hypothesis-test acceptance

The factor interpretation is supported only if all of the following are observed:

1. \(C_{primary} > 0\) by the pre-specified meaningful margin.
2. R+SF does not restore activity.
3. Matched ion/phosphate/protein controls do not restore activity.
4. R+Fheat remains active or nearly active, supporting heat stability of the filtrate factor.
5. Rheat+F is inactive or strongly reduced, supporting heat lability of the retentate component.
6. R+BE is active relative to R+SBE, if BE is used as the independent factor source.
7. Enzyme-integrity monitoring indicates that R is not simply damaged.
8. Independent separations show concordant results.

### 9.4 Stopping rules

Stop or downgrade the conclusion if:

- R+SF restores activity.
- R+ions/PO₄ restores activity.
- Inert protein restores activity.
- Heated F loses complementing activity.
- Heated R plus F remains active.
- R+BE is inactive, unless BE is shown to be an invalid factor source.
- Matching tolerances cannot be met.
- Independent separations disagree.
- Enzyme integrity cannot be demonstrated.

---

## 10. Troubleshooting

### Problem: Low recovery after fractionation

Possible causes:

- Factor lost during buffer exchange.
- Enzyme damaged during separation.
- pH or ions changed.
- Protein diluted below active range.

Proposed responses:

- For F, avoid dialysis or cutoff conditions that could lose a small factor.
- Use direct add-back of concentrated buffer salts rather than exhaustive dialysis.
- Shorten processing time.
- Verify pH and conductivity after processing.
- Concentrate fractions gently if compatible.

### Problem: R alone inactive but R+BE also inactive

Possible causes:

- R enzymes damaged.
- BE lacks factor.
- Heat treatment destroyed a needed heat-stable component.
- pH/salt mismatch.
- Substrate limitation.

Proposed responses:

- Check enzyme-integrity marker.
- Reduce heat severity if BE factor is lost.
- Add universal substrate if substrate limitation is possible.
- Re-match pH and ions.
- Prepare fresh R and BE.

### Problem: SF or SBE restores activity

Interpretation:

- The matched variables may be sufficient.
- pH, salt, phosphate, protein, substrate, or dilution artifacts are not excluded.

Proposed response:

- Do not claim a separate heat-stable factor.
- Re-measure and tighten matching.
- Test additional inactive analogs.
- If restoration persists, the factor interpretation is unsupported.

### Problem: R+Fheat inactive

Interpretation:

- The complementing activity is not heat-stable under the tested condition.
- Alternatively, heating changed pH, salt, or volume.

Proposed response:

- Re-measure and correct heated fraction.
- Test milder heat conditions.
- If activity remains lost, do not claim heat stability.

### Problem: Inert protein produces activity

Interpretation:

- Nonspecific stabilization or contamination is possible.

Proposed response:

- Test alternative inert proteins.
- Reduce protein matching to the minimum needed.
- Include protein-only controls.
- If unresolved, protein/dilution alternatives remain plausible.

---

## Alternatives and limits

### Alternatives that the protocol attempts to exclude

1. **pH artifact**  
   Addressed by measuring and matching pH after mixing.

2. **Salt artifact**  
   Addressed by ion add-back, conductivity matching, and ion-only controls.

3. **Phosphate artifact**  
   Addressed by phosphate measurement, phosphate add-back, and phosphate-only controls.

4. **Dilution artifact**  
   Addressed by fixed final volume, whole-dilution controls, and protein-normalized rates.

5. **Protein concentration artifact**  
   Addressed by matching total protein or using inert protein controls and testing their effects.

6. **Enzyme damage artifact**  
   Addressed by R+BE rescue, optional independent enzyme marker, and preincubation stability checks.

7. **Nonspecific stabilization artifact**  
   Addressed by inert matcher controls and comparison of immediate versus preincubated rates.

8. **Substrate artifact**  
   Addressed by adding saturating substrate to all tubes or by matching fermentable substrate.

### Remaining limits

1. **Unmeasured variables**  
   The protocol can match only measured variables. Unmeasured osmolytes, metabolites, metal ions, or small organic molecules could remain confounded.

2. **Operational, not structural, identity**  
   A positive result identifies a functional heat-stable complementing activity, not a chemical species.

3. **No NAD conclusion**  
   The protocol does not establish NAD identity, nicotinamide chemistry, nucleotide structure, redox role, or stoichiometry.

4. **Factor may be a mixture**  
   The active fraction may contain more than one required component. The conclusion is compatible with a multicomponent requirement.

5. **Boiled-extract ambiguity**  
   Boiling may alter small molecules, release bound species, or change metal availability. BE is useful as an independent heat-stable source, but equivalence to F must be demonstrated, not assumed.

6. **Separation cutoff arbitrariness**  
   Filtrate/retentate division depends on the chosen separation method. Independent separations reduce but do not eliminate this limitation.

---

## What would change the recommendation?

The recommendation would be strengthened if:

- R+F is active and R+SF is inactive across independent separations.
- R+BE is active and R+SBE is inactive.
- Heated F retains activity.
- Heated R does not support activity.
- Enzyme-integrity controls show intact R.
- Optional factor depletion and add-back reproduce the effect.

The recommendation would be weakened or rejected if:

- Matched SF or SBE restores activity.
- Salt, phosphate, protein, or dilution controls restore activity.
- Heat treatment destroys the filtrate factor.
- R cannot be rescued by BE or another validated factor source.
- Independent separations give inconsistent results.
- The primary contrast is small relative to calibrated noise.

---

## Final conditional statement

If the proposed assay meets its calibration, matching, enzyme-integrity, heat-control, and independent-separation criteria, then the strongest justified conclusion is:

> The yeast-juice system contains an operationally defined, heat-stable, separable factor or factor pool that is required for fermentative activity under the reconstitution conditions tested.

This conclusion is functional and conditional. It does not establish chemical structure, purity, molecular identity, or NAD identity. All experiments described above are proposed and require calibration before any inferential claim is made.
