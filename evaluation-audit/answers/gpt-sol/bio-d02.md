# GPT-5.6 Sol / bio-d02

Original final answer, shared by both scoring rounds.

## Recommended proposed test

**All experiments below are proposed; no outcomes are claimed.**

Use a depletion–reconstitution design in which a cell-free yeast-juice preparation is separated into an enzyme-rich retentate and a permeant filtrate, then recombined at matched extract equivalents. The decisive result would be a reproducible positive retentate–filtrate interaction, restoration by a heat-treated filtrate or boiled-extract supernatant, and failure of matched pH, ion, phosphate, protein, dilution, mineral-only, and inactive-fraction controls to restore activity. Enzyme integrity must remain equivalent to a sham-processed preparation.

If these conditions are met, the justified conclusion would be that **fermentative activity in this cell-free assay operationally requires a separable, heat-stable activity**. It would not identify the chemical structure, establish that the activity is a single molecule, or justify NAD identity.

---

# 1. Experimental objective and hypotheses

### Primary proposed hypothesis

Removing a permeant component from yeast juice leaves an enzyme-containing retentate with little fermentative activity, and adding the corresponding filtrate restores activity through a component-specific interaction.

### Heat-stability hypothesis

The restoring activity remains after a calibrated boiling treatment that destroys protein-enzyme activity.

### Main alternatives to exclude

1. Different pH after separation or heating.
2. Changes in inorganic ions, conductivity, osmolality, or free inorganic phosphate.
3. Simple dilution or concentration differences.
4. Loss, denaturation, or leakage of fermentation enzymes during fractionation.
5. Nonspecific stabilization by added protein, peptides, osmolytes, or extract matrix.
6. Carryover of intact yeast cells.
7. Background substrate, ethanol, or gas introduced by the add-back fraction.

---

# 2. Preliminary calibration

Exact buffer, ion, phosphate, volume, protein, cutoff, heating, and dilution values are unreported. They should therefore be calibrated in separate pilot experiments and locked before the confirmatory experiment.

## 2.1 Assay calibration

Using unfractionated yeast juice:

1. Establish a defined fermentation mixture containing a fermentable substrate such as glucose.
2. Calibrate substrate concentration to be nonlimiting over the measurement interval but below inhibitory concentrations.
3. Calibrate temperature, mixing, oxygen exclusion, headspace, and sampling times.
4. Identify a time interval over which ethanol production and, separately, carbon dioxide evolution are linear.
5. Select one readout as primary—preferably the initial linear rate of ethanol formation—and retain CO₂ evolution as an orthogonal confirmation.
6. Include no-substrate controls to quantify endogenous ethanol or gas production.
7. Define the lower limit of quantification and the smallest biologically relevant restoration, \(\delta_{\mathrm{req}}\), from assay variance and the activity of sham-processed parent material.

These values should be chosen before testing coded confirmatory samples.

## 2.2 Defined buffer calibration

Use a non-phosphate buffer so that buffering and phosphate can be controlled independently.

1. Measure native yeast-juice pH.
2. Screen defined buffers whose pKa values bracket that pH—for example, MES in an acidic range or MOPS nearer neutrality.
3. Select the lowest buffer concentration that holds pH within a predeclared maximum drift while preserving parent-juice fermentation.
4. Lock buffer identity, concentration, target pH, temperature of pH measurement, and titrant.
5. Use this same final buffer composition in every assay condition, including blanks and heat controls.

If no defined non-phosphate buffer preserves parent activity, the test cannot adequately exclude buffer effects and should be redesigned.

## 2.3 Ion and phosphate add-back calibration

Measure the sham-processed parent, retentate, filtrate, boiled extract, and chromatographic pools for:

- K⁺, Na⁺, Mg²⁺, Ca²⁺ and other abundant measured cations;
- Cl⁻, sulfate and other abundant measured anions;
- free inorganic phosphate;
- conductivity and osmolality;
- total phosphorus as characterization, without assuming all phosphorus is inorganic phosphate.

Define the target final concentrations as those in active sham-processed parent at the chosen assay dilution. Prepare a documented analytical-grade ion mixture that reproduces those concentrations, conductivity, and osmolality. Add ions and free phosphate separately so phosphate can also be tested independently.

For every reaction, calculate the ions already contributed by fractions and add only the amount needed to reach the common target. Candidate pools that cannot be buffer-exchanged without losing activity should be balanced by adding the same chromatography matrix to all comparator reactions.

