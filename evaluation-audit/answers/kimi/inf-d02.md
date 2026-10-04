# Kimi K3 / inf-d02

Original final answer, shared by both scoring rounds.

# Proposed bulk RNA-seq differential-expression plan

## 1. Recommended next action and execution status

**Recommended next action:** freeze an auditable design packet containing the unit definition, sample-sheet schema, randomization procedure, pinned input manifests, analysis configuration, acceptance criteria, and regeneration procedure. Calibrate all placeholders using independent pilot or control data before acquiring confirmatory data.

**Nothing has been executed.** No count matrices, sample sheets, reference files, annotation files, software versions, or results were supplied. Every path, version, numeric setting, threshold, analysis, and experiment below is **proposed**. Placeholders in brackets must be completed and frozen before execution.

---

## 2. Evidence-to-inference-to-conclusion chain

| Evidence and location | Permissible inference | Design conclusion |
|---|---|---|
| **E1.** Fixed evidence packet, source summary: the DESeq2 record describes negative-binomial generalized linear models with information sharing for dispersion and effect estimation, plus inference and diagnostics. | DESeq2 is an appropriate proposed count-model engine when the count observations correspond to the inferential units and the selected version behaves as documented. | Use a proposed DESeq2 negative-binomial GLM. Pin the implementation and verify its documentation before execution; the supplied packet does not establish current-version behavior. |
| **E2.** Same location: modelling does not create missing independent treatment replication. | Count models cannot convert technical replicates, wells, genes, or reads into independently allocated treatments. | The DESeq2 design table must contain one primary observation per independently allocated treatment unit. |
| **E3.** Same location: the experimental unit depends on independent treatment allocation. | The physical material receiving an independently assigned treatment is the unit; donor, well, or batch is not automatically the unit. | Determine the unit from the allocation mechanism before modelling. |
| **E4.** Same location: donor and well inference are distinct; one donor cannot identify across-donor heterogeneity merely by adding a donor random effect. | Multiple wells from one donor may support a within-donor comparison if independently allocated, but not a donor-population claim. | Record donor as a biological source or block. Make across-donor claims only when multiple independent donors and an estimable design support them. |
| **E5.** Fixed evidence packet: the read record is partial and no files or versions are supplied. | No implementation, model fit, diagnostic, or reproducibility claim can currently be made. | All analyses are proposed. The actual source and implementation must undergo a source-difference audit when available. |

**Central assumption:** DESeq2 will remain the analysis engine after its actual version, model interface, inference procedure, and FDR implementation are inspected. If they differ materially from the supplied record, revise the design or pin a version whose behavior is documented and validated.

---

## 3. Concept hierarchy and experimental-unit rule

The proposed hierarchy is:

```text
biological donor / source
  └─ independently allocated aliquot, culture, well, donor, or batch
       └─ sampled material
            └─ library preparation
                 └─ sequencing run
                      └─ reads
                           └─ gene counts
```

The inferential level is the level at which treatment was independently allocated:

1. **Treatment assigned independently to donors:** donor is the primary experimental unit.
2. **Treatment assigned independently to aliquots or wells within donors:** the aliquot or well is the treatment-allocation unit, while donor is a biological block. Wells must not be represented as independent donors.
3. **Treatment assigned independently to processing batches:** batch is the primary unit. Wells or donors within a batch are subsamples and must not inflate batch-level replication.
4. **Only libraries or sequencing lanes differ:** these are technical replicates and are not treatment replication.
5. **A gene is a measured feature, never an experimental unit.**

If the primary unit has repeated libraries or samples, combine them into one prespecified unit-level count profile or select one endpoint under a rule fixed before seeing differential-expression results. Repeated observations must not appear as independent rows in the primary model.

---

## 4. Proposed immutable input bundle

At design time, all files are missing. Create a manifest with status `MISSING_AT_DESIGN_TIME`, then complete and freeze it when inputs exist.

### 4.1 Manifest contents

For every input record:

- immutable identifier;
- original URI, accession, or provider;
- retrieval date and licence where applicable;
- file name and storage path as recorded at freeze;
- digest algorithm and digest;
- byte size;
- producer and production date where known;
- protocol or configuration version;
- status and reason for any replacement.

### 4.2 Required proposed inputs

