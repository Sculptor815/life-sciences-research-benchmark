# Qwen3.8 Max (0902) / mol-r03

Original final answer, shared by both scoring rounds.

## Bottom-line recommendation

**Most valuable next biological question:**  
Is the inflammatory-caspase-generated **N-terminal fragment of gasdermin D (GSDMD-NT)** itself sufficient to injure membranes, or does membrane injury require an additional cellular component or condition?

**Recommended next action:**  
Perform a preregistered, reductionist reconstitution program using **purified GSDMD fragments and defined protein-free membranes**, coupled to membrane-binding/oligomerization assays, electrophysiology or imaging, and cellular validation. The primary test is whether purified GSDMD-NT can permeabilize defined membranes without added cellular proteins.

This is a **proposal**, not a report of observed results. The fixed packet supplies only genetic and fragment-expression evidence; it does not supply purified-protein membrane experiments. Therefore, no direct physical action of the fragment can yet be asserted.

---

## 1. Evidence permitted by the packet

| Fixed evidence | Permitted inference | Not established by this evidence |
|---|---|---|
| Inflammatory caspases cleave gasdermin D. | GSDMD is downstream of inflammatory caspase activity. | Cleavage site, kinetics, stoichiometry, or whether cleavage is the only relevant caspase effect. |
| Genetic loss links GSDMD processing to pyroptotic cell death. | GSDMD is required or important for the death phenotype in the tested contexts. | Whether GSDMD itself physically executes membrane injury, or acts through another component. |
| Fragment-expression experiments link processing to pyroptotic death; the N-terminal portion carries cytotoxic activity. | The N-terminal region contains determinants that can produce a cytotoxic phenotype when expressed. | Whether N-terminal fragment is sufficient at physiological abundance, whether it acts directly on membranes, or whether expression causes indirect effects. |
| No purified-protein membrane experiments are supplied. | The physical mechanism remains unresolved. | Any claim of pore formation, membrane insertion, lipid specificity, or direct membrane rupture. |

### Evidence-to-inference-to-conclusion chain

1. **Evidence:** Inflammatory caspases cleave GSDMD.  
   **Inference:** GSDMD is a substrate of inflammatory caspases.

2. **Evidence:** Genetic loss of GSDMD or its processing impairs pyroptotic death.  
   **Inference:** GSDMD is necessary, or at least important, for the death program in those settings.

3. **Evidence:** Expression of an N-terminal fragment is cytotoxic.  
   **Inference:** The N-terminal portion can carry death-promoting activity when present in cells.

4. **Limit:** Genetic necessity and fragment-expression cytotoxicity do not reveal the physical action of the fragment.  
   **Conclusion:** The unresolved question is whether GSDMD-NT is a direct membrane-injury effector or whether it requires another cellular component or condition.

---

## 2. Unresolved biological question

**Primary unresolved question:**  
Does GSDMD-NT directly and sufficiently injure membranes, or is it an upstream regulator of another membrane-injury mechanism?

**Operational form of the question:**  
Can purified GSDMD-NT, in the absence of other cellular proteins, increase the permeability of defined lipid membranes in a reproducible, dose-dependent, and fragment-specific manner?

**Secondary questions, addressed conditionally:**

1. Does GSDMD-NT bind membranes?
2. Does GSDMD-NT oligomerize in or on membranes?
3. Does GSDMD-NT produce discrete, size-selective conduits, or does it cause nonspecific membrane destabilization?
4. If GSDMD-NT is not sufficient alone, what class of additional factor is required: a lipid environment, a protein cofactor, a post-translational modification, or another cellular process?
5. Does behavior in purified systems predict behavior in cells lacking upstream inflammatory caspase activity?

---

## 3. Competing mechanisms and discriminating predictions

### Mechanism A: GSDMD-NT is a direct membrane-permeabilizing executioner

**Description:**  
After cleavage, GSDMD-NT binds membranes and directly produces lesions, pores, or conduits that allow ion and solute flux, leading to osmotic swelling and membrane rupture.

**Predictions:**

1. Purified GSDMD-NT alone permeabilizes protein-free liposomes or planar lipid bilayers.
2. Activity is dose-dependent and time-dependent.
3. Heat-inactivated GSDMD-NT, C-terminal fragment alone, or non-cleaved full-length protein should be inactive or much less active, assuming proper folding and controls.
4. Membrane binding, insertion, and/or oligomerization should correlate with permeabilization.
5. Planar bilayers may show discrete conductance events or stepwise increases in ion flux.
6. Cellular expression of GSDMD-NT should cause membrane-permeability phenotypes even when upstream inflammatory caspase activity is inhibited, provided the fragment is properly expressed and folded.

