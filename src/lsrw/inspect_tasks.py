"""Optional Inspect task integration for local mock development.

Formal paid runs use `lsrw run`, which adds reservation accounting and locked
dataset checks around Inspect's model API. Direct `inspect eval` is exploratory.
"""
from inspect_ai import Task, task
from inspect_ai.dataset import MemoryDataset, Sample
from inspect_ai.model import ChatMessageSystem, ChatMessageUser
from inspect_ai.solver import generate
from inspect_ai.model import ContentImage, ContentText

from pathlib import Path
from .dataset import load_dataset
from .prompts import visible_request


@task
def public_pilot(dataset: str):
    samples = []
    for item in load_dataset(dataset):
        if item["split"] != "public":
            continue
        request = visible_request(item, Path(dataset).parent)
        content = [ContentText(text=request["text"])] + [ContentImage(image=i) for i in request["images"]]
        samples.append(Sample(id=item["id"], input=[ChatMessageSystem(content=request["system"]), ChatMessageUser(content=content)], target="", metadata={}))
    return Task(dataset=MemoryDataset(samples), solver=generate(), scorer=None, epochs=1, name="lsrw_public_pilot")
