"""Launch only through lsrw review; the UI receives a single blinded queue."""
import sys
from pathlib import Path

import streamlit as st

from lsrw.review import save_rating
from lsrw.storage import read_json, within


def main():
    st.set_page_config(page_title="Life Sciences Review", layout="wide")
    st.title("Life Sciences Evaluation · Independent Scoring")
    st.caption("Score using the supplied evidence and item-specific rubric. Submit when complete; submissions are retained, and the coordinator handles adjudication.")
    queue_path = Path(sys.argv[1]).resolve()
    queue = read_json(queue_path)
    pending = [i for i in queue["items"] if not (queue_path.parent/"ratings"/(i["blind_id"]+".json")).exists()]
    st.write(f"Completed {len(queue['items'])-len(pending)} / {len(queue['items'])}")
    if not pending:
        st.success("All assigned responses have been scored.")
        return
    selected = st.selectbox("Select a response to score", range(len(pending)), format_func=lambda i:pending[i]["blind_id"][:10])
    item = pending[selected]
    left, right = st.columns([3, 2])
    with left:
        st.subheader("Question and fixed evidence packet")
        st.write(item["question"]["prompt"])
        st.text(item["question"]["packet"])
        for asset in item["question"]["materials"]:
            st.image(str(within(item["asset_root"], asset["path"])))
        st.subheader("Response to score")
        st.text(item["answer"])
    with right:
        st.subheader("Item-specific scoring rubric")
        for name, dim in item["rubric"]["dimensions"].items():
            with st.expander(name):
                st.json(dim)
        with st.expander("Reference answer and sources"):
            st.json({k:v for k,v in item["rubric"].items() if k != "dimensions"})
        with st.form("rating-"+item["blind_id"]):
            scores = {name:st.selectbox(name, [None, 0, 1, 2, 3, 4], key=item["blind_id"]+name) for name in item["rubric"]["dimensions"]}
            refusal = st.selectbox("Is this an irrelevant refusal?", [None, False, True])
            paper = item["question"]["ability"] == "paper_appraisal"
            source_correct = st.selectbox("Is the source judgment correct?", [None, False, True]) if paper else None
            conclusion_correct = st.selectbox("Is the judgment of evidential support for the conclusion correct?", [None, False, True]) if paper else None
            rationale = st.text_area("Scoring rationale: cite the response and the corresponding rubric criteria")
            if st.form_submit_button("Submit independent rating"):
                try:
                    save_rating(queue_path, item["blind_id"], {"reviewer":queue["reviewer"], "scores":scores,
                                "rationale":rationale, "source_correct":source_correct, "conclusion_correct":conclusion_correct, "refusal":refusal})
                    st.rerun()
                except (ValueError, FileExistsError) as exc:
                    st.error(str(exc))


if __name__ == "__main__":
    main()
