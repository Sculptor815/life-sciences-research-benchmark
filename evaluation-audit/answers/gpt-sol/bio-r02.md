# GPT-5.6 Sol / bio-r02

Original final answer, shared by both scoring rounds.

# Recommended next question and action

**Most valuable next biological question:**  
**Does isolated F1-ATPase rotate through reproducible elementary angular transitions that are tightly coupled to individual nucleotide-turnover events, or is its motion continuous/loosely coupled—and how much of either behavior is created or obscured by the fluorescent filament load?**

The decisive next experiment is **simultaneous single-enzyme measurement of central-subunit angle and a validated nucleotide-turnover-linked signal across several ATP concentrations and several calibrated filament loads**. A low-load angular study should proceed even if a suitable chemical reporter is not yet available, but without that reporter it cannot resolve temporal coupling to nucleotide turnover.

---

# 1. Evidence, inference, and present limit

## Supplied evidence

- **E1, packet sentence 1:** A fluorescent filament attached to the central subunit of immobilized F1-ATPase rotates when ATP is present.
- **E2, packet sentence 2:** This establishes rotary motion in the isolated enzyme but does not resolve elementary mechanical events, their relationship to nucleotide turnover, or marker-load effects.
- **E3, packet sentence 3:** No subsequent stepping or energetic measurements are supplied.

## Evidence-to-inference-to-conclusion chain

1. **Observation:** The attached filament undergoes sustained angular displacement in ATP.
2. **Direct inference:** The central subunit of isolated, immobilized F1 can produce net rotary motion under the assay conditions.
3. **Not established:**  
   - Whether motion consists of discrete steps or continuous biased motion.  
   - Whether any mechanical transition has a fixed temporal or stoichiometric relationship to nucleotide binding, hydrolysis, or product release.  
   - Whether the filament faithfully reports central-subunit motion or instead slows, smooths, delays, or creates apparent transitions through drag and compliance.  
   - Torque, work, efficiency, or other energetic quantities.
4. **Conclusion:** The highest-value next study must measure elementary angular dynamics while explicitly varying marker load and, if technically possible, directly observing a turnover-linked chemical event at the same molecule.

---

# 2. Competing mechanisms and discriminating predictions

These mechanisms are not necessarily exhaustive or mutually exclusive; mixtures may occur.

## Mechanism A: Discrete, tightly coupled chemomechanical stepping

ATP turnover proceeds through repeated chemical states, and one or a fixed number of chemical transitions drives each elementary angular transition.

### Predictions

- Angular trajectories contain **recurrent dwell positions separated by transitions**, beyond localization noise and detector bandwidth.
- The same angular increment, or reproducible set of increments, recurs within and across molecules without assuming any particular step angle in advance.
- Nucleotide-reporter events occur at reproducible angular phases and with a narrow temporal ordering relative to mechanical transitions.
- The count ratio between productive chemical events and mechanical transitions is approximately constant after correction for missed events.
- Changing ATP concentration affects at least some dwell durations or state occupancies more strongly than it affects the angular increments.
- Increasing load may prolong transitions, increase dwell times, stalls, or backward events, but the underlying angular states and chemical-to-mechanical ratio should persist until coupling fails.
- Discrete states should remain detectable under the lowest measurable marker load if they are intrinsic.

## Mechanism B: Continuous or loosely coupled rotary drive

ATP turnover creates a time-averaged directional bias or torque, but individual turnovers are not obligatorily paired with fixed angular transitions.

### Predictions

- A continuous drift-and-fluctuation model explains trajectories as well as or better than a discrete-state model after accounting for measurement noise.
- There are no stable recurring angular dwell phases across molecules.
- Nucleotide events correlate with average rotational rate but not with individual transitions at a fixed phase or lag.
- The number of chemical events per angular displacement varies substantially, including apparent slips or rotations without a matched detected event after correction for reporter performance.
- ATP concentration changes mean velocity or fluctuation statistics without revealing a stable set of angular states.

## Mechanism C: Marker-load or measurement-generated stepping

The fluorescent filament’s drag, elasticity, attachment geometry, or finite imaging rate creates, merges, delays, or hides apparent mechanical events.

### Predictions

