# Grok 4.7 / inf-r01

Original final answer, shared by both scoring rounds.

The next action is to lock a pre-specified comparison of unshrunk count-model fold changes against cross-gene dispersion sharing plus a Normal prior on effects, then run that comparison as a methods-direction forecast. Do not treat any output as a reproduction of published biology. The evidence packet supports the rationale for shrinkage when replicates are few and counts are low or variable, but it does not establish the distribution of true biological effects, so a Normal-prior method is a testable proposal, not a settled recovery of real expression changes.

## Unresolved question

In a two-condition gene-level RNA-seq contrast with few biological replicates, which apparent expression changes are recoverable count-level differences rather than unstable estimates, and does sharing dispersion information across genes together with a Normal prior on effects recover those differences—including strong, high-information effects—without treating low-information extremes as biological signal?

“Recovered” here means a gene-level log-fold difference that is stable in independent biological material from the same contrast and is not an artifact of sampling variance. It does not mean a demonstrated transcriptional, compositional, or isoform mechanism. No dataset, accession, parameter value, or numerical result is supplied by the packet, and none is claimed as observed.

## Evidence, inference, and conclusion

Evidence in the packet:

- Gene-level expression differences are estimated with a count model.
- With few biological replicates, low or variable counts can yield unstable fold-change estimates.
- A described method stabilizes dispersion and fold-change estimates by sharing information across genes and placing a Normal prior on effects.
- That packet establishes a rationale for shrinkage.
- It does not supply evidence about every possible underlying distribution of biological effects.

Inference from that evidence alone:

- Instability is an information problem. An extreme unshrunk fold change is not, by itself, evidence that the biological effect is large or that it is null.
- Shrinkage should matter most where the count likelihood is weak: few replicates, low counts, or high dispersion. That is a prediction, not a measured result.
- Where the likelihood is strong, a Normal prior need not erase a large effect, but only if the prior is not so tight that it dominates even informative genes. Prior mean and variance are unreported, so preservation of strong effects must be tested rather than assumed.
- Because the effect distribution is not established, the same Normal prior can over-shrink true large effects if they are heavier-tailed, more discrete, or more asymmetric than the prior. That possibility is a required stress test, not a side note.

Conclusion for action: proceed only with a falsifiable, two-arm evaluation—simulation under a stated generative model, plus independent validation on an eligible raw-read dataset not used to fit the estimator. A pass supports a methods-direction forecast under the tested conditions. It does not reproduce a published biological result.

## Competing explanations and distinct predictions

Four explanations can produce the same extreme fold-change list. They are hypotheses, not findings.

1. Sampling instability. Low or variable counts and few replicates make the unshrunk estimator swing to large values, including from near-zero counts in one condition. Prediction: extreme unshrunk estimates concentrate in low-information genes; shrinkage reduces their error; high-information large effects keep sign and most of their magnitude.
2. Heavy-tailed or sparse true biology. A minority of genes truly change by a large amount, including among well-counted genes. Prediction: large effects are not confined to low counts; a tight Normal prior attenuates high-information large effects; a wider or heavier-tailed prior fits the strong-effect stratum better. The packet does not rule this in or out.
3. Technical shift rather than condition biology. Library composition, batch, strand, or quantification differences move counts. Prediction: error tracks technical factors more than count level, and shrinkage does not improve an independent replicate set that shares the same artifact—or it falsely “improves” agreement only when the artifact is shared.
4. Mean–variance misspecification. Dispersion sharing assumes genes are exchangeable after conditioning on expression level. Prediction: a subset of genuinely overdispersed genes is over-stabilized; gene-wise dispersion fits those genes better, and the harm appears in the high-dispersion tail rather than only in low counts.

These predictions are separable. Instability predicts benefit stratified by information. Heavy-tailed biology predicts loss of strong high-information effects. Technical bias predicts failure of independent validation despite simulation success. Dispersion misspecification predicts harm concentrated in dispersion outliers. A result that mixes these patterns is ambiguous, not a partial win to be narrated as success.

Biological generators of a true gene-level change—transcriptional regulation, cell-composition shift in bulk RNA, or isoform usage collapsed to a gene count—are not distinguished by this design. Recovering a count-level difference leaves that mechanism unresolved.

## Proposed method

