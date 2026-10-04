# GPT-5.6 Sol / mol-r03

Original final answer, shared by both scoring rounds.

# Recommended next biological question

**Does the caspase-generated amino-terminal fragment of gasdermin D directly and sufficiently permeabilize protein-free lipid membranes, and—if it does—does it form stable pores or instead cause non-pore membrane disruption?**

This is the highest-value next question because it directly resolves the gap in the packet: cellular genetics and fragment expression identify the amino-terminal fragment as a candidate effector, but do not establish its physical action or exclude an additional cellular executor.

The decisive first experiment should therefore place rigorously purified gasdermin D products into defined, protein-free membranes and measure binding, permeability, membrane integrity, and channel formation. A cellular-cofactor search should be a conditional second branch, not the first experiment.

---

# 1. Reported evidence, inference, and current limit

## Reported evidence in the packet

1. **Inflammatory caspases cleave gasdermin D.**
2. **Genetic loss and fragment-expression experiments link this processing to pyroptotic death.**
3. **The amino-terminal portion has cytotoxic activity.**
4. **Those observations do not reveal the fragment’s physical action or whether another cellular component executes membrane injury.**
5. **No purified-protein membrane experiments are supplied.**

## Evidence-to-inference-to-conclusion chain

- Caspase cleavage plus cytotoxicity of the amino-terminal portion supports the inference that cleavage generates or releases a death-associated activity.
- Expression inside cells does not distinguish:
  - direct action of the fragment on membrane lipids;
  - activation of another membrane-damaging cellular component;
  - a requirement for a cellular cofactor, modification, or particular membrane composition.
- Therefore, the strongest current conclusion is only that **the amino-terminal fragment is genetically and functionally linked to pyroptotic death in cells**.
- It is **not yet justified** to conclude that the fragment is itself a pore-forming protein, a general membrane disruptor, or the sole executor of membrane injury.
- A purified, defined membrane-reconstitution experiment is the most direct way to distinguish these possibilities.

---

# 2. Competing mechanisms and discriminating predictions

## Mechanism A: Direct formation of stable membrane pores

The amino-terminal fragment binds lipids, oligomerizes in the bilayer, and creates aqueous transmembrane pores.

### Predictions

1. Purified amino-terminal fragment causes leakage from protein-free liposomes.
2. Activity tracks fragment concentration and membrane binding.
3. Full-length gasdermin D and the complementary carboxy-terminal fragment are substantially less active under matched conditions.
4. Membranes remain broadly intact at concentrations that permit solute passage.
5. Leakage is size selective, defining an effective pore-size range.
6. Planar bilayers show reproducible insertion events or stepwise, persistent conductance.
7. Membrane-associated fragment forms oligomeric structures; ring- or arc-like assemblies would further support this mechanism.
8. Activity may depend on lipid composition, but does not require another cellular protein.

## Mechanism B: Direct but non-pore membrane disruption

The amino-terminal fragment acts directly on membranes but causes thinning, fragmentation, rupture, or detergent-like destabilization rather than stable aqueous pores.

### Predictions

1. Purified fragment still causes leakage from protein-free liposomes.
2. Leakage is associated with vesicle collapse, membrane fragmentation, lipid solubilization, or loss of visible membrane boundaries.
3. Solutes of widely different sizes are released together rather than through a reproducible size cutoff.
4. Planar bilayers show catastrophic or irregular failure rather than stable unitary conductance events.
5. Stable pore-like oligomers are absent or not correlated with permeability.

This outcome would establish direct membrane injury but would not justify calling the fragment a pore-forming protein.

## Mechanism C: Indirect activation of a cellular membrane-injury factor

The amino-terminal fragment activates, recruits, or releases another protein or cellular component that executes membrane injury.

### Predictions

