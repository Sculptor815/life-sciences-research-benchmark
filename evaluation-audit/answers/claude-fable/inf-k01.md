# Claude Fable 5 / inf-k01

Original final answer, shared by both scoring rounds.

# From GWAS Signal to Causal Variant and Effector Gene: What E1 Does and Does Not License

## Bottom line / recommended next action

From E1 alone, the only defensible conclusion is: **a haplotype of correlated variants spanning genes G and H is statistically associated with the trait.** Neither the lead SNP's causality nor G's status as the effector gene follows. The nearest-gene heuristic ("near gene G") is a naming convention, not an inference. The recommended next steps, in order, are (1) statistical fine-mapping with LD-aware methods to shrink the credible set of candidate causal variants, (2) colocalization with molecular QTLs (eQTL/pQTL/caQTL) in trait-relevant tissues to nominate the effector gene(s), and (3) functional perturbation (e.g., CRISPR editing/interference of the candidate regulatory element, allele-specific reporter assays) to establish mechanism. Each step closes a specific inferential gap the previous one cannot.

---

## Step 0 — What the GWAS association itself establishes

**Evidence (E1):** A well-controlled GWAS yields a genome-wide significant lead noncoding SNP; several linked variants span G and H.

**Inference licensed:** Under standard assumptions (adequate control of population stratification, relatedness, genotyping artifacts — "well-controlled" is asserted but is itself an assumption we inherit), the genotype–phenotype association at this locus is unlikely to be a false positive, and *some variant on the associated haplotype* (genotyped or imputed, possibly untyped) influences the trait, directly or through a correlated causal factor.

**Not licensed:**
- The lead SNP is not necessarily causal. The "lead" is simply the variant with the smallest p-value; in the presence of linkage disequilibrium (LD), a non-causal variant can have the strongest statistic due to allele frequency, imputation quality, or sampling noise.
- The effector gene is unknown. Noncoding variants commonly act through *cis*-regulatory elements (enhancers, promoters, splicing elements) that can skip the nearest gene entirely; the target could be G, H, or a gene outside the plotted window (long-range enhancer contacts of hundreds of kb to >1 Mb are documented).
- Direction and mechanism (expression, splicing, chromatin, protein function) are unknown.
- Residual confounding by uncorrected fine-scale stratification or cross-trait assortative mating, while mitigated by good design, is never fully excluded by association alone.

---

## Step 1 — Linkage (LD): why the signal is a region, not a point

**Concept:** LD means nearby variants are inherited together on haplotypes. Association statistics therefore "smear" across all variants correlated with the causal one(s). In E1, the linked variants spanning G and H define this LD block.

**What LD reasoning establishes:** It delimits a *candidate region* — the set of variants in appreciable r² with the lead — within which the causal variant(s) almost certainly lie (assuming the causal variant is tagged; poorly imputed rare variants or structural variants may be invisible).

**What it cannot establish:** Any ranking among tightly linked variants. If several variants have r² ≈ 1 with each other, association statistics are mathematically incapable of distinguishing them in a single population. LD also says nothing about which gene is affected: an LD block spanning G and H does not mean the mechanism involves either gene's coding sequence or even its regulation.

**Key pitfalls at this step:** (a) possibility of multiple independent causal variants in the region (allelic heterogeneity), which conditional analysis can reveal; (b) LD structure differs across ancestries, so the block boundaries in E1 are ancestry-specific.

---

## Step 2 — Statistical fine-mapping: shrinking variants, with explicit limits

**Proposed analysis (not supplied in E1):** Bayesian fine-mapping (e.g., SuSiE, FINEMAP) using in-sample LD, producing posterior inclusion probabilities (PIPs) and credible sets — sets of variants that contain the causal variant(s) with, say, 95% posterior probability.

**What fine-mapping can establish:** A probabilistic ranking of candidate causal variants and a reduced search space. Multi-ancestry fine-mapping is especially powerful because differing LD patterns across populations break ties that are unresolvable within one ancestry. If the trait-associated haplotype in E1 contains a variant in perfect LD with the lead in one ancestry but not another, cross-ancestry data can discriminate them.

**What it cannot establish:**
- Mechanism or effector gene. A PIP of 0.99 says the variant is likely *statistically causal for the association*, not what it does biologically or which gene it regulates.
- Correctness when assumptions fail: mismatched LD reference panels, unmodeled multiple causal variants, imputation error, or untyped causal variants (structural variants, repeat expansions) can produce confidently wrong credible sets.
- If LD is near-perfect among several variants, the credible set simply remains large — honest uncertainty, not resolution.