Proposed estimator, not a completed analysis: fit a gene-level overdispersed count model; estimate gene-wise dispersion and moderate it by sharing information across genes; estimate the condition log-fold effect with and without a Normal prior on that effect; compare the two estimators. The packet names a count model, dispersion, cross-gene sharing, and a Normal prior. It does not name software, prior variance, prior mean, degrees of freedom, normalization, or filters. Those are unreported parameters.

Assumptions, each labeled as an assumption:

- The mean–variance relationship is an overdispersed count model, not a Gaussian model on raw counts.
- The target parameter is a gene-level log-fold change between two pre-specified conditions.
- Genes are partially exchangeable for dispersion sharing after accounting for expression level.
- The Normal prior is centered at no systematic directional bias unless metadata justify another center. The packet does not state the center or the variance.
- “Few replicates” means the likelihood is weak relative to a moderate prior for low-count genes. The numerical replicate count of any future dataset is unreported.
- Independent validation assays the same contrast. A different treatment, tissue, or time point is not validation.

Unreported parameters that must be locked before outcome inspection, and must not be tuned after seeing error:

- Prior variance, and whether it is fixed or estimated from the estimation set only.
- Strength of dispersion sharing.
- Size-factor or compositional normalization.
- Any minimum-count filter. Aggressive filtering would remove the low-information extremes the question is about, so the primary analysis should retain low-count genes and stratify by information. A filtered analysis may be secondary only.
- The preservation and extremity thresholds defined below.
- Quantification tool, genome build, and annotation. These are operational choices, not evidence that the method works.

No implementation is treated as proof. If two implementations of the same specification disagree, that is an ambiguity about the estimator, not a biological result.

## Evaluation protocol

This is a proposed protocol. No step below has been run.

### 1. Lock the plan

Write the eligibility rules, strata, thresholds, simulation designs, and conditional conclusions before selecting the analysis dataset and before estimating effects. Sensitivity analyses are secondary. They do not replace a failed primary criterion.

### 2. Dataset eligibility

A dataset is eligible only if all of the following hold. No specific study is nominated here.

- Raw reads exist, not only a count matrix, so provenance can be checked.
- Two conditions define one contrast of biological interest, with sample labels independent of the expression matrix.
- The estimation arm is in the few-replicate regime the packet addresses. Proposed operational range: 2–3 biological replicates per condition. Technical replicates are not biological replicates.
- An independent arm exists: additional biological replicates of the same contrast, withheld entirely, or a separate cohort with the same contrast and documented raw reads. If only two or three replicates exist in total, independent validation is impossible; do not relabel a resample of the same samples as independent.
- Organism, assay type (bulk RNA-seq versus other), and pairing or blocking structure are documented. Hidden pairing is an exclusion, not a covariate to invent.
- Exclude contrasts whose condition label is confounded with a single batch, unless an explicit batch term is pre-specified and identifiable. If it is not identifiable, the dataset fails eligibility rather than being “corrected” after the fact.

If no dataset meets these rules, stop at simulation. That outcome is a limit, not a biological conclusion.

### 3. Raw-read provenance

Before alignment or counting, record for every sample: repository, accession, download date, file checksum, layout, nominal read length, strandedness if known, instrument if known, donor or animal identifier, biological versus technical replicate status, condition, and known batch factors. Record the reference sequence and annotation versions and the quantification procedure and version once chosen.

If strandedness, read length, or batch is unreported, state that uncertainty and do not impute a convenient value. Samples that fail pre-locked sequence-quality rules are excluded with a written reason before model fitting. Do not exclude samples because their fold changes look extreme; that would circularly remove the phenomenon under test.

Provenance supports trust in the input. It does not validate the shrinkage model.

### 4. From reads to a count matrix

Proposed processing, parameters unreported until locked: quantify to gene-level counts with one pre-specified annotation; do not mix gene-level and transcript-level targets in the primary endpoint. Apply one pre-specified normalization so library size and gross composition are not mistaken for condition effects. Keep the estimation matrix and the validation matrix separate. Do not pool them to estimate the prior, the dispersion trend, or the size factors.

### 5. Estimation

For each gene, compute:

- An unshrunk count-model fold-change estimate and its standard error or another pre-specified curvature summary.
- A dispersion estimate after cross-gene sharing, plus the unshared gene-wise estimate for the misspecification check.
- A shrunk fold-change estimate under the Normal prior, using only the estimation samples.

Define information before looking at agreement with validation. Proposed primary information measure: the standard error of the unshrunk log-fold estimate. Proposed secondary measure: mean normalized count. Both must be computed from the estimation arm only.