Perform a phosphate titration around the target concentration. The retentate–filtrate contrast should remain present when free inorganic phosphate is held constant. If phosphate alone restores activity, a separate heat-stable factor cannot be inferred from that experiment.

## 2.4 Fractionation calibration

Select a membrane cutoff that:

- retains total protein and at least two factor-independent enzyme markers;
- permits passage of small reference solutes;
- produces a filtrate with negligible marker-enzyme activity.

Calibrate the number of washes or diafiltration volumes needed to reduce retentate fermentation without unacceptable loss of marker enzymes. Do not choose wash extent solely because it maximizes the desired result.

Define one **extract equivalent** as the retentate or filtrate derived from the same starting volume of parent juice. Concentrate or dilute fractions so that recombination of one retentate equivalent and one filtrate equivalent reconstructs the original extract equivalent.

## 2.5 Heat-treatment calibration

In sealed or covered vessels:

1. Heat filtrate and a separate parent aliquot at boiling temperature for a calibrated duration.
2. Verify that a spiked heat-labile control enzyme and any endogenous marker-enzyme activity in the heated material are abolished to a predeclared criterion.
3. Clarify precipitated protein and retain the heat-stable supernatant.
4. Record vessel mass before and after heating and replace evaporated water.
5. Recheck pH, ions, phosphate, conductivity, and osmolality.
6. Process matched buffer-only and chromatography-buffer controls identically.

The boiling duration should be fixed before the confirmatory experiment.

---

# 3. Preparation and quality checks

## 3.1 Independent experimental units

Prepare multiple independent yeast-juice batches on different preparation occasions. Each independently prepared and fractionated batch is one biological experimental unit; replicate assay wells are only technical replicates.

Determine the number of independent units from pilot variance and a prospective power calculation for the primary contrast. Do not count repeated wells as independent observations.

## 3.2 Parent and sham controls

For each batch, reserve:

- untreated parent juice;
- a sham-processed parent exposed to the same time, temperature, handling, concentration, and buffer-exchange steps but without separating filtrate and retentate.

The sham parent is the main reference for processing damage and dilution.

## 3.3 Cell-free status

Before assay:

- inspect parent and fractions microscopically for intact cells;
- use a viability or colony-forming check where feasible;
- reject units in which cells capable of fermentation contaminate the fractions.

## 3.4 Fractionation

Conduct all manipulations cold and rapidly under a locked handling schedule.

1. Split each parent batch into the sham arm and fractionation arm.
2. Produce enzyme-rich retentate \(R\) and filtrate \(F\).
3. Collect all permeate washes assigned to \(F\).
4. Restore each fraction to its defined extract-equivalent volume.
5. Measure recovery of volume, total protein, ions, free phosphate, conductivity, osmolality, and marker-enzyme activities.
6. Store aliquots under identical validated conditions until use.

## 3.5 Enzyme-integrity monitoring

Select at least two yeast-juice enzyme activities that can be measured with defined substrates and saturating required reagents without relying on the unknown restoring factor. Prefer markers from different portions of the soluble enzyme system. Also record total soluble protein and a protein-profile measure.

Measure markers:

- in parent and sham parent;
- immediately after fractionation;
- after the maximum pre-assay holding time;
- after the assay incubation.

Retentate marker activity per unit enzyme protein should be equivalent to sham parent within a predeclared margin based on assay precision. A grossly damaged retentate should not be used to infer factor requirement.

---

# 4. Independent separation of restoring activity

Membrane fractionation alone may create membrane-specific or ionic artifacts. Therefore, perform an orthogonal proposed separation of the filtrate.

1. Subfractionate \(F\) by a different physicochemical principle, such as charge-based or adsorption chromatography.
2. Use scouting runs to identify conditions that recover restoring activity while separating it from the main conductivity and phosphate peaks.
3. Collect all fractions at fixed volume intervals.
4. Normalize their assay matrices for pH, buffer, ions, phosphate, conductivity, osmolality, and volume.
5. Assay each pool only by adding it to a common retentate aliquot.
6. Define an “active pool” and neighboring “inactive pools” using a separate pilot dataset. Freeze these definitions before confirmatory testing.

An adjacent inactive pool matched as closely as possible for volume, pH, conductivity, phosphate, osmolality, total organic content, and protein serves as the **operational inactive-analog control**. Because the chemical structure is unknown, it must not be described as a structural analog.

