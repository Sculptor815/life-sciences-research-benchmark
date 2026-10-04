# Kimi K3 / bio-d02

Original final answer, shared by both scoring rounds.

# Proposed Protocol: Testing the Requirement for a Heat-Stable, Separable Factor in Yeast-Juice Fermentation

**Status: All experiments described below are proposed. No results are reported. No chemical identity of any factor is asserted.**

---

## 1. Purpose, Background, and Inference Chain

**Objective.** To determine whether a heat-stable, physically separable component of yeast juice is *necessary* (under defined conditions) for fermentative activity of the macromolecular fraction, while excluding the alternative explanations that activity loss is due to pH shift, ionic-strength change, phosphate depletion, dilution, or irreversible enzyme damage during separation.

**Background (from the evidence packet).** The 1906 record shows yeast-juice filtrate and retentate are each inactive alone, that recombination restores activity, and that boiled extract can compensate for the missing fraction. Curator interpretation: this supports a heat-stable, separable factor. Stated limits: compensation does not establish chemical structure and does not alone determine identity (e.g., NAD). Named artifact classes: pH drift, inorganic-salt and phosphate changes during separation, and enzyme damage or dilution masked by nonspecific stabilizers.

**Evidence-to-inference-to-conclusion chain targeted by this protocol:**

1. **Prior evidence:** fractionation abolishes activity in both fractions; recombination restores it; boiled extract substitutes for one fraction.
2. **Candidate inference A (target):** a heat-stable, dialyzable/ultrafilterable solute is required alongside the protein fraction.
3. **Candidate inferences B–F (alternatives to exclude):** inactivation is caused by (B) pH excursion, (C) salt/ionic-strength change, (D) phosphate removal, (E) dilution of a macromolecular complex, or (F) irreversible protein damage during handling — any of which a nonspecific boiled extract might mask by buffering, ion supply, or protein stabilization.
4. **Design logic:** only if matched pH/ions/phosphate/volume/protein controls fail to restore activity, while re-addition of the heat-stable fraction restores it — and only if enzyme integrity is demonstrably preserved — can one infer a specific separable cofactor requirement.
5. **Conditional conclusion permitted:** "Under these calibrated conditions, a heat-stable, separable, low-molecular-weight component is required for fermentative activity." **Not permitted:** any claim about the factor's chemical structure, elemental composition, or identity as any named metabolite or nucleotide.

---

## 2. Materials and Preparatory Work (Proposed)

### 2.1 Source material
- A single large batch of fresh yeast juice (cell-free fermenting preparation) prepared by one consistent method, clarified by low-speed centrifugation, kept at 0–4 °C throughout.
- Reserve aliquots snap-frozen for baseline enzyme-integrity assays (Section 5).
- Boiled extract: a portion of the same yeast juice heated at 100 °C for a calibrated time (see Section 2.5), cooled, centrifuged to remove coagulated protein, filtered.

### 2.2 Defined assay buffer (calibration procedure, not invented values)
Because exact buffer and ion values are unavailable, they must be **calibrated empirically** before the main experiment:

- **Calibration step 1 (buffer selection and pH).** Assay unfractionated juice activity across a pH series (e.g., pH 5.5–8.0 in 0.25-unit steps) using two non-phosphate buffer systems (e.g., a zwitterionic buffer and an acetate system) at a fixed concentration tested at two or three levels (e.g., 10, 25, 50 mM). Select the pH of maximal activity that lies within the buffer's effective range and shows ≤10% activity change across ±0.2 pH units (a plateau region), so that minor residual drift cannot masquerade as fraction effects.
- **Calibration step 2 (ionic strength).** At the selected pH, titrate a defined monovalent salt (e.g., KCl or NaCl, whichever is closer to the juice's measured dominant cation) across a range (e.g., 0–200 mM). Record the activity–ionic-strength curve; choose a working ionic strength on a plateau, and record the inhibitory threshold for later interpretation.
- **Calibration step 3 (substrate and phosphate).** Titrate fermentable sugar (e.g., glucose) to a saturating level (activity increase ≤5% per doubling over the top two concentrations). Titrate inorganic phosphate separately (e.g., 0–100 mM as neutralized K₂HPO₄/KH₂PO₄ at fixed pH) and define (a) the juice's native phosphate requirement, (b) the saturating phosphate concentration, and (c) the inhibitory concentration, if any. This calibration is essential because phosphate is both a reactant in fermentation chemistry and a known artifact class.
- **Calibration step 4 (analytical baseline).** Measure native juice: pH, conductivity (as an ionic-strength proxy), total inorganic phosphate (e.g., molybdate colorimetry), total protein (e.g., Lowry or Bradford against a BSA standard), and baseline fermentation rate. These become the **target values** for matching all fractions and reconstitutions.

### 2.3 Fractionation (independent physical separations)
To avoid confounding factor identity with one device or membrane chemistry, use **two independent separation principles**:

- **Method 1 — size-based:** pressure or centrifugal ultrafiltration through a membrane of defined nominal molecular-weight cutoff (e.g., ~1–3 kDa, or calibrated as below), producing *retentate-1* (protein-rich) and *filtrate-1* (small-solute-rich).
- **Method 2 — equilibrium dialysis:** juice dialyzed against a large volume of the calibrated buffer at 0–4 °C; *inside* fraction = retentate-2, *outside* dialysate (concentrated if needed) = filtrate-2.

**Cutoff calibration:** because the factor's size is unknown, first run a graded-cutoff pilot (e.g., 1, 3, 10 kDa membranes). Use the smallest cutoff that (a) retains ≥95% of measurable protein and (b) passes ≥80% of measured inorganic phosphate and conductivity into the filtrate — confirming that small solutes genuinely equilibrate across the barrier.

### 2.4 Fraction characterization (mandatory before reconstitution)
For every fraction and every batch, measure: volume, pH, conductivity, inorganic phosphate, total protein, and (proposed, optional) total organic phosphate and reducing substances. Record recovery mass balance for protein and phosphate; flag any fraction where recovery deviates >15% from the parent juice for troubleshooting (Section 9).

### 2.5 Heat-treatment calibration
Because "heat-stable" is the key claim, the boiling step must itself be controlled:
- Pilot: heat aliquots of whole juice and of filtrate for 0, 5, 15, 30, 60 min at 100 °C; assay the treated material's **reconstituting capacity** (added to inactive retentate) and confirm ≥90% protein removal (coagulation). Define the minimum heating time that (a) fully abolishes the material's own fermentative activity and (b) fully preserves reconstituting capacity. Use that time for all heat arms. This prevents either under-heating (residual enzyme activity contaminating the "factor" arm) or over-heating (destruction of a moderately heat-labile factor, a false negative).

---

## 3. Enzyme-Integrity Monitoring (Proposed)

The decisive alternative to exclude is that fractionation *damages enzymes* and that boiled extract merely stabilizes damaged protein. Proposed monitoring battery:

1. **Marker-enzyme panel.** Before and after fractionation, assay at least two soluble enzyme activities that participate in, or report on, the glycolytic pathway (e.g., a kinase and a dehydrogenase) using defined substrate assays, plus one general proteolysis marker (free amino-group release). Acceptance: retentate marker activities ≥80% of starting juice per mg protein after correction for volume changes.
2. **Protein-state checks.** Quantify soluble protein recovery; inspect for aggregation (turbidity at 340 nm, or sedimentable protein after high-speed spin). Acceptance: ≤10% irreversible aggregation.
3. **Latency/reversibility test.** Subject a portion of retentate to the *full time course* of the experiment with matched buffer; if marker activities decay over time, the reconstitution assay must be completed within the validated stability window, or the experiment is invalid (stopping criterion, Section 8).
4. **Dilution-only control arm.** Dilute whole juice in calibrated buffer to the same protein concentration as the reconstituted mixtures and measure its activity. This defines what activity a non-fractionated, equally dilute system would show — the reference against which dilution artifacts are judged.

---

## 4. Experimental Design: Arms, Allocation, Blinding (Proposed)

### 4.1 Reconstitution rules (applied to every mixture)
- **Volume matching:** all mixtures brought to identical final volume with calibrated buffer; every arm includes the same volume of "vehicle" (buffer or boiled-buffer control) so that no arm differs in total added liquid.
- **Protein matching:** all arms containing protein adjusted to identical final protein concentration (measured, not assumed), including arms receiving boiled extract (which contributes some protein; measure and compensate by adjusting retentate input).
- **pH matching:** every mixture checked and, if needed, adjusted to the calibrated working pH (±0.05 units) with dilute acid/base, with the same adjustment volume added to all arms.
- **Ionic matching:** conductivity of every mixture measured; a defined salt add-back solution (composition set from the Section 2.2 calibration and the measured native juice conductivity) used to bring all arms within ±5% of the native-juice conductivity.
- **Phosphate matching:** inorganic phosphate measured in each fraction; all arms supplemented (or not, in deliberate low-phosphate arms) to the calibrated target, from a neutralized phosphate stock identical across arms. Include at least one arm at *saturating* phosphate to test whether phosphate limitation alone explains inactivity.

### 4.2 Arm structure (core set; each n ≥ 4 independent fractionation batches)
Group A — baselines: (1) whole juice, unmanipulated; (2) whole juice, diluted to match reconstitution protein concentration (dilution control); (3) whole juice sham-processed (passed through the device without separation, or mock-dialyzed against its own ultrafiltrate) to capture handling damage.

Group B — fractions alone: (4) retentate-1 alone; (5) filtrate-1 alone; (6) retentate-2 alone; (7) filtrate-2 alone. All pH/ion/phosphate/protein/volume matched.

Group C — reconstitutions: (8) retentate-1 + filtrate-1 at native ratio; (9) retentate-2 + filtrate-2; (10) cross-method: retentate-1 + filtrate-2 and retentate-2 + filtrate-1 (tests whether the active component is method-independent).

Group D — heat arms: (11) retentate + boiled extract (calibrated dose series, e.g., 0.25×, 1×, 4× native-equivalent volume); (12) retentate + boiled filtrate; (13) retentate + boiled retentate (protein-denatured macromolecular control — should *not* restore if the factor is the heat-stable small fraction and boiled protein is inert); (14) retentate + heat-treated inactive analog (see 4.3).

Group E — artifact-exclusion arms: (15) retentate + buffer with matched pH/ions/phosphate but no filtrate-derived material (the key "defined add-back" arm); (16) retentate + dialyzed-and-lyophilized filtrate reconstituted in buffer (removes filtrate water/ion contribution while retaining solutes); (17) retentate + protein stabilizer control (e.g., matched-concentration inert protein such as heat-denatured albumin or boiled-juice protein pellet resuspended) — tests the nonspecific-stabilizer explanation; (18) retentate + filtrate that has been treated to remove small molecules (e.g., charcoal-adsorbed or exhaustively dialyzed filtrate) — a destructive-control test that the filtrate's activity depends on its small-solute content.

### 4.3 Inactive-analog controls
Because the factor is structurally unidentified, a true chemical analog cannot be specified. Proposed proxies: (a) filtrate-equivalent material prepared from a *known-inactive* source (e.g., juice from heat-killed starting material processed identically, or filtrate stored until its reconstituting activity is verified lost); (b) a matched small-molecule cocktail reproducing the filtrate's measured pH, conductivity, and phosphate but lacking organic solutes (essentially arm 15, serving as the "defined ion-only analog"). Both are inactive-analog controls in the operational sense: same handling, same measured bulk chemistry, no biological activity expected.

### 4.4 Randomization, allocation, blinding
- Fractionation batches are the experimental units; within each batch, arm assignments are made by a pre-registered plan with mixture *order* of preparation randomized to decorrelate drift.
- Tubes coded by a second person; the assayist reads fermentation rate without knowledge of arm identity; decoding occurs only after data lock.
- A pre-specified randomization audit: at least one blinded replicate pair of identical mixtures per run to estimate assay noise.

---

## 5. Intervention and Sampling (Proposed)

1. Mix components at 0–4 °C in randomized order; allow a calibrated pre-incubation (duration set in pilot work, e.g., 5–15 min) at assay temperature to permit factor–enzyme association.
2. Initiate fermentation by adding substrate (calibrated saturating glucose plus target phosphate, identical addition to all arms).
3. Sample at pre-specified times (e.g., 0, 10, 20, 30, 60 min) or record continuously.

**Primary measurement:** rate of fermentative gas evolution (e.g., manometric CO₂) or an equivalent validated continuous readout (e.g., ethanol production or glucose disappearance by enzymatic assay), expressed per mg protein per minute. The kinetic slope over the validated linear range is the endpoint, not single-time-point gas volume (which conflates lag and rate).

**Secondary measurements:** pH and conductivity at end of run (drift audit); ATP/ADP or acid-production surrogates if available; marker-enzyme activities post-run (damage audit); residual glucose (completeness check).

---

## 6. Analysis Plan and Quantitative Primary Contrast (Proposed)

**Pre-specified primary contrast.** The single decisive comparison is:

> **C1:** Activity of (retentate + native filtrate) **minus** activity of (retentate + defined buffer add-back, arm 15), both fully matched for pH, ionic strength, phosphate, protein, and volume.

C1 isolates the contribution of the filtrate's specific solute content from every measured bulk-chemistry artifact. If C1 is large and positive, the restoration is not explained by pH, ions, phosphate, dilution, or volume.

**Secondary contrasts (all pre-specified):**
- C2: (retentate + boiled extract) vs. (retentate + boiled retentate + inert-protein control): tests heat-stability of the restorative principle against nonspecific protein stabilization.
- C3: within-method recombination vs. cross-method recombination (arms 8–10): concordance supports a physical component rather than a device artifact.
- C4: retentate-alone activity vs. dilution-control activity scaled for protein: confirms the retentate's loss exceeds what dilution predicts.
- C5: arm 16 (stripped filtrate) and arm 18 (small-molecule-depleted filtrate) vs. arm 8: tests that the active principle is small and nonvolatile/adsorbable-class.

**Statistics (proposed):** mixed-effects model with arm as fixed effect and batch as random effect; the primary test is a two-sided test on C1 at α = 0.05 with a pre-specified minimum effect size of interest (e.g., restoration ≥50% of dilution-control activity defines "meaningful restoration"); secondary contrasts corrected for multiplicity (e.g., Holm). All assumptions (variance homogeneity, approximate normality of residuals) checked; nonparametric fallback specified in advance. No interim peeking; analysis begins only after data lock and unblinding of arm means (not identities) to a second analyst for the coded analysis.

**Decision logic (conditional conclusion):**
- **Conclusion permitted** if: fractions individually inactive (C4 confirms loss exceeds dilution); C1 significantly positive; C2 shows boiled extract substitutes while boiled-protein/stabilizer controls do not; enzyme-integrity acceptance criteria met; cross-method reconstitutions concordant; and destructive filtrate controls abolish restoration. → *"A heat-stable, physically separable, low-molecular-weight component of yeast juice is required for fermentative activity of the protein fraction under these conditions."*
- **Conclusion NOT supported** if arm 15 (defined add-back) restores activity (→ artifact: ions/phosphate/pH), if arm 17 inert protein restores (→ nonspecific stabilization), if enzyme-integrity criteria fail (→ damage), or if boiled retentate restores equally (→ the "factor" is not heat-stable or not separable).
- **Explicitly not concluded in any outcome:** chemical structure, elemental composition, or identity with NAD or any named substance. Identity claims would require a separate chemical characterization program outside this protocol's scope.

---

## 7. Acceptance and Stopping Criteria (Proposed)

**Proceed to main experiment only if:** calibration plateaus found for pH, ionic strength, substrate, and phosphate; fractionation achieves ≥95% protein retention and ≥80% small-solute passage; heat-treatment time validated (Section 2.5); sham-processed juice retains ≥80% of fresh-juice activity per mg protein.

**Within-run stopping rules:** stop and invalidate a run if any arm's final pH deviates >0.1 unit from target, if conductivity spread across arms exceeds ±5% of target, if blinded replicate pairs differ by >2× the pre-assay noise estimate, or if marker-enzyme activity in any protein-containing arm falls below the 80% threshold mid-run.

**Experiment-level stopping:** if two independent batches fail enzyme-integrity criteria despite troubleshooting (Section 9), halt and redesign the separation (gentler conditions) rather than interpreting nulls.

---

## 8. Troubleshooting (Proposed)

- **Retentate retains residual activity:** filtrate incompletely removed → wash retentate with calibrated buffer (recorded wash volumes) until activity reaches background; re-verify protein retention.
- **Recombination fails to restore:** check (a) ratio mismatch — titrate filtrate dose; (b) factor lost during concentration of dialysate — test filtrate-1 (no concentration step); (c) degradation over time — shorten process, add stability-window validation.
- **Boiled extract inactive:** heat calibration wrong → repeat Section 2.5; consider that the factor may be partially heat-labile, which would itself be a reportable conditional finding (the "heat-stable" claim would then be qualified, not assumed).
- **Arm 15 restores activity:** the artifact hypothesis is supported; report that defined pH/ions/phosphate suffice, and the separable-factor claim fails.
- **High batch variability:** increase batch number; investigate juice age, yeast strain lot, and temperature excursions as variance components in the mixed model.
- **Charcoal/dialysis of filtrate fails to remove activity (arm 18):** the active principle is not in the expected small/adsorbable class; flag for re-characterization of the separation — a limit, not a refutation.

---

## 9. Key Uncertainties and What Would Change the Recommendation

1. **Unknown factor stability and size** — handled by graded-cutoff and heat-time calibration; if the factor is larger than expected or heat-labile, the "separable, heat-stable" framing must be revised.
2. **Unmeasured filtrate components** — arm 16/18 cover removal classes, but a component neither adsorbed nor dialyzed under these conditions would escape destructive controls; this residual gap is acknowledged.
3. **Protein stabilization subtleties** — arm 17 uses inert protein, but a specific protein–protein interaction unique to boiled juice proteins could evade it; adding a second, structurally different inert protein would strengthen the exclusion.
4. **NAD-identity question** — entirely out of scope by design; even perfect execution supports only a functional, operational definition ("the heat-stable filtrate activity"), which is the historically appropriate and honest endpoint.

**Word count: ~2,300. All procedures above are proposed; no data are claimed.**
