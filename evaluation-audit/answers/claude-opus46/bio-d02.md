# Claude Opus 4.6 / bio-d02

Original final answer, shared by both scoring rounds.

# Proposed Fractionation and Reconstitution Protocol: Testing Whether a Heat-Stable Separable Factor Is Required for Yeast-Juice Fermentative Activity

**Status: All experiments described below are proposed. No results are reported.**

---

## 1. SCIENTIFIC RATIONALE AND EVIDENCE-TO-INFERENCE CHAIN

### Starting Evidence
The 1906 record demonstrates that yeast-juice can be separated into a low-molecular-weight filtrate and a high-molecular-weight retentate; neither fraction alone sustains fermentation, but recombination restores activity; boiled whole extract can substitute for the filtrate fraction, implying the active small-molecule component survives boiling. The stated interpretive limit is that this reconstitution evidence supports the existence of a heat-stable separable factor but does not determine its chemical structure or establish NAD identity.

### Inference Gap
Five classes of artifact could produce the same reconstitution phenotype without requiring a discrete cofactor:
- **(A1) pH shift** during fractionation inactivates enzymes or alters substrate availability.
- **(A2) Inorganic salt redistribution** removes essential ions (Mg²⁺, K⁺, Mn²⁺) from the retentate.
- **(A3) Phosphate depletion** removes an obligate co-substrate from the retentate.
- **(A4) Dilution** reduces enzyme or substrate concentrations below kinetically effective levels.
- **(A5) Enzyme damage** during handling; the filtrate or boiled extract merely stabilizes damaged enzymes nonspecifically.

### Hypothesis Under Test
**H₁:** Fermentative activity in yeast-juice requires a heat-stable, low-molecular-weight factor that is separable by ultrafiltration and whose restoration cannot be explained by pH, salt, phosphate, dilution, or enzyme-stabilization effects alone.

**H₀:** Loss of activity in the retentate is fully attributable to one or more of artifacts A1–A5.

### Conclusion Logic (Conditional)
If retentate activity is restored by filtrate or boiled extract but **not** by the complete defined supplement (buffer + ions + phosphate + volume match + protein stabilizer), and enzyme integrity is independently confirmed, then H₀ is rejected and the data support the existence of at least one additional heat-stable separable factor. **No claim is made regarding the chemical identity of that factor.**

---

## 2. PREPARATION AND QUALITY CHECKS

### 2.1 Yeast-Juice Preparation
- Lyse fresh compressed baker's yeast by the press-juice method (hydraulic press or bead mill; method to be calibrated for the available equipment).
- Clarify by low-speed centrifugation (3,000 × g, 15 min, 4 °C) to yield crude yeast-juice (YJ).
- Record: total volume, total protein (Bradford), pH, conductivity, inorganic phosphate (molybdate assay), and glucose-dependent CO₂ evolution rate (baseline fermentative activity, see §4).

### 2.2 Calibration of Unknown Parameters
Because exact buffer molarity, ion concentrations, phosphate levels, protein content, and optimal volumes are unavailable from the source record:

| Parameter | Calibration procedure |
|---|---|
| **pH of YJ** | Measure immediately post-lysis; titrate aliquots to ±0.3 pH units and assay activity to define the permissive range. |
| **Ion composition** | Analyse YJ by ICP-OES for K⁺, Mg²⁺, Mn²⁺, Ca²⁺, Na⁺, Zn²⁺. These values set the add-back recipe (§3.3). |
| **Phosphate** | Quantify inorganic Pi by molybdate colorimetry in YJ and in each fraction post-separation. |
| **Protein** | Bradford on YJ and retentate; set volume-matching so retentate protein is ≥ 90 % of YJ protein per unit volume. |
| **MWCO selection** | Pilot ultrafiltration with 10 kDa and 30 kDa membranes; choose the cutoff that places >90 % of total protein in the retentate and passes the boiling-stable activity-restoring component (assessed by reconstitution pilot). |

### 2.3 Enzyme-Integrity Marker Selection
Choose two reporter enzyme activities present in the retentate whose catalytic mechanisms do not require the putative cofactor:

- **Hexokinase** (glucose + ATP → glucose-6-phosphate; coupled to NADP⁺-dependent G6PDH with exogenous NADP⁺ added in excess so the reporter is cofactor-independent).
- **Aldolase** (fructose-1,6-bisphosphate → DHAP + G3P; hydrazine-trap colorimetric assay).

These are measured before and after every manipulation to confirm that enzyme damage (A5) has not occurred.

---

## 3. INDEPENDENT SEPARATION UNIT (FRACTIONATION)

### 3.1 Design: Two Independent Separations
To exclude membrane-specific artifacts, perform ultrafiltration on two independent aliquots of the same YJ batch using **different membrane chemistries** (e.g., regenerated cellulose vs. polyethersulfone), each at the calibrated MWCO. Each separation yields its own Retentate (R) and Filtrate (F). Downstream experiments are run in parallel on both sets; concordance across membrane types is required for any conclusion.

### 3.2 Separation Procedure (per membrane)
1. Load 50 mL YJ onto a stirred ultrafiltration cell, 4 °C.
2. Apply N₂ pressure (calibrated to yield ≤ 2 mL/min flux to minimize protein shearing).
3. Collect filtrate until retentate volume is ~10 mL.
4. **Diafiltration wash:** add 40 mL of Defined Reconstitution Buffer (DRB; §3.3) to retentate, re-concentrate to 10 mL. Repeat twice. This removes residual small molecules while maintaining buffer/ion/phosphate composition and volume.
5. Adjust retentate volume to exactly 50 mL with DRB (volume matching to original YJ; addresses A4).
6. Record: pH, conductivity, protein, Pi, hexokinase activity, aldolase activity in R and F.

### 3.3 Defined Reconstitution Buffer (DRB)
Formulated from calibration data (§2.2) to replicate YJ supernatant milieu:

| Component | Concentration | Rationale |
|---|---|---|
| MES/bis-Tris buffer | Titrated to YJ pH ± 0.05 | Excludes A1 |
| KCl | Matched to YJ [K⁺] | Excludes A2 |
| MgCl₂ | Matched to YJ [Mg²⁺] | Excludes A2 |
| MnCl₂ | Matched to YJ [Mn²⁺] | Excludes A2 |
| ZnCl₂ | Matched to YJ [Zn²⁺] | Excludes A2 |
| CaCl₂ | Matched to YJ [Ca²⁺] | Excludes A2 |
| NaH₂PO₄/Na₂HPO₄ | Matched to YJ [Pi] at YJ pH | Excludes A3 |
| BSA (catalytically inert) | 1 mg/mL (or calibrated to match total non-enzymatic protein lost through membrane) | Addresses A5 crowding/stabilization |

If any ion is below detection limit in YJ, it is omitted from DRB.

### 3.4 Boiled-Extract Preparation
- Heat 50 mL YJ at 100 °C for 10 min; cool on ice; centrifuge to remove precipitated protein.
- Record: pH, Pi, conductivity, protein (expected ~0), hexokinase (expected 0), aldolase (expected 0).
- Verify absence of fermentative activity alone (negative control).

### 3.5 Inactive-Analog Control Preparation
Prepare a solution identical in molecular-weight profile and UV absorbance to the filtrate but lacking the putative cofactor activity: autoclave the filtrate at 134 °C, 30 min (exceeding the stability demonstrated at 100 °C) **or** treat with activated charcoal (which adsorbs nucleotide cofactors while passing salts and buffer), then elute charcoal with ethanol/water to recover non-nucleotide organics. This "depleted filtrate" (DF) is volume- and conductivity-matched to F using DRB. Its purpose is to control for nonspecific organic-molecule effects distinct from the putative cofactor.

---

## 4. EXPERIMENTAL UNITS, ALLOCATION, AND BLINDING

### 4.1 Conditions (10 arms, each in triplicate per membrane type = 60 reaction vessels total)

