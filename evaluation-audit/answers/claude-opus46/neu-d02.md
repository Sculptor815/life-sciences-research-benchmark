# Claude Opus 4.6 / neu-d02

Original final answer, shared by both scoring rounds.

# Proposed Calibration and Validation Protocol for a Genetically Encoded Calcium Indicator (GECI) Used to Infer Neural Activity

## 1. EXECUTIVE SUMMARY AND RECOMMENDED APPROACH

**Conclusion:** Before any GECI-based imaging dataset can be interpreted as neural spiking, a structured calibration must establish (i) the quantitative relationship between fluorescence transients and spike counts in the specific cell type, (ii) the magnitude and correction of non-neural sources of fluorescence change, and (iii) the detection limits and false-positive rates under the actual experimental conditions. The protocol below proposes to accomplish this through simultaneous two-photon imaging and juxtacellular or whole-cell electrophysiology, a structural reference channel, systematic neuropil and motion controls, and visual-response validation—all organized as independent, blinded experimental units with explicit acceptance and stopping criteria.

**Evidence basis:** The evidence packet states that fluorescence reflects calcium dynamics influenced by the indicator and imaging system, not error-free instantaneous spikes; that calibration in one cell type cannot be unconditionally extrapolated; and that movement, focus drift, neuropil contamination, indicator kinetics, saturation, and expression level are documented artifact sources. The protocol addresses each of these stated limitations.

---

## 2. PREPARATION AND QUALITY CHECKS

### 2.1 Animal Preparation (Proposed)
- Express the GECI in the target cell type using a cell-type-specific promoter or Cre-driver line. Co-express or co-inject a spectrally separated, calcium-insensitive structural fluorophore (e.g., a red fluorescent protein) to provide a **structural reference channel**.
- Implant a chronic cranial window over the target cortical area. Allow ≥2 weeks for expression stabilization before imaging.

### 2.2 Expression-Level Checks (Proposed)
- **Rationale:** The evidence states that expression level can make the same fluorescence amplitude correspond to different firing rates. Overexpression may buffer endogenous calcium and alter physiology; underexpression yields poor signal-to-noise.
- **Proposed procedure:**
  1. Acquire baseline fluorescence (F₀) images in both the GECI channel and the structural reference channel at standardized laser power.
  2. Compute the ratio of GECI baseline fluorescence to structural-channel fluorescence for every identified soma. This ratio indexes expression level independent of optical access.
  3. Rank all cells by this ratio. Partition into tertiles (low, medium, high expression).
  4. **Acceptance criterion:** Only cells in the central tertile proceed to spike-calibration experiments. If the distribution is bimodal (suggesting mosaic expression), flag the preparation for exclusion or re-injection.
  5. In a subset of cells, perform whole-cell recording and monitor resting membrane potential and input resistance to confirm that indicator expression has not measurably altered intrinsic excitability (compare to literature values or naïve animals of the same genotype).

### 2.3 Structural Reference Channel Validation (Proposed)
- Image the structural channel simultaneously with the GECI channel during deliberate z-stage steps (±5 µm in 1 µm increments) and lateral stage offsets (±3 µm).
- Record ΔF/F in both channels. The structural channel should show motion-correlated ΔF/F artifacts but **no** calcium-dependent transients. Any calcium-dependent signal in the structural channel indicates spectral bleedthrough; adjust emission filters or apply a linear unmixing correction whose coefficients are estimated from these calibration frames.

---

## 3. INDEPENDENT EXPERIMENTAL UNITS AND ALLOCATION/BLINDING

### 3.1 Unit Definition
- The independent experimental unit is one **cell–session pair**: a single identified neuron recorded on a single day with simultaneous electrophysiology and imaging.
- A minimum of N cell–session pairs is required per cell type (N determined by the stopping criteria below, §7).

### 3.2 Allocation and Blinding
- **Stimulus order:** Visual stimulus conditions (orientation, contrast, blank) are presented in a pseudo-randomized block design within each session.
- **Analysis blinding:** Spike sorting and fluorescence trace extraction are performed by separate analysts; spike-to-fluorescence mapping is performed only after both data streams are independently quality-checked and locked.

