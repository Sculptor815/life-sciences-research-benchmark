# Qwen3.8 Max (0902) / mol-r01

Original final answer, shared by both scoring rounds.

## Recommended next action and decisive question

**Decisive follow-up question:**  
*Is the liberated amino-terminal domain of GSDMD itself sufficient to compromise a membrane, or does it kill by activating a separate cellular effector that executes membrane disruption?*

**Recommended study:** Begin with a **minimal reconstitution test** using purified cleaved GSDMD N-terminal domain and protein-free defined lipid membranes. If membrane permeabilization occurs there, direct membrane action is mechanistically viable. If it does not, use **cell-fraction add-back** to test whether a cellular component supplies the missing activity. Then perform **cellular validation** with GSDMD deficiency, reconstitution, cleavage-defective mutants, inducible N-domain expression, and separate measurements of cytokine processing versus cytokine release.

This design distinguishes:

1. **Direct membrane action:** cleaved GSDMD-N binds lipid, oligomerizes/inserts, and creates a permeability lesion without requiring another cellular protein.  
2. **Indirect effector activation:** cleaved GSDMD-N requires, activates, or unleashes another cellular molecule or process that disrupts the membrane.

No proposed result below is asserted as observed; all interpretations are conditional.

---

## 1. Unresolved biological question

The fixed evidence establishes that GSDMD is required for inflammatory-caspase-associated lytic death in the tested cells, that proteolytic cleavage separates an inhibitory arrangement into two domains, and that the liberated amino-terminal domain can induce death. However, the evidence does **not** establish whether the N-terminal domain is the terminal membrane-disrupting executioner or an upstream regulator of some other cellular membrane-damaging effector.

The unresolved question is therefore:

> Does cleaved GSDMD-N directly perturb lipid bilayers, or does it cause lytic death by engaging another cellular effector pathway?

---

## 2. Evidence-to-inference-to-conclusion chain

| Evidence item | Inference | What it does not prove | Consequence for study design |
|---|---|---|---|
| Genetic screen identifies GSDMD as necessary for inflammatory-caspase-associated lytic death in tested cells | GSDMD lies somewhere in a causal pathway leading to lytic death | Necessity does not show whether GSDMD is the terminal membrane-disrupting step | Need assays that separate GSDMD activation from membrane permeabilization |
| Proteolytic cleavage separates two domains; liberated N-terminal domain can induce death; intact protein is autoinhibited | Death is associated with release of an N-terminal lethal module from inhibition | Cellular sufficiency of the N domain does not prove direct lipid bilayer action | Use purified N domain in protein-free membranes and compare with full-length and C-terminal controls |
| Cytokine processing and cytokine release can be separated experimentally | The terminal membrane-permeability event can be measured independently of cytokine maturation | Does not identify the route of release | Cellular validation should measure intracellular cytokine processing and extracellular cytokine release separately |
| Supplied evidence does not determine the physical mechanism by which the active domain compromises membrane integrity | Direct pore/lesion formation and indirect effector activation remain viable alternatives | Cannot infer mechanism from genetics or cell-based N-domain expression alone | Minimal reconstitution plus orthogonal biophysical assays are required |

---

## 3. Competing mechanisms and distinct predictions

### Mechanism A: Direct membrane action by cleaved GSDMD-N

**Definition:** The liberated N-terminal domain itself physically compromises the bilayer. This could occur through a defined channel/pore, toroidal lipid lesion, detergent-like destabilization, or another direct lipid perturbation. The key point is that no distinct cellular protein is required as the membrane-disrupting agent.

Predictions:

- Purified cleaved GSDMD-N permeabilizes protein-free liposomes or planar bilayers of suitable lipid composition.
- Full-length intact GSDMD is inactive unless cleaved.
- The isolated C-terminal domain is inactive and may inhibit N-domain activity if co-supplied.
- Membrane binding, oligomerization, insertion, and conductance or dye release should correlate with permeabilization.
- Mutations that abolish reconstituted membrane permeabilization should reduce cellular lytic death and cytokine release, assuming the mutation does not disrupt folding or cleavage.

### Mechanism B: Activation of another cellular effector

**Definition:** Cleaved GSDMD-N does not itself form the membrane lesion. Instead, it activates, recruits, inhibits, or unleashes another cellular component, such as a separate membrane-disrupting protein, lipid-modifying enzyme, trafficking regulator, ion channel, cytoskeletal effector, or membrane-repair inhibitor.

