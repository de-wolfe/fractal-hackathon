import streamlit as st
import writer
import test_gpt_call
import random
import numpy as np
import matplotlib.pyplot as plt

    

# Streamlit UI setup
st.title("Interactive Quiz App")
subject = st.text_input("What do you want to learn about?")
crazy_level = st.slider("Crazy Level")
if st.button("Click me"):
    test_gpt_call.ask_openai_teaching(subject, crazy_level)

import streamlit as st
import os
import json
from pathlib import Path
from module_generator import ModuleGenerator


# Helper functions for query param routing
def set_page(page, module_number=None, article_index=None):
    params = {"page": page}
    if module_number is not None:
        params["module"] = module_number
    if article_index is not None:
        params["article_index"] = article_index
    st.experimental_set_query_params(**params)


def get_current_page():
    params = st.experimental_get_query_params()
    page = params.get("page", ["home"])[0]
    module_number = int(params.get("module", [0])[0]) if "module" in params else None
    article_index = (
        int(params.get("article_index", [1])[0]) if "article_index" in params else 1
    )
    return page, module_number, article_index


def render_navbar():
    """Render a top navigation bar with a home icon that links back to the home page."""
    st.markdown(
        """
         <style>
         .navbar {
             background-color: #0e1117;  /* Dark background to match the rest of the page */
             padding: 10px;
             display: flex;
             align-items: center;
         }
         .navbar a {
             text-decoration: none;
             color: #FFFFFF; /* White text for visibility */
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
                    metadata_path = os.path.join(self.modules_dir, d, "module.py")
                    if os.path.exists(metadata_path):
                        with open(metadata_path, "r") as f:
                            module_data = json.loads(f.read())
                        modules.append((module_number, module_data))
                except Exception as e:
                    st.error(f"Error reading {d}: {e}")
        modules.sort(key=lambda x: x[0])
        return modules

    def generate_new_module(self, topic):
        """Generate a new module by incrementing from the last module number."""
        modules = self.get_all_modules()
        new_module_number = modules[-1][0] + 1 if modules else 1
        generator = ModuleGenerator(topic, new_module_number)
        generator.create_module_structure()
        generator.generate_content()

st.title("Introduction to Basic Thermodynamics")

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

        # Input for a new module
        topic = st.text_input("Enter a topic for a new module:")
        if st.button("Generate New Module"):
            if topic.strip():
                app.generate_new_module(topic.strip())
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
                        st.rerun()
        else:
            st.info("No modules available yet. Create one above!")

    elif current_page == "module":
        if module_number is None:
            st.error("No module specified.")
            return
        module_path = os.path.join("modules", f"module_{module_number}")
        metadata_file = os.path.join(module_path, "module.py")
        if not os.path.exists(metadata_file):
            st.error("Module not found!")
            return
        try:
            with open(metadata_file, "r") as f:
                module_data = json.loads(f.read())
            st.title(module_data.get("module_name", f"Module {module_number}"))
            st.write("Learning Objectives:")
            for objective in module_data.get("learning_objectives", []):
                st.write(f"- {objective}")
        except Exception as e:
            st.error(f"Error loading module: {e}")
            return

        st.write("## Navigation")
        if st.button("View Articles"):
            set_page("article", module_number=module_number, article_index=1)
            st.rerun()

    elif current_page == "article":
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

        # Create three columns for navigation
        col_prev, col_center, col_next = st.columns([1, 2, 1])

        # Show "Previous Article" button only if not on the first article
        if article_index > 1:
            with col_prev:
                if st.button("Previous Article"):
                    set_page(
                        "article",
                        module_number=module_number,
                        article_index=article_index - 1,
                    )
                    st.rerun()
        else:
            col_prev.empty()

        # Display the article progress in the center column
        with col_center:
            st.markdown(
                f"<div style='text-align: center;'>Article {article_index} of {total_articles}</div>",
                unsafe_allow_html=True,
            )

        # If it's the last article, change the button to "Take Quiz"
        with col_next:
            if article_index < total_articles:
                if st.button("Next Article"):
                    set_page(
                        "article",
                        module_number=module_number,
                        article_index=article_index + 1,
                    )
                    st.rerun()
            else:
                if st.button("Take Quiz"):
                    set_page("quiz", module_number=module_number)
                    st.rerun()
    elif current_page == "quiz":
        if module_number is None:
            st.error("No module specified for the quiz.")
            return
        module_path = os.path.join("modules", f"module_{module_number}")
        quiz_file = os.path.join(module_path, "quiz.py")
        if not os.path.exists(quiz_file):
            st.error("Quiz not found!")
            return
        with open(quiz_file, "r") as f:
            quiz_content = f.read()
            exec(quiz_content, globals())
        if st.button("Back to Module Overview"):
            set_page("module", module_number=module_number)
            st.rerun()
    else:
        st.error("Page not found!")

if __name__ == "__main__":
    main()
