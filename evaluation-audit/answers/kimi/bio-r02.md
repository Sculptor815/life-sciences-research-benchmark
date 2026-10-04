# Kimi K3 / bio-r02

Original final answer, shared by both scoring rounds.

## 1. Recommended next biological question

**The most valuable next question is: are elementary angular movements of the central subunit obligatorily coupled to ATP catalytic turnover, or does the fluorescent-filament rotation average over slipping, Brownian motion, probe compliance, or another ATP-dependent process?**

The recommended experiment is a **load-calibrated, time-synchronized single-molecule assay** that records:

1. central-subunit angle at sufficient bandwidth to detect dwells and steps;
2. nucleotide binding or occupancy, where a validated reporter is available;
3. ATP conversion and/or phosphate release from the same molecule, where a validated reporter is available; and
4. the effect of systematically changing the load and compliance of the attached reporter.

All methods below are **proposals**, not procedures reported in the supplied packet. The packet does not provide the enzyme source, subunit identity, immobilization chemistry, ATP concentration, temperature, buffer, filament dimensions, acquisition rate, rotation direction, or ATP-free control.

---

## 2. Evidence-to-inference-to-conclusion chain

### Supplied evidence

- **E1:** “A fluorescent filament attached to the central subunit of immobilized F1-ATPase rotates in the presence of ATP.”
- **E2:** The observation “demonstrates rotary motion in the isolated enzyme.”
- **E3:** The observation does not resolve elementary mechanical events.
- **E4:** It does not establish the relation of motion to nucleotide turnover.
- **E5:** It does not establish how marker load changes the observed motion.

### Justified inference

The probe undergoes angular motion relative to the immobilized enzyme support under the stated ATP-containing conditions.

### Not yet justified

The packet alone does not establish that:

- ATP hydrolysis, rather than ATP binding or an ATP-containing-buffer artifact, causes rotation;
- every catalytic turnover produces a fixed angular displacement;
- rotation is continuous or consists of discrete steps;
- the number of steps per revolution is three or any other value;
- rotation direction, torque, work, or energetic efficiency;
- the fluorescent filament faithfully reports central-subunit rotation rather than twisting, bending, dragging, or filtering rapid events;
- the result generalizes to the intact ATP synthase or to cellular conditions.

### Conclusion

The next experiment should not merely show rotation again. It should **count angular transitions and chemical turnovers from the same molecule while manipulating probe load**. That design directly addresses the three unresolved issues in the packet.

---

## 3. Competing mechanisms and discriminating predictions

### M1. Tight hydrolysis-driven power stroke

ATP binds, chemical conversion occurs, and that conversion directly produces one stereotyped angular transition or a fixed sequence of transitions.

**Predictions**

- A reproducible angular-step distribution.
- A fixed integer relationship between chemical turnovers and angular cycles.
- A short, reproducible lag from a validated chemistry event to motion.
- Nonhydrolyzable ATP analogs may bind but should not support sustained net rotation.
- Step angle remains relatively stereotyped as passive load changes, although step duration and dwell times may change.

### M2. Binding-driven power stroke

ATP association itself produces the major angular displacement; hydrolysis later resets the enzyme.

**Predictions**

- Nucleotide arrival precedes the angular step, but bond cleavage and phosphate release occur after it.
- A validated nonhydrolyzable analog may cause a transient advance that reverses or stalls upon dissociation.
- Chemical turnovers and angular transitions need not be one-to-one under analog conditions, although normal ATP should still show a reproducible relationship.

### M3. Product-release-driven motion

ATP cleavage occurs first, but the rotor remains mechanically restrained until phosphate and/or ADP release permits motion.

**Predictions**

- Chemistry precedes motion.
- A validated phosphate-release signal closely precedes the angular transition.
- Perturbations that specifically delay product release lengthen the post-chemistry, pre-step dwell.
- A phosphate-release signal alone cannot distinguish this model from M1 if cleavage and release are temporally inseparable; an independent chemistry reporter or specific perturbation is required.

### M4. Tight composite stepping

Each catalytic turnover drives more than one elementary angular substep in a fixed sequence.

**Predictions**

- A fixed number of substeps occurs per chemical turnover, even if individual substeps have unequal angles.
- Substeps occur in a reproducible order and sum to a reproducible angle per catalytic cycle.
- Chemical-event timing predicts the entire substep sequence rather than only one transition.

