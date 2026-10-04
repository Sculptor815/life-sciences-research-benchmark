# Kimi K3 / mol-r01

Original final answer, shared by both scoring rounds.

## Recommended decisive question and first action

**Mechanistically decisive question:**  
**Is the liberated GSDMD amino-terminal domain (GSDMD-NT) itself sufficient to bind and compromise a protein-free membrane under cell-matched conditions, or does it require a separable cellular effector to produce membrane permeabilization?**

**Recommended first experiment:** compare exact, purified GSDMD-NT and matched full-length GSDMD on protein-free liposomes made from lipids of the responsive cells, simultaneously measuring membrane binding and leakage. In parallel, test whether cytosol or native membrane fractions are required. This provides the cleanest initial separation between:

1. **Direct membrane action:** GSDMD-NT is the membrane-compromising agent, possibly requiring a particular lipid, membrane asymmetry, or recruiting cofactor.
2. **Indirect action:** GSDMD-NT activates another protein, channel, enzyme, or metabolite that subsequently compromises the membrane.
3. **Hybrid action:** GSDMD-NT directly creates an initial lesion that is amplified by a cellular effector.

No single assay is fully decisive. The decisive package must combine **minimal-system sufficiency**, **factor add-back/rescue**, and **cellular necessity measured at the earliest loss of membrane integrity**, rather than late viability alone.

---

# 1. Evidence-to-inference-to-conclusion chain

| Supplied evidence | Permitted inference | What it does not establish | Required next test |
|---|---|---|---|
| GSDMD is genetically necessary for inflammatory-caspase-associated lytic death | GSDMD lies on the causal pathway in the tested cells | It does not show that GSDMD physically damages the membrane | Measure the membrane-compromising activity of its active domain in defined systems |
| Cleavage separates two domains | Proteolysis changes domain interactions or accessibility | The exact cleavage boundary and mechanism of activation are not supplied | Map the boundary in the tested cells and compare exact fragments |
| Liberated GSDMD-NT can induce cell death | The amino-terminal domain contains an activity sufficient to initiate a death pathway when expressed or supplied in cells | Cellular death could still be indirect; gain-of-function expression can engage downstream effectors | Test purified GSDMD-NT on protein-free membranes and in factor-depletion/add-back systems |
| Intact GSDMD is autoinhibited | Full-length protein is a critical negative control; cleavage may relieve inhibition | It does not identify the target membrane or lesion type | Use matched full-length and cleavage-resistant constructs |
| Cytokine processing and release are experimentally separable | Cytokine maturation and membrane release are distinct events | Cytokine release cannot be used as a stand-alone proxy for membrane permeabilization | Measure cytokine processing, dye permeability, cytosolic-content release, and viability independently |
| Physical mechanism is unresolved | A pore, membrane rupture, lipid remodeling, or effector-mediated lesion should not be presupposed | The membrane target, stoichiometry, lipid requirement, and effector requirement are unknown | Use orthogonal binding, leakage, electrical, imaging, and genetic tests |

### Provisional causal models

```text
Inflammatory caspase activation
          ↓
GSDMD cleavage
          ↓
Liberated GSDMD-NT
          ├── Model A: directly binds/permeabilizes membrane
          │             ↓
          │       membrane permeability → lysis and release
          │
          └── Model B: activates cellular effector X
                        ↓
                  X compromises membrane
                        ↓
              permeability → lysis and release

Cytokine processing can occur in parallel and is not itself evidence
that membrane permeabilization has occurred.
```

---

# 2. Competing mechanisms and discriminating predictions

## Model A: Direct membrane action

**Operational definition:** intact GSDMD-NT must physically associate with the target membrane and be the polypeptide required to generate the measured membrane defect. This category includes direct action requiring a specific lipid or a protein that only recruits/orients GSDMD-NT.

**Predictions**