1. **Raw sequencing reads:** `[READ_SET_ID]`, files, source, digests, lane/run relationships.
2. **Reference genome:** `[REFERENCE_SOURCE]`, `[REFERENCE_BUILD]`, `[REFERENCE_RELEASE]`, URI and digest.
3. **Annotation:** `[ANNOTATION_SOURCE]`, `[ANNOTATION_RELEASE]`, coordinate system, feature-level definition, URI and digest.
4. **Sample and unit sheets:** schema below, with digests.
5. **Allocation ledger:** treatment assignments, seeds, strata, and reveal status.
6. **Count-production pipeline:** `[ALIGNER_OR_QUANTIFIER]`, `[VERSION]`, parameters, reference and annotation IDs, environment lock.
7. **DESeq2 pipeline:** `[DESEQ2_VERSION]`, package environment, model, contrasts, filtering, FDR procedure, diagnostics and plot scripts.
8. **Decision log:** every amendment, QC failure, exclusion, stopping decision, and source difference.

No undeclared input should be readable by the final analysis. The pipeline should fail if an input digest, declared file, or configuration value is absent or changed.

---

## 5. Proposed sample-sheet schema

Use one observation-level sample sheet and derive a separate unit-level design table.

### Observation-level sheet

| Column | Purpose |
|---|---|
| `observation_id` | Unique physical library or measurement ID |
| `analysis_unit_id` | Immutable independently allocated treatment unit |
| `donor_id` | Biological source, or `NA` when not applicable |
| `well_or_aliquot_id` | Physical allocation container, or `NA` |
| `treatment` | `treatment` or `control`; no alternative spellings |
| `dose`, `duration`, `vehicle` | Placeholders fixed in the intervention protocol |
| `allocation_batch_id` | Batch used for randomization/allocation |
| `processing_batch_id` | Library or sample-processing batch |
| `randomization_stratum` | Donor, batch, or other declared stratum |
| `allocation_seed_id` | Pointer to immutable randomization record |
| `library_id`, `run_id`, `lane_id` | Technical provenance |
| `technical_replicate_of` | Observation ID when applicable, otherwise `NA` |
| `sample_role` | Experimental, reference control, blank, or other declared role |
| `read_file_ids`, `read_file_digests` | Exact files and digests |
| `blinded_qc_status` | QC state assigned before treatment unblinding |
| `include_primary` | `yes/no` under the locked rule |
| `exclusion_reason_code` | Controlled vocabulary, never free-text post hoc labels |
| `reference_id`, `annotation_id` | Frozen input identifiers |
| `pipeline_config_id` | Exact count-analysis configuration |

### Unit-level design table

One row per `analysis_unit_id`:

| Column | Purpose |
|---|---|
| `analysis_unit_id` | Primary model row |
| `unit_type` | Donor, aliquot/well, or batch |
| `donor_id` | Biological source/block |
| `treatment` | Assigned condition |
| `processing_batch_id` | Technical covariate or unit, depending on allocation |
| `unit_count_profile_id` | Digest of the count profile representing that unit |
| `primary_endpoint_id` | Endpoint selected under the locked rule |
| `include_primary` | Locked inclusion status |

### Metadata acceptance checks

Before unblinding or differential-expression analysis:

- every `analysis_unit_id` is unique in the unit table;
- treatment has exactly the declared levels;
- every unit has one and only one treatment;
- every count profile maps to one unit;
- donor, well, batch, library, and run relationships match the allocation design;
- treatment-by-donor and treatment-by-batch crossing tables are complete enough for the intended model;
- no digest or read-file identifier is missing;
- all exclusions were assigned without inspecting treatment-associated differential-expression results.

**Stop condition:** missing unit identity, ambiguous treatment assignment, duplicate use of a count profile, or a confounded design. Do not repair these after viewing DE results.

---

## 6. Operational ordered protocol

### Step 0 — Preparation and design freeze

1. Define the primary scientific claim:
   - within-donor treatment effect;
   - between-donor treatment effect;
   - batch-level treatment effect; or
   - exploratory/feasibility analysis.
2. Identify the independent allocation level before choosing a model.
3. Specify treatment, control, dose, vehicle, duration, sampling endpoint and handling procedures as `[INTERVENTION_PARAMETERS]`.
4. Create the immutable manifests, controlled vocabularies, exclusion rules and analysis configuration.
5. Run a design-only model check with no biological counts:
   - construct the planned design matrix;
   - verify full rank;
   - verify treatment is estimable;
   - verify residual degrees of freedom are nonzero;
   - verify donor and batch are not aliased with treatment.
6. Record all placeholder values and assumptions.

