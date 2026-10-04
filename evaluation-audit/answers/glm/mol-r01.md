# GLM 5.3 FlashX / mol-r01

Original final answer, shared by both scoring rounds.

## Bottom line

The decisive follow-up question is:

**Is cleaved GSDMD amino-terminal domain sufficient by itself to permeabilize a defined lipid bilayer, or does it require another cellular effector to produce membrane lysis?**

A staged study should begin with a **minimal reconstitution** using purified GSDMD fragments and artificial membranes. If the liberated amino-terminal domain causes bilayer permeabilization in the absence of all cellular proteins, that supports **direct membrane action**. If it fails to do so but gains activity only when a cell-derived lipid, protein fraction, or candidate effector is added, that supports **effector-mediated membrane compromise**. Because a negative reconstitution result alone is not decisive, the study should also include orthogonal lesion assays and cellular rescue/validation in the screened cell system.

---

## 1. Evidence-to-inference-to-conclusion chain

### Supplied evidence

1. **GSDMD is required** for inflammatory-caspase-associated lytic death in the tested cells.  
   - Inference: GSDMD acts downstream of or parallel to inflammatory caspase activation, but necessity alone does not prove that GSDMD directly disrupts membranes.

2. **Proteolytic cleavage separates two domains.**  
   - Inference: cleavage likely removes an autoinhibitory constraint.

3. **The liberated amino-terminal domain can induce cell death, whereas intact GSDMD is autoinhibited.**  
   - Inference: the amino-terminal fragment is the likely execution module. However, the evidence does not show whether it kills by directly damaging membranes or by activating another cellular effector.

4. **Cytokine processing and cytokine release can be experimentally separated.**  
   - Inference: cytokine release should not be used as a proxy for lytic membrane damage. Caspase activity/cytokine processing and plasma-membrane rupture need independent readouts.

5. **The physical mechanism by which the active domain compromises membrane integrity is not determined.**  
   - Conclusion: the decisive question is whether the amino-terminal domain is itself a membrane-disrupting entity or whether it recruits/activates another effector.

---

## 2. Competing mechanisms and distinct predictions

### Mechanism A: Direct membrane action

**Model:** After cleavage, the GSDMD amino-terminal domain directly binds membranes and compromises lipid-bilayer integrity, potentially by forming aqueous pores, disrupting lipid packing, causing membrane thinning, destabilization, or rupture.

**Predictions:**

- Purified amino-terminal domain should be sufficient to permeabilize artificial liposomes or planar bilayers without any cellular protein.
- Activity should be lipid-dependent and dose-dependent.
- Orthogonal assays should show evidence of membrane lesions or conductance events, not merely bulk nonspecific precipitation.
- Full-length GSDMD and the isolated carboxy-terminal domain should show little or no activity under comparable conditions.
- Mutations that disrupt amino-terminal membrane binding or membrane-disrupting activity in vitro should reduce cellular lytic death without necessarily blocking upstream cytokine processing.

### Mechanism B: Activation of another cellular effector

**Model:** The amino-terminal domain is necessary but not sufficient; it localizes to membranes or activates another cellular protein, lipid domain, organelle pathway, ion channel, transporter, or membrane-remodeling system that causes lysis.

**Predictions:**

- Purified amino-terminal domain alone will not permeabilize minimal artificial membranes.
- Activity will appear only after addition of a cell-derived protein fraction, membrane fraction, or defined cofactor.
- Removal, inhibition, or genetic depletion of the required effector will prevent lysis despite normal GSDMD cleavage and possibly normal cytokine processing.
- Mutations that preserve GSDMD cleavage but prevent effector activation will block lytic death.

### Mechanism C: Indirect or artifact-associated membrane damage

This is a control category rather than a preferred biological mechanism.

**Model:** The amino-terminal fragment appears active because of aggregation, contaminating protease, endotoxin, detergent carryover, or nonphysiological overexpression.

**Predictions:**

- Activity will correlate with impurity, aggregation, storage-buffer conditions, or contaminating enzymatic activity.
- Highly purified, monodisperse amino-terminal domain may lose activity.
- Cellular death will correlate with expression artifacts rather than endogenous cleavage.

---

## 3. Overall study design

The study should be staged so that each step has a clear causal interpretation.

### Stage 1: Minimal reconstitution with purified components

Purpose: test whether the liberated amino-terminal domain is sufficient to compromise a defined membrane.

### Stage 2: Orthogonal biochemical and structural measurements