1. Purified GSDMD-NT binds protein-free membranes more strongly than matched full-length GSDMD.
2. GSDMD-NT, but not full-length protein, increases membrane permeability without cytosol, ATP-dependent metabolism, translation, secretion, or another cellular protein.
3. Permeability scales with membrane-bound GSDMD-NT.
4. Activity is reproduced after the active lipid requirement is reduced to a chemically defined composition.
5. Leakage, electrical permeability, and vesicle imaging give concordant results.
6. Depletion of a candidate cellular effector does not prevent the earliest membrane permeability after physiological GSDMD cleavage or calibrated GSDMD-NT expression.

## Model B: Activation of another cellular effector

**Operational definition:** GSDMD-NT initiates a downstream process in which a separable cellular protein, channel, enzyme, or metabolite executes membrane permeabilization.

**Predictions**

1. Purified GSDMD-NT alone does not permeabilize validated protein-free membranes, or does so only under conditions that do not match the cellular event.
2. A cytosolic or membrane-associated fraction restores permeabilization.
3. Activity can be fractionated and reconstituted with purified components.
4. If the effector is a protein, its activity should be reduced by proteolysis and should correlate with a specific fraction.
5. Genetic depletion of the effector blocks early membrane permeability, not merely later death, and re-expression rescues it.
6. Permeabilizing activity may persist after GSDMD-NT is removed if the downstream effector has already been activated.

## Model C: Hybrid mechanism

GSDMD-NT directly creates a limited membrane defect, while another cellular factor enlarges, stabilizes, repairs, or amplifies it.

**Predictions**

1. Protein-free membranes show partial or selective permeability.
2. A cellular fraction accelerates or expands the defect.
3. Effector depletion reduces but does not abolish early permeability, or changes lesion size and kinetics without eliminating initiation.

## Model D: Unresolved assay insufficiency

A negative minimal-system result may reflect missing lipid asymmetry, incorrect domain boundaries, protein aggregation, wrong ionic conditions, insufficient orientation, or an unknown membrane cofactor. Such a result is not, by itself, proof of an indirect mechanism.

---

# 3. Staged study

## Stage 0 — Establish exact reagents and quantitative boundaries

### 3.1 Map the active fragment

The evidence does not specify the exact cleavage boundary.

1. Trigger the same inflammatory-caspase-associated pathway used in the genetic screen.
2. Isolate endogenous GSDMD cleavage products.
3. Determine the amino-terminal fragment boundary by mass spectrometry or equivalent direct sequencing.
4. Generate:
   - native full-length GSDMD;
   - exact GSDMD-NT;
   - a cleavage-resistant full-length variant after the cleavage site is known;
   - the corresponding carboxy-terminal fragment, if useful as a specificity control;
   - a tagged variant only after demonstrating that the tag does not alter cleavage, localization, or death activity.

**Do not assume a historical cleavage-site sequence.** The packet does not provide it.

### 3.2 Purify structurally and functionally matched proteins

Use an expression host that yields soluble, correctly folded protein; the packet does not specify the best host.

For full-length protein, place the purification tag where cleavage releases an untagged amino-terminal domain. For standalone GSDMD-NT, use a removable solubility tag and remove it before functional assays.

Validate each preparation by:

- intact-mass measurement or mass spectrometry;
- SDS-PAGE and sensitive total-protein staining;
- size-exclusion chromatography coupled to multi-angle light scattering, or an equivalent aggregation assessment;
- absence of unplanned cleavage;
- comparison of at least two independent purification batches;
- mock-purified material from an empty-vector preparation;
- contamination testing appropriate to the cell system, particularly if the cells can respond to microbial products.

Avoid residual membrane-active detergent. If detergent is required for solubility, reduce or exchange it into assay buffer and include a mock-detergent control.

**Missing numerical settings:** optimum expression conditions, buffer pH, ionic strength, detergent concentration, storage temperature, and maximum freeze–thaw cycles are not supplied and must be determined empirically.

### 3.3 Estimate physiological abundance

