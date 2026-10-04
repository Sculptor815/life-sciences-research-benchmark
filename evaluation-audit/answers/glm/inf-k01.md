# GLM 5.3 FlashX / inf-k01

Original final answer, shared by both scoring rounds.

# From GWAS Signal to Causal Mechanism: An Inferential Chain Applied to the Supplied Locus

## Bottom line up front

With only E1 — a well-controlled GWAS association to a noncoding lead SNP near gene G, with several linked variants spanning G and H — the only defensible conclusion is that **one or more causal variants reside somewhere in the linked region, and neither the causal variant nor the effector gene (G vs. H) can be identified from the supplied evidence**. Every subsequent step (fine mapping, colocalization, functional perturbation) is a *proposed* experiment, not a completed result. The most common error at this stage — assigning the gene nearest the lead SNP as "the" gene — is not an inference the data support.

---

## Step 1: The GWAS association (what E1 actually establishes)

**Evidence:** A lead noncoding SNP exceeds genome-wide significance in a well-controlled study (E1). "Well-controlled" is assumed to mean adequate ancestry matching/population-structure correction, genotype quality, and appropriate multiple-testing thresholds (an assumption, since E1 does not enumerate the controls).

**Inference:** Genotypes at (or tagging) this SNP are statistically associated with the trait. Because the lead SNP is noncoding, the association itself says nothing about mechanism; it marks a genomic region.

**Conclusion (valid):** A causal locus exists in linkage disequilibrium (LD) with the lead SNP.

**What it cannot establish:**
- **Which variant is causal.** The lead SNP is only the variant with the strongest statistical signal; due to LD, it is a *tag*, not necessarily the cause. In E1, "several linked variants span G and H," meaning the credible causal variant lies anywhere in that correlated block.
- **Which gene is affected.** GWAS positional information is weak: a noncoding causal variant may regulate a gene hundreds of kilobases away, or act through a noncoding RNA, regulatory element, or chromatin architecture affecting either G or H (or another gene in the region).

**Key distinction — association vs. linkage:** Here "linkage" is used in two senses that must be kept separate. *Population LD* (correlation of alleles in a population) is what makes GWAS signals broad; it is a statistical property of the sample, not proof of physical co-segregation. *Linkage analysis* in pedigrees establishes co-segregation of a region with trait transmission but has far coarser resolution. A GWAS peak inherits the *location* of the causal variant only to within the LD block — which is precisely why E1's "several linked variants" all remain candidates.

---

## Step 2: Fine mapping (narrowing the candidate set)

**Proposed experiment (not supplied data):** Impute densely (or sequence) the region in a large, ancestrally diverse sample; compute posterior probabilities of causality for each variant (e.g., Bayesian credible sets, SuSiE/FINEMAP-style methods); exploit trans-ancestral or cross-population LD differences, where recombination patterns differ and only the true causal variant keeps its association.

**Inference chain:** LD structure differs across populations → the association pattern must be consistent for the true causal variant but only tag-dependent for proxies → variants whose posterior probability stays high across LD patterns are better causal candidates.

**Conclusion possible after this step:** A credible set — ideally one variant with high posterior probability, more realistically a small set — of candidate causal variants.

**What it cannot establish:**
- Fine mapping is still **statistical and correlational**. A variant at 95% posterior probability is not proven causal; the posterior depends on assumptions (one causal variant vs. multiple, LD reference accuracy, sample homogeneity).
- It **does not identify the effector gene**. Fine mapping resolves *variant* position, not *mechanism*. In E1, even a perfectly fine-mapped variant could regulate G, H, or a distal gene.
- If the causal variant is poorly tagged or rare in available populations, it may not even enter the credible set.

**Application to E1:** With several linked variants spanning G and H, fine mapping is the first step that can shrink the candidate list — but the supplied evidence contains none of it, so at present every linked variant remains a candidate.

---

## Step 3: Colocalization (connecting the GWAS signal to molecular phenotypes)

**Proposed experiment (not supplied data):** Test whether the *same* genetic signal drives both the GWAS trait and a molecular QTL — e.g., an eQTL for G or H (expression), sQTL (splicing), or pQTL (protein) — in relevant tissue/cell type, using methods such as coloc, eCAVIAR, or SMR/HEIDI that compare the LD-shared association signals.

