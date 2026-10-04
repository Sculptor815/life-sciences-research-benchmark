# DeepSeek V4.1 Flash / mol-r01

Original final answer, shared by both scoring rounds.

## Bottom line

The decisive follow-up question is: **does the liberated GSDMD amino-terminal domain directly disrupt the lipid bilayer, or does it act upstream of another cellular effector that then compromises membrane integrity?** The most informative first test is whether purified GSDMD-N can permeabilize a defined, protein-free lipid bilayer. The most informative cellular test is whether direct expression of GSDMD-N still kills cells when candidate downstream effectors are removed or inhibited. Direct membrane action requires GSDMD-N to be sufficient in a minimal lipid system and to remain sufficient in cells lacking the putative effector. Indirect action predicts failure or strong attenuation in protein-free liposomes and rescue/blockade by the effector.

The evidence packet establishes necessity of GSDMD, domain separation by proteolysis, sufficiency of the N-terminal domain to induce death, autoinhibition of the intact protein, and separability of cytokine processing from release. It does **not** establish the physical mechanism of membrane compromise. The study below is therefore designed to discriminate mechanism, not to assume one.

---

## 1. Unresolved biological question

**Question:** Is the GSDMD N-terminal domain itself the membrane-perturbing agent, or is it an upstream activator of a separate cellular effector that disrupts membrane integrity?

### Competing mechanisms

**H1 — Direct membrane action.**  
After proteolytic liberation, GSDMD-N binds membrane lipids, undergoes a conformational change and/or oligomerizes, and creates a pore or lytic lesion in the lipid bilayer. No other cellular protein or enzymatic cascade is required for the primary membrane lesion.

**H2 — Indirect action via another cellular effector.**  
GSDMD-N engages a cellular protein, membrane-associated enzyme, ion channel, lipid-modifying enzyme, redox system, or other effector. That effector then compromises membrane integrity. GSDMD-N is necessary but not sufficient for the primary lesion.

**H3 — Mixed mechanism.**  
GSDMD-N directly forms a primary pore, but full cellular lysis requires secondary effector-dependent amplification, membrane remodeling, or osmotic collapse. Distinguishing H3 from H1/H2 requires partial-loss and epistasis tests.

### Distinct predictions

| Test | H1 direct | H2 indirect | H3 mixed |
|---|---|---|---|
| Purified GSDMD-N + protein-free liposomes | Permeabilizes | Fails or requires cofactor | Permeabilizes weakly or only at high concentration |
| Planar lipid bilayer | Discrete conductance steps/pores | No intrinsic channel | Small or unstable conductance |
| Effector knockout/inhibition in cells | No rescue | Blockade of lysis | Partial rescue/delay |
| Direct N-domain expression in effector-null cells | Kills | Fails to kill | Delayed/partial killing |
| Order of events | N-domain membrane binding precedes lysis | Effector activation precedes lysis | N-domain binding precedes, effector activation follows |

---

## 2. Evidence-to-inference-to-conclusion chain

**Evidence 1:** A genetic screen identifies GSDMD as necessary for inflammatory-caspase-associated lytic death in the tested cells.  
**Inference:** GSDMD is required in the pathway, but necessity does not reveal whether it directly damages membranes or acts through another effector.

**Evidence 2:** Proteolytic cleavage separates two domains.  
**Inference:** The cleavage event is a candidate switch. The relevant active species may be one domain, but the physical target of that domain is unknown.

**Evidence 3:** The liberated amino-terminal domain can induce cell death; the intact protein is autoinhibited.  
**Inference:** GSDMD-N is sufficient to trigger death in cells. This still does not distinguish direct membrane action from activation of a downstream lethal effector.

**Evidence 4:** Cytokine processing and cytokine release can be separated experimentally.  
**Inference:** Caspase-dependent processing can be monitored independently of membrane permeabilization. This is useful for ordering events: processing marks upstream inflammatory-caspase activity, whereas release reports membrane compromise.

