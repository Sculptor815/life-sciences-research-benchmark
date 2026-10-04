# DeepSeek V4.1 Flash / inf-r02

Original final answer, shared by both scoring rounds.

## Recommended next biological question

**Which paired RNA–protein discordances at the single-cell level identify real, reproducible, perturbable cell states, and which are explained by modality-specific measurement noise or assay-visible surface-protein confounds?**  
A necessary companion is: **what calibrated integrated representation separates those possibilities?**

This is the most valuable next question from the packet because the packet establishes only that oligonucleotide-tagged antibodies can link selected surface-protein measurements and transcript measurements to the same single cells. It also states that the two measurements have complementary information and different noise/detection properties. The packet does **not** specify an optimal integrated representation and does **not** establish that all apparent RNA–protein disagreements define real cell states. Therefore the decisive gap is not simply “integrate RNA and protein,” but “validate which RNA–protein disagreements are biological.”

---

## 1. Evidence-to-inference-to-conclusion chain

**Evidence E1.** Oligonucleotide-tagged antibodies allow selected surface-protein measurements and transcript measurements to be linked to the same single cells.  
**Inference I1.** Paired RNA and protein observations can be obtained per cell, so cell-level discordance can be computed rather than inferred across separate populations.

**Evidence E2.** The two measurements can provide complementary information and have different noise and detection properties.  
**Inference I2.** Naive concordance, correlation, or log-ratio between RNA and protein will mix true biological coupling with modality-specific detection, background, dropout, and scaling effects. An RNA–protein disagreement is not automatically a biological state.

**Evidence E3.** The supplied result establishes joint measurement, but does not specify an optimal integrated representation or establish that all apparent RNA–protein disagreements define real cell states. No later integration algorithm or benchmark result is supplied.  
**Inference I3.** The unresolved question is calibration and validation: can a pre-specified integrated representation distinguish regulated RNA–protein decoupling from technical noise, and does that representation generalize across independent replicates?

**Conclusion C.** The strongest justified conclusion from the packet alone is: joint single-cell RNA–surface-protein measurement is possible, but the biological meaning of RNA–protein discordance is unestablished. The proposed next study should test whether reproducible discordant states exist and whether an integrated representation can separate them from noise. This is a proposal, not a reported result.

---

## 2. Competing mechanisms and discriminating predictions

Let a cell have transcript count \(R\) for a target gene and surface-protein count \(P\) for its encoded protein, measured jointly. Define discordance as a residual after accounting for RNA level, protein level, cell size, total counts, batch, and assay-specific detection.

| Mechanism | Biological/technical claim | Distinct predictions |
|---|---|---|
| **M1. Technical/statistical noise** | RNA and protein are measured with different noise; apparent discordance is mostly dropout, ambient RNA, antibody background, low counts, or normalization artifacts. | Discordance is not reproducible across technical aliquots or biological replicates; is explained by total counts, batch, ambient RNA, or cell size; does not predict functional state; permutation/null model reproduces the distribution. |
| **M2. Regulated post-transcriptional control** | RNA and protein are decoupled by translation efficiency, protein stability, trafficking, or degradation. | Discordance is reproducible across independent donors/batches; target-specific; changes in predicted direction after translation or proteasome perturbation; not explained by antibody clone alone. |
| **M3. Temporal/transient state** | RNA and protein reflect different time points in a dynamic response; RNA may lead protein. | Discordance correlates with time after stimulus; cross-correlation shows an RNA-to-protein lag; synchronization or time-course sampling collapses discordance. |
| **M4. Composition/normalization/cell-state scaling** | Both RNA and protein reflect cell size, cell-cycle, or global transcriptional state with different scaling. | Discordance disappears after size/total-count normalization or cell-cycle regression; correlates with total RNA, total protein, or cell-cycle score rather than target-specific regulation. |
| **M5. Surface-protein accessibility/occupancy confound** | Antibody measurement is affected by epitope masking, cleavage, internalization, secretion, or receptor occupancy. | Discordance is antibody-clone-dependent; associated with surface accessibility or cleavage markers; not mirrored by independent protein readout; can be real biology but confounds RNA–protein inference. |

**Key discriminator.** M1 predicts no reproducible cell-level structure after calibration. M2 predicts reproducible, target-specific, perturbation-sensitive discordance. M3 predicts time-dependent discordance with a measurable lag. M4 predicts normalization-dependent discordance. M5 predicts antibody/clone/accessibility dependence. These predictions are partly overlapping; the proposed design must include independent perturbation, technical replication, and orthogonal protein validation to separate them.

