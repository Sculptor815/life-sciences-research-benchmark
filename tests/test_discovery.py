import copy
import json
from pathlib import Path
import sys
import unittest
import uuid
import asyncio
from types import SimpleNamespace
from unittest.mock import patch

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
from lsrw.discovery import audit, export_drafts, import_decisions, render_review, validate_corpus
from lsrw.runner import load_config, prepare
from lsrw.storage import digest, read_json, write_new
from lsrw.adapters import InspectAdapter, RunError
from lsrw.runner import execute, verify_run


class DiscoveryTests(unittest.TestCase):
    def setUp(self):
        self.work=ROOT/'.test-work'/uuid.uuid4().hex
        self.work.mkdir(parents=True)
        self.corpus={'cases':[{'id':'test-case','domain':'biochemistry','paper':{'title':'Test-only fictional paper','url':'https://example.invalid','read_depth':'abstract'},
            'original_question':'Can the two mechanisms be distinguished?','experimental_design':'Independent controlled perturbations.',
            'questions':[{'ability':'essay','prompt':'Explain the supported inference.','reference_answer':'PRIVATE-CANARY '+('fixture '*350),'scoring_points':['bounded inference']},
                         {'ability':'research_reasoning','prompt':'Propose a discriminating test.','reference_answer':'PRIVATE-REASONING-CANARY '+('fixture '*1300),'scoring_points':['opposing predictions']}]}]}
    def payload(self):
        c=self.corpus['cases'][0]
        return {'corpus_sha256':digest(self.corpus),'reviewer':'test-human',
                'decisions':[{'case_id':c['id'],'case_sha256':digest(c),'decision':'retain','notes':'Test fixture only; not a real approval.',
                'checks':dict.fromkeys(['source_read','question_fair','answer_checked','rights_checked'],True)}]}
    def test_unverified_sources_are_visible_and_not_promoted(self):
        result=audit(self.corpus)
        self.assertTrue(result['valid']);self.assertFalse(result['formal_ready'])
        self.assertIn('original full text not completely verified',result['readiness_gaps'][0]['reasons'])
        self.assertIn('textbook bibliography link not verified',result['readiness_gaps'][0]['reasons'])
    def test_export_separates_answers_and_does_not_assign_splits(self):
        export_drafts(self.corpus,self.work/'drafts')
        visible=(self.work/'drafts/candidates.json').read_text(encoding='utf-8')
        self.assertNotIn('PRIVATE-CANARY',visible);self.assertNotIn('PRIVATE-REASONING-CANARY',visible)
        self.assertTrue(all(c['split']=='unassigned' for c in read_json(self.work/'drafts/candidates.json')))
    def test_stale_review_and_duplicate_decision_are_rejected(self):
        p=self.payload();self.corpus['cases'][0]['questions'][0]['prompt']='Changed'
        with self.assertRaises(ValueError):import_decisions(self.corpus,p,self.work/'decisions')
        p=self.payload();p['decisions']*=2
        with self.assertRaises(ValueError):import_decisions(self.corpus,p,self.work/'decisions')
    def test_retaining_requires_all_human_checks(self):
        p=self.payload();p['decisions'][0]['checks']['source_read']=False
        with self.assertRaises(ValueError):import_decisions(self.corpus,p,self.work/'decisions')
        p['decisions'][0]['decision']='revise'
        record=import_decisions(self.corpus,p,self.work/'decisions')
        self.assertEqual(record['review_type'],'candidate_selection_not_formal_bank_approval')
        self.assertFalse(audit(self.corpus)['formal_ready'])
    def test_exported_review_cannot_impersonate_formal_approval(self):
        p=self.payload();p['review_type']='formal_approved'
        self.assertEqual(import_decisions(self.corpus,p,self.work/'d')['review_type'],'candidate_selection_not_formal_bank_approval')
    def test_source_html_cannot_escape_embedded_json(self):
        self.corpus['cases'][0]['paper']['title']='</script><script>alert("x")</script>'
        page=render_review(self.corpus,self.work/'review.html').read_text(encoding='utf-8')
        self.assertNotIn('</script><script>alert',page)
        self.assertIn('\\u003c/script>',page)
    def test_invalid_knowledge_answer_is_a_validation_error(self):
        self.corpus['cases'][0]['questions'][0]['ability']='knowledge'
        self.assertTrue(validate_corpus(self.corpus))
    def test_question_variants_keep_distinct_answers(self):
        q=copy.deepcopy(self.corpus['cases'][0]['questions'][1]);q['id']='variant-two';q['reference_answer']='OTHER-ANSWER '+('fixture '*1300)
        self.corpus['cases'][0]['questions'].append(q)
        export_drafts(self.corpus,self.work/'variants')
        self.assertEqual(len(read_json(self.work/'variants/reference-answers.json')),3)
        self.corpus['cases'][0]['questions'].append(q)
        self.assertTrue(validate_corpus(self.corpus))
    def test_malformed_corpora_report_errors_without_crashing(self):
        for bad in [None,{}, {'cases':[None]}, {'cases':[{'id':False,'questions':None}]}]:
            self.assertFalse(audit(bad)['valid'])
        self.corpus['cases'][0]['questions'][0]['ability']='knowledge'
        self.corpus['cases'][0]['questions'][0]['choices']=None
        self.assertFalse(audit(self.corpus)['valid'])
        p=self.payload();p['decisions']=[None]
        with self.assertRaises(ValueError):import_decisions(self.corpus,p,self.work/'bad')
    def test_adapter_initialization_failure_is_explicit_and_sanitized(self):
        config=load_config(ROOT/'configs/mock.json');config['output_root']=str(self.work/'runs')
        with patch('lsrw.runner.MockAdapter',side_effect=RuntimeError('SECRET-CANARY')):
            with self.assertRaisesRegex(ValueError,'no model calls started'):execute(config)
        run=next((self.work/'runs').iterdir())
        self.assertEqual(read_json(run/'aborted.json')['calls_started'],0)
        self.assertNotIn('SECRET-CANARY',''.join(p.read_text(encoding='utf-8') for p in run.glob('*.json')))
        with self.assertRaisesRegex(ValueError,'incomplete or aborted'):verify_run(run)
    def test_provider_tool_request_is_rejected(self):
        try:import inspect_ai
        except ImportError:self.skipTest('Optional inspect runtime not installed')
        class ToolReturningModel:
            async def generate(self,*args,**kwargs):
                self.kwargs=kwargs
                return SimpleNamespace(choices=[SimpleNamespace(message=SimpleNamespace(tool_calls=['browser-call']))])
        adapter=InspectAdapter.__new__(InspectAdapter);adapter.loop=asyncio.Runner();adapter.model=ToolReturningModel();adapter.generation=None
        try:
            with self.assertRaises(RunError) as raised:adapter.generate({'text':'test','images':[],'system':'fixed packet'}, {})
            self.assertEqual(raised.exception.status,'forbidden_tool_request')
            self.assertEqual(adapter.model.kwargs['tools'],[]);self.assertEqual(adapter.model.kwargs['tool_choice'],'none')
        finally:adapter.loop.close()
    def test_browsing_cannot_be_enabled_through_config(self):
        config=read_json(ROOT/'configs/mock.json');config['evidence_mode']='web'
        write_new(self.work/'bad.json',config)
        with self.assertRaises(ValueError):load_config(self.work/'bad.json')
        with self.assertRaises(ValueError):prepare(config)
        config['evidence_mode']='fixed_packet';config['generation']={'tools':['web_search']}
        write_new(self.work/'tools.json',config)
        with self.assertRaises(ValueError):load_config(self.work/'tools.json')


if __name__=='__main__':unittest.main()