Purpose: determine whether any leakage reflects true bilayer lesion formation rather than aggregation, fusion, detergent-like nonspecific disruption, or assay artifact.

### Stage 3: Cofactor add-back reconstitution

Purpose: distinguish direct membrane-lipid action from dependence on a missing lipid, protein, metabolite, or cellular effector.

### Stage 4: Cellular validation in the GSDMD-dependent lytic-death system

Purpose: test whether the biochemical activity identified in reconstitution is required for lytic death in the original biological context.

---

## 4. Stage 1: Minimal reconstitution protocol

### 4.1 Reagents

Use purified proteins:

1. Full-length GSDMD.
2. Liberated amino-terminal domain.
3. Isolated carboxy-terminal domain.
4. Optionally, amino-terminal plus carboxy-terminal domain mixed after purification.
5. Cleavage-resistant full-length GSDMD, if the cleavage site can be specifically mutated.
6. Mutant amino-terminal domains selected after a pilot membrane-binding/oligomerization analysis.

Because the supplied evidence does not specify exact domain boundaries, cleavage-site residue numbers, or known functional motifs, these must be empirically mapped from the observed cleavage products. Do not assume residue numbers not present in the evidence packet.

### 4.2 Protein quality control

Before membrane assays:

- Confirm purity by SDS-PAGE and, if available, mass spectrometry.
- Confirm expected size and identity of the amino-terminal domain.
- Remove affinity tags if they could alter membrane binding.
- Assess aggregation by size-exclusion chromatography or dynamic light scattering.
- Include buffer-only controls matched to the protein storage buffer.
- Remove or control for contaminating protease, nucleic acid, lipid, detergent, and endotoxin, especially before later cellular experiments.

Operational caution: exact purification stringency, tag location, buffer composition, and endotoxin-removal thresholds are not specified by the supplied evidence and should be validated empirically.

### 4.3 Lipid vesicles

Prepare defined large unilamellar vesicles containing encapsulated soluble fluorescent reporters.

Recommended minimal vesicle panel:

1. **Neutral bilayer control**  
   - Example: phosphatidylcholine-only or phosphatidylcholine plus cholesterol.  
   - Purpose: test whether anionic lipids are required.

2. **Anionic bilayer panel**  
   - Phosphatidylcholine plus phosphatidylserine.
   - Phosphatidylcholine plus phosphatidylinositol or polyphosphoinositides.
   - Other anionic lipid mixtures relevant to cytosolic membrane leaflets.

3. **Cell-derived total lipid liposomes**  
   - Lipids extracted from the tested cell type.  
   - Purpose: determine whether the native lipid mixture is required.

The exact lipid compositions and mol percentages are not provided in the evidence packet. A practical pilot should test a matrix of neutral, mildly anionic, strongly anionic, and cell-extract-derived membranes.

### 4.4 Encapsulated reporters

Use at least two reporters with different size or charge properties:

1. **Small soluble fluorophore leakage assay**  
   - Example: self-quenched calcein or a comparable fluorophore/quencher system.  
   - Purpose: detect permeabilization to small solutes.

2. **Larger encapsulated macromolecule assay**  
   - Example: fluorescent dextrans of several defined sizes.  
   - Purpose: infer size selectivity.

3. **Membrane-label assay**  
   - Include a lipid fluorophore in the bilayer.  
   - Purpose: distinguish leakage from vesicle rupture, aggregation, fusion, or precipitation.

Exact dye concentration, dextran sizes, lipid concentration, and protein-to-lipid ratios are not specified by the evidence and should be established by pilot titration.

### 4.5 Reaction design

For each lipid composition, test:

- Buffer only: zero-leakage baseline.
- Detergent-treated vesicles: maximal release control.
- Full-length GSDMD.
- Amino-terminal domain.
- Carboxy-terminal domain alone.
- Amino-terminal plus carboxy-terminal domain mixed after purification.
- Heat-denatured amino-terminal domain.
- Protease-only or cleavage-reaction control, if cleavage is performed in vitro.
- Protein storage buffer matched to each condition.

Measure:

- Time course of fluorescence increase.
- Endpoint leakage.
- Dose dependence.
- Lipid-composition dependence.
- Reversibility or irreversibility.
- Vesicle integrity by light scattering or single-vesicle imaging.

### 4.6 Justified controls

Essential controls:

- The amino-terminal domain must be compared with full-length GSDMD because the evidence states that intact GSDMD is autoinhibited.
- The carboxy-terminal domain alone tests whether the inhibitory domain nonspecifically damages membranes.
- Denatured amino-terminal domain tests whether activity requires folded protein.
- Detergent treatment establishes the dynamic range for complete leakage.
- Buffer-only controls establish spontaneous leakage.
- Protein-storage buffer controls distinguish buffer effects from protein effects.
- Cell-extract lipid vesicles test whether native lipid composition, rather than a protein cofactor, is required.

---

## 5. Stage 2: Orthogonal measurements of membrane damage

A positive leakage assay alone is not sufficient to conclude direct membrane action. Use at least two additional, mechanistically different assays.

### 5.1 Single-vesicle microscopy

Encapsulate fluorescent soluble dye in individual vesicles labeled with a membrane dye. Add purified amino-terminal domain and monitor individual vesicles.

Interpretation:

- **Direct pore-like permeabilization:** individual vesicles lose soluble dye while retaining membrane continuity for a period, or show discrete leakage events without wholesale destruction.
- **Complete rupture:** vesicle membrane signal disappears rapidly.
- **Aggregation/fusion:** vesicles cluster or mix membrane labels.
- **Precipitation:** fluorescence concentrates in debris or large objects.

This measurement helps separate true permeabilization from gross vesicle destruction.

### 5.2 Planar lipid bilayer conductance

Reconstitute purified amino-terminal domain into a planar lipid bilayer and record ionic current.

Interpretation:

- **Direct membrane lesion:** discrete conductance steps or fluctuating current events appear after addition of the amino-terminal domain.
- **No direct lesion:** no conductance change despite possible leakage in vesicle assays.
- **Nonspecific disruption:** large unstable current bursts, baseline collapse, or bilayer breakage without reproducible unitary events.

Important caution: planar bilayer composition must be matched to the lipid compositions that showed activity in the liposome assay. Missing numerical settings include voltage protocol, salt concentration, lipid composition, protein concentration, and filtering parameters.

### 5.3 Structural imaging of membrane lesions

After incubation with vesicles, image membranes by cryo-electron microscopy, negative-stain electron microscopy, or atomic-force microscopy if available.

Interpretation:

- Observation of discrete ring-like, arc-like, or otherwise defined lesions supports a direct structural membrane-perturbing mechanism.
- Absence of visible lesions does not exclude direct destabilization, because some disruption mechanisms may not form stable structures detectable by a given imaging method.
- Imaging controls must include vesicles alone, full-length GSDMD, carboxy-terminal domain, and denatured amino-terminal domain.

### 5.4 Size-selectivity analysis

Compare release of encapsulated molecules of different sizes.

Interpretation:

- A defined size cutoff supports a structured aqueous lesion.
- indiscriminate release of all contents with rapid vesicle collapse suggests catastrophic rupture or nonspecific destabilization.
- No release of large dextrans but release of small dyes suggests smaller aqueous lesions.

### 5.5 Lipid-binding and oligomerization measurements

Measure amino-terminal-domain association with vesicles using flotation, sedimentation, fluorescence correlation, or surface-based binding assays.

Also assess oligomerization by native gel, crosslinking, size-exclusion chromatography, or single-molecule imaging.

Interpretation:

- Direct membrane action should correlate with membrane binding and, if the mechanism is pore-like, with membrane-associated oligomerization.
- Membrane binding without leakage suggests localization alone is insufficient.
- Leakage without detectable binding would raise concern for nonspecific aggregation or indirect effects.

---

## 6. Stage 3: Cofactor add-back and effector search

If purified amino-terminal domain does not permeabilize minimal membranes, the next question is whether it needs a lipid cofactor or a cellular effector.

### 6.1 Lipid add-back

Test liposomes made from:

- Total lipid extracts of the tested cell type.
- Organelle-enriched lipid mixtures, if biologically justified by cellular localization data.
- Individual lipid classes added to neutral bilayers.

Interpretation:

- If cell-derived lipid vesicles become sensitive to the amino-terminal domain while simple synthetic vesicles are not, the mechanism may still be **direct membrane action**, but requiring a specific lipid environment.
- If no lipid composition supports activity, a protein or metabolite cofactor becomes more likely.

### 6.2 Soluble-cellular-fraction add-back

Prepare separated soluble and membrane fractions from the tested cells under conditions that preserve protein activity.

Add:

- Amino-terminal domain alone.
- Soluble fraction alone.
- Membrane fraction alone.
- Amino-terminal domain plus soluble fraction.
- Amino-terminal domain plus membrane fraction.
- Heat-treated or protease-treated fractions as controls.

