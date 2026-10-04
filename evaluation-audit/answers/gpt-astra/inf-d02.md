# GPT-6 Astra / inf-d02

Original final answer, shared by both scoring rounds.

## Proposed recommendation and scope

**Freeze a versioned analysis specification before unblinding, and permit differential-expression inference only after verifying independent treatment replication and contrast estimability.** Libraries, sequencing lanes, and downstream subsamples must not be counted as additional experimental units.

**All experiments, analyses, checks, audits, and outputs below are proposed.** No files, sample sheets, count matrices, or actual versions are supplied; this is not an execution report. Every path, software/reference version, seed, numerical setting, and threshold would remain a recorded placeholder until justified and frozen.

## 1. Evidence → inference → conclusion

The evidence locations below refer to the supplied packet, not to an independently inspected publication.

| Evidence location | Supplied evidence | Inference | Proposed consequence |
|---|---|---|---|
| Source summary, first sentence | The DESeq2 record describes negative-binomial generalised linear models, information sharing for dispersion and effects, inference, and diagnostics. | A count-based negative-binomial workflow is appropriate to propose, subject to its assumptions. | Propose DESeq2 for an identifiable, suitably replicated fixed-effects design; archive its exact configuration and diagnostics. |
| Source summary, first and second sentences | Modelling does not create missing independent treatment replication; experimental units follow independent treatment allocation. | Borrowing information across genes cannot substitute for biological allocation units. | Reconstruct allocation before defining sample size or fitting a model. |
| Source summary, second sentence | Donor and well inference differ; a single donor cannot identify across-donor heterogeneity by adding a donor random effect. | The scope of inference depends on donors and allocation, not merely library count. | Restrict a single-donor experiment to that donor’s context; require independently sampled donors for across-donor inference. |
| Source summary, third sentence; hypothetical constraints | The read record is partial, and no files or versions are available. | Neither implementation details nor results can be verified. | Label the workflow as proposed, keep unresolved parameters explicit, and distinguish source-supported claims from protocol choices. |

The packet supports this statistical framework, **not any particular filtering threshold, software release, QC cutoff, or original-author implementation**.

## 2. Preparation: freeze inputs and expose all state

### Proposed immutable input bundle

Before analysis, archive read-only snapshots of:

- Raw reads, if available; otherwise the supplied count matrix and its upstream provenance.
- Sample sheet, allocation record, intervention/sampling records, and exclusion history.
- Reference sequence and annotation files.
- Analysis specification, executable source, dependency lockfile, and resolved configuration.

A proposed input manifest would contain:

`artifact_id, role, original_location, immutable_location, byte_size, checksum_algorithm, checksum, acquisition_date, source/accession, declared_version, parent_artifact_ids`

Locations would be placeholders such as `<immutable_input_location>`, not existing paths. Corrections would create new immutable revisions; no file would be silently overwritten.

### Proposed execution contract

The eventual workflow would:

1. Verify checksums and schema constraints.
2. Run from an empty work directory using only declared inputs.
3. Reject missing or incompatible configuration rather than silently selecting defaults.
4. Record the source revision, clean working-tree status, environment/container digest, package versions, operating system, numerical libraries, locale, thread settings, seeds, command lines, and relevant environment variables.
5. Produce a machine-readable run manifest, logs, output checksums, and an input-to-output dependency graph.

Downloaded resources and caches would either be forbidden during execution or declared and content-addressed. Any output-affecting software defaults would be captured in the resolved configuration. Manual edits to results or plots would be prohibited.

**Proposed acceptance gate:** unknown provenance would be reported explicitly. Count-only inputs could support downstream analysis if otherwise adequate, but would not support a claim of raw-read-to-result reproducibility.

## 3. Independent units and the proposed sample sheet

### Required sample-sheet structure

Use one row per physical library, with identifiers linking libraries to their true allocation units:

| Field group | Proposed fields |
|---|---|
| Identity | `library_id`, `biospecimen_id`, `allocation_unit_id`, `donor_id`, parent sample/culture ID |
| Allocation | treatment assignment, allocation level, randomisation block, paired-set ID |
| Intervention | treatment/control identity, dose, duration, administration time, deviations |
| Sampling | tissue/cell source, collection time, well/culture ID, processing order |
| Processing | extraction, library-preparation and sequencing batches; lane/run; library protocol; strandedness |
| Replication | technical-replicate group, biological-subsample relationship, repeated-measure relationship |
| Provenance/QC | input artifact IDs, prespecified covariates, QC fields, inclusion status and reason |