### Mechanism B: GSDMD-NT activates another cellular executioner

**Description:**  
GSDMD-NT is necessary but does not itself physically injure membranes. It activates, recruits, or releases another protein or pathway that executes membrane damage.

**Predictions:**

1. Purified GSDMD-NT alone does not permeabilize protein-free membranes.
2. Permeabilization may appear only after adding cell lysate, membrane fractions, or a specific candidate protein.
3. GSDMD-NT may show weak or no direct lipid binding.
4. Mutations that disrupt a protein-protein interaction surface, but not lipid binding, could abolish cellular toxicity.
5. Cellular toxicity may depend on downstream genes or proteins not yet identified.

### Mechanism C: GSDMD-NT requires a specific lipid, membrane geometry, or cellular condition

**Description:**  
GSDMD-NT can act directly on membranes, but only in a particular lipid environment, membrane curvature, charge environment, oxidizing or ionic condition, or after a modification not present in a minimal system.

**Predictions:**

1. GSDMD-NT is inactive on simple or default liposomes but active on a subset of lipid compositions or membrane states.
2. Activity may depend on anionic lipids, cholesterol-containing membranes, specific headgroups, membrane curvature, or lipid packing defects.
3. Fragment binding may occur without permeabilization unless the correct lipid context is present.
4. Cellular toxicity may be cell-type-dependent if the required lipid environment is cell-type-specific.

### Mechanism D: Fragment-expression cytotoxicity is indirect or nonphysiological

**Description:**  
Expression of GSDMD-NT causes cell stress, activates other pathways, or produces toxicity through non-membrane mechanisms. The fragment may be cytotoxic when overexpressed but not be the physiological membrane-injury agent.

**Predictions:**

1. GSDMD-NT toxicity correlates with expression level but not with membrane permeability.
2. Toxicity may be reduced by general stress-pathway interventions rather than by membrane-protective interventions.
3. Purified fragment shows no reproducible membrane activity.
4. Cellular death may have features distinct from pyroptotic membrane rupture.

---

## 4. Proposed research plan

This section is a **proposed protocol**. It does not report results and does not assume that any outcome has already been observed.

### 4.1 Overall design logic

The plan uses a hierarchical strategy:

1. **Establish valid reagents.**  
   Produce and validate purified GSDMD fragments and controls.

2. **Test direct membrane permeabilization in a minimal system.**  
   Use purified fragment and defined liposomes.

3. **Test physical membrane interaction.**  
   Measure binding, insertion, and oligomerization.

4. **Test biophysical nature of injury.**  
   Use planar bilayers or giant vesicles to distinguish discrete conduits from generalized destabilization.

5. **Validate in cells.**  
   Test whether fragment behavior in minimal systems predicts membrane injury in GSDMD-deficient cells.

6. **If direct activity is absent, search for missing cofactors.**  
   Add cellular fractions or varied lipid environments.

---

## 4.2 Prerequisites and assumptions

The packet does not supply protein-production methods, cleavage-site identity, purification conditions, lipid compositions, cell types, or quantitative expression levels. Therefore, the following prerequisites are proposed and must be fulfilled before mechanistic interpretation.

### 4.2.1 Protein reagents

Required proposed reagents:

1. Full-length GSDMD.
2. GSDMD-NT corresponding to the cytotoxic N-terminal portion.
3. GSDMD C-terminal fragment, if constructible.
4. A cleavage-resistant or non-cleavable full-length control, if the cleavage site can be defined.
5. Heat-inactivated or denatured GSDMD-NT.
6. Inflammatory caspase or caspases used to generate fragments, if cleavage is performed enzymatically.
7. Caspase-inhibited control preparations, if enzymatic cleavage is used.

If the exact cleavage boundary is not specified in available materials, it should first be defined by one or more of:

- protease cleavage followed by fragment separation,
- N-terminal sequencing,
- mass spectrometry,
- immunoblotting with fragment-specific antibodies,
- comparison with fragment-expression constructs already linked to cytotoxicity.

**Assumption:** Recombinant protein can be produced in soluble form. If not, the plan must pause and optimize expression, tags, truncations, refolding, or alternative expression systems before interpreting negative results.

### 4.2.2 Membrane systems

Proposed membrane systems:

1. **Large unilamellar liposomes** for dye-release assays.
2. **Giant unilamellar vesicles** for microscopy and influx assays.
3. **Planar lipid bilayers** for electrophysiology.
4. Optional: **lipid monolayers or nanodiscs** for binding and structural studies.

Because no lipid requirement is supplied in the packet, the proposal should begin with a small panel of defined lipid compositions rather than assuming one physiological composition.

