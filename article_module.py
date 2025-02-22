import os
import json
import streamlit as st
from module_generator import enhance_with_claude
import anthropic


def set_page(page, module_number=None, article_index=None):
    params = {"page": page}
    if module_number is not None:
        params["module"] = module_number
    if article_index is not None:
        params["article_index"] = article_index
    st.experimental_set_query_params(**params)
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
    st.markdown("---")

    if st.button("Turbocharge Article"):
        purpose = "Improve visual design, rewrite the code to fix any issues, and make the article more engaging. (Turbocharge it)"
        turbocharged_content = turbocharge_article(original_content, purpose)
        print(turbocharged_content)

        try:
            exec(turbocharged_content, globals())
            st.success("Article successfully turbocharged!")
        except Exception as e:
            st.error(f"Error executing turbocharged code: {e}")


claude_key = st.secrets["CLAUDE_KEY"]
claude_client = anthropic.Anthropic(api_key=claude_key)


def turbocharge_article(original_content, purpose):
    """
    Completely rewrites the given article code using Claude to fix syntax errors,
    improve readability, and add interactivity.

    The new code will include all necessary imports at the top and only use packages
    from the approved list: streamlit, altair, bokeh, matplotlib, plotly, pydeck,
    seaborn, pandas, numpy, pillow, rich, py3Dmol, stmol, webcolors.

    Parameters:
        original_content (str): The original article code.
        purpose (str): The goal for rewriting the code.

    Returns:
        str: The completely rewritten Streamlit code.
    """
    prompt = f"""As an expert in Streamlit development, completely rewrite the following article code from scratch. 
Your task is to fix any syntax errors, improve readability, and add interactivity.
Make sure the code includes all necessary imports at the top.
Only use packages from our approved list: streamlit, altair, bokeh, matplotlib, plotly, pydeck, seaborn, pandas, numpy, pillow, rich, py3Dmol, stmol, webcolors.

Here is the original code:
{original_content}

Purpose: {purpose}

Return the completely rewritten code between <code> and </code> tags."""

    response = claude_client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=5000,
        messages=[{"role": "user", "content": prompt}],
    )

    # Extract the text content from Claude's response
    if hasattr(response.content, "text"):
        response_text = response.content.text
    elif isinstance(response.content, list) and len(response.content) > 0:
        response_text = response.content[0].text
    else:
        response_text = str(response.content)

    # Extract code from between <code> and </code> tags
    import re

    code_match = re.search(r"<code>(.*?)</code>", response_text, re.DOTALL)
    if code_match:
        rewritten_content = code_match.group(1).strip()
    else:
        rewritten_content = response_text.strip()

    return rewritten_content
