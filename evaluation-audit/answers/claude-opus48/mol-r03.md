# Claude Opus 4.8 / mol-r03

Original final answer, shared by both scoring rounds.

## Bottom line / recommended next action

The single most valuable next question the packet leaves open is: **Does the gasdermin D N‑terminal fragment (GSDMD‑NT) itself physically injure the membrane—by binding lipids and assembling into a transmembrane pore—or does it instead act as a trigger that recruits or activates a separate host component that performs the actual membrane injury?**

The packet explicitly states that genetics and fragment‑expression show the N‑terminus is *necessary and sufficient for cytotoxicity* but do **not** reveal the physical action or the executioner. The decisive, discriminating experiment is a **cell‑free reconstitution**: purified GSDMD fragments added to chemically defined, protein‑free liposomes (and planar bilayers). This directly tests *sufficiency of the protein acting on lipid alone*, which is exactly the inference gap genetics cannot close. I lay out that plan below, with a complementary cell‑based genetic arm to connect the in‑vitro answer back to physiology.

I have no author purified‑protein data in the packet; everything beyond the quoted genetic/expression findings is an explicit proposal, not a reported result.

---

## 1. Evidence → inference → open question

**Evidence (supplied):**
- Inflammatory caspases cleave GSDMD.
- Genetic loss of GSDMD and expression of the cleavage fragment link processing to pyroptotic death.
- The amino‑terminal portion carries the cytotoxic activity.

**Valid inferences:**
- Cleavage is a licensing step; the N‑terminus is the active moiety; the C‑terminus is likely autoinhibitory (consistent with fragment‑expression toxicity but full‑length tolerance).

**What the evidence cannot decide (the gap):**
- Genetics/expression operate inside intact cells, which contain every possible host protein, lipid, and signaling pathway. Demonstrating that NT is *sufficient in a cell* does not distinguish an **intrinsic lipid‑attacking protein** from a **trigger that commandeers a host executioner**. "Sufficient component" ≠ "direct effector."

Hence the open biological question above.

---

## 2. Competing mechanisms and their discriminating predictions

**M1 — Direct, intrinsic, lipid‑selective pore former.**
GSDMD‑NT binds specific lipids (candidate: inner‑leaflet acidic lipids such as phosphatidylserine, phosphoinositides, cardiolipin), oligomerizes, and inserts to form a transmembrane pore. The protein alone is the effector; the only required partner is lipid.

**M2 — Indirect trigger of a separate host executioner.**
GSDMD‑NT does not itself breach the bilayer. It activates/recruits a distinct host component (e.g., a resident ion channel, a lipid‑remodeling enzyme, or a dedicated membrane‑rupture protein) or initiates a signaling cascade that executes permeabilization. The fragment is the switch, not the blade.

**M3 — Conditional direct attack (lipid‑/cofactor‑gated).**
GSDMD‑NT is intrinsically lytic but only against membranes of a particular composition or in the presence of a small non‑protein cofactor; this would explain selectivity (self vs. bystander, host vs. microbial membranes) while remaining "direct."

**Discriminating predictions:**

| Observation on **protein‑free defined liposomes/bilayers** | M1 predicts | M2 predicts | M3 predicts |
|---|---|---|---|
| Purified NT alone permeabilizes pure liposomes | **Yes** | **No** | Yes, but only for specific lipid/cofactor compositions |
| Requirement for any host protein | None | **Required** (reconstitution fails without it) | None (lipid/cofactor only) |
| Lipid‑composition dependence | Likely (inner‑leaflet acidic lipids) | N/A (fails regardless) | **Strong and necessary** |
| Oligomerization + discrete pores by EM | Yes | No (on pure lipid) | Yes (on permissive lipid) |
| Dose–response cooperativity (Hill > 1) | Yes | — | Yes |
| Full‑length / C‑terminal domain active | No | No | No |

The pivotal fork is the **first row**: does purified NT permeabilize a *protein‑free* bilayer? M2 is falsified by any robust, lipid‑dependent permeabilization of pure liposomes by the fragment alone.

---

## 3. Proposed research plan (detailed, ordered, auditable)

> All items below are **proposed** methods. I do not assert any outcome was observed.

### Arm A — Reagent production and validation (prerequisites)

