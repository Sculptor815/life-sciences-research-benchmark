# Claude Opus 4.6 / inf-r02

Original final answer, shared by both scoring rounds.

# Proposed Next Biological Question, Competing Mechanisms, and Research Plan

---

## 1. Unresolved Biological Question

**Do single cells that show discordant RNA and surface-protein abundance for the same gene occupy functionally distinct biological states, or do most such discordances arise from measurement-specific noise and detection characteristics?**

### Rationale for prioritizing this question
The supplied evidence establishes that (i) oligonucleotide-tagged antibodies permit joint surface-protein and transcript readouts per cell, (ii) the two modalities differ in noise structure and detection sensitivity, and (iii) it is not yet established whether apparent RNA–protein disagreements define real cell states. Resolving this question is the highest-value next step because every downstream use of the technology—cell-type classification, trajectory inference, regulatory-state discovery—depends on knowing which discordances carry biological information and which are technical artifacts. Without this knowledge, any integration algorithm risks either discarding real biology or amplifying noise.

---

## 2. Competing Mechanisms and Distinct Predictions

### Mechanism A: Biological discordance (post-transcriptional regulation)
RNA and protein levels can genuinely decouple through translational regulation, differential mRNA/protein half-lives, microRNA-mediated repression, or active protein trafficking and shedding. Under this mechanism, a cell with high mRNA but low surface protein for a given marker occupies a transiently regulated state that is distinct from a cell concordant on the same marker.

**Predictions under Mechanism A:**
- A-1. Discordant cells will cluster reproducibly across independent biological replicates (same donor, same tissue, different library preparations).
- A-2. Discordant cells will show coherent differential expression of known post-transcriptional regulators (e.g., genes encoding RNA-binding proteins, miRNAs targeting the discordant gene, ubiquitin-ligase pathway members for the protein).
- A-3. Discordant cells, if sorted and re-assayed after a defined time interval, will resolve the discordance in a directional manner (e.g., protein catches up to RNA, or RNA is silenced), consistent with a transient regulatory state.
- A-4. The magnitude and direction of discordance will differ systematically between cell types or stimulation conditions in a manner not explained by technical covariates alone.

### Mechanism B: Technical artifact (noise-driven discordance)
Because antibody-derived tag (ADT) counts and mRNA UMI counts have different capture efficiencies, dynamic ranges, background levels, and dropout rates, a fraction of cells will appear discordant purely by chance. Protein detection by ADT is often more sensitive for surface markers (lower dropout) whereas mRNA detection suffers from higher dropout; the two signals may also saturate at different points.

**Predictions under Mechanism B:**
- B-1. Discordant cells will not cluster reproducibly; their identities will shuffle across technical replicates from the same biological sample.
- B-2. The proportion of discordant cells will correlate with technical quality metrics (library size, mitochondrial fraction, ambient RNA contamination score) rather than with biological covariates.
- B-3. After spike-in of cells at known protein/RNA states (see calibration below), observed discordance rates will match those predicted by a noise model parameterized on the spike-in data.
- B-4. Discordant cells will show no coherent pathway enrichment beyond what is expected by random gene-set sampling at matched expression depth.

### Mechanism C: Mixed (both mechanisms contribute)
A subset of discordances is biological, embedded in a larger background of technical discordance. Under this mechanism, predictions A-1 through A-4 hold for a reproducible minority of discordant cells, while predictions B-1 through B-4 hold for the remainder. The key discriminating observation is the fraction of discordant cells that are reproducible across replicates and the magnitude of pathway enrichment after technical confounders are regressed out.

---

## 3. Detailed, Ordered Research Plan

### 3.1 Prerequisites

| Requirement | Justification |
|---|---|
| Access to oligonucleotide-tagged antibody panel (≥ 15 surface markers spanning receptors with known translational regulation, e.g., CD69, PD-1/PDCD1, CD25/IL2RA) | Must include markers where post-transcriptional regulation is documented so that true biological discordance has a plausible mechanistic basis |
| Primary human PBMCs from ≥ 3 healthy donors | Biological replicates; donor is the independent unit for generalizability |
| Stimulation reagent (e.g., anti-CD3/CD28 beads) | Creates a dynamic system where post-transcriptional regulation is active, increasing the expected frequency of biologically discordant cells |
| Single-cell platform capable of joint RNA + ADT capture (e.g., droplet-based system with feature-barcoding) | Established in the supplied evidence; no new technology development required |
| Spike-in calibration reagents: cell line with stable, known surface-protein expression (e.g., Jurkat) | Needed to parameterize the technical noise model (Section 3.3) |