Quantify endogenous GSDMD-NT generated after triggering by quantitative immunoblotting or targeted mass spectrometry using purified standards. Estimate total membrane lipid by lipid-phosphorus measurement or equivalent lipid quantification.

This permits in vitro protein-to-lipid ratios to be compared with the cellular ratio. A positive result obtained only at much higher ratios would be suggestive but not physiologically decisive.

---

## Stage 1 — Minimal reconstitution: purified GSDMD-NT plus protein-free membrane

### 3.4 Prepare protein-free membranes

Use two membrane classes.

#### A. Cell-derived, protein-free liposomes

1. Extract total lipids from responsive **GSDMD-null** cells. Using GSDMD-null cells reduces contamination by endogenous GSDMD fragments.
2. Remove aqueous contaminants and verify protein depletion by sensitive staining and, if feasible, mass spectrometry.
3. Dry lipids under inert gas.
4. Hydrate in an iso-osmotic, cytosol-like buffer.
5. Form large unilamellar vesicles by extrusion.

A provisional starting format is 100-nm-diameter vesicles, confirmed by dynamic light scattering or particle tracking. This is an operational starting point, not a packet-derived value.

#### B. Chemically defined liposomes

Because the required lipid composition is unknown, use a simple phosphatidylcholine-only bilayer as an initial baseline, then add individual lipid classes or lipid fractions identified from the responsive-cell extract.

Do not claim a particular lipid receptor before testing. If total-cell-lipid liposomes are active but simple synthetic liposomes are not, fractionate the extract and perform add-back to identify the required lipid class.

**Missing numerical settings:** cellular lipid composition, inner/outer leaflet asymmetry, exact buffer composition, and optimal lipid concentration are not supplied. These require lipidomics and pilot validation.

### 3.5 Encapsulated leakage assay

Prepare separate vesicle batches containing:

- a self-quenching small fluorescent dye;
- small labeled probes;
- larger labeled dextrans or other size-defined probes.

Provisional starting points:

- 50 mM carboxyfluorescein or an equivalent self-quenching dye;
- separate probes of approximately 3, 10, and 70 kDa for size discrimination;
- final liposome lipid in the tens-to-hundreds of micromolar range.

These values require validation for self-quenching, encapsulation efficiency, vesicle stability, osmotic balance, and probe–protein interactions.

Remove external probe by gel filtration or dialysis. Add:

1. buffer;
2. matched full-length GSDMD;
3. exact GSDMD-NT;
4. proteolyzed or otherwise inactivated GSDMD-NT;
5. mock purification eluate;
6. a validated membrane-disruption positive control, such as detergent, to define complete release.

Use at least four log-spaced protein-to-lipid ratios. A provisional search range is 0.001–10 mol% protein relative to lipid, subsequently narrowed around the measured cellular ratio. Record fluorescence continuously for at least 0–60 minutes at a validated temperature, with both room-temperature and physiological-temperature pilot runs.

Normalize leakage as:

\[
\%L(t)=100\times\frac{F_{\mathrm{sample}}(t)-F_{\mathrm{baseline}}}
{F_{\mathrm{complete\ lysis}}-F_{\mathrm{baseline}}}
\]

Measure both initial rate and area under the leakage curve.

### 3.6 Binding measurement

Measure membrane association by liposome flotation through a density gradient.

1. Incubate protein with liposomes.
2. Separate membrane-bound protein in floating liposome fractions from unbound protein in dense fractions.
3. Quantify GSDMD in each fraction by immunoblot, fluorescence, or mass spectrometry.
4. Include a no-liposome control to identify aggregation or precipitation.
5. Compare full-length GSDMD and GSDMD-NT at equal molar concentrations.

**Interpretation:** binding alone does not prove membrane damage. The decisive direct-action result is selective binding that quantitatively tracks with permeabilization.

### 3.7 Orthogonal measurement A: giant vesicle imaging

Form giant unilamellar vesicles from the same lipids and encapsulate a fluorescent probe.