**A1. Constructs.**
- Human (and in parallel a rodent ortholog for cross‑validation) GSDMD: (i) full‑length; (ii) N‑terminal domain (NT, residues ~1–275, boundary set at the caspase cleavage site); (iii) C‑terminal domain; (iv) a cleavage‑site mutant (uncleavable) full‑length control; (v) candidate "pore‑dead" point mutants in the predicted membrane‑insertion/lipid‑binding region for later use.
- Tags: cleavable N‑terminal His‑SUMO (or His‑MBP) to improve solubility and allow tag removal by TEV/SUMO protease, avoiding a residual tag on the active NT.

**A2. Expression strategy that controls for NT toxicity.**
- Because free NT may be toxic/aggregation‑prone in *E. coli*, express **full‑length GSDMD** (tolerated), purify, then generate NT **in vitro** by cleavage with recombinant active inflammatory caspase. This mirrors the physiological route and avoids an engineered junction.
- In parallel, express tagged NT directly as a fusion (kept soluble by the large tag) for an independent protein source.
- Two independent protein lineages (caspase‑cleaved vs. directly expressed NT) guard against artifacts of either route.

**A3. Purity and folding QC (must pass before any membrane assay — stop rule).**
- SDS‑PAGE/Coomassie ≥95% purity; identity by mass spectrometry and anti‑GSDMD immunoblot.
- Monodispersity by size‑exclusion chromatography and SEC‑MALS; dynamic light scattering to quantify aggregation.
- Secondary structure by circular dichroism consistent with a folded β‑rich domain; thermal stability (nanoDSF/DSF).
- Endotoxin and detergent quantification (both can nonspecifically lyse liposomes — critical confound). Use endotoxin‑low purification and verify lipid‑polymyxin or Triton assays rule out contaminating lytic activity.

**A4. Caspase reagent QC.**
- Recombinant active caspase, catalytically dead caspase mutant, and a non‑inflammatory protease control. Verify cleavage of GSDMD by immunoblot (appearance of NT band) and absence of cleavage with the uncleavable mutant and dead enzyme.

### Arm B — Defined liposome system (calibration and independent units)

**B1. Liposome compositions (independent experimental units; each prepared as ≥3 independent batches).**
- (L1) Inner‑leaflet mimic: PC/PE + phosphatidylserine ± phosphoinositides.
- (L2) Cardiolipin‑containing (mitochondrial/bacterial‑like).
- (L3) Outer‑leaflet mimic: PC/PE + sphingomyelin + cholesterol, no acidic lipids.
- (L4) Pure PC (neutral baseline).
- (L5) Bacterial lipid mimic (PE/PG/cardiolipin).
- Each loaded with a self‑quenching dye (calcein) or an ANTS/DPX pair; separately, versions loaded with fluorescent dextrans of graded size (e.g., 3, 10, 40, 70 kDa) for pore‑size sizing.
- Characterize all batches by dynamic light scattering (size), and confirm encapsulation efficiency and baseline leakage (<5% over assay window).

**B2. Calibration of the readout.**
- Define 0% release = buffer‑only well; 100% release = detergent (Triton X‑100) lysis.
- Positive pore‑forming control (e.g., a well‑characterized pore‑former or detergent titration) to establish dynamic range, signal‑to‑noise, and limit of detection.
- Establish linearity of dye signal vs. known release; set the quantitation window.

### Arm C — Core discriminating experiment: sufficiency on protein‑free bilayers

**C1. Dye‑release assay (primary endpoint).**
- Conditions (randomized plate layout; well positions coded by a colleague so the analyst is **blinded** to identity):
  - NT alone (caspase‑cleaved) across each liposome composition, dose series (e.g., 0–several µM) for EC50/Hill.
  - NT (directly expressed) — independent protein source, same series.
  - Full‑length GSDMD alone (negative).
  - C‑terminal domain alone (negative).
  - Uncleavable full‑length + active caspase (should not generate NT; negative).
  - Full‑length + active caspase in situ (should generate NT; test whether *in‑liposome* cleavage suffices).
  - Full‑length + catalytically dead caspase (negative).
  - Heat‑denatured NT (folding‑dependence control).
  - Buffer only (0%); Triton (100%).
- Biological units = independent protein preps × independent liposome batches; technical replicates per unit. Pre‑register n (e.g., ≥3 independent protein preps × ≥3 liposome batches) and the analysis plan.

**C2. Lipid‑binding (mechanistic linkage).**
- Liposome co‑flotation (sucrose gradient) and co‑sedimentation: does NT partition with membranes, and is partitioning lipid‑composition dependent? Full‑length and C‑terminal as controls.
- Protein–lipid overlay / bio‑layer interferometry to rank lipid affinities, with the caveat that overlay assays are qualitative.

