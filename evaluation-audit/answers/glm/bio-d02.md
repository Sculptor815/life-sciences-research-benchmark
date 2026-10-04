# GLM 5.3 FlashX / bio-d02

Original final answer, shared by both scoring rounds.

# Proposed Protocol: Testing Requirement for a Heat-Stable Separable Factor in Yeast-Juice Fermentation

**Status: all experiments below are proposed; no results exist. All quantitative values marked "calibrate" are unknown and must be determined empirically before the main experiment.**

---

## 1. Aim and Central Hypothesis

**Aim.** Determine whether fermentative activity in yeast juice requires recombination of two separable components — a heat-stable, filtrable factor and a heat-labile, protein-containing fraction — and whether that requirement can be distinguished from pH drift, inorganic-salt/phosphate changes, dilution, or enzyme damage during fractionation.

**Central hypothesis.** Filtrate and retentate are individually inactive but jointly active; activity of the recombine is lost when either partner is heat-denatured, and this pattern survives strict matching of pH, ionic composition, phosphate, protein concentration, and volume across all arms.

---

## 2. Evidence-to-Inference-to-Conclusion Chain

**Evidence (from the fixed packet).** (i) The 1906 record separates yeast juice into filtrate and retentate, recombines them, and uses boiled extract as a compensating partner; (ii) fractions are individually inactive while the combination restores activity; (iii) boiled extract can substitute in the compensation; (iv) the curator flags four artifact classes — pH, inorganic-salt and phosphate shifts, enzyme damage, dilution compensated by nonspecific stabilizers; (v) the record's stated limit is that compensation demonstrates separability, not chemical structure, and does not determine NAD identity.

**Inference.** If the recombination effect is real and not artifactual, then in a design where (a) fractions are produced independently and randomized, (b) every recombination arm is matched for pH, conductivity (ionic strength), inorganic phosphate, protein mass, and final volume, (c) heat inactivation is applied symmetrically to each partner, and (d) enzyme integrity is monitored in the labile fraction, the activity difference between native-native recombination and every matched inactive arm can be attributed to the presence of a heat-stable separable factor plus its heat-labile partner — and to nothing else the design varies.

**Conclusion (conditional, see §12).** Only if all acceptance criteria pass may one conclude that a heat-stable, separable, non-protein factor is *required* for fermentative activity under these conditions. One may not conclude anything about its chemical structure, nor that it is NAD, cozymase, or any named cofactor.

---

## 3. Design Logic in Correct Conceptual Order

1. **Reference standard first:** intact (unfractionated) yeast juice defines 100% activity. Without it, "restoration" is unanchored.
2. **Fractionation second:** each preparation is split into filtrate and retentate; fractions are the experimental units.
3. **Matching third:** pH, ions, phosphate, protein, volume are equalized *before* recombination, so the only planned difference between arms is the heat state and identity of the partners.
4. **Recombination fourth:** a factorial heat-state design (native/boiled × filtrate/retentate) tests the requirement symmetrically.
5. **Add-back arms fifth:** explicitly re-introduce whatever the separation changed (ions, phosphate, volume, protein mass) into inactive arms to show these cannot substitute for the factor.
6. **Analysis last:** one pre-specified primary contrast, with preparation as a random effect.

---

## 4. Phase 0 — Calibration of Unknown Parameters (Proposed Procedures, Not Invented Values)

All values below must be measured or titrated on pilot material; none are assumed from the historical record.

**4.1 Buffer system.** Propose a non-chelating, non-reactive buffer compatible with fermentation readouts (e.g., a weak phosphate or bicarbonate-free system if phosphate is itself a measured variable; if phosphate buffering is unavoidable, use it identically in all arms and treat phosphate as an add-back variable, §6.4). **Calibration:** titrate buffer strength so that, after recombination of the most acidic and most basic single fractions, mixture pH drift over 10 min at assay temperature is < 0.05 pH unit.

**4.2 Ion and phosphate set-point.** **Calibration:** measure conductivity and inorganic phosphate (molybdate colorimetric assay) in whole juice, filtrate, and retentate. Define a "reconstituted-juice ion mix" = whole-juice values, and use it for all add-back arms.

