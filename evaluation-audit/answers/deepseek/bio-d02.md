# DeepSeek V4.1 Flash / bio-d02

Original final answer, shared by both scoring rounds.

All experiments below are **proposed**. The evidence packet does not provide exact buffer, ion, phosphate, protein, volume, dilution, or assay values; those must be calibrated, not assumed.

## 1. Useful conclusion / recommended next action

Use a matched reconstitution design in which a heat-stable fraction is added back to an enzyme-containing retentate under identical pH, ion, phosphate, protein, volume, dilution, and handling conditions. The decisive comparison is not simply “filtrate + retentate is active,” but **active heat-stable fraction versus a matched inactive analog** added to the same retentate, with a heat-labile retentate control and enzyme-integrity monitoring. If that contrast is positive, reproducible across independent separations, and abolished by the inactive analog, the conditional conclusion is that a heat-stable separable factor is required for fermentative activity in these fractions. The conclusion must remain limited to a required separable factor under these conditions; it must **not** claim chemical structure or NAD identity.

## 2. Evidence-to-inference chain

**Evidence packet states:** yeast-juice filtrate and retentate are separated and recombined; boiled extract is used to compensate; fractions are individually inactive while the combination restores activity; this supports a heat-stable separable factor. **Curator limit:** compensation is not chemical structure and does not alone determine NAD identity. **Artifacts listed:** pH, inorganic-salt, and phosphate changes during separation; enzyme damage or dilution compensated by nonspecific stabilizers.

**Inference:** if activity requires a heat-stable separable factor, then retentate alone should be inactive or strongly limited, and adding the heat-stable fraction should restore activity. That restoration must survive controls for pH, salts, phosphate, dilution, protein/volume mismatch, enzyme damage, and nonspecific stabilization.

**Conclusion to be tested conditionally:** a heat-stable separable factor is required for fermentative activity in the reconstituted yeast-juice fractions under matched conditions. This is not a structural identification and not an NAD claim.

## 3. Proposed operational protocol

### Step 1. Preparation and quality checks

1. Prepare independent yeast-juice-derived fermenting preparations from separate batches. Record batch identity, preparation time, temperature, handling, and any visible changes.
2. Before fractionation, confirm the parent preparation has fermentative activity above a calibrated threshold. The packet does not specify the assay; calibrate one (e.g., CO₂ evolution/manometry, pressure change, glucose consumption, or ethanol production).
3. Measure and record parent pH, conductivity, major ions, inorganic phosphate, protein concentration, volume, and turbidity.
4. Confirm enzyme integrity of the parent preparation using a validated sentinel enzyme assay if available. If no sentinel assay is validated, use the preparation’s ability to be reactivated by a saturating heat-stable fraction as the integrity readout, after calibration.
5. Exclude any batch that fails activity, pH stability, contamination, or enzyme-integrity checks. Document exclusions.

### Step 2. Calibration of unknown parameters before the main experiment

The packet does not supply these values; calibrate each:

- **Defined buffer B:** select a single-lot buffer and concentration that maintains target pH during fermentation without inhibiting activity or precipitating. If phosphate is not required, prefer a non-phosphate buffer and add phosphate separately; if phosphate is required, use phosphate buffer and match phosphate by measurement. Define Buffer B by its recorded identity, pH, concentration, and ionic strength.
- **pH target and control:** titrate parent juice across a pH range and measure fermentative activity. Choose the target pH. Use Buffer B plus pH stat or manual acid/base to keep pH within a narrow pre-specified range during incubation.
- **Ion add-back:** measure conductivity and major ions in filtrate and retentate. Prepare an ion add-back stock that matches the target ionic composition. If ion chromatography is unavailable, use conductivity and pH as calibrated surrogates.
- **Phosphate add-back:** measure inorganic phosphate in each fraction. Prepare a phosphate stock and add it so all groups reach the same final phosphate concentration. Calibrate whether phosphate is stimulatory, inhibitory, or neutral.
- **Protein target:** calibrate a protein assay with yeast-juice fractions. Choose a target total protein concentration that supports parent activity and is technically achievable across fractions.
- **Volume/dilution target:** determine the minimal volume and concentration that preserves parent activity. Use concentration or dialysis to bring fractions into range.
- **Heat treatment:** calibrate temperature and time that inactivate the retentate enzyme but preserve the heat-stable factor. Test a range. The desired condition is: boiled retentate loses activity; boiled heat-stable fraction retains reconstituting ability.
- **Inactive analog:** calibrate an independent depletion of the heat-stable fraction that removes reconstituting activity while preserving pH, ions, phosphate, protein, and volume. Examples of proposed approaches include adsorption, dialysis, or enzymatic treatment, but the exact method must be selected by calibration and verified to fail to restore retentate activity.
- **Separation method:** calibrate a method that yields an active heat-stable filtrate and an inactive or factor-dependent retentate. Record mass balance.
- **Fermentative activity assay:** calibrate linear range, detection limit, precision, and stability. Define primary activity units, e.g., CO₂ per mg protein per min or cumulative CO₂ per mg protein.
- **Dose of heat-stable fraction:** calibrate a dose–response curve for adding the heat-stable fraction to retentate. Choose a saturating dose for the primary contrast.