### M5. Loosely coupled or slipping rotation

ATP turnover usually permits rotation, but chemical cycles and angular cycles are not obligatorily linked.

**Predictions**

- Variable numbers of turnovers per revolution.
- Angular steps with broad or changing angle distributions.
- Chemical events without angular transitions and angular transitions without nearby chemical events.
- Poor molecule-level cross-correlation even if population-averaged ATP consumption per revolution appears orderly.

### M6. Gated Brownian ratchet

Nucleotide-state changes rectify thermal motion rather than generating a stereotyped mechanical stroke.

**Predictions**

- Broad angular-transition distributions and frequent backward fluctuations.
- Strong sensitivity of trajectory shape to probe friction and thermal motion.
- Nucleotide occupancy may gate when movement is allowed without predicting a fixed step angle.
- Apparent directional motion can coexist with variable chemical-to-mechanical stoichiometry.

### M7. Probe or measurement artifact

The filament reports ATP-dependent flow, surface drift, filament bending, label photophysics, or motion of an attached complex rather than true rotor motion.

**Predictions**

- Similar motion occurs in ATP-free, catalytically inactive, no-enzyme, or misattached-probe controls.
- Apparent angular behavior changes qualitatively with filament length, attachment chemistry, or surface position.
- “Steps” appear in synthetic-noise or no-ATP controls at similar rates.
- Motion is uncorrelated with validated catalytic activity.

### Important conditional prediction

A threefold or approximately 120° stepping model should be tested only if independent structural information establishes three equivalent catalytic positions. The supplied packet does not provide that structural information. Therefore, the experiment should estimate the number and angles of steps rather than presuppose 120°.

---

## 4. Ordered, auditable research plan

## Phase 0 — Define claims and register the analysis before unblinding

### 0.1 Primary endpoints

Define before data collection:

1. angular-step angle distribution and number of steps per revolution;
2. chemical turnovers per revolution;
3. fraction of angular transitions matched to chemical events;
4. fraction of chemical events matched to angular transitions;
5. lag distribution between nucleotide binding, chemistry, product release, and motion;
6. dependence of dwell time, step size, and angular velocity on calibrated probe load.

A suggested operational criterion for strong molecule-level coupling is a **matched-event fraction whose lower uncertainty bound exceeds 0.90 after correcting for known chemical-detection efficiency**, with mismatches below 10%. This threshold is a proposed decision rule, not a conclusion derived from the packet. It must be fixed before analysis.

### 0.2 Audit trail

Assign immutable identifiers to:

- enzyme preparation;
- labeling reaction;
- flow chamber;
- molecule;
- probe;
- ATP or analog batch;
- acquisition session;
- analysis-code version.

Retain raw movies, timestamps, calibration files, environmental logs, excluded-molecule lists, and reasons for exclusion. Lock the primary analysis code before unblinding condition assignments.

### 0.3 Feasibility gates

Proceed to strong mechanistic claims only if:

- angular precision is adequate to recover calibrated synthetic steps;
- temporal resolution is at least approximately tenfold faster than the shortest dwell to be interpreted;
- chemical-reporter response and capture efficiency are known;
- no-ATP and catalytically inactive controls remain below the predefined artifact threshold;
- probe loading does not abolish ATPase activity.

---

## Phase 1 — Establish and validate the biological preparation

Because the packet omits the preparation, do not assume its properties.

### 1.1 Enzyme identity and activity

- Identify the enzyme source and construct.
- Verify purity and oligomeric integrity using orthogonal biochemical or biophysical measurements.
- Measure ATPase activity of unlabeled enzyme under the exact buffer and temperature intended for microscopy.
- Measure background phosphate or nucleotide degradation in ATP-only and buffer-only samples.
- Prepare a catalytically compromised version only after the construct is known; do not infer an appropriate mutation from the packet.

### 1.2 Central-subunit labeling

- Attach the reporter at a defined, unique position on the central subunit.
- Quantify labeling stoichiometry and the fraction of enzyme carrying a probe.
- Compare ATPase activity of unlabeled, dye-labeled, filament-labeled, and small-probe-labeled enzyme.
- Include a probe attached to a noncentral, immobilized part of the enzyme as a specificity control.

### 1.3 Immobilization geometry

