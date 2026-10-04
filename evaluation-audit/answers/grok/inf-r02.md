# Grok 4.7 / inf-r02

Original final answer, shared by both scoring rounds.

The most valuable next biological question is not which integration algorithm is optimal. It is whether apparent disagreements between a selected surface protein and its cognate transcript, measured in the same cell, are reproducible biological residuals after modality-specific detection limits and antibody background are accounted for, and, if so, whether those residuals behave as time- or regulation-lagged offsets or as discrete cell states.

Do not choose or deploy an integrated representation that treats RNA–protein conflict as a cell state until that discrimination is done. Joint measurement is already established; interpretability of disagreement is not.

## Evidence → inference → conclusion

**Reported (packet only).**
1. Oligonucleotide-tagged antibodies allow selected surface-protein measurements and transcript measurements to be linked to the same single cells.
2. The two measurements can provide complementary information and have different noise and detection properties.
3. The supplied result establishes joint measurement, but does not specify an optimal integrated representation and does not establish that all apparent RNA–protein disagreements define real cell states.
4. No later integration algorithm or benchmark result is supplied.

**Inference.** Because linkage is already shown, repeating a proof of co-measurement is not the highest-value next question. Because noise and detection differ, a cell that is high in one modality and low in the other is not, by itself, evidence of a biological state. Because no integration method or benchmark is supplied, selecting a representation now would optimize an undefined target and could encode technical structure as biology or erase a real residual as noise. Complementarity does not imply that every discordant cell is a new state; it only implies that the modalities are not redundant in principle.

**Conclusion that follows now.** The unresolved biological question is the mechanism of apparent disagreement, stratified by feature and context. An integrated representation is a downstream, conditional product of that answer, not the next experiment’s primary endpoint.

**What would change this recommendation.** A supplied benchmark with an external biological ground truth would make representation testing co-equal. Evidence that disagreements had already been shown to be real states would move the next question to regulatory mechanism or to representation. Evidence that per-cell linkage itself failed would move the next question back to measurement validity. None of those results are in the packet.

## Unresolved biological question

For jointly measured, pre-specified pairs of selected surface proteins and cognate transcripts: after calibration for modality-specific detection limits, background, and batch, which apparent disagreements remain in independent biological replicates, and do those residuals match a temporal or regulatory-offset model, a discrete protein-resolved state model, or neither?

Scope limits inherited from the packet: “selected” surface proteins only; surface protein is not total protein; no claim is available that all disagreements are states; no author integration method is available to adopt or refute.

## Competing mechanisms and distinct predictions

These mechanisms can co-occur across features. The experiment must classify pairs, not force one global winner.

**M1 — Detection-limit or dropout discordance (technical).** One modality is below its detection curve while the other is counted.  
Prediction: disagreements concentrate near the depth-dependent detection boundary; subsampling high-confidence double-positive cells recreates the observed single-positive rates; donor-level excess disagreement is compatible with zero after the noise model is fit on calibration data only.

**M2 — Antibody, oligo-tag, or ambient artifact (technical).** Protein-tag counts reflect nonspecific binding, isotype background, ambient antibody, or tag misassignment rather than epitope abundance.  
Prediction: protein-positive/RNA-negative signal is recapitulated by negative-control tags and by cells that lack the epitope by an orthogonal assay; it is not removed by deeper transcript sequencing; it tracks antibody dose or blocking if those controls are run.

**M3 — Temporal or regulatory offset (biological, not a stable extra state).** Transcription, protein accumulation, surface localization, and decay are offset in time. The same cell can be RNA-high/protein-low or the reverse without belonging to a discrete lasting state.  
Prediction: only a time- or perturbation-ordered design can support this. The lead–lag order is feature-specific and repeats across independent biological sources; a static cluster label fit in one time window does not reproduce at other times once depth and background are matched. Cross-sectional data alone cannot confirm M3.

**M4 — Discrete state visible in surface protein but not redundant with the cognate transcript (biological).**  
Prediction: residual groups remain after M1/M2 calibration, replicate across independent biological sources rather than batches, and are separated by a pre-specified orthogonal measurement that was not used to define the groups. A pure lag model fits worse than a state model if a time axis exists.

**M5 — Complementary but concordant information with different scaling (no true conflict).**  
Prediction: after a monotone, calibration-set-only mapping, rank concordance is high; residual quadrant calls match the noise model; neither modality’s unique clusters survive negative controls. Complementarity may still improve a pre-specified external prediction without any disagreement being a state.