Interpretation:

- If soluble fraction plus amino-terminal domain confers vesicle leakage, a soluble protein or metabolite effector is implicated.
- If membrane fraction plus amino-terminal domain confers leakage, a membrane-associated effector or membrane lipid/protein context is implicated.
- If heat or protease treatment of the active fraction removes activity, a protein effector is likely.
- If activity survives protease treatment but not lipid extraction, a lipid cofactor is likely.

Exact lysis conditions, fractionation buffers, and salt/detergent conditions are not specified in the evidence and must be optimized.

### 6.3 Biochemical fractionation and identification

If a cellular fraction restores membrane activity:

1. Fractionate the active extract chromatographically.
2. Track activity using the same vesicle-leakage assay.
3. Test heat sensitivity, protease sensitivity, nuclease sensitivity, and small-molecule dependence.
4. Identify active protein candidates by mass spectrometry if protease-sensitive activity is found.
5. Reconstitute purified candidate effector with purified amino-terminal domain and vesicles.

Causal interpretation:

- A purified effector that enables amino-terminal-domain-dependent permeabilization would identify the missing cellular component.
- Depletion or mutation of that candidate should reduce cellular lytic death despite normal GSDMD cleavage.

### 6.4 Genetic validation of a candidate effector

If a candidate cellular effector emerges, generate loss-of-function cells using the screen-compatible genetic system.

Compare:

- Control cells.
- GSDMD-deficient cells.
- Effector-deficient cells.
- Double-deficient cells.
- Cells reconstituted with wild-type effector.
- Cells reconstituted with effector mutants lacking interaction with GSDMD amino-terminal domain.

Measure GSDMD cleavage, caspase activity, cytokine processing, and lytic death separately.

Interpretation:

- If effector loss blocks lysis but not GSDMD cleavage or cytokine processing, the effector acts downstream of GSDMD activation.
- If effector loss blocks GSDMD cleavage too, it acts upstream and is not a selective lytic effector.
- Rescue with wild-type but not mutant effector strengthens causality.

---

## 7. Stage 4: Cellular validation in the original lytic-death system

### 7.1 Cell models

Use the cell type in which the genetic screen identified GSDMD as necessary.

Generate:

1. Parental cells.
2. GSDMD-deficient cells.
3. GSDMD-deficient cells reconstituted with wild-type full-length GSDMD.
4. GSDMD-deficient cells reconstituted with cleavage-resistant GSDMD, if the cleavage site can be specifically altered.
5. GSDMD-deficient cells expressing only the carboxy-terminal domain.
6. GSDMD-deficient cells inducibly expressing the amino-terminal domain.
7. GSDMD mutants identified from the reconstitution assay as defective in membrane binding, oligomerization, or permeabilization.

Expression should ideally be near endogenous. Strong overexpression of the amino-terminal domain may create artifacts and should be interpreted cautiously.

### 7.2 Activation of the inflammatory-caspase pathway

Use the same inflammatory-caspase stimulus and cellular context as the original screen.

The specific stimulus, dose, timing, caspase identity, and expression level are not specified in the supplied evidence. These must be empirically set to achieve detectable GSDMD cleavage with minimal nonspecific toxicity.

### 7.3 Independent cellular readouts

Measure at least four processes separately.

#### A. GSDMD cleavage

Use immunoblotting or quantitative proteomics to confirm that full-length GSDMD is cleaved in the relevant conditions.

Interpretation:

- Cleavage confirms that the active domain is liberated.
- Failure of a mutant to be cleaved would make it uninterpretable for downstream membrane action.

#### B. Caspase activation and cytokine processing

Measure active inflammatory caspase and processed cytokine species.

Interpretation:

- The evidence states that cytokine processing and release can be separated. Therefore, cytokine processing is an upstream or parallel readout, not a proxy for lytic death.
- A mutant that preserves cytokine processing but blocks lysis would specifically implicate GSDMD membrane action downstream of cytokine maturation.

#### C. Plasma-membrane lysis

Use live-cell membrane-integrity dyes, extracellular LDH release, or real-time swelling/rupture imaging.

Interpretation:

- Loss of lytic death despite preserved caspase activation and cytokine processing supports a specific defect in GSDMD-mediated membrane compromise.

#### D. Cytokine release

Measure released mature cytokines separately from intracellular cytokine processing.

Interpretation:

- If cytokines are processed but not released when membrane lysis is blocked, this supports separation between cytokine maturation and lytic membrane damage.
- Do not infer membrane rupture from cytokine release alone.

