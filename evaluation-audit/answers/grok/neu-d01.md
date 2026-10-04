# Grok 4.7 / neu-d01

Original final answer, shared by both scoring rounds.

The projection-specific necessity claim is supported only by an interaction: retrieval-timed terminal inhibition in Q must reduce correct choices in opsin animals beyond any change produced by identical, equally visible light in opsin-negative animals, and that choice effect must not be accounted for by locomotion impairment. Do not illuminate somata in P and treat the result as a P→Q test.

## Evidence → inference → conclusion

O1 states that P projects to Q and to another region. Inference: silencing P cell bodies, even if those cells were labeled from Q, can alter output to the other region if the same neurons collateralize, and it does not isolate synapses in Q. Conclusion: the necessity manipulation has to be light delivered at P terminals in Q. Soma illumination is only a physiological positive control and cannot carry the projection claim. Whether the Q-projecting cells are the same cells that innervate the other region is unknown; that is a histology question, not something to assume.

O2 states that an inhibitory opsin can be targeted to P neurons that project to Q. Inference: a loss-of-function restricted to that population is feasible, but expression in those neurons is not the same as silencing their synapses in Q. Conclusion: pair projection-targeted expression with terminal light in Q, and verify both expression location and functional suppression before interpreting behavior.

O3 states that the proposed outcome is correct choices while the task also requires locomotion. Inference: a drop in accuracy can be produced by failing to move, moving late, or taking an altered path, rather than by failing to retrieve the cue. Conclusion: accuracy on completed choices, omissions, and kinematics must be separate endpoints, and inhibition during locomotion outside retrieval must be tested with the same light parameters.

O4 states that light delivery can be visible. Inference: a flash at cue time can distract, mask, or become an extra cue, and that artifact is itself epoch-specific. An effect limited to the retrieval window therefore does not rule out a sensory confound. Conclusion: every light schedule used in opsin animals must be delivered, with matched visibility, to opsin-negative animals that have the same implants. Epoch specificity is necessary but not sufficient.

Joint conclusion: P→Q is necessary for cue retrieval only if all of the following hold. Retrieval-window light at Q terminals lowers correct-choice probability in opsin animals relative to interleaved no-light trials. The same contrast in opsin-negative animals is smaller, so the group × light interaction is the primary result. The same light during locomotion that does not overlap retrieval does not reproduce the choice deficit, and kinematic covariates do not remove the retrieval effect. Post-offset behavior is not the sole locus of the effect, which would suggest rebound rather than retrieval loss. Histology and a silencing calibration show that light reached P axons in Q and suppressed transmission at the power used. If any of those fail, the data do not support necessity.

## Relationships among the concepts

The causal target is synaptic output of P→Q during the retrieval epoch, not P activity in general, not Q activity in general, and not performance averaged across the trial. Choice accuracy is a downstream readout that shares a motor path with locomotion, so it is not a pure retrieval measure. Visible light is an independent sensory input that can enter the same epoch as the cue. Controls are therefore crossed with the manipulation, not stacked as optional checks: projection site (terminals in Q versus somata in P), time (retrieval versus locomotor epoch versus inter-trial interval), and light path (opsin versus no opsin, same visible light).

## Unknowns and how to calibrate them

No species, cue modality, geometry, opsin, power, wavelength, window length, laterality, or trial count is given. Do not fill these in from a favored paper. Fix them with the procedures below and lock the numbers in a protocol before the primary cohort.

Cue–movement overlap. Record a no-light baseline until performance is stable by a pre-set accuracy and omission rule. From the reaction-time distribution, define retrieval as the interval from cue onset until the earliest reliable choice-commitment movement. If cue sampling and locomotion always overlap, do not invent a separation. Either add a task epoch in which the cue is delivered while the animal is still, with a later go signal, or accept overlap and rely on the locomotor-epoch control plus kinematic matching. Report which of those two was true.