- Verify that the enzyme is immobilized through its peripheral scaffold rather than through the central rotating subunit.
- Test at least two independent immobilization chemistries if available.
- Measure nonspecific surface attachment of free probe and free enzyme.
- Confirm that rotation is not caused by movement of the whole enzyme on the surface.

### 1.4 Probe panel

Use, at minimum:

1. the original-style fluorescent filament, if it can be reconstructed;
2. a shortened or otherwise lower-drag filament;
3. a small, relatively rigid high-bandwidth probe.

If the original filament cannot be reconstructed because its size and chemistry are unreported, state that the new experiment tests the mechanism but does not exactly reproduce the supplied observation.

---

## Phase 2 — Instrument and assay calibration

### 2.1 Angular calibration

- Calibrate image scale, optical distortion, probe-centroid localization, and angular conversion.
- Use surface-tethered probes rotated through known angular increments where technically possible.
- Generate synthetic trajectories containing known step sizes, dwell times, drift, rotational diffusion, missed events, and photobleaching.
- Require blinded injection-recovery analysis to determine the smallest reliably detectable step and shortest detectable dwell.
- Quantify false-positive step rates from no-ATP and dead-enzyme movies.

### 2.2 Temporal calibration

- Verify camera timestamps and synchronization among angle and fluorescence channels.
- Measure illumination-induced delays and detector dead time.
- Use a calibrated fluorescence pulse to determine channel-to-channel offset.
- Correct all event times for measured offsets before calculating lags.

### 2.3 Load calibration

Estimate rotational drag by at least two orthogonal approaches, such as:

- measured probe geometry and independently measured buffer viscosity;
- probe rotational Brownian diffusion;
- an optical-torque calibration, if a load-clamped instrument is used.

Do not rely only on nominal probe dimensions. If two load estimates disagree materially, report relative probe-load classes rather than absolute torque.

Measure probe compliance independently. A flexible filament can store angular strain and then release it as an apparent step.

### 2.4 Chemical-event calibration

Three levels of chemical measurement are desirable:

1. **Nucleotide occupancy:** a validated hydrolyzable fluorescent ATP reporter;
2. **ATP conversion:** a reporter that distinguishes uncleaved from cleaved nucleotide;
3. **Product release:** a phosphate-specific single-molecule reporter.

For each reporter:

- establish spectral crosstalk and bleed-through;
- measure response amplitude, response time, saturation, bleaching, and reversibility;
- test discrimination among ATP, ADP, phosphate, and contaminating nucleotides;
- verify that the reporter does not materially change bulk ATPase activity or rotation;
- determine single-event capture efficiency using an independent calibrated source.

A phosphate-release reporter timestamps **release**, not necessarily the instant of bond cleavage. If no cleavage-sensitive reporter or specific kinetic perturbation is available, M1 and M3 cannot be fully separated.

### 2.5 Bulk ATPase calibration

Measure ATPase activity in parallel for every enzyme preparation and probe-labeling condition. Use enzyme-free ATP, ATP-free enzyme, probe-only, and surface-only controls. Avoid an ATP-regenerating system in phosphate-detection experiments unless its contribution can be independently measured.

---

## Phase 3 — Rotation and stepping measurements

### 3.1 Experimental design

- Immobilize enzyme sparsely enough that most probe signals can be assigned to single molecules.
- Record angle continuously across ATP concentrations spanning:
  - a low concentration where individual waiting periods can be isolated;
  - intermediate concentrations;
  - near-saturating concentration determined from pilot activity and rotation measurements.
- Use continuous buffer flow to limit ATP depletion and product accumulation.
- Record at a frame rate established by the injection-recovery calibration rather than by convenience.
- Record each molecule long enough to contain many angular cycles at the lower-rate conditions, unless terminated by a predefined censoring rule.

### 3.2 Allocation and blinding

- Use computer-generated random assignment of enzyme preparations and conditions to chambers.
- Balance preparation, day, microscope, chamber position, and acquisition order across conditions.
- For primary concentration comparisons, prefer independent molecules or chambers to reduce carryover.
- Use within-molecule concentration sequences only as a secondary paired design, with randomized order where feasible and validated washout.
- Code reservoirs and file names. Acquisition may be partly unblinded because ATP addition is operationally visible, but event detection and primary analysis should be performed blind to condition.
- Do not select molecules for analysis after seeing whether their behavior supports a model.

### 3.3 Controls