**4.3 Protein and volume.** **Calibration:** protein by biuret or equivalent; define protein matching as equal total protein per assay vessel in all arms containing retentate-derived material (±5%). Define volume matching as identical final volume in every vessel; achieve this with buffer, not water, and record the dilution factor of each fraction relative to whole juice.

**4.4 Substrate.** **Calibration:** run a glucose (or sucrose) dose–response on whole juice; select a saturating concentration (rate plateau) for the main experiment.

**4.5 Boiling condition.** **Calibration:** define a boiling protocol (time, vessel geometry, cooling rate) validated on pilot material by two criteria: (a) the boiled filtrate fully substitutes for native filtrate toward retentate (compensation preserved), and (b) boiled material shows no residual fermentative activity when recombined with anything.

---

## 5. Phase 1 — Preparation and Quality Checks

**5.1 Independent preparations.** Propose n = 3–5 independent yeast-juice preparations on different days, each processed identically. Each preparation is one biological replicate; all downstream arms are within-preparation.

**5.2 Per preparation, produce:**
- **W** — whole juice aliquot (reference, never fractionated);
- **F** — filtrate (heat-stable factor candidate);
- **R** — retentate (heat-labile fraction candidate);
- **Fᵇ, Rᵇ** — boiled aliquots of each (from the same parent aliquots, so heat state is the only within-pair difference);
- **BE** — boiled whole-juice extract (compensation reagent, per the 1906 logic).

**5.3 Immediate measurements on every fraction:** pH, conductivity, inorganic phosphate, protein concentration, volume recovered (dilution factor). These feed directly into the matching step (§6).

**5.4 Enzyme-integrity monitoring of the labile fraction (artifact exclusion).** Because R alone is fermentatively inert, integrity must be assessed by surrogate readouts proposed in advance:
- (a) **Non-fermentative marker enzyme(s)** known to be retentate-associated (calibrate on pilot material; e.g., any soluble glycolytic or invertase activity measurable in R without the factor). Report marker activity in R relative to W.
- (b) **Rescue test with excess BE:** incubate R with a surplus of boiled extract; if R+BE(↑) approaches W activity, the labile enzyme machinery is present and undamaged, and the limiting element is the factor. If R+BE(↑) is far below W, suspect enzyme damage — trigger troubleshooting (§11) before the main run.
- (c) **Protein profile** (e.g., SDS-PAGE or equivalent) of R vs W as a gross degradation check.
- (d) **Time-zero vs end-of-run marker activity** to quantify degradation during the assay window.

**5.5 Gate:** W must show robust fermentative activity (calibrate threshold on pilot, e.g., a CO₂-evolution rate above a pre-set floor). If W fails, stop; the preparation is unsuitable.

---

## 6. Phase 2 — Matching and Add-Back Construction (Excluding the Four Alternatives)

Perform after §5.3 measurements, per preparation.

**6.1 pH matching.** Adjust every arm's components (or the recombined mixture) to the same target pH — calibrate the target to whole-juice pH — with the same acid/base and identical titration procedure. Record pre- and post-assay pH for every vessel. *This addresses the pH alternative by measurement and equalization, not assumption.*

**6.2 Ion matching.** Adjust conductivity of every arm to the whole-juice set-point using the calibrated ion mix (§4.2). *Addresses inorganic-salt changes during separation.*

**6.3 Volume/dilution matching.** All vessels brought to identical final volume with buffer; each fraction's dilution factor recorded. Additionally include a **concentration–redilution control** (§7, arm 10): concentrate F (and/or R) back to whole-juice concentration and redilute — if activity tracks the factor's presence and not dilution per se, this arm behaves like its counterpart. *Addresses dilution artifact.*

**6.4 Phosphate matching and add-back.** Measure phosphate in each arm; where a boiled or filtered partner has lost phosphate, add inorganic phosphate to the whole-juice set-point. Additionally, run a dedicated **phosphate-only add-back arm**: boiled or buffer vehicle + R + phosphate to set-point. If phosphate alone restored activity, the "factor" would be exposed as a phosphate artifact; the design detects this. *Addresses phosphate artifact.*

**6.5 Protein matching.** Every arm containing R-derived material receives equal retentate protein per vessel; arms in which R is replaced by Rᵇ receive matched boiled-protein mass. Arms without retentate protein are flagged as protein-absent by design. *Prevents "more protein = more activity" confounds.*