**C3. Oligomerization state in the membrane.**
- Blue‑native PAGE and chemical crosslinking of NT incubated ± liposomes: migration shift to high‑order oligomer only in the presence of permissive lipid supports M1/M3.

**C4. Direct pore visualization.**
- Negative‑stain EM and, if rings are seen, cryo‑EM of NT‑treated liposomes to resolve ring/pore assemblies and inner diameter. Images coded and counted blind.

**C5. Electrical pore characterization (orthogonal, protein‑free).**
- Planar lipid bilayer (black lipid membrane) or droplet‑interface bilayer electrophysiology: add NT to one side; record stepwise conductance insertions. Measure single‑channel conductance, voltage behavior, and gating. A purely lipid bilayer with no host protein is the cleanest refutation of M2.

**C6. Pore‑size sizing.**
- Graded‑dextran release defines an exclusion limit (an estimate of functional pore diameter), to be cross‑checked against EM inner diameter.

### Arm D — Addressing the "other component" hypothesis directly (M2)

**D1. Crude‑vs‑pure membrane contrast.**
- Compare NT activity on protein‑free liposomes (Arm C) vs. protease‑/protein‑stripped native membrane vesicles vs. intact native membrane vesicles. If activity requires native‑membrane proteins, a required host executioner is implicated (favoring M2).

**D2. Candidate‑factor add‑back.**
- If pure liposomes fail but native membranes succeed, fractionate native membranes (detergent solubilization + chromatography) and test which fractions restore NT‑dependent permeabilization of liposomes, then identify constituents by mass spectrometry. This is the path to naming an executioner under M2.

**D3. Distinguish pore formation from terminal membrane rupture.**
- Conceptually, M2 could be true at a *downstream* step (a dedicated host protein executing final osmotic rupture) even if M1 is true for the initial pore. Design cell‑based readouts (Arm E) that separate **small‑molecule/ion flux through a pore** (early, dye influx, ion changes) from **large‑scale lysis/LDH release** (late), so the two steps are not conflated.

### Arm E — Cell‑based genetic bridge (connect in‑vitro answer to physiology)

**E1. Structure‑guided mutants in cells.**
- Reconstitute GSDMD‑knockout cells with: wild‑type, uncleavable mutant, and the "pore‑dead"/lipid‑binding mutants defined in Arm C. Trigger inflammasome.
- Prediction under M1: mutants that lose liposome permeabilization in vitro also lose pyroptosis in cells, while retaining caspase cleavage and correct localization — a genotype‑to‑biochemistry concordance tying the direct‑pore mechanism to cell death.

**E2. Membrane‑targeting readouts.**
- Live‑imaging of dye influx, propidium uptake kinetics, and membrane localization of tagged NT; correlate pore‑competent mutants with membrane recruitment.

**E3. Executioner‑gene test (only if M2 signals emerge).**
- If Arm D identifies a candidate host executioner, delete it genetically and ask whether NT‑driven death (or its terminal rupture step) is abolished while upstream events persist.

### Allocation, blinding, and statistics

- **Allocation:** plate/well assignment randomized; liposome batches and protein preps rotated across conditions so no condition is confined to one batch.
- **Blinding:** sample identities coded for the operator of dye‑release reads, EM counting, and electrophysiology scoring; unblinded only after analysis is locked.
- **Analysis:** per condition, compute % release normalized to detergent max; fit dose–response for EC50 and Hill coefficient; compare compositions and controls with pre‑specified tests (mixed‑effects model with prep/batch as random effects to respect independent units). EM: pore counts/diameters with blinded quantitation. Electrophysiology: event frequency and conductance distributions.
- **Pre‑registration:** compositions, n, EC50 fitting, and acceptance thresholds fixed before data collection.

### Stop rules and troubleshooting

- **Stop/repeat if positive control (detergent/known pore‑former) fails** or baseline liposome leakage >5% — the assay is not interpretable.
- **Stop/repeat if protein QC fails** (aggregation, endotoxin/detergent contamination, misfolding by CD). A negative result from aggregated protein is uninterpretable.
- **Caspase‑cleavage incompleteness:** verify by immunoblot; optimize enzyme:substrate ratio; include in‑gel densitometry of NT yield.
- **Nonspecific lysis artifact:** confirm full‑length and C‑terminal domain at matched concentrations do **not** release dye; confirm heat‑denatured NT is inactive; run detergent/endotoxin checks. If full‑length also lyses, suspect contamination.
- **No activity on any composition despite clean binding:** escalate lipid space (charge, curvature, specific phosphoinositides), test pH/ion conditions mimicking the target leaflet, and run Arm D crude‑membrane contrast before concluding.
- **Aggregation masquerading as oligomer:** distinguish lipid‑dependent oligomer (BN‑PAGE shift only with permissive liposomes) from buffer aggregation (DLS).