### 3.2 Experimental Design: Independent Units, Allocation, and Blinding

**Independent biological units:** Donors (n = 3 minimum for biological conclusions; power analysis below).

**Technical replicates:** For each donor × condition, prepare two independent library preparations from the same cell suspension (split after staining). This is critical for testing prediction A-1 vs. B-1.

**Conditions per donor:**
- Unstimulated PBMCs (resting; expected low discordance)
- Anti-CD3/CD28-stimulated PBMCs at 4 h (early activation; mRNA upregulated, protein may lag)
- Anti-CD3/CD28-stimulated PBMCs at 24 h (later activation; protein expected to catch up)

**Total libraries:** 3 donors × 3 conditions × 2 technical replicates = 18 libraries.

**Target cells per library:** 5,000 cells (total ~90,000 cells), balancing cost against statistical power for detecting a reproducible discordant subpopulation comprising ≥ 5 % of cells within a given cell type (see power note below).

**Blinding:** Library preparation and sequencing should be performed by an operator blinded to condition labels. Computational analysis should be performed on de-identified sample IDs; condition labels merged only after primary clustering and discordance calling are complete.

**Randomization:** Library preparation order randomized across conditions and donors. Sequencing lanes assigned by block randomization (each lane contains one library from each condition) to prevent lane effects from confounding condition effects.

### 3.3 Calibration Step: Technical Noise Model

**Purpose:** Establish the expected discordance rate attributable solely to technical noise, against which biological discordance can be tested.

**Procedure:**
1. Spike Jurkat cells (or another cell line with stable, homogeneous expression of selected markers) into each library at ~5 % of total cell input. These cells should be tagged with a distinct hashtag oligo so they can be computationally identified.
2. For each marker, quantify the variance of ADT counts and mRNA UMI counts across the spike-in cells. Because these cells are clonal and in a steady state, essentially all observed variance is technical.
3. Fit a bivariate noise model (e.g., bivariate negative binomial or Poisson-lognormal) to the spike-in joint distributions, separately for each marker.
4. Use this model to compute, for each marker, the expected fraction of cells that would appear "discordant" (defined as falling outside the 95 % joint confidence region) purely by technical noise.
5. Compare observed discordance rates in primary PBMCs against this null expectation. Excess discordance is the candidate biological signal.

**Critical control:** If the spike-in discordance rate is already very high for a given marker, that marker should be flagged as technically unreliable and excluded from biological interpretation.

### 3.4 Measurements

**Primary measurements per cell:**
- mRNA UMI count matrix (genome-wide transcriptome)
- ADT count vector (panel of surface proteins)
- Hashtag oligo counts (for demultiplexing and spike-in identification)

**Quality-control metrics per cell:**
- Total UMI count (RNA library size)
- Number of detected genes
- Mitochondrial transcript fraction
- Total ADT count
- Ambient RNA contamination score (e.g., estimated from empty droplets)
- Doublet probability score

**Derived per cell, per marker:**
- Discordance score: residual of observed protein level after regressing on RNA level within a cell type, normalized to the spike-in-derived noise expectation. A cell is "discordant" if its residual exceeds the 95th percentile of the spike-in null for that marker. Direction of discordance (RNA-high/protein-low vs. RNA-low/protein-high) is recorded.

### 3.5 Analysis Plan (ordered)

**Step 1. Quality control and filtering.**
Remove cells with extreme QC metrics (bottom/top 2.5 % of library size within each sample, >15 % mitochondrial reads, predicted doublets). Remove markers with <20 % detection rate in the spike-in cells (technically unreliable).

**Step 2. Normalization.**
- RNA: Scran-type pooling normalization or similar size-factor approach.
- ADT: Centered log-ratio (CLR) transformation across cells, applied per sample to avoid batch effects.
- Do not integrate the two modalities at this stage; keep them as parallel feature spaces.

**Step 3. Clustering using RNA alone, ADT alone, and a simple concatenated representation.**
For each, apply graph-based clustering (e.g., shared nearest-neighbor graph with Louvain community detection). Annotate clusters by known marker expression (e.g., CD3/CD4/CD8/CD14/CD19). This provides a reference cell-type label for downstream stratification.

**Step 4. Discordance calling (per marker, per cell type, per condition).**
Apply the calibrated noise model (Section 3.3). For each marker m in cell type t:
- Compute the bivariate distribution of (RNA_m, ADT_m).
- Compute the spike-in-calibrated null envelope.
- Classify cells as concordant, RNA-high/protein-low discordant, or RNA-low/protein-high discordant.
- Record the fraction of discordant cells (f_disc) and its 95 % bootstrap confidence interval.