Missingness would use explicit codes rather than ambiguous blanks. Direct identifying information would remain outside the analysis bundle; stable pseudonymous IDs would preserve linkage.

### Proposed unit decision rules

- **Treatment assigned to whole donors:** donors are experimental units. Wells, biopsies, or libraries within a donor are subsamples. Compatible measurements could be aggregated according to a prespecified rule, or analysed using a justified hierarchical model.
- **Treatment independently assigned to wells within donors:** wells may be treatment-allocation units, with donor acting as a block. This does not make wells independent donors.
- **Treatment assigned to a culture before splitting into wells:** the culture is the allocation unit; downstream wells are subsamples.
- **Repeated sequencing of the same library or biospecimen:** technical replication only. Compatible counts would be merged using a frozen rule, not entered as independent samples.
- **Repeated times or biologically distinct subsamples:** do not sum merely to remove dependence. Prespecify a relevant endpoint or use a model that represents the dependence.

For a single donor with independently allocated wells, the proposed inference would concern treatment effects under that donor’s experimental conditions. It would not estimate population-level donor variation.

**Proposed stopping gate:** if each arm has only one independently assigned unit, modelling and gene-wise information sharing would not rescue independent treatment replication. Restrict the work to descriptive QC/effect summaries, or propose additional independent allocations before inferential DE analysis.

## 4. Allocation and blinding

For a **proposed prospective experiment**:

1. Define the allocation unit and target estimand before treatment.
2. Randomise treatment at that level, using donor or other justified blocks where applicable.
3. Distribute treatment and control across processing batches where feasible.
4. Archive the allocation algorithm, seed, sequence, and authorised deviations.
5. Use coded samples for handling and treatment-blinded technical QC where feasible.
6. Freeze exclusions, processing choices, and the primary analysis before releasing the treatment key.

The key would be access-controlled during blinding and retained in the final restricted audit bundle; it would not remain undocumented hidden state.

For an existing study, reconstruct actual allocation and blinding from records. **Do not assume randomisation or balanced processing.**

**Proposed stopping gate:** if treatment and batch are perfectly confounded, adding batch to a model cannot identify separate effects. Seek bridging samples or a redesigned experiment; otherwise report the limitation and avoid a treatment-specific causal claim.

## 5. Intervention, sampling, measurements, and controls

### Intervention and sampling

Dose, exposure duration, collection time, tissue/cell source, handling interval, and storage conditions are unreported.

**Proposed calibration:** use feasibility work to assess tolerability, timing, yield, and handling stability; select conditions against prespecified biological and technical objectives, not the number of significant genes. Freeze the resulting protocol before the confirmatory experiment.

Collect a consistent biological compartment at the intended endpoint. Record deviations before expression results are inspected.

### Proposed measurements

The primary measurement would be a **gene-by-library matrix of nonnegative integer fragment/read counts**, with the counting unit matched to library layout. Record:

- Library layout and strandedness determination.
- Reference-building, alignment, and counting software versions and parameters.
- Policies for paired reads, multimapping, ambiguous overlaps, duplicates, and feature inclusion.
- Count summaries, assigned-read fractions, library complexity indicators, and sample identity checks when feasible.

TPM, FPKM, and log-transformed expression would not replace raw counts in the proposed primary count model. A transcript-quantification alternative would require a separately specified import and offset procedure.

### Proposed controls

- Concurrent biological treatment/control allocation at the correct unit level.
- Appropriate vehicle or handling controls, if required by the intervention.
- Extraction/library blanks where informative for contamination.
- Repeated reference material or bridge aliquots across processing batches where feasible.
- Spike-ins only if their purpose, introduction stage, and normalization assumptions are prespecified.

Technical controls would diagnose processing; they would not increase independent biological sample size. A global RNA-output question may require calibration beyond standard relative-expression normalization.

## 6. Reference, annotation, and preparation QC

### Proposed frozen reference record

Record and checksum:

- Organism, assembly accession, release/patch, and sequence file.
- Annotation provider, release, file, and matching assembly.
- Included contigs, decoys, masks, and special feature sets.
- Gene/transcript identifier conventions and transcript-to-gene mapping.
- Index-building software, parameters, commands, and index artifacts.

Preserve stable gene identifiers, including version suffixes where present; attach display symbols separately. Check duplicate identifiers, annotation/sequence compatibility, and count-table feature matching.

An annotation update would create a new analysis revision, not replace the old reference.

### Proposed QC order

1. Validate identifiers, file checksums, library relationships, and metadata consistency.
2. Assess read quality, adapters, contamination, mapping/assignment, and strandedness when raw reads are available.
3. Assess count-library sizes, sparsity, feature distributions, sample correlations, and exploratory sample structure.
4. Examine patterns against donor, allocation unit, processing batches, and treatment after unblinding.
5. Investigate discrepancies against laboratory records.

An unusual sample would trigger investigation, not automatic removal. Expression separation by treatment is neither a required QC outcome nor proof of biological validity.

### Calibration of unknown settings

| Unreported parameter | Proposed calibration procedure |
|---|---|
| Independent-unit sample size | Use feasible pilot estimates or explicitly labelled variance/effect scenarios; evaluate power at the intended FDR and include uncertainty and attrition. Count allocation units, not libraries. |
| Sequencing depth | Assess pilot depth/subsampling curves and the abundance range relevant to the scientific question. |
| Technical QC cutoffs | Use platform/process performance and blinded pilot distributions; freeze rules before inspecting treatment DE. |
| Low-count filter | Examine detectability versus depth without selecting thresholds for favourable treatment results; freeze the feature-eligibility rule. |
| FDR level and meaningful effect | Set from the scientific decision and consequences of false discoveries; record separately. |

Pilot data used to tune decisions would be identified. Reuse in confirmatory analysis would require explicit handling of that adaptation.

## 7. Proposed differential-expression analysis

### Estimand and design

The primary proposed estimand would be **treatment minus control in gene expression**, conditional on prespecified identifiable covariates and interpreted at the allocation/population level actually supported.

For a compatible count matrix, propose:

\[
K_{gj}\sim \mathrm{NB}(\mu_{gj},\alpha_g),\qquad
\operatorname{Var}(K_{gj})=\mu_{gj}+\alpha_g\mu_{gj}^{2},
\]

\[
\log(\mu_{gj})=\log(s_j)+\beta_{g0}
+\beta_{gT}T_j+\text{estimable donor/block and batch terms}.
\]

Here \(s_j\) is the proposed library-size/composition normalization factor. DESeq2 would provide gene-wise inference with information sharing as described in the packet.

Proposed design alternatives:

- **Independent donors assigned between arms:** treatment plus justified estimable covariates/batches. A separate fixed effect for every donor would absorb the between-donor treatment contrast and would not be added.
- **Treatment/control represented within multiple donors:** donor blocking plus treatment, with batch only if estimable.
- **Single donor, independently treated wells:** treatment and estimable technical covariates; donor-population inference would remain unavailable.
- **Additional repeated-measure or hierarchical dependence:** use a separately justified count-model framework if needed. A donor random effect is not a repair for a single donor or an unreplicated treatment.

Before fitting, archive the design matrix, factor levels, reference categories, contrast vector, rank/estimability checks, and counts of independent allocations per arm and block.

### Normalization and modelling assumptions

The proposed normalization method would be named and frozen. Its assumptions about relative expression and compositional change would be evaluated. Strong global shifts or domination by a few features could motivate prespecified control-based normalization, but only with suitable calibration data.

Information sharing would improve parameter estimation; it would not establish independence or eliminate confounding.

### Contrast, testing, and FDR

- Primary contrast: **treatment relative to control**, with positive log2 fold change meaning higher expression under treatment.
- Primary null: no treatment effect for the selected contrast.
- Proposed primary test: a recorded DESeq2 Wald-test configuration.
- Proposed multiplicity correction: Benjamini–Hochberg adjustment across the declared eligible gene family for that contrast.
- Decision threshold: `<FDR_target>`, fixed before unblinding.

Record the eligible family, filtering rule, any independent-filtering configuration, unavailable-test reasons, and handling of influential observations. Do not tune these choices to increase discoveries.