Proposed strata, cutpoints illustrative and not data-derived; lock numerical values before fitting:

- High information: unshrunk standard error at or below a locked \(s_{\mathrm{hi}}\).
- Low information: unshrunk standard error at or above a locked \(s_{\mathrm{lo}}\), with \(s_{\mathrm{lo}} > s_{\mathrm{hi}}\).
- Intermediate genes are reported but are not the pass/fail stratum.
- Strong simulated effect: absolute true log2 fold change at or above 1.
- Apparent extreme: absolute unshrunk log2 fold change at or above 2.

These cutpoints are assumptions of the decision rule. Different cutpoints can change a pass/fail; that is why they are locked first.

### 6. Simulation

Simulation tests the estimator under a known truth. It does not recover biology from the real dataset.

Proposed generative settings, to be fully specified before any fit:

- Setting N, inside the packet’s rationale: counts from the same overdispersed count family; log-fold effects drawn from a Normal distribution compatible with the prior; replicate numbers in the few-replicate regime; a realistic spread of mean counts and dispersions, including a large low-count fraction.
- Setting H, outside what the packet establishes: the same count process, but effects drawn from a heavier-tailed or two-component distribution in which a small fraction of genes has large effects. This is the stress test required by the packet’s silence on effect distributions.
- Setting D, dispersion outliers: a fraction of genes with dispersion far above the shared trend, to test harmful sharing.
- A null setting: all true effects zero, to measure how often low-information noise remains extreme after shrinkage.

Do not calibrate effect distributions to make the Normal prior win. Do not use validation samples to choose simulation parameters. Report each setting separately. A win only in setting N is not evidence about setting H.

Proposed error summaries, computed but not yet available: median absolute error of shrunk versus unshrunk estimates within information strata; sign agreement among strong high-information genes; the rate at which low-information genes with small true effects still show apparent extremes after shrinkage.

### 7. Independent validation

Apply the estimator locked on the estimation arm to nothing in the validation arm. Fit a higher-precision reference estimate on the validation samples alone, preferably with more replicates than the estimation arm. Treat that reference as a lower-noise proxy, not as absolute truth. If the validation arm is itself a few-replicate experiment, say so and downgrade the conclusion toward ambiguous.

Compare, within the pre-specified strata: absolute deviation of unshrunk and shrunk estimation-arm estimates from the reference; sign agreement; and whether genes called extreme only by the unshrunk estimator are low-information and discordant with the reference. Do not use pathway enrichment, a published gene list, or a narrative match to a paper as the endpoint.

### 8. Figure specification

Figures are to be generated only after the plan is locked. They are not results.

- Figure 1. Estimation-arm unshrunk versus shrunk log-fold estimates, stratified by information. Purpose: show whether shrinkage is selective.
- Figure 2. Simulation error against information for settings N, H, and D, with the strong-effect preservation rate marked against the locked threshold. Purpose: separate the methods forecast from the heavy-tail stress test.
- Figure 3. Estimation-arm shrunk and unshrunk estimates against the independent reference, same strata. Purpose: the only real-data check. No significance stars substituted for the pre-specified error comparison.
- Figure 4. Diagnostic for competing explanations: extreme unshrunk estimates versus information, versus dispersion residual, and versus known technical factors if present.

Each figure gets a caption that states the stratum rule and that no biological mechanism was identified. Do not add a volcano plot as a success metric; thresholding is not the question the packet poses.

### 9. Interpretation rule

Interpret only after all primary comparisons are computed. Do not iterate the prior until Figure 3 looks confirmatory. A methods-direction forecast may be stated only in the conditional language below.

## Preservation of strong effects without accepting low-information extremes

The test is a joint criterion. Meeting only one half is a failure or an ambiguity, not a success.

Preservation half. In simulation setting N, among high-information genes with absolute true log2 fold change at least 1, the shrunk estimate must keep the true sign and retain at least a locked fraction of the true magnitude. Proposed default to lock, not an observed value: 70% of the absolute true effect, in at least 90% of those genes. The same preservation summary is reported in setting H even though setting H is not the primary pass setting. On the real-data arm, high-information estimates that are large in the independent reference must not be moved by shrinkage across a pre-specified attenuation bound relative to that reference.