**Step 5. Test prediction A-1 vs. B-1 (reproducibility across technical replicates).**
For each donor × condition pair, the two technical replicates provide independent discordance calls. Compute the overlap: of cells classified as discordant in replicate 1, what fraction of cells with the same barcode (or, since barcodes differ, cells in the same position in joint embedding space) are also discordant in replicate 2? Use the Jaccard index of discordant cluster membership across replicates.
- **Decision rule:** If the Jaccard index for a given marker's discordant population is significantly greater than expected under the null (permutation of replicate labels, 1,000 permutations, α = 0.01 after Bonferroni correction for number of markers × cell types tested), conclude that the discordant population is reproducible (supports Mechanism A).
- Because the two replicates come from the same stained cell suspension split before droplet encapsulation, the same cells are not measured twice. Instead, reproducibility is assessed at the population level: does a subpopulation of the same size, location in gene-expression space, and discordance direction appear in both replicates?

**Step 6. Test prediction B-2 (association with technical covariates).**
For each marker, fit a logistic regression: discordance status ~ library size + mitochondrial fraction + ambient contamination score + (biological covariates: condition, cell type). Report the proportion of deviance explained by technical vs. biological covariates.
- **Decision rule:** If technical covariates explain >80 % of the deviance and biological covariates <5 %, this supports Mechanism B for that marker.

**Step 7. Test prediction A-2 (pathway coherence in discordant cells).**
Within each cell type, compare the transcriptomes of discordant cells vs. concordant cells (for each marker, each direction of discordance). Perform gene-set enrichment analysis on the ranked gene list (e.g., using the fgsea algorithm with MSigDB Hallmark and KEGG gene sets).
- **Decision rule:** If discordant cells show significant enrichment (FDR < 0.05) for post-transcriptional regulatory pathways (e.g., "mRNA surveillance," "ubiquitin-mediated proteolysis," "regulation of translation") and this enrichment is absent when discordance labels are permuted, this supports Mechanism A.

**Step 8. Test prediction A-4 (condition-dependent discordance).**
Compare f_disc across the three time points (unstimulated, 4 h, 24 h) using a mixed-effects model with donor as random intercept: f_disc ~ condition + (1|donor). If discordance is biologically driven, expect f_disc to peak at 4 h (when mRNA has risen but protein has not yet accumulated) and decline by 24 h for activation markers.
- **Decision rule:** A significant condition effect (likelihood-ratio test, p < 0.05) with the predicted temporal pattern supports Mechanism A. A flat profile across conditions supports Mechanism B.

**Step 9. Quantify the biological vs. technical fraction (Mechanism C assessment).**
Combine the results of Steps 5–8. For each marker, assign a "biological discordance confidence score" based on reproducibility, pathway enrichment, and condition dependence. Report the proportion of markers (and, weighted by cell counts, the proportion of discordant cell-observations) that pass all three criteria. This fraction estimates the extent to which Mechanism A vs. B dominates.

### 3.6 Stop Rules and Troubleshooting

| Issue | Trigger | Action |
|---|---|---|
| Spike-in cells show very high variance | Coefficient of variation of ADT counts in spike-in > 0.5 for > 50 % of markers | Suspect antibody panel quality; re-titrate antibodies before proceeding |
| Very low discordance rate | f_disc < 2 % for all markers in stimulated condition | Extend stimulation time points (1 h, 2 h, 6 h, 12 h) to capture the window of maximal RNA–protein lag |
| Ambient RNA contamination dominates | >30 % of mRNA UMIs in empty droplets map to the marker genes | Apply computational decontamination (e.g., SoupX or DecontX) and repeat discordance calling; if discordance disappears, conclude it was artifactual for those markers |
| Donor-to-donor variability obscures condition effect (Step 8) | Random-intercept variance ≫ condition effect | Increase to n = 6 donors or switch to a paired within-donor analysis |
| Sequencing saturation too low for RNA | Median genes per cell < 1,000 | Sequence additional reads before analysis |

### 3.7 Power Note
With 5,000 cells per library and a discordant subpopulation of 5 % within a cell type composing 30 % of all cells (e.g., CD4 T cells), each replicate would contain ~75 discordant CD4 T cells. A two-proportion z-test comparing f_disc between conditions (4 h vs. unstimulated) with n = 75 per group has >80 % power to detect a doubling of the discordance rate (from 5 % to 10 %) at α = 0.05. If the expected effect size is smaller, cell numbers per library should be increased.

---

## 4. Conditional Conclusions

