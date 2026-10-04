# GPT-6 Astra / bio-d02

Original final answer, shared by both scoring rounds.

## Proposed conclusion and scope

**All experiments below are proposed; no results are asserted.**

The recommended test is a paired **depletion–reconstitution experiment**: remove a separable fraction from yeast juice, restore all measured inorganic conditions without restoring that fraction, and then ask whether adding the fraction specifically restores fermentation. Repeat the finding with an independent separation method and test whether the restoring activity survives a documented heat treatment.

A positive result would support **a heat-stable, separable activity required under the tested conditions**. It would not establish a single compound, chemical structure, catalytic mechanism, or NAD identity.

### Evidence → inference → testable conclusion

- **Supplied evidence:** The source summary reports inactive filtrate and retentate separately, restoration on recombination, and compensation by boiled extract.
- **Inference:** Fermentative activity may require an enzyme-containing fraction plus a separable, heat-stable component.
- **Unresolved alternatives:** Separation may alter pH, salts, phosphate, concentration, or enzyme integrity; added material may merely stabilize damaged enzymes.
- **Proposed resolution:** Demonstrate fraction-specific rescue after matching these variables, with preserved enzyme capacity and independent separation.
- **Evidence location:** The supplied “Source summary and curator interpretation,” particularly its compensation finding and stated artifact and identity limitations. No finer historical methods or evidence locations are supplied.

## 1. Calibration and locked assay formulation

**Unreported parameters:** Buffer identity and concentration, pH, ion and phosphate concentrations, protein loading, volumes, dilution, substrate concentration, separation settings, heating duration, sampling interval, and acceptance thresholds. Establish these in pilot experiments, then lock them before confirmatory testing.

### 1.1 Calibrate fermentation measurement

Using unfractionated yeast juice, propose to:

1. Identify an enzyme-loading range with approximately proportional fermentation rate and a reproducible measurement window.
2. Select a common fermentable-substrate concentration that is not limiting during that window.
3. Fix temperature, mixing, oxygen exposure, vessel geometry, headspace, and sampling schedule.
4. Establish background, detection limit, precision, and recovery of the analytical measurements.
5. Measure substrate contributed by filtrate or boiled extract and equalize total starting substrate across arms. Include no-added-substrate controls to identify endogenous contributions.

The proposed primary readout is **CO₂ production rate**; ethanol accumulation is an independent confirmation of fermentation. Gas evolution alone is insufficient because acidification or carbonate release could imitate CO₂ production.

### 1.2 Define the final buffer and ion matrix

Select a **non-phosphate buffer** whose useful range includes the reproducible activity plateau of the preparation. Screen buffer identity and concentration for adequate pH control without suppressing unfractionated or recombined activity.

Define the final matrix as:

\[
D=\{B,b^*,pH^*,[\mathrm{P_i}]^*,\mathbf{c}_{ions}^*\}
\]

where \(B\) is the selected buffer, \(b^*\) its concentration, and \(\mathbf{c}_{ions}^*\) the measured target ion vector. Measure relevant major ions rather than assuming their concentrations; proposed analytes include potassium, sodium, magnesium, calcium, chloride, sulfate, and inorganic phosphate. Record buffer-titrant counterions.

Before confirmatory testing, produce an actual recipe specifying every reagent, stock concentration, addition volume, and final concentration. **The symbols above are calibration targets, not a complete executable recipe until those measurements are made.**

For every assay arm:

- Calculate add-back from the ions already contributed by retentate, filtrate, extract, substrate, and buffer stocks.
- Verify final pH, inorganic phosphate, major ions, and conductivity; conductivity alone cannot establish ion equivalence.
- Where material, verify free-ion availability, particularly if fractions change ion binding.
- Measure pH and phosphate through the assay, not only initially.

Prefer compensating additions to lower-content arms. Do not blindly desalt the active fraction, because that could remove the unknown activity. If matching requires inhibitory concentrations, reduce fraction loading or develop a recovery-validated purification step.

