# Claude Opus 4.6 / mol-r01

Original final answer, shared by both scoring rounds.

# Mechanistically Decisive Follow-Up: Does the GSDMD N-Terminal Domain Directly Permeabilize Membranes or Does It Require a Cellular Effector?

---

## 1. UNRESOLVED BIOLOGICAL QUESTION

The evidence establishes that:
- GSDMD is genetically necessary for inflammatory-caspase-driven lytic cell death.
- Proteolytic cleavage liberates an N-terminal domain (GSDMD-NT) from an autoinhibitory C-terminal domain.
- GSDMD-NT is sufficient to kill cells.
- The physical mechanism by which GSDMD-NT compromises membrane integrity is not determined.

**Decisive follow-up question:** Does GSDMD-NT act as a direct, autonomous membrane-disrupting agent (forming pores or lesions in lipid bilayers without any protein partner), or does it require activation of one or more cellular effectors (ion channels, scramblases, lipases, necroptotic machinery, etc.) to compromise membrane integrity?

This question is mechanistically decisive because the answer dictates entirely different downstream biology: a direct pore-former defines a new class of innate-immune effector and implies lipid-specificity as the regulatory checkpoint, whereas an effector-dependent mechanism implies druggable protein–protein interactions and potentially shared death-pathway components.

---

## 2. COMPETING MECHANISTIC HYPOTHESES

### Hypothesis A — Direct Membrane Action
GSDMD-NT inserts into and permeabilizes lipid bilayers autonomously. No cellular proteins, ATP, ion gradients, or signaling cascades are required. Predictions:
- A1. Purified recombinant GSDMD-NT will permeabilize protein-free synthetic liposomes.
- A2. Permeabilization will be observable as discrete conductance steps in planar lipid bilayers (consistent with defined oligomeric pores).
- A3. Membrane disruption in cells will not be rescued by broad-spectrum inhibition of cellular effector pathways (e.g., pan-caspase inhibitors beyond the activating caspase, MLKL knockout, pharmacological blockade of ion channels).

### Hypothesis B — Cellular Effector Activation
GSDMD-NT does not itself form membrane lesions. Instead, it activates a downstream cellular component (e.g., a pannexin channel, a calcium-dependent phospholipase, the MLKL pore-forming pathway, or mitochondrial permeability transition) that executes membrane disruption. Predictions:
- B1. Purified recombinant GSDMD-NT will NOT permeabilize protein-free synthetic liposomes.
- B2. No defined conductance events in protein-free planar bilayers.
- B3. Genetic deletion or pharmacological inhibition of the relevant effector will rescue cell viability even when GSDMD-NT is expressed.

### Hypothesis C (Hybrid)
GSDMD-NT has weak intrinsic membrane-binding/disrupting activity that is dramatically amplified by a cellular co-factor (e.g., a lipid-modifying enzyme that generates its preferred lipid substrate in situ). Predictions:
- C1. Weak or slow liposome permeabilization with pure GSDMD-NT; dramatically enhanced in the presence of a specific cofactor or lipid species.
- C2. Cell-based lethality partially but incompletely rescued by effector inhibition.

---

## 3. STAGED EXPERIMENTAL DESIGN

### STAGE 1 — Minimal Reconstitution in Protein-Free Synthetic Membranes

**Rationale and evidence-to-inference link:** If GSDMD-NT permeabilizes liposomes that contain zero cellular proteins, then no cellular effector is required for the core membrane-disruption event. This is the most direct test of Hypothesis A vs. B.

#### 1a. Liposome Dye-Release Assay

