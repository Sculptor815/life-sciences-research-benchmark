# Grok 4.7 / inf-d01

Original final answer, shared by both scoring rounds.

The reproducible object is a frozen, patient-level pre-to-post score built only from assay blocks whose treatment contrast is separable from batch, internally stable under patient resampling, and tested once on the locked second cohort. Integration constructs that score across incomplete modalities; enrichment interprets or optionally regularizes it; external validation is the only confirmation. Do not call a pathway hit, a joint factor model, or a development-set p-value a reproducible treatment program.

## Evidence → inference → conclusion

M1 supports a paired estimand: each patient’s post minus pre change, with the patient as the independent unit. n = 30 paired patients can support a low-dimensional score and stability checks. It cannot support a richly parameterized early-fusion model, feature-wise claims, or a causal estimate. No untreated paired controls are described, so the target is treatment-interval association, not proof that treatment caused the change. Time, procedure, sampling site, tumor evolution, and assay design can produce the same pattern.

M2 implies that batch structure differs by platform and must be audited before any joint model. “RNA and protein were run in different batches” does not by itself prove that batch is aliased with timepoint; that aliasing is testable from a batch-by-timepoint table. “Most post-treatment metabolomics samples share a batch” is already strong evidence that, for metabolites, batch and timepoint may be nearly collinear. Where they are collinear, a post-versus-pre metabolite difference is not identifiable as biology. A correction that “preserves the timepoint coefficient” preserves the confounded contrast; it does not validate it. Permutation p-values also fail for that block, because shuffling labels cannot separate batch from timepoint.

M3 implies that complete-case multi-omics uses an unknown, possibly selected subset. Missingness by platform, timepoint, batch, and patient is unreported, so MCAR, MAR, and MNAR cannot be distinguished yet. Imputing an entire missing platform from another platform would manufacture cross-omic agreement and is not acceptable for the primary program.

M4 implies that the second cohort is a confirmatory instrument only if it is unused for feature selection, weight tuning, threshold setting, enrichment shopping, and “sanity checks.” Its size, assays, batch design, and clinical comparability are unreported. Small n can support one pre-specified score contrast; it cannot support rediscovery of individual features. A null there is inconclusive if power is poor, and non-confirmatory if the pre-specified interval excludes the observed effect. Either result must stand. Do not revise the program and retest.

Conclusion: claim a reproducible integrated program only if three gates pass in order: identifiability given M2, patient-level stability in the development cohort given M1 and M3, and a single pre-specified score replication on the untouched cohort given M4. If metabolomics fails identifiability, the honest primary claim is an RNA–protein program plus a labeled, non-confirmatory metabolite sensitivity analysis. If only one platform is identifiable and stable, call it a single-platform program, not an integrated one. Enrichment is not one of the three gates.

## How the three concepts relate

Integration is the construction of one patient-level object from RNA, protein, and metabolite changes after QC. It sits downstream of the batch audit and missingness audit, and upstream of locking. It is not a software brand and not validation. Late integration is the primary design because scales, feature counts, missingness (M3), and batch structures (M2) differ: each identifiable platform yields a paired-change score; scores are combined only across platforms actually measured for that patient. Early concatenation is a secondary sensitivity analysis only, after feature-count balancing, and only on identifiable blocks.

Enrichment maps a stable ranked list or feature set onto a version-frozen annotation (pathways, complexes, metabolic modules). Its roles are interpretation, optional pre-specified dimension reduction, and a coherence check across platforms. It does not add patients, does not break a batch alias, and does not confirm transportability. Enrichment computed on the same data used to pick features is anti-conservative unless the permutation repeats the selection. A coherent pathway story can still be a batch artifact.

External validation asks whether the frozen score’s paired change travels to a cohort that did not influence development. Nuisance normalization may follow the same SOP inside the external cohort; program weights, selected features, direction, and success rule may not be refit there. Discordance can mean biological non-transport, a development-set batch artifact (especially metabolites, M2), or a non-comparable external cohort. Those explanations are not separable by re-tuning.

## Assumptions and unreported parameters

Assumptions, each labeled: pretreatment and post-treatment labels are correct (M1); paired samples are comparable tumor material (unverified); batch labels are complete (required for M2 to be usable); one shared program is a reasonable target despite possible treatment heterogeneity (unverified); the second cohort is held out in full (M4).

Unreported, and not invented here: treatment identity, dose, schedule, and concomitant therapy; sampling interval and site matching; tumor type; cohort-2 size and whether its batches alias timepoint; which assays are missing and why; QC pools, spike-ins, and clinical response labels; whether any normalization has already been applied. If a clinical response label is absent, do not convert this into a response predictor. The estimand remains coordinated change across the treatment interval.

## Ordered protocol

### 1. Preparation and quality checks

Build a sample manifest before any association ranking: patient ID, timepoint, platform, batch, processing date, and pass/fail. Make a three-way availability table (platform × timepoint × patient) and a batch-by-timepoint count table per platform.

