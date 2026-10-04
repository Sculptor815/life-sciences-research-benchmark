# Kimi K3 / mol-k01

Original final answer, shared by both scoring rounds.

## Bottom line / recommended next action

The **50-kDa band is the only signal with genetic specificity support**: in E1, a validated biallelic deletion of the entire target coding sequence removes the 50-kDa band while the 75-kDa band and loading remain unchanged. The best-supported interpretation is: **50 kDa is a candidate target-derived immunoreactive band whose detection depends on the intact target locus; 75 kDa must remain unassigned/non-target until proven otherwise.**  

Do **not** yet call the antibody “validated.” Treat 50 kDa as genetically supported, then run orthogonal rescue, independent-epitope, and IP–MS validation. The key decision experiment is **add-back/rescue of the deleted coding sequence in the knockout**, with LC–MS/MS of the 50-kDa band as the decisive identity test.

---

## Evidence → inference → conclusion chain

**Observation, E1:** antibody detects two bands: 50 kDa and 75 kDa.  
**Perturbation, E1:** validated biallelic deletion of the **entire target coding sequence**.  
**Result, E1:** 50-kDa band is lost; 75-kDa band is unchanged; loading is comparable.  
**Limits stated in E1:** figures are synthetic teaching materials; no additional validation data are available.

Inference chain:

1. Comparable loading reduces the trivial explanation that the 50-kDa loss is due to unequal sample loading or general protein loss.  
2. A biallelic whole-coding-sequence deletion should eliminate all protein products encoded by that target locus, assuming the deletion is correctly mapped, truly biallelic, and covers all coding exons/alternative splice donors that could produce target peptides.  
3. Therefore, disappearance of the 50-kDa band is consistent with that band requiring expression from the deleted target locus.  
4. Persistence of the 75-kDa band under the same perturbation argues that it does **not** require the deleted target coding sequence in this assay.  
5. Conclusion: **genetic specificity support attaches to the 50-kDa signal only**. The antibody as a reagent is still only partially characterized because it also detects an unexplained 75-kDa species.

Important distinction: this is **genetic specificity support**, not proof that the antibody directly binds the target protein. The 50-kDa band could still be an indirectly regulated cross-reactive protein whose abundance depends on the target. E1 supports “target-locus-dependent,” not yet “target-identity-confirmed.”

---

## Why the 50-kDa band has the stronger claim

The 50-kDa signal is genetically linked because the relevant genotype—loss of both copies of the entire coding sequence—co-varies with the signal: present in control, absent in deletion. That is the core logic of a knockout specificity test. The whole-coding-sequence deletion is stronger than a single-exon CRISPR indel because it lowers the risk that residual isoforms, alternative start sites, or in-frame exon skipping still produce antigen.

Still, the claim is bounded by assumptions that E1 does not supply data for:

- the deletion is clonal, biallelic, and junction-mapped;
- no nearby regulatory-element disruption causes a secondary expression change;
- the antibody is not detecting a downstream protein that collapses only in stable knockout cells;
- the apparent 50-kDa size is not due to an unrelated comigrating protein;
- replicates, quantification, and normalization were adequate, which are not reported.

If any of those fail, the inference weakens.

---

## Loss of antigen versus indirect effects

**Direct loss of antigen** predicts that the epitope is physically encoded by the deleted coding sequence. Expected downstream pattern:

- knockout removes 50 kDa;
- re-expression of the target coding sequence restores 50 kDa;
- independent antibodies against different target epitopes also lose/restore the same band;
- endogenous tag knock-in co-migrates with and shifts the 50-kDa band;
- IP of the 50-kDa band yields target peptides by LC–MS/MS in wild type and not in knockout.

**Indirect effect** predicts that deletion changes cell state, abundance, stability, modification, localization, or expression of a different immunoreactive protein. Warning signs:

- rescue with target cDNA does not restore the 50-kDa band even though target expression is confirmed;
- IP–MS identifies non-target proteins in the 50-kDa gel region;
- other target-specific antibodies fail to detect the same band;
- acute knockdown does not reproduce the stable-knockout phenotype, suggesting adaptation;
- deleting a cross-reactive candidate identified by MS removes the band while the original target remains intact.

E1 cannot separate these possibilities because loss of signal after deletion is compatible with both “the epitope is gone” and “a target-dependent cross-reactive antigen is gone.” Comparable loading only argues against global sample artifacts; it does not prove molecular identity.