Additional contrasts would have prespecified multiplicity families or be labelled exploratory. A minimum-effect hypothesis, if scientifically required, would be specified separately; post hoc fold-change filtering would not establish that effects exceed a meaningful threshold.

Report unshrunken estimates and inferential statistics separately from any proposed shrunken effects used for ranking or display, including the shrinkage method and settings.

### Proposed result table and sensitivity checks

Report gene ID, annotation, abundance summary, effect estimate, uncertainty, test statistic, raw and adjusted p-values, eligibility/outlier flags, contrast ID, and run ID.

Proposed diagnostics would assess dispersion fit, normalization, influential observations, residual structure, and covariate dependence. Prespecified sensitivity analyses could compare defensible normalization, filtering, or exclusion choices. They would qualify the primary result, not replace it with the most favourable analysis.

## 8. Plot regeneration and acceptance/stopping criteria

### Proposed plots

Generate library/count QC plots, sample-distance/PCA plots, dispersion diagnostics, MA and volcano plots, and selected-gene or heatmap displays.

Each plot would have:

- Declared source-table checksums and run ID.
- Script/function and resolved configuration.
- Exact sample/gene selection, transformation, scaling, and annotation rules.
- Dimensions, device, fonts, palettes, labels, and any seed.
- A companion data table where practical.

PCA and heatmap transformations would be for exploration/visualisation, not DE model inputs. Selected-gene plots would show allocation-unit observations or explicitly identify subsamples. Plotting would run noninteractively without objects from an earlier session.

**Proposed regeneration test:** rebuild tables and plots in a clean environment. Require matching checksums for deterministic artifacts; otherwise prespecify justified numerical or rendering tolerances and report differences.

### Proposed gates and troubleshooting

| Finding | Proposed action |
|---|---|
| Checksum or metadata mismatch | Stop; reconcile provenance and issue a new immutable revision. |
| Unresolved allocation structure | Stop inferential analysis; obtain allocation records. |
| No independent treatment replication or nonestimable contrast | Restrict to descriptive work or propose redesigned/additional allocations. |
| Failed technical QC | Investigate documented causes; rerun processing or exclude only under frozen rules. |
| Apparent sample swap | Require independent supporting records/identity evidence before relabelling. |
| Severe influence or poor model fit | Investigate; report prespecified sensitivity analysis or justify an alternative model. |
| No significant genes | Report estimates, uncertainty, and study limitations; do not lower thresholds to manufacture discoveries. |

No gene-level conclusion would be presented if the corresponding proposed gate failed.

## 9. Proposed source-difference audit

The audit would cover both **scientific claims** and **computational revisions**.

### Evidence-to-plan ledger

Archive the supplied packet unchanged. Record each claim’s packet location, whether it is a source-summary statement or curator interpretation, its proposed implementation consequence, and remaining uncertainty.

The ledger would explicitly note that:

- The packet is not a quotation of the original DESeq2 source.
- The underlying read record is partial.
- Model support is source-grounded; exact implementation choices here are proposals.
- Missing source text cannot be treated as evidence of agreement.

If fuller source material later became available, compare the exact archived passages and revisions, distinguishing direct statements, interpretation, omission, contradiction, and terminology differences.

### Revision-difference ledger

For every change, retain:

`old_artifact_hash, new_artifact_hash, change_reason, author/date, affected_stage, expected_consequence, review_status`

Perform both file-level and semantic comparisons of:

- Sample additions, exclusions, relabelling, and allocation-unit changes.
- Reference/annotation versions and gene-ID mappings.
- Counts and feature eligibility.
- Design matrices, contrasts, normalization, testing, and FDR configuration.
- Code and environment versions.
- Proposed output differences: effect estimates, uncertainty, adjusted p-values, and discovery membership.

Distinguish changes caused by gene-universe remapping from changed statistical estimates. Hold the primary specification fixed when comparing revisions where feasible; otherwise state why comparisons differ.

**Final proposed deliverable:** an immutable input bundle, sample/allocation records, frozen specification, executable workflow, environment record, generated tables/plots, and discrepancy ledger. This would make a future analysis auditable while preserving the central limitation: reproducibility cannot compensate for absent independent treatment replication.
