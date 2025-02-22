import os
import streamlit as st


def set_page(page, module_number=None, article_index=None):
    params = {"page": page}
    if module_number is not None:
        params["module"] = module_number
    if article_index is not None:
        params["article_index"] = article_index
    st.query_params.update(params)
    st.rerun()


def render_quiz_module(module_number):
    module_path = os.path.join("modules", f"module_{module_number}")
    quiz_file = os.path.join(module_path, "quiz.py")

    if not os.path.exists(quiz_file):
        st.error("Quiz not found!")
        return

    # Load and execute the quiz content
    with open(quiz_file, "r") as f:
        quiz_content = f.read()
        exec(quiz_content, globals())

    st.markdown("---")
    # Determine the total number of articles for this module
    articles = sorted(
        [f for f in os.listdir(module_path) if f.startswith("article_")],
        key=lambda x: int(x.split("_")[1].split(".")[0]),
    )
    total_articles = len(articles)

    # Navigation buttons
    col_prev, col_overview = st.columns(2)
    with col_prev:
        if st.button("Previous Article"):
            # Navigate back to the last article
            set_page(
                "article", module_number=module_number, article_index=total_articles
            )
    with col_overview:
        if st.button("Back to Module Overview"):
            set_page("module", module_number=module_number)