Suggested initial panel:

1. Neutral zwitterionic lipid composition.
2. Anionic lipid-containing composition.
3. Cholesterol-containing composition.
4. A mixed composition approximating a generic mammalian membrane, if such a mixture is operationally defined.

All lipid compositions should be documented by lot number, molar ratio, solvent, storage, and extrusion history.

### 4.2.3 Cellular systems

Proposed cellular systems:

1. Wild-type cells responsive to inflammatory caspase-mediated death.
2. GSDMD-deficient cells, generated by genetic loss or gene editing if not already available.
3. Complementation lines expressing inducible GSDMD-NT, full-length GSDMD, or inactive controls.

**Assumption:** GSDMD-deficient cells can be maintained and manipulated. If not, the cellular phase should be delayed until valid genetic tools are available.

---

## 4.3 Calibration and quality control

Calibration must be completed before hypothesis testing. Calibration data are not to be treated as mechanistic results.

### 4.3.1 Protein calibration

Measure and record:

1. Protein concentration using at least two compatible methods, for example absorbance-based quantification and dye-binding assay, with standard curves.
2. Purity by SDS-PAGE or equivalent, with densitometric quantification.
3. Fragment identity by immunoblot, mass spectrometry, or N-terminal sequencing.
4. Aggregation state by size-exclusion chromatography, dynamic light scattering, or native PAGE.
5. Stability over the assay time course.
6. Endotoxin level if proteins will be added to cells or immune-sensitive preparations.
7. Protease contamination, especially if inflammatory caspase was used to generate fragments.

Acceptance criteria should be set before unblinding. Examples:

- Purity above a pre-specified threshold, such as 90% for the intended species.
- No dominant high-molecular-weight aggregate unless intentionally studying oligomers.
- Fragment concentration accurate within a pre-specified tolerance.
- Caspase activity absent or inhibited in final fragment preparations used for membrane assays.

### 4.3.2 Liposome calibration

Measure and record:

1. Lipid concentration.
2. Vesicle size distribution.
3. Dye encapsulation efficiency.
4. Baseline leakage in assay buffer.
5. Maximum releasable signal after detergent lysis.
6. Osmolarity and pH matching between inside and outside solutions.
7. Batch-to-batch reproducibility.

Acceptance criteria:

- Baseline leakage below a pre-specified threshold.
- Detergent control produces a clear maximal signal.
- Size distribution stable across the assay window.
- No evidence of vesicle fusion or precipitation during calibration.

### 4.3.3 Instrument calibration

For fluorescence assays:

- Calibrate excitation/emission settings.
- Confirm linear response across the expected signal range.
- Test photobleaching.
- Include no-liposome and no-protein blanks.

For electrophysiology:

- Record baseline noise and seal resistance.
- Confirm stable bilayer capacitance.
- Include buffer-only additions.
- Verify that the amplifier and acquisition system have known calibration standards or documented performance checks.

For imaging:

- Calibrate illumination intensity, exposure, and focus.
- Include fixed-size reference beads if measuring swelling or vesicle size.
- Standardize temperature and environmental control.

---

## 4.4 Independent experimental units, replication, randomization, and blinding

### 4.4.1 Independent units

Avoid treating technical replicates as biological evidence.

For liposome assays:

- Independent unit 1: independent protein purification or cleavage preparation.
- Independent unit 2: independent liposome batch.
- Independent unit 3: independent assay day.

For electrophysiology:

- Independent unit: bilayers formed from independently prepared protein and lipid stocks.

For cellular assays:

- Independent unit: independently differentiated, passaged, or edited cell preparations.
- If clones are used, multiple clones should be tested where feasible to avoid clone-specific artifacts.

### 4.4.2 Allocation

Randomize sample positions:

- Plate wells.
- Liposome batches across plates.
- Protein dilution series across plate positions.
- Treatment order in electrophysiology and imaging sessions.

A written randomization scheme should be generated before data collection.

### 4.4.3 Blinding

Where practical:

1. Protein and lipid samples should be labeled with neutral codes.
2. The analyst performing primary data analysis should not know group identity until after quality-control criteria are met and the primary analysis plan is locked.
3. Imaging analysis should be blinded or automated.
4. Electrophysiology event detection should use predefined thresholds and, if possible, automated event-finding with blinded review.

Blinding may be partially limited for operations such as setting protein concentration, but outcome assessment can still be blinded.

---

# 5. Primary experiment: purified-fragment liposome permeabilization assay

## 5.1 Objective

Determine whether purified GSDMD-NT alone can increase permeability of protein-free liposomes.

## 5.2 Primary hypothesis