- Apparent step size, dwell duration, transition duration, or stall frequency changes systematically with filament dimensions or calibrated load.
- Steps appear only with larger/slower markers, or smaller elementary events appear as load and measurement bandwidth improve.
- Apparent states change with frame rate or analysis filtering.
- A chemical event may precede the observed filament movement by a delay that grows with load.
- Extrapolation toward minimal load is inconsistent with the behavior measured using the original or larger filament.
- Features attributed to the enzyme correlate more strongly with filament geometry or bending than with ATP concentration.

## Nuisance alternative: Heterogeneous immobilization or damaged complexes

Different attachment orientations or enzyme states, rather than a shared motor mechanism, generate heterogeneous trajectories.

### Predictions

- Step patterns are molecule- or preparation-specific rather than recurring across independent preparations.
- Behavior correlates with attachment geometry, surface location, or loss of activity.
- Results fail leave-one-preparation-out replication.

---

# 3. Proposed research plan

All elements below are **proposals**, not reported methods or results.

## Stage 0 — Preregister the decision framework

Before collecting confirmatory data:

1. Designate three primary questions:
   1. Are there resolvable recurrent angular states?
   2. Are chemical events temporally and stoichiometrically associated with mechanical transitions?
   3. Do these properties change with marker load?
2. Define two competing trajectory models:
   - A discrete-state/change-point model.
   - A continuous drift-and-fluctuation model with the same measurement-error structure.
3. Predefine primary endpoints:
   - Held-out predictive advantage of the discrete versus continuous model.
   - Distribution of inferred angular increments and dwell positions.
   - Chemical–mechanical event association relative to shuffled controls.
   - Corrected chemical-event/mechanical-transition count ratio.
   - ATP-by-load effects on dwell time, transition duration, step amplitude, velocity, stalls, and backward events.
4. Predefine quality-control exclusions, equivalence margins for reporter perturbation, and the detectable spatial and temporal limits.
5. Keep calibration/pilot data separate from the locked confirmatory analysis, or explicitly model them as exploratory rather than silently pooling them.

No particular number of states or angular increment should be assumed from the supplied observation.

---

## Stage 1 — Establish prerequisites

### 1.1 Reproduce the supplied phenomenon

Using the proposed assay implementation, first verify:

- Immobilized F1 bearing a filament on the central subunit shows reproducible directional rotation in ATP.
- The same preparation does not show comparable directed motion without ATP.
- ATP-dependent rotation occurs in multiple independent enzyme preparations.

Failure to reproduce this observation stops the mechanistic study and redirects effort to assay integrity.

### 1.2 Define all currently unreported parameters

The packet does not report these, so they must be selected, recorded, and disclosed:

- Immobilization and central-subunit attachment procedures.
- Filament length, diameter, labeling density, attachment point, and flexibility.
- ATP concentrations, ATP purity, and means of limiting depletion or product accumulation.
- Buffer composition, temperature, viscosity, chamber dimensions, and imaging duration.
- Frame rate, exposure time, localization precision, photobleaching rate, and spectral channels.
- Enzyme density and criteria for one enzyme driving one filament.
- Chemical reporter identity, if any, and which molecular event it actually reports.
- Preparation, chamber, field, molecule, and trace identifiers.

### 1.3 Chemical-reporter prerequisite

Develop or select a reporter capable of detecting at least one turnover-linked nucleotide transition at the same enzyme, such as occupancy, binding, hydrolysis-linked change, or release.

It must be established which event it reports. A binding reporter must not be described as a direct hydrolysis reporter.

Required validation:

- Event-detection efficiency and false-event rate.
- Temporal response and dead time.
- Spectral crosstalk with the filament channel.
- Stability under acquisition illumination.
- Comparison of rotation in reporter-containing and reporter-free ATP conditions.
- An orthogonal matched assay of ATP consumption by immobilized enzyme preparations.

**Critical limitation:** If no reporter can be shown not to perturb rotation within a prespecified equivalence margin, simultaneous chemical–mechanical conclusions should not be made. The study may still resolve mechanics and load effects.

---

## Stage 2 — Calibrate the angular measurement

### 2.1 Time and position calibration

1. Calibrate detector pixel size and channel registration.
2. Synchronize the angular and chemical channels using a common timing signal.
3. Place stationary fiducials in every field to quantify and correct stage drift.
4. Measure timestamp jitter, dropped frames, and exposure overlap.
5. Use stationary fluorescent filaments or equivalent orientation standards to estimate angular localization error as a function of brightness, filament length, and orientation.

### 2.2 Validate angle extraction

