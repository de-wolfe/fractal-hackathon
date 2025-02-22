import streamlit as st
import test_gpt_call

import os
import json
from pathlib import Path
from module_generator import ModuleGenerator
from module_overview import render_module_overview
from quiz_module import render_quiz_module
from article_module import render_article_module


# Helper functions for query param routing
def set_page(page, module_number=None, article_index=None):
    params = {"page": page}
    if module_number is not None:
        params["module"] = module_number
    if article_index is not None:
        params["article_index"] = article_index
    st.query_params.update(params)
    st.rerun()  # Using st.rerun() instead of experimental_rerun()


def get_current_page():
    params = st.query_params  # Use the new format
    
    page = params.get("page", "home")
    module_number = int(params.get("module", [0])[0]) if "module" in params else None
    article_index = (
        int(params.get("article_index", [1])[0]) if "article_index" in params else 1
    )
    return page, module_number, article_index


def update_module_progress(module_number, new_progress):
    """
    Update the module metadata (module.json) to reflect new progress.
    new_progress should be a dict like {"current_article": X, "quiz_passed": Y}
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


def render_navbar():
    """Render a top navigation bar with a home icon that links back to the home page."""
    st.markdown(
        """
         <style>
         .navbar {
             background-color: #FFFFFF;
             padding: 10px;
             display: flex;
             align-items: center;
         }
         .navbar a {
             text-decoration: none;
             color: #FFFFFF;
             font-size: 24px;
             font-weight: bold;
             margin-right: 20px;
         }
         </style>
         <div class="navbar">
             <a href="?page=home" target="_self">🏠</a>
         </div>
         """,
        unsafe_allow_html=True,
    )


class ContentApp:
    def __init__(self):
        self.modules_dir = "modules"
        if not os.path.exists(self.modules_dir):
            os.makedirs(self.modules_dir)

    def get_all_modules(self):
        """Return a sorted list of tuples (module_number, module_data) for all modules."""
        modules = []
        for d in os.listdir(self.modules_dir):
            if d.startswith("module_") and os.path.isdir(
                os.path.join(self.modules_dir, d)
            ):
                try:
                    module_number = int(d.split("_")[1])
                    metadata_path = os.path.join(self.modules_dir, d, "module.json")
                    if os.path.exists(metadata_path):
                        with open(metadata_path, "r") as f:
                            module_data = json.load(f)
                        modules.append((module_number, module_data))
                except Exception as e:
                    st.error(f"Error reading {d}: {e}")
        modules.sort(key=lambda x: x[0])
        return modules

    def generate_new_module(self, topic, learning_style):
        """Generate a new module by incrementing from the last module number."""
        modules = self.get_all_modules()
        new_module_number = modules[-1][0] + 1 if modules else 1
        generator = ModuleGenerator(topic, new_module_number, "claude")
        generator.create_module_structure()
        generator.generate_content(topic, learning_style)


def main():
    st.set_page_config(page_title="Educational Content Generator")
    app = ContentApp()
    current_page, module_number, article_index = get_current_page()

    # Render navbar on every page except home
    if current_page != "home":
        render_navbar()

    if current_page == "home":
        st.title("Educational Content Generator")
        st.write("Create a new module or select one from the list below.")
        # Streamlit UI setup
        topic = st.text_input("What do you want to learn about?")
        learning_style = st.text_input("How do you best learn?")
        crazy_level = st.slider("Crazy Level")
        # Input for a new module
        if st.button("Generate New Module"):
            if topic.strip():
                app.generate_new_module(topic.strip(), learning_style)
                st.success(f"Module on '{topic}' created!")
                st.rerun()
            else:
                st.error("Please enter a valid topic.")

        st.write("## Available Modules")
        modules = app.get_all_modules()
        if modules:
            for mod_num, mod_data in modules:
                with st.container():
                    st.subheader(mod_data.get("module_name", f"Module {mod_num}"))
                    st.write("Learning Objectives:")
                    for obj in mod_data.get("learning_objectives", []):
                        st.write(f"- {obj}")
                    if st.button("View Module", key=f"view_{mod_num}"):
                        set_page("module", module_number=mod_num)
        else:
            st.info("No modules available yet. Create one above!")

    elif current_page == "module":
        if module_number is None:
            st.error("No module specified.")
        else:
            render_module_overview(module_number)
    elif current_page == "article":
        if module_number is None:
            st.error("No module specified.")
        else:
            render_article_module(module_number, article_index)

    elif current_page == "quiz":
        if module_number is None:
            st.error("No module specified.")
        else:
            render_quiz_module(module_number)

    else:
        st.error("Page not found!")


if __name__ == "__main__":
    main()