GSDMD-NT, but not appropriate inactive controls, causes reproducible, dose-dependent release of encapsulated fluorescent dye from liposomes.

## 5.3 Proposed assay format

1. Prepare liposomes loaded with a self-quenching fluorescent dye at high internal concentration.
2. Remove external dye using size-exclusion spin columns, dialysis, or equivalent buffer-exchange method.
3. Add purified proteins or controls to liposomes in matched assay buffer.
4. Monitor fluorescence over time as dye release relieves quenching.
5. At the end, add detergent to define the maximum release signal.

This assay tests membrane permeability, not the molecular identity of the lesion. It is therefore a primary screen, not a proof of pore architecture.

## 5.4 Experimental conditions

Test each of the following across multiple protein-to-lipid ratios:

1. Buffer only.
2. GSDMD-NT, low concentration.
3. GSDMD-NT, intermediate concentration.
4. GSDMD-NT, high concentration.
5. Full-length GSDMD, if available.
6. C-terminal fragment, if available.
7. Heat-inactivated or denatured GSDMD-NT.
8. Caspase-only control, if caspase was used to generate NT.
9. Caspase-inhibited NT preparation.
10. Detergent-positive permeabilization control.
11. Empty-buffer or carrier-protein control if stabilizers are used.

The exact concentration range should be set during calibration and should span concentrations that are achievable and relevant in cellular fragment-expression experiments, where possible.

## 5.5 Controls and their purposes

| Control | Purpose |
|---|---|
| Buffer only | Defines baseline leakage. |
| Detergent | Defines maximum release and validates dye response. |
| Heat-inactivated NT | Tests whether activity requires folded protein. |
| C-terminal fragment | Tests whether activity is specific to NT. |
| Full-length protein | Tests whether cleavage or fragment release is required. |
| Caspase-only control | Excludes permeabilization by residual protease. |
| Caspase inhibitor | Confirms that protease activity is not responsible. |
| Liposomes without dye | Checks autofluorescence and scattering. |
| Dye without liposomes | Checks protein effects on free dye signal. |

## 5.6 Measurements

Primary measurement:

- Normalized dye-release kinetics.

Secondary measurements:

- Initial rate of release.
- Area under the release curve over a pre-specified time window.
- Endpoint release after a fixed time.
- Dose-response relationship.
- Dependence on lipid composition.
- Light-scattering or turbidity changes, if instrument permits.

## 5.7 Analysis plan

1. Subtract buffer-only background.
2. Normalize each trace:
   - 0% release: pre-addition baseline or buffer control.
   - 100% release: detergent-added maximum.
3. Exclude wells or traces failing calibration, such as detergent failure or extreme baseline drift.
4. Fit dose-response curves where possible.
5. Use mixed-effects modeling or an equivalent approach with protein preparation, liposome batch, and assay day as random effects.
6. Compare:
   - NT versus buffer.
   - NT versus heat-inactivated NT.
   - NT versus C-terminal fragment.
   - NT versus full-length protein.
7. Require consistency across independent protein preparations and liposome batches before accepting a positive result.

Pre-specified decision rule, example:

A positive direct-permeabilization result should meet all of the following:

1. NT produces release above buffer and heat-inactivated controls.
2. The effect is dose-dependent or saturable.
3. The effect is observed in at least three independent protein preparations and at least two lipid batches.
4. The effect survives correction for multiple comparisons or is supported by a pre-registered effect-size threshold.
5. Calibration and positive-control criteria are met.

## 5.8 Stop rules for the primary assay

Do not interpret biological mechanism if any of the following occur:

1. Buffer-only leakage is high.
2. Detergent-positive control fails.
3. Protein is visibly aggregated or degraded.
4. NT preparation contains active contaminating protease.
5. Fluorescence signal is unstable in no-protein controls.
6. Protein adheres extensively to plastic and effective concentration is unknown.
7. Liposome size changes before protein addition.

In these cases, troubleshoot before drawing conclusions.

## 5.9 Troubleshooting

| Problem | Possible cause | Corrective action |
|---|---|---|
| High baseline leakage | Fragile liposomes, osmotic mismatch, dye toxicity | Adjust lipid composition, match osmolarity, change dye concentration, extrude freshly |
| No detergent response | Dead dye, wrong wavelength, instrument failure | Re-make dye stock, recalibrate instrument, verify filter settings |
| High variability | Liposome batch instability, pipetting error, protein aggregation | Standardize extrusion, use multichannel or automated liquid handling, check SEC/DLS |
| Apparent activity only at very high protein concentration | Nonspecific detergent-like effect or aggregation | Test lower concentrations, add binding controls, examine oligomerization |
| Activity lost after storage | Protein instability | Use fresh protein, change buffer, avoid freeze-thaw, add stabilizers if compatible |
| Caspase contamination | Incomplete removal after cleavage | Add chromatography step, use irreversible caspase inhibitor, include caspase-only control |