**Troubleshooting:** if treatment is aliased with donor or batch, redesign allocation. Do not add another model term as a substitute for replication.

### Step 1 — Calibration of unknown parameters

Use independent pilot or control data, frozen separately from confirmatory data. If no calibration material exists, label the study feasibility work rather than inventing parameters.

| Unknown | Proposed calibration |
|---|---|
| Number of donors and units `[N_DONOR]`, `[N_UNIT_PER_ARM]` | Estimate biological variation at the actual allocation level from pilot data; simulate the exact randomized design and planned count model over a range of unit numbers and effect sizes. Record assumptions and candidate values before choosing. |
| Across-donor heterogeneity | Measure donor-level effect variation using multiple independent donors in pilot data. A single donor cannot calibrate this quantity. |
| Number of processing batches `[N_BATCH]` | If treatment is assigned to batches, simulate batch-level replication. If batch is only a processing nuisance, ensure treatment is crossed across batches. |
| Sequencing depth `[TARGET_DEPTH]` | Use pilot libraries and prespecified downsampling to assess QC stability, count recovery and DE stability. Freeze the selected depth before confirmatory sequencing. |
| QC thresholds `[QC_*]` | Run known-reference controls and process controls across planned batches; derive thresholds from their distributions and failure modes before treatment outcome unblinding. |
| FDR target `[Q_PRIMARY]` | Choose from the study’s tolerance for false discoveries before analysis. Simulation can illustrate operating characteristics under assumed truths but cannot prove the realized FDR. |
| Biological effect threshold `[L_EFFECT]` | Derive from independent domain calibration. Use only as a secondary annotation unless preregistered as part of the decision rule. |

All calibration datasets, scripts, seeds, outputs and selected values become immutable design inputs.

### Step 2 — Allocation and blinding

1. Enumerate eligible experimental units before allocation.
2. Define strata, such as donor or allocation batch, only where they reflect the design.
3. Randomize treatment independently at the declared unit level:
   - randomization procedure `[RANDOMIZATION_METHOD]`;
   - seed `[RANDOM_SEED]`;
   - allocation software/version `[ALLOCATION_SOFTWARE]`;
   - complete assignment ledger.
4. Commit a digest of the allocation plan before intervention. Reveal the mapping to analysts only after the locked blinded-QC stage.
5. Balance processing order, plate or lane position, and library batches across treatment where feasible.
6. Record every allocation deviation and whether the assigned treatment was actually received.

**Stop condition:** treatment assignment is lost, non-independent, or completely confounded with donor or batch.

**Troubleshooting:** document a broken allocation and either repeat allocation with new independent units or downgrade the analysis to descriptive/feasibility work. Do not re-randomize after seeing biological outcomes.

### Step 3 — Intervention and sampling

1. Apply treatment and control under the frozen `[INTERVENTION_PARAMETERS]`.
2. Preserve `analysis_unit_id` through intervention, sampling, extraction and library preparation.
3. Use one primary endpoint per unit unless a repeated-measures design is separately specified and justified.
4. Record timing, operator, vessel, processing order and deviations.
5. If a unit is split after treatment, label the products technical subsamples, not independent treatment units.

**Stop condition:** identity mix-up, unequal handling that cannot be separated from treatment, or loss of allocation provenance.

### Step 4 — Measurements and controls

Proposed control set `[CONTROL_SET]`, to be validated during calibration:

- the planned biological control condition;
- known-reference samples carried across processing batches where available;
- process blanks where meaningful for the selected library method;
- optional positive controls with an independently established expected response;
- technical library replicates for pipeline precision, not treatment replication;
- optional external spike-ins only if validated and incorporated into the reference/counting procedure.

Control results calibrate process performance but must not be silently entered into the treatment contrast. If controls are included in any analysis, define their role before execution.

### Step 5 — Library and sequencing quality checks

Before treatment unblinding:

1. Verify sample and file identity against the immutable manifest.
2. Record library yield/quality metrics using `[LIBRARY_QC_METRICS]`.
3. Record read-level and alignment/quantification metrics using `[SEQUENCE_QC_METRICS]`.
4. Apply only the pre-calibrated `[QC_*]` thresholds.
5. Assign `blinded_qc_status` and exclusion codes without inspecting treatment DE results.
6. Freeze the QC-pass and QC-fail sets.

**Stop condition:** widespread control failure, batch-wide identity failure, or evidence that the count-production pipeline did not use the pinned reference or annotation.