### 7.4 Cellular conductance or ion-flux readouts

If reconstitution suggests pore-like or channel-like activity, test cells expressing wild-type or mutant GSDMD for early changes in membrane conductance, cation influx, or membrane depolarization before overt lysis.

Interpretation:

- Early conductance changes that correlate with amino-terminal-domain appearance and are lost in membrane-action-defective mutants support direct cellular membrane permeabilization.
- Absence of early conductance changes despite lysis would suggest a distinct lytic mechanism.

### 7.5 Imaging cellular localization

Tag full-length GSDMD or the amino-terminal domain with a minimally perturbing fluorescent tag.

Validate that the tag does not block cleavage or activity.

Interpretation:

- Direct membrane action predicts enrichment of active amino-terminal signal at membranes before rupture.
- Effector-mediated action may also show membrane recruitment, so localization alone is not decisive.
- Localization is useful mainly when compared with biochemical and mutant data.

---

## 8. Mutant strategy linking reconstitution to cells

A decisive causal link requires variants whose behavior differs in the minimal reconstitution and whose cellular phenotype can be compared.

### Proposed approach

After Stage 1 and Stage 2 identify conditions under which the amino-terminal domain binds or disrupts membranes, generate a panel of amino-terminal-domain mutants. Because the evidence packet does not specify functional residues, do not assume specific residue numbers. Use:

1. Deletion mapping.
2. Charge-reversal mutants in basic surface patches, if membrane binding suggests electrostatic lipid interaction.
3. Alanine or conservative-mutation scans of conserved exposed regions.
4. Mutations that reduce oligomerization if oligomerization correlates with leakage.
5. Mutations that preserve folding but impair membrane binding.

Each mutant should be tested for:

- Protein expression and stability.
- Cleavage, if expressed as full-length GSDMD.
- Vesicle binding.
- Vesicle leakage.
- Conductance activity, if applicable.
- Cellular lytic death.
- Caspase activation.
- Cytokine processing.

### Causal interpretation

- A mutant defective in liposome permeabilization and cellular lysis, but normal in expression and cleavage, supports the conclusion that the in vitro membrane activity is biologically relevant.
- A mutant defective in liposome permeabilization but still able to mediate cellular lysis would argue that the original reconstitution did not capture the true mechanism.
- A mutant defective in cellular lysis but normal in liposome permeabilization would suggest missing cellular regulation, localization, or timing.

---

## 9. Conditional outcomes

### Outcome 1: Positive direct-action result

**Observed pattern, if it occurs:**

- Purified amino-terminal domain permeabilizes defined liposomes.
- Full-length GSDMD and carboxy-terminal domain do not.
- Leakage is dose- and lipid-dependent.
- Orthogonal assays show discrete lesions, conductance steps, or size-selective permeabilization.
- Mutants defective in reconstitution activity are also defective in cellular lysis.
- Cellular caspase activation and cytokine processing remain intact in the lysis-defective mutants.

**Causal conclusion supported:**

The cleaved amino-terminal domain is sufficient to compromise membranes directly. Its membrane action is the likely execution mechanism for lytic death.

**Limits:**

- Direct activity in artificial membranes does not exclude that cellular effectors amplify, regulate, or spatially localize the process.
- Reconstitution may exaggerate activity if protein-to-lipid ratios are nonphysiological.
- Cellular validation is still needed to connect the biochemical mechanism to native lysis.

### Outcome 2: Negative minimal-reconstitution result but rescue by cell-derived component

**Observed pattern, if it occurs:**

- Purified amino-terminal domain does not permeabilize minimal synthetic membranes.
- It also does not produce conductance events or visible lesions.
- Addition of soluble or membrane cellular fraction restores leakage.
- Activity is heat- or protease-sensitive.
- Fractionation identifies a candidate protein effector.
- Genetic loss of that effector blocks cellular lysis despite GSDMD cleavage and cytokine processing.

**Causal conclusion supported:**

GSDMD amino-terminal domain is necessary for triggering lysis but is not sufficient by itself. It likely activates or requires another cellular effector to compromise membranes.

**Limits:**

- Failure to reconstitute with synthetic membranes does not rule out direct membrane action if the correct lipid composition, membrane asymmetry, curvature, tension, or post-translational modification is missing.
- Fractionation can damage or remove required cofactors.
- Loss of effector function may indirectly alter cell state rather than specifically remove the lytic effector.

### Outcome 3: Lipid-dependent direct action