**Discriminators that are not interchangeable.** Depth subsampling separates M1 from M4 only if double-positive cells are abundant enough to subsample. Isotype or epitope-negative controls separate M2 from M4. A time axis separates M3 from M4. Donor-level replication separates stable biology from batch. An orthogonal assay separates a protein-resolved state from a tag artifact. Missing any one of these leaves the corresponding pair of mechanisms confounded.

## Alternatives considered and rejected as the primary next question

- **Optimal integrated representation.** Premature. No benchmark is supplied, and the packet explicitly does not establish that disagreements are states. Representation comparison is included only as a locked secondary analysis.
- **Which modality is less noisy.** The packet already states that noise and detection differ. Estimating those curves is a calibration prerequisite, not the biological question.
- **Panel expansion or biomarker discovery.** Not supported by any clinical or comprehensive-panel result in the packet. Scaling before classification would multiply uninterpreted disagreements.

## Proposed research plan

All steps below are **proposals**. No author method is implied. No outcome below has been observed. Parameters marked **unreported** are absent from the packet and must be measured or locked as assumptions before inference.

### 0. Prerequisites and scope lock

1. Write a one-page protocol freeze before any disagreement clustering: biological sources, feature pairs, primary estimand, exclusion rules, and the Stage B go/no-go rule.
2. **Unreported and required before biology:** organism or cell system, which selected surface proteins, which cognate transcripts, antibody clones, tag chemistry, transcript-count chemistry, and sequencing depth. Do not invent these from outside the packet.
3. Include only pairs declared before inspection. Split them into a primary set (confirmatory) and an exploratory set. Do not promote exploratory pairs after seeing residuals.
4. Treat per-cell linkage as a supplied capability that still requires experiment-specific verification. Linkage in the packet is not a QC result for a new run.
5. Choose biological sources that can yield **independent units** (donors, animals, or independent differentiations). Cells from one suspension are not independent biological replicates.
6. If no perturbation or time course can be justified for the chosen system, state in the freeze that M3 cannot be tested. Do not infer lag from a single cross-section.

**Assumption (planning, not data):** a pilot of 3 independent biological sources can estimate the donor-level variance of excess disagreement before the confirmatory sample size is locked. Illustrative size formula, not a result: for a two-sided test of mean excess disagreement versus 0 at α = 0.05 and 80% power, n ≈ 7.84 σ²/δ². If the smallest effect worth acting on is δ = 0.10 and pilot σ ≈ 0.10, n ≈ 8 sources; if σ ≈ 0.15, n ≈ 18. Replace these placeholders with pilot estimates. If the pilot cannot be done, the confirmatory claim is limited to description.

### 1. Ordered experimental phases

**Phase A — Calibration, locked on non-outcome samples.**  
Purpose: estimate detection and background before any biological contrast.

**Phase B — Multi-source cross-section.**  
Purpose: test whether excess disagreement survives M1/M2 and replicates across independent sources (M4/M5 versus technical).

**Phase C — Time or perturbation axis, conditional.**  
Purpose: separate M3 from M4 only for pairs that pass Phase B stop rules. Do not start Phase C to rescue a null Phase B.

**Phase D — Secondary representation comparison, conditional.**  
Purpose: among pre-specified representations, ask which preserves calibrated biological residuals and does not create clusters from negative-control tags. This does not establish a universally optimal integration; none is supplied.

### 2. Calibration and controls

Proposed controls, not reported author methods:

- **Negative-control tags:** isotype or otherwise non-targeting oligonucleotide-tagged antibodies carried through the same staining and counting path.
- **Epitope-negative biological controls,** if obtainable without altering the scientific target: cells lacking the epitope by genotype or by a pre-specified orthogonal stain. If unavailable, record M2 as only partly testable.
- **Positive concordance controls:** pre-specified pairs expected, on independent grounds locked before this experiment, to be jointly detectable. Those grounds are **unreported** here; if they cannot be stated without circular use of the same joint assay, drop the pair from the positive-control set.
- **Ambient and empty-droplet profiles** from the same runs, used only to set background.
- **Bridge sample:** one aliquoted control suspension in every batch and lane.
- **Technical split:** each biological suspension divided into at least two independent loadings or library batches.
- **Depth curve:** computational subsampling of transcript and protein-tag counts from double-positive calibration cells. This is an analysis control, not extra wet-lab depth unless the subsample leaves too few cells (see troubleshooting).
- **Optional orthogonal protein measure** on held-out aliquots (different clone or flow cytometry). Proposal only. Do not treat it as already performed.

**Threshold lock.** On calibration data only, with biological group labels stripped, set:

- transcript detected if count ≥ t_R(feature, library depth);
- protein-tag detected if count ≥ t_P(feature, depth, negative-control distribution).

Record the date and a checksum of the threshold file. Do not retune thresholds after viewing biological disagreements.

### 3. Allocation, blinding, and independent units

- **Independent biological unit:** source (donor, animal, or independent differentiation). Primary inference uses source-level summaries.
- **Technical units:** staining batch, loading or emulsion replicate, library batch, sequencing lane. These are nuisance factors, not biological n.
- **Allocation:** randomize sources to staining batches and lanes so that batch is not nested inside a biological contrast. Balance bridge samples across batches. If a source yields too few cells, pre-specify exclusion rather than pooling silently with another source.
- **Blinding:** the analyst who fits noise models and thresholds receives calibration matrices without biological labels. A second analyst applies the locked thresholds to biological cells. Orthogonal-assay readers, if used, are blinded to single-cell quadrant calls.
- **Cell-level randomization** inside a droplet assay is not assumed possible. Do not claim it.

### 4. Measurements and operational definitions

Per cell, record at least: cognate transcript count, matching protein-tag count, negative-control tag counts, total transcript counts, total protein-tag counts, and any doublet or ambient score the assay yields. Exact count chemistry is **unreported**; analyze the count representation the assay actually emits, and state it in the report.

**Proposed definitions (not observed results):**

- Quadrants after locked thresholds: RNA+protein+, RNA+protein−, RNA−protein+, RNA−protein−.
- Apparent disagreement: RNA+protein− or RNA−protein+.
- Continuous residual: protein-tag rank or calibrated expectation minus the value predicted from transcript level by a mapping fit on calibration cells only.
- **Primary estimand:** source-level excess disagreement fraction (EDF) = observed disagreement rate minus the rate predicted by the locked noise model, computed within source, then summarized across sources. Report RNA+protein− and RNA−protein+ separately; they implicate different mechanisms.
- **Secondary estimands:** source-level correlation of residuals; batch variance component; orthogonal-assay concordance; Phase C lead–lag; Phase D held-out predictive score.

Pre-specify cell exclusion (failed linkage, extreme total counts, doublet call) and apply it before quadrant counts. Also report a sensitivity analysis with the doublet filter removed, because doublets can manufacture mixed-modality calls.

### 5. Analysis order

1. Verify linkage and bridge-sample stability. If this fails stop rules, stop.
2. Fit the noise and background model on calibration cells only. Freeze it.
3. Apply frozen thresholds to biological cells. Do not refit on those cells.
4. Compute source-level EDFs for primary pairs.
5. Variance components: source versus batch versus technical split. The confirmatory test is across sources.
6. **M1 check:** compare observed single-positive rates with rates from depth-matched subsampling of double-positive cells.
7. **M2 check:** compare RNA−protein+ rates with negative-control tags and epitope-negative controls, using the same thresholds.
8. **M5 check:** after the locked monotone map, test whether residual EDF is compatible with zero.
9. **M4 check (only if EDF remains):** stability of residual groups across sources, and separation by the pre-specified orthogonal measurement.
10. **M3 check (Phase C only):** feature-specific lead–lag across the pre-specified time grid; compare predictive fit of lag versus static state on held-out sources.
11. Multiplicity: confirmatory claims only for the primary pair list. Exploratory pairs are labeled exploratory even if extreme.
12. Report effect sizes and intervals for source-level EDF, not cell-level p-values as the primary evidence. Cell counts describe precision within source; they are not the sample size for biology.

**Phase D candidates, pre-specified, none claimed optimal:** (i) concatenated calibrated features; (ii) a joint factor model with explicit modality-specific noise; (iii) transcript-primary embedding with protein residual as annotation. Locked selection rule: better held-out prediction of an orthogonal label not used in training, and no spurious grouping of negative-control tags. If no orthogonal label exists, do not declare a winner.

### 6. Stop rules

- **Stop before biological interpretation** if per-cell linkage fails in the bridge sample at a pre-registered rate, if positive-control pairs do not show joint detection above the noise model, or if target protein-tag distributions are indistinguishable from negative-control tags.
- **Do not open Phase C** if every primary pair has source-level EDF whose interval includes zero after M1/M2 calibration.
- **Do not claim a stable state** if batch or lane explains more source-level residual variance than biological source, or if the orthogonal assay does not separate the groups.
- **Do not declare an optimal representation** if Phase D criteria are unmet or if Phase B did not leave a biological residual to preserve.
- **No post-hoc feature addition** to the confirmatory list. New pairs require a new freeze.
- **Sample-size adaptation** is allowed once, after the pilot variance estimate, and only for the already frozen primary estimand.

