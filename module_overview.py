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


def create_progress_visual(module_path, current_article, quiz_passed):
    
    # Count all article files (assuming they start with "article_")
    articles = sorted(
        [f for f in os.listdir(module_path) if f.startswith("article_")],
        key=lambda x: int(x.split("_")[1].split(".")[0]),
    )
    total_articles = len(articles)
    progress_percentage = ((current_article - 1 + (1 if quiz_passed else 0)) / (total_articles + 1)) * 100
    st.progress((progress_percentage/100), text=f"{progress_percentage}% completed")
    


def render_module_overview(module_number):
    module_path = os.path.join("modules", f"module_{module_number}")
    metadata_file = os.path.join(module_path, "module.json")
    if not os.path.exists(metadata_file):
        st.error("Module not found!")
        return

    try:
        with open(metadata_file, "r") as f:
            module_data = json.load(f)
    except Exception as e:
        st.error(f"Error loading module: {e}")
        return

    # Display module title and learning objectives
    st.title(module_data.get("module_name", f"Module {module_number}"))
    st.subheader("Learning Objectives")
    for obj in module_data.get("learning_objectives", []):
        st.write(f"- {obj}")

    # Retrieve progress data
    progress = module_data.get("progress", {})
    current_article = progress.get("current_article", 1)
    quiz_passed = progress.get("quiz_passed", False)

    # Display visual progress for articles and quiz (bigger and centered)
    st.markdown("### Progress")
    progress_visual = create_progress_visual(module_path, current_article, quiz_passed)
    
 

    # Determine how many articles exist in this module
    articles = [f for f in os.listdir(module_path) if f.startswith("article_")]
    total_articles = len(articles)

    st.markdown("---")

    # Navigation buttons: Direct the user to the correct page based on progress.
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Start/Resume Module", key=f"start_resume_{module_number}"):
            if current_article <= total_articles:
                set_page(
                    "article",
                    module_number=module_number,
                    article_index=current_article,
                )
            else:
                set_page("quiz", module_number=module_number)
    with col2:
        if st.button("Restart Module", key=f"restart_{module_number}"):
            set_page("article", module_number=module_number, article_index=1)
            