**Troubleshooting:** repeat the failed technical step if independent material remains and the repeat was allowed by protocol. A failed unit is not replaced by a non-random convenience sample.

### Step 6 — Immutable count freeze

1. Quantify gene counts using `[COUNT_PIPELINE_ID]`, the frozen reference and frozen annotation.
2. Produce a gene-by-unit primary count matrix. If multiple technical profiles exist per unit, apply the locked unit-aggregation rule and retain all component profiles for audit.
3. Record gene identifiers, feature definitions, unassigned-count categories and quantification parameters.
4. Digest the raw count matrix, unit-level matrix, sample sheets and configuration.
5. Do not edit counts manually.

**Stop condition:** duplicate gene identifiers are unresolved, reference and annotation coordinates are incompatible, or count profiles cannot be mapped uniquely to units.

---

## 7. Proposed DESeq2 analysis

### 7.1 Model

Let \(i\) index independently allocated units and \(g\) index genes. Conceptually:

\[
Y_{gi} \sim \text{NegativeBinomial}(\mu_{gi}, \phi_g), \qquad
h(\mu_{gi})=\text{offset}_i + X_i\beta_g .
\]

The exact link, offset handling, dispersion procedure, estimator and inference implementation must be taken from the pinned DESeq2 documentation and recorded. The supplied evidence supports the proposed use of a negative-binomial GLM and reports information sharing for dispersion and effect estimation; it does not establish the details of an unpinned version.

### 7.2 Candidate design formulas

Choose exactly one primary formula before unblinding:

1. **Donor-level independent treatment assignment, one profile per donor:**

   `~ [BATCH_TERMS] + treatment`

   Use only if processing batch is crossed with treatment and the matrix is full rank.

2. **Independent aliquot/well assignment within donors:**

   `~ donor + [BATCH_TERMS] + treatment`

   This estimates the model-defined common within-donor treatment contrast when treatment is crossed within donor. It does not by itself establish a donor-population effect.

   Secondary heterogeneity model, only with enough independent donors:

   `~ donor + [BATCH_TERMS] + treatment + donor:treatment`

3. **Treatment assigned independently to batches:**

   Use one prespecified count profile per batch. Do not enter wells or donors within batches as independent batch-level observations.

4. **Aliased design:** if treatment is perfectly confounded with donor or batch, stop and redesign; there is no estimable causal treatment contrast under the planned model.

A donor random effect is not proposed as a remedy for absent donor replication. A mixed-model alternative would be outside the supplied evidence and would require separately documented methods and validation.

### 7.3 Primary contrast

- Primary contrast: treatment coefficient minus control coefficient.
- Null hypothesis: the primary treatment-control contrast is zero.
- Alternative: two-sided unless a directional hypothesis is preregistered.
- Exact contrast vector: generated from the final design-matrix coding and archived, rather than inferred from coefficient names.
- Effect reporting: report the implementation’s coefficient scale and any fold-change transformation exactly.

If the secondary donor-by-treatment interaction is used, test all interaction terms jointly and treat it as a separate hypothesis family.

### 7.4 Filtering and FDR

Before model execution, freeze:

- tested feature universe `[FEATURE_SET]`;
- low-count or other filtering rule `[FILTER_RULE]`;
- FDR method `[FDR_METHOD]`;
- primary FDR target `[Q_PRIMARY]`;
- secondary FDR target `[Q_SECONDARY]`;
- missing adjusted-value handling `[NA_RULE]`;
- independent-filtering or equivalent setting `[FILTERING_SETTING]`, if available in the pinned implementation.

A discovery call requires an adjusted value at or below `[Q_PRIMARY]`. An effect-size threshold `[L_EFFECT]` may be applied only as a preregistered secondary decision or annotation. Unadjusted p-values must not be used for the primary discovery claim.

### 7.5 Diagnostics and sensitivity analyses

Proposed diagnostics include:

- unit-level count and library summaries;
- sample relationship plots inspected before and after unblinding as scheduled;
- donor and batch balance summaries;
- dispersion and model-fit diagnostics provided by the pinned implementation;
- contrast-specific effect and uncertainty summaries;
- counts of tested, filtered, significant and non-estimable genes.

Predefined sensitivity analyses may include:

- QC-pass units only;
- a locked alternative treatment of QC-flagged units;
- the heterogeneity model only if specified before execution;
- a reference/annotation comparison only as a separately labelled analysis.

Any model-formula change after viewing results is an amendment requiring full regeneration from raw inputs, not a silent revision.

---