1. Predefine an algorithm that estimates filament orientation and frame-wise uncertainty.
2. Test it on synthetic movies containing:
   - Smooth rotation.
   - Known discrete transitions.
   - Brownian angular fluctuations.
   - Photobleaching, background changes, and stage drift.
3. Verify that the analysis does not convert smooth simulated rotation into steps.
4. Process confirmatory data without seeing ATP, load, or chemical-event labels.
5. Repeat key analyses with an independently implemented method or blinded second analyst.

### 2.3 Determine detection limits

From calibration, declare:

- Smallest distinguishable angular transition.
- Shortest resolvable dwell.
- Shortest resolvable transition duration.
- Range of angular velocities not blurred by exposure.
- Confidence required to call backward steps or stalls.

Events below these limits must be reported as unresolved rather than absent.

---

## Stage 3 — Create and calibrate marker-load conditions

### 3.1 Load series

Prepare at least three proposed filament classes:

1. **Minimal detectable load:** The smallest/least-dragging filament that still provides reliable angle estimates.
2. **Intermediate load.**
3. **Higher but still functional load:** Sufficient to test load sensitivity without making all molecules immobile.

Measure the actual dimensions and brightness of every analyzed filament rather than relying only on nominal classes.

### 3.2 Separate load from optical quality

Because a larger filament may both impose more load and yield a better orientation estimate:

- Match labeling density where feasible.
- Include localization uncertainty explicitly in the trajectory model.
- Downsample or add calibrated noise to high-quality traces as a sensitivity analysis.
- Analyze filament dimensions as continuous covariates in addition to categorical load classes.

### 3.3 Relative versus absolute load

Attempt to calibrate relative drag using filament geometry and a separately validated reference response, such as the thermal fluctuations of a suitably pivoted non-driven marker or response to a known external fluid perturbation.

This calibration is an **assumption-dependent proposal**. If absolute drag cannot be established, report only relative marker-load classes and do not infer torque, work, or efficiency.

### 3.4 Check compliance

Track both proximal and distal filament features when optical resolution allows. Load-dependent bending or delayed distal motion would indicate that the filament is an elastic filter rather than a rigid angular reporter.

---

## Stage 4 — Select ATP conditions by pilot study

Use pilot data to choose:

- No ATP.
- Several nonzero ATP concentrations spanning slow detectable motion through the fastest reliably measured regime.
- If a plateau in mean rate is observed, include conditions below and near that plateau; do not assume one must exist.

Confirm ATP concentration at preparation and, where feasible, before and after acquisition. Choose observation duration and chamber volume so that ATP depletion and product accumulation remain below predefined tolerances.

ATP concentrations selected in the pilot should then be locked for confirmatory testing.

---

## Stage 5 — Experimental units, replication, and sample size

### Independent units

- **Primary single-molecule unit:** One enzyme–filament complex.
- Frames, dwells, steps, and revolutions from one molecule are repeated observations, not independent replicates.
- Multiple molecules in one chamber share solution conditions and constitute a chamber-level cluster.
- Independent enzyme preparations provide the strongest replication against preparation-specific behavior.
- For ensemble ATP-consumption measurements, the independent unit is a separately prepared chamber or aliquot, not each molecule inferred to be present within it.

Use at least three independent enzyme preparations as a proposed minimum, with multiple chambers and molecules per condition in each preparation.

### Sample-size determination

Use pilot-estimated measurement error and between-molecule/preparation variability to simulate the confirmatory design. Select the number of preparations, chambers, and molecules to achieve:

- A prespecified power, for example 90%, for the minimum biologically interpretable load or coupling effect.
- Adequate confidence-interval precision around step amplitude and event ratio.
- Enough independent preparations to ensure conclusions are not driven by a single batch.

Do not treat thousands of frames or transitions from one molecule as a large biological sample size.

---

## Stage 6 — Allocation and blinding

1. Use a balanced factorial design crossing ATP concentration with marker-load class.
2. Randomize chambers to ATP condition within each preparation and acquisition day.
3. Distribute aliquots from each preparation across all feasible conditions.
4. Randomize chamber acquisition order to prevent time-of-day, bleaching, or preparation-age confounding.
5. Have one person code solutions and sample identifiers where practical.
6. Use automated acquisition settings fixed before condition decoding.
7. Blind trajectory analysts to ATP concentration, marker load, chemical-event times, and control identity.
8. Detect mechanical and chemical events independently; reveal their relative timing only after each event list is locked.
9. Decode conditions only after exclusions and primary analysis settings are finalized.

