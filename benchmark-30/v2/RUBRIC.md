# Second-round scoring rubric

Version: **strict-v2.1-public**. This owner-requested post-hoc rescore uses the same 360 selected responses after completion and archiving of round one. The scientific criteria, point deductions and applicability are unchanged from strict-v2.0; this revision updates coverage, public-release policy and reference provenance. It does not change candidate prompts retroactively or imply that candidates were told the new checklist in advance.

![Scoring workflow](../../docs/assets/scoring-workflow-v2.svg)

## Scope and provenance

The current set has ten essays, ten experimental designs and ten research-reasoning questions. There is one answer per question, with browsing disabled. The owner confirmed careful human review of all 30 questions and reference answers on 3 October 2026. Candidate scoring is a single Codex referee's assessment, with identities visible; it is not an independent human-panel score. Model identity, company, prestige and an expected ranking are never grading criteria.

Round-one scientific scores and matching evidence are archived byte-for-byte. Round two requires another complete read of each final answer against its question, packet, reference and applicable checks. References are aids, not infallible answers: a missing reference detail does not waive an explicit criterion, and an erroneous reference must receive a dated correction applied consistently. The owner explicitly authorized publication of all 30 questions, both reference versions, historical targets and scoring criteria on 4 October 2026. API credentials and raw candidate records remain private. The original owner review applies to version one; the new reference revisions have been checked by Codex and await the owner's review. They are not represented as independently human-reviewed revisions.

## Score calculation

The new scientific-quality scale starts at **100**. Subtract each applicable failed check below, subject to the non-duplication rule, and floor at zero. This is a new checklist scale, **not a subtraction from the first-round score**: subtracting again from that score would charge many omissions twice. Preserve the first-round score alongside it.

**Q2 = max(0, 100 − sum of distinct applicable deductions).**

A demonstrably false central premise that makes the principal recommendation invalid caps Q2 at 20. A wholly off-topic answer or valid refusal receives zero task performance; an empty refusal has no assessable written-explanation index. Partial returned answers are assessed as received and marked partial. Missing or transport-uncertain answers receive no score, not zero.

For essays and experimental designs, the item score is Q2. For research reasoning:

**Research score = 60 × qualified historical-direction Hit@1 + 0.40 × Q2.**

Hit@1 retains the five-component definition: biological question, mechanism, intervention, readout and predicted outcome must jointly match the sealed continuation without a critical control or inference failure. Keywords or a paper name do not qualify. Missing matching review stays unavailable. A new Methods-lookup omission does not automatically invalidate a direction hit; an actual causal or measurement failure can. Reassess the saved matching evidence; explain any correction in round two without changing round one. The 60/40 amendment applies to both rounds and is also post-hoc.

When all 30 items for a model are available, total = **0.20 × essay mean + 0.30 × design mean + 0.50 × research mean**. Category denominators are ten. Do not prorate missing questions or compare unequal subsets as full scores. A complete score for one model does not create a complete roster ranking.

## Decision states and evidence

Every applicable check receives `met`, `unmet` or `not_applicable`, with a specific reason. A materially incomplete or incorrect implementation is `unmet` and incurs the full stated deduction; there are no arbitrary half penalties. Exact wording is unnecessary: scientifically equivalent explanations qualify. A mere keyword, list heading or promise to determine everything later does not.

Record the criterion ID, points, exact answer quote and an explanation of the missing causal or operational requirement. For an absence, record `absent_after_full_read` and the nearest relevant passage or a whole-answer scope statement. Do not invent a quotation. A quote anchors the review; it is not an automatic keyword score. Record candidate SHA-256, question/reference version, rubric hash and any reference correction.

Before charging two checks, identify the **distinct missing actions and distinct consequences**. Charge one underlying defect once, using the most specific criterion; if two checks describe the same defect, use the larger penalty and mark the other `covered_by`. For example, an absent negative control belongs to C, not also G2 and P03. An absent Methods plan and an absent quantitative calibration procedure are different missing actions and can both be charged. Multiple absent concentrations in one intervention are one P02 failure, not an unlimited penalty per number. All applicable distinct failures count even if the score has already reached zero; record uncapped and capped totals.

## Ten-point checks

| ID | Deduction | Full satisfaction |
|---|---:|---|
| C | 10 | In a molecular, biochemical or circuit experiment, explicitly plan to verify what the relevant positive, negative and procedural controls establish, and design the necessary controls **before** experimental data collection. Explain the comparison and how each control rules in or out an alternative. This is one combined check: missing either definition verification or prospective design costs ten once. A literal internet search is not required. |
| M | 10 | Across all four domains, explicitly propose consulting and checking prior papers' Methods, supplements or validated protocols **before execution**, to select detailed conditions and verify transfer to the present system. A generic citation, 'standard methods', future documentation or unnamed optimization is insufficient. No actual browsing is expected or rewarded. |

