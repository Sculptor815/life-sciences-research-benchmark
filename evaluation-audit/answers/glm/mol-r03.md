# GLM 5.3 FlashX / mol-r03

Original final answer, shared by both scoring rounds.

# Recommended Next Question and Research Plan

## 1. Lead recommendation (the most valuable next biological question)

**Does the caspase-generated amino-terminal fragment of gasdermin D (GSDMD-N) directly and autonomously disrupt lipid bilayers by forming discrete pores, or does it require one or more additional cellular cofactors to execute membrane injury?**

This is the single highest-value question because the supplied evidence establishes only *correlation and sufficiency in cells* (genetic loss and fragment expression link GSDMD processing to pyroptosis), not the *physical mechanism*. Resolving it determines whether GSDMD-N is itself the membrane-effector molecule or merely an upstream recruiter/trigger — a distinction that changes every downstream experimental and therapeutic strategy in the field.

---

## 2. Evidence-to-inference-to-conclusion chain

**Reported evidence (from packet only):**
- E1: Inflammatory caspases cleave gasdermin D.
- E2: Genetic loss and fragment-expression experiments link this cleavage to pyroptotic death.
- E3: The amino-terminal portion carries cytotoxic activity.
- E4: The packet explicitly notes that these observations do not reveal the physical action of the fragment, and that **no subsequent purified-protein membrane experiments are supplied**.

**Permissible inferences:**
- I1: The N-terminal fragment is *necessary in the cellular context* (loss-of-function) and *sufficient for killing when expressed in cells* (fragment expression). (From E1–E3.)
- I2: Cytotoxicity measured in cells is an endpoint that cannot distinguish direct membrane action from recruitment of an endogenous effector, or from an indirect physiological trigger of lysis. (From I1 plus E4.)

**Conclusion warranted by the packet (and no further):**
- C1: GSDMD processing is functionally required for pyroptosis, and the N-terminal fragment is the cytotoxic species — but the packet is *silent* on whether GSDMD-N physically acts on membranes itself, acts through a cofactor, or triggers death indirectly. This gap is the defined unresolved question.

**Explicit limit:** Nothing in the packet demonstrates membrane binding, oligomerization, pore structures, lipid specificity, or any purified-protein activity. All such claims below are **proposals**, not reported results.

---

## 3. Competing mechanisms and discriminating predictions

### Mechanism A — Direct autonomous pore formation (GSDMD-N is the effector)
Caspase cleavage releases the N-terminal fragment from autoinhibition by the C-terminal fragment; the free fragment binds inner-leaflet membrane lipids, oligomerizes, and forms a discrete aqueous pore. Osmotic influx through pores causes swelling and lysis.

**Predictions:**
- A1: Purified GSDMD-N alone (no cytosol) renders defined synthetic liposomes leaky in a protein-dose- and time-dependent manner.
- A2: Oligomeric ring/slab structures of reproducible diameter are visible on liposomes by electron microscopy or atomic force microscopy.
- A3: Leakage shows a defined size cutoff (graded fluorescent dextrans of increasing hydrodynamic radius), consistent with pores of a characteristic diameter; small osmoprotectants block cell swelling, large ones do not.
- A4: Full-length GSDMD is inactive on liposomes unless cleaved by caspase *in the reaction* — establishing cleavage as the activation event at the membrane.
- A5: Activity depends on liposome lipid composition in a systematic, saturable way.

### Mechanism B — Cofactor-dependent membrane injury (GSDMD-N recruits/activates a host effector)
GSDMD-N binds membranes or a cytosolic partner and recruits/activates an endogenous membrane-disrupting protein; GSDMD-N is a targeting/triggering subunit, not the effector.

**Predictions:**
- B1: Purified GSDMD-N alone does not permeabilize defined liposomes; permeabilization requires addition of cytosolic extract (or a specific fraction of it).
- B2: The cofactor activity is heat-labile and protease-sensitive (proteinaceous).
- B3: Depletion of the cofactor from cells (genetic or immunodepletion) abrogates pyroptosis despite normal GSDMD cleavage.
- B4: Cofactor dependence is lost if a defined purified protein is reconstituted with GSDMD-N on liposomes.

### Mechanism C — Indirect physiological trigger (no direct membrane contact)
GSDMD-N triggers death through metabolism, signaling, or organelle stress; membrane rupture is a secondary consequence.

