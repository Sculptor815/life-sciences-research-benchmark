import argparse
import json
import os
import subprocess
import sys
from pathlib import Path

from .curation import calibration, lock_dataset
from .dataset import load_dataset, validate
from .results import compare, report, score_run
from .review import prepare_review
from .runner import dry_run, execute, load_config
from .storage import read_json, read_jsonl, write_new


def main(argv=None):
    # Inspect's packaged model catalogue contains Unicode. Some releases open
    # it with the process default encoding, which is GBK on Chinese Windows.
    # Start the CLI in Python's supported UTF-8 mode before importing providers.
    if os.name == "nt" and not sys.flags.utf8_mode:
        result = subprocess.run([sys.executable, "-X", "utf8", "-m", "lsrw", *(sys.argv[1:] if argv is None else argv)])
        raise SystemExit(result.returncode)
    parser = argparse.ArgumentParser(prog="lsrw", description="Life Sciences Research Workbench")
    commands = parser.add_subparsers(dest="command", required=True)
    cmd = commands.add_parser("validate")
    cmd.add_argument("--dataset", default="data/public/items.jsonl")
    cmd.add_argument("--formal", action="store_true")
    cmd = commands.add_parser("run")
    cmd.add_argument("--config", required=True)
    cmd.add_argument("--dry-run", action="store_true")
    cmd = commands.add_parser("review")
    cmd.add_argument("--queue", help="Only this reviewer's queue is shown")
    cmd.add_argument("--prepare", action="store_true")
    cmd.add_argument("--run")
    cmd.add_argument("--keys", default=os.environ.get("LSRW_KEYS"))
    cmd.add_argument("--output")
    cmd.add_argument("--reviewers", nargs=2)
    cmd = commands.add_parser("score")
    cmd.add_argument("--run", required=True, help="Absolute path to a completed run directory")
    cmd.add_argument("--keys", default=os.environ.get("LSRW_KEYS"))
    cmd.add_argument("--reviews")
    cmd.add_argument("--adjudications")
    cmd.add_argument("--output")
    cmd = commands.add_parser("report")
    cmd.add_argument("--run", required=True)
    cmd.add_argument("--scores")
    cmd.add_argument("--output", required=True)
    cmd = commands.add_parser("compare")
    cmd.add_argument("--left", required=True)
    cmd.add_argument("--right", required=True)
    cmd = commands.add_parser("calibrate")
    cmd.add_argument("--records", required=True)
    cmd.add_argument("--output", required=True)
    cmd = commands.add_parser("lock")
    for flag in ("dataset", "keys", "approvals", "calibration", "output"):
        cmd.add_argument("--"+flag, required=True)
    cmd = commands.add_parser("research", help="Private discovery corpus and human candidate review")
    cmd.add_argument("action", choices=("audit", "review", "export", "import-decisions"))
    cmd.add_argument("--corpus", required=True)
    cmd.add_argument("--output")
    cmd.add_argument("--decisions")
    cmd = commands.add_parser("question-quality", help="Summarize six-dimension research-question ratings")
    cmd.add_argument("--record", required=True)
    cmd.add_argument("--output")
    args = parser.parse_args(argv)
    try:
        if args.command == "question-quality":
            from .question_quality import summarize
            result=summarize(read_json(args.record))
            if args.output:
                write_new(args.output,result)
            print(json.dumps(result,ensure_ascii=False,indent=2))
        elif args.command == "research":
            from .discovery import audit, export_drafts, import_decisions, render_review
            corpus = read_json(args.corpus)
            if args.action == "audit":
                result = audit(corpus)
                if args.output:
                    write_new(args.output, result)
                print(json.dumps(result, ensure_ascii=False, indent=2))
                if not result["valid"]:
                    raise SystemExit(1)
            else:
                if not args.output:
                    raise ValueError("Research action requires --output")
                if args.action == "review":
                    print(render_review(corpus, args.output))
                elif args.action == "export":
                    print(json.dumps(export_drafts(corpus,args.output), ensure_ascii=False))
                else:
                    if not args.decisions:
                        raise ValueError("Provide a human-exported --decisions file")
                    print(json.dumps(import_decisions(corpus,read_json(args.decisions),args.output),ensure_ascii=False))
        elif args.command == "validate":
            items = read_jsonl(args.dataset)
            errors = validate(items, Path(args.dataset).resolve().parent, args.formal)
            print(json.dumps({"valid":not errors,"items":len(items),"formal":args.formal,"errors":errors}, indent=2))
            if errors:
                raise SystemExit(1)
        elif args.command == "run":
            config = load_config(args.config)
            print(json.dumps(dry_run(config), indent=2))
            if not args.dry_run:
                print(execute(config))
        elif args.command == "review":
            if args.prepare:
                if not all((args.run, args.keys, args.output, args.reviewers)):
                    raise ValueError("Review preparation requires --run, --keys, --output and --reviewers")
                print(prepare_review(args.run, args.keys, args.output, args.reviewers))
            else:
                if not args.queue:
                    raise ValueError("Use --queue PATH to open an assigned blind review queue")
                result = subprocess.run([sys.executable,"-X","utf8","-m","streamlit","run",str(Path(__file__).with_name("review_app.py")),"--server.address","127.0.0.1","--",str(Path(args.queue).resolve())])
                raise SystemExit(result.returncode)
        elif args.command == "score":
            if not args.keys:
                raise ValueError("Provide an external --keys file or LSRW_KEYS")
            print(score_run(args.run, args.keys, args.reviews, args.adjudications, args.output))
        elif args.command == "report":
            choices = list((Path(args.run)/"scores").glob("*.json"))
            path = args.scores or (str(choices[0]) if len(choices)==1 else None)
            if not path:
                raise ValueError("Choose an explicit --scores artifact when zero or multiple versions exist")
            if read_json(path)["run_id"] != read_json(Path(args.run)/"manifest.json")["run_id"]:
                raise ValueError("Scores belong to a different run")
            print(report(path, args.output))
        elif args.command == "compare":
            print(json.dumps(compare(args.left, args.right), indent=2))
        elif args.command == "calibrate":
            result = calibration(read_json(args.records))
            write_new(args.output, result)
            print(json.dumps(result, indent=2))
        elif args.command == "lock":
            print(json.dumps(lock_dataset(args.dataset, args.keys, args.approvals, args.calibration, args.output), indent=2))
    except (ValueError, OSError, KeyError, ImportError) as exc:
        parser.exit(2, f"lsrw: {exc}\n")
