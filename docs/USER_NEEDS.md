# What a useful research assistant should help users do

The benchmark's purpose is to identify assistants that improve research decisions and execution. The following are proposed user needs and evaluation designs, not claims of measured performance.

| Researcher's need | Useful assistance | Observable evaluation target |
|---|---|---|
| Understand a mechanism | Explain what was observed, why the experiment was informative, what remains uncertain, and how the finding applies to the user's system. | The user can distinguish evidence from inference and predict the effect of a new perturbation. |
| Choose a worthwhile question | Identify an unresolved issue, competing explanations, practical relevance, and a tractable way to distinguish them. | The proposed question remains meaningful after checking the supplied literature and can change a scientific decision. |
| Plan an experiment | Turn the question into a feasible protocol with controls, independent units, allocation, measurements, analysis and outcome-dependent decisions. | An independent researcher can identify all prerequisites and execute or explicitly resolve every blocking input. |
| Diagnose a failed or contradictory experiment | Prioritize plausible causes and inexpensive discriminating checks, rather than list every possible cause. | A held-out fault or alternative explanation is resolved with a recorded number of steps, cost and consequential errors. |
| Analyze biological data | Check identities and assumptions, run a reproducible workflow, recover numerical results and explain which conclusions survive sensitivity analysis. | Independent execution from frozen raw measurements regenerates the specified tables and figures within justified tolerances. |
| Assess an unreliable claim | Trace an observation to a measurement problem and its consequence for a specific inference; consider benign alternatives and contrary evidence. | Detect substantiated problems while avoiding unsupported accusations in matched reliable controls. |
| Decide what to do next | Compare options using the user's equipment, samples, time and budget; prioritize the experiment with the greatest decision value. | The next action is feasible and its positive, negative and ambiguous outcomes lead to explicit, defensible decisions. |
| Maintain a trustworthy research record | Preserve versions, evidence, failed attempts, exclusions and unresolved inputs; communicate a concise recommendation with supporting detail. | Another researcher can reconstruct what was done, what was only proposed, and why a decision changed. |

## Author each task around a real decision

Record the user's objective, biological system, current evidence, constraints, immediate decision, expected deliverable and observable success condition. State which resources and supplied evidence the evaluated model can use. Missing information can be intentional: an excellent answer may identify a blocking input and give a conditional plan instead of inventing a number.

For example, a perturbation that lowers a viability readout should lead to a decision about what to check next: assay interference, cell number, target engagement, an independent readout or a rescue. The task should reward a justified order and explain how each result changes the interpretation. Merely naming every possible control does not establish that the researcher was helped.

Detailed protocols belong in experimental-design and research-reasoning answers, but detail must remain operational and traceable. A concise recommendation followed by an ordered protocol is more usable than an undifferentiated methods dump. The long reference-answer requirement checks authoring coverage; it does not require a model to pad its answer. Proposed parameters must remain distinguishable from source-reported parameters.

## Score benefit, then diagnose the reason

The primary score uses scientific accuracy (35%), decision value (25%), actionability (20%), verifiability (15%) and communication (5%). These initial weights require expert calibration. Technical concept coverage, directed logic, protocol detail and historical follow-up matching explain strengths and weaknesses; they do not replace utility. A feasible, informative new research direction can score highly even if the historical author pursued something else.

Research reasoning provides five independent opportunities, but the report also preserves first-attempt performance and the cost of all attempts. Best-of-five performance assumes that a reviewer can select the useful answer. It is not equivalent to a user receiving one reliable answer without that selection effort.

Before using the benchmark to recommend an assistant, run a blinded user study: researchers attempt a prespecified next step with and without assistance under comparable conditions. Record scientific correctness, completion, consequential mistakes, time, resources and unresolved inputs. Include negative and ambiguous outcomes, failed workflows and justified decisions to stop. Satisfaction is informative but cannot compensate for a wrong biological conclusion. This workbench has not yet completed that validation.