### 4.1 Positive outcome (supports Mechanism A predominantly)
**If:** (i) discordant subpopulations are reproducible across technical replicates (Step 5 Jaccard index significant), (ii) discordant cells are enriched for post-transcriptional regulatory pathways (Step 7), (iii) discordance rate changes with stimulation time in the predicted direction (Step 8), and (iv) technical covariates explain a minority of discordance variance (Step 6), **then** the strongest justified conclusion is:

*A substantial fraction of RNA–protein discordances detected by joint single-cell measurement reflect genuine, transient post-transcriptional regulatory states. These states are biologically informative and should be preserved—not smoothed away—by integration algorithms. The joint modality provides information about cell states that neither modality alone can capture.*

This conclusion would motivate development of integration methods that explicitly model and retain biologically validated discordance, rather than forcing RNA and protein into agreement.

### 4.2 Negative outcome (supports Mechanism B predominantly)
**If:** (i) discordant cell identities are not reproducible across technical replicates, (ii) technical covariates dominate the logistic regression, (iii) no pathway enrichment survives permutation control, and (iv) discordance rate is invariant across stimulation conditions, **then** the strongest justified conclusion is:

*Most RNA–protein discordances observed in this system are attributable to the distinct noise and detection properties of the two measurement modalities, not to real biological states. Integration algorithms should therefore prioritize noise reduction and cross-modal smoothing; apparent discordant populations should not be interpreted as novel cell states without independent validation.*

This conclusion would redirect effort toward better noise models and normalization strategies rather than biological exploration of discordant populations.

### 4.3 Ambiguous outcome (supports Mechanism C, or inconclusive)
**If:** results are mixed—for example, some markers show reproducible, pathway-enriched discordance while others do not; or reproducibility is borderline; or the condition effect is present but does not reach significance with three donors—**then** the strongest justified conclusion is:

*RNA–protein discordance is a mixture of biological signal and technical noise, with the ratio depending on the specific marker, cell type, and dynamic context. No single integration strategy is universally appropriate. Marker-specific noise calibration (using spike-in or steady-state reference cells) is required before discordance can be interpreted biologically.*

This would motivate a follow-up study with (a) more donors for statistical power, (b) an expanded time course, and (c) orthogonal validation of the most promising discordant markers (e.g., fluorescence-activated cell sorting of discordant cells followed by functional assays such as cytokine secretion or proliferation).

---

## 5. Relationship to the Supplied Evidence

| Claim | Status |
|---|---|
| Joint RNA + protein measurement per single cell is feasible via oligonucleotide-tagged antibodies | **Established** by the supplied evidence |
| RNA and protein modalities have different noise and detection properties | **Established** by the supplied evidence |
| An optimal integrated representation of the two modalities exists | **Not established**; the proposed experiment informs what integration should preserve vs. smooth |
| All apparent RNA–protein disagreements define real cell states | **Not established**; this is exactly what the proposed experiment tests |
| Any specific discordance rate, pathway enrichment, or temporal pattern | **Not observed**; these are predictions of the proposed experiment, not reported results |

---

## 6. Key Assumptions and Limitations

1. **Spike-in validity.** The Jurkat (or equivalent) spike-in is assumed to approximate the technical noise of primary cells. If primary cells have systematically different capture efficiency (e.g., due to size), the noise model will be mis-calibrated. Mitigation: include a second spike-in cell line of different size.

2. **Antibody specificity.** ADT signal is assumed to reflect the cognate surface protein. Non-specific binding would inflate apparent discordance. Mitigation: include isotype-control antibodies in the panel and use their signal distribution to set a background threshold.

3. **Temporal resolution.** Three time points may miss the peak of discordance. Mitigation: the stop rule above prescribes additional time points if discordance is unexpectedly low.

4. **Generalizability.** Results in PBMCs under T-cell activation may not generalize to other tissues or perturbations. This limitation should be stated explicitly; extension to other systems would be a subsequent study.

5. **Confounding by protein turnover kinetics.** Known differences in protein half-life could produce discordance that is "biological" in a trivial sense (all cells of a type show the same lag). The analysis addresses this by looking for cell-to-cell heterogeneity in discordance within a cell type, not just average lags.

---

## 7. Summary

The most valuable next question is whether RNA–protein discordances in joint single-cell measurements are predominantly biological or technical. The proposed experiment uses stimulation time-course data, spike-in calibration, technical replicates, and blinded analysis to discriminate between these mechanisms. The answer directly determines how the two modalities should be integrated and interpreted, making it a prerequisite for all downstream biological applications of this technology.
