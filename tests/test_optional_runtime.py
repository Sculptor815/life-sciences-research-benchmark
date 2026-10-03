"""Offline integration checks, enabled when optional dependencies are installed."""
import importlib.util
import json
from pathlib import Path
import sys
import unittest
import uuid

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"src"))


@unittest.skipUnless(importlib.util.find_spec("inspect_ai"), "Inspect AI is not installed")
class InspectIntegrationTests(unittest.TestCase):
    def test_real_inspect_mock_provider_reuses_one_event_loop(self):
        from lsrw.adapters import InspectAdapter
        from lsrw.runner import load_config
        from lsrw.prompts import visible_request
        from lsrw.dataset import load_dataset
        config=load_config(ROOT/"configs/mock.json")
        config["model"]="mockllm/lsrw-offline"
        adapter=InspectAdapter(config)
        try:
            item=load_dataset(ROOT/"data/public/items.jsonl")[0]
            for _ in range(2):
                response=adapter.generate(visible_request(item,ROOT/"data/public"),config)
                self.assertIsInstance(response["text"],str)
                self.assertIsNotNone(response["input_tokens"])
        finally:
            adapter.close()

    def test_native_inspect_task_has_no_keys_targets_or_metadata(self):
        from lsrw.inspect_tasks import public_pilot
        task=public_pilot(str(ROOT/"data/public/items.jsonl"))
        self.assertEqual(len(task.dataset),20)
        for sample in task.dataset:
            self.assertFalse(sample.target)
            self.assertFalse(sample.metadata)


@unittest.skipUnless(importlib.util.find_spec("streamlit"), "Streamlit is not installed")
class StreamlitIntegrationTests(unittest.TestCase):
    def test_blinded_form_renders_without_exceptions(self):
        from streamlit.testing.v1 import AppTest
        from lsrw.dataset import load_dataset
        from lsrw.storage import write_new
        from lsrw.taxonomy import DIMENSIONS
        work=ROOT/".test-work"/uuid.uuid4().hex
        item=next(i for i in load_dataset(ROOT/"data/public/items.jsonl") if i["ability"]=="experimental_design")
        queue={"reviewer":"test-only", "items":[{"blind_id":"test-blind-id", "question":item,"answer":"Synthetic test answer.","asset_root":str(ROOT/"data/public"),
                "rubric":{"dimensions":{d:{"anchors":{str(n):"Test anchor" for n in range(5)}} for d in DIMENSIONS[item["ability"]]}}}]}
        write_new(work/"queue.json",queue)
        script="import sys\nsys.argv=['review', "+repr(str(work/"queue.json"))+"]\nfrom lsrw.review_app import main\nmain()\n"
        app=AppTest.from_string(script).run()
        self.assertFalse(app.exception)
        self.assertEqual(len(app.selectbox),12)


if __name__=="__main__": unittest.main()
