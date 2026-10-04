# Qwen3.8 Max (0902) / bio-r01

Original final answer, shared by both scoring rounds.

## Recommended next action

The next decisive test is to **impose calibrated rotation of the γ coordinate** on the surface-anchored F₁ preparation while **directly measuring de novo ATP formation from ADP and inorganic phosphate**. The central manipulation should be mechanical: command γ rotation in the direction opposite to the ATP-driven direction, measure the mechanical work actually delivered, and ask whether ATP appears only under the conjunction of active F₁, ADP, phosphate, and reverse rotation.

The strongest version of the experiment should not rely on a single optical ATP reporter. It should combine:

1. **Controlled mechanical input**: closed-loop magnetic or optical torque application to the γ-linked actin marker or an equivalent γ-attached handle.  
2. **Direct chemical output**: offline HPLC or LC–MS/MS quantification of ATP, preferably with isotopically labeled phosphate to prove newly formed ATP rather than pre-existing ATP.  
3. **Auxiliary time-resolved output**: a calibrated luminescent or fluorescent ATP readout, used only as a secondary signal and validated against the chemical assay.

A clean positive result would be: **ATP is produced only when active F₁, ADP, phosphate, and reverse γ rotation are all present; the product is chemically identified as ATP; production scales with imposed angular displacement or mechanical work; and all no-enzyme, no-substrate, wrong-direction, inactive-enzyme, and field-only controls remain negative.** That pattern would support reversible mechanochemical coupling. Any result lacking this conjunction would be insufficient and could be explained by contamination, drift, nonspecific nucleotide release, or readout artifacts.

This is a proposed experiment; no proposed results are claimed as observed.

---

## Evidence-to-inference-to-conclusion chain

### Evidence supplied

A surface-anchored F₁ preparation carries a fluorescent actin marker attached to its central γ subunit. In ATP-containing solution, the marker exhibits sustained directional rotation.

### Inference supported by that evidence

The observation supports the inference that **chemical fuel availability can be converted into directional mechanical motion** in isolated F₁. Because the rotation is directional rather than purely diffusive, the system has a chemically biased mechanical cycle under the tested conditions.

### What the evidence does not establish

The supplied observation does not establish:

1. Whether imposing motion on the γ coordinate can drive the reverse chemical reaction.  
2. Whether ATP is produced when γ is externally rotated.  
3. Whether the chemical-to-mechanical coupling is reversible or functionally rectified under the tested conditions.  
4. Whether the observed rotation is tightly coupled to a defined chemical stoichiometry.  
5. Whether any future ATP signal would arise from true synthesis rather than contamination, release of pre-bound nucleotide, or assay artifacts.

### Mechanistic conclusion for the next step

The next experiment must invert the perturbation: instead of adding ATP and observing rotation, it must **control rotation and observe ATP chemistry**. The unresolved question is therefore whether γ rotation is not merely an output of ATP availability but also a sufficient control variable for reversing catalytic operation.

---

## Unresolved biological question

**Can controlled rotation of the γ subunit, in the direction opposite to ATP-driven rotation, drive ATP formation from ADP and inorganic phosphate in surface-anchored F₁?**

More specifically:

1. Is the ATP signal dependent on the direction of imposed γ rotation?  
2. Is it dependent on ADP and phosphate?  
3. Is it dependent on active F₁?  
4. Does the amount of ATP formed scale with imposed angular displacement, torque, or mechanical work?  
5. Can the product be chemically identified as newly synthesized ATP rather than contaminating ATP or released bound nucleotide?

---

## Competing mechanisms and distinct predictions

### 1. Reversible mechanochemical coupling

**Mechanism:** γ rotation and catalytic state are conjugated. ATP hydrolysis drives rotation in one direction; externally imposed rotation in the opposite direction drives the reverse chemical reaction, ATP formation from ADP and phosphate.

**Predictions:**

- ATP appears only when active F₁, ADP, phosphate, and reverse rotation are present.  
- Same-direction rotation produces little or no ATP under ATP-free conditions.  
- No-enzyme, inactive-enzyme, no-ADP, and no-phosphate controls give no ATP.  
- ATP production increases with imposed revolutions or mechanical work, within a viable range.  
- If labeled phosphate is used, the ATP product contains the label.  
- The signal is confirmed by orthogonal chemical analysis, not only by an optical reporter.

### 2. Irreversible or rectified chemo-mechanical operation

**Mechanism:** ATP hydrolysis can drive rotation, but imposed reverse rotation does not efficiently drive ATP synthesis under the tested conditions. The motor may slip, stall, denature, or undergo nonproductive mechanical deformation.

**Predictions:**

- No reproducible ATP formation occurs during reverse rotation despite verified mechanical input and enzyme activity in a separate ATP-driven rotation test.  
- If ATP appears, it is not direction-dependent, not phosphate-dependent, or not proportional to mechanical work.  
- The result may reflect damage or nonspecific nucleotide release rather than reversible catalysis.

