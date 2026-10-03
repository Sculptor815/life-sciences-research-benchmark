import copy
import json
import math
import os
from pathlib import Path
import sys
import unittest
import uuid
import zipfile

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT/"src"))

from lsrw.adapters import MockAdapter
from lsrw.curation import calibration
from lsrw.dataset import load_dataset, validate
from lsrw.grading import objective_score, resolve_ratings, validate_key, validate_rating
from lsrw.prompts import visible_request
from lsrw.results import compare, report, score_run, summarize, verify_scores
from lsrw.review import collect_reviews, prepare_review, save_rating
from lsrw.runner import dry_run, execute, load_config, verify_run
from lsrw.statistics import family_interval, macro, paired_comparison
from lsrw.storage import digest, read_json, write_new
from lsrw.taxonomy import ABILITIES, CELL_COUNTS, DIMENSIONS, DOMAINS, TOPICS


class WorkbenchTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.work = ROOT/".test-work"/uuid.uuid4().hex
        cls.work.mkdir(parents=True)
        cls.pilot = load_dataset(ROOT/"data/public/items.jsonl")

    def config(self, **changes):
        config = load_config(ROOT/"configs/mock.json")
        config["output_root"] = str(self.work/"runs")
        config.update(changes)
        return config

    def rating(self, ability="experimental_design", reviewer="r1", values=None):
        return {"reviewer":reviewer,"scores":dict(zip(DIMENSIONS[ability],values or [3]*5)),"rationale":"Test-only expert-style record; not an actual human judgment.",
                "source_correct":True if ability=="paper_appraisal" else None,"conclusion_correct":True if ability=="paper_appraisal" else None,"refusal":False}

    def toy_keys(self):
        # Deliberately arbitrary keys test plumbing, not the scientific pilot answers.
        keys = {}
        for item in self.pilot:
            key = {"id":item["id"],"version":"test-only","references":[{"source":"test fixture"}]}
            if item["response_type"]=="choice":
                key["answer"]="A"
            elif item["response_type"]=="numeric":
                key.update(value=2,units=["u"],absolute_tolerance=.01,relative_tolerance=0)
            else:
                key["dimensions"]={d:{"anchors":{str(n):"Test rubric "+str(n) for n in range(5)},"acceptable_alternatives":["fixture"],"critical_errors":["fixture"]} for d in DIMENSIONS[item["ability"]]}
                if item["ability"]=="paper_appraisal":
                    key.update(source_state="insufficient_to_verify",support_state="insufficient_evidence")
            keys[item["id"]]=key
        path=self.work/(uuid.uuid4().hex+"-keys.json")
        write_new(path,keys)
        return path

    def full_fixture(self):
        result=[]
        source=self.pilot[0]
        image=next(i for i in self.pilot if i["modality"]=="image")
        for domain in DOMAINS:
            for ability in ABILITIES:
                for (split,modality),count in CELL_COUNTS.items():
                    for n in range(count):
                        item=copy.deepcopy(image if modality=="image" else source)
                        item.update(id=f"{domain}-{ability}-{split}-{modality}-{n}",domain=domain,ability=ability,split=split,status="reviewed",topics=list(TOPICS[domain]),response_type="choice" if ability=="knowledge" else "open",choices=source["choices"] if ability=="knowledge" else {},packet="Test-only packet")
                        item["family_id"]=item["source_family"]=item["id"]
                        result.append(item)
        return result

    def test_pilot_has_sixteen_cells_and_four_visuals(self):
        self.assertEqual(len(self.pilot),20)
        self.assertEqual(len({(i["domain"],i["ability"]) for i in self.pilot}),16)
        self.assertEqual(sum(i["modality"]=="image" for i in self.pilot),4)

    def test_formal_counts_accept_320_fixture(self):
        items=self.full_fixture()
        self.assertEqual(len(items),320)
        self.assertEqual(validate(items,ROOT/"data/public",True),[])
        self.assertTrue(validate(items[:-1],ROOT/"data/public",True))

    def test_pilot_is_not_formal(self):
        self.assertTrue(validate(self.pilot,ROOT/"data/public",True))

    def test_family_and_source_leakage_rejected(self):
        a,b=copy.deepcopy(self.pilot[:2]); b["split"]="heldout"
        for field in ("family_id","source_family"):
            b[field]=a[field]
            self.assertTrue(any("crosses" in e for e in validate([a,b],ROOT/"data/public")))

    def test_unknown_answer_metadata_rejected(self):
        item=copy.deepcopy(self.pilot[0]); item["answer"]="B"
        self.assertTrue(validate([item],ROOT/"data/public"))

    def test_requests_ignore_arbitrary_grader_data(self):
        item=copy.deepcopy(self.pilot[0]); item.update(answer="CANARY-GOLD-SECRET",rubric="CANARY-GOLD-SECRET")
        request=visible_request(item,ROOT/"data/public")
        self.assertNotIn("CANARY-GOLD-SECRET",json.dumps(request))
        self.assertNotIn("family_id",request["text"])

    def test_image_hash_and_path_escape_rejected(self):
        item=copy.deepcopy(self.pilot[-1]); item["materials"][0]["sha256"]="bad"
        self.assertTrue(validate([item],ROOT/"data/public"))
        item["materials"][0]["path"]="../../outside.png"
        self.assertTrue(validate([item],ROOT/"data/public"))

    def test_field_types_fail_cleanly(self):
        item=copy.deepcopy(self.pilot[0]); item["prompt"]=[]
        self.assertTrue(validate([item],ROOT/"data/public"))
        self.assertTrue(validate([],ROOT))

    def test_choice_correct_wrong_malformed_empty(self):
        key={"answer":"B"}
        self.assertEqual(objective_score('{"answer":"B"}',key,"choice")["score"],100)
        self.assertEqual(objective_score('{"answer":"A"}',key,"choice")["score"],0)
        for text in ("", "A B", "{bad", '{"answer":["B"]}'):
            self.assertFalse(objective_score(text,key,"choice")["format_valid"])

    def test_numeric_tolerance_units_nan(self):
        key={"value":30,"units":["nmol/min","nmol min^-1"],"absolute_tolerance":.02,"relative_tolerance":0}
        for unit in key["units"]:
            self.assertEqual(objective_score(json.dumps({"value":30.01,"unit":unit}),key,"numeric")["score"],100)
        self.assertEqual(objective_score('{"value":30,"unit":"mol/min"}',key,"numeric")["score"],0)
        self.assertFalse(objective_score('{"value":NaN,"unit":"nmol/min"}',key,"numeric")["format_valid"])

    def test_dimension_disagreement_threshold(self):
        left=self.rating(values=[1,3,3,3,3]); right=self.rating(reviewer="r2",values=[3,3,3,3,3])
        self.assertEqual(resolve_ratings([left,right],"experimental_design")["status"],"needs_adjudication")

    def test_total_disagreement_strictly_over_ten(self):
        left=self.rating(values=[2,2,3,3,3]); right=self.rating(reviewer="r2")
        self.assertEqual(resolve_ratings([left,right],"experimental_design")["status"],"scored")
        left=self.rating(values=[2,2,2,3,3])
        self.assertEqual(resolve_ratings([left,right],"experimental_design")["status"],"needs_adjudication")

    def test_adjudicator_independence_and_original_preservation(self):
        pair=[self.rating(values=[0]*5),self.rating(reviewer="r2",values=[4]*5)]
        before=copy.deepcopy(pair)
        with self.assertRaises(ValueError): resolve_ratings(pair,"experimental_design",self.rating())
        result=resolve_ratings(pair,"experimental_design",self.rating(reviewer="r3",values=[2]*5))
        self.assertEqual(result["score"],50)
        self.assertEqual(pair,before)

    def test_invalid_rating_and_self_pair_rejected(self):
        bad=self.rating(); bad["scores"]["controls"]=True
        with self.assertRaises(ValueError): validate_rating(bad,"experimental_design")
        with self.assertRaises(ValueError): resolve_ratings([self.rating(),self.rating()],"experimental_design")

    def test_model_identity_cannot_change_objective_grading(self):
        key={"answer":"A"}
        for name in ("model-X","model-Y"):
            self.assertEqual(objective_score(json.dumps({"answer":"A","model":name}),key,"choice")["score"],100)

    def test_retry_only_transport_two_retries(self):
        root=execute(self.config(mock_events=["rate_limit","timeout","ok"]),sleep=lambda _:None)
        first=read_json(root/"responses"/(self.pilot[0]["id"]+".json"))
        self.assertEqual([a["status"] for a in first["attempts"]],["rate_limit","timeout","completed"])
        root=execute(self.config(mock_events=["timeout"]*3),sleep=lambda _:None)
        first=read_json(root/"responses"/(self.pilot[0]["id"]+".json"))
        self.assertEqual(len(first["attempts"]),3); self.assertEqual(first["status"],"timeout")

    def test_no_retry_empty_refusal_or_malformed_completion(self):
        for event in ("empty","refusal","malformed"):
            root=execute(self.config(mock_events=[event]),sleep=lambda _:None)
            first=read_json(root/"responses"/(self.pilot[0]["id"]+".json"))
            self.assertEqual(first["status"],"completed"); self.assertEqual(len(first["attempts"]),1)

    def test_context_error_and_image_unsupported_are_not_scientific_zeros(self):
        root=execute(self.config(mock_events=["context_limit"],supports_images=False),sleep=lambda _:None)
        scores=verify_scores(score_run(root,self.toy_keys()))
        self.assertIsNone(scores["rows"][0]["score"])
        self.assertTrue(all(r["status"]=="unsupported_image" and r["score"] is None for r in scores["rows"] if r["modality"]=="image"))

    def test_budget_exhaustion_stops_before_request(self):
        root=execute(self.config(input_usd_per_million=10,output_usd_per_million=10,budget_usd=.172),sleep=lambda _:None)
        completion=read_json(root/"completion.json")
        self.assertEqual(completion["completed"],1)
        self.assertAlmostEqual(completion["reserved_usd"],.172)

    def test_dry_run_writes_nothing(self):
        config=self.config(output_root=str(self.work/"should-not-exist"))
        result=dry_run(config)
        self.assertEqual(result["maximum_attempts"],60)
        self.assertFalse(Path(config["output_root"]).exists())

    def test_invalid_live_budget_and_generation_override(self):
        config=self.config(backend="inspect")
        path=self.work/"invalid-live.json"; write_new(path,config)
        with self.assertRaises(ValueError): load_config(path)
        config=self.config(generation={"max_retries":100})
        path=self.work/"invalid-override.json"; write_new(path,config)
        with self.assertRaises(ValueError): load_config(path)

    def test_immutable_run_detects_tampering(self):
        root=execute(self.config(),sleep=lambda _:None)
        verify_run(root)
        (root/"items.json").write_text("[]",encoding="utf-8")
        with self.assertRaises(ValueError): verify_run(root)

    def test_blind_review_scoring_and_report_reproducibility(self):
        root=execute(self.config(model="MODEL-IDENTITY-CANARY"),sleep=lambda _:None)
        keypath=self.toy_keys()
        reviews=prepare_review(root,keypath,self.work/"reviews",["first","second"])
        for folder in ("rater-1","rater-2"):
            path=reviews/folder/"queue.json"; queue=read_json(path)
            self.assertNotIn("MODEL-IDENTITY-CANARY",path.read_text(encoding="utf-8"))
            for entry in queue["items"]:
                save_rating(path,entry["blind_id"],self.rating(entry["question"]["ability"],queue["reviewer"]))
        scorepath=score_run(root,keypath,reviews)
        self.assertEqual(scorepath,score_run(root,keypath,reviews))
        summary=summarize(verify_scores(scorepath))
        self.assertFalse(summary["tracks"]["text"]["eligible_for_formal_leaderboard"])
        self.assertEqual(summary["tracks"]["text"]["scored"],16)
        a=report(scorepath,self.work/"report-a"); b=report(scorepath,self.work/"report-b")
        self.assertEqual(a.read_bytes(),b.read_bytes())

    def test_no_overwriting_ratings(self):
        path=self.work/"write-once.json"; write_new(path,{"a":1})
        with self.assertRaises(FileExistsError): write_new(path,{"a":2})

    def test_macro_equal_cells_not_item_weighted(self):
        rows=[]
        for d in DOMAINS:
            for a in ABILITIES:
                rows.append({"domain":d,"ability":a,"score":100 if (d,a)==(DOMAINS[0],ABILITIES[0]) else 0,"family_id":d+a})
        rows.extend([rows[0].copy() for _ in range(9)])
        self.assertEqual(macro(rows),6.25)

    def test_cluster_bootstrap_and_pairing_reproducible(self):
        rows=[]
        for d in DOMAINS:
            for a in ABILITIES:
                for n in range(10):
                    rows.append({"id":d+a+str(n),"domain":d,"ability":a,"score":60,"family_id":d+a+str(n),"modality":"text"})
        a=family_interval(rows,draws=500); b=family_interval(rows,draws=500)
        self.assertEqual(a,b); self.assertEqual(a["interval"],[60,60])
        other=[{**r,"score":50} for r in rows]
        result=paired_comparison(rows,other)
        self.assertEqual(result["difference_left_minus_right"],10)
        with self.assertRaises(ValueError): paired_comparison(rows,other[:-1])

    def test_no_ci_or_overall_with_missing_cells(self):
        rows=[{"domain":"molecular_biology","ability":"knowledge","score":100,"family_id":"one"}]
        self.assertIsNone(macro(rows)); self.assertIsNone(family_interval(rows)["interval"])

    def test_image_target_three_families_per_cell_preserves_cells(self):
        rows=[{"domain":d,"ability":a,"score":50+n*10,"family_id":d+a+str(n)} for d in DOMAINS for a in ABILITIES for n in range(3)]
        result=family_interval(rows,draws=500)
        self.assertEqual(result["valid_draws"],500)
        self.assertIsNotNone(result["interval"])

    def test_calibration_statistics(self):
        result=calibration([{"ability":"experimental_design","ratings":[self.rating(),self.rating(reviewer="r2")]}])
        self.assertEqual(result["dimension_exact_agreement"],1)
        self.assertEqual(result["total_mean_absolute_difference_percentage_points"],0)

    def test_unknown_usage_halts_next_paid_request(self):
        class MissingUsageAdapter(MockAdapter):
            def generate(self, request, config):
                return {**super().generate(request,config),"input_tokens":None,"output_tokens":None}
        config=self.config(backend="inspect")
        run=execute(config,adapter=MissingUsageAdapter(config),sleep=lambda _:None)
        completion=read_json(run/"completion.json")
        self.assertEqual(completion["completed"],1)
        self.assertTrue(completion["billing_uncertain"])

    def test_failed_attempts_keep_budget_reservations(self):
        config=self.config(input_usd_per_million=10,output_usd_per_million=10,budget_usd=.344,mock_events=["rate_limit","timeout"])
        run=execute(config,sleep=lambda _:None)
        first=read_json(run/"responses"/(self.pilot[0]["id"]+".json"))
        self.assertEqual(first["status"],"budget_exhausted")
        self.assertEqual(len(first["attempts"]),2)
        self.assertEqual(read_json(run/"completion.json")["completed"],0)

    def test_package_allowlist_rejects_private_and_heldout(self):
        sys.path.insert(0,str(ROOT/"scripts"))
        from package_release import package
        work=self.work/"package-fixture"; work.mkdir()
        (work/"visible.txt").write_text("public",encoding="utf-8")
        (work/"not-listed.txt").write_text("secret",encoding="utf-8")
        (work/"manifest.txt").write_text("visible.txt\n",encoding="utf-8")
        package(work,work/"manifest.txt",work/"safe.zip")
        with zipfile.ZipFile(work/"safe.zip") as archive:
            self.assertNotIn("not-listed.txt",archive.namelist())
        (work/"items.jsonl").write_text(json.dumps({"split":"heldout"})+"\n",encoding="utf-8")
        (work/"bad-manifest.txt").write_text("items.jsonl\n",encoding="utf-8")
        with self.assertRaises(ValueError): package(work,work/"bad-manifest.txt",work/"bad.zip")

    def test_score_artifact_tampering_detected(self):
        run=execute(self.config(),sleep=lambda _:None)
        path=score_run(run,self.toy_keys())
        data=read_json(path); data["rows"][0]["score"]=99
        path.write_text(json.dumps(data),encoding="utf-8")
        with self.assertRaises(ValueError): verify_scores(path)


if __name__=="__main__": unittest.main()