**Protein preparation:**
- Express human GSDMD-NT (residues 1–275, or the exact fragment liberated by caspase-1/4/5/11 cleavage — the precise boundary should be mapped by mass spectrometry of the cleavage product; this is a parameter to be validated experimentally) as a His₆- or GST-tagged fusion in *E. coli* BL21(DE3).
- Purify by affinity chromatography followed by tag cleavage (TEV or PreScission protease) and size-exclusion chromatography. Confirm monodispersity by SEC-MALS. Confirm identity by intact-mass spectrometry.
- **Critical controls:** (i) Full-length GSDMD (should be autoinhibited and inactive). (ii) GSDMD C-terminal domain alone. (iii) A point mutant in a predicted membrane-interacting region (candidate residues to be selected by hydrophobicity analysis and conservation; e.g., mutate a cluster of hydrophobic residues to aspartate — **specific residues flagged as requiring validation**). (iv) Heat-denatured GSDMD-NT. (v) Buffer-only.

**Liposome preparation:**
- Prepare large unilamellar vesicles (LUVs, 100–200 nm diameter by extrusion through polycarbonate filters) encapsulating a self-quenching concentration of sulforhodamine B (50 mM) or carboxyfluorescein.
- Lipid compositions to test: (i) PC:cholesterol (80:20 mol%); (ii) PC:PE:cholesterol (60:20:20); (iii) A composition mimicking the inner leaflet of the mammalian plasma membrane: PC:PE:PS:PI(4,5)P₂:cholesterol (approximate ratios 25:25:20:5:25 mol% — **exact physiological ratios flagged for literature validation**). Rationale: if GSDMD-NT has lipid selectivity (e.g., for phosphoinositides or PS, which mark the inner leaflet), this panel will reveal it and also explain why the intact cell is initially protected.
- All lipid stocks from a single lot; extrusion at room temperature; removal of unencapsulated dye by gel filtration (Sephadex G-50).

**Assay execution:**
- Add GSDMD-NT (concentration range: 50 nM–5 µM, in 2-fold dilutions) to liposome suspension (lipid concentration ~100 µM) at 37 °C in physiological buffer (150 mM NaCl, 20 mM HEPES pH 7.4, 1 mM EDTA).
- Monitor fluorescence dequenching (λ_ex/λ_em for sulforhodamine B: 565/586 nm) continuously for 60 min in a plate reader (e.g., 96-well format, triplicate).
- At endpoint, add 0.1% Triton X-100 to lyse all liposomes (100% release reference).
- Calculate fractional dye release = (F − F₀) / (F_Triton − F₀).

**Interpretation matrix:**

| Outcome | Inference |
|---|---|
| GSDMD-NT causes dose- and time-dependent dye release from protein-free liposomes; full-length protein and C-terminal domain do not | **Strong support for Hypothesis A.** The N-terminal domain autonomously permeabilizes membranes. |
| No dye release at any concentration/time | **Supports Hypothesis B.** A cellular cofactor is required. Proceed to Stage 1c (addition of cell lysate fractions). |
| Dye release only with PI(4,5)P₂- or PS-containing liposomes | **Supports Hypothesis A with lipid specificity.** Suggests that inner-leaflet lipids are the physiological target, explaining autoinhibition at the intact-cell level. |
| Slow, incomplete dye release | **Ambiguous; consistent with Hypothesis C.** Proceed to Stage 1c. |

#### 1b. Planar Lipid Bilayer Electrophysiology

**Rationale:** Dye release shows permeabilization but does not distinguish detergent-like disruption from discrete pore formation. Electrophysiology resolves single-channel events.

**Protocol:**
- Form planar bilayers (painted or folded) across an aperture (diameter ~100–200 µm) in a Teflon partition separating two chambers (cis/trans), using the lipid composition that gave the strongest signal in 1a (or all compositions if there is lipid selectivity).
- Buffer: symmetric 150 mM KCl, 20 mM HEPES pH 7.4, 1 mM EDTA.
- Apply +50 mV holding potential (and test ±20 to ±100 mV range).
- Add GSDMD-NT (100 nM–1 µM) to the cis chamber. Record current (Axopatch 200B or equivalent; filter at 1 kHz, sample at 10 kHz) for ≥30 min.
- Controls: buffer alone, full-length GSDMD, C-terminal domain, denatured GSDMD-NT.