For each platform, compute technical QC on the technical distribution, never by which samples maximize a treatment contrast. RNA: depth, assignment/duplication or equivalent assay metrics, outlier status on minimally transformed abundances, and sex-check against metadata if genotypes or sex markers exist. Protein: per-sample and per-feature missingness, intensity distribution, internal-standard CV if standards exist. Metabolites: blank contamination, internal-standard recovery, drift, and peak-quality flags if those channels exist. If fingerprints or standards were not run, record that as a limitation; do not invent concordance.

Identifiability audit, per platform: fraction of post-treatment samples in the majority batch, and association between batch and timepoint. Where both timepoints occur in the same batches with replication, batch and treatment are separable in principle. Where almost all post-treatment metabolite samples share a batch (M2), declare the metabolite treatment contrast non-identified unless a bridge exists. Do not “correct” a non-identified contrast into a primary feature.

Calibration, not a borrowed cutoff: decompose paired-delta variance into components attributable to batch where the design allows it. Pre-specify that a platform enters the primary program only if a batch model is estimable and residual batch-attributable variance in the paired contrast is below a fraction chosen by simulation under a batch-only null, using the observed batch sizes. If the design matrix is singular, the fraction is undefined; exclusion is mandatory, not a matter of p-value. Repeat the decision at neighboring fractions in a sensitivity analysis so the conclusion is not an artifact of one cutoff.

Missingness audit: rates by platform, timepoint, batch, and patient, plus any recorded failure reason. Pre-specify the analysis population. Recommended primary rule, labeled as a proposal: a patient is in the paired analysis for every platform with both timepoints passing QC, and in the integrated score if at least two identifiable platforms are paired. Report n at each tier. Do not require all three platforms for the primary population unless the complete-case n remains adequate under the calibration below.

### 2. Independent units

Resample and permute patients, never features, samples, or pathways. Keep both timepoints and all available assays of a patient together. Features and pathways are dependent readouts, not sample size. Batches that contain many patients are clusters; patient bootstrap intervals are the default uncertainty. Clustering cannot identify a treatment effect that is aliased with batch.

### 3. Allocation and blinding

No treatment allocation is described; do not analyze this as a randomized trial. Analysis allocation is the protection.

Lock cohort 2 before development: no matrices, no summaries of molecular values, no exploratory plots. A gatekeeper who is not developing the model may report only cohort-2 paired n and assay-availability counts so the confirmation rule can state power. If even that contact is forbidden, keep the confirmation rule confidence-interval-based and label an underpowered null as inconclusive. Do not use cohort-2 outcomes either way.

Inside cohort 1, use patient-level repeated nested cross-validation or bootstrap optimism correction rather than one small holdout. With n = 30 (M1), a single split is unstable. Calibration of fold count and repeats: simulate paired scores with the observed missingness pattern and a range of true effect sizes; choose the resampling scheme that recovers the true effect with acceptable variance and does not systematically inflate stability. Fit all selection inside inner loops only.

Blinding limit: timepoint cannot be hidden, because timepoint defines the estimand. External molecular data and any unreported clinical-response labels must stay hidden. Anyone who has seen cohort-2 molecular results cannot set thresholds.

### 4. Intervention and sampling

Document the actual treatment window and sampling rules from source records before modeling. If intervals vary, the primary analysis remains the paired difference; a sensitivity model adds interval as a covariate. Do not impute a common interval or a common drug exposure.

Proposed experiment, only if residual material and a new batch are available: a bridge plate with pre- and post-treatment aliquots from more than one original batch, plus technical replicates, balanced across positions. That experiment is what would make an aliased metabolite contrast identifiable. If material does not exist, leave the metabolite primary contrast unidentified. Do not collect a new convenience set and call it cohort 2.

### 5. Measurements

Use frozen quantification pipelines. Choose normalization by negative-control behavior, not by treatment-effect size. Calibration: if spike-ins, blanks, or QC pools exist, prefer the transformation and scaling that removes association with library size or drift while leaving spike-in recovery stable. If they do not exist, compare candidate normalizations by independence from technical covariates and by stability of pre-specified technical controls; record the choice before ranking biology.

Analyze paired differences of transformed values (typically log-scale abundances for RNA and protein; metabolite scale chosen in the same calibration). Feature-level filters (detection rate, variance) are fit inside discovery folds and then frozen for confirmation folds.

Batch adjustment is allowed only in identifiable strata: location-scale or mixed-model adjustment using batches that contain both timepoints, with parameters estimated without reference to cohort 2. Do not apply a cohort-1 batch model to cohort 2 as if batches were shared. For external samples, rerun the same SOP within cohort 2, then apply frozen biological weights to cohort-2 paired deltas.

Missing features: calibrate “filter high-missingness features” against “simple within-platform imputation” by simulating the observed missingness rates and scoring bias in the paired mean. Do not impute a missing platform. Patients with a missing platform contribute their observed platform scores only.

### 6. Controls

Technical negatives: blanks, spike-ins, and QC pools if present; sex-mismatch markers as identity checks, not as biological negatives.

Design negative: sign-flip of paired deltas within batch strata that contain both timepoints. This is valid only where batch and timepoint are separable. Do not report that null for the aliased metabolite block.