**Evidence 5:** The supplied evidence does not determine the physical mechanism by which the active domain compromises membrane integrity.  
**Inference:** The decisive experiment must measure membrane perturbation directly, in a minimal system, and then test epistasis in cells.

**Conclusion:** The field needs a staged test of sufficiency and necessity: first, GSDMD-N alone on defined membranes; second, orthogonal biophysical confirmation of a membrane lesion; third, cellular validation with effector removal; fourth, causal rescue/order-of-events tests.

---

## 3. Proposed staged study

### Stage 0 — Reagent definition, controls, and missing parameters

**Purpose:** Generate clean reagents that isolate the N-terminal domain and distinguish it from full-length autoinhibited GSDMD and the C-terminal domain.

**Proposed operational details:**

1. **Constructs.** Use the GSDMD species and isoform from the tested system once specified. Define the N-terminal and C-terminal domain boundaries by the cleavage event observed in the screen. If the exact cleavage site is not given, map it empirically using recombinant inflammatory caspase and mass spectrometry.  
   - Full-length GSDMD.  
   - Full-length cleavage-resistant variant if the cleavage site can be identified or mutated without disrupting folding.  
   - N-terminal domain alone.  
   - C-terminal domain alone.  
   - N-terminal domain with candidate lipid-binding or oligomerization mutations, once identified in Stage 1–2.  
   - Empty vector and irrelevant protein controls.

2. **Expression and purification.** Because GSDMD-N may be toxic to expression hosts, a practical route is to express full-length GSDMD with an affinity tag, purify the autoinhibited protein, then cleave in vitro with the relevant inflammatory caspase. If the tag is placed on the C-terminal domain, the liberated N-terminal domain can be separated from the C-terminal fragment and tagged caspase by affinity chromatography. Verify purity by SDS-PAGE, immunoblot, and mass spectrometry. Remove endotoxin for cellular work.  
   - **Missing:** exact tag, tag position, expression host, caspase identity, cleavage buffer, temperature, time, and final protein concentration. These must be determined empirically.

3. **Controls.** Full-length GSDMD without caspase; full-length GSDMD plus caspase; caspase alone; cleavage-resistant full-length plus caspase; heat-inactivated N domain; C-terminal domain; buffer alone; and detergent-permeabilized membranes for maximal release.

**Causal link:** If purified N domain, but not full-length or C-terminal domain, damages membranes, the active species is the N domain. If full-length also damages membranes, the autoinhibition model or reagent purity is in question.

---

### Stage 1 — Minimal reconstitution with protein-free lipid bilayers

**Purpose:** Test whether GSDMD-N is sufficient to permeabilize a defined lipid bilayer without any cellular effector.

**Proposed operational details:**

1. **Liposome preparation.** Prepare large unilamellar vesicles (LUVs) by thin-film hydration and extrusion through 100 nm polycarbonate membranes. Encapsulate a self-quenching fluorescent dye such as calcein or sulforhodamine. Remove free dye by size-exclusion chromatography. Confirm vesicle size by dynamic light scattering.

2. **Lipid compositions to test.** Use a panel, because lipid dependence is mechanistically informative:
   - 100% neutral phospholipid, e.g., DOPC.
   - Neutral + acidic phospholipid, e.g., DOPC:DOPG or DOPC:DOPS.
   - Neutral + cholesterol.
   - Plasma-membrane-like mixture.
   - Mitochondria-like mixture, if relevant to the cell type.
   - Brain polar lipid extract as a complex natural membrane.
   - Exact molar ratios are **missing** and should be fixed from pilot studies; do not treat them as established.

3. **Leakage assay.** Add purified GSDMD-N at increasing concentrations to dye-loaded LUVs. Measure fluorescence at the dye’s emission wavelength. Define 0% release as buffer-only and 100% release as detergent-lysed vesicles. Calculate percentage release.  
   - **Missing numerical settings:** protein concentration range, incubation time, temperature, buffer pH, ionic strength, and dye concentration. Determine by pilot titration.

4. **Controls.** Full-length GSDMD, C-terminal domain, heat-inactivated N domain, irrelevant protein, buffer, and detergent. Include liposomes without protein.