- Add protein externally.
- Record lumen fluorescence, vesicle radius, membrane morphology, and rupture by time-lapse microscopy.
- Quantify the fraction losing probe, time to loss, and whether loss is complete, partial, or transient.

This distinguishes graded permeability from wholesale vesicle destruction. If the relevant physiological target is the cytosolic leaflet, generate asymmetric vesicles or otherwise recreate leaflet composition before interpreting a negative result.

### 3.8 Orthogonal measurement B: planar-bilayer electrophysiology

Form planar bilayers from the same lipid composition.

1. Verify bilayer stability and capacitance.
2. Add GSDMD-NT to one chamber and monitor current at fixed voltage.
3. Test both chamber orientations and several voltages.
4. Repeat with full-length and inactivated GSDMD-NT.

A provisional voltage series of ±10, ±50, and ±100 mV can be used, with exact settings optimized for bilayer stability. NT-dependent conductance would support direct membrane permeabilization. Lack of stable conductance would not exclude a transient or electrically silent lesion; therefore, interpret electrophysiology only together with leakage and imaging.

### 3.9 Minimal-reconstitution decision rules

**Supports direct sufficiency if:**

- GSDMD-NT permeabilizes protein-free membranes;
- full-length protein is inactive at matched concentration;
- activity is abolished by proteolysis or another validated loss-of-function treatment;
- binding and leakage correlate;
- concordant results are obtained by dye release, giant-vesicle imaging, and, where feasible, electrophysiology;
- the response occurs at a protein-to-lipid ratio compatible with measured cellular abundance;
- defined lipid add-back can reproduce activity after cell-derived lipid fractionation.

**Does not yet establish indirect action if:**

- GSDMD-NT binds but does not leak;
- only one readout is positive;
- total-cell-lipid liposomes respond but simple synthetic liposomes do not;
- all proteins appear active;
- positive activity occurs only at unmeasured or very high protein ratios.

---

## Stage 2 — Determine whether a cellular effector is required

## 3.10 Soluble-effector matrix

Prepare clarified cytosol from GSDMD-null responsive cells. Remove membranes by ultracentrifugation and verify the absence of membrane vesicles as far as technically possible.

Test protein-free liposomes under a full factorial design:

| Arm | GSDMD-NT | Cytosol | Purpose |
|---|---:|---:|---|
| 1 | − | − | Baseline |
| 2 | + | − | Direct sufficiency |
| 3 | − | + | Cytosol-alone artifact |
| 4 | + | + | Soluble cofactor requirement or amplification |
| 5 | + | dialyzed cytosol | Protein/macromolecule versus small-molecule contribution |
| 6 | + | protease-treated cytosol | Protein dependence |
| 7 | full-length | + | Cleavage specificity |

Add protease inhibitors after protease treatment to protect subsequently added GSDMD-NT.

### Interpretation

- **NT alone positive, cytosol unnecessary:** supports direct capacity.
- **NT plus native cytosol positive, NT alone negative:** indicates a missing soluble condition or factor, not yet its identity.
- **Dialyzed cytosol remains active but protease-treated cytosol does not:** supports a macromolecular, likely protein, effector.
- **Dialysis removes the activity but proteolysis does not:** suggests a metabolite, ion, or lipid-modifying activity; chemical fractionation is required.
- **Cytosol alone permeabilizes vesicles:** cytosol contains an independent membrane-active activity or vesicle contamination; the experiment is uninterpretable until corrected.

## 3.11 Membrane-resident-effector matrix

A soluble cytosol assay will miss integral membrane channels or membrane-bound enzymes.

Compare:

1. protein-free cell-lipid liposomes;
2. native plasma-membrane vesicles or giant plasma-membrane vesicles from GSDMD-null cells, washed to remove cytosol;
3. detergent-solubilized membrane fractions reconstituted into liposomes;
4. fractions enriched or depleted for candidate proteins.