Positive control: only if treatment class is documented before looking. Pre-specify one to three canonical pharmacodynamic markers. If they fail QC, do not replace them with markers that “worked.” If treatment class is unknown, there is no positive control.

No untreated control arm is in the packet. That is a limit on causal language, not a cue to invent a historical control.

### 7. Analysis

Platform-wise, on identifiable data only: patient-level paired deltas; shrink feature effects with a prior fit inside discovery folds (empirical-Bayes or penalized estimation). Calibrate the penalty by inner-loop stability, not by the smallest p-value. Rank features by stability across patient bootstraps, not by a single p-value screen.

Late integration, primary: for each identifiable platform, form a one-dimensional score from a sparse patient-level decomposition of deltas or from a pre-specified feature set chosen without outcome shopping. Standardize scores using discovery-fold means and SDs. Combine available platform scores with weights fixed in the SAP. Start with equal weights among observed platforms so missingness does not require imputation. A stability-weighted alternative may replace equal weights only if inner-loop calibration shows better recovery of a simulated shared signal under the observed missingness; freeze the winner before any external look.

Early integration, secondary only: latent factors on concatenated blocks after balancing feature counts, excluding non-identified metabolite data from the primary factor. Calibrate factor count by patient-fold reconstruction error, not by separation of timepoints. If a factor is dominated by one platform or by a batch indicator, discard it as a program.

Enrichment, after the stable list exists: version-lock annotations; test RNA, protein, and identifiable metabolites separately; permute by repeating selection. Cross-omic coherence is descriptive agreement of directions or modules, not a p-value stacked on a p-value. Do not promote an enrichment hit whose member features fail the stability gate.

Internal performance: optimism-corrected mean paired score change and a stability curve (inclusion frequency versus bootstrap null). Influence: leave-one-patient-out. A program driven by one patient fails the stability gate.

Freeze a single object: transformations, feature list or loadings, direction, combination rule, and the external success statistic. Write the SAP before the lock opens.

External test, once: apply the frozen rule to cohort-2 paired deltas after within-cohort SOP normalization. Primary statistic: mean paired change of the integrated score, with a confidence interval. Feature-level concordance is exploratory on a small cohort, not a second primary endpoint.

### 8. Acceptance and stopping

Development stops and the score freezes when QC, the identifiability audit, and the SAP are complete, and either the internal stability gate passes or a platform is explicitly dropped.

Internal pass, calibrated: inclusion frequencies exceed the null inclusion distribution obtained by sign-flip within identifiable strata, at a false-inclusion target chosen in simulation before ranking (target a pre-set expected false inclusions, then read the frequency cutoff off that null). The optimism-corrected score change must have the pre-specified sign. If no set meets the null-calibrated bar, stop and report a null. Do not loosen the cutoff and re-mine.

External pass, pre-specified: interval for the mean paired score change excludes zero in the pre-specified direction, or lies above a minimum effect set from the cohort-1 optimism-corrected estimate attenuated by a factor taken from the internal bootstrap attenuation distribution. Choose that factor before opening cohort 2. If gatekeeper n implies very low power, an exclusion failure is “not confirmed,” not “disproved.” A direction reversal is evidence against transport of this program.

Stop calling the result integrated if fewer than two platforms pass identifiability and stability. Stop all threshold edits after the external test is run. A post-hoc rescue requires a third cohort that is not in this packet.

### 9. Troubleshooting

Batch aliased with timepoint: drop that platform from the primary score; keep a clearly labeled sensitivity analysis; consider the bridge experiment. Do not use outcome-preserving batch correction as proof.

High assay missingness: stay with the tiered late-integration score; publish the missingness table. If complete multi-omics n collapses, do not impute platforms to restore it.

One influential patient or one dominant RNA feature block: fail the influence or balance check and return to the stability gate. Do not let the larger RNA matrix define a “multi-omic” factor by concatenation.

RNA–protein discordance: report it as a possible post-transcriptional or technical mismatch. Forcing agreement with a joint model is not troubleshooting; it hides the discrepancy.

Enrichment without stable features: discard the enrichment claim.

External failure: report non-confirmation. Do not refit weights, swap pathways, or move the metabolite block back into the score and test again.

## Alternatives and limits

Alternative estimand: if a clinical response label exists and is documented before analysis, a secondary model can ask whether baseline or paired scores associate with response. That is a different claim and needs its own frozen test. It is not licensed by M1–M4 as stated.

Alternative integration: early fusion or a single supervised multi-block model, only as sensitivity, and only on identifiable complete-enough blocks. Expect RNA to dominate unless feature influence is constrained.

Alternative confirmation: internal nested validation alone if cohort 2 is judged non-comparable once treatment, tumor type, or sampling are known. Then the strongest honest claim is internal stability, not external reproducibility. Non-comparable external data should not be forced into a pass/fail.

Limits that no analysis removes: n = 30; no untreated controls; possible treatment heterogeneity; metabolite batch aliasing unless a bridge exists; unknown missingness mechanism; small external n; enrichment dependence; and the inability of cohort 2 to both teach the model and confirm it. The analysis identifies a reproducible associated program only in the narrow sense of a frozen paired score that survives those gates. It does not identify mechanism, causality, or a clinical decision rule.