Predictions:

- Purified cleaved GSDMD-N does not permeabilize protein-free liposomes under conditions where it remains folded and membrane-competent.
- Addition of a defined cellular fraction restores membrane permeabilization.
- The restoring activity may be sensitive to heat or protease if it is proteinaceous.
- Cellular lytic death may require a separable genetic or pharmacologic component downstream of GSDMD-N.
- Mutations that preserve cellular lethality but lack reconstituted liposome activity would weaken the direct-action model.

### Mechanism C: Hybrid or cofactor-dependent direct action

**Definition:** GSDMD-N directly contacts membrane but requires a specific lipid, lipid modification, post-translational modification, membrane curvature, ionic condition, or accessory factor to become membrane-disruptive. This is not identical to activation of a separate effector, but it is also not explained by the simplest protein-only pore model.

Predictions:

- GSDMD-N binds liposomes but fails to permeabilize them unless a specific lipid species, lipid metabolite, or cellular lipid extract is added.
- A cell fraction restores activity, but the active component may be lipid rather than protein.
- Cellular death may still be ultimately executed by GSDMD-N, but only in a membrane environment not captured by initial minimal liposomes.

---

## 4. Overall staged logic

The study is organized as a decision tree.

### Stage 1 — Minimal reconstitution

Ask whether purified cleaved GSDMD-N is sufficient to permeabilize protein-free membranes.

- If yes: direct membrane action becomes the leading mechanism.
- If no: proceed to fraction add-back before concluding indirect action, because missing lipid or environmental requirements could produce false-negative results.

### Stage 2 — Orthogonal biophysical measurements

If Stage 1 is positive, ask what kind of direct membrane lesion occurs.

- Discrete conductance events plus size-selective dye leakage support a defined pore/channel-like lesion.
- Catastrophic vesicle rupture, rapid loss of large dextrans, and gross morphological collapse support nonspecific membrane destabilization.
- Binding without leakage suggests that additional requirements are missing.

### Stage 3 — Cellular effector dependence

If Stage 1 is negative or ambiguous, ask whether a cellular component supplies the missing activity.

- Restoration by a protein-containing fraction suggests a protein effector or chaperone.
- Restoration by a lipid extract suggests a lipid cofactor or membrane-environment requirement.
- Restoration only by a combination suggests a lipid-modifying enzyme or regulated membrane state.

### Stage 4 — Cellular validation

Ask whether the biochemical activity identified in reconstitution is necessary and sufficient for the original cellular phenotype.

- Cleavage-defective GSDMD should fail to produce lytic death if cleavage is required.
- Inducible N-domain expression should bypass upstream inflammatory-caspase activation if the N domain is the lethal module.
- Mutants that lose reconstituted membrane activity but retain cellular lethality argue against direct membrane action as the sole mechanism.
- Mutants that retain reconstituted membrane activity but fail to kill cells argue that additional cellular context is required.

---

## 5. Proposed staged protocol

The following is a proposed experimental design. Missing numerical parameters are flagged rather than invented.

---

# Stage 0. Reagents and validation

## 0.1 Biological source

Use the same species, isoform, and cell type context as the original genetic screen where possible.

**Unreported parameter:** species, cell line, GSDMD isoform, and endogenous expression level are not specified in the evidence packet and must be confirmed.

## 0.2 Constructs

Generate expression constructs for:

1. Full-length GSDMD.  
2. Isolated N-terminal domain.  
3. Isolated C-terminal domain.  
4. Cleavage-defective full-length GSDMD.  
5. Optional: N domain plus C domain supplied as separate polypeptides.  
6. Optional: fluorescently tagged GSDMD-N, tested at both N and C termini if folding permits.

**Justification:** The evidence states that proteolytic cleavage separates two domains and that the intact protein is autoinhibited. Therefore, full-length, N-terminal, and C-terminal fragments are the minimal domain-based reagents required.

**Unreported parameter:** exact cleavage site boundaries are not specified. The N-domain boundary should be defined by sequencing or mass spectrometry of the cleaved product in the relevant system.

## 0.3 Cleavage strategy

Two acceptable approaches:

### Approach A: Use the relevant inflammatory caspase

If the relevant inflammatory caspase can be purified or supplied in active form, cleave full-length GSDMD under controlled conditions.

Controls:

- Mock-cleaved full-length GSDMD.
- Heat-inactivated caspase control.
- Caspase-only control added to liposomes to exclude protease-mediated membrane artifacts.

### Approach B: Engineered orthogonal protease site

If the exact inflammatory protease system is impractical, introduce an orthogonal protease recognition site at or near the physiological cleavage region.

Controls:

- Verify that cleavage yields an N-terminal fragment with the expected boundary.
- Test whether any extra residues alter activity.
- Include protease-only controls in membrane assays.

**Unreported parameters:** enzyme-to-substrate ratio, cleavage time, temperature, buffer composition, salt concentration, pH, and cleavage efficiency threshold are not specified and must be determined.

## 0.4 Protein quality control

Before membrane assays, validate:

- Purity by SDS-PAGE or equivalent.
- Identity by mass spectrometry or immunoblot.
- Cleavage status by SDS-PAGE or immunoblot.
- Monodispersity by size-exclusion chromatography or dynamic light scattering.
- Absence of contaminating proteases or lipases by functional controls.
- Low endotoxin if proteins will be added to live-cell assays.
- Folding or conformational integrity by a biophysical proxy such as thermal shift, circular dichroism, or comparative binding behavior.

**Assumption:** Recombinant GSDMD fragments can be produced in a folded, cleavable, and membrane-competent form. This must be validated.

---

# Stage 1. Minimal reconstitution: is GSDMD-N sufficient in protein-free membranes?

This is the decisive initial test.

## 1.1 Defined liposome leakage assay

### Rationale

If purified cleaved GSDMD-N permeabilizes protein-free liposomes, then membrane disruption can occur without another cellular effector. If it does not, direct action is not excluded, because the membrane composition or buffer may be inadequate.

### Liposome preparation

Prepare liposomes from defined synthetic lipids. Avoid undefined lipid mixtures or cell-derived vesicles in the primary sufficiency test, because those could introduce uncontrolled cofactors.

Suggested lipid conditions:

1. Neutral phosphatidylcholine-only membranes as a baseline.  
2. Phosphatidylcholine plus phosphatidylserine.  
3. Phosphatidylcholine plus phosphatidylinositol or phosphoinositides.  
4. Phosphatidylcholine plus phosphatidic acid or cardiolipin.  
5. Optional cholesterol-containing membranes.  
6. Native-cell lipid extracts only in secondary assays, not as the sole initial test.

**Justification:** The relevant lipid dependence is unknown. Many membrane-acting proteins require anionic lipids, specific headgroups, or membrane charge. Testing multiple defined compositions allows lipid dependence to be discovered without assuming the mechanism.

**Unreported parameters:** lipid molar ratios, vesicle size, extrusion pore size, total lipid concentration, buffer composition, pH, ionic strength, temperature, and protein-to-lipid ratios are not specified and must be determined by pilot titration.

### Encapsulated reporters

Use at least two classes of trapped reporters:

1. A small self-quenching fluorescent dye, for example a high-concentration calcein-like dye, whose fluorescence increases upon release.  
2. A panel of fluorescent dextrans or other inert probes of increasing molecular size.

**Purpose:** Small-dye release with retention of large dextrans would support size-limited permeability. Release of both small and large probes would support larger lesions, vesicle rupture, or catastrophic membrane failure.

**Unreported parameters:** exact dye identities, molecular weight cutoffs, loading concentrations, and external quenching strategy must be validated.

### Reaction setup

For each lipid condition, test:

1. Buffer-only negative control.  
2. Purified cleaved GSDMD-N.  
3. Uncleaved full-length GSDMD.  
4. Cleaved full-length GSDMD with C-terminal fragment still present.  
5. Isolated C-terminal domain.  
6. Heat-inactivated GSDMD-N.  
7. Detergent positive control for maximal dye release.  
8. Protease-only or mock-cleavage control where relevant.  
9. Osmotic protectants such as soluble polymers of defined size, if vesicle stability permits.

Measure fluorescence change over time and normalize to detergent-induced maximal release.

### Go/no-go interpretation

**Positive sufficiency signal:** Cleaved GSDMD-N causes reproducible dye release above controls in at least one defined lipid condition, while uncleaved full-length GSDMD and isolated C-terminal domain do not.

**Negative sufficiency signal:** Cleaved GSDMD-N fails to cause dye release despite evidence that it is folded, cleaved, and capable of lipid binding.