### 3. Contamination or side enzymatic activity

**Mechanism:** ATP is already present in reagents, is released from damaged proteins, or is generated by contaminating enzymes such as adenylate kinase-like activities.

**Predictions:**

- ATP is detected in no-F₁ controls.  
- ATP is present before rotation or appears independently of rotation.  
- ATP appears without phosphate, suggesting conversion of adenine nucleotides rather than phosphate-dependent synthesis.  
- ATP appears in both rotation directions.  
- If labeled phosphate is used, the ATP remains unlabeled.  
- ATP concentration may correlate with reagent batch or enzyme concentration but not with mechanical work.

### 4. Mechanical drift or false rotation assignment

**Mechanism:** Apparent γ rotation is caused by stage drift, bead drift, surface movement, or incorrect reference-frame subtraction rather than true enforced γ rotation.

**Predictions:**

- Apparent angular displacement persists when fiduciary markers are moving.  
- The commanded field phase and measured γ angle are not locked.  
- Estimated mechanical work is near zero despite apparent angle change.  
- Chemical output, if any, does not depend on verified torque or work.  
- Inactive or no-enzyme controls may show similar apparent motion.

### 5. Readout artifact

**Mechanism:** The ATP reporter signal changes because of magnetic field, bead position, scattering, photobleaching, temperature, pH, or detector instability rather than because ATP concentration changes.

**Predictions:**

- Optical ATP signal changes during field application even without enzyme or substrates.  
- The signal appears immediately with field changes rather than accumulating as a chemical product.  
- HPLC or LC–MS/MS does not confirm ATP.  
- Field-only or bead-only controls reproduce the optical signal.  
- Spike-recovery controls show quenching or distortion.

---

## Proposed experimental design: overview

Use the existing surface-anchored F₁ system but add a mechanical handle that allows externally controlled γ rotation. The actin marker can serve as both a fluorescent angular reporter and a mechanical lever if a magnetic bead or equivalent handle is attached to it. Alternatively, a separate γ-linked magnetic handle can be used while retaining a fluorescent marker for angle readout.

The preparation is placed in an ATP-free solution containing ADP and inorganic phosphate. A calibrated rotating field imposes γ rotation. The direction is defined relative to the ATP-driven direction observed in a calibration step. Mechanical work is measured. Chemical samples are collected over time and analyzed directly for ATP. A subset of experiments uses labeled phosphate to demonstrate de novo phosphate incorporation into ATP.

The core design is factorial:

| Active F₁ | ADP | Pi | Rotation direction | Expected for reversible coupling |
|---|---:|---:|---|---|
| Yes | Yes | Yes | Reverse | ATP formation |
| Yes | Yes | Yes | Same | Little or no ATP |
| Yes | Yes | Yes | None | No ATP above baseline |
| Yes | No | Yes | Reverse | No ATP |
| Yes | Yes | No | Reverse | No ATP |
| No | Yes | Yes | Reverse | No ATP |
| Inactive | Yes | Yes | Reverse | No ATP |
| Yes | Yes | Yes | Reverse, but no net work | No ATP |

---

## Detailed proposed protocol

### 1. Preparation and mechanical manipulation

#### 1.1 Surface-anchored F₁ with γ-linked probe

Use the supplied surface-anchored F₁ preparation in which the γ subunit carries a fluorescent actin marker. For controlled energy input, attach a magnetic or optically tractable handle to the same γ-linked structure.

One possible implementation:

- Keep the fluorescent actin marker as the angular reporter.  
- Attach a small superparamagnetic bead or magnetic nanorod to the actin marker through a specific linkage, for example biotin–streptavidin or an antibody against actin, depending on the available labeling chemistry.  
- Use a short and stiff actin segment if pilot calibration shows that long filaments introduce excessive torsional compliance.  
- Passivate the surface to prevent nonspecific bead or protein attachment.

The exact geometry, bead size, filament length, linkage chemistry, and surface density are operational parameters that must be validated. They should not be assumed from the initial observation.

#### 1.2 Orientation control

For ensemble chemical measurements, the direction of ATP-driven rotation must be known and uniform across the active population. If F₁ molecules are randomly oriented, reverse rotation for one molecule may be forward rotation for another, and bulk ATP signals will be ambiguous.

Procedure:

1. Introduce a brief, low ATP concentration calibration pulse.  
2. Record the direction of rotation for a representative subset of molecules.  
3. Define the ATP-driven direction as the positive direction, +θ.  
4. Wash out ATP thoroughly.  
5. Accept the preparation for bulk synthesis measurement only if the active population has a strongly biased orientation, for example a predefined majority rotating in the same direction during calibration. The exact acceptance threshold is a parameter to be set during pilot validation.  
6. If orientation is not sufficiently uniform, either improve oriented immobilization or restrict analysis to single-molecule chambers where each molecule’s direction can be assigned individually.