Within-molecule ATP washout and re-addition can test reversibility, but it is a secondary repeated-measures control and does not replace independently allocated molecules.

---

## Stage 7 — Required controls

### Negative and artifact controls

- No ATP.
- ATP-containing chamber without enzyme.
- Fluorescent filament immobilized without an active motor, to quantify drift and non-motor fluctuations.
- Inactive or deliberately nonfunctional enzyme control, provided its attachment properties remain interpretable.
- Spectral crosstalk controls for each fluorescence channel alone.
- Matched ATP-consumption blanks without active enzyme.

### Positive/process controls

- A reference marker condition that reproducibly recapitulates the supplied ATP-dependent rotation.
- ATP removal and re-addition where technically possible, testing whether rotation follows ATP availability reversibly.
- Active control chambers in every acquisition session.

### Reporter controls

- Unlabeled ATP condition versus reporter-containing condition.
- Reporter-only background and false-event measurements.
- Matched ensemble ATP-consumption measurements with and without the reporter.
- A dilution series or other calibration establishing reporter-event detection efficiency.

### Attachment and multiplicity controls

- Use sparse enzyme density or another validated criterion to minimize multiple motors acting on one filament.
- Predefine acceptable pivot geometry and trajectory shape.
- Record but do not selectively exclude unusual attachment geometries after examining outcomes.

---

## Stage 8 — Confirmatory acquisition sequence

For each chamber:

1. Record metadata and environmental parameters.
2. Acquire a baseline before ATP exposure when feasible.
3. Introduce coded ATP condition and mark the synchronized time.
4. Record the filament and chemical-reporter channels simultaneously at the calibrated rate.
5. Acquire fixed-duration traces determined from pilot bleaching and depletion limits; do not selectively extend interesting traces.
6. Record fiducials and background at the beginning and end.
7. Measure filament geometry and brightness.
8. Document detachment, overlap, focus loss, photobleaching, filament bending, or chamber flow.
9. Preserve raw movies, timestamps, metadata, and all analysis versions.

If the turnover reporter cannot be validated, retain the same design for angle versus ATP and marker load, but label the chemical-coupling question unresolved.

---

# 4. Measurements

## Primary mechanical measurements

- Unwrapped angular position versus time.
- Directionality and net revolutions.
- Candidate dwell positions and their angular phases.
- Angular increments and their uncertainty.
- Dwell durations.
- Transition durations and angular velocities.
- Pauses, stalls, reversals, and apparent slips.
- Within-molecule and between-molecule variability.
- Dependence on ATP concentration, filament dimensions, and relative load.

## Chemical measurements

- Time and classification of each reporter event.
- Reporter amplitude, duration, detection confidence, and dead time.
- Event phase within the angular cycle.
- Lag between chemical and nearest mechanical events.
- Number of chemical events per mechanical transition and per angular displacement.
- Matched ensemble ATP consumption under each condition.

Ensemble consumption is an orthogonal check but cannot by itself establish same-molecule event timing.

## Assay-integrity measurements

- Stage drift and channel timing.
- Angular localization precision.
- Photobleaching and photodamage rates.
- ATP stability before and after acquisition.
- Filament dimensions, bending, and brightness.
- Chamber, day, and preparation identifiers.

---

# 5. Analysis plan

## 5.1 Preprocessing

- Correct stage drift using fiducials.
- Estimate frame-wise angular uncertainty.
- Do not apply unvalidated smoothing.
- Mark low-quality intervals without using knowledge of ATP or event timing.
- Retain raw and corrected traces.

## 5.2 Test discrete versus continuous motion

Fit both:

1. **Discrete-state model:** Recurrent angular states with transitions, allowing the number and spacing of states to be learned with a complexity penalty.
2. **Continuous model:** Directed angular drift and fluctuations with matched measurement noise and condition-dependent rate.

Compare them using held-out predictive performance and simulation-based checks, not visual inspection alone. A model must recover known synthetic inputs and should not infer steps from smooth simulated trajectories.

Report whether inferred states recur:

- Within a molecule.
- Across molecules in one preparation.
- Across independent preparations.
- Across ATP and load conditions.

## 5.3 Test chemical–mechanical coupling

Chemical events must first be identified without viewing angle traces.