**Interpretation:**

| Outcome | Inference |
|---|---|
| Discrete, stable conductance steps with defined unitary conductance (e.g., in the nS range, suggestive of a large pore) | **Strong support for Hypothesis A — pore formation.** The step size constrains the pore diameter. |
| Erratic, noisy conductance increases without resolvable steps | Membrane destabilization (carpet/detergent mechanism) rather than a defined pore; still direct action but a different physical model. |
| No conductance change | **Supports Hypothesis B** if dye release in 1a was also negative, or indicates that the bilayer system lacks a necessary lipid if 1a was positive. |

#### 1c. Conditional Reconstitution with Cytosolic Fractions (if 1a is negative or ambiguous)

- Prepare S100 cytosolic extract from the same cell type used in the genetic screen (e.g., bone-marrow-derived macrophages or THP-1 cells).
- Fractionate by sequential ammonium-sulfate precipitation and ion-exchange chromatography.
- Add individual fractions plus GSDMD-NT to liposomes and repeat 1a.
- If a fraction restores activity, identify the active component by mass spectrometry.
- This tests Hypothesis B (effector-dependent) and Hypothesis C (cofactor-amplified).

---

### STAGE 2 — Orthogonal Biophysical Measurements on Synthetic Membranes

**Rationale:** Even if Stage 1 supports direct membrane action, the nature of the lesion (proteinaceous pore vs. lipid destabilization vs. toroidal pore) remains undefined. Orthogonal, non-fluorescence-based measurements provide independent evidence and constrain the physical model.

#### 2a. Negative-Stain and Cryo–Electron Microscopy

- Incubate GSDMD-NT (0.5–5 µM) with liposomes (lipid composition from Stage 1 that gives strongest activity) for 10–30 min at 37 °C.
- For negative stain: apply to glow-discharged carbon grids, stain with 2% uranyl acetate, image at 120–200 kV. Look for ring-shaped oligomeric assemblies on or in liposome membranes.
- For cryo-EM: vitrify on holey-carbon grids, collect tilt-series or single-particle data at 300 kV. Resolve the structure of any oligomeric assembly.
- **Positive for A:** Ring or arc-shaped assemblies of defined diameter (predicted: ~15–20 nm outer diameter based on analogy to other pore-forming proteins — **flag: no quantitative prediction can be justified from the supplied evidence alone**).
- **Negative for A:** No ordered assemblies; disordered membrane disruption or no structural change.

#### 2b. Atomic Force Microscopy on Supported Lipid Bilayers

- Deposit supported lipid bilayers on mica.
- Add GSDMD-NT; image in fluid tapping mode over time.
- Quantify pore-like features: diameter, depth (should equal bilayer thickness ~4–5 nm for transmembrane pores), and surface density.

#### 2c. Dynamic Light Scattering / Calcein-Cobalt Quench Assay

- DLS to monitor liposome size changes (lysis → size decrease or aggregation).
- Calcein-cobalt assay: encapsulate calcein-Co²⁺ (quenched) inside liposomes; external EDTA chelates released Co²⁺, causing fluorescence increase — an independent dye-release chemistry that cross-validates 1a.

**Evidence-to-inference link:** Concordance between fluorescence dye release (1a), electrophysiology (1b), electron microscopy (2a), AFM (2b), and DLS/calcein (2c) on the same protein-free membrane system constitutes a multi-method, internally controlled demonstration that GSDMD-NT is a direct, autonomous membrane-permeabilizing agent — or, if all are negative, that it is not.

---

### STAGE 3 — Cellular Validation

**Rationale:** Reconstitution proves sufficiency in vitro; cellular experiments test necessity and physiological relevance. The key question: does the direct pore-forming activity observed in Stages 1–2 account for cell death, or is an additional cellular effector also required?

#### 3a. Inducible Expression of Wild-Type and Mutant GSDMD-NT in Cells