### Step 3. Fractionation and independent separation

For each independent yeast-juice batch:

1. Split the parent preparation into aliquots.
2. **Separation A:** fractionate into filtrate F and retentate R using the calibrated method. Record volumes, protein, pH, ions, phosphate, and activity.
3. **Separation B:** independently fractionate a separate aliquot using a second separation principle. The packet does not name the method; choose two independent principles after calibration, for example a membrane-based method and a non-membrane method. This yields F′ and R′.
4. **Mock separation:** subject a retentate aliquot to the same handling, time, temperature, shear, and dilution as R, but without the actual separation step. This produces R_mock for enzyme-damage control.
5. **Heat treatment:** prepare boiled aliquots of F, R, F′, R′, and R_mock using the calibrated heat condition. Verify the heat condition in calibration.
6. **Inactive analog:** prepare F_inactive from F by the calibrated depletion method. Then add-back pH, ions, phosphate, protein, and volume so F_inactive matches F as closely as possible. Verify in a pilot that F_inactive fails to restore R.
7. For every fraction and reconstitution group, measure pH, conductivity, major ions, inorganic phosphate, protein, and volume. Add Buffer B, ion stock, phosphate stock, and protein/volume adjusters to bring all groups to the same target values.

### Step 4. Reconstitution matrix and controls

All groups should be matched for final pH, ions, phosphate, total protein, volume, dilution, substrate concentration, temperature, and incubation time. If exact protein matching is impossible without adding a confounding protein, run a protein-dose response and include protein as a covariate.

Proposed groups:

1. **Parent juice:** positive control.
2. **Buffer alone:** negative control.
3. **R alone:** retentate only.
4. **F alone:** heat-stable fraction only.
5. **R + F:** active reconstitution.
6. **R + F_inactive:** inactive-analog control.
7. **R_boiled + F:** enzyme heat-lability control. Expected low if enzyme is required.
8. **R + F_boiled:** factor heat-stability control. Expected high if factor is heat-stable.
9. **R_boiled + F_boiled:** double heat control. Expected low.
10. **R_mock + F:** enzyme-damage control. Compare with R + F.
11. **R′ + F′:** independent separation replicate.
12. **R′ + F′_inactive:** independent inactive-analog control.

Add an inert-protein-only control if an inert protein is used for matching.

### Step 5. Allocation, blinding, and independent units

- Treat each independent yeast-juice batch as an independent biological unit. Use at least three independent batches, or more if assay variability requires it.
- Within each batch, use technical replicates per group.
- Code all tubes and randomize assay order. Keep the analyst blinded to group identity until measurements are locked.
- Pre-specify exclusion criteria for batches, runs, and outliers before unblinding.
- Use blocked analysis by batch.

### Step 6. Intervention and sampling

1. Add a calibrated fermentable substrate if required by the preparation. The packet does not specify substrate; measure endogenous substrate and match or add a saturating calibrated amount.
2. Incubate all groups at the calibrated temperature with mixing if appropriate.
3. Maintain pH with Buffer B and pH stat or calibrated manual adjustment.
4. Sample at pre-specified intervals for primary activity and secondary measurements.
5. At the end of incubation, measure final pH, ions, phosphate, protein, and enzyme integrity.

### Step 7. Measurements

**Primary:** fermentative activity, measured by the calibrated assay, expressed per mg protein and per volume.

**Secondary:** glucose consumption, ethanol production, CO₂ evolution if not primary, pH, conductivity, major ions, inorganic phosphate, protein concentration, volume, turbidity, and enzyme-integrity readouts.