**Conclusion chain so far:** association (E1) → LD defines region → fine-mapping (proposed) narrows to credible variant set. Gene identity still unresolved between G, H, and non-local candidates.

---

## Step 3 — Colocalization: linking the variant set to a molecular phenotype and candidate gene

**Proposed analysis (none supplied in E1):** Test whether the GWAS signal and a molecular QTL signal — e.g., an eQTL for G or H in a disease-relevant tissue/cell type — share a single causal variant, using methods such as *coloc* (posterior probability of shared causal variant, PP.H4), eCAVIAR, or SMR with HEIDI.

**What colocalization can establish:** Evidence that the *same* underlying variant drives both trait risk and, say, expression of G in tissue T. This nominates G as a plausible effector gene and expression in T as a plausible mechanism, with an implied direction of effect (risk allele increases/decreases G).

**What it cannot establish:**
- Causality of the gene for the trait. Colocalization is consistent with mediation (variant → G expression → trait) but also with **horizontal pleiotropy**: one variant independently affecting G's expression and the trait through a separate pathway, or affecting both G and H.
- Uniqueness: the same credible set may colocalize with eQTLs for both G and H (shared regulatory elements are common); both could colocalize and only one (or neither) mediate the trait.
- Tissue/context completeness: absence of colocalization may reflect missing context (cell type, developmental stage, stimulation state) rather than absence of regulation. Many GWAS loci show no eQTL in surveyed adult bulk tissues.
- Distinguishing a single shared variant from two distinct, tightly linked variants (coloc's H3 vs H4) is power- and LD-limited.

---

## Step 4 — Functional perturbation: establishing mechanism

**Proposed experiments (none supplied; these are design suggestions, not results):**
1. **Element-level:** CRISPRi/CRISPRa tiling or deletion of the candidate enhancer harboring credible-set variants in a relevant cell model; readout = expression of G and H (and neighbors) plus a cellular phenotype proxy.
2. **Variant-level:** base editing or prime editing to install each allele on an isogenic background; massively parallel reporter assays (MPRA) to test allelic regulatory activity at scale.
3. **Gene-level:** knockdown/knockout/overexpression of G and of H to test which perturbation recapitulates or modifies the cellular phenotype.
4. **Chromatin contact mapping** (Hi-C/Capture-C/ABC-style predictions) to ask whether the element physically contacts G's or H's promoter — supportive, not sufficient.

**What perturbation can establish:** That a specific sequence element or allele is *sufficient* to alter expression of a specific gene in that cellular context, and that modulating that gene alters a relevant cellular phenotype. This is the strongest available evidence for the variant→element→gene→cell-phenotype segment of the causal chain.

**What it cannot establish:**
- Organism-level trait causation: cell models may lack the relevant context; effect sizes in vitro need not translate.
- Exclusivity: a positive result for G does not exclude a parallel contribution via H.
- External validity across the human population (background effects, epistasis).

---

## Explicit evidence → inference → conclusion chain for this locus

| Step | Evidence status in E1 | Inference if evidence obtained | Residual gap |
|---|---|---|---|
| Association | **Supplied** | Haplotype spanning G/H is trait-associated | Which variant; which gene |
| Linkage/LD | Supplied (linked variants described) | Causal variant(s) lie within tagged region, probably | Cannot rank tied variants |
| Fine-mapping | **Not supplied** | Credible set of candidate variants | No mechanism or gene |
| Colocalization | **Not supplied** | Shared signal with e.g. G-eQTL → G nominated | Pleiotropy; H not excluded |
| Perturbation | **Not supplied** | Element/allele regulates gene; gene affects cell phenotype | Organismal causation; exclusivity |

**Overall conclusion from E1:** Only the first two rows are supported. Claims that "the lead SNP is causal" or "G is the disease gene" would be overreach. G and H are symmetric candidates until QTL/colocalization or perturbation data discriminate them; non-local genes remain possible.

## Consequential uncertainties that would change the plan

- **Multiple independent signals** at the locus (test by conditional analysis first) would require signal-specific fine-mapping and colocalization.
- **An untyped structural variant** as the true driver would invalidate SNP-based credible sets; long-read or SV-genotyped reference data would be needed.
- **Context-specific regulation**: failure to colocalize in available tissues should trigger single-cell or stimulated-state QTL data, not dismissal of G/H.
- **Coding variants in LD**: if the credible set contains a missense variant in G or H, the mechanistic prior shifts from regulatory to protein-level assays.

All figures are stated to be synthetic teaching materials; no validation results exist, so every row below "Linkage" above is a proposal, not a finding.
