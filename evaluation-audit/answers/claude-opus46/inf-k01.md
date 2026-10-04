# Claude Opus 4.6 / inf-k01

Original final answer, shared by both scoring rounds.

# From GWAS Hit to Causal Mechanism: The Inferential Chain

## 1. Conclusion Up Front

A GWAS lead SNP near gene G establishes a **genomic region** associated with a trait but, by itself, identifies neither the causal variant nor the effector gene. Resolving those requires a strict sequence of additional analyses—linkage-disequilibrium (LD) characterisation, statistical fine mapping, colocalization with molecular QTL data, and functional perturbation—each of which narrows a distinct layer of ambiguity. For the locus described in **E1**, where linked variants span genes G and H and no functional or colocalization data exist, we are stalled after the first two steps; claiming G (or H) as the effector gene is premature.

---

## 2. Step-by-Step Inferential Chain

### Step 1 — GWAS Association and the LD Problem

**What is established.** A well-controlled GWAS tells us that somewhere in the LD block tagged by the lead SNP there exists at least one variant whose allelic state (or a correlated allele's state) influences the trait at genome-wide significance. This is a *regional* statement, not a *variant-level* statement.

**What is NOT established.**

| Ambiguity | Why it persists |
|---|---|
| Causal variant identity | Any SNP in high LD (r² ≳ 0.8) with the lead SNP is statistically indistinguishable from it in the discovery sample. |
| Number of independent signals | A single association peak can hide multiple independent causal variants whose effects are conflated by LD. |
| Effector gene identity | Proximity ≠ causality. The nearest gene (G) is the true effector roughly 40–60 % of the time in benchmarked loci; genes further away (H, or even more distal genes reached by chromatin looping) can be responsible. |
| Mechanism of action | A noncoding lead SNP could act through transcriptional regulation, splicing, mRNA stability, or could simply be tagging a coding variant in LD. |

**Application to E1.** The lead SNP is noncoding and near G, but variants in LD extend across G and H. At this stage both genes are equally plausible candidates; the "near gene G" label is a convenience of annotation, not evidence of function.

---

### Step 2 — Statistical Fine Mapping

**Purpose.** Shrink the list of candidate causal variants by computing posterior inclusion probabilities (PIPs) for every variant in the region, typically constructing credible sets (e.g., 95 % credible sets via SuSiE, FINEMAP, or analogous methods).

**What is established.** A ranked set of variants that, under model assumptions (one or a small number of causal variants, a correctly specified LD reference), jointly account for ≥ 95 % of the posterior probability of causality. If the credible set is small (e.g., 1–3 SNPs), variant-level resolution is high.

**What is NOT established.**

- The effector gene. Even a single high-PIP variant in an intron of G could regulate H (or a distal gene) via a long-range enhancer.
- Mechanism. Fine mapping is agnostic to function; it only reweights statistical evidence.
- Certainty. Credible-set calibration depends on LD-matrix accuracy and the single-causal-variant (or sparse) assumption. Mismatched LD references inflate sets and can mis-rank variants.

**Application to E1.** Fine mapping should be the immediate next analysis. If the 95 % credible set collapses to variants overlapping only one gene's regulatory landscape, the candidate space narrows—but gene assignment still requires the next steps.

---

### Step 3 — Colocalization with Molecular QTLs

**Purpose.** Test whether the GWAS signal and a molecular-phenotype signal (eQTL, sQTL, pQTL, caQTL) share the **same causal variant** rather than merely overlapping by LD coincidence.

**What is established.** A high posterior probability of a shared causal variant (e.g., PP.H4 > 0.8 in coloc; or convergent credible sets in coloc-SuSiE) links the trait association to a specific molecular intermediate (e.g., expression of gene G in tissue T). This is the first step that formally connects a GWAS signal to a candidate effector gene through a plausible mechanism.

**What is NOT established.**

- Causality of the molecular intermediate. Colocalization is correlative; the eQTL could be a bystander if transcription of G and the true regulatory function are both driven by the same variant but through independent mechanisms.
- Tissue and context specificity. Absence of colocalization in available eQTL catalogues does not exclude a gene—it may be an effector only in a cell type, developmental stage, or stimulus condition not yet profiled.
- Direction of effect or sufficiency. Even strong colocalization does not prove that changing expression of G is sufficient to change the trait.

**Application to E1.** No colocalization data are supplied. Until eQTL/sQTL/pQTL datasets in relevant tissues are interrogated, we cannot distinguish whether the locus acts through G, H, both, or neither of the two nearest genes. This is the critical missing layer.

---

### Step 4 — Functional Perturbation

**Purpose.** Move from statistical association to experimental evidence of causality at the variant and/or gene level.

**Variant-level perturbation.** CRISPR base-editing or saturation mutagenesis of the credible-set region in a relevant cell type tests whether specific alleles alter a molecular readout (reporter activity, endogenous gene expression, chromatin accessibility). Massively parallel reporter assays (MPRAs) can screen many variants simultaneously, though they test activity outside native chromatin context.

**Gene-level perturbation.** CRISPRi/a of candidate enhancers, or direct knockout/knockdown of G versus H, followed by phenotypic readout, tests whether changing the gene's expression alters the trait-relevant cellular phenotype.

**What is established.** A direct, experimentally controlled link between a specific allele or gene and a measurable phenotype—the closest approximation to causality available outside human genetic perturbation (e.g., loss-of-function carrier studies).

**What is NOT established.**

- In-vivo relevance. Cell-line perturbations may not recapitulate organismal physiology.
- Quantitative effect size. CRISPR knockouts test necessity/sufficiency of a gene, not the modest allelic effects typical of common-variant GWAS.
- Completeness. Negative results may reflect wrong cell type, time point, or readout rather than true non-involvement.

**Application to E1.** No perturbation data exist. Designing the right experiment depends on outputs from Steps 2–3 (which variants and genes to target) and on knowledge of the trait-relevant cell type.

---

## 3. Summary of the Inferential Hierarchy

| Step | Resolves | Key output | Remaining ambiguity |
|---|---|---|---|
| GWAS | Region → trait | Lead SNP, p-value | Variant, gene, mechanism all unknown |
| Fine mapping | Region → candidate variant(s) | Credible set, PIPs | Gene and mechanism unknown |
| Colocalization | Variant → candidate gene via shared QTL | PP.H4, effector gene hypothesis | Causality of molecular intermediate unproven |
| Functional perturbation | Variant/gene → phenotype (experimental) | Allele-specific or gene-specific effect | Organismal translation uncertain |

Each step **requires** the output of the preceding step for rational design, and each reduces a distinct class of ambiguity that no other step can resolve.

---

## 4. Limits and Alternatives for the E1 Locus

- **Strongest current inference:** A region spanning G and H is associated with the trait. Nothing more.
- **Most consequential next step:** Statistical fine mapping to define a credible set, followed immediately by colocalization against multi-tissue eQTL and chromatin-accessibility QTL atlases.
- **What would change the recommendation:** (a) If the credible set contains a missense variant in H, gene assignment shifts without needing colocalization. (b) If colocalization implicates G's expression in a specific tissue, perturbation experiments should target G's regulatory element in that cell type. (c) If colocalization is absent for both G and H across all available datasets, one must consider unmeasured cell types or non-transcriptional mechanisms (e.g., splicing, 3-D looping to a distal gene).

**Bottom line.** Naming gene G as the effector on the basis of proximity alone would be an inferential shortcut that skips three layers of necessary evidence. The locus in E1 is, at present, a regional association—no more and no less.