**Predictions:**
- C1: Neither purified GSDMD-N nor GSDMD-N plus extract permeabilizes liposomes.
- C2: Cellular death depends on ongoing metabolism/energy, transcription, or an intact signaling pathway; a cell-free membrane system is refractory by design.
- C3: Membrane injury markers (ion flux, dye entry) appear only late, after metabolic collapse.

**Key discriminating experiment logic:** A cell-free, chemically defined liposome system with purified components is the minimal setting that cleanly separates A from B and C, because it removes all cellular physiology. If the fragment is active there, Mechanism A is supported. If activity appears only with extract, B is supported. If never, C (or a technical failure — see troubleshooting) is implicated.

A secondary axis discriminates **discrete pores vs. detergent-like lytic activity** (a refinement within A): graded-size dextran protection and pore-imaging distinguish a defined pore architecture from nonspecific surfactant disruption.

---

## 4. Proposed research plan (detailed, ordered, auditable)

> **All steps below are proposals. No results exist in the supplied packet for any of them. Reagents, constructs, and conditions listed are assumptions to be verified experimentally.**

### Phase 0 — Prerequisites and assumptions to verify

| Item | Status | Action |
|---|---|---|
| Clones encoding full-length GSDMD, GSDMD-N (amino-terminal portion), GSDMD-C | Not supplied | Assume generation or acquisition; verify sequences |
| Purified inflammatory caspase with confirmed activity on GSDMD | Not supplied | Procure/produce; verify cleavage by SDS-PAGE/immunoblot before any membrane experiment |
| Purification/presentation system for GSDMD-N | Not reported by original authors | **Assumption:** soluble expression or refolding from inclusion bodies with endotoxin-free preparation; verify monodispersity by SEC and dynamic light scattering (DLS). Endotoxin removal is mandatory — contaminating LPS would confound every membrane assay. |
| Defined lipid mixtures mimicking inner and outer plasma-membrane leaflets | Not supplied | Assume formulation from commercial synthetic lipids; compositions chosen a priori and documented |
| Known pore-forming protein positive control (e.g., a lytic toxin with well-characterized pore behavior) | Not supplied | Procure; needed for assay calibration |
| Protease/inhibitor-free assay buffers, fluorescent dextrans (graded MW), encapsulated fluorophore/quencher pairs | Assumed available | Commercial |

**Assumption register (unreported parameters that could change the design):** the exact N-terminal boundary of the cytotoxic fragment, whether the fragment is stable in soluble form, the caspase cleavage site efficiency in vitro, and the physiological relevance of any artificial lipid mixture. Each is explicitly tested or flagged below.

---

### Phase 1 — Assay calibration (before any GSDMD experiment)

**1.1 Liposome platform construction.** Prepare two platforms:
- (a) Large unilamellar vesicles (LUVs, ~100–200 nm) encapsulating a fluorophore/quencher pair or a self-quenching dye (e.g., ANTS/DPX or sulforhodamine) for bulk leakage kinetics.
- (b) Giant unilamellar vesicles (GUVs) or supported bilayers for single-vesicle microscopy.

**1.2 Calibration set (must pass before Phase 2):**
- Define maximal leakage (100% signal) with nonionic detergent; define zero with buffer alone.
- Establish the leakage dose–response of the positive-control pore-former on each lipid mixture; record EC50, slope, and kinetics. This benchmark defines what "pore-like" graded leakage looks like in this assay.
- Establish the size-selectivity curve with the positive control using liposomes loaded with fluorescent dextrans of graded hydrodynamic radius (this simultaneously validates the dextran-protection readout for the pore-vs-detergent discrimination).
- Verify liposome stability: <5% spontaneous leakage over the assay duration at assay temperature; confirm by negative controls in every plate.

**1.3 Protein quality gate (stop rule S1, below):** GSDMD-N batches must pass: (i) single dominant band on SEC; (ii) DLS polydispersity within a pre-specified window; (iii) documented endotoxin level below a pre-registered threshold; (iv) no leakage activity from the *storage buffer alone* on liposomes. Batches failing any criterion are repurified before proceeding.

---

### Phase 2 — Anchor experiment: purified GSDMD-N on defined liposomes (discriminates A from B/C)

**2.1 Independent units.** Independent unit = independently prepared liposome batch × independently prepared protein prep, on separate days. Minimum 3 independent liposome preparations and 2 independent protein preparations; all within-plate wells are technical, not biological, replicates and must not be counted as independent units.