**Cell system:** Use the same cell type from the original genetic screen (e.g., iBMDMs or THP-1). Also use HEK293T cells (which lack inflammasome components) to test sufficiency in a "naïve" background.

**Constructs:**
- Doxycycline-inducible GSDMD-NT (wild-type).
- GSDMD-NT carrying the membrane-interaction mutant(s) identified in Stage 1.
- Full-length GSDMD (autoinhibited control).
- GSDMD-NT fused to a mitochondrial targeting sequence (tests whether lethality requires plasma-membrane localization — if the pore acts on the PM, mis-targeting should reduce canonical pyroptotic morphology).

**Readouts (measured at 1, 2, 4, 6 h post-induction):**
- Plasma-membrane integrity: LDH release, propidium iodide uptake (flow cytometry and live imaging).
- Cell morphology: phase-contrast and fluorescence time-lapse microscopy — pyroptotic swelling and ballooning vs. apoptotic blebbing.
- Electrolyte flux: intracellular potassium measurement by ICP-MS or PBFI fluorescent indicator (potassium efflux is expected from large pores).
- IL-1β processing and release: separate from cell death (the evidence states these can be experimentally uncoupled). ELISA for mature IL-1β in supernatant; western blot for pro- vs. mature forms.

**Interpretation:**

| Outcome | Inference |
|---|---|
| WT GSDMD-NT kills HEK293T cells (lacking inflammasome machinery) with pyroptotic morphology; membrane mutant does not | GSDMD-NT is sufficient for lytic death without requiring inflammasome-associated effectors; the same residues needed for liposome permeabilization are needed in cells. **Strong causal link between direct pore formation and cell death.** |
| WT GSDMD-NT kills inflammasome-competent macrophages but NOT HEK293T cells | A macrophage-specific effector is required; Hypothesis B gains support. |
| Membrane mutant still kills cells despite failing to permeabilize liposomes | GSDMD-NT has a second, effector-dependent killing mechanism in addition to (or instead of) direct pore formation. |

#### 3b. Pharmacological and Genetic Effector Blockade in Cells

**Rationale:** If a cellular effector mediates membrane damage downstream of GSDMD-NT, blocking that effector should rescue viability.

**Interventions (applied before inducing GSDMD-NT):**

| Intervention | Target pathway | Concentration / genetic approach |
|---|---|---|
| Necrosulfonamide (NSA) | MLKL (necroptosis pore) | 5 µM — **dose to be validated by MLKL phosphorylation blot** |
| zVAD-fmk | Pan-caspase | 20–50 µM |
| Glycine | Non-specific cytoprotectant (blocks secondary lysis but not pore formation) | 5 mM |
| BAPTA-AM | Intracellular calcium chelation | 10 µM |
| CBN (carbenoxolone) | Pannexin-1 channels | 50 µM |
| *Mlkl*⁻/⁻ cells | MLKL | CRISPR-Cas9 knockout, confirmed by western blot |
| *Panx1*⁻/⁻ cells | Pannexin-1 | CRISPR-Cas9 knockout |
| *Ripk3*⁻/⁻ cells | RIPK3 (necroptosis kinase) | CRISPR-Cas9 knockout |

**Readout:** LDH release and PI uptake at matched time points.

**Interpretation:**

| Outcome | Inference |
|---|---|
| None of the interventions rescue cells from GSDMD-NT–induced death | **Strong support for Hypothesis A.** No single downstream effector is required; consistent with direct membrane action. |
| One specific knockout or inhibitor fully rescues | **Support for Hypothesis B.** That effector is the executioner, and GSDMD-NT is an upstream activator rather than the pore itself. |
| Partial rescue by calcium chelation or glycine | **Consistent with Hypothesis A with secondary amplification.** Glycine is known to delay osmotic lysis downstream of pore formation without blocking the pore itself. Calcium entry through GSDMD-NT pores could activate secondary pathways (scramblases, calpains) that accelerate death. |

#### 3c. Patch-Clamp Electrophysiology on Intact Cells

