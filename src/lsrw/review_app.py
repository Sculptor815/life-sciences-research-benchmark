"""Launch only through lsrw review; the UI receives a single blinded queue."""
import sys
from pathlib import Path

import streamlit as st

from lsrw.review import save_rating
from lsrw.storage import read_json, within
from lsrw.taxonomy import FOLLOWUP_FIELDS
from lsrw.service import DIMENSIONS as SERVICE_DIMENSIONS


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
        st.subheader("The researcher's goal")
        st.write(item["rubric"].get("user_goal",item["question"]["prompt"]))
        st.subheader("Item-specific scoring rubric")
        for name, dim in item["rubric"]["dimensions"].items():
            with st.expander(name):
                st.json(dim)
        with st.expander("Reference answer and sources"):
            st.markdown(item["rubric"].get("reference_answer","Reference answer unavailable"))
            st.json(item["rubric"].get("references",[]))
        with st.expander("User-service criteria and anchors"):
            st.json({k:item["rubric"].get(k) for k in ("service_criteria","service_anchors","limitations","followup_target")})
        with st.expander("Concept matches to verify in context (not automatic scores)"):
            st.json(item.get("concept_screening", {}))
        with st.form("rating-"+item["blind_id"]):
            st.caption("Primary score: how reliably this answer helps the user make progress. Technical task scores are supporting diagnostics.")
            user_service={name:st.selectbox("User service: "+name.replace('_',' '),[None,0,1,2,3,4],key=item["blind_id"]+'service-'+name) for name in SERVICE_DIMENSIONS}
            scores = {name:st.selectbox(name.replace('_',' '), [None, 0, 1, 2, 3, 4], key=item["blind_id"]+name) for name in item["rubric"]["dimensions"]}
            refusal = st.selectbox("Is this an irrelevant refusal?", [None, False, True])
            paper = item["question"]["ability"] == "essay" and "source_state" in item["rubric"]
            source_correct = st.selectbox("Is the source judgment correct?", [None, False, True]) if paper else None
            conclusion_correct = st.selectbox("Is the judgment of evidential support for the conclusion correct?", [None, False, True]) if paper else None
            followup = {field:st.selectbox("Follow-up match: "+field, [None, False, True], key=item["blind_id"]+field) for field in FOLLOWUP_FIELDS} if item["question"]["ability"] == "research_reasoning" else None
            rationale = st.text_area("Scoring rationale: cite the response and the corresponding rubric criteria")
            if st.form_submit_button("Submit independent rating"):
                try:
                    save_rating(queue_path, item["blind_id"], {"reviewer":queue["reviewer"], "scores":scores,
                                "rationale":rationale, "source_correct":source_correct, "conclusion_correct":conclusion_correct, "refusal":refusal,"followup_match":followup,"user_service":user_service})
                    st.rerun()
                except (ValueError, FileExistsError) as exc:
                    st.error(str(exc))


if __name__ == "__main__":
    main()