### 1.3 Challenge the inorganic alternatives

Propose a pilot factorial/titration study of retentate with:

- Buffer/pH correction alone.
- Measured salt replacement without phosphate.
- Phosphate replacement with compensatory adjustment of other ions.
- Full matrix \(D\).
- Full matrix plus active fraction.

Explore the non-inhibitory range around the target values and the measured uncertainty in fraction contributions. The confirmatory target should lie in a robust activity region, not on a steep pH or salt response. If inorganic correction alone reproduces rescue, the separable-factor interpretation is not established.

## 2. Independent units, allocation, and blinding

- Use independently prepared yeast-juice batches as biological experimental units.
- Split every batch across the principal treatment arms and separation routes. Wells or vessels from one batch are technical replicates, not independent biological units.
- Use pilot variability and a prespecified minimum meaningful rescue to determine the required number of independent batches.
- Randomize processing and assay order within batch; balance time since preparation.
- Have a separate operator code active, heated, inactive-comparator, and matrix preparations. Blind measurement and analysis where feasible; document unavoidable processing unblinding.
- Keep pilot fraction selection separate from confirmatory testing. Lock exclusions, contrasts, and analysis before decoding.

## 3. Preparation and separation quality checks

### 3.1 Input and controls

Prepare a homogeneous yeast-juice-derived fermenting preparation. Record initial fermentation rate, protein, pH, phosphate, ions, substrate content, and relevant handling conditions.

Reserve:

- **U:** Handling-matched unfractionated input.
- **Process blank:** Buffer carried through separation apparatus.
- **Complete recombination:** All recovered retentate, filtrate, and relevant wash fractions combined in their recovered proportions.

Match handling time, temperature, agitation, and final assay dilution as closely as possible. Quantify losses through fraction volumes, total protein, selected enzyme markers, and recovered fermentation capacity.

### 3.2 Primary separation

Propose membrane fractionation, with retention characteristics selected empirically, to obtain:

- **R:** Enzyme-rich retentate.
- **F:** Candidate complement-containing filtrate.

Collect serial washes if needed to deplete the complement from R. Assay washes rather than discarding them uncharacterized. Stop washing if enzyme leakage or declining recoverable capacity indicates damage.

The aim is not simply an inactive retentate: it is a depleted retentate whose enzyme machinery remains recoverable.

### 3.3 Independent separation

Propose a second, non-membrane partition of fresh matched input—for example, a charge-based chromatographic separation selected in pilot work—to obtain:

- **E₂:** Enzyme-rich, complement-depleted pool.
- **C₂:** Candidate restoring pool.

Validate recovery and correct the different salt backgrounds before interpretation. Test within-route recombination and cross-rescue:

- \(R+C_2\)
- \(E_2+F\)

An orthogonal separation of F alone could help localize activity, but would not fully replace independent production of an enzyme-rich depleted pool. If the second route cannot preserve enzyme capacity, report that limitation rather than counting it as confirmation.

## 4. Protein, volume, and dose matching

For all comparisons containing R, use the **same R aliquot and enzyme-protein dose**. Do not reduce R to compensate for protein introduced by F or boiled extract.

Bring every assay to the same:

- Final volume and retentate dilution.
- Starting substrate concentration.
- Total protein concentration.
- Buffer, pH, ion, and phosphate targets.
- Handling duration and measurement conditions.

Use a pilot-validated, factor-free protein carrier to fill protein deficits. It must neither rescue depleted R by itself nor inhibit the positive control. Validate protein-assay recovery in each fraction matrix.

In enzyme-free controls, replace R with matrix plus carrier, denoted **M**. This matches total protein but intentionally lacks the fermentative enzyme complement.

For fraction dose–response experiments, keep R and final volume fixed; replace omitted fraction volume with matched matrix. Express doses by original-juice equivalent and measured recovered volume, not an unknown factor molarity.