Rejection-of-extremes half. In the low-information stratum, median absolute error of the shrunk estimate must be smaller than that of the unshrunk estimate. Separately, among low-information genes whose true effect is small (proposed: absolute true log2 fold change below 0.5), the fraction that remain apparent extremes after shrinkage must fall relative to the unshrunk estimator. Pulling those estimates toward the prior mean is the intended behavior. It counts only if the preservation half also holds.

Explicit non-acceptance rule: a method that shrinks every estimate toward zero, including high-information effects above the preservation bound, fails even if low-information error improves. A method that leaves low-information extremes intact fails even if strong effects are untouched. Intermediate genes cannot be reassigned after inspection to repair either half.

The dispersion-outlier check is reported beside this test. If shared dispersion, not the Normal prior, is what attenuates strong effects, the failure is attributed to sharing, not to the prior, and the joint criterion still fails.

## Conditional conclusions

None of these has been observed. They are the only interpretations allowed after the protocol is actually run.

Positive, methods-direction only. State a positive forecast only if all of the following occur: setting N meets both halves of the joint criterion; the null setting shows fewer retained low-information extremes after shrinkage; independent validation agrees in direction for the low-information error reduction and does not show attenuation of high-information reference-supported effects beyond the locked bound; technical factors do not explain the validation gain. The permitted statement is that, under these conditions, shrinkage better recovered count-level differences than the unshrunk estimator. It is not a statement that any gene, pathway, or published claim was confirmed.

Negative. State that the proposed Normal-prior procedure failed the recovery task if setting N misses either half of the joint criterion, or if independent validation shows no error reduction in the low-information stratum, or if high-information effects supported by the reference are attenuated past the bound. If setting N passes and setting H fails preservation, the negative conclusion is narrower and more important: the procedure is not reliable for heavy-tailed effect distributions, which the packet does not exclude. Do not average N and H into a single success rate.

Ambiguous. Use this label, and do not upgrade it, if any of the following hold: simulation passes but no eligible independent arm exists; the reference arm is as noisy as the estimation arm; low-information error improves while strong-effect preservation fails, or the reverse; validation disagrees because the second cohort is not the same contrast; batch is inextricable from condition; implementations of the same specification disagree; or cutpoint sensitivity changes the call. Ambiguity means the packet’s rationale remains unconfirmed for the dataset, not that a weaker biological claim may be substituted.

## Forecast versus reproduction

A methods-direction forecast says: if the count model, the information gradient, and an effect distribution close to the Normal prior hold, then the proposed shrinkage should reduce error on unstable estimates and retain strong high-information effects. That forecast is entirely about estimator behavior.

An actual reproduction would require a pre-specified published claim, the original raw data, the original contrast, and a comparison to that claim’s stated biological result. This protocol does none of that. Using a public dataset that happens to have been published is provenance, not reproduction. Agreement with a held-out reference is a measurement check. It does not confirm mechanisms, clinical meaning, or any gene-level finding from the literature. No such finding is reported here because none was produced.

## Alternatives, limits, and what would change the recommendation

Alternatives if the primary criterion fails, to be chosen by the pre-specified failure mode rather than by appearance of a plot:

- If setting H fails and diagnostics show a heavy tail among high-information genes, a heavier-tailed prior is the relevant alternative. The packet does not establish that alternative; it would be a new proposal requiring the same joint criterion.
- If dispersion outliers drive the failure, prefer less aggressive dispersion sharing for that subset, again as a new pre-specified test.
- If validation failure tracks batch or composition, stop attributing error to fold-change variance. Shrinkage is the wrong remedy for confounding.
- If the scientific target is isoform or cell-composition change, gene-level counts are the wrong endpoint. This protocol cannot be reinterpreted as answering that question.

Limits: the packet gives a rationale, not a prior variance, not a universal effect distribution, and not a dataset. Simulation cannot prove the real effect distribution. A validation reference is not truth. Bulk gene counts confound transcription, composition, and isoform usage. Few replicates limit any method; shrinkage does not create information that the reads do not contain. Thresholds proposed here are decision rules, not biological constants.

What would change the recommendation: evidence, from the locked setting H or from the real-data information strata, that true large effects are common in high-information genes and are materially attenuated by the Normal prior; evidence that technical confounding, not count variance, dominates; or failure to find any dataset with raw-read provenance and a truly independent arm. Any of those would withdraw the recommendation to use this shrinkage specification for biological recovery and would leave only a qualified simulation forecast, or a different pre-registered estimator. What would not change it is a post-hoc gene list that matches a familiar story.