---

## 4. INTERVENTION AND SAMPLING

### 4.1 Simultaneous Electrophysiology and Imaging (Proposed)
- **Electrophysiology:** Juxtacellular (loose-seal, cell-attached) recording is the preferred ground-truth modality because it minimally perturbs intracellular calcium. Whole-cell recording may be used in a subset to obtain subthreshold membrane potential, with the caveat that dialysis of intracellular contents alters calcium buffering; such cells are analyzed separately.
- **Imaging:** Two-photon laser-scanning microscopy at the highest achievable frame rate consistent with adequate signal-to-noise. Because the exact imaging rate is unavailable, it must be treated as a calibration parameter:
  1. Image the same cells at multiple frame rates (e.g., 15, 30, 60 Hz if technically feasible) during evoked spiking.
  2. At each rate, determine the minimum resolvable inter-spike interval and the single-spike ΔF/F amplitude and decay time constant.
  3. Select the frame rate at which single action potentials are reliably detected (see §6.1 for detection criteria). Report this rate as a calibrated parameter.

### 4.2 Visual Stimulation Protocol (Proposed)
- Present drifting gratings at 8–12 orientations, multiple contrasts (including 0% = mean-luminance blank), and a static gray screen, each in randomized interleaved blocks of ≥10 repetitions.
- Include a **behaviorally salient, high-contrast** flashed stimulus that is expected to elicit both neural responses and reflexive eye/body movements; this stimulus serves double duty for visual-response validation and motion-artifact assessment.

### 4.3 Three-Dimensional Motion Estimation (Proposed)
- **Lateral (x-y) motion:** Register every frame of both channels to a session-averaged template using rigid or piece-wise affine registration. Record the displacement time series.
- **Axial (z) motion:** Exploit the structural reference channel: because the structural fluorophore is calcium-insensitive, any slow drift in its fluorescence that correlates with respiration, heartbeat, or locomotion reports z-displacement (defocus). Calibrate this relationship using the deliberate z-step data from §2.3, yielding a z-displacement estimate per frame.
- **Acceptance criterion for each trial:** If the estimated peak-to-peak lateral displacement exceeds 2 µm or z-displacement exceeds 3 µm (or a cell-diameter-fraction threshold determined empirically), the trial is flagged. If >20% of trials are flagged in a session, the session is excluded.
- **Residual motion artifact test:** After registration, compute ΔF/F in the structural channel. Any residual correlation between structural-channel ΔF/F and the motion-displacement time series indicates incomplete correction; report the magnitude of this correlation as a motion-artifact floor.

---

## 5. MEASUREMENTS AND CONTROLS

### 5.1 Neuropil Contamination Sensitivity Analysis (Proposed)
- **Rationale:** The evidence explicitly lists neuropil contamination as producing behaviour-related false signals.
- **Procedure:**
  1. For every ROI (soma), define a surrounding annulus (inner edge = soma boundary + 2 µm guard band; outer edge = soma boundary + 15 µm, excluding other somata).
  2. Extract the neuropil fluorescence trace F_neuropil(t) from this annulus.
  3. Subtract a fraction r × F_neuropil(t) from the somatic trace, where r is a contamination coefficient.
  4. **Calibration of r:** Vary r from 0 to 1 in steps of 0.05. For each value, re-estimate ΔF/F and correlate with the electrophysiology-derived spike train. Select r that minimizes the residual between predicted and observed spike-related fluorescence (or, equivalently, that removes stimulus-locked transients present in the neuropil but absent from the spike train). Report r and its confidence interval per cell and per cortical depth.
  5. **Sensitivity test:** Report how detection sensitivity (§6.1) and false-positive rate (§6.2) change across the range of r. If a ±0.1 change in r alters the false-positive rate by >50%, flag the dataset as neuropil-sensitive and restrict conclusions accordingly.