Then assess:

- Cross-correlation and lag distributions.
- Angular phase concentration of events.
- Fraction of mechanical transitions with a nearby chemical event.
- Fraction of chemical events with a nearby mechanical transition.
- Corrected count ratio, incorporating reporter detection efficiency and uncertainty.

Compare observed associations with:

- Time-shuffled events within each trace.
- Circularly shifted event trains preserving event frequency.
- No-ATP and inactive controls.

A fixed association should be claimed only if it exceeds these nulls and is reproduced across preparations.

## 5.4 Test ATP and load effects

Use a hierarchical model with:

- Fixed effects for ATP concentration, load, and their interaction.
- Random effects for preparation, chamber, and molecule.
- Repeated events nested within molecule.

Test whether ATP or load changes:

- Step amplitude or angular phase.
- Dwell or transition durations.
- Mean rotational rate.
- Stall, reversal, or slip probability.
- Chemical–mechanical lag and event ratio.

Particularly discriminating patterns are:

- **Stable angular states with ATP-dependent dwell times:** favors intrinsic chemical stepping.
- **Load-dependent dwell but stable step amplitude:** consistent with intrinsic states whose kinetics are mechanically opposed.
- **Load-dependent apparent step amplitude or emergence of steps only at high load:** favors marker filtering or distortion.

## 5.5 Robustness analyses

- Repeat analysis with an alternative event detector.
- Vary reasonable thresholds within preregistered ranges.
- Leave out each preparation in turn.
- Match or equalize localization precision across load groups.
- Exclude visibly compliant filaments in a predefined sensitivity analysis while retaining the full analysis as primary.
- Report confidence intervals and detection bounds, not only significance tests.

---

# 6. Stop rules

## Calibration stop rules

Stop or redesign before confirmatory data collection if:

- ATP-dependent rotation cannot be reproduced across independent preparations.
- No-ATP or motor-free controls show comparable directed motion.
- Angular resolution or frame rate cannot distinguish the prespecified minimum feature.
- Load classes cannot be separated, or the proposed high-load condition stalls nearly all complexes.
- Stage drift, timing jitter, or crosstalk is comparable to the expected signal.
- ATP depletion exceeds the predefined tolerance.
- The chemical reporter’s event identity or detection efficiency cannot be established.
- The reporter alters rotational behavior beyond the prespecified equivalence margin.

Failure of the chemical-reporter gate stops only the direct coupling arm, not necessarily the mechanics/load arm.

## Per-trace stop and exclusion rules

Terminate acquisition for:

- Complete photobleaching.
- Filament detachment.
- Loss of focus or unresolved trajectory overlap.
- Saturation or unrecoverable timing failure.
- Gross chamber flow or drift.

Predefine which intervals are excluded. A biological stall must not be excluded merely because it is inconvenient; it is excluded only if accompanied by a technical failure.

## Study-level stopping

- Use a fixed sample size determined before confirmatory analysis.
- Do not stop early because the emerging result appears favorable.
- Allow early futility stopping only for predefined assay failure, such as persistent inability to resolve angle or reporter events, rather than lack of the desired biological effect.

---

# 7. Troubleshooting

| Problem | Diagnostic | Action and interpretive limit |
|---|---|---|
| Apparent steps disappear at higher frame rate or after less smoothing | Reprocess identical traces and synthetic smooth controls | Treat earlier steps as analysis/bandwidth artifacts |
| Fast movement is motion-blurred | Exposure-dependent angular uncertainty | Increase temporal resolution or report transitions below resolution; do not assign a false step size |
| Minimal-load markers are too dim | Localization precision fails calibration | Improve labeling or optics without increasing dimensions; otherwise report the accessible load floor |
| Larger markers show cleaner steps only because they are brighter | Error differs by load | Model uncertainty and equalize effective precision by sensitivity analysis |
| Filament bends or distal end lags | Proximal–distal discrepancy | Model compliance or exclude by predefined QC; avoid treating distal motion as direct shaft motion |
| Reporter changes rotational rate | Reporter-free comparison fails equivalence | Do not infer native coupling from that reporter; use orthogonal ensemble ATP consumption only |
| Chemical events are missed at high rate | Reporter dead time becomes limiting | Restrict quantitative ratio estimates to calibrated rates or correct with explicit uncertainty |
| Strong molecule-to-molecule heterogeneity | Effects cluster by attachment or preparation | Increase independent preparations, inspect attachment covariates, and avoid universal step claims |
| Apparent backward steps track low signal | Backsteps coincide with large angular error | Require confidence above calibrated false-call rate |
| ATP condition changes during acquisition | Before/after measurements fail tolerance | Shorten acquisition, increase reservoir, or redesign ATP handling |
| Multiple motors may drive one filament | Complex trajectories or excessive surface density | Reduce density and enforce predefined single-pivot criteria |
| Chemical and mechanical channels drift in time | Synchronization control fails | Correct if possible; otherwise temporal coupling is uninterpretable |