**2.2 Allocation and blinding.**
- Randomize treatment wells across plates using a pre-registered allocation sequence; equal numbers of each condition per plate to control for plate-position artifacts (edge wells avoided or filled with buffer).
- Blinding: for microscopy and any manual scoring, coded samples are imaged and quantified by an analyst blinded to condition; automated image-analysis pipelines are pre-registered, and all extracted metrics are locked before unblinding.

**2.3 Conditions (core matrix).**
| Arm | Liposomes + | Purpose |
|---|---|---|
| 1 | Buffer only | Baseline leakage |
| 2 | Heat-denatured GSDMD-N | Nonspecific protein/control |
| 3 | GSDMD-C fragment | Fragment specificity control |
| 4 | Unrelated purified protein of similar size/charge | Nonspecific cationic-protein control |
| 5 | GSDMD-N, dose series (≥6 log-spaced doses) | Core test of Mechanism A |
| 6 | Full-length GSDMD (uncleaved) | Test of autoinhibition |
| 7 | Full-length GSDMD + purified active caspase | Physiological-processing test (Prediction A4) |
| 8 | Full-length GSDMD + heat-inactivated caspase | Cleavage specificity control |
| 9 | GSDMD-N + cytosolic extract (dialyzed, caspase-free) | First test of Mechanism B |
| 10 | Cytosolic extract alone | Extract-alone control |
| 11 | Positive-control pore-former | Assay-performance sentinel on every plate |

**2.4 Measurements.**
- **Primary:** kinetic leakage signal (fluorescence over time), quantified as % of detergent-max, area-under-the-curve and initial rate.
- **Secondary:**
  - Size-selectivity: repeat Arm 5 (at an active dose from the primary screen) with dextrans of graded radius → pore size estimate or exclusion (Prediction A3).
  - Binding: liposome flotation or cosedimentation with immunoblot — does GSDMD-N associate with membranes, and does the full-length protein?
  - Morphology: negative-stain EM / cryo-EM / AFM of liposomes ± GSDMD-N, with blinded classification of structures; pre-register what counts as a ring/oligomer vs. debris (Prediction A2).
  - Osmotic modulation: external osmolytes of graded size added to leaky liposomes/cells to test the osmotic-swelling mechanism of lysis.
  - Lipid scan: repeat Arm 5 across a small pre-registered panel of defined lipid mixtures varying inner-leaflet candidate lipids (Prediction A5). Pre-register the panel before seeing data.

**2.5 Analysis plan (pre-registered).**
- Primary comparison: leakage in Arm 5 vs. Arms 1–4 (Dunnett-style many-vs-one against buffer control), with dose–response fitted (four-parameter logistic). Significance is secondary to effect size: a pre-specified biologically meaningful threshold (e.g., ≥20% leakage above baseline at a dose where control proteins show <5%) set *a priori*.
- Compare Arm 7 vs. Arm 6 (cleavage-dependent activation) and Arm 7 vs. Arm 8 (caspase-activity dependence) by planned contrasts.
- Multiple-testing correction across the condition matrix; exact model (mixed-effects with plate as random effect) specified before data collection.

**2.6 Stop rules.**
- **S1:** Any protein batch failing the Phase 1 quality gate → halt, repurify; two consecutive batch failures → stop and redesign expression.
- **S2:** Positive-control pore-former fails its pre-registered performance window on a plate → discard that plate entirely (all conditions), repeat.
- **S3:** Buffer-only or denatured-protein controls exceed the pre-registered leakage ceiling (e.g., >10% of detergent max) → plate invalid; troubleshoot liposome preparation.
- **S4:** Interim check after the first full matrix: if variance among independent liposome preparations exceeds a pre-set CV threshold, halt and stabilize the platform before collecting the full dataset.
- **S5:** Pre-defined maximum number of full matrices (e.g., 3) to prevent unbounded iteration; document all stops.

**2.7 Troubleshooting (anticipated, in order of likelihood).**
- *Protein aggregation/precipitation:* lower concentration, adjust salt/pH, add mild detergent only after verifying it does not itself permeabilize liposomes; consider chaperone-assisted refolding.
- *Nonspecific leakage from cationic protein–membrane interaction:* include the matched-charge unrelated-protein control (Arm 4); consider charge-matched mutant or peptide controls.
- *Full-length protein contamination of N-fragment prep:* verify by immunoblot with C-terminal antibody; residual full-length/caspase contamination is the main false-positive risk for Arms 6–7.
- *Extract confounds (Arms 9–10):* endotoxin or residual active caspase in extract; test by caspase inhibitor and endotoxin spiking controls.
- *No signal anywhere despite passing sentinels:* consider that the fragment may require post-translational modification, a specific membrane curvature, or may be insoluble in the presentation used — this is an ambiguity trigger, not a negative result (see Section 5).