### 7. Troubleshooting (decision paths, not results)

- **High RNA−protein+ resembling isotype tags:** treat as M2 until antibody titration, blocking, or epitope-negative controls say otherwise. Do not integrate that protein as a state marker.
- **High RNA+protein− only at low transcript depth:** favor M1. If it persists in the upper depth quartile and in technical splits, leave it as a residual and do not force an M1 label.
- **Discordance only in one batch:** do not pool. Repeat the bridge sample. If it does not repeat, the finding is technical.
- **Doublet-sensitive disagreements:** report both filters. If the biological claim depends on one filter, the result is ambiguous.
- **Too few double-positive cells to subsample:** M1 cannot be simulated directly. Either increase depth in a dedicated calibration run or mark M1 as unresolved for that pair.
- **Orthogonal assay disagrees with the protein tag:** trust is not automatic for either assay. Classify the pair as ambiguous and withhold both a state claim and a representation that depends on that protein.
- **Phase C order reverses across sources:** do not average to a single lag story. M3 is not supported for that pair.

## Conditional outcomes and the strongest justified conclusion

**Positive for a technical account (M1/M2/M5).** Source-level EDF intervals include zero; subsampling and negative controls recreate apparent disagreements; no orthogonal separation.  
**Strongest conclusion:** in this system and this locked panel, apparent RNA–protein disagreements are accounted for by measured detection limits and background. They do not justify new cell-state claims. Complementary information may still exist as calibrated, concordant signal (M5), but that is a separate, pre-specified prediction test, not a disagreement result. This does not prove that all disagreements in all systems are technical.

**Positive for a biological residual, mechanism still open.** EDF remains after locked M1/M2 calibration and replicates across sources, but Phase C was not run or was underpowered, or the orthogonal assay was not done.  
**Strongest conclusion:** those pairs show reproducible disagreement beyond the calibrated noise model. That is not yet evidence of a discrete cell state, not yet evidence of regulatory lag, and not a license to treat every discordant cell as a state in an integrated map.

**Positive for temporal offset (M3).** Phase B residual exists; Phase C lead–lag repeats across held-out sources; a static state label does not.  
**Strongest conclusion:** for those pairs, disagreement is consistent with ordered regulatory or surface-display offset rather than an additional stable state. Half-lives and trafficking rates are **unreported** here; do not invent them to decorate the conclusion.

**Positive for a protein-resolved state (M4).** Residual groups replicate across sources, are not explained by batch, depth simulation, or negative tags, and are separated by the blinded orthogonal measurement; if Phase C was run, a pure lag model fits worse.  
**Strongest conclusion:** for those pairs, surface-protein signal resolves a reproducible biological distinction that is not redundant with the cognate transcript under the tested conditions. This still does not establish that all apparent disagreements are states, and it does not name an optimal global integration method.

**Ambiguous.** Residuals in a subset of pairs, batch-limited signals, orthogonal disagreement, or Phase C instability.  
**Strongest conclusion:** mechanism unresolved for the affected pairs. Do not deploy an integration that encodes all disagreements as states. Report pair-level uncertainty. A representation may still be used for concordant features that passed calibration, with discordant pairs held out or down-weighted by the locked noise model.

**Phase D outcomes, always secondary.** A candidate wins only on the locked external criterion and only if negative-control tags do not form state-like groups. A win is a conditional operating choice for this panel, not the optimal integrated representation the packet says is unspecified. If candidates tie or the external label is missing, the justified conclusion is that representation optimality remains open.

## Assumptions, unreported parameters, and limits

**Assumptions to label in any report:** source-level exchangeability after batch balancing; thresholds transported from calibration to biological cells; cognate transcript–protein pairing is correctly specified; surface-tag counts are the intended protein measurement and not a different epitope or cleavage product unless tested.

**Unreported in the packet and not to be filled in as if known:** panel identity, clones, count chemistry, depth, donor number, batch structure, author QC thresholds, author integration algorithm, any benchmark score, protein half-lives, and any claim that disagreements were already shown to be real.

**Limits.** Results apply only to the locked selected proteins and system. Surface localization can disagree with total protein for reasons this design does not measure unless an orthogonal total-protein assay is added. Failure to reject M1 is not proof of biology. A significant cell-level test with one source is not a biological replication. Mixed mechanisms within a pair can produce an ambiguous EDF even when each mechanism is real. No proposed result in this plan should be cited as observed.