If a specific molecule is later nominated, an equimolar chemically related but fermentation-inactive analog may be added as a further proposed control; its availability or performance is not established here.

---

# 5. Protein, enzyme, and volume matching

For the primary comparisons:

- use the same aliquot and amount of retentate in every \(R\)-containing reaction;
- use the same final reaction volume;
- use the same number of original extract equivalents;
- hold substrate, buffer, ions, phosphate, temperature, and incubation time constant.

Measure protein in all additions. Bring total protein to a common target with a validated inert carrier protein that does not alter fermentation across the relevant concentration range. All arms should receive the same carrier lot. Repeat the key comparison without carrier or with a second validated carrier as a sensitivity test.

This matching prevents extra filtrate protein from acting merely as a nonspecific stabilizer. It does not by itself prove that all possible stabilization effects are absent, so the enzyme-stability and inactive-pool controls remain necessary.

---

# 6. Proposed randomized intervention groups

Within each independent separation unit, prepare at least the following coded conditions:

| Condition | Purpose |
|---|---|
| Complete reaction mixture without yeast fraction | Chemical and instrument blank |
| Untreated parent | Native activity reference |
| Sham-processed parent | Processing and dilution reference |
| \(R\) alone | Activity after removal of permeant material |
| \(F\) alone | Tests intrinsic activity or enzyme leakage |
| \(R+F\) | Primary reconstitution |
| \(R+\) heat-treated \(F\) | Heat-stability test |
| \(R+\) boiled-parent supernatant | Historical compensation-type control |
| Heat-treated \(R+F\) | Confirms that active enzymes reside in \(R\) |
| \(R+\) ion/phosphate reconstruction only | Salt and phosphate control |
| \(R+\) phosphate-only add-back | Specific phosphate control |
| \(R+\) mineral-only equivalent of active pool | Inorganic-component control |
| \(R+\) heat-treated buffer blank | Heating and vessel control |
| \(R+\) active orthogonal-separation pool | Independent rescue test |
| \(R+\) matched inactive-analog pool | Matrix and nonspecific-solute control |
| \(R+F\), no fermentable substrate | Endogenous background control |

The mineral-only equivalent can be prepared either from quantitative ion analysis or, if analytically validated, from an ash/mineral residue of the active pool. Because heating or ashing can alter phosphate species, analytical ion reconstruction is the primary mineral control.

A subset should also use cross-combinations, such as \(R_i+F_j\), across independently prepared batches. Consistent cross-rescue would show that the effect is not restricted to accidental compatibility within one preparation.

---

# 7. Allocation, blinding, intervention, and sampling

1. Randomize condition positions within each batch and assay run.
2. Have one operator prepare coded add-back solutions and a second blinded operator run the fermentation assay.
3. Balance conditions across assay positions, time blocks, and instruments.
4. Add retentate last or otherwise use one locked order of addition for every condition.
5. Start reactions simultaneously within defined blocks.
6. Record ethanol and CO₂ at enough time points to estimate an initial linear rate.
7. Measure pH at time zero and endpoint; monitor conductivity or osmolality in representative reaction aliquots.
8. Retain endpoint samples for protein and marker-enzyme activity.
9. Correct time-zero ethanol or dissolved carbon introduced by boiled or chromatographic fractions.

Technical replicates should be averaged before statistical analysis at the independent-unit level.

---

# 8. Primary contrast and analysis

Let \(v_X\) be the blank-corrected initial fermentation rate for condition \(X\), expressed per fixed retentate enzyme-protein amount.

The proposed primary contrast is the factorial interaction:

\[
I = v_{R+F}-v_R-v_F+v_0
\]

where \(v_0\) is the complete reaction-mixture blank.

A positive \(I\) tests whether recombination produces more activity than the additive activity of the separated fractions. Also report the reconstruction ratio:

\[
Q = \frac{v_{R+F}-v_0}{v_{\mathrm{sham\ parent}}-v_0}
\]

with confidence intervals.

Analyze rates using a mixed-effects model with retentate presence, filtrate presence, heat treatment, and separation method as fixed effects and independent preparation/fractionation unit as a random effect. Assay wells are nested technical replicates.

Use equivalence testing—not failure to find a difference—for:

- heat-treated versus unheated filtrate rescue;
- retentate marker-enzyme integrity versus sham parent;
- pH, ion, phosphate, and protein matching within predefined margins.

