import copy
import unittest
from pathlib import Path
import uuid

from lsrw.grading import concept_diagnostics, resolve_ratings, validate_key
from lsrw.reproduction import check_reproduction
from lsrw.runner import execute, response_slots, dry_run
from lsrw.results import score_run, verify_scores
from lsrw.review import prepare_review, save_rating
from lsrw.storage import read_json, write_new, digest, file_hash
from lsrw.taxonomy import FOLLOWUP_FIELDS
from lsrw import service


class OpenProtocolTests(unittest.TestCase):
    def setUp(self):
        # Reuse the explicitly synthetic fixture builder, not scientific answer keys.
        from test_workbench import WorkbenchTests
        self.fixture=WorkbenchTests()
        self.fixture.work=Path(__file__).resolve().parents[1]/'.test-work'/uuid.uuid4().hex
        self.fixture.work.mkdir(parents=True)
        from lsrw.dataset import load_dataset
        self.fixture.pilot=load_dataset(Path(__file__).resolve().parents[1]/'data/public/items.jsonl')

    def test_only_three_open_task_types_and_long_answer_gate(self):
        self.assertEqual({i['ability'] for i in self.fixture.pilot},{'essay','experimental_design','research_reasoning'})
        self.assertTrue(all(i['response_type']=='open' and not i['choices'] for i in self.fixture.pilot))
        keys=read_json(self.fixture.toy_keys());item=self.fixture.pilot[0]
        keys[item['id']]['reference_answer']='A correct-looking but underspecified answer.'
        with self.assertRaisesRegex(ValueError,'shorter'):validate_key(item,keys[item['id']])

    def test_user_benefit_is_primary_and_a_useful_alternative_can_miss_history(self):
        pair=[self.fixture.rating('research_reasoning',reviewer=r,values=[3]*5) for r in ['a','b']]
        for rating in pair:rating['user_service']=dict.fromkeys(service.DIMENSIONS,4)
        result=resolve_ratings(pair,'research_reasoning')
        self.assertEqual(result['score'],100)
        self.assertEqual(result['task_quality_score'],75)
        self.assertFalse(result['historical_hit'])
        for rating in pair:rating['user_service']['scientific_accuracy']=0
        self.assertLessEqual(resolve_ratings(pair,'research_reasoning')['score'],20)
        pair[1]['user_service']['scientific_accuracy']=1
        self.assertEqual(resolve_ratings(pair,'research_reasoning')['status'],'needs_adjudication')

    def test_five_independent_samples_are_distinct_from_transport_retries(self):
        config=self.fixture.config(generation={'seed':17})
        self.assertEqual(dry_run(config)['initial_requests'],36)
        root=execute(config,sleep=lambda _:None)
        item=next(i for i in self.fixture.pilot if i['ability']=='research_reasoning')
        records=[read_json(root/'responses'/(s+'.json')) for s,_ in response_slots(item)]
        self.assertEqual(len(records),5)
        self.assertEqual([r['generation']['seed'] for r in records],[17,18,19,20,21])
        self.assertEqual(len({r['request_sha256'] for r in records}),1)
        self.assertTrue(all(len(r['attempts'])==1 for r in records))
        self.assertEqual(read_json(root/'completion.json')['total'],36)

    def test_keyword_presence_and_partial_target_matching_cannot_award_hit(self):
        key={'required_concepts':[{'id':'rescue','aliases':['rescue'],'criterion':'Functional rescue after a valid perturbation'}], 'logic_chain':[]}
        result=concept_diagnostics('Rescue rescue; rescue proves nothing and was never tested.',key)
        self.assertIsNone(result['automatic_score'])
        self.assertTrue(result['concepts'][0]['matched_aliases'])
        pair=[self.fixture.rating('research_reasoning',reviewer=r,values=[4]*5) for r in ['a','b']]
        for rating in pair:
            rating['followup_match']=dict.fromkeys(FOLLOWUP_FIELDS,True)
            rating['followup_match']['readout']=False
        self.assertFalse(resolve_ratings(pair,'research_reasoning')['historical_hit'])
        for rating in pair:
            rating['followup_match']['readout']=True
            rating['scores']['task_detail']=1
        self.assertFalse(resolve_ratings(pair,'research_reasoning')['historical_hit'])

    def test_best_of_five_never_combines_partial_matches(self):
        root=execute(self.fixture.config(),sleep=lambda _:None)
        key_path=self.fixture.toy_keys()
        reviews=prepare_review(root,key_path,self.fixture.work/'review',['a','b'])
        coordinator=read_json(reviews/'coordinator-only.json')
        for folder in ['rater-1','rater-2']:
            queue_path=reviews/folder/'queue.json';queue=read_json(queue_path)
            for entry in queue['items']:
                ability=entry['question']['ability']
                rating=self.fixture.rating(ability,queue['reviewer'],[4]*5)
                if ability=='research_reasoning':
                    response_id=coordinator['mapping'][entry['blind_id']]
                    n=read_json(root/'responses'/(response_id+'.json'))['sample_number']
                    rating['followup_match']=dict.fromkeys(FOLLOWUP_FIELDS,True)
                    rating['followup_match'][FOLLOWUP_FIELDS[n-1]]=False
                save_rating(queue_path,entry['blind_id'],rating)
        scores=verify_scores(score_run(root,key_path,reviews))
        reasoning=[r for r in scores['rows'] if r['ability']=='research_reasoning']
        self.assertTrue(all(r['historical_hit_at_5']==0 and r['samples_scored']==5 for r in reasoning))
        self.assertEqual(len(scores['sample_rows']),36)

    def test_missing_sample_review_leaves_best_of_five_pending(self):
        root=execute(self.fixture.config(),sleep=lambda _:None)
        keys=self.fixture.toy_keys()
        scores=verify_scores(score_run(root,keys))
        self.assertTrue(all(r['score'] is None and r['historical_hit_at_5'] is None for r in scores['rows']))

    def test_reproduction_rejects_processed_inputs_omissions_and_changed_files(self):
        root=self.fixture.work
        for name in ['raw','code','environment','execution_log','figure','derived_table']:
            (root/(name+'.txt')).write_text('Synthetic test fixture only',encoding='utf-8')
        raw={'level':'raw','accession':'test-only','license':'test-only','path':'raw.txt','sha256':file_hash(root/'raw.txt')}
        spec={'paper_doi':'test-only','figure_panels':['test'], 'raw_inputs':[raw], 'reference_build':'test','software_lock':'test',
              'targets':{'effect':{'expected':2,'absolute_tolerance':.1,'relative_tolerance':0}}}
        submission={'spec_sha256':digest(spec),'metrics':{'effect':2.05},'artifacts':{n:{'path':n+'.txt','sha256':file_hash(root/(n+'.txt'))} for n in ['code','environment','execution_log','figure','derived_table']}}
        result=check_reproduction(spec,submission,root)
        self.assertTrue(result['numerical_agreement']);self.assertFalse(result['agent_capability_verified'])
        missing=copy.deepcopy(submission);missing['metrics']={}
        with self.assertRaises(ValueError):check_reproduction(spec,missing,root)
        processed=copy.deepcopy(spec);processed['raw_inputs'][0]['level']='normalized_counts'
        with self.assertRaisesRegex(ValueError,'genuine raw'):check_reproduction(processed,{**submission,'spec_sha256':digest(processed)},root)
        (root/'raw.txt').write_text('changed',encoding='utf-8')
        with self.assertRaisesRegex(ValueError,'checksum'):check_reproduction(spec,submission,root)


if __name__=='__main__':unittest.main()