#### 1.3 Controlled energy input

Use a two-axis magnetic field generator, magnetic tweezers, or an optical torque wrench to impose rotation.

Primary control mode:

- **Angular position clamp**: command γ angle as a function of time,  
  \[
  θ_{\gamma}^{\text{command}}(t) = θ_0 + sωt
  \]
  where \(s = +1\) for the ATP-driven direction and \(s = -1\) for the reverse direction.  
- Use real-time image feedback to adjust the applied field so that the measured γ angle follows the command.  
- Record the torque required to maintain the commanded motion.  
- Compute mechanical work per enzyme or per bead ensemble as  
  \[
  W = \int τ_{\gamma}(t)\,dθ_{\gamma}(t)
  \]
  after correcting for linker compliance and viscous dissipation where possible.

Secondary control modes:

- **Torque clamp**: impose a constant torque and measure resulting angular velocity.  
- **Work-controlled epochs**: rotate until a target integrated work has been delivered.  
- **Zero-net-rotation control**: apply oscillatory torque or equal forward and reverse rotations so that total angular displacement is zero. This tests whether any chemical output requires net directional cycling rather than merely mechanical agitation.

The independent mechanical variables are:

- Direction, \(s\).  
- Angular displacement, total revolutions.  
- Angular velocity, \(ω\).  
- Applied torque, \(τ\).  
- Integrated work, \(W\).

The measured output is ATP concentration, ATP production rate, and, if labeled phosphate is used, labeled ATP formation.

---

### 2. Reaction components and chemical output

#### 2.1 Baseline reaction mixture for attempted synthesis

The synthesis-attempt solution should contain:

- Surface-anchored F₁ with γ probe.  
- ADP at a defined concentration.  
- Inorganic phosphate at a defined concentration.  
- Appropriate buffer, salt, and divalent cation conditions. The exact buffer composition, pH, ionic strength, and cofactor requirements are parameters to be validated.  
- No added ATP at the start.  
- Optional: pretreatment of ADP and phosphate stocks with an ATP-removing enzyme, followed by removal or inactivation of that enzyme before the assay. This reduces contaminating ATP but must be validated so that it does not damage F₁ or alter ADP/Pi.

The exact ADP and phosphate concentrations are not fixed by the supplied evidence. They must be chosen through pilot experiments and reported as validated parameters.

#### 2.2 Primary direct chemical readout: HPLC or LC–MS/MS

The primary chemical output should be measured by direct separation and quantification of adenine nucleotides.

Recommended procedure:

1. Collect timed aliquots from the reaction chamber or flow path during mechanical manipulation.  
2. Immediately quench samples to stop enzymatic activity. Quench method, pH change, and compatibility with detection must be validated.  
3. Separate ATP, ADP, and AMP by HPLC or LC–MS/MS.  
4. Quantify ATP using external standards and internal standards prepared in the same reaction matrix.  
5. Report retention time, mass transition, peak area, concentration, limit of detection, and limit of quantification.  
6. If possible, measure ADP and phosphate consumption in parallel to test stoichiometric consistency.

This assay is preferred over a purely optical ATP reporter because it provides chemical identity and is less susceptible to field- or bead-related optical artifacts.

#### 2.3 Isotopic phosphate labeling to prove de novo synthesis

To distinguish true synthesis from contaminating ATP or released pre-bound ATP, include experiments with isotopically labeled phosphate.

Possible implementations:

- Stable-isotope-labeled phosphate, detected by LC–MS/MS.  
- Radiolabeled phosphate, detected after separation by scintillation counting or phosphor imaging, if appropriate safety and validation are available.

Prediction for true synthesis:

- Reverse rotation in the presence of labeled phosphate produces labeled ATP.  
- No-enzyme and inactive-enzyme controls do not produce labeled ATP.  
- Pre-existing contaminating ATP remains predominantly unlabeled.

This is one of the strongest discriminating measurements because contamination can produce ATP signal but cannot easily produce phosphate-dependent isotopic incorporation into ATP.

#### 2.4 Auxiliary time-resolved ATP readout

A continuous or semi-continuous optical ATP reporter may be used for high time resolution, but it should not be the sole evidence.

Possible reporters:

- Luciferin–luciferase luminescence.  
- A fluorescent ATP-binding biosensor, if compatible with the mechanical assay and validated not to perturb the reaction.

Required calibrations:

- ATP standard curve in the exact reaction mixture.  
- Reporter response time.  
- Reporter consumption of ATP, if any.  
- Effect of magnetic field, bead position, scattering, pH, and temperature on reporter signal.  
- Spike-recovery tests to verify that added ATP is detected quantitatively.