### 5.2 Known Spike-Count Calibration (Proposed)
- Using simultaneous electrophysiology data, construct the **ΔF/F-vs-spike-count transfer function** for the target cell type:
  1. Align fluorescence transients to electrophysiologically identified spikes.
  2. For isolated single spikes (no other spike within ±200 ms), measure peak ΔF/F, rise time (10–90%), and decay time constant (single-exponential fit). These are the single-AP parameters.
  3. For bursts of 2, 3, … n spikes occurring within a defined window, measure the aggregate ΔF/F. Fit a saturating function (e.g., Hill equation: ΔF/F = A × n^h / (n^h + K^h)) to characterize linearity and saturation.
  4. Report the spike count at which ΔF/F reaches 90% of saturation (n_sat). This defines the upper counting range.
  5. **Cell-type specificity caveat (from evidence):** This calibration applies only to the recorded cell type. If multiple cell types are imaged, each requires its own calibration dataset or an explicit assumption of equivalence with stated uncertainty.

### 5.3 Paired Ground-Truth Reporting (Proposed)
- For every cell with simultaneous recordings, report the following paired metrics:
  - Spike-triggered average fluorescence waveform ± SEM.
  - Event-triggered (fluorescence transient → spike-train) verification: fraction of detected fluorescence events that contain ≥1 spike (true positive rate) and fraction that contain 0 spikes (false positive rate).
  - Correlation coefficient between inferred spike rate (from any deconvolution algorithm applied) and actual spike rate binned at the frame period.
  - Mutual information between fluorescence trace and spike train.

---

## 6. DETECTION PERFORMANCE AND FALSE-POSITIVE REPORTING

### 6.1 Detection Threshold Calibration (Proposed)
- Because the exact detection threshold is unavailable, calibrate it empirically:
  1. Sweep a candidate threshold (in units of noise standard deviations, e.g., 2σ to 5σ) across the fluorescence traces.
  2. At each threshold, compute: **True Positive Rate (TPR)** = fraction of electrophysiologically confirmed spikes that produce a supra-threshold fluorescence transient; **False Positive Rate (FPR)** = fraction of supra-threshold fluorescence transients that lack a corresponding spike.
  3. Construct a receiver-operating-characteristic (ROC) curve. Report the area under the curve (AUC) and the threshold that yields a target FPR ≤ 5% (or, if this is unattainable, the minimum achievable FPR and the corresponding TPR).

### 6.2 False-Positive Attribution (Proposed)
- For every false-positive event (supra-threshold transient without a spike), classify the likely cause:
  - **Motion artifact:** Correlates with displacement time series or structural-channel ΔF/F.
  - **Neuropil bleedthrough:** Correlates with the annular neuropil trace.
  - **Slow calcium event (non-spike):** Broad transient not matching the spike-triggered waveform template.
  - **Unclassified.**
- Report the fraction attributable to each category. This decomposition directly addresses the evidence packet's enumerated artifacts.

---

## 7. ANALYSIS, ACCEPTANCE, AND STOPPING CRITERIA

### 7.1 Analysis Pipeline
1. Motion correction (§4.3) → 2. ROI segmentation → 3. Neuropil subtraction (§5.1) → 4. ΔF/F computation (F₀ = rolling 10th-percentile or mode of baseline distribution) → 5. Spike inference (template matching or deconvolution) → 6. Paired comparison with electrophysiology (§5.3) → 7. Visual-response quantification (orientation selectivity index, contrast-response function) computed from both fluorescence-inferred and electrophysiology-derived spike rates, compared per cell.

### 7.2 Acceptance Criteria (Proposed)
| Parameter | Minimum acceptable value | Action if not met |
|---|---|---|
| Single-AP ΔF/F SNR (peak / noise σ) | ≥ 2 at chosen frame rate | Increase expression time or laser power; re-evaluate |
| Structural-channel ΔF/F residual (after registration) | < 1% peak-to-peak per trial | Improve registration algorithm or exclude session |
| ROC AUC for spike detection | ≥ 0.85 | Report reduced sensitivity; restrict to burst detection |
| False-positive rate at chosen threshold | ≤ 5% | Increase threshold; accept reduced TPR |
| Neuropil coefficient r sensitivity | FPR changes < 50% for r ± 0.1 | Report neuropil-sensitive; restrict imaging depth or field of view |
| Expression-ratio CV across included cells | < 0.3 | Narrow inclusion window or re-inject |