1. Correctly folded purified fragment binds weakly or not at all to protein-free membranes and does not produce reproducible permeability over a broad validated range.
2. Permeability is restored by a cellular fraction only when both fragment and fraction are present.
3. The cellular fraction alone is inactive or substantially less active.
4. Activity can be tracked during fractionation and ultimately reproduced with the fragment plus a purified cofactor.
5. The cofactor could be catalytic, structural, or required to place the fragment into an active conformation.

A negative purified-membrane result alone would not prove this mechanism because an incorrect fragment boundary, misfolding, missing modification, wrong lipid composition, or assay insensitivity could also explain the result.

## Mechanism D: Direct action requiring activation context

The fragment may be intrinsically membrane active but require native caspase cleavage, a transient cleavage complex, a modification, or a particular membrane composition.

### Predictions

1. A directly expressed amino-terminal fragment is inactive, while a fragment generated by purified caspase cleavage is active.
2. Activity appears only in particular defined lipid compositions.
3. Activity correlates with a particular molecular state of the fragment rather than with bulk fragment concentration.

This is an important alternative if different fragment-generation methods disagree.

---

# 3. Proposed research plan

Everything below is a **proposal**, not a report of completed experiments.

## Phase 0: Prerequisites and preregistration

### 0.1 Define the molecular species

The packet does not state the exact caspase cleavage position, fragment boundaries, sequence, molecular mass, tags, or purification conditions. These are unresolved prerequisites.

Before membrane testing:

1. Determine the exact termini of the caspase-generated products by analyzing purified full-length gasdermin D after cleavage with an inflammatory caspase.
2. Construct:
   - full-length gasdermin D;
   - the exact amino-terminal cleavage product;
   - the complementary carboxy-terminal product;
   - a cleavage-resistant full-length control, if the cleavage position can be altered without grossly disrupting protein structure.
3. Prepare both:
   - an independently expressed amino-terminal fragment; and
   - an amino-terminal fragment generated by cleavage of purified full-length protein.

Agreement between these two preparations would substantially reduce the risk that activity comes from an artificial terminus or a purification contaminant.

### 0.2 Predefine primary hypotheses and endpoints

The primary hypothesis should be:

> Purified amino-terminal gasdermin D causes concentration-dependent permeability of protein-free lipid vesicles beyond matched negative controls.

Primary endpoints:

- detergent-normalized leakage area under the time curve;
- initial leakage rate;
- endpoint leakage at a preregistered time.

Secondary endpoints:

- membrane binding;
- vesicle integrity;
- size selectivity;
- planar-bilayer conductance;
- membrane-associated oligomerization.

### 0.3 Define an operational effect threshold

Because the packet provides no expected potency or assay variance, a biologically grounded numerical threshold cannot be inferred.

A proposed auditable rule is to use the pilot only to estimate negative-control variability, then define the confirmatory minimal effect as:

> the larger of 10 percentage points of detergent-normalized release or three pooled standard deviations above matched negative controls.

This is an operational assay threshold, not a claim about the amount of leakage required for cell death. It must be locked before confirmatory sample identities are unblinded.

---

## Phase 1: Protein production and quality control

### 1.1 Independent preparations

Produce at least three independently expressed and purified lots of each principal protein species on different days:

- amino-terminal fragment;
- full-length protein;
- carboxy-terminal fragment.

Also prepare at least three independent cleavage reactions generating the amino-terminal fragment from full-length protein.

The independent unit is a separately expressed and purified protein lot, not an aliquot or assay well.

### 1.2 Matched handling

For all comparisons:

1. Exchange proteins into the same final buffer.
2. Match salt, pH, reducing conditions, glycerol or other additives, and residual tag-cleavage reagents.
3. Remove purification detergents because they could themselves permeabilize membranes.
4. Remove affinity tags where feasible, or test tagged and tag-free forms separately.
5. Include a buffer carried through the same purification workflow as a process blank.

### 1.3 Required protein quality checks

For every lot:

1. Confirm molecular identity and fragment termini.
2. Quantify purity and catalog detectable contaminants.
3. Measure concentration by a method not strongly affected by aggregation.
4. Assess monodispersity and soluble aggregation.
5. Confirm that the fragment remains soluble throughout the assay time and temperature.
6. Examine stability before and after membrane incubation.
7. For cleavage-generated material, document cleavage completeness and remove or separately control the caspase.

A nominally pure preparation is not sufficient by itself because a low-abundance membrane-active contaminant could create a strong signal. The two independent fragment-generation routes and activity co-fractionation with gasdermin D are therefore essential.

### 1.4 Protein-lot rejection rule

Do not interpret membrane activity from a lot that:

- visibly precipitates;
- contains uncontrolled detergent;
- shows substantial time-dependent aggregation before membrane addition;
- has uncertain identity or fragment boundary;
- differs materially in buffer composition from its controls.

If activity occurs only in aggregated preparations, classify it as ambiguous until aggregation can be separated from specific activity.

---

## Phase 2: Defined membrane systems and assay calibration

### 2.1 Lipid-composition panel

The physiological lipid target is not supplied. A single lipid composition could therefore produce a false negative.

Prepare a preregistered panel of defined large unilamellar vesicles including, at minimum:

1. predominantly zwitterionic phospholipid vesicles;
2. vesicles containing a defined fraction of negatively charged phospholipid;
3. the same compositions with and without cholesterol;
4. one broader mixed composition intended to approximate a cellular membrane while remaining protein free.

All identities and molar ratios must be recorded before testing. Conclusions should refer only to the tested compositions.

### 2.2 Independent membrane preparations

Prepare at least three independent liposome lots per key composition on separate days. Measure:

- lipid concentration;
- vesicle-size distribution;
- baseline leakage;
- encapsulation efficiency;
- stability during the complete assay interval.

A fresh extrusion from the same lipid stock is an independent liposome preparation; replicate wells from one extrusion are not.

### 2.3 Primary leakage assay

Encapsulate a self-quenched fluorophore or fluorophore–quencher pair inside vesicles and remove unencapsulated material.

For every well, collect:

1. baseline fluorescence before protein addition;
2. continuous fluorescence after protein addition;
3. maximum fluorescence after adding a membrane-solubilizing detergent at the end.

Normalize each time point:

\[
\text{fractional release} = \frac{F_t-F_0}{F_{\mathrm{detergent}}-F_0}.
\]

### 2.4 Calibration controls

Each plate or run should include:

- vesicles plus buffer: spontaneous-release control;
- detergent-treated vesicles: 100% release calibration;
- protein without vesicles: optical interference control;
- free fluorophore plus protein: fluorescence quenching or enhancement control;
- vesicles plus a matched inert protein: nonspecific protein-crowding control;
- purification-process blank;
- full-length gasdermin D;
- carboxy-terminal fragment;
- amino- plus carboxy-terminal fragments mixed at matched molar ratio.

The last mixture tests whether the complementary fragment suppresses or alters amino-terminal activity, but any interpretation as physiological inhibition would require additional evidence.

### 2.5 Run-acceptance criteria

Proposed technical criteria:

- untreated vesicles release less than 10% of detergent-normalized signal during the assay;
- detergent creates a clear dynamic range;
- technical duplicates differ by less than 15% of the relevant signal;
- protein does not independently alter the reporter enough to invalidate normalization;
- measured vesicle size remains within the preregistered preparation range.

Runs failing these criteria should be repeated with a new membrane preparation and should not be included selectively.

### 2.6 Orthogonal permeability reporter

Repeat key conditions with a chemically distinct encapsulated reporter. This controls for direct interaction between the fragment and the primary fluorophore.

---

## Phase 3: Pilot concentration and time-course study

Because potency is unknown, first perform a bounded pilot rather than choosing a single arbitrary concentration.

1. Test a logarithmically spaced series of amino-terminal fragment-to-lipid ratios.
2. Bound the upper range by protein solubility and absence of visible aggregation.
3. Use identical total protein concentrations in controls where possible.
4. Record continuous kinetics rather than only an endpoint.
5. Cross at least two independent protein lots with two independent liposome lots.

