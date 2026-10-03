"""Execute small offline scientific workflow checks, not model capability scores.

All inputs are synthetic. The planted truth stays outside analysis inputs.
This does not claim a complete production WGS/GATK or MOFA/DESeq2 replication.
"""
import argparse
import hashlib
import importlib.metadata
import json
import os
import platform
from pathlib import Path
import sys
import time


def dump(path, data):
    path.write_text(json.dumps(data,indent=2,allow_nan=False)+'\n',encoding='utf-8')


def run(output):
    output=Path(output).resolve()
    output.mkdir(parents=True,exist_ok=False)
    report={'kind':'offline_synthetic_workflow_validation','is_agent_evaluation':False,
            'is_real_data_validation':False,'seed':20261003,'python':sys.executable,'checks':[],
            'environment':{'python_version':platform.python_version(),'platform':platform.platform(),
                           'machine':platform.machine(),'thread_settings':{k:os.environ.get(k) for k in ['OMP_NUM_THREADS','MKL_NUM_THREADS','OPENBLAS_NUM_THREADS']}}}
    try:
        import numpy as np
        import pandas as pd
        from scipy import stats
        from sklearn.cross_decomposition import CCA
        from sklearn.preprocessing import StandardScaler
        import statsmodels.api as sm
    except ImportError as exc:
        report.update(status='dependency_unavailable',missing_dependency=str(exc),all_implemented_checks_passed=False)
        dump(output/'pipeline-report.json',report)
        return 2
    rng=np.random.default_rng(20261003)
    def check(name, fn):
        start=time.monotonic()
        try:
            details=fn()
            report['checks'].append({'name':name,'status':'passed','seconds':time.monotonic()-start,**details})
        except Exception as exc:
            report['checks'].append({'name':name,'status':'failed','error':f'{type(exc).__name__}: {exc}','seconds':time.monotonic()-start})
        dump(output/'pipeline-report.json',report)
    def enrichment():
        universe={f'g{i}' for i in range(100)}
        selected={f'g{i}' for i in range(10)}
        pathways={'planted':{f'g{i}' for i in range(12)},'null':{f'g{i}' for i in range(40,60)},'overlap':{f'g{i}' for i in range(5,20)}}
        rows=[]
        for name,genes in pathways.items():
            measured=genes&universe
            k=len(measured&selected)
            p=float(stats.hypergeom.sf(k-1,len(universe),len(measured),len(selected)))
            rows.append({'pathway':name,'overlap':k,'tested_pathway_size':len(measured),'p':p})
        values=np.array([r['p'] for r in rows]); order=np.argsort(values)
        q=np.minimum.accumulate((values[order]*len(values)/np.arange(1,len(values)+1))[::-1])[::-1]
        for idx,value in zip(order,q):rows[int(idx)]['q']=float(min(value,1))
        # Independent implementation verifies the assignment back to pathway rows.
        from statsmodels.stats.multitest import multipletests
        assert np.allclose([r['q'] for r in rows],multipletests(values,method='fdr_bh')[1])
        assert rows[0]['q']<.01 and rows[1]['q']==1
        assert np.isclose(stats.hypergeom.sf(1,10,3,2),3/45)
        pd.DataFrame(rows).to_csv(output/'enrichment.csv',index=False)
        return {'method':'one-sided ORA, hypergeometric + BH','universe':100,'known_exact_tail_verified':True,'limit':'Not a GSEA implementation; no biological pathway claims from synthetic gene sets.'}
    check('enrichment',enrichment)
    def multiomics():
        n=100
        z=rng.normal(size=(n,2)); x=z@rng.normal(size=(2,12))+rng.normal(scale=.2,size=(n,12)); y=z@rng.normal(size=(2,10))+rng.normal(scale=.2,size=(n,10))
        ids=np.array([f'person-{i}' for i in range(n)])
        # Deliberately permute the second view, then align by ID before fitting.
        perm=rng.permutation(n); paired=dict(zip(ids[perm],y[perm])); aligned=np.array([paired[s] for s in ids])
        assert np.array_equal(y,aligned)
        train=np.arange(70); test=np.arange(70,n)
        sx=StandardScaler().fit(x[train]); sy=StandardScaler().fit(aligned[train])
        model=CCA(n_components=2,scale=False,max_iter=2000).fit(sx.transform(x[train]),sy.transform(aligned[train]))
        a,b=model.transform(sx.transform(x[test]),sy.transform(aligned[test]))
        corr=float(np.corrcoef(a[:,0],b[:,0])[0,1])
        shuffled=float(np.corrcoef(a[:,0],b[rng.permutation(len(b)),0])[0,1])
        assert corr>.85 and abs(shuffled)<.6
        pd.DataFrame({'sample':ids[test],'view1':a[:,0],'view2':b[:,0]}).to_csv(output/'multiomics-heldout.csv',index=False)
        return {'method':'paired CCA; preprocessing fit only on training subjects','heldout_correlation':corr,'permuted_pair_correlation':shuffled,'train_subjects':70,'test_subjects':30,'limit':'Smoke validation of paired integration; not MOFA, missing-view modeling or causal discovery.'}
    check('multiomics',multiomics)
    def pseudobulk():
        # Eight independent donors per arm; cells are nested technical observations.
        donors=16; per_donor=25; genes=60
        counts=[]; donor_ids=[]
        for d in range(donors):
            rate=np.full(genes,3.0)*rng.lognormal(0,.1,size=genes)
            if d>=8:rate[:6]*=5
            counts.append(rng.poisson(rate,size=(per_donor,genes)));donor_ids.extend([d]*per_donor)
        counts=np.vstack(counts); donor_ids=np.array(donor_ids)
        aggregate=np.vstack([counts[donor_ids==d].sum(axis=0) for d in range(donors)])
        assert int(aggregate.sum())==int(counts.sum())
        logcpm=np.log2(1+aggregate/aggregate.sum(axis=1,keepdims=True)*1e6)
        p=stats.ttest_ind(logcpm[:8],logcpm[8:],axis=0,equal_var=False).pvalue
        order=np.argsort(p); q=np.empty_like(p);q[order]=np.minimum(1,np.minimum.accumulate((p[order]*genes/np.arange(1,genes+1))[::-1])[::-1])
        recall=float(np.mean(q[:6]<.05)); assert recall==1
        pd.DataFrame({'gene':[f'g{i}' for i in range(genes)],'p':p,'q':q,'effect_log2cpm':logcpm[8:].mean(axis=0)-logcpm[:8].mean(axis=0)}).to_csv(output/'pseudobulk-de.csv',index=False)
        design=np.column_stack([np.ones(donors),np.arange(donors)>=8,np.arange(donors)>=8])
        assert np.linalg.matrix_rank(design)<design.shape[1]
        return {'method':'donor aggregation + exploratory Welch test on log-CPM, BH','independent_units':donors,'cells':len(counts),'planted_gene_recall':recall,'perfect_batch_condition_confound_detected':True,'limit':'Tests donor accounting and contrasts; not a validated negative-binomial DESeq2/edgeR analysis. Strong compositional changes can affect unspiked genes.'}
    check('differential_expression',pseudobulk)
    def gwas():
        n=800;m=60
        ancestry=rng.normal(size=n)
        frequencies=1/(1+np.exp(-(.9*ancestry[:,None]+rng.normal(size=(1,m)))))
        g=rng.binomial(2,frequencies)
        phenotype=1.8*g[:,7]+1.5*ancestry+rng.normal(size=n)
        rows=[]
        for j in range(m):
            fit=sm.OLS(phenotype,sm.add_constant(np.column_stack([g[:,j],ancestry]))).fit()
            rows.append({'variant':f'v{j}','p':float(fit.pvalues[1]),'beta':float(fit.params[1])})
        assert min(rows,key=lambda r:r['p'])['variant']=='v7'
        assert rows[7]['p']<.05/m and abs(rows[7]['beta']-1.8)<.2
        pd.DataFrame(rows).to_csv(output/'gwas.csv',index=False)
        return {'method':'quantitative-trait OLS with a supplied ancestry covariate','subjects':n,'variants':m,'planted_lead':'v7','estimated_beta':rows[7]['beta'],'limit':'No LD/fine-mapping/relatedness/rare-variant clinical validation; associated locus is not an effector-gene conclusion.'}
    check('gwas',gwas)
    def single_cell():
        import scanpy as sc
        import anndata as ad
        from sklearn.cluster import KMeans
        from sklearn.metrics import adjusted_rand_score
        group=np.repeat([0,1],150);means=np.full((300,120),2.0);means[group==0,:12]=15;means[group==1,12:24]=15
        counts=rng.poisson(means).astype(np.float32)
        counts[0,:]=0  # Exercise QC removal and validation-label realignment.
        data=ad.AnnData(counts.copy());data.var_names=[f'g{i}' for i in range(120)];data.obs_names=[f'cell-{i}' for i in range(300)]
        truth=dict(zip(data.obs_names,group))
        data.layers['counts']=counts.copy()
        sc.pp.calculate_qc_metrics(data,percent_top=None,inplace=True)
        sc.pp.filter_cells(data,min_genes=20)
        before=hashlib.sha256(data.layers['counts'].tobytes()).hexdigest()
        group=np.array([truth[name] for name in data.obs_names]);assert len(group)==299
        sc.pp.normalize_total(data,target_sum=1e4);sc.pp.log1p(data)
        sc.pp.pca(data,n_comps=15,random_state=0);sc.pp.neighbors(data,n_neighbors=15,n_pcs=15,random_state=0)
        sc.tl.umap(data,random_state=0)
        predicted=KMeans(n_clusters=2,random_state=0,n_init=10).fit_predict(data.obsm['X_pca'])
        ari=float(adjusted_rand_score(group,predicted));assert ari>.9
        assert before==hashlib.sha256(data.layers['counts'].tobytes()).hexdigest()
        assert np.isfinite(data.obsm['X_umap']).all()
        data.obs['cluster']=pd.Categorical(predicted.astype(str));data.write_h5ad(output/'single-cell.h5ad')
        pd.DataFrame({'cell':data.obs_names,'truth_for_validation_only':group,'cluster':predicted}).to_csv(output/'single-cell-validation.csv',index=False)
        return {'method':'Scanpy QC, normalization, PCA, neighbors, UMAP; KMeans baseline','cells':data.n_obs,'genes':data.n_vars,'adjusted_rand_index':ari,'counts_preserved':True,'limit':'Easy synthetic two-population control, not a real-data cell annotation or scVI benchmark.'}
    check('single_cell',single_cell)
    def trajectory():
        import scanpy as sc
        import anndata as ad
        time_truth=np.linspace(0,1,200)
        centers=np.linspace(0,1,40)
        features=np.exp(-((time_truth[:,None]-centers[None,:])/.22)**2)+rng.normal(0,.015,size=(200,40))
        data=ad.AnnData(features.astype(np.float32))
        sc.pp.neighbors(data,n_neighbors=10,use_rep='X',method='gauss',random_state=0)
        sc.tl.diffmap(data,n_comps=10,random_state=0);data.uns['iroot']=0;sc.tl.dpt(data,n_dcs=10)
        forward=data.obs['dpt_pseudotime'].to_numpy().copy();data.uns['iroot']=199;sc.tl.dpt(data,n_dcs=10)
        reverse=data.obs['dpt_pseudotime'].to_numpy().copy()
        corr=float(stats.spearmanr(time_truth,forward).statistic);reverse_corr=float(stats.spearmanr(time_truth,reverse).statistic)
        assert corr>.9 and reverse_corr<-.9
        pd.DataFrame({'latent_time_for_validation_only':time_truth,'root_first':forward,'root_last':reverse}).to_csv(output/'trajectory.csv',index=False)
        return {'method':'Scanpy diffusion map / DPT on synthetic continuous expression','forward_spearman':corr,'reverse_spearman':reverse_corr,'limit':'Root reversal is expected; pseudotime is not elapsed time or lineage ancestry. No branching benchmark.'}
    check('trajectory',trajectory)
    def variant_qc():
        # Fixed miniature VCF exercises downstream QC only, not read alignment/calling.
        text='##fileformat=VCFv4.2\n#CHROM\tPOS\tID\tREF\tALT\tQUAL\tFILTER\tINFO\tFORMAT\ts1\n1\t101\t.\tA\tG\t60\tPASS\t.\tGT:DP:GQ\t0/1:30:60\n1\t202\t.\tC\tT\t10\tLowQual\t.\tGT:DP:GQ\t0/1:3:5\n1\t303\t.\tG\tA\t60\tPASS\t.\tGT:DP:GQ\t./.:0:0\n'
        (output/'mini.vcf').write_text(text,encoding='utf-8')
        passed=[]
        for line in text.splitlines():
            if line.startswith('#'):continue
            fields=line.split('\t'); sample=dict(zip(fields[8].split(':'),fields[9].split(':')))
            if fields[6]=='PASS' and int(sample['DP'])>=10 and int(sample['GQ'])>=20 and '.' not in sample['GT']:
                passed.append(int(fields[1]))
        assert passed==[101]
        return {'method':'fixed VCF downstream genotype QC','accepted_positions':passed,'limit':'Full FASTQ→alignment→joint calling→normalization→truth-set comparison NOT executed; requires a prebuilt GATK/bcftools environment and licensed/reference data.'}
    check('variant_qc_only',variant_qc)
    report['unverified_workflows']=['whole_genome_FASTQ_to_joint_variant_calls','production_MOFA_missing_views','production_DESeq2_or_edgeR','real_data_external_validation','agent_generated_pipeline_execution_in_OS_network_isolation']
    report['versions']={}
    for name in ['numpy','scipy','pandas','scikit-learn','statsmodels','scanpy','anndata']:
        try: report['versions'][name]=importlib.metadata.version(name)
        except importlib.metadata.PackageNotFoundError: report['versions'][name]=None
    report['files']={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in output.iterdir() if p.is_file() and p.name!='pipeline-report.json'}
    report['all_implemented_checks_passed']=all(c['status']=='passed' for c in report['checks'])
    dump(output/'pipeline-report.json',report)
    print(json.dumps(report,indent=2))
    return 0 if report['all_implemented_checks_passed'] else 1


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output',required=True);args=p.parse_args()
    raise SystemExit(run(args.output))
