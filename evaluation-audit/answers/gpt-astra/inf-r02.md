# GPT-6 Astra / inf-r02

Original final answer, shared by both scoring rounds.

## Recommended next question

**Test whether RNA–surface-protein disagreement is a reproducible feature of a biological transition before treating it as a new cell state or choosing an integrated representation.**

For one selected surface protein and its cognate transcript, in one experimentally tractable cell population, the most valuable next question is:

> **Does a reversible biological perturbation generate reproducible RNA–surface-protein discordance, and is that discordance explained by delayed protein production/persistence, regulated surface redistribution, or technical and compositional effects?**

A controlled induction-and-recovery experiment is more discriminating than another unperturbed atlas: it supplies a known temporal direction, matched controls, and opportunities to intervene on candidate mechanisms.

**Everything below is proposed research, not a reported result.** The packet supplies no organism, target, perturbation, sampling times, assay chemistry, or quantitative performance estimates. Those must be established rather than attributed to the original work.

## 1. Evidence → inference → recommendation

The evidence locations are the three substantive statements in the supplied packet:

| Evidence location | What it establishes | Inference and limit |
|---|---|---|
| **E1:** “Oligonucleotide-tagged antibodies allow selected surface-protein measurements and transcript measurements to be linked to the same single cells.” | Joint, cell-linked measurement is possible. | One can investigate joint RNA–protein distributions. This does not establish accurate detection of every molecule or longitudinal measurement of the same cell. |
| **E2:** The measurements “can provide complementary information and have different noise and detection properties.” | Their signals need not be redundant; their errors need not be equivalent. | Discordance could carry biology, but asymmetric detection can also produce it. A zero RNA count is not sufficient evidence of absent transcription. |
| **E3:** The result does not establish an optimal integrated representation or that all apparent disagreements define real states. | Both interpretation and integration remain unresolved. | Neither separate clusters nor a combined embedding would, by themselves, establish a biological state. No later algorithm or benchmark can be presumed. |

**Conclusion:** Prioritize a calibrated, perturbational test of biological discordance. Retain the two modalities separately during the primary analysis; do not make a particular integration method part of the biological definition.

## 2. Competing mechanisms and discriminating predictions

These mechanisms can coexist. The objective is to identify contributions, not necessarily select one exclusive explanation.

| Proposed mechanism | Distinct predictions | Most discriminating evidence |
|---|---|---|
| **M1. Production and persistence lag** | Under a model in which RNA responds faster than protein, induction produces RNA-high/protein-low cells before protein rises. After cue removal, RNA falls before persistent protein, producing the opposite discordance. Total protein should change consistently with production and loss. | Ordered induction/recovery measurements; total alongside surface protein; a brief, validated intervention on new protein synthesis after RNA induction. Opposite-direction discordance is conditional on the relevant lifetimes, not guaranteed. |
| **M2. Regulated surface redistribution** | Surface protein changes disproportionately to total protein, potentially without an accompanying RNA change. An intracellular pool or measured surface delivery/internalization changes. | Independent localization or surface pulse–chase measurements and a validated intervention on the implicated transport step. Stable total protein alone is insufficient: balanced synthesis and degradation could mimic it. |
| **M3. Persistent production/turnover uncoupling** | Discordance persists through a sufficiently long plateau and recovery window rather than resolving as a simple lag. Protein production or loss differs despite comparable RNA. | Extended follow-up plus direct production/turnover measurements or selective perturbations. Finite observation cannot establish permanent uncoupling. |
| **M4. Detection, specificity, or processing artifact** | Discordance varies with antibody concentration, reagent identity, cell loading, capture depth, background, or processing batch; independent assays fail to reproduce it. | Specificity and background controls, technical perturbations, alternative epitopes, and independent same-cell RNA–protein measurement. |
| **M5. Population replacement or mixing** | Apparent temporal changes arise from differential survival, proliferation, changing subtype proportions, or multiplets rather than within-cell transitions. | Absolute recovery, viability, proliferation and composition measurements; analysis within prespecified strata; lineage or live-cell evidence if individual-cell transition claims are required. |