Light power, duty cycle, and heat. Measure power at the fiber tip with a meter before every session. In a bench or ex vivo calibration, map temperature next to the fiber across power and duration. Set the maximum allowable temperature rise from the institutional animal-care limit before any behavioral test, and discard powers that exceed it. In a separate pilot, not the inference cohort, find the lowest power and the shortest duration that suppress P→Q transmission, using a transmission assay appropriate to the lab’s available method (evoked synaptic response, terminal calcium, or a transmitter indicator). Use that minimum effective setting. Choose continuous versus pulsed light from the opsin construct’s documented kinetics plus that pilot, not from a default. Confirm the same setting does not produce a lasting choice or motor change after light offset in the pilot.

Opsin class at terminals. Somatic silencing does not validate terminal silencing. Some inhibitory opsins suppress axons poorly or can increase terminal release. Run the transmission assay at the Q terminals with the actual construct. If the construct does not suppress P→Q output, do not start the necessity cohort with that construct.

Laterality and collaterals. In a tracing subset, determine whether P→Q is uni- or bilateral and whether Q-projecting P neurons also innervate the other region named in O1. Illuminate the terminal fields that the tracing shows are required to cover the projection. Do not assume bilateral implants. Collateralization changes interpretation of any soma control; it does not replace terminal light.

Visibility. In the real box, with the real implant and the room lights used in testing, measure light leak with a camera or sensor at the animal’s position. If leak is detectable, either eliminate it by shielding that does not block the task cue, or match that leak in every control. Record cue modality. If the cue and the leak share a modality, add a cue-detection or cue-sampling measure in opsin-negative animals; a retrieval-timed accuracy drop in those animals means the light is competing with the cue.

Sample size. From a calibration cohort, estimate variance of the group × light contrast on completed-trial accuracy and of the kinematic covariates. Set N from that variance and a pre-specified smallest effect you intend to interpret. Do not choose N after seeing the primary result.

Expression time. Run a short histology time series for the actual constructs and coordinates. Start behavior only after terminal labeling in Q and restricted somata in P are reliable in that series.

## Ordered protocol

### 1. Preparation and quality checks

Define the trial in writing before surgery: cue onset, retrieval window, choice commitment, locomotor completion, outcome, and inter-trial interval. The primary behavioral endpoint is probability of a correct choice given a completed choice. Secondary endpoints, all pre-specified, are omission or timeout rate, choice latency, speed, path length, trajectory deviation, and post-offset choice probability.

Prepare two cohorts with identical fibers aimed at P terminals in Q. Experimental animals receive projection-targeted inhibitory opsin in P neurons that project to Q, using the targeting route justified by O2. Control animals receive a non-opsin reporter via the same route and the same fiber hardware. Do not use unoperated animals as the light control.

Quality checks before an animal enters analysis: stable baseline performance; fiber-tip power within the calibrated range; implant and shielding unchanged; video and light TTL on a common clock. After the experiment, accept an animal only if histology shows opsin or reporter in P neurons labeled from Q, terminal label under the Q fiber, and no substantial off-target expression that would make the light non-selective. Fiber placement outside that terminal field is a miss.

In a separate pilot set, complete the transmission, heating, visibility, laterality, and collateral calibrations above. Do not mix pilot animals into the confirmatory contrast.

### 2. Independent units

The animal is the independent unit for inference. Trials and sessions are repeated measures nested in animal. Cells, fibers, or video frames are not independent samples. Plan the analysis and the sample size at the animal level. A physiological silencing pilot may use slices or sessions as its own units, but those results only calibrate the intervention; they are not the necessity result.

### 3. Allocation and blinding

Randomize animals to opsin versus reporter before surgery, balanced across cages and surgical days. Within animal, interleave retrieval-light and no-light trials in every test session so slow drifts are shared. Run the other-epoch conditions (locomotor epoch and inter-trial interval) as separate, counterbalanced sessions or blocks with the same power and duration, not as a post-hoc subset of bad trials.