Run these controls interleaved with experimental samples:

1. ATP-free buffer;
2. ATP with catalytically compromised enzyme;
3. nonhydrolyzable ATP analog verified to be free of hydrolyzing contamination;
4. ADP alone and phosphate alone where relevant;
5. no-enzyme surface plus ATP;
6. free probe attached directly to the surface;
7. probe attached to a noncentral enzyme location;
8. alternate immobilization chemistry;
9. alternate probe lengths and rigidities;
10. illumination-only and flow-only controls;
11. ATP washout and re-addition for reversible ATP dependence;
12. sensor-only chemical controls.

A nonhydrolyzable analog is an interpretive tool only if its lack of conversion is directly verified under the assay conditions.

---

## Phase 4 — Synchronized chemistry and angle

### 4.1 Nucleotide-arrival channel

At low nucleotide concentration, record fluorescent ATP association and dissociation from colocalized enzyme molecules.

Determine:

- arrival time;
- residence time;
- nonproductive binding fraction, if association and chemistry can be distinguished;
- lag from arrival to angular motion.

If a fluorescent nucleotide changes enzyme kinetics, use the lowest validated reporter fraction and correct interpretation for different reporter and unlabeled-ATP kinetics. A binding event is not by itself proof of hydrolysis.

### 4.2 Chemistry and product-release channels

Where validated reporters are available, record chemistry and phosphate release on the same clock as angle.

Classify the observed order as:

- binding → step → cleavage/release: favors binding-driven motion;
- binding → cleavage → step → phosphate release: favors hydrolysis-driven motion;
- binding → cleavage → phosphate release → step: favors release-driven motion;
- one chemistry event → several fixed angular substeps: favors composite stepping;
- no stable temporal order: favors loose coupling, poor detection, or unresolved rapid intermediates.

Do not interpret phosphate release as the instant of hydrolysis unless independent evidence shows that cleavage and release are temporally inseparable.

### 4.3 Perturbation tests

Use the following perturbations to move beyond correlation:

- nonhydrolyzable analog to test binding-driven motion;
- slowly hydrolyzed ATP analog to test whether slowing chemistry predictably delays motion;
- catalytically compromised enzyme to test enzyme dependence;
- product-release-altering conditions, if a specific and validated perturbation is available;
- probe-load series to test mechanical consequences without changing the catalytic construct.

Avoid interpreting a mutant or analog as a specific stage perturbation unless purity, folding, nucleotide binding, and catalytic defect are independently validated.

---

## Phase 5 — Marker-load and conditional energetic measurements

### 5.1 Passive-load series

At matched ATP conditions, compare original filament, shortened filament, and small probes.

Measure:

- angular velocity;
- dwell duration;
- step size;
- backward-step frequency;
- ATPase activity;
- probe compliance;
- chemical-to-angular event ratio.

If step geometry is invariant while kinetics scale with drag, that supports a stereotyped mechanical transition whose rate is load-sensitive. If apparent stepping disappears with a small probe, filament compliance or filtering remains a major concern.

### 5.2 Conditional torque clamp

Only after molecule-level coupling is established, use a calibrated optical torque clamp, if available, to apply assisting and resisting torque.

Measure:

- torque-dependent velocity;
- stall torque;
- reverse rotations;
- work per angular step, \(W=\tau\Delta\theta\);
- chemical turnovers at each torque.

Do not calculate energetic efficiency unless ATP, ADP, phosphate, temperature, and chemical-reporter contributions are measured well enough to estimate the relevant chemical free-energy change. Standard textbook free-energy values should not be substituted for the actual assay conditions.

---

## 5. Measurements and statistical analysis

### 5.1 Preprocessing

- Correct stage drift using stationary fiducials.
- Correct fluorescence background, spectral bleed-through, bleaching, and channel offsets.
- Unwrap angular trajectories without imposing a preferred step size.
- Flag but do not automatically delete pauses; long pauses may be biological states or inactive molecules.

### 5.2 Step detection

Analyze each trajectory with at least two independent methods, such as:

- a change-point detector; and
- a hidden-state model.

Validate both against synthetic trajectories and blinded negative controls. Report agreement and discordance rather than selecting the method that yields the clearest steps.

Use circular statistics for angular distributions. Fit step angles without fixing the number of steps unless there is independent structural justification. Compare step-plus-dwell models against continuous drift-plus-diffusion models using held-out likelihood or another preregistered model-selection criterion.