## 3. Ordered, auditable proposed research plan

### Step 1 — Define scope, prerequisites, and decision gates

**Proposed default system:** independently obtained donors supplying the same accessible cell population, maintained under a reversible experimental cue. If this is infeasible, use independent culture initiations from a defined model and restrict conclusions to that model. Different wells or cells from one donor are not independent donor replicates.

Before starting, document:

1. Cell source, eligibility criteria, and relevant collection/processing variables.
2. A cue that can be applied and removed without unacceptable cell loss.
3. A target antibody–gene mapping and a measurable dynamic range for both modalities.
4. A way to measure surface protein independently of oligonucleotide-tag recovery.
5. A sufficiently sensitive independent target-RNA assay.
6. Whether total protein and surface redistribution can be measured without changing target behavior.
7. Feasible limits on culture duration, cell input, and perturbation toxicity.

Select the target primarily for specificity, measurable response, and mechanistic tractability—not because it gives the most striking discordant plot. If several targets or cues must be screened, label that phase **discovery**, retain the full screening record, and use new biological units for confirmation.

**Gate:** Do not undertake a mechanistic discordance study with an unverified antibody, inadequate RNA sensitivity, or no measurable biological response.

### Step 2 — Establish an audit trail and separate discovery from confirmation

Create a versioned protocol with:

- Unique identifiers linking donor, culture, condition, time, processing batch, reagent lot, and assay.
- Raw-data preservation and a recorded analysis pipeline.
- Predefined technical exclusions and their rationale.
- A deviation log recording handling failures, missing samples, and decisions made before unblinding.
- A frozen confirmatory target, time windows, endpoints, and analysis.

**Proposed pilot:** four independent donors, used only for feasibility, calibration, timing, and variance exploration. This number is a starting allocation, not an assertion of adequate statistical power. Expand calibration if variability or uncertainty remains too large.

Pilot data must not count as independent confirmation of a hypothesis selected using those data.

### Step 3 — Calibrate the joint assay and orthogonal assays

Run calibration on material representative of the intended experimental conditions, not solely on an unrelated reference.

#### A. Antibody specificity and response range

- Titrate tagged antibody across concentrations.
- Seek a concentration with adequate binding, low nonspecific signal, and no detector/count saturation.
- Include independently verified target-positive and target-negative material where feasible.
- A target-depletion control is useful only if depletion and cell integrity are independently verified.
- Test an independent antibody recognizing a different epitope, if available.
- Compare tagged with independently labeled or untagged versions where possible.
- Test whether staining changes viability, cue response, or target redistribution over the intended exposure period.

Isotype controls and antigen competition can diagnose problems but are not, alone, complete specificity validation.

#### B. Background, recovery, and cell assignment

Include:

- No-antibody and matched cell-free processing controls.
- Oligonucleotide-only or free-tag controls where compatible with the selected assay.
- Standardized washing, with a pilot wash-stringency comparison.
- Cell-loading or controlled-mixture experiments to assess incorrect cell assignment and multiplets.
- A repeated reference sample in each processing batch.
- Read-depth and library-complexity assessment.

If the implementation partitions cells, examine cell-free partitions as an additional background source. The packet does not specify such an implementation, so this is conditional.

Downsampling or additional sequencing can assess sequencing limitations; neither establishes the recovery of molecules lost before library generation.

#### C. Independent measurements

Validate, on matched aliquots:

1. **Surface protein:** quantitative fluorescence or imaging using an independent detection scheme.
2. **Target RNA:** an independently calibrated transcript assay, preferably allowing individual-cell assessment.
3. **Joint orthogonal confirmation:** where compatible, surface staining followed by fixation and RNA imaging in the same cells.
4. **Total protein:** a validated total-protein measurement, with surface and intracellular localization distinguished where possible.

Check fixation and permeabilization effects on epitopes and RNA detection. Do not interpret a ratio of unrelated fluorescence intensities as a molecular surface fraction without compatible calibration.

#### D. Define interpretable ranges