Use the pilot to:

- select the concentration range for confirmation;
- identify suitable observation times;
- estimate variance;
- determine whether one or more lipid compositions should be retained.

The pilot must not be used to claim definitive activity. Its parameters should be frozen before the confirmatory phase.

### Pilot stop rule

Stop concentration escalation if:

- protein precipitates;
- inert control protein also causes leakage;
- optical artifacts prevent reliable normalization;
- leakage occurs only after gross vesicle aggregation;
- the required concentration is physically incompatible with maintaining a bilayer assay.

Such findings indicate an uninterpretable range rather than evidence for direct pore formation.

---

## Phase 4: Confirmatory direct-sufficiency experiment

### 4.1 Design and independent units

Use three new independent protein lots crossed with three new independent liposome preparations for each retained key lipid composition. The full cross gives nine protein-lot/liposome-lot combinations.

For each combination, test:

- buffer;
- process blank;
- inert matched protein;
- amino-terminal fragment concentration series;
- full-length protein;
- carboxy-terminal fragment;
- amino- plus carboxy-terminal mixture;
- detergent calibration.

Technical duplicates or triplicates improve precision but are not counted as independent units.

### 4.2 Allocation and blinding

1. A person not conducting the assay assigns coded identities to protein treatments.
2. Randomize treatment positions while balancing treatments across plate rows and columns.
3. Keep the assay operator blinded to fragment identity.
4. Analyze fluorescence using a locked script before unblinding.
5. For imaging assays, use automated field selection or select fields while blinded.
6. Purification personnel cannot practically be blinded to constructs, but they should not make inclusion decisions after seeing membrane activity.

### 4.3 Primary success criterion

Direct membrane activity is supported if:

1. the amino-terminal fragment exceeds the preregistered effect threshold relative to buffer, process blank, inert protein, full-length protein, and carboxy-terminal fragment;
2. the effect is concentration dependent or reproducibly present at two adjacent concentrations;
3. it occurs across independent protein and liposome preparations;
4. it is reproduced by a second permeability reporter;
5. it is not explained by protein precipitation or reporter interference.

This would establish direct permeability in the tested defined membranes, but not yet a stable pore mechanism.

---

## Phase 5: Membrane binding and oligomerization

Perform these assays at concentrations spanning inactive to active leakage conditions.

### 5.1 Membrane binding

Use a flotation or equivalent separation assay to quantify membrane-associated versus soluble fragment.

Controls:

- each protein incubated without liposomes, to detect sedimenting aggregates;
- buffer and process blanks;
- full-length and carboxy-terminal proteins;
- liposome compositions that were active and inactive in leakage assays.

### Predictions

- Leakage without detectable binding would raise concern about assay artifact or transient binding below detection.
- Binding without leakage would indicate that membrane association alone is insufficient.
- Correlation of bound amino-terminal fragment with leakage supports a direct membrane mechanism but does not distinguish pores from rupture.

### 5.2 Oligomerization

Assess membrane-associated molecular assemblies using at least two approaches where feasible, such as:

- size analysis after membrane association;
- native electrophoretic analysis;
- controlled crosslinking;
- direct membrane imaging.

Crosslinking alone is insufficient because it can create artificial oligomers. Oligomer abundance should correlate with active membrane conditions.

---

## Phase 6: Distinguish stable pores from membrane destruction

### 6.1 Cargo-size selectivity

Prepare otherwise matched vesicles containing reporters of several hydrodynamic sizes.

Predictions:

- release of small reporters with retention of larger reporters supports size-limited pores;
- simultaneous release of all sizes, especially with vesicle destruction, supports rupture or solubilization;
- heterogeneous release could reflect heterogeneous pore sizes, mixed mechanisms, or vesicle variability.