C applies to the wet-lab/circuit study or validation requested by the question. It does not require unrelated viral, PCR or microscopy controls. Purely computational questions use their applicable validation checks below. M applies to every current item because each asks for an experiment, analysis or falsifying/validation check, including essay validation components.

## Five-point scientific-content checks

| ID | Deduction | Failure condition |
|---|---:|---|
| G1 | 5 per independent error; maximum 20 | A substantive factual, mathematical, unit or tool-principle error not already charged under a more specific check. Enumerate the independent propositions; restatements count once. |
| G2 | 5 per independent omission; maximum 20 | An explicitly requested central concept or task component is absent. Identify it from the frozen prompt, not an invented hidden expectation. Specific procedural checks take precedence. |
| G3 | 5 | The observation → comparison → inference → conclusion chain is missing, reversed or non-identifying. Distinguish evidence from a mechanism-compatible story. |
| G4 | 5 | A consequential competing explanation and a discriminating test are missing or scientifically invalid. Research questions need competing mechanisms and differing predictions, not labels alone. |
| G5 | 5 | The conclusion exceeds the data: association becomes causation, a proxy becomes the target, a null becomes proof of absence, or a contested source becomes proof of intent. |
| G6 | 5 | The answer materially fails the requested format or word limit, or is so disorganized that the required decision/procedure cannot be followed. Shortness alone is not failure. |
| G7 | 5 | Proposed, measured, externally established and unknown quantities are not distinguished; fabricated source conditions or claims of unperformed execution appear. |
| G8 | 5 | A research answer lacks a biologically meaningful unresolved question that follows from the supplied packet. A scientifically valid alternative direction can pass despite missing the historical target. |

## Five-point execution checks

Each listed ID is a single five-point check, not five points per noun in its description. The applicability table distinguishes full protocols from essay-scale validation.

| ID | Full satisfaction |
|---|---|
| P01 | Select an identifiable system, material/data source and feasible assay or computational platform, with prerequisite identity/integrity checks. Unknown source facts are explicitly marked and resolved through a defined plan. |
| P02 | Give an ordered preparation/intervention workflow with relevant quantities, units, timing and settings, or a concrete calibration procedure that will set unknown values before confirmation. A list of unspecified settings is insufficient. |
| P03 | Specify assay-specific calibration and interference/artifact controls: what is measured, reference/blank, acceptance criterion and the action when calibration fails. C owns absent biological/procedural controls; this check concerns independent measurement calibration. |
| P04 | Define a quantitative endpoint, units/denominator, baseline or background correction and rules for weak, saturated or missing measurements. Merely naming 'fluorescence', 'viability', a cluster or a figure is insufficient. |
| P05 | Identify the independent allocation unit and nested subsamples; specify independent replication and a justified precision/power or pilot plan. More cells, wells or trials cannot replace missing treatment replication. |
| P06 | Specify applicable randomization, allocation concealment, blinding and balanced processing. If infeasible or irrelevant, explain the limitation and an equivalent bias-control measure. |
| P07 | Predefine inclusion, exclusion, attrition and stopping rules independent of desired outcomes. Preserve biological nonresponses and report denominators. |
| P08 | Define the primary contrast/statistical estimand, model assumptions, uncertainty and multiplicity handling where needed. No automatic significance-to-mechanism inference. |
| P09 | Explain the principle and assumptions of the core measurement/inference tool and where it cannot identify the target. For computational work, explain the model's relevant likelihood, transformation or integration logic rather than name software alone. |
| P10 | Specify a bounded parameter/sensitivity exploration, its evaluation criterion and a lock before confirmatory testing. Do not tune until the desired biological result appears. |
| P11 | Anticipate at least one plausible failure with a diagnostic measurement, alternative cause and ordered repair/retest. Generic 'optimize' is insufficient. |
| P12 | Plan iteration over technically failed or ambiguous work, including what is frozen, what may change and what needs fresh independent confirmation. Recognize that the biological hypothesis can be wrong; repeated attempts do not justify selective reporting. |
| P13 | Give discriminating supportive, negative and ambiguous outcomes and identify what would falsify or materially revise the proposed mechanism. G4 owns absence of competing mechanisms; this check owns the experiment's decision rule. |
| P14 | Make independent or orthogonal validation operational and explain the remaining uncertainty. Reusing discovery labels/markers or the same artifact-prone readout is not independent confirmation. |
| P15 | Preserve raw inputs, provenance, sample/event identifiers, versions, code/settings and analysis outputs sufficient for audit. Record actual execution status. Computational work needs an immutable manifest and reproducible environment/commands. |
| P16 | Computational work: protect discovery/tuning/holdout separation at the independent sample/donor level, keeping fitted transformations inside folds; prevent endpoint/label leakage. If no learning/tuning occurs, justify N/A and preserve an independent confirmation design. |
| P17 | Computational work: address confounding, missingness, appropriate null or baseline comparisons, and stress tests without erasing biology. A visually pleasing embedding is not validation. |
| P18 | Computational work: specify numerical outputs behind target figures, a clean-environment rerun, tolerances for stochastic steps, resource/failure logs and a source-difference audit. No files supplied means a plan only, never reproduction credit. |