**Observed pattern, if it occurs:**

- Simple neutral liposomes are resistant.
- A specific anionic lipid class or total cell-lipid mixture confers susceptibility.
- No protein cofactor is needed.
- Activity tracks lipid composition, not heat-sensitive cell proteins.
- Cellular GSDMD mutants defective in binding that lipid class fail to mediate lysis.

**Causal conclusion supported:**

GSDMD may act directly on membranes, but only in a specific lipid context. This remains a direct membrane mechanism rather than protein-effector activation.

**Limits:**

- Total lipid extracts can obscure the identity of the required lipid.
- Individual lipid add-back may not reproduce native membrane asymmetry.
- Cellular lipid composition may change during inflammatory activation.

### Outcome 4: Ambiguous result

Examples:

- Purified amino-terminal domain causes leakage only at very high protein concentrations.
- Leakage occurs without detectable lesions, conductance, size selectivity, or membrane binding.
- Activity correlates with aggregation.
- Mutants defective in liposome leakage do not correlate with cellular lysis.
- Cellular death is altered by expression level or tag position but not reproducibly by GSDMD cleavage status.

**Causal conclusion:**

The reconstitution assay is not yet decisive. Additional purification, lower expression, alternative lipid systems, asymmetric vesicles, cellular membrane preparations, or unbiased effector search are needed.

**Recommended next action:**

Do not overinterpret leakage alone. Establish a reproducible assay window, remove aggregation, test membrane compositions that better resemble the native target membrane, and couple the assay to cellular mutants.

---

## 10. Alternative interpretations and how the design handles them

### Alternative 1: Apparent membrane activity is due to contamination

Handled by:

- High-purity protein preparation.
- Buffer-matched controls.
- Denatured-protein controls.
- Protease-free cleavage controls.
- Aggregation assays.
- Independent preparations of protein.
- Endotoxin removal before cellular experiments.

### Alternative 2: Reconstitution lacks native membrane properties

Handled by:

- Testing multiple lipid compositions.
- Testing total cell-lipid liposomes.
- Testing curvature, charge, cholesterol, and membrane-tension variants.
- Using both vesicles and planar bilayers.
- Considering asymmetric vesicles if lipid orientation is important.

### Alternative 3: The amino-terminal domain localizes to membranes but does not rupture them directly

Handled by:

- Separating membrane binding from permeabilization.
- Using size-selective leakage.
- Conductance assays.
- Structural lesion imaging.
- Mutants that bind membranes but fail to leak vesicles.

### Alternative 4: Another cellular effector is required

Handled by:

- Fraction add-back.
- Heat/protease sensitivity.
- Biochemical purification of the cofactor.
- Genetic depletion of candidate effectors.
- Cellular rescue with wild-type and mutant effector.

### Alternative 5: Cytokine processing confounds interpretation

Handled by:

- Measuring cytokine processing, cytokine release, and lytic death separately.
- Using the supplied fact that cytokine processing and release can be experimentally separated.
- Identifying mutants or conditions that preserve cytokine processing but block lysis.

---

## 11. Key missing numerical settings

The evidence packet does not specify many operational parameters. These should be empirically validated rather than assumed:

- Exact GSDMD domain boundaries and cleavage-site sequence context.
- Identity of the inflammatory caspase and activating stimulus in the tested cells.
- Cell type-specific stimulus dose and time course.
- Endogenous GSDMD expression level.
- Correct amino-terminal-domain expression level for cellular assays.
- Optimal protein-to-lipid ratio for reconstitution.
- Physiologically relevant lipid composition of the target membrane.
- Required membrane curvature or tension.
- Buffer ionic strength, pH, divalent cations, and reducing conditions.
- Dye and dextran sizes/concentrations for size-selectivity assays.
- Planar bilayer voltage, salt conditions, and filtering settings.
- Whether native membrane asymmetry or post-translational modification is required.

These missing settings are not fatal, but they define the validation work needed before the study can be interpreted conclusively.

---

## 12. Recommended first experiment

The single most decisive first experiment is:

**Purified amino-terminal GSDMD versus purified full-length GSDMD, added to defined fluorescently loaded liposomes under at least three lipid conditions, followed by orthogonal confirmation with single-vesicle imaging and planar-bilayer conductance or structural lesion imaging.**

A positive result would establish sufficiency for direct membrane action in a defined system. A negative result would motivate lipid add-back and cellular-fraction add-back to determine whether the missing component is a lipid cofactor or a cellular effector.