### 7.3 Stopping Rules
- **Minimum sample:** Propose a pilot cohort of 15 cell–session pairs. After the pilot, estimate the standard error of the single-AP ΔF/F and the ROC AUC. Continue adding pairs until the 95% CI on the single-AP ΔF/F amplitude is ≤ 20% of the point estimate, or until 50 pairs are reached (resource ceiling). If the acceptance criteria in §7.2 cannot be met after 50 pairs, the preparation or indicator is deemed unsuitable for single-spike inference in this cell type.

---

## 8. TROUBLESHOOTING DECISION TREE

| Observed problem | Likely cause (from evidence) | Proposed remedy |
|---|---|---|
| Large ΔF/F in structural channel correlated with locomotion | Residual lateral or axial motion | Re-run registration with non-rigid algorithm; add z-piezo feedback |
| Stimulus-locked ΔF/F without spikes | Neuropil contamination | Increase neuropil subtraction coefficient r; verify with annulus trace |
| Declining baseline F₀ across session | Photobleaching or indicator loss | Shorten session; normalize per-trial; check expression stability over weeks |
| ΔF/F saturates at low spike counts | Indicator saturation or overexpression | Restrict to lower-expression cells; use indicator variant with higher Kd if available |
| High cell-to-cell variability in single-AP ΔF/F | Expression-level heterogeneity | Stratify by expression ratio (§2.2); report calibration per stratum |

---

## 9. EVIDENCE-TO-INFERENCE-TO-CONCLUSION CHAIN

1. **Evidence:** Fluorescence reflects calcium dynamics influenced by the indicator and imaging system, not error-free spikes. → **Inference:** A transfer function from ΔF/F to spike count must be measured, not assumed. → **Protocol element:** §5.2, spike-count calibration with simultaneous electrophysiology.

2. **Evidence:** Calibration in one cell type cannot be unconditionally extrapolated. → **Inference:** Every target cell type requires its own calibration dataset. → **Protocol element:** Cell-type specificity caveat in §5.2; stopping rules require sufficient paired recordings per type.

3. **Evidence:** Movement, focus drift, neuropil contamination produce false signals. → **Inference:** Each artifact source must be independently measured and its contribution to false positives quantified. → **Protocol element:** §4.3 (3D motion), §5.1 (neuropil), §6.2 (false-positive attribution).

4. **Evidence:** Indicator kinetics, saturation, and expression level cause the same ΔF/F to correspond to different firing. → **Inference:** Expression must be controlled and the saturation regime characterized. → **Protocol element:** §2.2 (expression checks), §5.2 (saturation curve).

---

## 10. ALTERNATIVES AND LIMITS

- **Alternative ground truth:** Juxtacellular recording may miss spikes at low seal resistance; whole-cell recording dialyzes calcium buffers. A hybrid approach (juxtacellular for primary calibration, whole-cell for subthreshold validation in a separate subset) mitigates both weaknesses.
- **Alternative motion correction:** Adaptive optics or simultaneous reflectance imaging could provide z-motion estimates independent of the structural channel, but add hardware complexity.
- **Fundamental limit:** Even with perfect calibration, the indicator's kinetics impose a temporal resolution ceiling. The protocol characterizes but cannot remove this limit; conclusions about spike timing finer than the measured rise time should not be drawn from fluorescence alone.
- **Generalizability:** All calibration parameters (single-AP ΔF/F, r, detection threshold) are specific to the combination of indicator, cell type, cortical layer, imaging wavelength, and optical setup. Any change in these factors requires re-calibration.

**All experiments described above are proposed.**
