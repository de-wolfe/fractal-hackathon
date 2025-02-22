import os
import json
import streamlit as st


def set_page(page, module_number=None, article_index=None):
    params = {"page": page}
    if module_number is not None:
        params["module"] = module_number
    if article_index is not None:
        params["article_index"] = article_index
    st.query_params.update(params)
    st.rerun()


def update_module_progress(module_number, new_progress):
    """
    Update the module metadata file (module.json) for the given module_number
    with the new progress data.
    """
    module_path = os.path.join("modules", f"module_{module_number}")
    metadata_file = os.path.join(module_path, "module.json")
    if not os.path.exists(metadata_file):
        st.error("Module metadata file not found!")
        return
    try:
        with open(metadata_file, "r") as f:
            module_data = json.load(f)
        module_data["progress"] = new_progress
        with open(metadata_file, "w") as f:
            json.dump(module_data, f, indent=2)
    except Exception as e:
        st.error(f"Error updating module progress: {e}")


def render_article_module(module_number, article_index):
    if module_number is None:
        st.error("No module specified for the article.")
        return

    module_path = os.path.join("modules", f"module_{module_number}")
    article_file = os.path.join(module_path, f"article_{article_index}.py")
    if not os.path.exists(article_file):
        st.error("Article not found!")
        return

    # Load and execute the article content
    with open(article_file, "r") as f:
        article_content = f.read()
        exec(article_content, globals())

    # Determine the total number of articles for this module
    total_articles = len(
        [f for f in os.listdir(module_path) if f.startswith("article_")]
    )

    # Load current metadata to check progress
    metadata_file = os.path.join(module_path, "module.json")
    try:
        with open(metadata_file, "r") as f:
            module_data = json.load(f)
        current_progress = module_data.get("progress", {}).get("current_article", 1)
    except Exception as e:
        st.error(f"Error reading module progress: {e}")
        current_progress = 1

    # If the user has reached a new article (or quiz), update the metadata
    if article_index > current_progress:
        new_progress = {
            "current_article": article_index,
            "quiz_passed": module_data.get("progress", {}).get("quiz_passed", False),
        }
        update_module_progress(module_number, new_progress)

    # Navigation buttons
    col_prev, col_center, col_next = st.columns([1, 2, 1])

    # Previous Article button: only show if not on the first article.
    if article_index > 1:
        with col_prev:
            if st.button("Previous Article"):
                new_article_index = article_index - 1
                update_module_progress(
                    module_number,
                    {
                        "current_article": new_article_index,
                        "quiz_passed": module_data.get("progress", {}).get(
                            "quiz_passed", False
                        ),
                    },
                )
                set_page(
                    "article",
                    module_number=module_number,
                    article_index=new_article_index,
                )
    else:
        col_prev.empty()

    # Center: Display article progress information.
    with col_center:
        st.markdown(
            f"<div style='text-align: center;'>Article {article_index} of {total_articles}</div>",
            unsafe_allow_html=True,
        )

    # Next Article or Take Quiz button: if we're not on the last article, show Next; otherwise, show Take Quiz.
    with col_next:
        if article_index < total_articles:
            if st.button("Next Article"):
                new_article_index = article_index + 1
                update_module_progress(
                    module_number,
                    {
                        "current_article": new_article_index,
                        "quiz_passed": module_data.get("progress", {}).get(
                            "quiz_passed", False
                        ),
                    },
                )
                set_page(
                    "article",
                    module_number=module_number,
                    article_index=new_article_index,
                )
        else:
            if st.button("Take Quiz"):
                # Set progress to indicate quiz stage (current_article > total_articles)
                update_module_progress(
                    module_number,
                    {
                        "current_article": total_articles + 1,
                        "quiz_passed": module_data.get("progress", {}).get(
                            "quiz_passed", False
                        ),
                    },
                )
                set_page("quiz", module_number=module_number)
