"""Verify published records and reproduce both scoring rounds; no scientific judging or API calls."""
from pathlib import Path
import csv,hashlib,json,math
from collections import Counter
from statistics import mean
HERE=Path(__file__).resolve().parent
REPO=HERE.parent
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
MATCH=('biological_question','mechanism','intervention','readout','predicted_outcome')
WEIGHTS={'scientific_accuracy':35,'decision_value':25,'actionability':20,'verifiability':15,'communication':5}
CAT={'essay':.2,'experimental_design':.3,'research_reasoning':.5}
def close(a,b):assert math.isclose(float(a),float(b),rel_tol=0,abs_tol=1e-8),(a,b)
def main():
 for rel,digest in read(HERE/'SHA256SUMS.json').items():assert sha(HERE/rel)==digest,rel
 manifest=read(HERE/'EXPORT-MANIFEST.json')
 exports={x['file']:x for x in manifest['review_exports']}
 for rel,x in exports.items():assert sha(HERE/rel)==x['published_sha256'],rel
 items={i['id']:i for i in read(REPO/'benchmark-30/v1/questions.json')}
 app=read(REPO/'benchmark-30/v2/applicability.json')
 models=sorted(p.name for p in (HERE/'answers').iterdir() if p.is_dir())
 assert len(models)==12 and len(items)==30
 pub1={r['code']:r for r in csv.DictReader((REPO/'docs/first-round-20261003/model-summary.csv').open(encoding='utf-8-sig'))}
 pub2={r['model_code']:r for r in csv.DictReader((REPO/'docs/second-round-20261004/model-summary.csv').open(encoding='utf-8-sig'))}
 reports=[];checks=0;reviews=0
 for code in models:
  assert {p.stem for p in (HERE/'answers'/code).glob('*.json')}==set(items)
  grouped={n:{k:[] for k in CAT} for n in (1,2)};ex={1:[],2:[]};hitcounts={1:0,2:0}
  for iid,item in items.items():
   a=read(HERE/'answers'/code/(iid+'.json'));text=a['answer']
   assert hashlib.sha256(text.encode()).hexdigest()==a['answer_utf8_sha256']
   r1=read(HERE/'round-one/reviews'/code/(iid+'.json'));r2=read(HERE/'round-two/reviews'/code/(iid+'.json'))
   assert a['original_candidate_record_sha256']==r1['candidate_sha256']==r2['candidate_sha256']
   rel=f'round-one/reviews/{code}/{iid}.json';assert r2['first_round_review_sha256']==exports[rel]['original_sha256']
   q1=sum(WEIGHTS[k]*r1['service'][k]/4 for k in WEIGHTS)
   if r1['service']['scientific_accuracy']==0:q1=min(20,q1)
   close(q1,r1['service_score'])
   for e in r1.get('errors',[]):
    if e.get('quote'):assert e['quote'] in text,(code,iid,'v1 quote')
   if r1['reasoning_index'] is not None:
    close(sum(r1['reasoning'].values())*6.25,r1['reasoning_index']);ex[1].append(r1['reasoning_index'])
   ids=[c['id'] for c in r2['checks']];assert len(ids)==len(set(ids)) and set(ids)==set(app[iid]['applicable_checks'])
   assert r2['complete_final_answer_read']
   for c in r2['checks']:
    assert c['quote'] in text,(code,iid,c['id'],'v2 quote')
    if not c['quote']:assert c['evidence_type'] in ('absent_after_full_read','empty_final_answer')
    if c['state']!='unmet':assert c['points']==0
    if c.get('covered_by'):assert c['points']==0 and any(t['id']==c['covered_by'] and t['points']>0 for t in r2['checks'])
    checks+=1
   q2=max(0,100-sum(c['points'] for c in r2['checks']))
   if r2.get('central_false_premise'):q2=min(20,q2)
   if r2.get('override'):assert not text.strip();q2=0
   close(q2,r2['quality_score'])
   if r2['explanation_index'] is not None:
    close(sum(r2['explanation_scores'].values())*6.25,r2['explanation_index']);ex[2].append(r2['explanation_index'])
   for n,r,q,key in ((1,r1,q1,'followup_match'),(2,r2,q2,'historical_match')):
    score=q
    if item['ability']=='research_reasoning':
     match=r[key];assert set(match)==set(MATCH) and all(type(v)==bool for v in match.values())
     hit=all(match.values());hitcounts[n]+=hit;score=60*hit+.4*q
    if n==2:close(score,r2['item_score'])
    grouped[n][item['ability']].append(score);reviews+=1
  vals={}
  for n,report in ((1,pub1[code]),(2,pub2[code])):
   assert all(len(v)==10 for v in grouped[n].values())
   means={k:mean(v) for k,v in grouped[n].items()};total=sum(CAT[k]*v for k,v in means.items());vals[n]=total
   close(total,report['score' if n==1 else 'total_score'])
   for cat,col1,col2 in [('essay','essay','essay_mean'),('experimental_design','design','design_mean'),('research_reasoning','research','research_mean')]:close(means[cat],report[col1 if n==1 else col2])
   close(mean(ex[n]),report['explanation' if n==1 else 'explanation_mean'])
   assert hitcounts[n]==int(report['historical_hits' if n==1 else 'research_hits'])
  reports.append((code,vals[1],vals[2]))
 assert reviews==720 and checks==7560
 print(f'PASS: 360 answers, {reviews} reviews, {checks} strict checks; hashes, exact deduction quotes and all 24 model totals verified.')
 for code,v1,v2 in reports:print(f'{code:18s} round one {v1:6.2f}  round two {v2:6.2f}')
if __name__=='__main__':main()