**Rationale:** The most direct cellular correlate of Stage 1b. If GSDMD-NT forms pores in the plasma membrane of living cells, whole-cell or cell-attached patch-clamp should detect large-conductance currents coincident with cell swelling.

**Protocol:**
- Whole-cell configuration on cells expressing inducible GSDMD-NT.
- Hold at −60 mV; ramp or step protocols to characterize current–voltage relationship.
- Monitor capacitance (cell swelling → increased capacitance before lysis).
- Record continuously from induction onset.

**Predictions:**
- **Hypothesis A:** Appearance of large, non-selective conductance (consistent with pore diameter from EM) that precedes cell swelling and lysis. Reversal potential near 0 mV (non-selective pore).
- **Hypothesis B:** No intrinsic conductance; or, conductance blocked by a specific channel inhibitor tested in 3b.

---

## 4. CAUSAL INTERPRETATION CHAIN

```
Stage 1 (reconstitution): GSDMD-NT + protein-free liposomes → permeabilization?
       │
       ├── YES → GSDMD-NT is sufficient for membrane disruption without any cellular protein.
       │         │
       │         Stage 2 (orthogonal): EM, AFM, electrophysiology define the lesion structure.
       │         │
       │         ├── Ordered pore → GSDMD-NT is a pore-forming protein.
       │         ├── Disordered disruption → GSDMD-NT is a membrane-lytic peptide/protein.
       │         │
       │         Stage 3 (cellular): Do the same residues / same activity account for cell death?
       │         │
       │         ├── Membrane mutant dead in vitro AND in cells → direct pore = death mechanism.
       │         ├── Membrane mutant dead in vitro but alive in cells → additional factor contributes.
       │         └── Effector KO rescues → amplification pathway identified.
       │
       └── NO  → GSDMD-NT is NOT an autonomous pore-former.
                 │
                 Stage 1c: add cytosolic fractions → identify required cofactor.
                 │
                 Stage 3: effector KO screen → identify the executioner.
```

Each stage answers a logically prior question before the next is interpretable: sufficiency in the absence of cellular proteins (Stage 1) must precede structure determination (Stage 2) and cellular necessity testing (Stage 3), because without Stage 1 one cannot attribute cellular membrane damage to GSDMD-NT's intrinsic activity rather than to an activated effector.

---

## 5. EXPLICIT ALTERNATIVE OUTCOMES AND THEIR CONSEQUENCES

### Scenario I: All stages positive for direct action
GSDMD-NT permeabilizes liposomes, forms visible pores by EM, produces discrete conductance steps in bilayers and cells, membrane-interaction mutants lose activity in vitro and in cells, no effector knockout rescues.

**Conclusion:** GSDMD-NT is a direct, pore-forming effector of pyroptotic cell death. The autoinhibitory C-terminal domain and caspase-cleavage requirement constitute the regulatory switch. Lipid selectivity (if observed) explains why only the inner-leaflet-exposed membrane is targeted and may inform why only certain cell types or organelles are vulnerable.

### Scenario II: Reconstitution negative, cellular effector identified
No liposome permeabilization; a specific knockout (e.g., *Mlkl*⁻/⁻ or *Panx1*⁻/⁻) rescues cell death.

**Conclusion:** GSDMD-NT is an upstream activator, not the executioner. Therapeutic targeting should focus on the effector.

### Scenario III: Reconstitution weakly positive, effector amplification
Slow or low-level liposome permeabilization; cell death partially rescued by calcium chelation; EM shows small or transient pores.

**Conclusion:** GSDMD-NT forms a limited pore (possibly allowing ion flux and IL-1β release) that triggers secondary lytic mechanisms (e.g., calcium-dependent scramblase activation, osmotic swelling). Both the pore and the amplification loop are necessary for full pyroptotic lysis. This would explain how cytokine release (through small pores) and lytic death (requiring amplification) can be experimentally separated, as stated in the evidence.