If native membrane vesicles respond but protein-free liposomes do not, two possibilities remain:

- a missing lipid or leaflet asymmetry;
- a membrane-resident cofactor or downstream effector.

Resolve this by lipid add-back and membrane-protein fractionation.

## 3.12 Activity-guided fractionation and reconstitution

If cytosol or membrane extract is required:

1. Fractionate by size, charge, hydrophobicity, or other orthogonal properties.
2. Assay each fraction with GSDMD-NT and protein-free liposomes.
3. Identify proteins or metabolites enriched specifically in active fractions.
4. Test purified candidates alone and with GSDMD-NT.
5. Deplete the candidate from the active extract.
6. Rescue with purified candidate.
7. Repeat in candidate-null cells.

A factor that merely increases GSDMD-NT membrane recruitment should be classified as a **cofactor for direct action**. A factor that remains membrane-active after GSDMD-NT has been removed is stronger evidence for a **downstream executor**.

## 3.13 GSDMD-NT-removal experiment

For an apparently indirect activity:

1. Incubate GSDMD-NT with the candidate-containing fraction.
2. Remove GSDMD-NT using a validated specific binder or immunodepletion reagent.
3. Test whether the remaining fraction permeabilizes fresh liposomes.
4. Add purified GSDMD-NT back to confirm that removal was specific.

**Conditional interpretations**

- Activity remains after NT removal: supports activation of a persistent downstream effector.
- Activity disappears with NT removal: supports direct action, a required NT-containing complex, or nonspecific co-depletion.
- Candidate alone is active without NT: candidate may be a basal membrane-active protein rather than a GSDMD-dependent effector.

This test depends on the availability of a binder that does not itself inhibit membrane association.

---

## Stage 3 — Cellular validation using early membrane permeability, not late death alone

## 3.14 Genotypes

Use the same cell background as the genetic screen:

1. wild type;
2. GSDMD-null;
3. GSDMD-null rescued with full-length GSDMD;
4. GSDMD-null rescued with cleavage-resistant GSDMD after the cleavage site is mapped;
5. candidate-effector-null cells;
6. candidate-null cells with a rescue construct.

If endogenous tagging is required, validate that the tag does not alter cleavage, abundance, localization, or death.

## 3.15 Endogenous-pathway time course

Trigger the same inflammatory-caspase-associated pathway and collect densely spaced samples. The “early” time point should be defined empirically as the first reproducible increase in membrane permeability, not assigned a fixed minute.

Measure in parallel:

- full-length and cleaved GSDMD;
- GSDMD-NT abundance and localization;
- influx of a validated cell-impermeant dye;
- efflux of a preloaded intracellular probe;
- release of a stable cytosolic protein such as LDH, after validating it as a lysis marker in these cells;
- intracellular processed cytokine;
- extracellular processed cytokine;
- morphology and membrane rupture by live imaging;
- later viability.

This separation is essential because the supplied evidence establishes that cytokine processing and cytokine release can be uncoupled.

## 3.16 Calibrated GSDMD-NT expression

In GSDMD-null cells, use an inducible system to express:

- exact GSDMD-NT;
- full-length GSDMD;
- cleavage-resistant full-length GSDMD;
- an untransfected or empty-vector control.

Titrate expression to the amount of endogenous GSDMD-NT generated after pathway triggering. Excess expression can create artificial membrane damage or recruit low-affinity effectors.

Compare:

- time to dye influx;
- magnitude and size selectivity of release;
- localization;
- cytokine processing and release;
- later death.

## 3.17 Candidate-effector epistasis

For every candidate arising from Stage 2:

1. Delete or silence the candidate.
2. Trigger endogenous GSDMD cleavage.
3. Verify that GSDMD cleavage and GSDMD-NT abundance are unchanged.
4. Measure early membrane permeability.
5. Repeat with calibrated GSDMD-NT expression.
6. Restore the candidate by re-expression.

### Causal interpretation