**Important caution:** A negative result here is not proof of indirect action. It may mean the membrane composition, protein state, ionic environment, or post-translational requirement is missing.

## 1.2 Giant unilamellar vesicle imaging

### Rationale

Bulk liposome leakage reports average permeability but cannot distinguish pore formation, vesicle rupture, membrane budding, fusion, or gross destabilization. Giant unilamellar vesicles allow direct visualization.

### Protocol outline

1. Form giant unilamellar vesicles from defined lipid mixtures.  
2. Include a small fraction of fluorescent lipid for membrane visualization.  
3. Encapsulate one soluble fluorescent reporter.  
4. Add a different-color extracellular reporter to detect influx.  
5. Add purified cleaved GSDMD-N, optionally sparsely labeled.  
6. Image by time-lapse confocal or TIRF microscopy.

Measure:

- Loss of encapsulated dye.
- Entry of extracellular dye.
- Timing relative to GSDMD-N binding.
- Vesicle shape changes, budding, shrinking, swelling, or rupture.
- Whether permeabilization is graded or abrupt.

**Unreported parameters:** GUV formation method, imaging frame rate, temperature, laser power, GSDMD-N concentration, and fluorophore labeling stoichiometry must be optimized.

## 1.3 Stage 1 causal interpretation

| Stage 1 outcome | Inference | Next step |
|---|---|---|
| GSDMD-N alone permeabilizes protein-free liposomes | Direct membrane action is sufficient under tested conditions | Proceed to Stage 2 to classify lesion type |
| GSDMD-N binds liposomes but does not permeabilize them | Binding is insufficient; missing cofactor, lipid, or effector may be required | Proceed to Stage 3 fraction add-back |
| GSDMD-N neither binds nor permeabilizes | Protein may be misfolded, wrong lipid environment missing, or direct action unlikely under tested conditions | Validate folding, expand lipid conditions, then Stage 3 |
| Uncleaved full-length GSDMD also permeabilizes | Autoinhibition may be lost in vitro or preparation artifact | Re-evaluate protein integrity and cleavage dependence |

---

# Stage 2. Orthogonal measurements of direct membrane action

If Stage 1 shows permeabilization, use orthogonal assays to determine whether the mechanism resembles a defined pore/channel, a toroidal or protein-lipid lesion, or nonspecific membrane disruption.

## 2.1 Planar lipid bilayer electrophysiology

### Rationale

Discrete ionic conductance events support formation of channel-like lesions. Large irreversible conductance increases or bilayer collapse support nonspecific destabilization.

### Protocol outline

1. Form planar lipid bilayers across an aperture using the lipid compositions identified in Stage 1.  
2. Add purified cleaved GSDMD-N to one compartment.  
3. Record ionic current under controlled voltage.  
4. Compare with uncleaved full-length GSDMD, isolated C domain, heat-inactivated GSDMD-N, and buffer-only controls.

Measure:

- Appearance of stepwise conductance events.
- Unit conductance levels, if present.
- Voltage dependence.
- Ion selectivity, if stable channels are observed.
- Latency from protein addition to event appearance.
- Irreversible bilayer rupture versus stable openings.

**Unreported parameters:** voltage protocol, salt composition, bilayer aperture size, lipid composition, protein concentration, and recording bandwidth must be determined.

### Causal role

If dye leakage, GUV permeabilization, and discrete conductance events all require GSDMD-N and correlate with oligomerization or insertion, the direct membrane-action model is strongly supported.

## 2.2 Lipid-binding assay

### Rationale

Direct action should usually involve membrane binding, although some detergent-like mechanisms could appear binding-independent in bulk assays.

### Protocol outline

Use liposome co-sedimentation, flotation, or a surface-binding assay.

1. Incubate cleaved GSDMD-N with liposomes of defined composition.  
2. Separate membrane-associated from soluble protein by ultracentrifugation.  
3. Quantify protein in pellet and supernatant.  
4. Compare full-length GSDMD, N domain, and C domain across lipid compositions.

Controls:

- Protein without liposomes to detect aggregation-driven pelleting.
- Heat-inactivated protein.
- Known membrane-binding positive control if available.

**Unreported parameters:** centrifugation speed, time, lipid concentration, protein concentration, and buffer conditions must be validated.

### Causal role

If N-domain binding correlates with permeabilization, direct membrane interaction is supported. If N domain binds but does not permeabilize, binding alone is insufficient, and a cofactor or effector may be needed.

## 2.3 Oligomerization assay

