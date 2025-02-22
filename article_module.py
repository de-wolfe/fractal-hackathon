import os
import json
import streamlit as st

import anthropic


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

    # Flag to indicate if the article failed to load
    article_failed = False
    original_content = ""

    # Try to load and execute the article
    if not os.path.exists(article_file):
        st.error("Article not found!")
        article_failed = True
    else:
        try:
            with open(article_file, "r") as f:
                article_content = f.read()
            original_content = article_content  # Save for turbocharge use
            try:
                exec(article_content, globals())
            except Exception as e:
                st.error(f"Error executing article content: {e}")
                article_failed = True
        except Exception as e:
            st.error(f"Error reading article file: {e}")
            article_failed = True

    # Continue with loading module metadata and progress regardless of article loading
    total_articles = len(
        [f for f in os.listdir(module_path) if f.startswith("article_")]
    )
    metadata_file = os.path.join(module_path, "module.json")
    try:
        with open(metadata_file, "r") as f:
            module_data = json.load(f)
        current_progress = module_data.get("progress", {}).get("current_article", 1)
    except Exception as e:
        st.error(f"Error reading module progress: {e}")
        current_progress = 1

    # Update progress if the user has reached a new article
    if article_index > current_progress:
        new_progress = {
            "current_article": article_index,
            "quiz_passed": module_data.get("progress", {}).get("quiz_passed", False),
        }
        update_module_progress(module_number, new_progress)

    # Layout for navigation buttons
    col_prev, col_center, col_next = st.columns([1, 2, 1])

    # Previous Article button
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

    # Center: Article progress info
    with col_center:
        st.markdown(
            f"<div style='text-align: center;'>Article {article_index} of {total_articles}</div>",
            unsafe_allow_html=True,
        )

    # Next Article or Take Quiz button
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

    # --- Turbocharge Section ---
    # st.markdown("---")
    #
    # if st.button("Turbocharge Article"):
    #     purpose = "Improve visual design, rewrite the code to fix any issues, and make the article more engaging. (Turbocharge it)"
    #     turbocharged_content = turbocharge_article(original_content, purpose)
    #     print(turbocharged_content)
    #
    #     try:
    #         exec(turbocharged_content, globals())
    #         st.success("Article successfully turbocharged!")
    #     except Exception as e:
    #         st.error(f"Error executing turbocharged code: {e}")


claude_key = st.secrets["CLAUDE_KEY"]
claude_client = anthropic.Anthropic(api_key=claude_key)


def turbocharge_article(original_content, purpose):
    """
    Turbocharge the given article code using a two-stage process:

    1. Extraction Stage:
       - Analyze the original code and break it into key sections (e.g., imports,
         helper functions, main logic, navigation, etc.).
       - Return the breakdown as a JSON object.

    2. Rewrite Stage:
       - Use the extracted sections to rewrite the entire code into a crazy complex,
         interactive, and visually engaging Streamlit application.
       - Ensure that all necessary imports are included at the top and that only the
         approved packages are used.

    Parameters:
        original_content (str): The original article code.
        purpose (str): The goal for turbocharging the code.

    Returns:
        str: The completely rewritten and turbocharged Streamlit code.
    """
    # Stage 1: Extract Sections from the Original Code
    extraction_prompt = f"""As an expert in Streamlit development, please analyze the following article code and break it down into its key sections. 
Divide the code into sections such as:
- Imports
- Helper functions
- Main rendering logic
- Navigation controls
- Turbocharge section
- Any other significant sections.

Return the result as a JSON object with keys representing each section (e.g. "imports", "helper_functions", "main_logic", "navigation", "turbocharge").
Here is the original code:
{original_content}
"""
    extraction_response = claude_client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=2000,
        messages=[{"role": "user", "content": extraction_prompt}],
    )
    # Extract the text from the response
    if hasattr(extraction_response.content, "text"):
        extraction_text = extraction_response.content.text
    elif (
        isinstance(extraction_response.content, list)
        and len(extraction_response.content) > 0
    ):
        extraction_text = extraction_response.content[0].text
    else:
        extraction_text = str(extraction_response.content)

    # Attempt to parse the JSON from the extraction
    try:
        import json

        sections_json = json.loads(extraction_text)
    except Exception as e:
        # If parsing fails, fall back to a simple key
        sections_json = {"extracted_sections": extraction_text}

    # Stage 2: Rewrite the Code Using the Extracted Sections
    rewrite_prompt = f"""Using the following JSON object that contains sections of a Streamlit article code, rewrite and turbocharge the entire code to be more complex, interactive, and visually engaging.
Combine the sections appropriately, fix any syntax errors, and include all necessary imports at the top.
Only use packages from our approved list: streamlit, altair, bokeh, matplotlib, plotly, pydeck, seaborn, pandas, numpy, pillow, rich, py3Dmol, stmol, webcolors.

DO NOT INCLUDE THIS: st.set_page_config()
1. Fix any potential issues or bugs.
2. Make the display more visually appealing and interactive.
3. Remove any st.set_page_config calls.
4. Keep the core teaching content but make it more engaging.
5. Ensure that all necessary imports are included at the top of the code. In particular, if the code uses functions or modules like colorsys or numpy (as np), include "import colorsys" or "import numpy as np" respectively.
6. Only use packages from our approved package list: streamlit, altair, bokeh, matplotlib, plotly, pydeck, seaborn, pandas, numpy, pillow, rich, py3Dmol, stmol, webcolors.
7. Maintain any essential existing imports.

include your thoughts in a <thinking> tag 

Return the completely rewritten code between <code> and </code> tags.

Sections JSON:
{json.dumps(sections_json, indent=2)}

Purpose: {purpose}
"""
    rewrite_response = claude_client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=5000,
        messages=[{"role": "user", "content": rewrite_prompt}],
    )
    # Extract text from the rewrite response
    if hasattr(rewrite_response.content, "text"):
        rewrite_text = rewrite_response.content.text
    elif (
        isinstance(rewrite_response.content, list) and len(rewrite_response.content) > 0
    ):
        rewrite_text = rewrite_response.content[0].text
    else:
        rewrite_text = str(rewrite_response.content)

    # Extract the code between <code> and </code> tags
    import re

    code_match = re.search(r"<code>(.*?)</code>", rewrite_text, re.DOTALL)
    if code_match:
        turbocharged_content = code_match.group(1).strip()
    else:
        turbocharged_content = rewrite_text.strip()

    return turbocharged_content
