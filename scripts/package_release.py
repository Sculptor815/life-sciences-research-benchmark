"""Build a deterministic public archive from a reviewed explicit file inventory."""
import argparse
import hashlib
import json
from pathlib import Path
import zipfile


def package(root, manifest, output):
    root=Path(root).resolve()
    lines=[line.strip() for line in Path(manifest).read_text(encoding="utf-8").splitlines() if line.strip() and not line.startswith("#")]
    if len(lines)!=len(set(lines)):
        raise ValueError("Duplicate release paths")
    files={}
    forbidden={"private","runs","reviews","reports",".git",".venv",".test-work","__pycache__"}
    for relative in lines:
        path=(root/relative).resolve()
        if not path.is_relative_to(root) or not path.is_file() or any(part in forbidden for part in Path(relative).parts) or path.name.startswith(".env"):
            raise ValueError("Disallowed release path: "+relative)
        if path.name.endswith("keys.json") or path.name in {"coordinator-only.json","adjudications.json"}:
            raise ValueError("Private grading material is not publishable")
        if path.suffix==".jsonl":
            for line in path.read_text(encoding="utf-8").splitlines():
                if not line.strip(): continue
                item=json.loads(line)
                if item.get("split")!="public" or {"answer","rubric","dimensions","anchor_answers"}&set(item):
                    raise ValueError("Held-out items or answer fields in public dataset")
        files[relative]=path.read_bytes()
    inventory={name:hashlib.sha256(content).hexdigest() for name,content in sorted(files.items())}
    files["SHA256SUMS.json"]=(json.dumps(inventory,indent=2)+"\n").encode("utf-8")
    with zipfile.ZipFile(output,"x",compression=zipfile.ZIP_DEFLATED) as archive:
        for relative,content in sorted(files.items()):
            info=zipfile.ZipInfo(relative,date_time=(2026,1,1,0,0,0))
            info.compress_type=zipfile.ZIP_DEFLATED
            info.external_attr=0o100644<<16
            archive.writestr(info,content)
    return inventory


if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--manifest",required=True)
    parser.add_argument("--output",required=True)
    args=parser.parse_args()
    root=Path(__file__).resolve().parents[1]
    inventory=package(root,args.manifest,args.output)
    print(json.dumps({"files":len(inventory),"archive":str(Path(args.output).resolve())}))