If the optical reporter gives a signal but LC–MS/HPLC does not confirm ATP, treat the result as an artifact until proven otherwise.

---

## Calibration

### 1. Direction calibration

Define the coordinate system explicitly.

Let the optical axis be \(z\), pointing from the surface into solution. Let \(θ\) be the in-plane angular coordinate of the fluorescent actin marker. Define:

- **+θ**: the direction of sustained γ-linked rotation observed when ATP is present during the calibration pulse.  
- **−θ**: the opposite direction, used as the candidate ATP-synthesis direction.

This convention is empirical. It does not assume a universal structural handedness. It uses the ATP-driven direction observed in the same preparation as the reference.

If the preparation is used for bulk chemical measurement, the population must be orientation-homogeneous. If single-molecule chemical detection is used, each molecule can be assigned its own +θ and −θ.

### 2. Mechanical calibration

Calibrate the following before interpreting chemical output.

#### 2.1 Angular tracking

- Determine the angular position of the fluorescent actin marker as a function of time.  
- Use fiduciary surface markers to subtract stage drift.  
- Validate angular unwrapping over multiple revolutions.  
- Determine the angular resolution and the maximum resolvable velocity.

#### 2.2 Torque calibration

For magnetic handles:

- Calibrate bead or rod magnetic moment.  
- Calibrate applied field amplitude and phase.  
- Estimate torque from the field–handle interaction or from rotational drag at known angular velocity.  
- Validate torque using thermal fluctuation analysis, stall tests, or known viscous loads.

For optical torque:

- Calibrate trap stiffness and torque from trapped-handle angular fluctuations or known standards.

#### 2.3 Linker compliance

The handle and actin marker may twist relative to γ.

Measure:

- Phase lag between handle angle and fluorescent actin angle during oscillatory driving.  
- Apparent torsional stiffness of the γ–actin–handle linkage.  
- Whether the fluorescent actin marker reports γ angle faithfully under load.

If compliance is large, the commanded handle angle is not identical to the γ angle. In that case, use feedback based on the fluorescent marker angle or correct the mechanical work calculation using the measured compliance.

#### 2.4 Energy input calibration

Compute the mechanical energy delivered to the enzyme as:

\[
W = \int τ_{\gamma}\,dθ_{\gamma}
\]

Do not assume that the commanded handle angle equals energy input. Torque and actual γ displacement must both be measured or inferred through validated calibration.

### 3. Chemical calibration

Calibrate the chemical assay under conditions matching the experiment.

Required chemical calibrations:

- ATP standard curve in reaction buffer.  
- ATP standard curve in the presence of ADP, phosphate, surface material, beads, and F₁ preparation if possible.  
- Recovery of known ATP spikes from reaction samples.  
- Limit of detection and limit of quantification.  
- Linearity range.  
- Isotopic natural-abundance correction if labeled phosphate is used.  
- Stability of ATP, ADP, and phosphate during sampling and quenching.  
- Active enzyme count or active enzyme fraction, estimated from a separate ATP-driven rotation assay or another validated activity measurement.

### 4. Active enzyme calibration

A negative result is hard to interpret if the enzyme is inactive. Therefore, after the synthesis-attempt epoch, perform a positive mechanical control:

1. Wash out ADP/phosphate.  
2. Add ATP-containing solution.  
3. Verify that the same molecules or preparation still rotate directionally.  
4. Record rotation direction and speed.  
5. If possible, estimate the number of active molecules from rotating fluorescent markers.

If the enzyme fails this post-test, a negative synthesis result cannot distinguish irreversibility from loss of activity.

---

## Counterfactual controls

The following controls are essential. Each should be run with the same time course, sampling, detector settings, and mechanical commands as the test condition unless otherwise noted.

### 1. No-F₁ control

Components:

- Surface, beads, actin handle if present, ADP, phosphate, buffer.  
- No F₁.

Manipulation:

- Reverse rotation command applied to beads or handles if present.

Purpose:

- Detect contaminating ATP.  
- Detect field-, bead-, or surface-induced chemical artifacts.  
- Detect optical reporter artifacts.

Expected for reversible coupling: no ATP above baseline.

### 2. Inactive-F₁ control

Components:

- F₁ rendered inactive by heat, chemical denaturation, or a validated catalytically inactive variant if available.

Manipulation:

- Reverse rotation.

Purpose:

- Test whether ATP formation requires catalytically competent F₁ rather than merely the presence of protein or mechanical movement.

Expected for reversible coupling: no ATP above baseline.

### 3. No-ADP control

Components:

- Active F₁, phosphate, buffer, no added ADP.

Manipulation:

- Reverse rotation.

Purpose:

- Test whether ATP formation requires ADP.  
- Detect contaminating ADP or phosphate-independent side reactions.

Expected for reversible coupling: no ATP, or only a small signal explainable by measured contaminating ADP.

### 4. No-phosphate control