### 5.3 Dwell and kinetics analysis

- Estimate dwell-time distributions at each ATP concentration.
- Test whether low-ATP waiting times are consistent with a single ATP-dependent waiting process.
- Avoid interpreting multiexponential dwells as distinct molecular states unless heterogeneity, missed events, and photophysics have been excluded.

### 5.4 Chemistry–angle coupling

For each molecule:

- count chemical events and angular transitions;
- estimate events per complete revolution;
- calculate lag histograms;
- estimate conditional probabilities:
  - \(P(\text{angular step} \mid \text{chemical event})\);
  - \(P(\text{chemical event} \mid \text{angular step})\).

Correct for measured chemical-event capture efficiency, but also report the uncorrected values. Generate null distributions by circularly shifting one event train within the same molecule or by block permutation that preserves event-rate and dwell structure.

A population average of an integer number of turnovers per revolution is not sufficient evidence for molecule-level coupling; it can arise from heterogeneous or slipping molecules.

### 5.5 Independent units and hierarchical inference

The primary biological unit is an **independent enzyme preparation**. Molecules from one preparation are nested technical observations and should not be treated as fully independent preparations.

A practical starting design is:

- at least three independent enzyme preparations;
- at least two independently assembled chambers per preparation and condition;
- enough accepted molecules and events to achieve the preregistered precision.

Set final sample size from pilot variance. Suggested precision targets are:

- mean step-angle uncertainty no greater than approximately \(2^\circ\), where angular calibration permits;
- a confidence or credible interval half-width no greater than 0.10 for the matched-event fraction;
- enough events to detect the smallest biologically meaningful mismatch rate specified before unblinding.

Use hierarchical models with fixed effects for ATP condition, probe class, and perturbation, and random effects for preparation, chamber, day, and molecule. Report preparation-level variability explicitly.

---

## 6. Stop rules

### 6.1 Molecule-level censoring

Stop or censor an individual trace at the first predefined occurrence of:

- irreversible photobleaching below the validated detection threshold;
- probe detachment;
- loss of colocalization;
- focus or drift exceeding calibrated angular noise;
- irreversible pause longer than a preregistered multiple of the condition-specific dwell-time scale;
- evidence that the signal contains multiple molecules.

Censored traces remain in the audit file and are handled by time-to-event or missing-data methods rather than deleted.

### 6.2 Session-level stopping

Stop a session before biological interpretation if:

- no-ATP or dead-enzyme controls exceed the calibrated false-step threshold;
- ATP-only samples show unacceptable background hydrolysis or phosphate;
- chemical-reporter calibration fails;
- synchronization error exceeds the shortest interpretable lag;
- surface density prevents reliable single-molecule assignment;
- bulk enzyme activity differs materially from the qualified preparation range.

### 6.3 Experiment-level stopping

Do not stop early because an initial positive result appears statistically significant. Continue until the preregistered precision target is reached unless a prespecified feasibility rule fails.

Stop claims of event-level coupling if the chemical-event capture efficiency is too low or too uncertain to support the required upper bound on missed events. A suggested feasibility threshold is at least 80% known capture efficiency for a strong one-to-one claim, but the exact threshold should be derived from the desired mismatch bound.

---

## 7. Troubleshooting

| Problem | Likely causes | Proposed response |
|---|---|---|
| No rotation | inactive enzyme, blocked rotor, excessive surface constraint, bad ATP, failed labeling | verify bulk ATPase, ATP quality, immobilization site, label stoichiometry, and surface geometry |
| Rotation only with original filament | small probe alters activity; filament amplifies compliance or drift | test alternate small probes, attachment chemistries, and bulk activity |
| Apparent steps in ATP-free controls | drift, photophysics, filament relaxation, detector noise | reject or recalibrate analysis; use stiffer probes and fiducial correction |
| No chemical events despite bulk ATPase | low reporter capture, spectral crosstalk, surface quenching | recalibrate sensor; use population ATPase measurements but restrict conclusions |
| Chemical events without steps | loose coupling, missed small steps, inactive labeled subpopulation | improve angular bandwidth; correlate with activity; estimate detection limits |
| Steps without chemical events | reporter misses events, probe artifact, ATP-independent motion | quantify capture efficiency; inspect no-ATP and dead-enzyme controls |
| Nonhydrolyzable analog supports rotation | ATP contamination, analog hydrolysis, binding-driven motion, flow artifact | assay analog purity and conversion; repeat with dead enzyme and washout |
| Coupling varies by preparation | heterogeneous constructs, labeling, immobilization, contaminants | treat preparation as a random effect; do not pool without testing |
| Excessive photobleaching | illumination too high or reporter unstable | lower illumination, reduce frame duty cycle, change validated reporter |
| Poor load calibration | uncertain probe geometry, compliance, viscosity | use orthogonal calibration; report relative load if absolute torque is unreliable |