---

# 6. Secondary experiments: membrane binding, insertion, and oligomerization

A positive permeabilization assay does not by itself prove direct binding or pore formation. These assays test the physical relationship between fragment and membrane.

## 6.1 Liposome co-sedimentation binding assay

### Objective

Determine whether GSDMD-NT associates with liposomes.

### Proposed design

1. Incubate purified GSDMD-NT with liposomes of defined composition.
2. Separate liposome-associated protein from free protein by ultracentrifugation.
3. Quantify protein in pellet and supernatant.
4. Repeat with:
   - no-liposome control,
   - C-terminal fragment,
   - heat-inactivated NT,
   - varied lipid compositions,
   - varied salt concentrations.

### Measurements

- Fraction of protein pelleted.
- Apparent binding affinity.
- Lipid-composition dependence.
- Salt or pH dependence.

### Interpretation

- Strong lipid-dependent pelleting supports membrane association.
- Pelleting without liposomes suggests aggregation.
- Lack of pelleting argues against direct membrane binding under tested conditions.

## 6.2 Protease-protection or insertion assay

### Objective

Distinguish surface-bound fragment from membrane-inserted fragment.

### Proposed design

1. Incubate fragment with liposomes.
2. Treat with an external protease.
3. Measure protected fragment by immunoblot or quantitative gel analysis.
4. Compare intact liposomes with detergent-permeabilized liposomes.

### Interpretation

- Protection of part or all of the fragment in intact liposomes suggests insertion or internalization.
- Complete digestion suggests surface exposure or weak association.
- Protection only after detergent-induced disruption suggests the assay failed to report insertion properly and must be repeated.

## 6.3 Oligomerization assay

### Objective

Determine whether permeabilization correlates with oligomer formation.

### Proposed methods

Use at least two orthogonal approaches:

1. Chemical crosslinking followed by SDS-PAGE or immunoblot.
2. Blue-native PAGE or native PAGE.
3. Size-exclusion chromatography with multi-angle light scattering, if available.
4. Negative-stain or cryogenic electron microscopy, if resources permit.
5. Single-vesicle imaging of fluorescently labeled fragment, if available.

### Measurements

- Monomer, oligomer, and aggregate fractions.
- Oligomer size distribution.
- Dependence on membranes.
- Correlation with dye release.

### Interpretation

- Membrane-dependent oligomerization correlated with permeabilization supports a pore/lesion mechanism.
- Oligomerization without permeabilization suggests binding or assembly is not sufficient.
- No oligomerization despite permeabilization suggests an alternative lesion mechanism or assay limitation.

---

# 7. Biophysical characterization: discrete conduits versus general destabilization

If the primary liposome assay is positive, the next question is whether the fragment produces discrete, reproducible conduits or nonspecific membrane damage.

## 7.1 Planar lipid bilayer electrophysiology

### Objective

Test whether GSDMD-NT produces ion-conducting events in a protein-free bilayer.

### Proposed design

1. Form a planar lipid bilayer across an aperture.
2. Add purified GSDMD-NT to one side.
3. Record current under voltage clamp.
4. Compare with:
   - buffer-only addition,
   - heat-inactivated NT,
   - C-terminal fragment,
   - bilayers formed from different lipid compositions.

### Measurements

- Baseline conductance.
- Stepwise conductance transitions.
- Open and closed dwell times.
- Conductance amplitude distribution.
- Voltage dependence.
- Ion selectivity, if stable events are observed.
- Reversal potential under asymmetric salt conditions.

### Positive outcome for discrete conduit model

- Reproducible stepwise conductance increases.
- Characteristic conductance states.
- Dependence on NT and lipid composition.
- Absence of comparable events with inactive controls.

### Negative outcome

- No discrete events despite liposome dye-release activity.
- This may indicate large transient defects, bilayer incompatibility, or insufficient sensitivity.

### Troubleshooting

- High noise: improve grounding, salt concentration, lipid purity, chamber cleaning.
- Unstable bilayer: change lipid mixture, aperture geometry, or bilayer formation method.
- No events: test wider voltage range, alternative lipid compositions, freshly purified protein.

## 7.2 Giant unilamellar vesicle imaging

### Objective

Visualize membrane permeability, swelling, and rupture at the single-vesicle level.

### Proposed design

1. Prepare giant vesicles containing a small internal fluorescent dye.
2. Add GSDMD-NT or controls externally.
3. Monitor by time-lapse fluorescence microscopy.
4. Optionally include external dyes of different molecular sizes to estimate size selectivity.

