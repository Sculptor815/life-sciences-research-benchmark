"""Launch only through lsrw review; the UI receives a single blinded queue."""
import sys
from pathlib import Path

import streamlit as st

from lsrw.review import save_rating
from lsrw.storage import read_json, within


def main():
    st.set_page_config(page_title="Life Sciences Review", layout="wide")
    st.title("生命科学评测 · 独立评分")
    st.caption("依据题目证据和专属细则评分。完成后提交；提交记录保留，复核由协调人处理。")
    queue_path = Path(sys.argv[1]).resolve()
    queue = read_json(queue_path)
    pending = [i for i in queue["items"] if not (queue_path.parent/"ratings"/(i["blind_id"]+".json")).exists()]
    st.write(f"已完成 {len(queue['items'])-len(pending)} / {len(queue['items'])}")
    if not pending:
        st.success("本次分配的题目已评完。")
        return
    selected = st.selectbox("选择待评回答", range(len(pending)), format_func=lambda i:pending[i]["blind_id"][:10])
    item = pending[selected]
    left, right = st.columns([3, 2])
    with left:
        st.subheader("题目与固定材料")
        st.write(item["question"]["prompt"])
        st.text(item["question"]["packet"])
        for asset in item["question"]["materials"]:
            st.image(str(within(item["asset_root"], asset["path"])))
        st.subheader("待评回答")
        st.text(item["answer"])
    with right:
        st.subheader("专属评分细则")
        for name, dim in item["rubric"]["dimensions"].items():
            with st.expander(name):
                st.json(dim)
        with st.expander("参考答案与来源"):
            st.json({k:v for k,v in item["rubric"].items() if k != "dimensions"})
        with st.form("rating-"+item["blind_id"]):
            scores = {name:st.selectbox(name, [None, 0, 1, 2, 3, 4], key=item["blind_id"]+name) for name in item["rubric"]["dimensions"]}
            refusal = st.selectbox("是否属于无关拒答？", [None, False, True])
            paper = item["question"]["ability"] == "paper_appraisal"
            source_correct = st.selectbox("来源判断是否正确？", [None, False, True]) if paper else None
            conclusion_correct = st.selectbox("结论支持程度判断是否正确？", [None, False, True]) if paper else None
            rationale = st.text_area("评分依据：引用回答内容和对应细则")
            if st.form_submit_button("提交独立评分"):
                try:
                    save_rating(queue_path, item["blind_id"], {"reviewer":queue["reviewer"], "scores":scores,
                                "rationale":rationale, "source_correct":source_correct, "conclusion_correct":conclusion_correct, "refusal":refusal})
                    st.rerun()
                except (ValueError, FileExistsError) as exc:
                    st.error(str(exc))


if __name__ == "__main__":
    main()