### Rationale

Many direct membrane pore mechanisms require oligomerization. However, oligomerization alone is not proof of pore formation.

### Protocol outline

Compare the oligomeric state of GSDMD-N under:

1. Soluble conditions.  
2. Liposome-bound conditions.  
3. Permeabilizing versus non-permeabilizing lipid compositions.

Methods may include:

- Chemical crosslinking followed by SDS-PAGE or immunoblot.
- Native PAGE.
- Size-exclusion chromatography with multi-angle light scattering.
- Single-particle imaging or electron microscopy where feasible.

**Unreported parameters:** crosslinker identity, concentration, reaction time, and detection thresholds must be optimized.

### Causal role

If mutations or conditions that prevent oligomerization also prevent permeabilization, oligomerization is causally implicated. If oligomers form without permeabilization, oligomerization is insufficient.

## 2.4 Membrane insertion assay

### Rationale

Direct pore-forming mechanisms often involve insertion of part of the protein into the bilayer. Peripheral membrane disruption may not.

### Protocol outline

1. Incubate GSDMD-N with liposomes.  
2. Treat with protease under conditions that digest exposed protein domains.  
3. Detect protected fragments by immunoblot or mass spectrometry.  
4. Use detergent to confirm access where appropriate.

Controls:

- Soluble GSDMD-N without liposomes should be fully digested.
- Liposome-protected soluble marker should remain protected if vesicles are intact.

**Unreported parameters:** protease type, concentration, digestion time, and epitope mapping strategy must be determined.

### Causal role

Protected fragments indicate that at least part of GSDMD-N enters or associates tightly with the bilayer. This strengthens direct membrane action but does not alone prove pore formation.

## 2.5 Structural visualization

If resources permit, use cryo-electron microscopy, atomic force microscopy, or negative-stain electron microscopy to inspect liposomes or bilayers after GSDMD-N addition.

Possible observations:

- Ring-like oligomers or pores: strong support for direct pore-like action.
- Irregular membrane deformation: direct but non-channel disruption.
- No visible structures despite leakage: lesion may be transient, small, or incompatible with imaging.

**Unreported parameters:** sample preparation, grid type, staining or freezing conditions, and imaging thresholds are not specified.

---

# Stage 3. Effector dependence and fraction add-back

This stage is especially important if Stage 1 is negative or ambiguous.

## 3.1 Cell fraction preparation

Prepare fractions from the same cell type used in the genetic screen, ideally from GSDMD-deficient cells to reduce background GSDMD.

Suggested fractions:

1. Cytosol.  
2. Peripheral membrane fraction.  
3. Integral membrane fraction.  
4. Detergent-soluble membrane fraction.  
5. Total lipid extract.  
6. Protein-free lipid fraction, if separable.  
7. Heat-inactivated or protease-treated versions of each fraction.

**Unreported parameters:** cell number, lysis method, centrifugation speeds, fraction normalization, and storage conditions must be determined.

## 3.2 Add-back matrix

Test liposome permeabilization in a matrix format:

| Condition | GSDMD-N | Cell fraction | Predicted interpretation if leakage appears |
|---|---|---|---|
| 1 | No | No | Baseline |
| 2 | Yes | No | Direct sufficiency if positive |
| 3 | No | Yes | Fraction alone has membrane activity; must subtract or control |
| 4 | Yes | Cytosol | Soluble effector/cofactor possible |
| 5 | Yes | Membrane fraction | Membrane-associated effector/cofactor possible |
| 6 | Yes | Lipid extract | Lipid cofactor possible |
| 7 | Yes | Heat-inactivated fraction | Protein effector likely if activity lost |
| 8 | Yes | Protease-treated fraction | Protein effector likely if activity lost |

## 3.3 Interpretation rules

### Protein effector supported

If permeabilization requires GSDMD-N plus a protein-containing fraction, and the activity is destroyed by heat or protease treatment, a proteinaceous cellular effector is implicated.

### Lipid cofactor supported

If permeabilization requires GSDMD-N plus a lipid extract or a specific lipid species, direct action with a lipid cofactor is implicated.

### Enzymatic effector supported

If a fraction only becomes active after ATP, ions, or incubation time, and the active lipid species appears over time, a lipid-modifying enzyme may be involved.

### No effector detected

If no fraction restores activity, the study remains inconclusive. Possible explanations include:

- Missing post-translational modification.
- Missing membrane geometry or tension.
- Missing organelle-specific environment.
- GSDMD-N instability.
- Effector destroyed during fractionation.
- Assay sensitivity too low.

## 3.4 Fractionation and identification

If a fraction restores activity, further purify the active component by biochemical fractionation, such as size-exclusion, ion-exchange, or lipid-class separation. Track activity at each step. Identify candidate components by mass spectrometry or lipidomics only after activity is reproducibly enriched.

**Important limitation:** The fixed evidence does not name a candidate effector. Therefore, this stage is discovery-oriented and should not assume a specific downstream molecule.

---

# Stage 4. Cellular validation

The cellular stage tests whether the biochemical mechanism identified in Stages 1–3 explains the original lytic-death phenotype and cytokine-release phenotype.

## 4.1 Cell models

Use:

1. Parental cells from the original tested system.  
2. GSDMD-deficient cells from the same background, if obtainable.  
3. Reconstitution lines expressing defined GSDMD variants.

Variants to compare:

- Empty vector.  
- Wild-type full-length GSDMD.  
- Cleavage-defective full-length GSDMD.  
- Inducible isolated N domain.  
- Inducible isolated C domain.  
- GSDMD mutants identified in reconstitution assays as defective for binding, oligomerization, insertion, or permeabilization, provided they fold properly.

**Unreported parameters:** expression levels, induction dose, time after induction, and cell density must be optimized. Expression should be quantified and, if possible, matched near endogenous levels.

## 4.2 Inflammatory-caspase activation

Activate the relevant inflammatory-caspase pathway using the stimulus appropriate to the tested cells.

**Unreported parameter:** the stimulus identity, dose, and timing are not specified in the evidence packet and must be determined from the original system.

Measure:

- Caspase activity using a fluorogenic or cleavage-based assay.  
- GSDMD cleavage by immunoblot.  
- Timing of membrane permeabilization relative to cleavage.

## 4.3 Lytic-death readouts

Use at least two independent measures of membrane compromise:

1. Uptake of a membrane-impermeant fluorescent dye.  
2. Release of a cytosolic enzyme or other lytic marker.  
3. Time-lapse morphology to detect swelling, blebbing, or rupture.

**Unreported parameters:** dye identity, concentration, imaging interval, and endpoint timing must be validated.

## 4.4 Cytokine processing versus release

Because the evidence states that cytokine processing and release can be separated experimentally, these must be measured separately.

### Cytokine processing

Measure intracellular maturation of the relevant cytokine by immunoblot, intracellular staining, or equivalent assay.

### Cytokine release

Measure extracellular cytokine in conditioned medium by ELISA or equivalent assay.

### Key comparisons

1. Stimulus that induces processing but not release.  
2. Stimulus that induces both processing and release.  
3. Inducible N-domain expression in cells with preformed processed cytokine.  
4. Conditions where membrane permeabilization is blocked or delayed.

This determines whether GSDMD-associated membrane permeabilization is sufficient for release of already processed cytokine, or whether release requires a separate event.

## 4.5 Acute N-domain activation in cells

To reduce dependence on upstream signaling, test acute N-domain activity.

Possible approaches:

1. Inducible expression of the isolated N domain.  
2. Delivery of purified cleaved GSDMD-N into GSDMD-deficient cells by electroporation or protein transduction.  
3. Rapid chemically induced cleavage system, if compatible with the native cleavage architecture.

Controls:

- Heat-inactivated GSDMD-N.  
- Isolated C domain.  
- Delivery reagent only.  
- Full-length uncleaved GSDMD where feasible.

Measure membrane dye uptake shortly after delivery or induction.

**Interpretation:** Rapid permeabilization after acute N-domain delivery supports direct or pre-existing-effector action. Delayed permeabilization, or dependence on new protein synthesis, would support a requirement for induced cellular processes. However, because an effector could be pre-existing, this cellular assay alone is not fully decisive; it must be interpreted with the reconstitution data.

**Unreported parameters:** delivery efficiency, protein dose, induction timing, and metabolic inhibitor toxicity must be validated.

## 4.6 Osmotic protection in cells

Add extracellular osmoprotectants of defined size, such as polyethylene glycols or dextrans, to determine whether they delay or prevent lytic death.

Interpretation:

- If larger osmoprotectants block lysis more effectively than smaller ones, this is consistent with a size-limited permeability lesion followed by osmotic swelling.  
- If no osmoprotectant affects death, the lesion may be very large, actively enzymatic, or not primarily osmotic.