Components:

- Active F₁, ADP, buffer, no added phosphate.

Manipulation:

- Reverse rotation.

Purpose:

- Test whether ATP formation requires phosphate.  
- Detect adenine-nucleotide-only side reactions, such as contaminating adenylate kinase-like activity.  
- Detect release of preformed ATP.

Expected for reversible coupling: no phosphate-dependent ATP formation. If ATP appears here, contamination or nucleotide release is likely.

### 5. Same-direction rotation control

Components:

- Active F₁, ADP, phosphate.

Manipulation:

- Impose +θ rotation, the ATP-driven direction.

Purpose:

- Test direction specificity.

Expected for reversible coupling: little or no ATP formation under ATP-free conditions, or at least a strong asymmetry favoring reverse rotation. If both directions produce ATP equally, direction-specific reversible coupling is not established.

### 6. No-rotation control

Components:

- Active F₁, ADP, phosphate.

Manipulation:

- Same chamber and time course but no imposed rotation.

Purpose:

- Measure baseline chemical drift, slow contamination, spontaneous nucleotide exchange, or detector drift.

Expected for reversible coupling: no ATP increase beyond baseline.

### 7. Zero-net-rotation control

Components:

- Active F₁, ADP, phosphate.

Manipulation:

- Apply oscillatory or equal forward/reverse rotation so that net angular displacement is zero while exposing the system to comparable mechanical stress.

Purpose:

- Test whether ATP formation requires net directional cycling rather than nonspecific mechanical perturbation.

Expected for reversible coupling: little or no ATP compared with reverse rotation of the same total mechanical exposure.

### 8. Field-only and bead-only optical controls

Components:

- Reporter mixture, beads, surface, but no F₁ or no substrates.

Manipulation:

- Apply magnetic or optical fields used in test conditions.

Purpose:

- Detect field-dependent changes in luminescence, fluorescence, scattering, or detector baseline.

Expected for reversible coupling: no ATP-like signal.

### 9. ATP spike-recovery control

Components:

- Reaction mixture with or without F₁.

Manipulation:

- Add known ATP at known times.

Purpose:

- Verify that ATP is not adsorbed, degraded, quenched, or masked by the assay mixture.  
- Validate quantitative recovery.

Expected: recovery near 100% within validated error.

### 10. Post-experiment activity control

Components:

- Same F₁ preparation after synthesis attempt.

Manipulation:

- Add ATP and observe directional rotation.

Purpose:

- Confirm that the mechanical coordinate remained functional.  
- Prevent misinterpretation of negative synthesis results due to inactive enzyme.

Expected: directional rotation in the previously assigned +θ direction.

---

## Time-resolved measurement scheme

A representative sequence for each experimental unit is:

### Phase 0: Preparation and baseline verification

1. Assemble chamber with surface-anchored F₁ and γ-linked handle.  
2. Wash into ATP-free synthesis buffer containing ADP and phosphate.  
3. Record baseline mechanical data: γ angle, fiducial markers, bead/handle position.  
4. Record baseline chemical signal: optical reporter if used, and collect a time-zero sample for HPLC/LC–MS.  
5. Verify that ATP at time zero is below the predefined limit of quantification.

### Phase 1: Direction calibration

1. Briefly introduce ATP.  
2. Record rotation direction.  
3. Assign +θ as the ATP-driven direction.  
4. Wash out ATP thoroughly.  
5. Return to ATP-free ADP/phosphate buffer.  
6. Confirm that chemical baseline is stable.

This calibration may be omitted for a given trial only if orientation has already been established by a validated, preparation-level protocol.

### Phase 2: Reverse-rotation synthesis attempt

1. Command γ rotation in the −θ direction.  
2. Record:
   - γ angle.  
   - Handle angle.  
   - Applied field or trap parameters.  
   - Estimated torque.  
   - Fiducial drift.  
   - Optical ATP reporter signal, if used.  
3. Collect chemical samples at multiple times, for example at predefined intervals throughout the rotation epoch. The exact interval is a parameter to be determined by expected signal size and detector sensitivity.  
4. Continue for a predefined number of revolutions or integrated work target.

### Phase 3: Wash or pause

1. Stop rotation.  
2. Record chemical baseline and mechanical stability.  
3. Collect post-rotation sample.

### Phase 4: Same-direction or alternative-direction control

1. In a randomized order, impose +θ rotation, zero-net rotation, or no rotation.  
2. Use the same sampling scheme.  
3. Compare chemical output with reverse rotation.

### Phase 5: Positive mechanical control

1. Add ATP.  
2. Verify rotation.  
3. Record direction and speed.  
4. Optionally measure ATP hydrolysis-associated chemical changes if relevant.

### Phase 6: Terminal chemical validation

1. Collect final sample.  
2. Spike a subset with known ATP to test recovery.  
3. Analyze all samples by HPLC or LC–MS/MS.  
4. If labeled phosphate was used, analyze isotopologue distribution.