Establish background, reliable detection ranges, between-run variation, and uncertainty in low counts. Explicitly identify conditions in which “not detected” remains compatible with low abundance.

Do not equate RNA counts and antibody-tag counts numerically. Their scales and sampling processes differ.

**Gate:** If technical discordance cannot be distinguished from the minimum biological effect of interest, improve calibration or change the target. Proceeding directly to clustering would not solve the problem.

### Step 4 — Pilot induction and recovery; lock sampling and discordance definitions

Use matched cultures for:

- Sham treatment.
- Cue maintained.
- Cue applied and subsequently removed.

Sample densely enough in the pilot to locate the initial RNA response, subsequent protein behavior, and recovery. Exact times and doses are **unreported parameters to be determined**, not author methods.

For confirmation, freeze seven sampling positions:

1. Baseline.
2. Early induction.
3. Intermediate induction.
4. Immediately before cue removal.
5. Early recovery.
6. Intermediate recovery.
7. Late recovery or plateau.

The actual intervals must follow pilot kinetics. Extend the observation window if it cannot distinguish delayed resolution from persistent mismatch.

#### Operational definition of discordance

Use independently calibrated, marker-specific high and low bands for each modality, with an intermediate uncertainty region. Freeze cutpoints before confirmation.

Define:

- \(q_{R+S-}\): fraction confidently RNA-high/surface-protein-low.
- \(q_{R-S+}\): fraction confidently RNA-low/surface-protein-high.

Report uncertain cells separately. Do not automatically classify zero-RNA-count/protein-positive cells as biological discordance.

Estimate false classification using validated references and technical controls. This estimate will not necessarily capture every condition-dependent artifact; orthogonal confirmation remains necessary.

Also retain continuous measurements. A conclusion that exists only at one threshold is weak.

**Proposed primary contrasts:**

- Cue versus sham for \(q_{R+S-}\) in the locked early-induction window.
- Cue removal versus continued cue for \(q_{R-S+}\) in the locked recovery window.

These specifically test the simple lag hypothesis. Continuous RNA, total-protein, and surface-protein trajectories test alternatives that do not produce these particular categories.

### Step 5 — Determine independent sample size and cell allocation

For donor-based confirmation:

- **Biological independent unit:** donor.
- **Randomization unit:** culture well or aliquot receiving a treatment.
- **Subsamples:** cells and technical libraries.
- **Proposed within-donor replication:** two independently handled cultures per condition–time combination, where material permits. These do not double the donor count.

Choose confirmatory donor number by simulation of the planned donor-blocked analysis using conservative pilot variance estimates.

Before simulation, specify:

- Minimum meaningful change in discordant fraction, \(\delta\).
- Desired precision for that change.
- Minimum temporal separation that would meaningfully support a lag.
- Power and multiplicity criterion.
- Anticipated missingness and technical failure allowance.

These values are not supplied and cannot be defensibly filled with purported empirical numbers.

Choose cells per culture to obtain useful precision for the expected discordant fractions, then prioritize additional independent donors over excessive sampling of one donor. Evaluate power across plausible variance estimates rather than trusting a noisy pilot point estimate.

If an important-effect threshold cannot be justified, preregister an estimation study rather than presenting a binary significance test as definitive.

### Step 6 — Allocate treatments, control handling, and blind measurements

For each donor, distribute cells across:

| Arm | Initial exposure | At the removal time |
|---|---|---|
| Sham | Vehicle/control | Matched mock exchange |
| Continued cue | Cue | Exchange with cue-containing medium |
| Cue removal | Cue | Exchange with cue-free medium |

Use separately assigned cultures for destructive time points. Do not count shared baseline or pre-removal samples twice.

- Randomize well position, treatment allocation, harvest order within permissible timing windows, and assay position.
- Balance donors, conditions, and phases across processing batches.
- Apply equal handling and exchange schedules.
- Record actual exposure and harvest times, not only intended times.

If storage or preservation is needed to balance batches, validate that it preserves the relevant measurements. Otherwise, use staggered initiation and reference samples. **A phase fully confounded with batch cannot establish a temporal effect.**

