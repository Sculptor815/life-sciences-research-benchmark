# Claude Opus 4.8 / bio-d02

Original final answer, shared by both scoring rounds.

# Proposed Protocol: Testing for a Heat-Stable Separable Factor in Yeast-Juice Fractions

**All experiments below are proposed. No results are reported. Parameter values are to be calibrated, not assumed.**

## Lead Recommendation

Run a factorial fractionation–reconstitution experiment in which yeast-juice filtrate and retentate are each assayed alone and recombined, with the recombination also attempted using boiled extract as the compensating fraction. Match all fractions and the recombinant for pH, defined buffer, ions, phosphate, protein mass, and total volume *before* assay, and monitor enzyme integrity independently. The **primary quantitative contrast** is the fermentation rate of the reconstituted combination versus the summed rates of the individually matched fractions. If, and only if, boiled extract restores activity to an inactive matched retentate while pH/salt/phosphate/dilution/enzyme-integrity controls are held equal, you may conclude conditionally that a **heat-stable, separable, non-enzymatic component is required** — without claiming its chemical structure or that it is NAD.

---

## 1. Concept Map and Evidence-to-Inference-to-Conclusion Chain

**Core claim under test:** Fermentative activity requires a heat-stable, dialyzable/separable factor that is distinct from the heat-labile enzyme fraction.

**Evidence available (per packet):**
- Fractions (filtrate, retentate) are individually inactive; the combination restores activity.
- Boiled extract substitutes for the separable fraction (heat stability).
- The factor is not structurally identified.

**Confounders the design must neutralize:** separation can alter pH, inorganic salts, phosphate, protein concentration, and dilution; boiled extract might act nonspecifically (generic stabilizer, osmolyte, pH/ionic adjustment) rather than as a specific required factor; enzyme damage during fractionation could masquerade as "loss of a factor."

**Inference logic:**
1. If each fraction is inactive but the recombinant is active *under matched physicochemical conditions*, then neither pH, salt, phosphate, dilution, nor volume explains inactivity (these are equalized across arms).
2. If boiled extract restores activity while a heat-destroyed or inactive-analog substitute does not, under identical buffering, then the restoring agent is heat-stable and specific, not a generic stabilizer.
3. If enzyme-integrity markers in the retentate are unchanged across arms, then "inactivity alone" reflects a missing cofactor-like component, not enzyme damage.

**Conclusion (conditional, bounded):** The data support that a heat-stable separable factor is *required* for fermentative activity. The design does **not** identify the factor's chemical structure and does **not** establish that it is NAD; those claims require orthogonal structural/identity evidence outside this protocol.

---

## 2. Preparation and Quality Checks

### 2.1 Starting material
Prepare a single large batch of yeast-juice fermenting preparation; split it so that all downstream fractions derive from one source lot (removes between-batch biological variation as a confounder). Reserve aliquots of the **whole unfractionated juice** as a positive activity reference and as the source of "boiled extract."

### 2.2 Baseline characterization (QC gate before any fractionation)
Measure on the whole juice:
- Fermentation rate (primary readout assay, Section 6).
- pH.
- Total protein (e.g., a colorimetric protein assay standardized to a reference protein).
- Inorganic phosphate concentration.
- Conductivity (proxy for total ionic strength).

**QC acceptance:** whole juice must show robust, reproducible fermentation (coefficient of variation across triplicate aliquots below a pre-set threshold, e.g., CV < 15%; calibrate threshold in a pilot). If not, do not proceed — fix the preparation first.

### 2.3 Boiled extract
Prepare boiled extract by heating an aliquot of whole juice under defined, recorded conditions (temperature, duration) sufficient to destroy enzymatic activity, then clarifying. **Calibration needed:** determine minimal heating time/temperature that abolishes fermentative enzyme activity (assayed per Section 6) in a boiled-only control while retaining the putative heat-stable factor. Proposed calibration: a heat–time matrix (e.g., several temperatures × several durations) tested for (a) loss of standalone activity and (b) retention of reconstituting capacity when added to fresh retentate. Choose the mildest condition that gives zero standalone activity.

---

## 3. Independent Separation (Two Orthogonal Methods)

To avoid a method-specific artifact (the separation procedure itself being the cause), perform fractionation by **two independent principles**:

- **Method A — size separation** (e.g., filtration/dialysis across a defined molecular-weight cutoff): yields filtrate (small/diffusible) and retentate (large/enzyme-bearing).
- **Method B — a different physical basis** (e.g., size-exclusion or ultracentrifugal/precipitation-based fractionation): yields a low-molecular-mass fraction and a protein fraction.

**Inference value:** if the heat-stable-factor requirement reproduces across both separation principles, the effect is unlikely to be an artifact of one method's incidental pH/salt/phosphate perturbation. Record pH, conductivity, phosphate, and protein for every fraction from both methods.