---

## 3. Proposed research plan

The following is a proposed protocol. The packet does not report platform, target genes, antibody tags, cell numbers, noise model, or integration method. Those are **unreported parameters** and must be specified before execution. Do not treat any proposed result as observed.

### Phase 0. Preregistration and assumptions

**Prerequisites**

1. A biological system with at least one selected surface protein whose encoding transcript is detectable at single-cell level and whose protein can be perturbed independently of transcription.
2. Validated oligonucleotide-tagged antibodies against the target surface protein, plus an isotype control with a matched oligonucleotide tag.
3. A joint single-cell workflow that preserves pairing of antibody-derived and transcript-derived measurements in the same cell.
4. Enough cells per condition to estimate cell-level discordance and enough independent donors/wells/batches to estimate reproducibility.
5. Pre-registered primary endpoint, thresholds, and analysis code.

**Assumptions that must be verified, not assumed**

- Antibody signal is specific to the target.
- Transcript counts are not dominated by ambient RNA.
- Technical replicates can be generated from the same cell suspension.
- Independent biological replicates exist.
- Perturbations affect protein level or localization without destroying cell viability.

**Unreported parameters to document before start**

Platform; target gene/protein; antibody clone and tag; number of cells; sequencing depth; protein count distribution; negative-control distribution; batch structure; donor/well allocation; pre-specified QC thresholds.

---

### Phase 1. System and target selection

**Proposed design**

Select at least three surface-protein targets with different known or hypothesized regulatory modes:

- One target expected to be tightly RNA–protein coupled.
- One target with known post-transcriptional regulation or protein stability control.
- One target with surface cleavage, internalization, or occupancy biology.

If only one target is available from the packet, the study is still possible but weaker; the conclusion would be target-specific, not general.

**Rationale**

A single target cannot distinguish target-specific regulation from global scaling or antibody artifact. Multiple targets with different biology allow internal replication and negative/positive control logic.

---

### Phase 2. Calibration

**Purpose**

Estimate detection limits, background, overdispersion, and the null distribution of RNA–protein discordance under no real biological decoupling.

**Calibration steps**

1. **Antibody titration.** Test 8-point dilution series on target-positive and target-negative cells. Choose a concentration where target signal is clearly separated from isotype and not saturated.
2. **Isotype and no-antibody controls.** Measure background oligo-tag counts. Require isotype signal to be below a pre-specified threshold and separable from target.
3. **RNA spike-in calibration.** If the platform permits spike-in RNA, use known ratios to estimate capture efficiency and limit of detection.
4. **Joint spike-in cells.** If available, use cells or beads with known fixed RNA/protein ratios across dilution series to fit measurement-specific noise.
5. **Technical replicate calibration.** Split the same cell suspension into 4–8 aliquots. Process in parallel. Compute intraclass correlation (ICC) of RNA, protein, and discordance scores across aliquots.
6. **Null calibration.** Permute RNA and protein labels within batch or use negative-control pairs to estimate the distribution of discordance under no true coupling. This null is essential because the packet explicitly notes different noise/detection properties.

**Calibration gate**

Proceed only if:

- Target antibody signal is separable from isotype.
- Technical replicate ICC for RNA and protein exceeds a pre-specified minimum.
- Spike-in recovery and background are within pre-specified limits.

If calibration fails, stop and optimize assay before biological inference.

---

### Phase 3. Design, independent units, allocation, and blinding

**Independent units**

- For technical noise: aliquots, wells, or capture lanes.
- For biological inference: donors, independent differentiations, litters, or independent experimental batches.
- Cells are nested within these units and are not independent for condition-level inference.

**Allocation**

- Randomize condition, time point, and perturbation to wells/lanes.
- Randomize antibody tag and staining order across wells.
- Balance batches so condition is not confounded with batch.
- Include bridge samples across batches.
- Pre-register sample size and primary comparison.

**Blinding**

- Analysts performing QC and primary analysis are blinded to condition labels where possible.
- Functional validation (e.g., imaging, flow, or independent protein assay) is scored blinded to RNA–protein discordance classification.
- Perturbation identity is unblinded only after discordance scores are locked.

---

### Phase 4. Data generation and controls

**Measurements per cell**

- Target transcript counts.
- Target surface-protein counts from oligonucleotide-tagged antibody.
- Isotype/no-antibody background counts.
- Total RNA counts and total protein/antibody counts.
- Cell size, viability, cell-cycle score, mitochondrial fraction.
- Ambient RNA estimate.
- Batch, well, donor, time, perturbation, antibody lot, tag.