- **Candidate depletion blocks early dye influx and is rescued by add-back:** candidate is a plausible obligatory downstream effector.
- **Candidate depletion blocks late death but not early permeability:** candidate acts downstream of membrane failure, possibly in repair, inflammation, or death execution.
- **Candidate depletion reduces GSDMD cleavage or NT abundance:** it is upstream of GSDMD activation, not necessarily the membrane executor.
- **Candidate depletion has no effect on early permeability:** supports direct GSDMD-NT action or redundancy among effectors.
- **Partial block:** supports a hybrid model, redundant effectors, or incomplete depletion.

## 3.18 Test cytokine as cargo rather than executor

Because cytokine processing and release are separable:

- quantify intracellular and extracellular processed cytokine independently;
- test whether blocking cytokine processing or depleting the relevant cytokine changes early membrane permeability;
- test purified processed cytokine on protein-free liposomes only if cytokine has been proposed as the effector;
- compare cytokine release with dye influx and cytosolic-protein release over time.

If processed cytokine accumulates without membrane permeability, cytokine maturation alone is not sufficient for release. If cytokine manipulation blocks release but not early permeability, the cytokine is downstream cargo rather than the membrane executor.

---

# 4. Conditional outcome matrix

| Outcome | Conditional conclusion | Main caveat |
|---|---|---|
| GSDMD-NT, but not full-length protein, binds and permeabilizes protein-free liposomes; defined lipids reproduce the effect; cellular factor depletion does not block early permeability | Strong support for direct membrane action sufficient under physiological conditions | Does not exclude additional amplification or repair pathways in cells |
| No protein-free permeabilization; cytosol restores activity; fractionation identifies one protein; knockout blocks early permeability; add-back rescues | Strong support for an indirect protein effector | Must show that the knockout does not reduce GSDMD cleavage or abundance |
| Protein-free liposomes inactive, but defined lipid add-back restores activity | Direct, lipid-dependent membrane action | A residual protein contaminant must be excluded |
| Protein-free liposomes inactive, but a membrane-protein fraction plus GSDMD-NT is active | Cofactor-dependent direct action or downstream membrane effector | NT-removal and activity-guided experiments are needed to classify the protein’s role |
| Protein-free leakage occurs, but cytosol accelerates it or increases cargo size | Hybrid direct initiation plus cellular amplification | Overexpression or cytosol-induced aggregation must be excluded |
| Binding without leakage | Nonproductive binding, missing condition, or indirect mechanism | Binding alone is not evidence of membrane damage |
| Dye leakage without giant-vesicle or electrical concordance | Probe artifact, vesicle destabilization, or nonconductive lesion | Repeat with independent probes and vesicle integrity assays |
| Full-length and NT both permeabilize membranes | Reagent aggregation, contamination, spontaneous cleavage, or failed autoinhibition | Do not interpret as physiological activity |
| No protein preparation is active, while positive-control membrane disruption works | Mechanism unresolved | Negative minimal reconstitution alone does not prove indirect action |
| Candidate knockout prevents death but not early permeability | Candidate acts downstream of membrane failure | Survival is not a valid readout of the initial lesion |
| Candidate knockout prevents NT-induced but not endogenous-cleavage-induced permeability | Construct-expression artifact or pathway branching | Match expression level and cleavage before interpreting |

---

# 5. Positive, negative, and ambiguous final conclusions

## Conditional positive conclusion: direct membrane action

A direct mechanism would be justified if all of the following occur:

1. Exact purified GSDMD-NT binds and permeabilizes protein-free membranes.
2. Matched full-length GSDMD is inactive.
3. The result is reproduced with independent protein and lipid preparations.
4. Binding, leakage, imaging, and electrical measurements are concordant.
5. Chemically defined lipids can replace the cell-derived lipid extract.
6. Activity occurs at a physiologically calibrated protein-to-lipid ratio.
7. Early cellular permeability persists when candidate cellular effectors are depleted, while GSDMD cleavage and NT abundance remain intact.
8. Cellular permeability has comparable timing and cargo-size behavior to the reconstituted event.