## 5. Proposed intervention panel

All additions below are corrected to the locked final matrix and protein/volume targets.

| Arm | Purpose |
|---|---|
| U, handling matched | Reference activity |
| Complete recovered recombination | Process recovery |
| R + D | Inorganic correction without candidate fraction |
| M + F | Filtrate-alone activity and background |
| R + F | Primary reconstitution |
| M + D | Enzyme-free baseline |
| R + graded F | Dose dependence without dilution confounding |
| R + heated F; M + heated F | Heat survival and heated-fraction background |
| R + boiled-extract supernatant; supernatant without R | Historical-type compensation and residual enzyme check |
| R + inactive comparator I; M + I | Operational inactive-analog control |
| R + F + I versus matched R + F | Detect inhibition by I |
| R + nonspecific stabilizer controls | Test stabilization alternatives |
| R + process blank | Apparatus-derived effects |
| E₂ + D, E₂ + C₂, cross-rescue arms | Independent separation |

### Heat controls

Calibrate a recorded boiling exposure that reduces whole-preparation enzyme activity below the assay detection limit. Record actual sample temperature and exposure time.

Apply the locked treatment to F and to whole extract; include sham-heated aliquots. Cool, replace evaporative loss, remove precipitate using a matched handling scheme, and remeasure pH, ions, phosphate, volume, and protein.

Test boiled-extract supernatant alone and with additional active F to check for surviving fermentative enzyme capacity. A heat-stability claim applies only to the documented treatment and recovered restoring activity.

### Inactive-analog controls: necessary qualification

Because the active substance is unidentified, a **chemically defined structural analog cannot presently be specified**.

Propose an operational inactive analog, **I**: an adjacent inactive fraction from the orthogonal separation, selected in pilot experiments and matched for measured inorganic composition, volume, protein, and other measurable bulk properties. Alternatively, use an activity-depleted aliquot if a recovery-validated depletion method becomes available. Include sham processing.

Validate I independently in confirmatory batches and establish that it does not suppress rescue by active F. Otherwise, failure of \(R+I\) could reflect inhibition rather than lack of restoring activity.

This is a matched inactive-preparation control, not proof of molecular specificity. Heating F is not an adequate inactive control when heat stability is the hypothesis.

### Nonspecific stabilizer controls

Propose matched carrier protein, appropriately processed inactive protein material, and a compatible nonmetabolizable crowding/stabilization control selected during calibration. Test each alone and with active F. These controls address plausible stabilization mechanisms but cannot exhaust all possible stabilizers.

## 6. Intervention timing and sampling

1. Equilibrate coded fractions to the locked assay conditions.
2. Verify final composition using parallel aliquots.
3. Add F, I, boiled extract, or matrix to the fixed R dose.
4. Initiate fermentation consistently, for example by adding common substrate.
5. Record a time course spanning mixing, any lag, and the prespecified rate window.
6. Take matched samples for ethanol, substrate, pH, and phosphate.
7. Stop reactions using a pilot-validated procedure that preserves the measured analytes.

Add two proposed timing experiments:

- **Delayed rescue:** Hold depleted R for a defined period, then add F. Compare with immediate addition and matched inactive/stabilizer additions.
- **Removal–rescue cycle:** Rescue R, remove the separable activity again while maintaining matrix conditions, and re-add it. Track enzyme recovery throughout.

Rapid, repeatable dependence on fraction presence, without loss of enzyme capacity, would weigh against irreversible preparation damage. Timing alone would not exclude reversible stabilization.

## 7. Enzyme-integrity monitoring

Propose checks before separation, after depletion, after matched incubation, and after reconstitution:

1. **Protein/enzyme recovery:** Track enzyme markers in R and F, aggregation or precipitation, and evidence of degradation.
2. **Independent activity assays:** Measure several accessible enzyme activities using assays demonstrated in pilot work not to depend on the removed fraction.
3. **Recoverable fermentative capacity:** Challenge parallel aliquots with the same excess of a validated active complement pool. Compare maximal recovered rates at matched enzyme loading.
4. **Time dependence:** Determine whether declining retentate activity parallels a loss of recoverable capacity.
5. **Stabilizer comparison:** Ask whether inactive protein or other nonspecific stabilizers reproduce F rescue.

The common-complement challenge is useful but is not by itself an independent proof of enzyme integrity. Physical and component-activity measurements provide complementary evidence. If suitable fraction-independent enzyme assays cannot be established, confidence in excluding damage must be reduced.

## 8. Quantitative analysis

Let \(v_b(X)\) be the prespecified, background-corrected CO₂ rate for treatment \(X\) in independent batch \(b\). Propose the primary batch-level contrast:

\[
\Delta_b=
\frac{
[v_b(R+F)-v_b(R+D)]
-
[v_b(M+F)-v_b(M+D)]
}{
v_b(U)
}.
\]

This estimates fraction-dependent rescue beyond any fermentation or gas signal contributed by F itself, normalized to matched input activity. Report the unnormalized contrast as well.

Also report:

- Reconstitution recovery relative to U.
- Activity of each fraction alone.
- Heat-treated versus sham-treated rescue.
- Inactive-comparator and nonspecific-stabilizer effects.
- Orthogonal-route and cross-rescue effects.
- Ethanol-based confirmation.

Use paired batch contrasts or a model accounting for batch and technical nesting. Report effect sizes and confidence intervals. Prespecify a minimum meaningful rescue and equivalence margins for composition matching, heat survival, and process recovery from pilot precision and scientific relevance. Nonsignificance is not evidence of equivalence.

## 9. Acceptance, stopping, and troubleshooting

### Accept a qualified factor-dependence interpretation only if:

- Input and recovered-recombination controls are reproducibly active.
- R is depleted and F lacks appreciable independent fermentative enzyme activity, within prespecified limits.
- The primary rescue contrast exceeds the minimum meaningful effect.
- Inorganic correction and sensitivity challenges do not account for rescue.
- Protein, volume, substrate, and dilution matching pass.
- Enzyme capacity is preserved sufficiently to reject gross damage or loss as the explanation.
- Matched inactive preparations and tested nonspecific stabilizers do not reproduce rescue.
- Restoring activity survives the documented heat treatment.
- The independent separation and cross-rescue support the same interpretation.

### Stop interpretation or redesign if:

- **Poor total recovery:** Investigate adsorption, enzyme leakage, excessive washing, precipitation, or handling delay.
- **Matrix mismatch:** Recalibrate add-back; nominal stock calculations are insufficient.
- **Salt or phosphate alone rescues:** Attribute rescue to inorganic restoration unless an additional fraction-specific effect remains.
- **F alone ferments:** Tighten separation or quantify the enzyme contribution before interpretation.
- **Inactive comparator inhibits:** Replace it; it is not a valid specificity control.
- **Integrity deteriorates or stabilizers rescue equally:** The damage/stabilization alternative remains unresolved.
- **CO₂ rises without ethanol confirmation:** Investigate nonfermentative gas release.
- **R retains substantial activity:** Conclude enhancement or incomplete depletion, not absolute requirement.
- **Heating loses rescue:** Do not claim heat stability at that exposure.

## Conditional conclusion and limits

If these proposed criteria are met, the defensible conclusion would be:

> Fermentation in this depleted yeast-juice preparation depends on a separable restoring activity that survives the tested heat treatment. Rescue is not explained by the measured pH, inorganic-ion, phosphate, substrate, protein, volume, or dilution differences, and the tested enzyme-damage and nonspecific-stabilization alternatives are disfavored.

This remains an operational conclusion. The restoring material could contain multiple components, a required metabolite or cosubstrate, or a specific reversible stabilizer not distinguished by these assays. It would **not establish chemical structure or NAD identity**—the explicit inferential limit of the supplied evidence.