**Controls**

- **Positive:** target-positive cells, induced/repressed target, spike-in control.
- **Negative:** target-negative cells, isotype antibody, no-antibody, empty droplets, target knockout/knockdown if available.
- **Technical:** split-sample aliquots; repeated staining; repeated sequencing lanes.
- **Biological:** independent donors or independent differentiations.
- **Perturbation:** vehicle, translation inhibitor, proteasome inhibitor, transcription inhibitor, and time-course sampling.
- **Batch:** bridge samples and randomized batch assignment.

---

### Phase 5. QC and preprocessing

**Proposed QC**

- Remove empty droplets, doublets, low-quality cells, and cells with extreme total counts.
- Estimate and subtract ambient RNA using negative-control or empty-droplet information.
- Flag cells with high isotype protein counts.
- Retain cells with detectable target transcript and/or protein above calibrated limits.

**Caution**

Do not filter on the discordance score itself before primary analysis, because that would bias the test. Discordance should be computed after pre-specified QC only.

---

### Phase 6. Integrated representation and noise calibration

The packet does not supply an optimal integration algorithm. Therefore the proposed study should benchmark pre-specified representations, not assume one is correct.

**Candidate representations**

1. **Naive log-ratio:** \(\log(1+P) - \log(1+R)\). Simple but likely confounded by scaling and noise.
2. **Regression residual:** regress protein on RNA, total counts, cell size, batch, and sex/cell-cycle covariates; use residual as discordance.
3. **Hierarchical latent-variable model:** model RNA and protein counts with separate observation models and a shared latent biological state:
   \[
   R_i \sim \text{NB}(\lambda^R_i), \quad P_i \sim \text{NB}(\lambda^P_i)
   \]
   \[
   \log \lambda^R_i = f_R(z_i, x_i), \quad \log \lambda^P_i = f_P(z_i, x_i, s_i)
   \]
   where \(z_i\) is latent biological state and \(s_i\) captures surface accessibility. Discordance is the residual not explained by \(z_i\), \(x_i\), or \(s_i\).
4. **Rank/quantile representation:** compare within-batch ranks to reduce global scaling effects.

**Benchmark metrics**

- Reproducibility across technical aliquots (ICC).
- Reproducibility across independent biological replicates.
- Calibrated false-discovery rate against permutation/null.
- Cross-batch and cross-donor transfer.
- Prediction of perturbation labels (AUROC).
- Stability under normalization choices.

**Primary endpoint**

Pre-specify one metric, for example: ICC of the discordance score across independent biological replicates, with a calibrated FDR < 0.05.

---

### Phase 7. Biological validation and perturbation

**Perturbation logic**

If discordance reflects regulated post-transcriptional control (M2), then:

- Translation inhibition should reduce protein without proportional RNA loss.
- Proteasome inhibition should increase protein without proportional RNA increase.
- Transcription inhibition should reduce RNA first, then protein.
- Effects should be target-specific and reproducible.

If discordance is technical noise (M1), perturbations should not produce a coherent, reproducible discordance shift beyond the null.

If discordance is temporal (M3), time-course sampling should show an RNA-to-protein lag and discordance should correlate with time since stimulus.

If discordance is surface accessibility (M5), antibody clone or accessibility treatment should change it without matching independent protein changes.

**Orthogonal validation**

Use an independent protein readout where possible, e.g., flow cytometry, immunofluorescence, or mass-spectrometry-based surface protein measurement. The packet does not specify these, so they are proposed orthogonal methods, not reported author methods.

---

### Phase 8. Independent replication

Repeat the full pipeline in:

- A second independent donor or differentiation.
- A second batch.
- A second antibody lot if available.

Pre-specify that positive claims require replication in at least one independent biological unit and one independent batch. If the effect appears only in one donor or one antibody lot, it is ambiguous or target-specific.

---

### Phase 9. Analysis and decision rules

**Statistical model**

Use mixed-effects or hierarchical models with random effects for donor, batch, well, and aliquot. Treat cells as nested observations. For condition-level inference, use pseudobulk or mixed models; do not treat thousands of cells as independent biological replicates.

**Analysis steps**

1. Lock preprocessing and QC.
2. Fit candidate integrated representations on training batches.
3. Compute discordance scores on held-out batches.
4. Calibrate FDR using permutation/null.
5. Estimate ICC across technical and biological replicates.
6. Test association with perturbation, time, cell size, cell cycle, and surface accessibility.
7. Compare representations on pre-specified metrics.
8. Report effect sizes with uncertainty intervals.

