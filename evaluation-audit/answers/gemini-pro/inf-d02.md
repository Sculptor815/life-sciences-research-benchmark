# Gemini 3.1 Pro Preview / inf-d02

Original final answer, shared by both scoring rounds.

**Recommended Next Action**
The recommended next action is to deploy a proposed, stateless, and immutable computational protocol for bulk RNA-seq differential expression analysis. This proposed plan uses a negative-binomial generalized linear model (GLM) via DESeq2. Because no files are currently supplied, all parameters, reference versions, and paths must be treated as placeholders. The core of this design restricts the definition of the experimental unit strictly to the level of independent treatment allocation, ensuring that technical or within-donor replication is not falsely modeled as across-donor biological heterogeneity. 

**Scientific Argument**
Robust reproducibility in transcriptomics requires an analysis pipeline devoid of hidden state, where outputs are uniquely determined by immutable inputs (raw reads, sample sheets, reference genomes, and code versions). According to the supplied evidence, DESeq2 utilizes negative-binomial GLMs with information sharing across genes to estimate dispersion and effect sizes, providing rigorous inference and diagnostics. However, the evidence explicitly states that statistical modelling cannot create missing independent treatment replication. Therefore, an audit-compliant analysis must correctly specify the experimental unit. If multiple treatments are allocated to wells derived from a single donor, the experimental unit is the well; while inference can be made about that specific donor, it is impossible to identify across-donor heterogeneity merely by adding a donor random effect (Evidence: Source summary). The proposed design mandates a sample sheet and contrast matrix that explicitly distinguish between biological donors and technical/well replicates, preventing pseudoreplication.

**Consequential Uncertainties & Limits**
1. **Unreported True Biological Variance:** Because no data files are available at design time, the magnitude of across-donor vs. within-donor variance is unknown. If the data is ultimately derived from a single donor, the proposed protocol limits conclusions strictly to within-donor effects. 
2. **Batch Confounding:** The interaction between processing batches and treatment allocation is unknown. If batches perfectly correlate with treatments, the batch effect cannot be mathematically decoupled from the biological effect, which would mandate stopping the analysis and requiring new independent experiments.
3. **Missing Count Matrices:** All code execution, read alignment, and count generation steps are strictly proposed. Calibration of FDR and log2-fold-change (LFC) thresholds will depend on empirical dispersion distributions once data is available.

---

### Proposed Operational Protocol

*Note: All analyses, paths, numeric settings, and thresholds described below are proposed. No execution is claimed as no files have been supplied.*

#### 1. Preparation and Quality Checks
*   **Immutable Inputs Definition:** All input files must be secured in read-only storage and cryptographically hashed (e.g., SHA-256). These include:
    *   Raw FASTQ files (Path: `[PLACEHOLDER_FASTQ_DIR]`).
    *   Reference Genome (Version: `[PLACEHOLDER_GENOME_VERSION]`, Path: `[PLACEHOLDER_GENOME_FASTA]`).
    *   Annotation GTF (Version: `[PLACEHOLDER_GTF_VERSION]`, Path: `[PLACEHOLDER_GTF]`).
*   **Sample Sheet Formalization:** Construct a plain-text, version-controlled metadata file (`[PLACEHOLDER_SAMPLESHEET.csv]`). This sheet must contain columns for `SampleID`, `Treatment_Status` (Intervention vs. Control), `DonorID`, `Processing_Batch`, and `Allocation_Unit` (e.g., WellID).
*   **Pre-computation QC (Proposed):**
    *   Calculate FastQC metrics on raw reads. 
    *   *Calibration:* Read depth thresholds are unknown; propose retaining samples with mapped reads > `[PLACEHOLDER_READ_MIN]` and transcriptomic mapping rates > `[PLACEHOLDER_MAP_RATE]%`.

#### 2. Independent Units 
*   **Defining the Unit:** The experimental unit must be defined as the physical entity independently randomized to the treatment. 
    *   *Scenario A (Multi-donor):* If treatments are randomized across independent subjects, `DonorID` is the experimental unit. 
    *   *Scenario B (Single-donor, multi-well):* If treatments are randomized to wells populated by cells from a single donor, the `Allocation_Unit` (well) is the experimental unit. The analysis will not claim across-donor generalization because modeling does not create missing biological replication (Evidence: Source summary).

#### 3. Allocation and Blinding
*   **Allocation Tracking:** The sample sheet must record the precise randomization scheme. If batch processing was used, batches (`Processing_Batch`) must be orthogonal to `Treatment_Status` to prevent confounding. 
*   **Blinding:** Analysis code will be written against dummy variable names (e.g., Group A vs Group B) until the final contrast is authorized, preventing parameter-tuning bias during model design.