All mechanical and chemical timestamps should be synchronized using hardware triggers or a common time base.

---

## Replication and analysis

### 1. Replication hierarchy

Distinguish biological, technical, and analytical replicates.

- **Independent protein preparations**: at least multiple independent F₁ preparations, with the exact number set by pilot variability and power analysis.  
- **Independent chambers or flow cells**: multiple chambers per preparation.  
- **Multiple fields of view or single-molecule records**: where applicable.  
- **Repeated analytical injections**: for HPLC/LC–MS samples, but these are analytical replicates, not independent biological evidence.

Do not treat repeated measurements from the same chamber as independent biological replicates.

### 2. Randomization and blinding

- Randomize the order of direction conditions across chambers and days.  
- Randomize sample labels before chemical analysis.  
- Blind the chemical analysis to condition identity where practical.  
- Predefine exclusion criteria before data collection.

### 3. Mechanical data analysis

For each record:

1. Subtract fiducial drift.  
2. Extract γ angle \(θ_{\gamma}(t)\).  
3. Compute angular velocity \(ω(t)\).  
4. Compute total revolutions.  
5. Compute torque \(τ(t)\) from calibrated field/handle relationship.  
6. Compute mechanical work \(W\).  
7. Flag records with excessive drift, loss of tracking, detachment, or failure to follow the commanded angle.

Predefine acceptance criteria. For example, a record may be required to achieve a minimum fraction of commanded revolutions and maintain fiducial drift below a validated threshold. These thresholds are operational parameters, not assumptions.

### 4. Chemical data analysis

For each sample:

1. Convert detector response to ATP concentration using matrix-matched calibration.  
2. Subtract baseline where appropriate.  
3. Subtract no-enzyme and no-rotation backgrounds using the predefined statistical model.  
4. If using labeled phosphate, compute labeled ATP fraction and correct for natural isotope abundance.  
5. Estimate ATP production rate over each time interval.  
6. If active enzyme number is known, estimate ATP per active enzyme per unit time or per revolution.

### 5. Statistical model

A suitable model should include fixed effects and random effects. Conceptually:

\[
\text{ATP rate}_{ijk} =
β_0
+ β_1(\text{active F1})
+ β_2(\text{ADP})
+ β_3(\text{Pi})
+ β_4(\text{reverse rotation})
+ β_5(\text{active F1} \times \text{ADP} \times \text{Pi} \times \text{reverse rotation})
+ \text{random effects}_{\text{prep/chamber}}
+ ε
\]

The key term is the full interaction: ATP formation should require the conjunction of active F₁, ADP, phosphate, and reverse rotation.

Secondary analyses:

- Regression of ATP amount on imposed revolutions.  
- Regression of ATP amount on mechanical work.  
- Comparison of reverse versus same direction.  
- Comparison of labeled ATP in labeled-phosphate experiments.  
- Equivalence testing for negative controls to show they are not merely underpowered.

### 6. Predefined decision thresholds

Before running the experiment, define:

- Minimum detectable ATP rate.  
- Minimum acceptable signal-to-noise ratio.  
- Required separation between test condition and controls.  
- Required consistency across independent preparations.  
- Criteria for accepting a negative result, including post-experiment enzyme activity and adequate chemical sensitivity.

These thresholds should be based on pilot calibration, not on desired outcomes.

---

## How the complete result pattern discriminates among mechanisms

### Pattern supporting reversible mechanochemical coupling

A result would support reversible coupling if all of the following are true:

1. **Chemical identity confirmed**: HPLC or LC–MS/MS identifies the product as ATP.  
2. **Substrate dependence**: ATP formation requires ADP and phosphate.  
3. **Enzyme dependence**: no-F₁ and inactive-F₁ controls show no comparable ATP formation.  
4. **Direction dependence**: reverse rotation produces ATP; same rotation produces substantially less or none.  
5. **Work dependence**: ATP amount increases with imposed angular displacement or mechanical work over the tested range.  
6. **Isotopic confirmation**: when labeled phosphate is used, the ATP product contains the label.  
7. **Temporal behavior**: ATP accumulates during reverse rotation and does not accumulate during no-rotation or zero-net-rotation periods.  
8. **Mechanical validity**: fiducial drift is small, γ angle follows command, torque is nonzero, and post-test ATP-driven rotation confirms enzyme activity.  
9. **Control negativity**: no-ADP, no-phosphate, no-enzyme, inactive-enzyme, field-only, and no-rotation controls remain below the predefined threshold.  
10. **Orthogonal consistency**: optical ATP reporter, if used, agrees with direct chemical quantification.