### Measurements

- Time to dye loss.
- Time to external dye entry.
- Vesicle swelling.
- Vesicle bursting.
- Dependence on fragment concentration and lipid composition.

### Interpretation

- Gradual dye loss with swelling supports osmotic permeabilization.
- Sudden all-or-none rupture may indicate catastrophic failure.
- Size-selective entry of small but not large external solutes would support defined conduits, though quantitative pore size requires additional calibration.

---

# 8. Cellular validation

Minimal-system experiments must be connected back to the cellular phenotype described in the packet. This phase asks whether fragment behavior in purified systems predicts membrane injury in cells.

## 8.1 Objective

Determine whether GSDMD-NT can cause membrane-permeability changes in cells without requiring upstream inflammatory caspase cleavage.

## 8.2 Proposed cellular models

1. GSDMD-deficient cells.
2. Wild-type parental cells.
3. GSDMD-deficient cells reconstituted with inducible constructs:
   - empty vector,
   - full-length GSDMD,
   - GSDMD-NT,
   - inactive or cleavage-resistant controls,
   - binding- or oligomerization-defective variants, if identified from the in vitro phase.

## 8.3 Experimental conditions

1. Uninduced control.
2. Induced empty vector.
3. Induced full-length GSDMD.
4. Induced GSDMD-NT.
5. Induced inactive controls.
6. Induced GSDMD-NT with inflammatory caspase inhibitor.
7. Induced full-length GSDMD with inflammatory caspase activation stimulus, if such a stimulus is available in the system.
8. Osmotic or membrane-stabilizer controls, where compatible.

## 8.4 Measurements

Primary cellular measurements:

1. Membrane permeability by dye uptake or release assays.
2. Cell viability or metabolic activity.
3. Time-lapse morphology, including swelling and rupture if observable.
4. Fragment expression level by immunoblot or quantitative fluorescence.

Secondary measurements:

1. Inflammatory caspase activity, to confirm inhibitor effectiveness.
2. Fragment localization by microscopy.
3. Oligomerization in cells, if detectable.
4. Dependence on expression level.

## 8.5 Controls

| Control | Purpose |
|---|---|
| Empty vector | Controls for induction system and transfection effects. |
| Uninduced cells | Controls for leaky expression. |
| Caspase inhibitor | Tests whether NT acts downstream of upstream caspase activity. |
| Full-length GSDMD | Provides comparison with physiological precursor. |
| Inactive fragment variants | Tests specificity of any NT effect. |
| GSDMD-deficient background | Reduces ambiguity from endogenous GSDMD. |
| Multiple clones or passages | Reduces clone-specific artifacts. |

## 8.6 Analysis

1. Quantify membrane-permeability rate and endpoint.
2. Compare NT-expressing cells with empty-vector and inactive controls.
3. Test whether NT-induced permeability persists when inflammatory caspase activity is inhibited.
4. Correlate fragment abundance with permeability.
5. Use mixed-effects models with experiment, passage, and clone as random factors where appropriate.
6. Require consistency across independent cell preparations.

## 8.7 Interpretation

- If NT causes membrane permeability in GSDMD-deficient cells and this is not blocked by upstream caspase inhibition, the result supports NT acting downstream of upstream caspase activation.
- If NT causes death but not membrane permeability, the mechanism may be indirect or the assay may be insufficiently sensitive.
- If NT requires wild-type cellular background or specific cell type, cofactors or lipid environments may be needed.

---

# 9. Contingency plan if GSDMD-NT is not sufficient alone

If purified GSDMD-NT fails to permeabilize protein-free membranes, the correct conclusion is not automatically “GSDMD does not execute pyroptosis.” The fragment may require a missing component.

## 9.1 Candidate missing components

1. Specific lipid species or lipid states.
2. Membrane curvature or lipid packing defects.
3. A cytosolic or membrane-associated protein cofactor.
4. A post-translational modification of GSDMD-NT.
5. A second caspase substrate acting in parallel.
6. An ionic or redox condition absent from the minimal assay.

## 9.2 Fraction add-back experiment

### Objective

Determine whether a cellular fraction restores GSDMD-NT membrane activity.

### Proposed design

1. Prepare subcellular fractions:
   - cytosol,
   - membrane,
   - lipid extract,
   - heat-inactivated fraction,
   - protease-treated fraction where appropriate.
2. Add fractions alone and with GSDMD-NT to liposomes.
3. Measure dye release.

### Interpretation