**Note on dialysis as an independent axis:** dialysis against defined buffer also serves double duty — it lets you *impose* a known common buffer/ion environment on fractions (Section 4), decoupling physicochemical state from fraction identity.

---

## 4. Defined Buffer, Ion Add-Back, Phosphate, Protein, and Volume Matching

This section neutralizes the pH/salt/phosphate/dilution/volume confounders explicitly. **All target values are calibrated, not assumed.**

### 4.1 Common buffer
Equilibrate (by dialysis or defined dilution) every fraction and every assay mixture into a **single defined buffer** at a fixed pH. **Calibration:** determine the pH optimum of the whole-juice fermentation in a pilot pH–rate curve; set the common buffer pH at that optimum and verify buffer capacity holds pH constant over the assay window.

### 4.2 Ion and phosphate add-back
Define target concentrations for key inorganic ions and for phosphate, then add them back to **every arm** so all arms share identical ionic strength (verified by conductivity) and identical phosphate (verified by phosphate assay). **Calibration:** 
- Phosphate dose–response on whole juice to find a saturating, non-inhibitory phosphate level; set all arms to that level.
- Ionic strength titration to find the range over which rate is insensitive; set all arms within that plateau.

The point is not to find optima per se but to ensure **no arm differs in pH, ionic strength, or phosphate** — so these cannot explain differential activity.

### 4.3 Protein matching
Measure protein in each fraction. For arms where the biologically relevant protein differs (e.g., filtrate alone has little protein), **match total protein mass** by adding an inert, catalytically irrelevant bulking protein to equalize protein concentration across arms where appropriate. **Caution:** the bulking protein must be shown not to affect fermentation or to act as a nonspecific stabilizer (test in a control arm, Section 5). **Calibration:** titrate bulking protein into whole-juice assay to confirm inertness.

### 4.4 Volume and dilution matching
Fix a single final assay volume for all arms. Each fraction is brought to the same volume with common buffer so that the **enzyme fraction experiences the same dilution** in "alone" and "recombined" arms. This is the specific control against the "dilution reduces activity" artifact: the retentate is at identical concentration whether assayed alone or with the added factor.

---

## 5. Experimental Arms (Interventions and Controls)

Each arm is prepared to identical pH, ionic strength, phosphate, protein mass, and final volume (Section 4). Minimum arm set (replicate each; see Section 7):

| Arm | Composition | Purpose |
|---|---|---|
| 1 | Whole juice (matched) | Positive activity reference |
| 2 | Retentate alone | Individually inactive test |
| 3 | Filtrate alone | Individually inactive test |
| 4 | Retentate + Filtrate (recombined) | Reconstitution test |
| 5 | Retentate + Boiled extract | Heat-stable-factor substitution |
| 6 | Retentate + Heat-destroyed "factor" control | **Negative heat control** — boiled extract further treated to destroy the factor (see 5.1) |
| 7 | Retentate + inactive-analog substitute | **Inactive-analog control** — nonspecific stabilizer/osmolyte/bulking agent in place of factor |
| 8 | Buffer-only blank | Background/drift |
| 9 | Boiled extract alone | Confirms substitute has no standalone activity |
| 10 | Filtrate + Filtrate (self, volume-matched) | Controls that "adding any second fraction" isn't the cause |

**Repeat the full arm set for each separation method (A and B).**

### 5.1 Heat control (critical for the heat-stability claim)
Arm 6 tests whether activity restoration specifically requires the heat-stable factor. Take boiled extract and apply a treatment expected to destroy the candidate factor (e.g., a harsher/longer thermal or chemical treatment) *without* adding confounding salts/pH shifts (re-equilibrate to common buffer). If Arm 5 restores activity but Arm 6 does not, the restoring agent behaves as a definable, destructible component rather than a generic physicochemical adjustment. **Calibration:** the destroying treatment must be validated to abolish reconstituting capacity while not introducing inhibitors — test the treated buffer alone added to whole juice for inhibition.

### 5.2 Inactive-analog control (critical against nonspecific stabilizer artifact)
Arm 7 substitutes a nonspecific stabilizer / osmolyte / inert bulking agent (chosen to mimic colligative or crowding effects of boiled extract) for the boiled extract. If Arm 7 fails to restore activity while Arm 5 succeeds, the restoration is specific, not a generic stabilizing or crowding effect.

---

## 6. Measurements

### 6.1 Primary readout — fermentation rate
Quantify fermentative activity as **rate of fermentation** (e.g., volumetric gas/CO₂ evolution per unit time, or substrate-consumption/product-formation rate) under fixed, defined conditions (temperature, substrate concentration, time window). Use a continuous or densely sampled time course so rates are measured in the linear/initial-rate regime, not endpoint only. **Calibration:** establish the linear window and substrate-saturating concentration in a pilot on whole juice.