**Stop rules**

- **Calibration failure:** if isotype signal overlaps target or spike-in CV exceeds threshold, stop.
- **Power failure:** if technical replicate ICC for discordance is below pre-specified minimum, stop.
- **Confounding failure:** if condition is confounded with batch or donor, stop or re-randomize.
- **Futility:** if after independent replication the null model explains discordance and no perturbation effect is detected, conclude negative.
- **Success:** if discordance is reproducible across independent biological replicates, calibrated FDR is controlled, and perturbation effects match M2/M3 predictions, conclude positive.
- **Ambiguity:** if effects are target-specific, batch-specific, or explained by surface accessibility but not by independent protein readout, conclude ambiguous.

**Troubleshooting**

| Problem | Proposed action |
|---|---|
| Low protein counts | Titrate antibody, increase cell number, optimize staining, use brighter tag if available. |
| High ambient RNA | Add DNase/washes, use empty-droplet correction, validate with negative cell types. |
| High isotype background | Optimize blocking, wash, antibody concentration, Fc receptor block. |
| Epitope masking | Test alternative antibody clone, compare surface accessibility conditions, use knockout control. |
| Batch effects | Randomize, include batch random effects, use bridge samples, analyze within batch. |
| RNA dropout | Increase sequencing depth, use targeted probes, require housekeeping detection. |
| Discordance not reproducible | Check technical ICC; if low, discordance is likely noise; do not interpret biologically. |

---

## 4. Conditional positive, negative, and ambiguous outcomes

### Positive outcome

**Observation pattern.** Discordance is reproducible across independent donors, batches, and technical aliquots; calibrated FDR is controlled; perturbation of translation or protein stability changes discordance in the predicted direction; an independent protein readout supports the protein assignment; the integrated representation outperforms naive log-ratio on pre-specified metrics.

**Strongest justified conclusion.** At least some RNA–protein disagreements define real regulated cell states, consistent with post-transcriptional control or temporal regulation. The optimal integrated representation should be measurement-noise-aware and calibrated, not a naive RNA–protein ratio. This would extend the packet’s joint-measurement result into a validated biological interpretation.

### Negative outcome

**Observation pattern.** Discordance is not reproducible across technical or biological replicates; permutation/null explains the distribution; perturbation produces no coherent effect; discordance disappears after controlling for total counts, cell size, batch, or ambient RNA.

**Strongest justified conclusion.** In the tested system, apparent RNA–protein disagreements are not established as real cell states. They are consistent with modality-specific noise and detection differences. The packet’s warning that not all disagreements define real states would be supported. Naive discordance should not be interpreted biologically without calibration.

### Ambiguous outcome

**Observation pattern.** Discordance is reproducible for some targets or conditions but not others; it is confounded with cell cycle, size, or surface accessibility; perturbation effects are small or target-specific; cross-batch transfer fails.

**Strongest justified conclusion.** RNA–protein discordance is a mixture of real and artifactual components. No global claim that “all discordance is biological” or “all discordance is noise” is justified. Target-specific calibration and orthogonal validation are required. The next question becomes which target classes and which regulatory mechanisms produce validated discordant states.

---

## 5. Limits and what would change the recommendation

**Limits from the packet.** The evidence covers selected surface proteins, not the whole proteome. It does not specify platform, target genes, noise model, cell numbers, integration algorithm, or benchmark. Therefore any claim about “all apparent RNA–protein disagreements” is unsupported. The proposed plan is an independent attempt and has no prior feedback.

**What would change the recommendation.**

- If a later integration algorithm or benchmark were supplied and validated, the next question could shift from “can discordance be validated?” to “which specific discordant states are functional?”
- If calibration shows protein detection is too noisy, the priority becomes assay improvement before biological inference.
- If perturbations are unavailable, the study becomes observational and weaker; temporal or orthogonal protein validation becomes more important.
- If only one target is available, conclusions must be target-specific.

**Bottom line.** The most valuable next biological question is whether joint single-cell RNA–surface-protein discordance identifies real regulated states or only measurement noise. The proposed plan is a calibrated, replicated, perturbation-aware test with pre-specified stop rules. A positive result would validate selected discordant states and an integrated representation; a negative result would show that apparent disagreements should not be over-interpreted; an ambiguous result would show that discordance is a mixture requiring target-specific and context-specific validation.