Reporter loading and baseline stability must be calibrated separately for each size.

### 6.2 Giant-vesicle imaging

Add coded protein preparations to giant unilamellar vesicles containing:

- a membrane marker;
- an internal soluble marker;
- external fluorescent probes of different sizes.

Measure:

- fraction of vesicles becoming permeable;
- time to permeabilization;
- maintenance or loss of membrane boundary;
- changes in vesicle area and shape;
- rupture, fragmentation, or aggregation.

Interpretation:

- probe entry while the vesicle boundary remains intact supports pore-like permeability;
- sudden collapse or disappearance of the membrane supports non-pore disruption;
- events only at membrane-contact aggregates remain ambiguous.

### 6.3 Planar-bilayer electrophysiology

Form protein-free planar bilayers from the active lipid composition.

Calibration and acceptance:

- verify stable baseline conductance;
- record membrane capacitance and noise;
- reject bilayers that leak before protein addition;
- add matched buffer and control proteins in separate randomized recordings.

Add the amino-terminal fragment over the active concentration range and quantify:

- latency to first event;
- event frequency;
- conductance amplitude distribution;
- event duration;
- catastrophic bilayer failure.

Independent units are separately formed bilayers on different days using independent protein lots; multiple events in one bilayer are nested observations, not independent replicates.

### Pore decision rule

Use the term **stable pore-forming activity** only if direct permeability is accompanied by:

1. reproducible, persistent channel-like conductance events; and
2. at least one independent pore-consistent feature, such as size-selective passage with membrane retention or visible membrane-associated pore-like oligomers.

Leakage alone is not sufficient to call the structure a pore.

### 6.4 Vesicle integrity and lipid solubilization

Measure vesicle size, turbidity or scattering, recoverable lipid, and morphology before and after active treatment.

- Preserved vesicle structure with increased permeability favors pores.
- Loss of particles, broad fragmentation, or lipid solubilization favors non-pore disruption.
- Pore formation at low concentration and rupture at high concentration is possible; mechanism should therefore be assigned using the lowest clearly active range.

---

## Phase 7: Reconstitute caspase activation

This phase tests whether cleavage itself is sufficient to activate membrane injury.

Conditions:

1. full-length gasdermin D alone;
2. inflammatory caspase alone;
3. full-length gasdermin D plus active caspase;
4. full-length cleavage-resistant gasdermin D plus caspase;
5. pre-isolated amino-terminal fragment;
6. matched cleavage-reaction buffer;
7. inactive-caspase control if an appropriate inactive preparation is available.

Confirm cleavage in every reaction rather than assuming it occurred.

Test both:

- cleavage before exposure to liposomes, followed by caspase removal where feasible;
- cleavage in the presence of liposomes.

### Interpretation

- Leakage only when cleavage occurs, together with activity of the isolated native-boundary amino-terminal fragment, strongly supports cleavage-dependent direct activation.
- Leakage caused by caspase alone invalidates that run as evidence for gasdermin D activity.
- Activity of the cleavage mixture but not of isolated fragment could indicate fragment instability, a transient cleavage-dependent state, caspase contamination, or another reaction component; it is ambiguous until resolved.
- Failure of cleavage-resistant protein to become active is supportive but not decisive because the substitutions might alter folding.

---

## Phase 8: Conditional search for a cellular cofactor

Proceed here only after technically valid protein-free experiments fail or give weak, inconsistent activity.

### 8.1 Source selection

Ideally use cellular material from the biological context in which genetic loss and amino-terminal fragment expression produced the reported phenotype. The packet does not identify that system, so this is an unreported prerequisite.

If available, use cells lacking endogenous gasdermin D to prevent endogenous protein from confounding reconstitution.

### 8.2 Fraction-rescue assay

Separate cellular material into operational fractions, initially:

- soluble;
- membrane-associated;
- protein-enriched;
- lipid-enriched or protein-depleted.

Add each fraction to protein-free liposomes under four matched conditions:

1. fraction alone;
2. amino-terminal fragment alone;
3. fraction plus amino-terminal fragment;
4. fraction plus full-length or carboxy-terminal control.

Any fraction that damages liposomes by itself is not evidence for a fragment-specific cofactor unless the combined effect is demonstrably more than the independent activities and remains specific.

### 8.3 Determine the nature of the rescuing activity

For a rescuing fraction:

1. Test heat sensitivity.
2. Test protease sensitivity by treating the fraction before fragment addition and then removing or neutralizing the protease.
3. Test whether activity is retained in soluble or membrane material.
4. Fractionate by size, charge, and other orthogonal properties.
5. Track rescue activity rather than protein abundance.
6. Identify enriched candidate components.
7. Produce the candidate separately and reconstitute activity with purified amino-terminal fragment and synthetic membranes.

### Strong cofactor criterion

A cellular cofactor mechanism is strongly supported only when:

- fragment alone is inactive under validated conditions;
- cofactor alone is inactive or clearly insufficient;
- the combination is active;
- activity follows the candidate during fractionation;
- purified candidate plus purified fragment reproduces permeability.

Rescue by crude extract alone demonstrates only the existence of a rescuing activity, not its identity or whether it executes membrane injury directly.

---

# 4. Analysis plan

## Primary statistical model

Analyze each protein-lot/liposome-lot combination as an independent experimental unit. Use a hierarchical model with:

- fixed effects for protein treatment, concentration, lipid composition, and time;
- interactions between fragment treatment and lipid composition;
- random effects for protein lot, liposome lot, and experimental day.

Do not treat individual wells, vesicles, fluorescence time points, or channel events as independent biological replicates.

## Concentration-response analysis

Where the data support it, estimate:

- maximal leakage;
- concentration producing half-maximal activity;
- initial rate;
- concentration threshold;
- uncertainty intervals.

Do not force a sigmoidal model if a plateau is not reached or if aggregation dominates the upper range.

## Multiple endpoints

The confirmatory claim should rest on the preregistered primary leakage endpoint. Binding, imaging, size selectivity, conductance, and oligomerization determine the physical mechanism. Correct secondary comparisons or present confidence intervals without selectively emphasizing nominal significance.

## Reproducibility requirement

A mechanistic claim should not rest on one protein lot, one lipid lot, one reporter, or one high concentration. Lot-specific effects should be reported explicitly.

---

# 5. Stop rules and troubleshooting

## Stop or reject a run when

- baseline liposome leakage exceeds the preregistered limit;
- detergent calibration fails;
- protein visibly precipitates;
- control proteins or process blanks produce comparable leakage;
- reporter fluorescence is directly altered by the protein;
- bilayers are unstable before protein addition;
- sample identity, cleavage status, or concentration cannot be verified.

## Troubleshooting hierarchy

### If spontaneous liposome leakage is high

1. Confirm osmolarity and buffer matching.
2. Prepare fresh vesicles.
3. remeasure vesicle size.
4. lower assay temperature or duration only if changed for all groups and preregistered for the repeat.

### If the fragment aggregates

1. Test freshly purified material.
2. remove aggregates immediately before assay and document the procedure;
3. screen compatible salt, pH, and reducing conditions;
4. repeat with native caspase-generated fragment;
5. do not interpret aggregate-associated leakage as pore formation.

### If fluorescence suggests leakage but imaging does not

1. test direct fluorophore interaction;
2. repeat with a second reporter;
3. measure external free dye;
4. assess whether protein changes fluorescence without membrane passage.

### If binding occurs without leakage

Test:

- broader concentration range within solubility limits;
- alternative lipid compositions;
- native cleavage-generated fragment;
- whether a cellular fraction supplies a required activating factor.

The justified conclusion remains membrane association without demonstrated injury.

### If leakage occurs but planar bilayers show no channels