**6.6 Nonspecific stabilizer compensation.** Because the packet flags that damage or dilution may be masked by nonspecific stabilizers, propose adding the same calibrated concentration of an inert stabilizer (e.g., a defined protein carrier or glycerol equivalent — calibrate for compatibility) to **all** arms uniformly, so stabilizer effects cancel across contrasts.

---

## 7. Phase 3 — Arms, Allocation, and Blinding

**7.1 Arm list (per preparation; final volume, pH, conductivity, phosphate, protein matched in all):**

| # | Arm | Purpose |
|---|-----|---------|
| 1 | W (whole juice) | 100% reference |
| 2 | F alone | filtrate inactive |
| 3 | R alone | retentate inactive |
| 4 | F + R | **primary test: native recombination** |
| 5 | Fᵇ + R | factor must be heat-*stable*; enzyme partner intact |
| 6 | F + Rᵇ | heat-labile partner required |
| 7 | Fᵇ + Rᵇ | both inactive |
| 8 | BE + R | 1906-style compensation with boiled extract |
| 9 | Vehicle + R + ion/phosphate add-back | salt/phosphate artifact exclusion |
| 10 | Concentrated-and-rediluted F + R | dilution artifact exclusion |
| 11 | F + R + stabilizer-only change | stabilizer control (§6.6) |
| 12 | Inactive-analog control: heat-denatured substitute protein (calibrated inert protein) + F | nonspecific protein cannot substitute for R |

**7.2 Independent separation.** Arms 2–12 are constructed from fractions produced in §5.2 within each independent preparation; no pooling across preparations before the primary contrast is computed.

**7.3 Allocation and blinding.** Randomize vessel position and assay order within each preparation run (e.g., random permutation; seed recorded). Code the identity of each vessel for the analyst who records gas volumes/readings; decode after all data are locked. Boiled and native aliquots are handled identically in identical vessels so handlers cannot infer condition.

**7.4 Replication.** Propose ≥2 technical replicates per arm per preparation; n = 3–5 preparations. Total vessels ≈ 12 arms × 2–3 replicates × 3–5 preparations.

---

## 8. Phase 4 — Intervention and Sampling

**8.1 Sequence per vessel (proposed):** add buffer → add matched ion/phosphate mix or vehicle → add fraction(s) in pre-randomized order → equilibrate at assay temperature (calibrate; e.g., near the historical fermentation temperature, set on pilot material for rate stability) → add saturating substrate (§4.4) to start → seal for gas collection immediately.

**8.2 Sampling schedule:** continuous or discrete gas measurement (§9) at fixed intervals for a calibrated window chosen from pilot kinetics (early linear phase; avoid substrate depletion). Withdraw parallel sacrificial vessels at start and end for pH, and at end for marker-enzyme activity (§5.4d) — sacrificial design avoids perturbing gas volumes.

**8.3 Pre-registration of the primary contrast and thresholds before unblinding.**

---

## 9. Measurements

**9.1 Primary endpoint.** Initial fermentative rate: CO₂ evolution per unit time during the pre-specified linear window, normalized to total vessel volume (and secondarily to retentate protein). Any gas-collection method is acceptable if calibrated: verify linearity of the manometer/gas burette with an injected known gas volume (calibration check each run day).

**9.2 Secondary endpoints.** (a) pH change per vessel; (b) conductivity and phosphate of recombined mixtures; (c) marker-enzyme activity retention in R (start vs end); (d) total substrate consumed or product formed (calibrate an orthogonal assay if available) to confirm that gas evolution reflects fermentation.

---

## 10. Analysis

**10.1 Primary contrast (pre-specified, quantitative).**

Δ = Rate(F + R) − max[ Rate(Fᵇ + R), Rate(F + Rᵇ), Rate(Fᵇ + Rᵇ), Rate(F alone), Rate(R alone + add-backs) ]

Hypothesis test: mixed-effects model on rates with arm as fixed effect and preparation as random effect; contrast = Arm 4 vs each of Arms 2, 3, 5, 6, 7, 9 (and family-wise correction across these inactive comparators).