Code group and light condition so that choice scoring, kinematic scoring, and histology inclusion calls are made without knowledge of opsin status or of which trials were illuminated. Automated port or video scoring is preferable. Light-on trials may be visible to the animal; that is the confound O4 requires you to control, not a reason to skip blinding of scorers. The surgeon and the person who sets power may know group; the person who locks inclusion and the person who runs the primary model should not, until the inclusion list is frozen.

### 4. Intervention and sampling

Test only after baseline performance meets the pre-set stability rule. On each test day, verify tip power, then run interleaved retrieval-light and no-light trials. Light onset and offset are TTL-locked to the pre-defined retrieval window and to nothing else on those trials. No-light trials use the same trial structure with the light source armed but not emitted, so handling and sound are matched as far as the hardware allows. If the hardware click is audible, the no-light trials must include that click.

On other days, deliver the same power and duration locked to locomotion that does not overlap retrieval, and, separately, to the inter-trial interval. Order these epoch sessions by a counterbalanced schedule across animals. Do not increase power if the first sessions are null; power stays at the calibrated minimum effective setting.

Sampling rule: collect a pre-specified number of completed choices per light condition per epoch, based on the calibration variance. Stop a session for welfare criteria below, not because accuracy moved. Record continuous video and port events on the same clock as the light TTL.

Soma light in P, if used at all, is a separate positive-control condition in a subset and is labeled as a cell-body manipulation. It is not pooled with terminal-light trials.

### 5. Measurements

For every trial, store cue time, light state, epoch, choice identity, correct or incorrect, completion, latency to commitment, and kinematic summaries from video. Derive a cue-sampling measure appropriate to the cue modality, calibrated in pilot animals, so you can tell failure to acquire the cue from failure to use it. Store fiber power for that session. Store a leak measurement whenever shielding or room light changes.

From histology, store fiber-tip coordinates relative to the terminal field, expression laterality, and a collateral score to the other region. These are covariates and inclusion factors, not optional notes.

### 6. Controls and what each one rules out

Reporter animals plus identical retrieval light rule out visible light, heat, implant, and strategy shifts caused by a flash at cue time. They are mandatory because of O4.

No-light trials inside the same opsin animal rule out nonspecific poor performance and give the within-animal contrast.

Locomotor-epoch light at the same site and power tests the O3 motor confound. If this condition impairs speed or completion as much as retrieval light does, a retrieval-specific claim is not available from accuracy alone.

Inter-trial light tests prolonged suppression, rebound, and general disruption outside the cue.

Completed-trial accuracy versus omission rate separates “wrong choice” from “did not move.” Kinematic matching, described below, asks whether the accuracy effect survives when movement is comparable.

Terminal versus soma light, interpreted with the collateral histology, separates a Q-synapse effect from silencing all outputs of Q-projecting P cells.

A post-offset analysis window checks rebound. An effect that appears only after light ends is not evidence that the projection was required during retrieval.

### 7. Analysis

Freeze the inclusion list from histology and pre-set behavioral exclusions before fitting the primary model. Pre-set exclusions should include unstable baseline, power outside the calibrated range, fiber miss, and absent terminal expression. Exclusions are by animal, not by inconvenient trial.

Primary model: a mixed-effects logistic regression of correct choice on completed trials, with group (opsin vs reporter), light (on vs off), and their interaction, plus random intercepts for animal and, if sessions vary, session nested in animal. The confirmatory estimate is the interaction: the on-minus-off change in the opsin group minus the same change in the reporter group, under retrieval-timed terminal light. Report the estimate and interval, not only a significance call.

Fit the same contrast for locomotor-epoch and inter-trial light. A retrieval claim requires the retrieval interaction and requires that the locomotor-epoch interaction not account for it.

Separately model omissions, latency, speed, and path. Then refit the primary accuracy model with the pre-specified kinematic covariates, and, as a sensitivity check, refit on a movement-matched subset defined by a rule locked before unblinding. If the interaction disappears once movement is accounted for, do not claim retrieval necessity.