Adjust secondary comparisons for multiplicity. Show all independent-unit values and confidence intervals.

---

# 9. Proposed acceptance and stopping criteria

## Acceptance criteria

A result would support the operational requirement hypothesis only if all of the following occur:

1. Parent and sham parent show reproducible fermentation.
2. \(R\) and \(F\) individually are below the predefined activity threshold or represent only a small predefined fraction of sham-parent activity.
3. The lower confidence bound for \(I\) exceeds \(\delta_{\mathrm{req}}\).
4. \(R+F\) restores a substantial, reproducible fraction of sham-parent activity.
5. Heat-treated \(F\) and boiled-parent supernatant rescue within the predefined equivalence margin for unheated \(F\).
6. The active pool from the independent separation rescues, whereas the matched inactive pool does not.
7. Ion/phosphate-only, mineral-only, heat-blank, carrier-protein, and inactive-pool controls do not reproduce the rescue.
8. Initial and endpoint pH, measured ions, free phosphate, conductivity, osmolality, total volume, and protein satisfy matching criteria.
9. Retentate marker enzymes and protein profiles remain equivalent to sham-processed material.
10. Ethanol and CO₂ measurements are directionally concordant.

## Stop or redesign if

- sham parent loses substantial activity;
- retentate marker enzymes are damaged or leak materially into \(F\);
- intact cells contaminate a fraction;
- pH, ions, phosphate, volume, or protein cannot be matched;
- fermentation rates are not linear;
- only one separation batch shows rescue;
- salt, phosphate, mineral, carrier, or inactive-pool controls rescue comparably;
- activity follows conductivity or phosphate across the independent separation;
- heating changes pH or concentration in a way that cannot be corrected;
- \(R+F\) fails to restore activity despite acceptable fraction recovery.

---

# 10. Troubleshooting interpretations

- **\(R\) remains strongly active:** depletion was incomplete. Increase calibrated diafiltration while monitoring enzyme retention.
- **Both \(R\) and \(F\) are inactive and recombination remains inactive:** examine enzyme damage, fraction recovery, substrate conditions, irreversible loss to the membrane, and incompatible storage.
- **Only boiled whole extract rescues:** nonspecific stabilizers, peptides, or metabolites remain plausible; do not infer a distinct factor until an independently separated active pool also rescues.
- **Ion or phosphate reconstruction rescues:** the experiment does not exclude an inorganic explanation.
- **Active and inactive pools differ in conductivity or osmolality:** rematch matrices or further separate them before interpretation.
- **Heat-treated \(F\) loses rescue:** a separable component may still be required, but heat stability is not supported.
- **Marker enzymes decline in every fractionated retentate:** redesign the fractionation; add-back rescue could reflect stabilization of damaged enzymes.
- **Ethanol rises without corresponding CO₂:** investigate background ethanol, assay interference, or nonfermentative reactions.

---

# 11. Evidence-to-inference-to-conclusion chain

### Supplied evidence

1. **Source summary and curator interpretation:** the 1906 record reports inactive filtrate and retentate fractions, restoration when recombined, and compensation by boiled extract.
2. **Stated artifacts:** pH, inorganic salts, phosphate, enzyme damage, dilution, and nonspecific stabilization can imitate compensation.
3. **Stated limits:** compensation does not establish chemical structure or NAD identity.
4. **Hypothetical constraints:** fractionation and candidate fractions are available, but exact operating parameters and factor identity are unknown.

### Proposed inference

- Loss after depletion plus a positive \(R\times F\) interaction supports necessity of something removed into the filtrate.
- Rescue after verified boiling supports heat stability.
- Rescue by an independently separated activity pool supports physical separability rather than a single membrane artifact.
- Failure of matched pH, ion, phosphate, mineral, protein, dilution, and inactive-pool controls to rescue narrows the explanation beyond those alternatives.
- Preserved marker-enzyme activity limits, but cannot absolutely eliminate, enzyme-damage explanations.

### Conditional conclusion

If all acceptance criteria are met, conclude only:

> Under the defined proposed cell-free assay conditions, fermentative activity operationally requires a separable activity that survives the calibrated heat treatment, and the observed restoration is not explained by the tested pH, inorganic-ion, free-phosphate, dilution, protein-loading, gross enzyme-damage, or nonspecific matrix controls.

Do **not** conclude a chemical structure, purity, molecular class, single-factor stoichiometry, in vivo universality, or NAD identity.