### 6.2 Enzyme-integrity monitoring (independent of the fermentation readout)
To exclude "enzyme damage" as the explanation for retentate inactivity, monitor the integrity of the heat-labile enzyme machinery **independently** of the fermentation assay. Proposed approaches (use at least one, ideally two):
- An activity assay for a component enzyme step that does **not** require the separable factor, run on the retentate in each arm, to show the enzyme protein remains catalytically competent.
- A structural/quantity marker (e.g., protein integrity by a size/denaturation-sensitive readout) comparing retentate across arms.

**Acceptance:** enzyme-integrity markers must be statistically indistinguishable between the "retentate alone" and "retentate + factor" arms. If retentate in Arm 2 shows degraded enzyme relative to Arm 4/5, the design cannot distinguish "missing factor" from "damaged enzyme," and the result is inconclusive until fractionation is made gentler.

### 6.3 Physicochemical verification (per arm, at assay time)
Record final pH, conductivity, phosphate, and protein in each prepared arm to **document** that matching was achieved. These are not outcomes but QC confirmations that the confounders were held equal.

---

## 7. Independent Units, Replication, Allocation, and Blinding

### 7.1 Independent units
The unit of independent replication is a **separately prepared fraction set processed on a distinct occasion** (biological/process replicate), not merely repeated pipetting from one tube (that is technical replication). Plan both: technical replicates within a run to estimate assay noise; independent process replicates across runs/days to estimate reproducibility. **Calibration:** a pilot variance estimate sets the number of independent replicates via power calculation for the primary contrast (Section 8).

### 7.2 Allocation and run-order
Randomize the assay order of arms within each run to avoid time/drift confounding (e.g., instrument warm-up, reagent aging). Interleave arms rather than running all of one arm together.

### 7.3 Blinding
Label coded tubes so the operator performing the fermentation assay and the analyst scoring rates are **blinded to arm identity**. Unblind only after rates are recorded. This guards against expectation bias in reading gas evolution / endpoint calls.

---

## 8. Analysis and the Quantitative Primary Contrast

### 8.1 Primary contrast
Define reconstitution quantitatively. The key signature of a *required co-acting* factor is **supra-additivity**: the recombinant rate exceeds the sum of the individual fraction rates.

Primary statistic:
$$\Delta = R_{\text{recombined}} - \left( R_{\text{retentate}} + R_{\text{filtrate}} \right)$$

Test H₀: Δ ≤ 0 (no restoration beyond additivity) vs H₁: Δ > 0. Because individual fractions are expected to be near-zero, this reduces to testing whether the recombinant rate significantly exceeds background and exceeds either fraction alone.

Parallel contrast for boiled-extract substitution:
$$\Delta_{\text{boil}} = R_{\text{ret+boiled}} - \left( R_{\text{retentate}} + R_{\text{boiled alone}} \right)$$

### 8.2 Specificity contrasts (confounder exclusion, quantitative)
- Heat specificity: R(Arm 5, ret+boiled) **>** R(Arm 6, ret+heat-destroyed), with a pre-set minimum effect size.
- Nonspecific-stabilizer exclusion: R(Arm 5) **>** R(Arm 7, inactive analog).
- Dilution/volume exclusion: R(Arm 2, retentate alone at matched volume) remains low — i.e., bringing retentate to full assay volume with buffer does not itself restore activity.

### 8.3 Statistical model
Use a mixed-effects model with arm as a fixed effect and independent-replicate/run as a random effect; report effect sizes with confidence intervals, not p-values alone. Pre-register the contrasts and the minimum biologically meaningful effect size before unblinding.

### 8.4 Cross-method concordance
Require the restoration effect to replicate qualitatively (sign) and ideally quantitatively across separation Methods A and B.

---

## 9. Acceptance, Positive-Result, and Stopping Criteria

**Declare support for the heat-stable-factor hypothesis only if ALL hold:**
1. Arms 2 and 3 (fractions alone) are inactive (not distinguishable from blank, within a pre-set margin).
2. Arm 4 (recombined) is active with Δ significantly > 0.
3. Arm 5 (retentate + boiled extract) restores activity.
4. Arm 6 (heat-destroyed) does **not** restore (R5 > R6, meeting effect-size threshold).
5. Arm 7 (inactive analog) does **not** restore (R5 > R7).
6. Enzyme-integrity markers equal across retentate-containing arms.
7. pH, ionic strength, phosphate, protein, volume documented equal across arms.
8. Effect reproduces across both separation methods and across the pre-specified number of independent replicates.