Treatment operators may be impossible to blind. Where possible, blind assay operators to condition, and provide analysts masked labels until quality exclusions and analysis code are frozen.

### Step 7 — Collect the necessary measurements

At every locked condition–time point, obtain:

1. Joint single-cell transcript and antibody-tag measurements.
2. Target RNA and target surface protein by independent methods on matched material.
3. Total target protein at selected informative times, preferably across the full kinetic sequence.
4. Viable cell recovery and absolute cell counts.
5. Viability/death and proliferation indicators.
6. Prespecified cell-identity or composition measurements.
7. Per-sample and per-cell technical quality metrics.
8. A measure showing that the cue was delivered and elicited a response independently of the target pair.

Retain enough material for targeted remeasurement where feasible.

Avoid quality filters that selectively discard stimulated, dying, or RNA-rich cells without documenting the biological consequences. Report exclusions and recovery by condition.

**Important limit:** sampling different cells over time produces population kinetics, not observed trajectories of individual cells. If replacement remains plausible, add validated lineage or live-cell tracking. If live reporters are required, their effects on RNA and protein behavior must themselves be tested.

### Step 8 — Perform conditional causal discrimination

Proceed only if the discordance is reproducible and independently confirmed. Prefer new donors for this phase, particularly if the intervention was chosen after examining confirmation data.

Select the smallest intervention set capable of separating the leading explanations.

#### A. Test dependence on new protein synthesis

Introduce a brief, validated intervention after the initial RNA response, with:

- Vehicle control.
- Matched intervention without cue.
- Evidence of intervention activity.
- Viability and RNA-response measurements.
- Release/recovery control where feasible.

**Prediction:** preventing new protein accumulation while retaining the initial RNA response supports a production-dependent lag. A surface change drawn from an existing protein pool may persist.

This is interpretable only if the intervention does not itself abolish cue signaling, alter antibody detection, or cause substantial selective death.

#### B. Test surface redistribution

Use an independently validated pulse–chase/localization assay and, if feasible, perturb the implicated delivery or internalization step.

**Prediction:** altered surface movement with little corresponding total-protein change, together with a cue-specific perturbation effect, supports regulated redistribution.

A transport intervention changing baseline surface abundance is not enough. Measure whether it changes the **cue-induced response**, and check that it does not merely conceal the antibody epitope.

#### C. Test persistent uncoupling

If mismatch persists, extend observation and measure production or loss rates where feasible. A long-lived protein and altered turnover can resemble stable regulation within a short experiment.

If no sufficiently interpretable intervention exists, stop at a descriptive kinetic conclusion rather than assigning a causal mechanism.

### Step 9 — Analyze with donor-level inference and explicit measurement uncertainty

#### Primary analysis

Estimate each discordant fraction by donor, arm, and time, retaining within-donor subsampling.

Use a prespecified donor-blocked model or donor-level paired contrasts. Control multiplicity across the two primary contrasts. Provide effect sizes and confidence intervals, not only significance tests.

Do not use thousands of cells as thousands of independent biological replicates.

#### Continuous and mechanistic analysis

Analyze RNA, surface protein, and total protein jointly as **separate observed variables**, including technical uncertainty where identifiable.

Compare constrained mechanistic models, for example:

- Production/loss with approximately constant surface allocation.
- Time-varying surface redistribution.
- Persistent differences in production or turnover.
- Technical-error-only and composition-change explanations.

A simple production/loss model could propose:

\[
\frac{dP_{\mathrm{total}}}{dt}=\alpha R-\beta P_{\mathrm{total}}.
\]

Here, \(R\) and \(P_{\mathrm{total}}\) represent underlying abundance, not automatically raw sequencing or fluorescence counts. Observation models and scale assumptions must be stated.

Use models to generate held-out temporal or intervention predictions. A better fit to the same snapshots does not establish uniquely identifiable molecular rates.

#### Required sensitivity analyses

Repeat the principal comparisons:

- Across reasonable frozen threshold alternatives.
- With continuous rather than categorical measurements.
- Across processing batches and reagent lots.
- Within prespecified cell strata.
- With and without borderline-quality cells.
- Under alternative background and detection assumptions.
- Accounting for viability, recovery, and composition changes.

Do not adjust away a biological effect merely because it changes total RNA or cell size; distinguish potential confounders from possible mediators.

Do not use a joint embedding or inferred pseudotime as independent validation of a state defined from those same measurements.

### Step 10 — Apply stop rules and troubleshoot transparently

Freeze numerical operating limits after the pilot and before confirmation.

| Trigger | Action and consequence |
|---|---|
| Specificity fails or orthogonal protein measurements disagree systematically | Halt target interpretation; investigate epitope accessibility, tagging, nonspecific binding, and staining effects. |
| Technical false-discordance uncertainty overlaps the meaningful biological effect | Improve assay sensitivity or reduce the claim; do not declare biological absence or presence. |
| Cue fails its independent response check | Treat as failed perturbation, not a negative biological result. |
| Differential death or composition change exceeds the predefined tolerance | Reduce exposure or redesign. Retain affected data for documenting selection, not silently exclude them. |
| Time and batch are inseparable | Repeat with balanced processing before interpreting kinetics. |
| Discordance depends strongly on one normalization or cutpoint | Report instability; seek independent quantification. |
| Mechanistic intervention changes RNA, viability, and detection simultaneously | Classify the mechanism test as uninterpretable; shorten exposure or find a more selective intervention. |
| A calibrated, adequately precise confirmation excludes effects of size \(\delta\) | Stop escalation for that target–system–cue combination. |
| Confidence intervals remain too wide | Call the result inconclusive; add biological units only under a predefined extension rule. |

Do not stop early for an attractive plot or nominal significance unless a sequential rule was preregistered. All reruns should have recorded causes.

## 4. Interpretation of possible outcomes

### Positive: reproducible kinetic discordance

**Required pattern:** cue-dependent discordance exceeds calibrated uncertainty, appears in independent donors and orthogonal assays, follows an ordered induction/recovery sequence, and is not explained by composition.

**Stronger mechanistic evidence:** total-protein kinetics and selective interventions support production/persistence lag.

**Strongest justified conclusion:** the selected RNA–surface-protein mismatch reports a reproducible temporal feature of this response and is at least partly explained by the supported mechanism.

Without individual-cell tracking, say **transient population enrichment**, not directly observed switching of the same cells.

### Positive: regulated redistribution

**Required pattern:** surface and total protein behave differently; localization or movement measurements corroborate redistribution; an interpretable intervention changes the cue-specific surface response.

**Strongest justified conclusion:** surface localization regulation contributes to the discordance. This does not imply that transcript abundance is uninformative or that translation is irrelevant.

### Positive: persistent uncoupling

Persistent, independently reproduced mismatch would support sustained RNA–protein uncoupling over the observed interval.

A distinct, stable **cell state** requires more: reproducibility beyond the marker pair, persistence or recurrence, and preferably a separately specified functional difference. No appropriate function assay is supplied; it must be chosen according to the selected biological system.

### Negative

If the cue works, both assays are sensitive, and confidence intervals exclude a meaningful discordance change:

> No meaningful cue-induced discordance was detected for this target, population, and observation window.

This would not establish universal RNA–protein concordance, disprove other biological states, or select an optimal integration algorithm.

### Ambiguous

Examples include reproducible mismatch only in the tagged assay, low-RNA counts below reliable detection, unresolved selective survival, competing mechanisms with indistinguishable predictions, or insufficient temporal resolution.

The correct conclusion is that the experiment has not separated biological uncoupling from the remaining alternative. The next action should address that specific ambiguity—not enlarge the cell atlas indiscriminately.

## 5. Overall justified conclusion

**The packet establishes joint measurement, not the biological reality of any particular disagreement.** The proposed study would determine whether one well-controlled discordance is technical, temporal, localization-dependent, or persistently regulated.

That result would inform what information an eventual integrated representation should preserve. It would not, by itself, establish a universally optimal representation or justify treating every RNA–protein disagreement as a new cell state.