---

## Why the 75-kDa band remains unassigned

The 75-kDa band remains unassigned because it is **genetically invariant** under the target deletion: it is present at similar intensity despite removal of the entire target coding sequence. Under the simplest interpretation, it is not encoded by the deleted target locus.

Possible classes of explanation:

- nonspecific antibody binding to an abundant unrelated protein;
- specific cross-reactivity to a paralog or shared epitope encoded elsewhere;
- a contaminating immunoreactivity in the antibody preparation;
- a target-related species only if the deletion did not actually remove the relevant coding capacity, which would contradict the stated validation and must not be assumed without evidence.

Because E1 reports no rescue, peptide competition, second antibody, IP–MS, or paralog-knockout data, there is no basis to call 75 kDa an isoform, dimer, precursor, readthrough product, or modified form. The unchanged band is evidence against target-locus dependence, not positive evidence of what it is.

---

## Orthogonal validation plan and interpretable outcomes

Label: **proposed experiments; none are reported in E1.**

| Test | Outcome supporting 50 kDa = target | Outcome weakening direct assignment | Outcome for 75 kDa |
|---|---|---|---|
| **Rescue/add-back in knockout**: reintroduce WT target coding sequence, ideally near endogenous level; include empty-vector and expression controls | 50 kDa returns specifically with target expression; 75 kDa unchanged | 50 kDa does not return despite confirmed rescue expression; suggests indirect loss, wrong locus model, or comigrating artifact | If 75 kDa changes with rescue, revisit deletion mapping; otherwise remains non-target/cross-reactive |
| **Independent antibodies to distinct target epitopes**, e.g. N- vs C-terminal | both detect 50 kDa in control and lose it in knockout; same rescue behavior | discordance implies epitope loss, isoform complexity, or one antibody detects a comigrating non-target | independent target antibodies should not assign 75 kDa unless deletion mapping is wrong |
| **IP of 50-kDa region + LC–MS/MS** in control and knockout | target peptides enriched in control 50-kDa IP/band and absent in knockout | 50-kDa region yields mostly non-target peptides; supports cross-reactive/comigrating band | IP–MS of 75 kDa identifies the actual antigen; candidate can then be genetically tested |
| **Endogenous epitope-tag knock-in** at target locus | anti-tag and study antibody co-detect the same 50-kDa species; tag shifts mass predictably; knockout removes both | tag-positive protein differs in size from antibody band or persists after deletion | tag strategy does not explain 75 kDa unless unexpected fusion/readthrough is found |
| **Acute depletion** by CRISPRi/siRNA where viable | rapid reduction of 50 kDa tracks with target mRNA/protein loss | delayed/adaptive loss or no loss despite target depletion suggests indirect or stable-KO artifact | useful only after 75-kDa identity candidate exists |
| **Peptide/epitope blocking** with immunizing antigen | blocks 50 kDa and not merely all bands nonspecifically | blocks both bands or fails to block 50 kDa; weak evidence | if blocking selectively removes 75 kDa, it may share the immunizing epitope but is not target-encoded |
| **Candidate cross-reactive gene perturbation** guided by IP–MS/paralog analysis | deleting true target removes 50 kDa; deleting candidate does not | deleting candidate removes 50 kDa even when target is intact; reassignment needed | deleting/ knocking down candidate removes 75 kDa, solving the unassigned band |

Decision rule: assign the 50-kDa band as target only when **genetics, rescue, independent epitopes, and peptide identity converge**. If rescue restores the band but MS finds no target peptides, suspect comigration or rescue-induced indirect expression. If MS finds target peptides but independent antibodies disagree, suspect isoform/epitope masking or antibody-specific artifacts. If all orthogonal tests agree, the 75-kDa band should still be reported as a separate immunoreactivity unless its own identity is established.

---

## Limits and what would change the recommendation

E1 is sufficient to prioritize 50 kDa and deprioritize 75 kDa, but not to validate the antibody. The conclusion would strengthen if deletion junctions, clonality, replicate quantification, and normalization were shown and rescue restored 50 kDa. It would change if the deletion were found to remove a neighboring regulatory element, if a residual target transcript/protein persisted, if IP–MS failed to identify the target in the 50-kDa band, or if rescue restored target expression without restoring the band. Until those are resolved, report: **“50-kDa band shows knockout-dependent genetic specificity support; 75-kDa band is unresolved and should be treated as non-target/unassigned.”**