| Arm | Contents (all at matched 1 mL final volume) | Tests |
|---|---|---|
| **C1** | YJ (undiluted positive control) | Baseline activity |
| **C2** | R alone in DRB | Retentate-only |
| **C3** | F alone | Filtrate-only |
| **C4** | R + F (reconstituted, volume-matched) | Primary reconstitution |
| **C5** | R + DRB only (no F, no boiled extract) | Full artifact-exclusion control (pH + ions + Pi + volume + BSA) |
| **C6** | R + boiled extract (volume-matched) | Heat-stable-factor restoration |
| **C7** | R + DF (depleted filtrate) | Inactive-analog control |
| **C8** | Boiled extract alone | Negative (no enzymes) |
| **C9** | DRB + glucose | Negative (no enzymes, no cofactor) |
| **C10** | R + DRB + additional BSA (2× BSA of C5) | Nonspecific protein-stabilization dose control (A5) |

### 4.2 Blinding
An independent operator codes each vessel (random alphanumeric). The analyst measuring CO₂ evolution and performing enzyme-integrity assays is blinded to arm identity until all raw data are recorded.

### 4.3 Randomisation
Vessel positions in the incubation apparatus (water bath rack or multi-well manometer) are randomized by a random-number generator to control for positional temperature gradients.

---

## 5. INTERVENTION AND SAMPLING

### 5.1 Reaction Initiation
- Equilibrate all vessels to 25 °C (or calibrated optimum) for 5 min.
- Add glucose to 2 % w/v (final) simultaneously via multichannel pipette.
- Cap with manometric or volumetric CO₂-collection apparatus.

### 5.2 Time Course
- Measure CO₂ evolved (µL or µmol) at 0, 15, 30, 60, 90, and 120 min.
- At t = 0 and t = 120 min, withdraw 20 µL for hexokinase and aldolase assays (enzyme-integrity monitoring throughout the reaction).

### 5.3 Post-Reaction Sampling
- Measure residual glucose (glucose oxidase kit) and ethanol (alcohol dehydrogenase-coupled UV assay or GC headspace) to confirm stoichiometric fermentation.
- Measure final pH (to confirm DRB maintained pH within permissive range; excludes A1).

---

## 6. MEASUREMENTS AND INSTRUMENT CALIBRATION

| Measurement | Method | Precision target |
|---|---|---|
| CO₂ evolution | Manometric (Warburg-type) or infrared gas analyser | CV < 10 % across triplicates |
| Glucose consumption | Glucose oxidase colorimetric | ± 0.5 mM |
| Ethanol production | ADH/NAD⁺ coupled UV₃₄₀ or GC | ± 0.5 mM |
| Hexokinase activity | G6PDH-coupled Δ A₃₄₀/min | ± 5 % of YJ baseline |
| Aldolase activity | Hydrazine-trap A₂₄₀ | ± 5 % of YJ baseline |
| pH | Glass electrode | ± 0.02 |
| Inorganic phosphate | Molybdate A₇₀₀ | ± 0.2 mM |

---

## 7. CONTROLS MATRIX AND ARTIFACT EXCLUSION LOGIC

| Artifact | Excluded by comparison | Required outcome |
|---|---|---|
| A1 (pH) | C5 pH = C4 pH = C1 pH (all ± 0.05); DRB buffered | pH equivalent yet C5 inactive |
| A2 (salts) | DRB ion composition matches YJ | C5 inactive despite matched ions |
| A3 (phosphate) | DRB [Pi] matches YJ | C5 inactive despite matched Pi |
| A4 (dilution) | All arms volume-matched to 1 mL; protein concentration in R ≥ 90 % of YJ | C2 and C5 inactive at same concentration |
| A5 (enzyme damage) | Hexokinase and aldolase ≥ 85 % of YJ levels in R at t = 0 and t = 120 min; C10 (extra BSA) does not rescue | Enzymes intact yet retentate inactive |

---

## 8. ANALYSIS PLAN

### 8.1 Primary Quantitative Contrast
**Cumulative CO₂ at 120 min in C4 (R + F) versus C5 (R + DRB)**, analysed by two-sample t-test (or Mann-Whitney if normality is rejected by Shapiro-Wilk, α = 0.05), pooling triplicates from both membrane types only if no significant membrane × arm interaction is detected (two-way ANOVA).

- **Effect-size threshold:** C4 must reach ≥ 50 % of C1 (YJ) cumulative CO₂ and exceed C5 by ≥ 3-fold to be considered biologically meaningful.