---

# 8. Conditional interpretations

## Outcome 1: Discrete states plus reproducible chemical coupling

Suppose recurrent angular states persist under minimal load, a fixed chemical–mechanical ordering is reproduced across preparations, and the corrected event ratio is stable.

**Conclusion:** Isolated F1 operates through a discrete chemomechanical cycle under the tested conditions, with a measurable coupling relationship between the observed reporter-defined chemical event and elementary rotation.

**Limits:**

- If the reporter detects binding, the result establishes coupling to binding, not necessarily directly to hydrolysis.
- The coupling ratio applies to detected productive events under the tested ATP, load, immobilization, and marker conditions.
- Energetic efficiency remains unmeasured without absolute load and chemical free-energy information.

## Outcome 2: Discrete mechanical steps but no chemical association

**Conclusion:** Elementary mechanical transitions are supported, but tight coupling to the measured nucleotide event is not established.

Possible explanations include:

- Truly loose coupling.
- Reporter events that are missed, delayed, or chemically misassigned.
- Coupling to a different nucleotide transition.
- Temporal resolution inadequate for the lag.

The strength of the negative conclusion depends on reporter detection efficiency and timing calibration.

## Outcome 3: Chemical events are phase-linked, but angular motion appears continuous

**Conclusion:** Nucleotide events are associated with rotary progression, but elementary mechanical transitions are smaller or faster than resolution, smoothed by filament compliance, or genuinely continuous.

This does not justify claiming absence of stepping.

## Outcome 4: Apparent stepping depends strongly on filament load

If steps emerge only with larger markers, inferred amplitudes change with marker dimensions, or chemical-to-filament lag grows with load:

**Conclusion:** The filament materially filters or distorts observed motion. The original observation still demonstrates ATP-dependent rotation, but its fine time structure cannot be assumed to represent unloaded central-subunit dynamics.

If stable states remain at the lowest load while only dwell or stall frequencies change, the states are more likely intrinsic and load is modifying kinetics rather than creating the states.

## Outcome 5: No resolvable steps and no event-level chemical coupling

If calibration shows adequate sensitivity, continuous models predict held-out traces better, and association remains at shuffled-control levels:

**Conclusion:** There is no evidence for discrete steps above the stated angular and temporal detection limits or for tight coupling to the measured chemical event under the tested conditions.

The correct conclusion is not that rotation is definitively continuous or uncoupled; smaller, faster, or reporter-invisible events remain possible.

## Outcome 6: Load arrests rotation while chemical events continue

**Conclusion:** This is consistent with mechanical slippage, incomplete coupling, or filament compliance under load. It would argue against obligatory one-to-one conversion of every detected chemical event into observed filament motion, but alternative reporter artifacts must be excluded.

## Outcome 7: Load arrests both rotation and detected turnover

**Conclusion:** Mechanical opposition and the chemical cycle are interdependent, consistent with coupling. This alone does not establish a step angle or fixed stoichiometry.

## Outcome 8: Results vary mainly by preparation or attachment geometry

**Conclusion:** Assay heterogeneity prevents a general mechanistic claim. The next priority would be standardizing immobilization and attachment rather than assigning a universal stepping scheme.

---

# 9. Strongest currently justified conclusion

From the supplied packet alone, the strongest defensible statement is:

**An attached fluorescent filament reports ATP-dependent rotary motion of the central subunit in isolated, immobilized F1-ATPase. The observation does not establish elementary step structure, temporal or stoichiometric coupling to nucleotide turnover, unloaded motor behavior, torque, work, or energetic efficiency.**

The proposed synchronized, load-varied experiment is valuable because it can distinguish intrinsic chemomechanical stepping from continuous/loose coupling and from marker-induced dynamics while explicitly bounding what remains unresolved.