This pattern would discriminate reversible coupling from contamination because contamination would not require active F₁, ADP, phosphate, and reverse rotation simultaneously. It would discriminate from mechanical drift because the chemical output would depend on verified work and direction. It would discriminate from readout artifacts because direct chemical analysis would confirm ATP and isotopic labeling would confirm de novo synthesis.

### Pattern indicating contamination

Contamination is likely if:

- ATP is present at time zero before rotation.  
- ATP appears in no-F₁ controls.  
- ATP appears without phosphate.  
- ATP appears equally in reverse and same directions.  
- ATP appears without net rotation.  
- ATP does not incorporate labeled phosphate.  
- ATP concentration correlates with reagent age or enzyme stock but not mechanical work.  
- HPLC/LC–MS shows ATP in samples where the optical reporter is negative, or vice versa, in a way inconsistent with calibration.

In that case, the result cannot be interpreted as reversible mechanochemical coupling.

### Pattern indicating mechanical drift

Mechanical drift is likely if:

- Apparent γ rotation occurs without applied field or with field phase inconsistent with the angle trace.  
- Fiduciary markers move with the same apparent angular signature.  
- Calculated torque or work is near zero despite apparent angular displacement.  
- Rotation records disappear after fiducial correction.  
- Chemical output, if any, is not correlated with verified work.  
- No-rotation controls show similar apparent angular changes.

Drift can produce false mechanical input but should not produce a substrate- and direction-dependent ATP signal unless accompanied by another artifact.

### Pattern indicating readout artifact

Readout artifact is likely if:

- The optical ATP signal changes during field application in no-enzyme or no-substrate controls.  
- The signal changes instantaneously with field switching rather than accumulating chemically.  
- Bead position or magnetic field changes luminescence or fluorescence in calibration samples lacking ATP.  
- Spike recovery is poor or variable with field state.  
- HPLC/LC–MS fails to confirm ATP despite a positive optical signal.  
- The signal disappears when detector settings, optical path, or reporter concentration is altered, even though mechanical input is unchanged.

A positive optical signal alone is therefore insufficient. Direct chemical confirmation is necessary.

---

## Conditional conclusions

### Positive conclusion

If reverse γ rotation produces ATP only when active F₁, ADP, and phosphate are present; the ATP is confirmed by direct chemical analysis; labeled phosphate is incorporated; and all relevant controls are negative, then the conclusion is:

**The γ coordinate is mechanically sufficient to drive reverse catalytic operation under the tested conditions. The F₁ preparation exhibits reversible mechanochemical coupling between γ rotation and ATP chemistry.**

This conclusion would still be bounded by the experimental conditions. It would not by itself establish physiological regulation, native efficiency, or behavior in a complete membrane-embedded complex. It would, however, directly answer the next mechanistic question.

### Negative conclusion

If no ATP is detected during reverse rotation despite verified mechanical input and post-experiment ATP-driven rotation, the conclusion is limited:

**Under the tested conditions, controlled γ rotation did not measurably drive ATP synthesis.**

This would not prove that F₁ is fundamentally irreversible. Possible explanations include:

- Insufficient torque or inappropriate angular velocity.  
- Excessive compliance in the mechanical linkage.  
- Loss of catalytic competence under the synthesis-attempt conditions.  
- Missing chemical components or incorrect chemical potentials.  
- Inadequate detection sensitivity.  
- True kinetic rectification under these conditions.

A negative result should be accepted as strong only if the assay sensitivity, enzyme activity, and mechanical delivery have all been validated.

### Ambiguous conclusion

The result is ambiguous if:

- ATP appears but also appears in controls.  
- ATP appears without phosphate or without active F₁.  
- ATP appears equally in both directions.  
- Optical reporter and direct chemical assay disagree.  
- Mechanical work cannot be reliably calculated.  
- Enzyme orientation is mixed in a bulk assay.  
- The signal is near the limit of detection.  
- Labeled phosphate is not incorporated despite apparent ATP accumulation.

In these cases, the experiment does not distinguish reversible coupling from contamination, nonspecific nucleotide release, drift, or readout artifacts.

---

## Measured values versus numerical parameters requiring validation

It is important to separate what the experiment actually measures from parameters that must not be assumed.

### Directly measured or directly calibratable quantities

These can be measured in the proposed experiment:

- Fluorescent actin marker angle over time.  
- Fiducial marker displacement.  
- Commanded field phase and amplitude.  
- Handle angular position.  
- Angular velocity.  
- Number of commanded and achieved revolutions.  
- Torque calibration coefficients.  
- Estimated mechanical work.  
- Sample collection times.  
- Detector response for ATP standards.  
- HPLC or LC–MS peak areas.  
- ATP concentration derived from calibration.  
- ADP and phosphate concentrations, if measured.  
- Isotopic enrichment of phosphate and ATP.  
- Fraction of molecules rotating during calibration.  
- Post-experiment ATP-driven rotation status.  
- Detection limit and quantification limit of the chemical assay.