### 8.2 Secondary Contrasts
- C6 (R + boiled extract) vs. C5: tests heat-stability of the factor.
- C7 (R + depleted filtrate) vs. C4: tests whether the active component is charcoal-adsorbable / autoclave-labile, supporting specificity.
- C3 and C8 alone: must show < 5 % of C1 activity (confirms enzymes are retained and cofactor alone is insufficient).
- C10 vs. C5: tests whether extra protein rescues; if no rescue, A5 is excluded.

### 8.3 Enzyme-Integrity Acceptance Gate
If hexokinase or aldolase in the retentate (any arm containing R) drops below 85 % of the YJ value at t = 0 or declines > 20 % from t = 0 to t = 120 min **selectively in inactive arms**, the experiment is deemed inconclusive for A5 exclusion and must be repeated with gentler handling (lower transmembrane pressure, shorter processing time, added DTT/glycerol in DRB).

### 8.4 Concordance Requirement
Results must be qualitatively concordant across both independent membrane chemistries. Discordance triggers investigation of membrane-specific adsorption or leaching artifacts.

---

## 9. ACCEPTANCE, STOPPING, AND TROUBLESHOOTING

| Outcome pattern | Interpretation |
|---|---|
| C4 ≫ C5, C6 ≫ C5, C7 ≈ C5, enzymes intact, pH/ions/Pi matched | **Supports H₁:** a heat-stable, charcoal-adsorbable, separable factor is required; artifacts A1–A5 excluded to the resolution of the controls. |
| C4 ≈ C5 ≈ C1, enzymes intact | Factor is not required; DRB alone rescues. Examine which DRB component is responsible by drop-out sub-experiment. H₀ not rejected. |
| C4 ≫ C5 but enzymes degraded in R | Inconclusive; repeat with revised handling. |
| C4 ≫ C5, C6 ≈ C5 | Factor is required but not heat-stable; contradicts boiling evidence. Re-examine boiled-extract preparation. |
| C4 ≫ C5, C7 ≈ C4 | Active component is not charcoal-adsorbable; revise depleted-filtrate preparation or consider non-nucleotide identity. |

### Troubleshooting Calibration Failures
- If YJ baseline fermentation is weak (< 50 µL CO₂ / mL·h), increase yeast freshness or lysis efficiency.
- If diafiltration does not reduce filtrate-spectrum UV₂₆₀ in retentate by ≥ 95 %, add further wash cycles.
- If DRB causes visible protein precipitation, reduce individual ion concentrations and re-measure activity.

---

## 10. EXPLICIT LIMITS OF INTERPRETATION

1. **No chemical identity is claimed.** Even if H₁ is supported, the protocol demonstrates requirement for a separable, heat-stable, low-molecular-weight factor but does not determine whether that factor is NAD⁺, another nucleotide, or a mixture of cofactors.
2. **Charcoal and autoclave controls narrow but do not define structure.** Charcoal adsorbs many aromatic/nucleotide species; autoclave lability is not uniquely diagnostic.
3. **The MWCO boundary is operational, not molecular.** Some factors near the cutoff may partition ambiguously.
4. **Completeness of artifact exclusion depends on calibration accuracy.** If YJ contains an unmeasured essential small molecule not included in DRB (e.g., a trace organic acid), the protocol could misattribute its absence to "the factor."
5. **Generalisability is limited to the yeast strain, lysis method, and substrate (glucose) tested.**

---

## 11. SUMMARY EVIDENCE-TO-CONCLUSION CHAIN

**Evidence (source record):** Fractionation eliminates activity; recombination or boiled-extract addition restores it.
→ **Inference gap:** Restoration could reflect cofactor requirement OR artifact correction.
→ **Proposed protocol:** Adds defined-buffer/ion/phosphate add-back (excludes A1–A3), volume and protein matching (excludes A4), enzyme-integrity monitoring (excludes A5), independent membrane replication, heat control, and inactive-analog control.
→ **Predicted decisive contrast:** If R + F ≫ R + DRB while all artifacts are controlled, the data support the existence of at least one heat-stable separable factor required for fermentation.
→ **Conditional conclusion (if supported):** Yeast-juice fermentative activity depends on a heat-stable, low-molecular-weight, separable factor whose chemical structure remains unassigned by this experiment alone.

*All experiments described herein are proposed; no results are reported.*