Check the post-offset window with the same model structure. Check cue-sampling in reporter animals as the sensory-competition test.

Do not drop animals or conditions because the effect is in the unexpected direction. Do not analyze trials as if they were independent animals.

### 8. Acceptance, welfare stopping, and interpretation rules

Accept a necessity conclusion only if the retrieval-window group × light interaction is in the direction of fewer correct choices under opsin light, the reporter retrieval contrast does not explain it, locomotor-epoch inhibition plus kinematic analyses do not explain it, the post-offset window is not the sole effect, and QC confirms terminal targeting and the calibrated suppression setting. Otherwise report a dissociation failure or a null, not a qualified necessity claim.

Stop light delivery in an animal if you see seizure-like events, persistent freezing, inability to complete the locomotor requirement, or implant damage. Those animals are welfare stops, not silent exclusions: report them. An experiment-level interim look at the primary interaction is allowed only if the spending rule was registered before that look. Otherwise finish the pre-specified N.

### 9. Troubleshooting

No terminal expression: stop behavioral inference for that animal. Recheck the targeting route and the expression-time series; do not raise light power to compensate for missing opsin.

Expression present, transmission assay shows no suppression: the behavioral test is not yet a necessity test. Change duty cycle or power only inside the pre-set heat limit, or change construct, and repeat the transmission assay. Do not interpret a behavioral null until suppression is shown.

Accuracy drops in reporter and opsin animals: treat this as a sensory or heat confound. Reduce leak, add cue-modality-safe shielding, or lower power while rechecking suppression. Do not add more opsin animals to “overcome” a control effect.

Accuracy drops only in opsin animals but speed, path, or omissions change, and locomotor-epoch light does the same: the result is compatible with a motor role of the projection. It is not evidence that the projection is required for cue retrieval. Separate cue and movement in the task and repeat, or restrict the claim to performance during movement.

Effect only after light offset: suspect rebound or a lingering sensory cue. Shorten illumination using the kinetics calibration, and do not call the offset effect retrieval necessity.

Effect at every epoch including the inter-trial interval: the manipulation is not retrieval-specific. Check fiber location, power, and whether light is suppressing a general contribution of P→Q to arousal or movement.

Soma light produces an effect and terminal light does not, with confirmed terminal suppression: the Q synapse was not necessary under this task; a cell-body effect may reflect the other projection in O1 or collaterals. Report that boundary explicitly.

## Alternatives and limits

If the scientific question were only whether Q-projecting P neurons matter at some time in the trial, soma inhibition or a slow projection-targeted chemogenetic manipulation could be informative. Neither can support necessity during cue retrieval. Chemogenetics lack the epoch resolution this question requires. Exciting the projection would test sufficiency or gain, which is a different claim and is not requested.

Terminal inhibition can be incomplete, can alter local ions, and can fail even when somatic inhibition works. That is why the transmission calibration is an acceptance condition. Antidromic effects from terminal light are not fully excluded by this design; a clean somatic silencing control that does not match the terminal behavioral effect reduces, but does not eliminate, that concern. Visible-light controls do not cover every non-optical sensation if the fiber click or heat differs; match those in hardware. A null result means this inhibition did not reveal necessity at this power and window, not that the projection is unused. A positive interaction still does not identify which downstream computation in Q failed.

## What would change the recommendation

Change the primary manipulation if tracing shows that the behaviorally relevant axons are not under a Q fiber, or if no available inhibitory construct suppresses P→Q transmission within the heat limit. In that case, do not force a behavioral cohort; the tool does not match the claim. Change the epoch rule if baseline behavior shows no stationary retrieval interval and a task revision cannot create one: the locomotor control then becomes co-primary, and a pure retrieval conclusion should be abandoned in advance. Change the sensory-control weight if leak cannot be made undetectable and the cue shares the leak’s modality: cue-detection in reporter animals becomes an acceptance criterion, not a secondary plot. A collateral result from O1 changes only the soma-control sentence, not the decision to use terminal light.