### Scenario IV: Contradictory results across methods
For example, dye release positive but electrophysiology negative, or EM shows no structures.

**Interpretation:** Technical artifact in one assay (e.g., dye leakage from liposome instability; detergent contamination of protein prep). Requires repetition with fresh reagents, additional controls (e.g., testing the inactive C-terminal domain to rule out non-specific effects of adding any protein), and possibly a different dye/detection system.

---

## 6. FLAGGED PARAMETERS REQUIRING EMPIRICAL VALIDATION

The following numerical or procedural details are stated as starting points and must be optimized:

1. **Exact GSDMD cleavage site:** The residue boundary between N- and C-terminal domains after caspase-1 cleavage. Must be confirmed by mass spectrometry of the cleavage product. Commonly reported but not derivable from the supplied evidence alone.

2. **Lipid composition of the inner leaflet model:** The mol% of PS, PI(4,5)P₂, PE, PC, and cholesterol. Published lipidomic data for the specific cell type should be consulted; different cell types vary.

3. **Protein-to-lipid ratio for liposome assays:** The 50 nM–5 µM range is a starting screen. The physiologically relevant concentration depends on copy number of GSDMD per cell and the volume of the cytosol — values not supplied.

4. **Planar bilayer aperture size and painting solvent:** These affect bilayer stability and capacitance. Standard conditions (decane or squalene as solvent; 150–200 µm aperture) are starting points.

5. **Doxycycline dose for inducible expression:** Must be titrated to achieve expression levels comparable to endogenous GSDMD-NT generated during inflammasome activation; over-expression may produce artifacts.

6. **NSA concentration for MLKL inhibition:** 5 µM is commonly used but should be validated by showing rescue of necroptosis (TSZ-treated cells) in a parallel positive-control experiment.

7. **Time course of patch-clamp recording after induction:** Doxycycline-induced expression requires hours; chemical activation (e.g., adding recombinant active caspase-1 and full-length GSDMD via intracellular delivery) may be faster and more compatible with the time constraints of patch-clamp.

---

## 7. LIMITS OF THE DESIGN

- **Sufficiency ≠ exclusivity.** Even if GSDMD-NT forms pores directly, the cell may employ additional mechanisms in parallel (e.g., GSDMD-NT could also signal to mitochondria). The design detects the dominant mechanism but may miss redundant ones.
- **Recombinant protein may differ from the physiological cleavage product.** Post-translational modifications, local concentration effects at the inflammasome speck, and chaperone-assisted folding are not recapitulated in *E. coli* expression. If reconstitution fails, this should be considered before concluding Hypothesis B.
- **Lipid composition is an approximation.** The in vitro bilayer may lack a critical minor lipid (e.g., cardiolipin, oxidized phospholipids) that is essential for activity. A negative reconstitution result therefore does not definitively rule out direct action — only that direct action under the tested conditions was not observed.
- **The genetic screen identifies necessity, not sufficiency.** GSDMD may be necessary because it activates another necessary component. The reconstitution (Stage 1) specifically addresses this gap.

---

## 8. SUMMARY

The decisive question is whether GSDMD-NT is the physical agent of membrane disruption or an upstream signal. The staged design uses a **minimal, protein-free reconstitution** (liposome dye release and planar bilayer electrophysiology) to test autonomous membrane-permeabilizing activity; **orthogonal structural methods** (cryo-EM, AFM) to define the nature of the lesion; and **cellular validation** (inducible expression of wild-type and mutant constructs, effector knockouts, and whole-cell electrophysiology) to confirm that the in vitro mechanism operates in living cells. Each stage yields interpretable outcomes under each hypothesis, and together they build a causal chain from molecular activity to cell-biological phenotype. The key branch point is Stage 1a: liposome permeabilization by purified GSDMD-NT in the complete absence of other proteins. A positive result would establish GSDMD-NT as a direct pore-forming toxin-like effector of the innate immune system; a negative result would redirect the investigation toward identifying the cellular mediator that GSDMD-NT activates.