**10.2 Acceptance criteria (all must hold):**
- **C1:** Rate(W) exceeds the calibrated reference floor in every preparation (QC gate, §5.5).
- **C2:** Rate(F + R) ≥ 50% of Rate(W) (calibrate this threshold on pilot recombination; 50% is a proposed working value, not a fact).
- **C3:** Each comparator arm in the max[·] term is < 10% of Rate(W) (calibrated inactivity threshold), with the 95% CI of each contrast excluding zero and exceeding the threshold margin.
- **C4:** Compensation arms behave as required: Rate(BE + R) ≥ C2 threshold (boiled extract substitutes — the heat-stability signature); Rate(F + Rᵇ) and Rate(Fᵇ + Rᵇ) below inactivity threshold (heat-labile partner required).
- **C5:** Enzyme integrity: marker-enzyme retention in R ≥ calibrated floor (e.g., ≥ 70% of W marker activity — calibrate) at time zero and ≥ calibrated retention at assay end; R + BE(↑) rescue ≥ C2 threshold.
- **C6:** Artifact arms negative: Arms 9, 10, 11, 12 below inactivity threshold; pH drift < 0.05 unit in all vessels.

**10.3 Stopping rules.** Stop before unblinding and troubleshoot if C1 fails (preparation failure), if C5 fails (enzyme damage suspected — do not interpret the main contrast), or if pilot recombination (F + R) shows no activity in two consecutive preparations (fractionation may be destroying the factor; recalibrate separation conditions). Do not add arms post hoc without declaring them exploratory.

**10.4 Troubleshooting table.**

| Symptom | Likely cause (per packet's artifact list) | Proposed remedy |
|---|---|---|
| Fᵇ + R inactive but BE + R active | Boiling damaged/diluted the heat-stable factor in Fᵇ; or F over-diluted | Concentrate F; recalibrate boiling time; verify Fᵇ phosphate/ions |
| F + R weak, W strong | Retentate enzyme damage | Shorten processing, lower temperature, add matched stabilizer to all arms, re-run §5.4 rescue |
| Arm 9 active | Salt/phosphate artifact — "factor" is ionic | Abandon factor claim; report ionic requirement |
| Arm 12 active | Factor is nonspecific protein/heat-stable protein | Redesign: protease or further fractionation of F (exploratory) |
| All recombinations inactive | Separation destroys factor or pH drift | Recheck §5.3 logs, adjust buffer capacity |

---

## 11. Alternatives Explicitly Excluded and How

- **pH:** measured and equalized in every arm; pH logged pre/post (C6).
- **Inorganic salts and phosphate:** conductivity/phosphate measured; set-point matching plus dedicated add-back arm 9 — activity restored by ions alone would falsify the factor hypothesis.
- **Dilution:** volume matching; concentration–redilution control (arm 10); stabilizer uniformity (§6.6).
- **Enzyme damage:** surrogate marker enzymes, rescue with excess boiled extract, protein profile, time-course retention (C5); boiled arms handled identically so heat treatment itself cannot differentially harm handled samples.
- **Nonspecific protein substitution:** inactive-analog arm 12.

---

## 12. Conditional Conclusion and Limits

**Permitted conclusion if C1–C6 pass:** Under these defined conditions, fermentative activity of yeast juice requires recombination of a heat-labile fraction with a heat-stable, separable, filtrable factor; the requirement survives exclusion of pH, salt, phosphate, dilution, and enzyme-damage artifacts by matched design.

**Explicitly not claimed:** the chemical structure of the factor; its identity with NAD, cozymase, or any named cofactor; its molecular mechanism. As the source summary states, compensation demonstrates separability only; identity and structure would require purification and structural analysis beyond this design. If C3 or C4 fails, the correct conclusion is that the separable-factor hypothesis is not supported under these conditions, and the troubleshooting table governs next steps.

**Key consequential uncertainties:** the calibrated thresholds (50% restoration, 10% inactivity, 70% enzyme retention) are proposed working values requiring pilot confirmation; the buffer system's compatibility with phosphate measurement; and the availability of a valid non-fermentative marker enzyme in R. Each, if mis-set, would bias the primary contrast — hence they are resolved in Phase 0 before any main-run data are interpreted.