5. **Interpretation.**
   - If GSDMD-N causes reproducible, dose-dependent leakage from protein-free liposomes, it has intrinsic membrane-permeabilizing activity.
   - If it fails across all lipid compositions, a required cofactor or effector is missing.
   - If it works only on a specific lipid composition, the mechanism is lipid-dependent but still potentially direct.

**Causal link:** This is the minimal direct test. Sufficiency in a protein-free bilayer is strong evidence for H1. Failure under conditions where GSDMD-N binds is evidence for H2 or a missing cofactor.

---

### Stage 2 — Orthogonal biophysical measurements

**Purpose:** Confirm that any leakage reflects a defined membrane interaction and not a nonspecific artifact. Distinguish direct pore formation from detergent-like solubilization or activation of a contaminating enzyme.

**Proposed measurements:**

1. **Membrane binding.** Incubate GSDMD-N with LUVs, ultracentrifuge, and quantify protein in pellet versus supernatant by immunoblot or fluorescence. Use liposome flotation as an orthogonal binding assay. Test PC-only versus acidic-lipid and cholesterol-containing vesicles.  
   - Direct model predicts binding and leakage correlate.  
   - Indirect model may show binding without leakage if an effector is missing.

2. **Oligomerization.** Incubate GSDMD-N with or without liposomes, crosslink with DSS or BS3, and analyze by SDS-PAGE and immunoblot. Use native or blue-native PAGE, size-exclusion chromatography coupled to multi-angle light scattering, or single-molecule FRET.  
   - Direct pore model predicts membrane-dependent oligomerization into defined species.  
   - Indirect model predicts no intrinsic pore-sized oligomer, or oligomerization only after effector addition.

3. **Planar lipid bilayer electrophysiology.** Add purified GSDMD-N to one chamber of a planar lipid bilayer. Record current at positive and negative holding voltages. Look for discrete stepwise conductance increases, open-channel behavior, and ion selectivity by reversal potential under asymmetric KCl.  
   - Direct model predicts discrete pores or defined conductance steps.  
   - Indirect model predicts no channel activity unless effector is added.

4. **Giant unilamellar vesicle imaging.** Form GUVs containing a fluorescent lipid and a soluble dye. Add fluorescently labeled GSDMD-N. Monitor binding, clustering, and dye efflux by confocal microscopy.  
   - Direct model predicts local protein accumulation followed by membrane permeabilization.  
   - Indirect model predicts binding without permeabilization unless effector is present.

5. **Structural imaging.** Incubate GSDMD-N with liposomes and visualize by negative-stain electron microscopy or cryo-electron microscopy. Look for rings, arcs, pores, or membrane deformation. This is supportive, not definitive, unless high resolution is achieved.

6. **Size-cutoff measurements.** Use encapsulated dextrans of different molecular weights to estimate whether the lesion is a defined pore or a general lytic defect.  
   - Direct pore model predicts a size cutoff.  
   - Indirect enzymatic or detergent-like model may show progressive membrane disassembly without a sharp cutoff.

**Causal link:** Orthogonal measurements convert “leakage” into a mechanism: binding, oligomerization, conductance, and membrane deformation. If these are absent, the leakage may be nonspecific or require an effector.

---

### Stage 3 — Cellular validation and effector epistasis

**Purpose:** Test whether the mechanism inferred in vitro operates in the tested cells and whether another cellular effector is required.

**Proposed operational details:**

1. **Cell system.** Use the tested cell type from the screen once specified. Generate isogenic wild-type, GSDMD knockout, and GSDMD knockout lines reconstituted with:
   - Full-length GSDMD.
   - Cleavage-resistant full-length GSDMD.
   - N-terminal domain expressed directly, bypassing caspase cleavage.
   - N-terminal domain with candidate lipid-binding/pore mutation.
   - C-terminal domain.
   - Empty vector.

   **Missing:** exact cell line, species, passage, culture medium, transfection/transduction method, selection, and expression levels. These must be controlled by comparing protein levels across variants.