This would support the causal chain:

\[
\text{GSDMD cleavage}\rightarrow\text{GSDMD-NT membrane engagement}
\rightarrow\text{direct permeabilization}\rightarrow\text{lysis/release}.
\]

## Conditional positive conclusion: indirect effector

An indirect mechanism would be justified if:

1. GSDMD-NT alone fails under validated protein-free conditions;
2. a defined cytosolic or membrane fraction restores permeabilization;
3. the active factor can be depleted and reconstituted;
4. candidate-null cells lose early permeability despite normal GSDMD cleavage;
5. rescue restores early permeability;
6. downstream activity can be shown to persist after GSDMD-NT removal or otherwise function as the executor.

This would support:

\[
\text{GSDMD-NT}\rightarrow\text{effector activation}
\rightarrow\text{effector-mediated membrane failure}.
\]

## Conditional negative conclusion

A conclusion that GSDMD-NT is not directly membrane-active should not be made from a single negative liposome assay. It becomes defensible only after:

- the exact domain boundary is confirmed;
- protein quality and membrane binding are demonstrated;
- cell-derived and defined lipids are tested;
- missing lipid classes and membrane asymmetry are evaluated;
- soluble and membrane-associated fractions are tested;
- assay sensitivity is shown with positive controls;
- cellular abundance and protein-to-lipid ratios are matched.

## Ambiguous conclusions

The mechanism remains unresolved if:

- only membrane binding is observed;
- leakage occurs only at unphysiologically high concentrations;
- cell-derived lipid activity cannot be reduced to defined components;
- cellular factor depletion affects both cleavage and permeability;
- redundant effectors prevent single-knockout interpretation;
- direct reconstitution is positive but does not resemble cellular timing, localization, or cargo selectivity.

---

# 6. Controls, replication, and analysis

- Use at least three independent biological preparations for protein, lipids, and cell experiments; determine the final sample size by pilot variance.
- Randomize plate positions and blind image quantification where feasible.
- Include buffer, full-length protein, mock purification, no-liposome, liposome-only, and complete-lysis controls in every run.
- Use independent protein batches to exclude preparation-specific contaminants.
- Report dose–response curves, initial rates, time to half-maximal leakage, area under the curve, and confidence intervals.
- Predefine whether the primary cellular endpoint is dye influx, preloaded-probe efflux, or cytosolic-enzyme release; use the others as orthogonal endpoints.
- Use mixed-effects models or another design-appropriate method that accounts for batch and replicate. Apply multiplicity correction when screening fractions or candidates.

---

# 7. Missing parameters requiring validation

The supplied evidence does not specify the following, and none should be filled in from presumed historical precedent:

- exact cell type, species, and inflammatory trigger;
- exact cleavage site and GSDMD-NT boundaries;
- endogenous abundance of cleaved GSDMD-NT;
- physiological membrane target and leaflet orientation;
- cellular lipid composition and asymmetry;
- optimal buffer pH, ionic composition, and temperature;
- active protein oligomeric state;
- required protein-to-lipid ratio;
- probe concentrations and cargo-size thresholds;
- electrophysiological voltage and recording conditions;
- identity of any downstream effector;
- availability of validated antibodies, binders, and tagged constructs.

---

## Bottom line

The most informative path is to test **exact purified GSDMD-NT on protein-free, cell-derived liposomes**, using full-length GSDMD as the matched negative control and binding, leakage, imaging, and electrophysiology as orthogonal measurements. If activity requires cytosol or a membrane fraction, identify the factor by activity-guided fractionation, depletion, and add-back, then test whether it is necessary for the **earliest cellular membrane permeability**. Only concordance across minimal reconstitution and calibrated cellular genetics can decisively distinguish direct membrane action, activation of another effector, and a hybrid mechanism.