---

## 4. Conditional conclusions (what each outcome licenses)

**Positive for M1 (direct pore former).**
If purified NT (from both independent protein sources) permeabilizes protein‑free liposomes in a dose‑dependent, cooperative (Hill > 1), lipid‑composition‑dependent manner; binds the same permissive lipids; forms high‑order oligomers only on permissive membranes; yields discrete ring/pore structures by EM; and produces stepwise conductance in pure planar bilayers — while full‑length, C‑terminal domain, uncleavable substrate, dead caspase, and heat‑denatured NT are all inactive — then the strongest justified conclusion is: **GSDMD‑NT is itself the membrane effector, an intrinsic, lipid‑selective pore‑forming protein that requires no additional host protein to breach the bilayer.** Arm E concordance (pore‑dead mutants lose pyroptosis despite normal cleavage) would then tie this directly to pyroptotic death in cells. This falsifies M2 at the pore‑formation step.

**Positive for M2 (separate executioner).**
If purified, well‑folded NT does **not** permeabilize any pure liposome composition yet does permeabilize intact native membranes, and if a fractionated native‑membrane protein component restores activity on liposomes (identified by mass spectrometry), with genetic deletion of that component abolishing NT‑driven permeabilization in cells — then: **GSDMD‑NT acts as a trigger and a distinct host component executes membrane injury.** Naming that component becomes the next program.

**Positive for M3 (conditional direct attack).**
If NT permeabilizes pure liposomes but strictly only for a defined lipid/cofactor composition (e.g., requires a specific acidic lipid or small cofactor, inactive on others), with oligomer/EM/electrophysiology signatures present on permissive lipid only — then: **GSDMD‑NT is a direct but lipid‑/cofactor‑gated pore former,** explaining membrane selectivity without invoking a host protein executioner.

**Negative / ambiguous outcomes and their handling.**
- *Weak release only at very high, nonphysiological protein concentrations:* ambiguous — could indicate a missing cofactor (M3/M2) or suboptimal lipid/buffer. Do not conclude "direct"; pursue Arm D and expanded lipid space before interpretation.
- *Binding without permeabilization:* consistent with either a disabled in‑vitro insertion step (technical) or a genuine requirement for a partner (M2). Requires the crude‑vs‑pure membrane contrast to disambiguate.
- *Activity present but no visible pores by EM / no stepwise conductance:* ambiguous between a pore and a non‑pore lipid‑disrupting (detergent‑like) mechanism; recheck contamination, refine EM/electrophysiology, and use graded‑dextran sizing to test for a defined exclusion limit (a defined limit argues for a structured pore, not diffuse disruption).
- *Discordance between arms* (e.g., in‑vitro pore but cell mutants not matching) flags that a cell step beyond pore formation (possibly a downstream rupture executioner) is also operating — compatible with M1 for the pore and M2 for terminal lysis simultaneously; the early‑vs‑late readouts in E2/D3 are designed to detect exactly this layered answer.

---

## 5. Limits of the proposal

- **Sufficiency in vitro ≠ exclusivity in vivo.** A positive M1 result proves the protein *can* form pores on lipid alone but does not by itself prove this is the sole or dominant route in cells; the genetic concordance arm (E) is required to bridge that gap, and even then a downstream host executioner for terminal rupture is not excluded.
- **Lipid space is large.** A negative liposome result is only as strong as the compositions tested; the conclusion "requires a host factor" is safe only after the crude‑vs‑pure membrane contrast (D1) shows native‑protein dependence.
- **Reagent artifacts dominate false signals.** Endotoxin, residual detergent, and aggregation can mimic or mask pore activity; the QC stop rules are integral, not optional.
- **Boundary/tag choices** for the NT fragment could perturb activity; using caspase‑generated NT as the primary reagent mitigates this, and the two independent protein sources cross‑check it.
- No author purified‑protein data exist in the packet; all of Arm A–E and every predicted outcome are **proposals**, not reported findings.