**Inference chain:** If one causal variant explains both the trait association and the G-expression signal (and not H's, or vice versa), the parsimonious explanation is that the variant alters that gene's expression, and that molecular change plausibly mediates the trait.

**What it can establish (probabilistically):** That the GWAS and QTL signals are *consistent with a single shared causal variant*, and therefore that a specific gene is the *likely* effector.

**What it cannot establish:**
- Colocalization is sensitive to **LD reference accuracy, sample overlap, and model misspecification**. Two distinct causal variants in high LD can masquerade as one colocalized signal (the classic false "causal gene" call).
- It requires the **right tissue, cell type, and stimulus**. An eQTL for G in whole blood may be irrelevant if the trait's relevant cell type is, say, a stimulated immune subset where H responds instead. Absence of colocalization in tested contexts is not evidence against a gene.
- It shows *association with an intermediate molecular trait*, not that the molecular change *causes* the disease phenotype (an exposure-like assumption, not a tested causal link).

**Application to E1:** Since G and H both sit under the linked block, colocalization with eQTL/sQTL data for **both** genes is the decisive discriminator between them. Without such data (as E1 states), any claim that "G is the effector because it is nearest the lead SNP" is unsupported — proximity is a prior, not evidence.

---

## Step 4: Functional perturbation (from correlation toward mechanism)

**Proposed experiments (none performed):**
- **Variant-level:** Allele-specific reporter assays, MPRA/STARR-seq, or CRISPR base/prime editing of the candidate variant in a relevant cell type to test whether the alleles differentially affect regulatory activity or target-gene expression.
- **Gene-level:** CRISPRi/a, knockout, or overexpression of G vs. H to test whether perturbing each gene recapitulates trait-relevant cellular phenotypes.

**Inference chain:** If editing the fine-mapped variant alters the activity of a specific enhancer, and that enhancer's deletion or CRISPRi selectively changes expression of G (not H), and perturbing G produces the disease-relevant cellular phenotype, then the chain *variant → regulatory element → effector gene → mechanism* is experimentally connected.

**What it can establish:** Direct, perturbational evidence of molecular mechanism in the tested system.

**What it cannot establish (fully):**
- In vitro results are **context-dependent**: cell type, stimulus, and assay design may not reflect in vivo disease biology; reporter assays in particular disconnect the variant from native chromatin.
- Perturbing the gene and observing a phenotype does not prove that the *GWAS variant's effect* operates through that gene — the "recapitulation fallacy." Genetic validation requires showing that the *endogenous* variant's effect on the trait is mediated through the perturbed target (e.g., via allele-specific editing or chromatin perturbation).
- Human disease relevance ultimately requires convergent evidence (e.g., rare coding variants in the gene associating with related phenotypes, or rescue experiments).

---

## The complete chain, assembled

1. **Association (E1, supplied):** trait ↔ lead SNP region. Establishes *a causal locus exists*; nothing more.
2. **Fine mapping (proposed):** narrows to candidate variant(s) statistically, exploiting LD heterogeneity. Does not name a gene.
3. **Colocalization (proposed):** statistically links the variant's signal to a molecular phenotype of G or H, nominating the likely effector gene. Correlational, context-dependent.
4. **Functional perturbation (proposed):** tests variant → regulatory → gene → phenotype links causally in controlled systems. Strongest evidence, but generalizable only to the extent the model system matches human biology.

Each step *constrains* the hypothesis space; no single step is sufficient. The causal claim is the conjunction, with residual uncertainty at every link.

## Explicit limits for the supplied locus

- **Current state (E1 only):** Causal locus: yes. Causal variant: unknown among the linked set. Effector gene: **unknown between G and H** — including the formal possibility of multiple causal variants affecting different genes within the block.
- **Assumptions I am making:** "Well-controlled" GWAS implies standard ancestry and QC safeguards (E1 does not specify); no functional or colocalization data exist (E1 states this explicitly); all figures are synthetic teaching materials, so no additional validation is implied.
- **Key uncertainties that would change the interpretation:** (i) the LD block size and recombination pattern — a short block makes fine mapping decisive; a long, high-LD block makes colocalization and functional work essential; (ii) whether the trait-relevant tissue/cell type is known — without it, colocalization may be uninformative or misleading; (iii) whether multiple independent causal variants exist in the block, which colocalization models assuming a single signal can miss.

## Recommended next action

Prioritize **(1)** dense imputation/sequencing and fine mapping of the G–H block in diverse ancestries, then **(2)** eQTL/sQTL colocalization for both G and H in the trait-relevant tissue. Only after a gene is nominated by colocalization should **(3)** allele-specific editing and gene-level perturbation be mounted. Do not privilege gene G on the basis of proximity to the lead SNP — the supplied evidence provides no basis for preferring G over H.