---

## 8. Conditional outcomes and justified conclusions

### Positive outcome: tight discrete chemomechanical coupling

A strong positive package would show:

- reproducible angular dwells and steps;
- fixed chemical-event stoichiometry per angular cycle;
- high bidirectional matching between chemistry and motion;
- a consistent event order across ATP concentrations and enzyme preparations;
- robustness to probe identity after correcting for load;
- loss or predictable alteration of motion with validated catalytic perturbations.

**Strongest justified conclusion:** under the specified isolated-enzyme conditions, ATP catalytic turnover is temporally coupled to a fixed sequence of angular transitions, and the measured event order identifies whether binding, chemistry, or product release most immediately precedes motion.

If three equal steps and three chemical turnovers per revolution were observed, that would support—but the packet does not presently establish—a threefold stepping cycle. If one chemical event produced multiple fixed substeps, the conclusion would instead be a composite mechanochemical cycle.

### Positive outcome for binding-driven motion

If nucleotide arrival precedes angular motion and a verified nonhydrolyzable analog produces a reversible angular displacement without sustained chemistry, the justified conclusion would be that nucleotide binding can generate or permit the observed mechanical transition. Sustained ATP-driven cycling might still require later chemistry.

### Positive outcome for hydrolysis- or release-driven motion

If cleavage precedes motion, M1 is favored. If cleavage occurs but motion follows phosphate release, M3 is favored. If the available reporter cannot separate cleavage from release, the conclusion must remain “post-binding catalytic processing precedes motion,” not a more specific claim.

### Negative outcome: rotation without fixed coupling

If chemical events are numerous but angular transitions show no stable stoichiometry or lag, and both detectors are adequately calibrated, the result favors slipping, loose coupling, or a gated Brownian mechanism. This would not prove that coupling is impossible under all loads; it would reject tight obligatory coupling under the tested conditions.

### Negative outcome: no detectable steps

If synthetic injection-recovery shows that the relevant step sizes would have been detected, yet trajectories are continuous across independent preparations and probes, the result favors a spatially distributed or effectively continuous mechanical process under the tested temporal resolution. It cannot exclude smaller or faster substeps below the demonstrated detection limit.

### Negative outcome: no rotation in the reconstructed assay

This would not directly refute the supplied packet because the original preparation and methods are unreported. It would show that rotation is conditional on unidentified features of the original construct, immobilization, probe, buffer, or analysis. The appropriate conclusion would be irreproducibility under the new, documented conditions—not proof that the original observation was false.

### Ambiguous outcomes

- **Correct population stoichiometry but poor molecule-level correlation:** average coupling only; possible heterogeneity or slipping.
- **Steps with the filament but not with small probes:** possible load-dependent biology, but also filament compliance or amplification.
- **Phosphate correlated with motion but no cleavage reporter:** product release is associated with motion; hydrolysis versus release timing remains unresolved.
- **Nonhydrolyzable analog induces motion:** could support binding-driven motion, but only after contamination, analog conversion, and flow artifacts are excluded.
- **Step angles cluster near a symmetry value:** consistent with a structural periodicity but not sufficient to prove chemical coupling.
- **Load changes both chemistry and rotation:** the probe may directly alter catalysis, preventing separation of passive mechanical loading from enzyme perturbation.

## Overall recommendation

Proceed first with the **high-bandwidth stepping assay plus calibrated probe-load comparison**, because it requires the fewest assumptions. Add synchronized nucleotide and phosphate reporters only after they pass explicit activity, specificity, timing, and capture-efficiency gates. Treat ensemble ATPase measurements as supporting evidence, not as proof of molecule-level coupling. Even a decisive result would apply to the tested isolated F1 preparation and would not by itself establish the mechanism, torque, or efficiency of intact ATP synthase.