**Enzyme-integrity monitoring:** measure retentate reactivation capacity with saturating F before and after fractionation, and compare R + F with R_mock + F. If available, measure a validated sentinel enzyme activity in R before and after handling. Only use batches where retentate can be reactivated to a calibrated level.

### Step 8. Analysis and quantitative primary contrast

Define the primary contrast as:

\[
\Delta_{\text{primary}} = A(R + F_{\text{active}}) - A(R + F_{\text{inactive}})
\]

where \(A\) is fermentative activity under matched pH, ions, phosphate, protein, volume, dilution, substrate, temperature, and handling conditions.

Also define a secondary reconstitution contrast:

\[
\Delta_{\text{recon}} = A(R + F_{\text{active}}) - [A(R) + A(F_{\text{active}})]
\]

Analyze with a mixed-effects model:

\[
A \sim \text{group} + (1|\text{batch})
\]

Use pre-specified contrasts. Report effect sizes with confidence intervals. If pH, ions, phosphate, or protein are not perfectly matched, include them as covariates in a sensitivity analysis.

Pre-specify the acceptance threshold after calibration. A reasonable proposed rule: \(\Delta_{\text{primary}}\) must exceed the calibrated assay noise, for example greater than three standard deviations of the matched negative control and at least a calibrated fraction of parent-juice activity. The exact threshold is a calibration output, not an assumed number.

### Step 9. Acceptance and stopping criteria

**Accept the conditional requirement if:**

- Parent positive control exceeds the calibrated activity threshold.
- Negative controls are below the calibrated detection limit.
- \(\Delta_{\text{primary}}\) exceeds the pre-specified threshold.
- The effect is reproduced with independent separation B.
- Heat controls show the expected pattern: R + F active, R_boiled + F low, R + F_boiled active if the factor is heat-stable.
- The inactive analog fails to restore activity.
- Enzyme-integrity checks show R and R_mock behave comparably when supplemented with F.
- pH, ions, phosphate, protein, volume, and dilution are matched or adjusted in analysis.

**Stop or reinterpret if:**

- Parent juice fails activity or pH control.
- Contamination or precipitation occurs.
- pH drifts outside the calibrated range.
- Enzyme integrity fails in R or R_mock.
- The inactive analog retains reconstituting activity, indicating failed depletion.
- \(\Delta_{\text{primary}}\) is not distinguishable from noise.

### Step 10. Troubleshooting

- **No parent activity:** check substrate, pH, ions, phosphate, temperature, and enzyme integrity.
- **R + F inactive:** check dose of F, heat-treatment calibration, pH/ion/phosphate mismatch, and retentate damage.
- **Inactive analog still active:** depletion failed; recalibrate with a different independent method.
- **High variability:** increase independent batches, use batch blocking, and standardize handling time and temperature.
- **pH drift:** use stronger Buffer B or pH stat; verify buffer does not inhibit.
- **Protein mismatch:** use concentration/dilution; if impossible, use protein-dose response and covariate adjustment.
- **Enzyme damage suspected:** shorten handling, reduce shear/temperature, use R_mock, and require a calibrated reactivation threshold before including a batch.

## 4. Alternatives and limits

The design can exclude pH, salt, phosphate, dilution, and enzyme-damage alternatives only if those variables are measured and matched. Even then, residual alternatives remain:

- The factor may be incompletely separated and present in both fractions.
- Heat treatment may alter more than the intended factor.
- The inactive analog may differ in unidentified ways despite matching measured variables.
- Reconstitution may not equal the original yeast-juice state.
- The activity assay may not be linear or may measure a downstream effect.
- Nonspecific stabilizers may still contribute if the heat-stable fraction contains unmeasured protective molecules.
- The packet does not identify the factor’s chemical structure; therefore no structural conclusion is justified.
- The packet does not establish NAD identity; the protocol must not claim it.

## 5. Conditional conclusion

If the primary contrast is positive, reproducible across independent separations, abolished by the matched inactive analog, and accompanied by the expected heat and enzyme-integrity controls, the conditional conclusion is:

**Under these matched conditions, a heat-stable separable factor from the yeast-juice filtrate/boiled extract is required for fermentative activity in the retentate fraction.**

This conclusion is limited to a required separable factor. It does **not** identify chemical structure, and it does **not** establish that the factor is NAD. If the criteria are not met, the conclusion is that the requirement is not demonstrated under these conditions, and the listed alternatives remain unresolved.