2. **Inflammatory caspase activation.** Use the trigger from the original screen once specified. Confirm caspase activation by activity assay, FLICA, or immunoblot for caspase processing. Separately measure cytokine processing by immunoblot and cytokine release by ELISA, using the evidence that processing and release are separable.

3. **Membrane integrity and order of events.** Measure membrane permeabilization by:
   - PI or Sytox uptake.
   - LDH release.
   - Calcein or dextran release from preloaded cells.
   - Time-resolved imaging of fluorescent GSDMD-N membrane recruitment and dye influx.

   Direct model predicts GSDMD-N recruitment and membrane permeabilization precede or occur independently of effector activation. Indirect model predicts effector activation precedes permeabilization.

4. **Effector discovery.** Because the evidence does not identify a downstream effector, use unbiased approaches:
   - Immunoprecipitation of GSDMD-N followed by mass spectrometry.
   - Proximity labeling with TurboID or APEX fused to GSDMD-N.
   - CRISPR modifier screen for genes whose loss blocks or enhances GSDMD-N-induced death.
   - Phosphoproteomic or lipidomic profiling after GSDMD-N activation.

   **Missing:** candidate effector identities. These are to be discovered, not assumed.

5. **Effector validation.** For top candidates, perform CRISPR knockout or RNAi knockdown, pharmacological inhibition, and rescue. Test whether effector loss:
   - Blocks lysis in cells expressing GSDMD-N directly.
   - Blocks lysis after inflammatory caspase activation.
   - Prevents the membrane lesion in isolated membranes.
   - Restores lysis when the effector is re-expressed.

   Direct model predicts no blockade. Indirect model predicts blockade. Mixed model predicts partial blockade or delay.

6. **Isolated membrane bridge.** Prepare giant plasma membrane vesicles or inside-out membrane vesicles from wild-type and effector-null cells. Add purified GSDMD-N with or without cytosol.  
   - Direct model predicts permeabilization of protein-free or membrane-protein-containing vesicles without cytosol.  
   - Indirect model predicts permeabilization only when cytosol or the effector is added.  
   - This bridges the minimal reconstitution and whole-cell epistasis.

**Causal link:** Cellular validation tests necessity in the physiological context. If GSDMD-N kills effector-null cells as efficiently as wild-type cells, the effector is not required. If effector loss blocks death, GSDMD-N acts upstream of that effector.

---

### Stage 4 — Causal integration and decision rules

**Direct membrane action is supported if:**
1. Purified GSDMD-N permeabilizes protein-free liposomes across at least two orthogonal leakage assays.
2. Binding and oligomerization correlate with permeabilization.
3. Planar bilayers show discrete conductance steps or defined pores.
4. Full-length autoinhibited GSDMD does not permeabilize unless cleaved.
5. Directly expressed GSDMD-N kills effector-null cells.
6. Effector inhibitors or knockouts do not block GSDMD-N-induced lysis.
7. Pore-defective N mutants lose both in vitro permeabilization and cellular lysis.

**Indirect action via another effector is supported if:**
1. Purified GSDMD-N binds membranes but fails to permeabilize protein-free liposomes under all tested conditions.
2. Permeabilization requires cytosol, a membrane protein, or a purified candidate effector.
3. Effector activation precedes membrane permeabilization in cells.
4. Effector knockout or inhibition blocks lysis even when GSDMD-N is generated or directly expressed.
5. Effector re-expression restores lysis.

**Mixed mechanism is supported if:**
1. GSDMD-N directly permeabilizes liposomes, but cellular lysis is only partially blocked by effector removal.
2. Effector inhibition delays but does not prevent lysis.
3. Reconstitution requires non-physiological protein concentrations or specific lipids not present in the tested cells.

**Ambiguous outcomes:**  
If GSDMD-N permeabilizes only a narrow lipid composition, or only at concentrations far above cellular expression, or if effector inhibition gives inconsistent results across assays, the conclusion should remain “direct membrane interaction is possible but not established as the physiological mechanism.” Additional experiments should identify the missing cofactor, test physiological concentration ranges, and repeat in the relevant cell type.