**Unreported parameters:** polymer sizes, concentrations, osmolarity limits, and cell-type tolerance must be determined.

---

# 5. Conditional conclusions and alternative outcomes

## Outcome set A: Strong support for direct membrane action

### Expected pattern

- Purified cleaved GSDMD-N permeabilizes protein-free liposomes.
- Full-length uncleaved GSDMD does not.
- Isolated C domain does not.
- Heat-inactivated GSDMD-N does not.
- GUV imaging shows N-domain-dependent dye flux.
- Electrophysiology shows discrete conductance events or defined membrane lesions.
- Lipid binding, oligomerization, and insertion correlate with permeabilization.
- Mutations that abolish reconstituted permeabilization also reduce cellular lytic death and cytokine release without reducing inflammatory-caspase activation or cytokine processing.
- Inducible N domain bypasses upstream stimulus.

### Conclusion

Cleaved GSDMD-N is sufficient to compromise membranes in a minimal system and is causally linked to cellular lytic death. The simplest interpretation is that GSDMD-N is a direct membrane-disrupting executioner.

### Remaining limits

This does not exclude modulatory cellular factors. It also does not distinguish whether the terminal cellular rupture is caused solely by GSDMD-N lesions or by GSDMD-N-initiated osmotic consequences.

---

## Outcome set B: Support for activation of another cellular effector

### Expected pattern

- Purified cleaved GSDMD-N does not permeabilize protein-free liposomes.
- GSDMD-N is folded, cleaved, and capable of lipid binding or cellular lethality.
- Addition of a cell-derived protein fraction restores permeabilization.
- Restoring activity is lost after heat or protease treatment.
- Cellular lytic death requires an additional cellular component or is blocked by inhibiting that component.
- GSDMD-N mutants that cannot permeabilize liposomes nevertheless kill cells only when the putative effector pathway is intact.

### Conclusion

GSDMD-N is not the terminal membrane-disrupting agent under these conditions. It likely activates or requires another cellular effector.

### Required next step

Purify and identify the effector-containing fraction. Test candidate effectors genetically in GSDMD-dependent lytic death.

---

## Outcome set C: Direct action requiring a lipid cofactor

### Expected pattern

- GSDMD-N alone does not permeabilize initial defined liposomes.
- GSDMD-N binds membranes.
- A lipid extract or specific lipid species restores permeabilization.
- Heat-inactivated or protein-free lipid fractions remain active.
- Cellular death correlates with presence of the relevant lipid environment.

### Conclusion

GSDMD-N may directly compromise membranes, but only in a specific lipid environment. This is not evidence for a separate protein effector, but it does show that the minimal direct mechanism is more complex than protein plus generic bilayer.

### Required next step

Identify the lipid species or lipid modification required. Reconstitute with defined lipids and test cellular relevance.

---

## Outcome set D: Direct small-permeability lesion with secondary rupture

### Expected pattern

- GSDMD-N causes small-dye release but not large-dextran release in liposomes.
- Electrophysiology shows small conductance events.
- Cells show early dye uptake or cytokine release without immediate large-molecule release.
- Full lytic rupture requires additional osmotic swelling, membrane repair failure, or another amplification step.

### Conclusion

GSDMD-N may directly generate a small permeability lesion, but complete lytic death may involve secondary physical or cellular amplification.

### Required next step

Separate early permeabilization from terminal rupture using osmoprotectants, time-lapse imaging, and cytokine-release kinetics.

---

## Outcome set E: Inconclusive negative reconstitution

### Expected pattern

- GSDMD-N does not permeabilize any tested protein-free liposome.
- No cell fraction restores activity.
- Protein quality controls are ambiguous, or GSDMD-N fails to bind membranes.

### Conclusion

The data are insufficient to distinguish direct action from indirect action. A negative result cannot be treated as proof of an effector because the assay may lack required conditions.

### Required next step

Validate protein folding and cleavage, expand lipid compositions, test native membrane preparations, evaluate post-translational modifications, and consider that the active state may be transient or require membrane tension/organelle context.

---

## Outcome set F: Discordant cellular and reconstituted activity

### Pattern F1: Reconstitution-active mutants fail to kill cells

Interpretation: Direct membrane activity in vitro is not sufficient in cells. Cellular targeting, trafficking, regulation, or an effector may be required.