- Activity only with NT plus a specific fraction suggests a required cofactor.
- Heat sensitivity of the fraction suggests a proteinaceous cofactor.
- Lipid extract dependence suggests lipid specificity.
- Fraction-alone activity must be subtracted or controlled.

## 9.3 Lipid panel

If lipid dependence is suspected, test an expanded lipid panel:

1. Different headgroup charges.
2. Different acyl-chain saturation.
3. Cholesterol-containing and cholesterol-free membranes.
4. Inner-leaflet-like and outer-leaflet-like compositions, if operationally defined.
5. High-curvature small vesicles versus low-curvature giant vesicles.

## 9.4 Genetic cofactor search

If a protein cofactor is suspected:

1. Use genetic loss-of-function screening or candidate-gene testing in the cellular assay.
2. Test whether loss of a candidate blocks NT-induced membrane permeability.
3. Reintroduce the candidate to restore activity.

This phase should begin only after the primary minimal-system assays have been properly controlled.

---

# 10. Statistical and audit plan

## 10.1 Preregistration

Before unblinding primary experiments, record:

1. Primary hypothesis.
2. Primary endpoint.
3. Inclusion and exclusion criteria for technical replicates.
4. Calibration acceptance criteria.
5. Statistical model.
6. Decision rules for positive, negative, and ambiguous outcomes.
7. Protein and lipid batch identifiers.

## 10.2 Sample-size and power

The packet supplies no variance information, so no fixed sample size can be justified without pilot calibration. The proposed approach is:

1. Run calibration experiments to estimate variance.
2. Choose replicate number to detect a biologically meaningful effect with adequate power.
3. Use at least three independent protein preparations and three independent liposome or cell preparations for primary conclusions.
4. Avoid treating technical replicate wells as independent evidence.

## 10.3 Data management

Record:

1. Reagent lot numbers.
2. Protein purification trace.
3. Lipid composition and storage history.
4. Instrument calibration logs.
5. Randomization seed.
6. Blinding code key, stored separately until analysis lock.
7. Raw data files in unedited form.
8. Analysis scripts or step-by-step transformation records.

This makes the plan auditable and distinguishes biological conclusions from technical artifacts.

---

# 11. Conditional outcomes and conclusions

## 11.1 Positive outcome: GSDMD-NT permeabilizes minimal membranes

### Pattern of results

1. Purified GSDMD-NT causes dose-dependent dye release from liposomes.
2. Heat-inactivated NT and C-terminal controls are inactive.
3. Activity is reproducible across independent protein and lipid preparations.
4. Binding and/or oligomerization correlate with permeabilization.
5. Planar bilayer or giant-vesicle assays show membrane conductance, influx, or rupture consistent with direct injury.
6. Cellular NT expression causes membrane permeability without requiring upstream inflammatory caspase activity.

### Strongest justified conclusion

GSDMD-NT is sufficient, under the tested conditions, to directly injure membranes. It is therefore a strong candidate for the direct executioner of pyroptotic membrane damage.

### Limits of this conclusion

Even with a positive outcome, the result would not prove:

1. That GSDMD-NT is the only executioner in native cells.
2. That the exact lesion architecture in purified membranes matches the lesion in living cells.
3. That no regulatory cofactors are required in vivo.
4. That all pyroptotic death in all cell types is fully explained by GSDMD-NT alone.

## 11.2 Negative outcome: GSDMD-NT does not permeabilize minimal membranes

### Pattern of results

1. Purified GSDMD-NT is well-behaved, monodisperse enough to interpret, and properly controlled.
2. Calibration and positive permeabilization controls work.
3. NT does not cause dye release, conductance changes, or vesicle rupture.
4. Inactive controls also do not act.
5. Cellular assays may or may not show toxicity.

### Strongest justified conclusion

GSDMD-NT alone is not sufficient to permeabilize the tested membranes. Therefore, direct membrane execution by NT alone is not supported under those conditions.

### Important caveat

A negative result would not prove that GSDMD is not involved. It would mean that the supplied minimal system lacks a required lipid, protein, modification, geometry, ionic condition, or other factor.

### Next action

Proceed to fraction add-back, lipid panel, modification testing, or genetic cofactor discovery.

## 11.3 Ambiguous outcome: activity only under limited or artificial conditions

### Pattern A: activity only at very high concentration

Interpretation:

- Could reflect weak specific activity.
- Could reflect nonspecific protein-induced membrane stress.
- Cannot be used alone to prove physiological direct execution.

Next action:

- Compare active concentration with cellular fragment abundance.
- Test binding specificity.
- Test mutant fragments.
- Seek cellular corroboration.

### Pattern B: activity only with one lipid composition

Interpretation:

- Supports a lipid-dependent direct mechanism.
- Does not yet prove that the active lipid composition is physiologically relevant.

Next action:

- Map lipid dependence.
- Test corresponding cellular membranes or extracts.
- Mutate candidate lipid-binding surfaces if identifiable.

### Pattern C: liposome dye release without electrophysiological events

Interpretation:

- May indicate transient defects, membrane thinning, or unstable pores.
- May indicate that planar bilayer conditions are unsuitable.
- Does not establish a stable pore.

Next action:

- Use giant-vesicle influx assays.
- Vary voltage, lipid composition, and protein concentration.
- Test whether oligomerization correlates with release.

### Pattern D: cellular toxicity without minimal-system membrane activity

Interpretation:

- Suggests indirect cellular mechanism or missing cellular cofactor.
- Also raises the possibility of non-membrane toxicity or expression artifact.

Next action:

- Add cellular fractions to minimal assay.
- Test whether toxicity depends on other genes.
- Measure non-membrane stress markers.

### Pattern E: membrane binding without permeabilization

Interpretation:

- Binding is not sufficient for injury.
- May require oligomerization, lipid specificity, or a second factor.

Next action:

- Test oligomerization mutants.
- Test lipid panel.
- Test accessory proteins.

---

# 12. Strongest overall conclusion that can be drawn from the packet alone

From the supplied packet alone, the strongest justified conclusion is:

**Inflammatory caspase cleavage of GSDMD and the cytotoxic activity of its N-terminal portion implicate GSDMD in pyroptotic cell death, but the packet does not establish whether the N-terminal fragment directly injures membranes or whether another cellular component executes membrane damage.**

The most valuable next step is therefore not additional genetic association alone, but a controlled test of direct membrane sufficiency using purified components.

---

# 13. Alternatives and limits

## 13.1 Alternative explanations for fragment-expression cytotoxicity

Fragment expression may:

1. Overwhelm protein quality-control systems.
2. Activate another cell-death pathway.
3. Alter membrane traffic indirectly.
4. Require an unidentified binding partner.
5. Produce nonphysiological localization.
6. Act only when expressed above a threshold not reached during endogenous cleavage.

These alternatives do not invalidate the fragment-expression evidence, but they prevent a direct-execution conclusion.

## 13.2 Alternative explanations for genetic-loss phenotypes

Genetic loss of GSDMD could affect:

1. Upstream signaling.
2. Inflammatory caspase activation thresholds.
3. Cytokine or danger-signal release.
4. Secondary cellular responses.
5. Other substrates or pathways not supplied in the packet.

Thus, genetic necessity does not establish physical execution.

## 13.3 Limits of proposed purified-system assays

Purified-system assays have their own limits:

1. They may miss required post-translational modifications.
2. They may miss required lipid asymmetry.
3. They may miss accessory proteins.
4. They may use nonphysiological protein concentrations.
5. They may fail to reproduce membrane tension or cytoskeletal constraints present in cells.
6. Dye-release assays may detect nonspecific destabilization rather than regulated pore formation.

Therefore, positive and negative outcomes must be interpreted together with cellular validation.

---

# 14. What would change the recommendation?

The recommendation to prioritize purified-membrane reconstitution would change if new evidence showed:

1. GSDMD-NT is unstable unless bound to a specific chaperone.  
   Then chaperone co-reconstitution would become a prerequisite.

2. GSDMD-NT requires a specific enzymatic modification before membrane activity.  
   Then the modification enzyme and modified fragment would need to be produced first.

3. GSDMD-NT acts only in a specific organelle membrane.  
   Then organellar lipid extracts or native membrane preparations would take priority.

4. A genetic screen identifies another required executioner.  
   Then the direct-execution hypothesis should be subordinated to testing that factor.

5. Fragment-expression toxicity is shown to correlate with non-membrane stress markers.  
   Then non-membrane mechanisms should be investigated before further membrane reconstitution.

---

# 15. Final concise statement

The packet establishes that inflammatory caspase processing of GSDMD is linked to pyroptotic death and that the N-terminal fragment carries cytotoxic activity. It does **not** establish the physical action of the fragment.

The most valuable next question is:

**Is purified GSDMD-NT sufficient to permeabilize defined membranes without additional cellular components?**

The proposed plan tests this with purified proteins, defined liposomes, binding and oligomerization assays, electrophysiology or imaging, and cellular validation. A positive outcome would support GSDMD-NT as a direct membrane-injury effector. A negative outcome would show that NT alone is not sufficient under tested conditions and would redirect work toward missing cofactors, lipid requirements, modifications, or alternative executioners. An ambiguous outcome would require additional controls and conditional experiments before any mechanistic conclusion is accepted.