---

## 4. Explicit alternative outcomes and conditional conclusions

### Outcome A — Positive direct mechanism
**Observations:** Purified GSDMD-N causes lipid-dependent leakage, binds and oligomerizes, forms conductance steps in planar bilayers, and kills effector-null cells. Full-length GSDMD is inactive until cleaved.  
**Conclusion:** The liberated N-terminal domain directly compromises membrane integrity. The other cellular effector is not required for the primary lesion.  
**Caveat:** Cellular lysis may still be amplified by downstream processes, but the primary membrane defect is intrinsic to GSDMD-N.

### Outcome B — Negative direct mechanism / indirect via effector
**Observations:** Purified GSDMD-N binds membranes but does not permeabilize protein-free liposomes. Permeabilization requires cytosol or a specific effector. Effector knockout blocks cellular lysis even when GSDMD-N is present.  
**Conclusion:** GSDMD-N is an upstream activator of another cellular effector that disrupts membranes.  
**Caveat:** The effector must be identified and validated by rescue.

### Outcome C — Mixed mechanism
**Observations:** GSDMD-N directly permeabilizes liposomes, but effector removal partially protects cells. Effector activation follows initial GSDMD-N binding.  
**Conclusion:** GSDMD-N forms a primary lesion, and full cellular lysis requires secondary effector-dependent amplification.  
**Caveat:** The relative contribution of direct and indirect arms is context-dependent.

### Outcome D — Ambiguous or non-physiological
**Observations:** Reconstitution requires non-physiological lipid or protein conditions; cellular results do not match in vitro results; effector inhibition gives inconsistent effects.  
**Conclusion:** Current evidence is insufficient to assign direct versus indirect action. The next step is to identify the missing cofactor or refine the reconstituted membrane composition to match the cellular membrane.

---

## 5. Causal interpretation connecting experiments to the question

- **Minimal reconstitution** asks whether GSDMD-N is sufficient for membrane damage without cellular effectors. Sufficiency supports direct action; failure points to a missing effector.
- **Orthogonal biophysics** asks whether the membrane damage has the signature of a proteinaceous pore: binding, oligomerization, discrete conductance, and size cutoff. This distinguishes direct pore formation from nonspecific lysis or enzymatic membrane disassembly.
- **Cellular validation** asks whether the same N-domain activity is necessary and sufficient in the physiological context. Direct expression of GSDMD-N bypasses upstream caspase activation and tests this cleanly.
- **Effector epistasis** asks whether any candidate downstream factor is required. If effector loss blocks lysis, GSDMD-N is upstream, not the direct executioner. If effector loss does not block lysis, the effector is dispensable for the primary lesion.
- **Order-of-events imaging** asks whether membrane permeabilization follows GSDMD-N recruitment directly or requires prior effector activation. Temporal order strengthens causal direction.
- **Rescue experiments** ask whether the effector is not only necessary but sufficient to restore the phenotype, which is required for a causal claim.

---

## 6. Missing numerical settings and parameters to fill before execution

The following are not specified in the evidence packet and must not be invented as historical facts:

- GSDMD species, isoform, exact domain boundaries, cleavage site, and the inflammatory caspase responsible.
- Cell type, culture conditions, inflammatory trigger, dose, and time course.
- Protein expression host, tag, purification protocol, final buffer, and concentration.
- Lipid compositions, molar ratios, liposome size, dye concentration, and leakage assay settings.
- Protein concentration ranges, incubation times, temperatures, pH, and ionic conditions.
- Transfection/transduction efficiency, expression levels, induction times, and selection.
- Inhibitor identities, concentrations, and specificity controls.
- Effector candidate identities; these must be discovered experimentally.
- Statistical thresholds, effect sizes, replicate numbers, blinding, and randomization.

**Recommended first action:** purify full-length GSDMD and its N-terminal domain, verify cleavage and purity, then run a pilot liposome leakage and binding assay across a small lipid panel. Use the pilot to set concentrations and effect sizes before scaling to orthogonal biophysics and cellular epistasis.