---

### Phase 3 — Cofactor dependency (disambiguates B if Phase 2 is negative or extract-dependent)

If GSDMD-N alone is inactive but extract restores activity:
1. Fractionate extract (heat, protease, size-exclusion, ion exchange); track activity; a heat-labile, protease-sensitive, finite-MW activity supports a protein cofactor (Prediction B2).
2. Reconstitute candidate purified cofactor with GSDMD-N on liposomes.
3. In parallel, cell-based test: deplete the candidate in cells, induce pyroptosis physiologically, and ask whether death is lost despite normal GSDMD cleavage (Prediction B3).

If GSDMD-N alone is active, Phase 3 is abbreviated to a check that extract neither requires nor enhances activity beyond the pre-registered threshold — confirming sufficiency.

### Phase 4 — Cellular cross-check (ties the cell-free result back to pyroptosis)

Regardless of Phase 2 outcome:
- Express (or deliver) active GSDMD-N in intact cells and measure (i) membrane dye entry vs. cytolysis timing, (ii) size-selective osmoprotection with graded dextran-osmolytes (small protect, large do not → pore-like mechanism), (iii) whether a membrane-binding-deficient version (identified from the Phase 2 lipid scan) loses both liposome activity and cellular toxicity. This concordance test is the strongest bridge from reconstitution to biology.

---

## 5. Conditional outcomes and the strongest justified conclusion in each

**Positive outcome (Arms 5 and 7 positive; Arms 1–4, 6, 8 negative; size cutoff and oligomeric structures observed).**
- *Strongest justified conclusion:* GSDMD-N is sufficient, in a chemically defined system, to bind and permeabilize lipid bilayers, and caspase cleavage of full-length GSDMD activates this function — i.e., the fragment is a direct membrane-effector pore-forming protein, and pyroptotic lysis is parsimoniously explained by fragment-formed pores. This supports Mechanism A.
- *What it does not establish:* the in-cell pore architecture, physiological lipid dependence, pore stoichiometry at atomic resolution, or that pores (rather than a further cellular amplifier) are the lethal lesion in vivo.

**Negative outcome (no leakage in any arm, sentinels passing, protein quality verified).**
- *Strongest justified conclusion:* under the tested conditions, GSDMD-N does not act directly on simple lipid bilayers; this *refutes sufficiency for this system only* and redirects support toward Mechanisms B or C.
- *Limits and ambiguity triggers:* lack of activity may reflect wrong fragment boundaries, missing modification, presentation failures (aggregation already excluded by the quality gate), or a lipid mixture lacking a required component. The lipid scan (Phase 2.4) and Phase 3 are the designed antidotes; if both fail, Mechanism C becomes primary and the plan shifts to intact-cell physiology.

**Ambiguous outcome.**
- Sub-threshold leakage, activity only with extract but also with extract alone, activity seen in one lipid mixture but not reproducibly, or structural "pore-like" objects without functional leakage.
- *Strongest justified conclusion:* the system is insufficiently defined to support or refute Mechanism A; the correct conclusion is a *methodological* one (present the ambiguity, do not claim mechanism), with pre-planned escalation: repeat at the failing variable (batch, lipid, dose), and only after two reproducible failures at a variable, treat it as biological (e.g., lipid-specificity) rather than technical.
- *Critical rule:* ambiguity must not be narratively resolved into "positive"; the stop rules exist to prevent this.

---

## 6. Distinguishing proposals from reported results — summary

| Reported (packet) | Proposed (this plan) |
|---|---|
| Caspase cleavage of GSDMD | In vitro caspase cleavage on liposomes (Arm 7) |
| Cleavage ↔ pyroptosis (genetic/fragment expression) | Purified-fragment liposome permeabilization (Arm 5) |
| N-terminal fragment is cytotoxic | Pore structures, size cutoffs, lipid dependence (Phase 2.4) |
| Nothing about the physical mechanism | All of Phases 0–4 |

No result from the proposed plan may be reported as observed; the plan is a single pre-registered attempt with explicit calibration, blinding, independent-unit definitions, stop rules, and three fully specified interpretive endpoints, so that its outcome — positive, negative, or ambiguous — yields an auditable and appropriately bounded conclusion about how gasdermin D execution of pyroptosis actually works.