#### 4. Intervention and Sampling (Proposed Constraints)
*   **Intervention:** The study consists of a designated Treatment and a Control. 
*   **Sampling:** RNA extraction methodologies and timepoints must be identical across groups. Any deviation in extraction time must be recorded as a new covariate in `[PLACEHOLDER_SAMPLESHEET.csv]`.

#### 5. Measurements 
*   **Quantification:** Proposed generation of a count matrix using a pseudo-aligner or splice-aware aligner (Software: `[PLACEHOLDER_ALIGNER]`, Version: `[PLACEHOLDER_ALIGNER_VERSION]`). 
*   **Matrix Generation:** A raw count matrix mapping `SampleID` to gene identifiers defined by `[PLACEHOLDER_GTF_VERSION]`. This matrix is immutable once generated and hashed for the audit trail.

#### 6. Controls
*   **Technical Controls:** RNA integrity (RIN) scores and batch processing dates will be assessed as potential covariates. 
*   **Model Controls:** The intercept of the GLM will be set to the Control group using the `Treatment_Status` factor, ensuring that the estimated effect is specifically the departure of the Treatment from the baseline.

#### 7. Analysis (DESeq2 Proposed Design)
*   **Stateless Execution Engine:** The analysis will be orchestrated via a workflow manager (e.g., Snakemake or Nextflow) enclosed within a container (e.g., Docker image version `[PLACEHOLDER_CONTAINER_HASH]`), ensuring that no hidden local state influences the environment.
*   **Count Model Formulation:** 
    *   The proposed model uses DESeq2 (Version `[PLACEHOLDER_DESEQ2_VER]`).
    *   *Design Formula:* `~ Processing_Batch + DonorID + Treatment_Status`. (Note: `DonorID` is included only if multiple donors exist and treatments are applied within-donor; if a single donor is used, `DonorID` is omitted to prevent matrix rank deficiency, reflecting the evidence that a random effect cannot substitute for missing donors).
    *   *Distribution:* Negative-binomial GLM.
    *   *Information Sharing:* The model will share information across genes to estimate dispersion parameters (Evidence: Source summary).
*   **Contrast and FDR:**
    *   *Contrast:* Specifically extract the LFC for `Treatment_Status`: Treatment vs. Control.
    *   *FDR Threshold:* Benjamini-Hochberg adjusted p-value limit set to `[PLACEHOLDER_FDR_ALPHA]`. 
*   **Plot Regeneration Module:**
    *   Code will automatically generate Principal Component Analysis (PCA) plots (to assess sample clustering by Treatment vs. Batch), MA plots (to assess log-fold change against mean normalized counts), and Volcano plots.
    *   Plotting scripts will pull strictly from the audited count matrix and sample sheet, preventing manual data subsetting.
*   **Source-Difference Audit:**
    *   All code, sample sheets, and parameter files must be committed to a Git repository.
    *   The audit trail consists of: 1) The Git commit hash of the analysis scripts, 2) the cryptographic hashes of the input FASTQ/Count matrices, and 3) the container image ID. An auditor can re-run the exact Git commit against the hashed inputs to bit-for-bit reproduce the outputs.

#### 8. Acceptance and Stopping Criteria
*   **Model Acceptance:** The analysis will be accepted if the DESeq2 dispersion plot demonstrates the expected asymptotic decrease in dispersion with increasing mean counts. If the dispersion estimates fail to converge or cluster around the upper boundary, the negative-binomial assumption may be violated, and the analysis will be stopped.
*   **Replication Check:** The analysis will be terminated prior to testing if the sample sheet reveals that the `Allocation_Unit` count for either Treatment or Control falls below `[PLACEHOLDER_MIN_REPLICATES]`. The model cannot invent missing independent replication (Evidence: Source summary).

#### 9. Troubleshooting and Parameter Calibration
*   **Calibration of Batch Effects:** If PCA indicates that `Processing_Batch` captures more variance than `Treatment_Status`, the batch covariate will be retained in the GLM. If batch and treatment are perfectly confounded, no statistical correction is possible, and the experiment must be flagged for redesign.
*   **Overdispersion/Outliers:** If specific sample libraries exhibit extreme Cook's distances in the DESeq2 diagnostics (Evidence: Source summary inference/diagnostics), they will be flagged. Sample removal is strictly prohibited unless a documented technical failure (e.g., failed library prep) is recorded in the sample sheet *prior* to unblinding.
