import copy
import unittest
from lsrw.question_quality import summarize, DIMENSIONS


class QualityTests(unittest.TestCase):
    def setUp(self):
        self.record={'candidate_id':'test-only','scores':dict.fromkeys(DIMENSIONS,3),
                     'rationales_by_dimension':dict.fromkeys(DIMENSIONS,'Test fixture rationale.'),
                     'current_literature_review':{'status':'not_started'}}
        self.record['scores']['novelty']=None
    def test_unknown_novelty_is_not_zero_or_a_complete_score(self):
        result=summarize(self.record)
        self.assertEqual(result['partial_score'],15);self.assertIsNone(result['total_score'])
        self.assertFalse(result['formal_rank_eligible'])
        self.record['scores']['novelty']=4
        with self.assertRaises(ValueError):summarize(self.record)
    def test_complete_record_still_is_not_an_approval(self):
        self.record['scores']['novelty']=2
        self.record['current_literature_review']={'status':'completed_within_declared_scope','search_log':['test-only search'],'closest_prior_studies':['test-only record']}
        result=summarize(self.record)
        self.assertEqual(result['total_score'],17);self.assertFalse(result['formal_rank_eligible'])
    def test_invalid_scores_and_absent_reason_are_rejected(self):
        for value in [True,4.5,-1,5]:
            record=copy.deepcopy(self.record);record['scores']['importance']=value
            with self.assertRaises(ValueError):summarize(record)
        self.record['rationales_by_dimension'].pop('importance')
        with self.assertRaises(ValueError):summarize(self.record)


if __name__=='__main__':unittest.main()