### Parameters requiring validation and not to be assumed

These may be estimated from the experiment but must not be treated as known in advance:

- ATP molecules produced per γ revolution.  
- Step angle of mechanical substeps.  
- Stall torque.  
- Mechanical efficiency.  
- Torsional stiffness of the γ–actin–handle linkage.  
- Fraction of surface-anchored F₁ molecules that are catalytically active.  
- Orientation uniformity of the immobilized population.  
- Kinetic rate constants for synthesis under force.  
- Dependence of synthesis rate on ADP, phosphate, and ATP chemical potentials.  
- Free-energy change of ATP synthesis under the exact chamber conditions.  
- Slip probability or nonproductive mechanical cycles.  
- Effective torque at γ, as opposed to torque at the external handle.  
- Reporter perturbation of the reaction.  
- Stability of F₁ over the measurement interval.

Any numerical value for these parameters should be reported as an experimentally derived estimate with uncertainty, not as an assumed constant.

---

## Key assumptions and how to test them

### Assumption 1: The γ-linked handle can be rotated without detaching or damaging F₁

Test:

- Monitor attachment over time.  
- Verify post-experiment ATP-driven rotation.  
- Compare rotation traces before and after mechanical epochs.  
- Include gentle versus strong torque conditions.

### Assumption 2: The fluorescent actin marker reports γ angle under load

Test:

- Compare handle angle with actin marker angle.  
- Measure phase lag under oscillatory driving.  
- Use shorter or stiffer handles if compliance is excessive.  
- If necessary, use a separate small γ label for angle readout.

### Assumption 3: The surface anchor prevents stator rotation

Test:

- Label or otherwise monitor the F₁ body if possible.  
- Verify that fiduciary markers and surface-bound features do not rotate with the handle.  
- Use stronger or more specific surface attachment if stator movement is suspected.

### Assumption 4: ADP and phosphate stocks are not contaminated with ATP

Test:

- Analyze stocks by HPLC/LC–MS before use.  
- Use ATP-removing pretreatment and verify removal.  
- Include no-enzyme and time-zero controls.  
- Use labeled phosphate to distinguish new synthesis from old ATP.

### Assumption 5: The chemical assay detects ATP quantitatively in the reaction matrix

Test:

- Matrix-matched standard curves.  
- Spike recovery.  
- Internal standards.  
- Orthogonal assay comparison.

### Assumption 6: The enzyme remains capable of ATP-driven rotation after the synthesis attempt

Test:

- Perform post-experiment ATP calibration.  
- Exclude trials failing the post-test.  
- Track survival curves across mechanical conditions.

---

## What would change the recommendation?

The recommended experiment would need modification if pilot data show any of the following:

1. **Single-enzyme ATP output is below detection limit**  
   Change: increase the number of active enzymes in a controlled ensemble, improve product accumulation by reducing flow volume, or use a more sensitive single-molecule ATP reporter tethered near F₁.

2. **Orientation is not uniform**  
   Change: develop oriented immobilization, sort molecules by ATP-driven rotation direction before chemical measurement, or move to single-molecule chemical detection.

3. **Actin handle is too compliant**  
   Change: shorten the actin filament, use a stiffer handle, attach the magnetic/optical probe closer to γ, or use direct γ attachment with a separate small angle reporter.

4. **Optical ATP reporter is perturbed by the field or beads**  
   Change: rely primarily on offline HPLC/LC–MS and use the optical reporter only after validating independence.

5. **Reagent contamination is substantial**  
   Change: purify nucleotide and phosphate stocks, use ATP-removing pretreatment, replace suspect reagents, and add isotope-labeling controls.

6. **Enzyme loses activity during imposed rotation**  
   Change: reduce torque, shorten epochs, alter buffer, add stabilizing agents if compatible, or use a more robust preparation.

7. **Torque at γ cannot be calibrated**  
   Change: redesign the mechanical handle to allow direct torque calibration, for example using a calibrated birefringent rotor or a magnetic handle with well-characterized moment.

---

## Minimal acceptable evidence for a strong claim

To claim reversible mechanochemical coupling, the minimal acceptable evidence should include:

1. ATP-driven rotation observed in the same preparation, establishing the +θ direction.  
2. Verified reverse γ rotation under ATP-free ADP/phosphate conditions.  
3. Measured mechanical work during reverse rotation.  
4. Direct chemical detection of ATP.  
5. Phosphate dependence.  
6. Active-F₁ dependence.  
7. Direction asymmetry.  
8. Negative no-enzyme, no-substrate, and no-rotation controls.  
9. Confirmation that the ATP is newly formed, ideally by labeled phosphate incorporation.  
10. Post-experiment confirmation that the enzyme remains mechanically functional.

Without this full pattern, a positive-looking ATP signal remains vulnerable to contamination, drift, nonspecific release, or detector artifact.