**Inconclusive / do-not-conclude conditions:**
- Any confounder (pH, ion, phosphate, protein, volume) not successfully matched → repeat with corrected matching.
- Enzyme-integrity markers degraded in retentate-alone → gentler fractionation needed; current data cannot separate "missing factor" from "damaged enzyme."
- Arm 7 restores as well as Arm 5 → effect is a nonspecific stabilizer/crowding artifact, not a specific factor.

**Stopping rules:**
- Stop for success when criteria 1–8 are met at the pre-planned replicate count.
- Stop for futility if, after the powered number of replicates, Δ confidence intervals exclude the pre-set minimum meaningful effect.
- Stop and troubleshoot (not conclude) if QC gates (Section 2.2, matching, integrity) fail.

---

## 10. Troubleshooting

- **Whole juice inactive at baseline:** fix preparation before fractionating; check substrate, temperature, phosphate (phosphate is known to participate in fermentation — ensure it is present and controlled).
- **Recombinant inactive despite expectation:** check that fractionation did not strand both an enzyme *and* a cofactor requirement in the same fraction; verify enzyme integrity; verify the factor survived separation (test factor fraction + fresh whole-juice enzyme).
- **Fractions "alone" show residual activity:** improve separation completeness; confirm cutoff; the "inactive alone" premise must hold for the contrast to be interpretable.
- **pH/conductivity/phosphate mismatch between arms:** extend dialysis equilibration; re-measure; the matching step is mandatory, not optional.
- **High inter-run variance:** increase independent replicates; tighten temperature/timing control; confirm linear-regime sampling.
- **Boiled extract introduces inhibition:** re-equilibrate boiled extract to common buffer; test boiled extract alone added to whole juice for inhibitory effect; adjust boiling calibration to mildest sufficient condition.
- **Bulking/analog protein not inert:** rechoose an inert agent validated by the whole-juice inertness titration (Section 4.3).

---

## 11. Alternatives, Limits, and the Conditional Conclusion

### 11.1 Alternatives the design addresses
- *pH/salt/phosphate changes during separation* → neutralized by common buffer + ion/phosphate add-back + per-arm verification.
- *Dilution* → neutralized by volume matching so enzyme concentration is identical across alone/recombined arms.
- *Enzyme damage* → neutralized/exposed by independent enzyme-integrity monitoring.
- *Nonspecific stabilizer in boiled extract* → neutralized by the inactive-analog control (Arm 7) and the heat-destroyed control (Arm 6).

### 11.2 Residual limits (what this design cannot do)
- It does **not** reveal the chemical structure of the factor. Restoration of function is not structure elucidation.
- It does **not** establish that the factor is NAD or any specific molecule. Even with perfect behavior-based evidence of a heat-stable required component, molecular identity requires orthogonal evidence (purification to homogeneity, structural/spectroscopic/analytical identification, and demonstration that the pure identified molecule reproduces the restoration) — explicitly outside this protocol.
- "Heat-stable" is operationally defined by the calibrated boiling conditions; it is a functional stability claim, not a thermodynamic characterization.
- The separable factor could be a class/mixture rather than a single species; functional reconstitution cannot resolve this.

### 11.3 Conditional conclusion (as to be reported)
*If* the acceptance criteria (Section 9) are met across both independent separation methods and the powered replicate set, *then* the results support the conclusion that **fermentative activity in yeast-juice fractions requires a heat-stable, separable, non-enzymatic component**, with pH, inorganic salt, phosphate, dilution, volume, nonspecific-stabilizer, and enzyme-damage explanations excluded by the matching and control arms. **This conclusion is strictly functional; it makes no claim about the factor's chemical structure and does not identify the factor as NAD.** Any identity claim is deferred to subsequent purification and structural studies.

---

## Summary of Calibration Procedures (for unknown parameters)

| Unknown parameter | Calibration procedure (proposed) |
|---|---|
| Buffer pH | pH–rate curve on whole juice; set at optimum with adequate buffer capacity |
| Ionic strength target | Ionic-strength titration; set on insensitive plateau; verify by conductivity |
| Phosphate target | Phosphate dose–response; set at saturating non-inhibitory level |
| Protein-match level | Measure fraction proteins; add validated inert protein to equalize; confirm inertness by titration |
| Final assay volume / dilution | Fix one volume; verify retentate-alone (matched volume) stays inactive |
| Boiling condition | Heat–time matrix: mildest condition abolishing standalone activity yet retaining reconstituting capacity |
| Factor-destroying treatment (Arm 6) | Validate loss of reconstituting capacity + no added inhibition |
| Linear assay window / substrate | Pilot time course on whole juice; sample in initial-rate regime |
| Replicate number | Power calculation from pilot variance for the primary Δ contrast and pre-set effect size |
| Separation cutoff/method | Two independent methods; verify completeness so fractions are individually inactive |

**All experiments described are proposed; no outcomes are asserted.**