## 8. Plot regeneration without hidden state

Generate every figure from a script that reads only the frozen manifests and declared outputs. Proposed figure families are:

1. sample/unit QC and relationship plots;
2. donor and batch composition plots;
3. dispersion/model diagnostic plots;
4. effect-size plots;
5. primary-contrast volcano-style plot;
6. gene-level count plots for prespecified control or follow-up genes.

For each figure record:

- plot ID and purpose;
- source result/count-table digest;
- plotting script and environment digest;
- parameter values;
- random seed, if any stochastic method is used;
- underlying plot-data table and digest;
- rendered image and digest.

The canonical audit object is the underlying plot data plus deterministic code, not a manually edited image. A clean rerun must reproduce the declared plot-data digest. If image rendering differs across environments while plot data match, record the rendering difference and its cause in the difference ledger.

---

## 9. Acceptance, stopping and troubleshooting summary

| Stage | Acceptance criterion | Stop/troubleshooting action |
|---|---|---|
| Design | Unit level explicit; treatment estimable; design full rank | Redesign allocation; no model-based rescue of aliasing |
| Inputs | All required files, versions and digests immutable | Do not run until completed or document an explicit proposed amendment |
| Metadata | Unique unit mapping; no unresolved treatment/donor/batch ambiguity | Stop and reconcile provenance |
| Allocation | Independent, seeded and auditable | Re-randomize only before intervention; otherwise downgrade claim |
| Controls/QC | Calibrated `[QC_*]` criteria pass | Repeat permitted technical step or stop failed batch |
| Counts | Unique gene/unit mapping; reference-annotation compatibility | Correct pipeline before DE; no manual count edits |
| Model | Full rank, nonzero residual information, planned rows only | Simplify only under a preregistered rule or collect more units |
| Diagnostics | Predeclared diagnostic actions satisfied | Run locked sensitivity analysis or report infeasibility |
| FDR | Method, feature universe and target recorded | Do not call discoveries from unadjusted values |
| Reproduction | Clean rerun reproduces declared digests | Investigate through the source-difference ledger before interpretation |

---

## 10. Source-difference audit

Maintain an append-only audit table with one row per source, implementation, reference, annotation or output difference.

### Proposed audit fields

- audit ID;
- evidence or input source ID and digest;
- frozen implementation/version and digest;
- expected behavior or content;
- observed behavior or content;
- exact files, genes, samples or contrasts affected;
- whether the difference is documentation-only, formatting, substantive or outcome-changing;
- decision: retain, pin alternate version, requantify, remodel, or stop;
- scripts and outputs regenerated;
- reviewer, date and approval digest.

### Required comparisons

1. **DESeq2 record versus actual version:** compare the supplied record’s model, inference and diagnostic description with the pinned implementation documentation. Current status: **not assessed**.
2. **Reference versus annotation:** compare coordinate system, sequence names, feature identifiers and feature boundaries. Current status: **not assessed**.
3. **Reference or annotation versions over time:** report added, removed, renamed and changed features. If changed, requantify from raw reads or label the comparison as a separate secondary analysis.
4. **Pipeline source or environment changes:** compare declared and observed package versions and parameters.
5. **Sample-sheet amendments:** compare before/after sheets and show affected units.
6. **Plot or result regeneration:** compare canonical output digests and record any nondeterminism.

No source differences are currently known because no source files or software versions were supplied.

---

## 11. Alternatives, limits and decision-changing evidence

- **Single donor only:** report, at most, a conditional within-donor comparison supported by independently allocated units. Do not claim across-donor generalization.
- **Only one donor per treatment:** donor and treatment are aliased; redesign with independent donors.
- **Treatment confounded with processing batch:** batch-level causal inference is not available unless batches were independently randomized.
- **Technical replicates only:** use the study to estimate measurement reproducibility, not biological treatment effects.
- **Insufficient donors for heterogeneity:** omit the donor-by-treatment hypothesis or present it as exploratory.
- **Alternative mixed-effects model:** potentially relevant for correlated donor designs, but it is outside the supplied DESeq2 evidence and requires separate specification, calibration and validation.
- **Actual DESeq2 documentation differs from the supplied record:** revise the model specification, pin a compatible version, and rerun from immutable raw inputs.
- **No pilot data:** retain all numeric parameters as unresolved and treat the first study as feasibility rather than confirmatory.

All proposed analyses remain unexecuted and contingent on frozen files, calibrated parameters, independent treatment allocation and a completed source-difference audit.