## Calibration and assay-specific implementation

Precision must be justified, not invented. Where the prompt explicitly withholds settings, P02/P10 can be met by naming the exact variable and unit, a defensible proposed starting range or a procedure to derive it, a pilot design, an objective acceptance rule, and when the setting will be frozen. A proposed value is labeled proposed; an unknown historical value stays unknown. For quantities that cannot be set responsibly before a source/system is identified, specify the prerequisite and a concrete lookup/calibration-to-decision procedure. 'Determine locally' alone fails.

Evaluate only techniques needed for the question or essential to the candidate's chosen causal claim. Equivalent nonviral or non-PCR routes are allowed. If a chosen technique is central, apply these details within P02–P04/P10, not as duplicate extra deductions:

- Viral delivery: identity, functional titer/dose with units, target amount/cell number, exposure/expression timing, expression distribution and toxicity checks.
- PCR: template and amplicon identity/length, primer-validation plan, reagent amounts, cycling/extension logic, product identity and quantitative efficiency where relevant.
- Enzymatic processing: correct substrate identity, amount, enzyme activity, volume/buffer, temperature/time, conversion measurement and time/enzyme titration. DNA restriction digestion is not RNA digestion; no universal 'minutes per ng' is assumed.
- Fluorescence/imaging: acquisition settings, dynamic range, background/reference, ROI/cell selection, intensity or positive-frequency denominator, motion/bleaching and independent readout validation.
- Biochemical reconstitution: component purity and amounts, stoichiometry, buffer/ions, temperature/time, mass/energy balance where relevant and artifact-resistant product measurement.
- Neural experiments: population and intervention localization, expression/light/stimulation calibration, behavioral and sensory/motor controls, synchronized physiology, allocation unit and humane approval prerequisites where applicable.
- Computational pipelines: accession/input schema, reference releases, normalization/model choices, contrasts, filtering, parameter ranges, seeds, split boundaries, code/environment and quantitative target outputs.

Unsolicited optional techniques do not create an unlimited penalty surface. Assess the primary proposed route and any additional experiment on which the answer's claimed conclusion depends. Record that selection before checklist scoring.

## Frozen applicability for the 30 items

All items: M and G1–G7. Research items also G8. C applies to all `mol`, `bio` and `neu` items; bioinformatics essays do not acquire C merely by mentioning a possible future wet-lab validation. Item-specific checks are tied to the supplied task, not to later-paper details.

| Profile | Items | Additional applicable checks | Expected scope |
|---|---|---|---|
| V | mol-k01, mol-k02, mol-p01, bio-k01, bio-k02, bio-p01, neu-k01, neu-p01 | P03, P04, P13, P14 | A technically interpretable, quantitative falsifying/validation check; not a full surgical or assay SOP. |
| A | inf-k01, inf-p01 | P08, P09, P13, P14, P17 | Correct association/causal and provenance reasoning; calibrated validation logic, confounding and tested universe. |
| W | mol-d01, mol-d02, bio-d01, bio-d02, bio-d03, neu-d01, neu-d02, mol-r01, mol-r02, mol-r03, bio-r01, bio-r02, neu-r01, neu-r02, neu-r03 | P01–P15 | A complete proposed wet-lab, biochemical or neural study. |
| B | inf-d01, inf-d02, inf-d03, inf-r01, inf-r02 | P01–P18 | An auditable computation/analysis and independent validation plan; P06/P16 may be N/A only under the explicit structural exceptions above. |

Within those profiles, identify case-specific obligations directly from the question: for example, matched damage and arrest-versus-death measurement; buffer/ion add-back; isotope tracing and carbon balance; paired imaging/spiking; allocation-level replication; or leakage-free multimodal validation. Do not require unrelated techniques. Conditional N/A requires an explicit scientific justification and must be applied identically to equivalent answers.

## Explanation, cost and time

Separately score the **visible scientific explanation** on four original 0–4 dimensions: factual correctness, evidence grounding, causal validity, and alternatives/limits, equally weighted. Anchors: 0 absent/wrong; 1 isolated valid elements with major gaps; 2 partly useful but substantial correction needed; 3 sound with noncritical gaps; 4 fully satisfies the item. This is not hidden-chain-of-thought accuracy, and it does not get added again to Q2.

Report confirmed API charges separately from unresolved reservations; account balance is not proof that an uncertain request was unbilled. Response time includes provider/network waiting; summed request seconds are not wall-clock project duration. No judge API, answer regeneration or new charge is needed for rescoring. Do not retry valid refusals or uncertain calls.

Publish both rounds' available-item coverage, category denominators, score changes and limitations. A written plan does not establish a successful laboratory experiment or raw-data pipeline execution. Historical matching is retrospective and vulnerable to training contamination, not proof of independent discovery.