1. verify bilayer lipid composition matches active liposomes;
2. test lower and intermediate concentrations before catastrophic failure;
3. examine giant-vesicle rupture and lipid solubilization;
4. classify the result as direct membrane disruption unless stable pore evidence emerges.

### If only one lipid composition is active

Repeat that composition from independent lipid lots and systematically alter one lipid component at a time. Conclude lipid-dependent direct activity only for the tested compositions.

### If crude fractions rescue activity but also leak alone

Further fractionate or reduce fraction concentration. Do not call this cofactor dependence until fragment-specific enhancement can be separated from intrinsic fraction toxicity.

---

# 6. Conditional interpretation of outcomes

## Positive outcome 1: Direct permeability plus stable pore evidence

Observed pattern:

- amino-terminal fragment causes reproducible leakage from protein-free vesicles;
- controls are inactive;
- native cleavage-generated and independently expressed fragments agree;
- fragment binds and oligomerizes on membranes;
- membranes remain intact while selected solutes cross;
- planar bilayers show persistent conductance events.

### Strongest justified conclusion

**The caspase-generated amino-terminal gasdermin D fragment is sufficient to form permeabilizing pores in the tested lipid bilayers without another cellular protein.**

Limits:

- This does not prove that the same pore geometry or lipid dependence occurs in cells.
- It does not prove that no cellular regulator contributes in vivo.
- It does not establish that pore formation is the only cause of pyroptotic death.

## Positive outcome 2: Direct leakage with membrane destruction but no pore evidence

Observed pattern:

- purified fragment causes leakage;
- vesicles rupture, fragment, or solubilize;
- there are no stable channel events or reproducible size cutoff.

### Strongest justified conclusion

**The amino-terminal fragment is sufficient for direct membrane disruption under the tested conditions, but stable pore formation has not been demonstrated.**

Calling it a pore-forming protein would be unjustified.

## Positive outcome 3: Activity only after native caspase cleavage

### Conclusion

The direct activity depends on cleavage context or on a molecular state produced during cleavage. Further work must distinguish authentic fragment activation from caspase carryover, fragment instability, or a transient cleavage complex.

## Negative purified-membrane outcome with cofactor rescue

Observed pattern:

- validated purified fragment is inactive across tested lipid compositions;
- a cellular fraction restores fragment-specific activity;
- fraction alone is inactive;
- purified candidate plus fragment reproduces activity.

### Strongest justified conclusion

**The fragment requires the identified cofactor for membrane permeabilization in the defined reconstituted system.**

Additional evidence would still be needed to establish that the same factor executes membrane injury in intact cells.

## Negative outcome without cofactor rescue

### Conclusion

**No direct membrane activity was detected under the tested conditions.**

This does not establish an indirect mechanism. Remaining explanations include:

- incorrect fragment termini;
- misfolding;
- missing post-translational modification;
- insufficient concentration;
- untested lipid composition;
- missing cellular cofactor;
- insensitive assay.

The strongest current cellular conclusion would remain unchanged.

## Ambiguous outcomes

The following should not support a direct pore claim:

- activity only at the highest aggregating concentration;
- comparable leakage from carboxy-terminal, inert-protein, or process controls;
- activity from only one protein lot;
- leakage detected with one reporter but not an orthogonal reporter;
- binding or oligomerization without permeability;
- crude extract rescue without fragment specificity;
- conductance only as immediate bilayer rupture;
- leakage from cleavage reactions when caspase alone is also active.

---

# 7. Overall strongest conclusion justified by the packet

At present, the packet supports that inflammatory-caspase cleavage of gasdermin D and the amino-terminal fragment are linked to pyroptotic cell death. It does **not** establish the fragment’s physical mechanism or direct membrane sufficiency.

The most valuable next experiment is therefore a controlled purified-protein reconstitution in protein-free membranes, followed by orthogonal tests that distinguish stable pores from nonspecific membrane disruption. Only if those tests are convincingly negative should the investigation pivot to activity-guided identification of a required cellular cofactor.