### Pattern F2: Reconstitution-inactive mutants still kill cells

Interpretation: The cellular lethal pathway does not require the reconstituted direct membrane activity. This strongly supports an alternative cellular effector or a missing in vitro requirement.

### Pattern F3: Full-length GSDMD kills without detectable cleavage

Interpretation: Either cleavage was undetected, or a cleavage-independent mechanism exists. This would require re-evaluation of the cleavage-dependence assumption.

---

# 6. Causal map connecting experiments to the question

| Experiment | What it tests | How it bears on direct versus indirect action |
|---|---|---|
| Purified GSDMD-N plus protein-free liposomes | Sufficiency of GSDMD-N for membrane permeabilization | Positive result shows no other cellular protein is required under those conditions |
| Full-length and C-domain controls | Autoinhibition and domain specificity | Confirms that activity maps to liberated N domain and is not a preparation artifact |
| GUV imaging | Morphology of permeabilization | Distinguishes discrete permeability from vesicle rupture or gross destabilization |
| Planar bilayer electrophysiology | Ionic conductance lesions | Discrete events support channel-like direct action; absence leaves mechanism open |
| Lipid binding | Membrane engagement | Binding without leakage indicates membrane contact is insufficient alone |
| Oligomerization and insertion | Assembly into membrane complex | Correlation with leakage supports direct pore/lesion assembly |
| Fraction add-back | Requirement for cellular component | Restoration by protein fraction supports indirect effector; restoration by lipid supports cofactor |
| GSDMD-deficient cellular reconstitution | Necessity and sufficiency in cells | Links biochemical activity to original genetic phenotype |
| Cleavage-defective mutant | Role of proteolytic activation | If inactive, cleavage is required; if active, cleavage-independent pathway may exist |
| Inducible N domain | Bypass of upstream inflammatory caspase | Tests whether N domain is the lethal module downstream of cleavage |
| Cytokine processing versus release assays | Separation of maturation from membrane release | Determines whether membrane permeabilization is the rate-limiting release step |
| Osmoprotectants | Osmotic nature of lysis | Supports or weakens pore/osmotic-swelling model |

---

# 7. Assumptions

The following assumptions are required and should be explicitly validated.

1. The GSDMD ortholog or isoform used in the screen can be faithfully represented by a recombinant protein.  
2. Proteolytic cleavage can be reproduced in vitro without altering the functional N-domain boundary.  
3. The N domain remains stable and fold-competent when isolated.  
4. Defined liposomes can approximate at least one relevant cellular membrane state.  
5. Cellular death readouts reliably reflect membrane compromise rather than upstream signaling toxicity.  
6. Cytokine processing and release can be measured with adequate temporal resolution.  
7. Genetic manipulation of the tested cells is feasible.  
8. Fractionation does not irreversibly destroy the relevant effector or lipid cofactor.

---

# 8. Missing numerical settings and parameters requiring validation

The following parameters are not supplied by the evidence packet and must not be invented.

1. Species and cell type.  
2. GSDMD sequence and isoform.  
3. Exact protease identity and cleavage site.  
4. Expression system and purification conditions.  
5. Protein concentration range for membrane assays.  
6. Lipid composition and molar ratios.  
7. Vesicle size and lipid concentration.  
8. Dye identities and molecular weight cutoffs.  
9. Electrophysiology voltage, salt, and buffer conditions.  
10. Centrifugation conditions for lipid-binding assays.  
11. Cell culture density and passage conditions.  
12. Inflammatory stimulus identity, dose, and duration.  
13. Cytokine assay reagents and dynamic range.  
14. Induction conditions for N-domain expression.  
15. Timepoints for cleavage, dye uptake, LDH release, and cytokine release.  
16. Statistical thresholds and biological replicate number.

---

# 9. Final conditional recommendation

The most decisive immediate experiment is:

> Test purified cleaved GSDMD-N in defined protein-free liposomes and planar bilayers, with full-length, C-terminal, heat-inactivated, and cleavage-defective controls.

If this assay is positive and cellular mutants with defective reconstituted activity lose lytic death, the direct membrane-action model is strongly favored.

If this assay is negative but cellular lethality persists, the study should shift to fraction add-back and effector identification.

If neither minimal reconstitution nor fraction add-back reveals activity, the mechanism remains unresolved, and the most honest conclusion is that the available evidence does not distinguish direct membrane action from indirect effector activation.
