import os
import json
from pathlib import Path
import concurrent.futures
from openai import OpenAI
import anthropic
import streamlit as st

openai_key = st.secrets["OPENAI_API_KEY"]
claude_key = st.secrets["CLAUDE_KEY"]

# Initialize API clients
openai_client = OpenAI(api_key=openai_key)
claude_client = anthropic.Anthropic(api_key=claude_key)


def clean_streamlit_code(code):
    """Remove setup config and unnecessary imports from Streamlit code."""
    lines = code.splitlines()
    cleaned_lines = []
    for line in lines:
        # Skip markdown fences and st.set_page_config and extraneous imports
        if line.strip().startswith("```") or "st.set_page_config" in line:
            continue
        cleaned_lines.append(line)
    return "\n".join(cleaned_lines)

def enhance_teaching_with_claude(content, purpose):
    """Use Claude to enhance and fix Streamlit content."""
    prompt = f"""As an expert in creating engaging Streamlit applications, please enhance this code:
1. Fix any potential issues or bugs.
2. Make the display more visually appealing and interactive.
3. Remove any st.set_page_config calls.
4. Keep the core teaching content but make it more engaging.
5. Ensure that all necessary imports are included at the top of the code. In particular, if the code uses functions or modules like colorsys or numpy (as np), include "import colorsys" or "import numpy as np" respectively. Only use packages from our approved package list.
6. Maintain any essential existing imports.

Here's the code to enhance:
{content}

Purpose of this content: {purpose}

Return the enhanced code between <code> </code> tags. Include ALL necessary imports at the top of the code."""

    response = claude_client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=2000,
        messages=[{"role": "user", "content": prompt}],
    )

    # Extract the text content from Claude's response
    if hasattr(response.content, "text"):
        response_text = response.content.text
    elif isinstance(response.content, list) and len(response.content) > 0:
        response_text = response.content[0].text
    else:
        response_text = str(response.content)

    if not response_text:
        return content  # Return original content if enhancement fails

    # Extract code from between <code> tags
    import re

    code_match = re.search(r"<code>(.*?)</code>", response_text, re.DOTALL)

    if code_match:
        enhanced_content = code_match.group(1).strip()
    else:
        # If no code tags found, try to use the full response
        enhanced_content = response_text.strip()

    # Only clean the code if it's not just imports
    if not all(
        line.strip().startswith("import") or line.strip().startswith("from")
        for line in enhanced_content.splitlines()
    ):
        enhanced_content = clean_streamlit_code(enhanced_content)

    return enhanced_content

def enhance_assessment_with_claude(content, purpose, previous_module):
    """Use Claude to enhance and fix Streamlit content."""
    prompt = f"""As an expert in creating engaging Streamlit educational assessment applications, please enhance this code:
1. Fix any potential issues or bugs.
2. Make the display more visually appealing and interactive.
3. Remove any st.set_page_config calls.
4. Keep the core assessment the same but make it more aesthetic.
5. Ensure that all necessary imports are included at the top of the code. In particular, if the code uses functions or modules like colorsys or numpy (as np), include "import colorsys" or "import numpy as np" respectively. Only use packages from our approved package list.
6. Maintain any essential existing imports.
7. Once a user gets all the answers correct on the assessment, be certain to call a function called exactly this:'utils.quiz_passed(module_number). Never include 'import utils' in the code.
8. Make sure the assessment only tests material that could be learned from this module: {previous_module}

Here's the code to enhance:
{content}

Purpose of this content: {purpose}

Return the enhanced code between <code> </code> tags. Include ALL necessary imports at the top of the code."""

    response = claude_client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=2000,
        messages=[{"role": "user", "content": prompt}],
    )

    # Extract the text content from Claude's response
    if hasattr(response.content, "text"):
        response_text = response.content.text
    elif isinstance(response.content, list) and len(response.content) > 0:
        response_text = response.content[0].text
    else:
        response_text = str(response.content)

    if not response_text:
        return content  # Return original content if enhancement fails

    # Extract code from between <code> tags
    import re

    code_match = re.search(r"<code>(.*?)</code>", response_text, re.DOTALL)

    if code_match:
        enhanced_content = code_match.group(1).strip()
    else:
        # If no code tags found, try to use the full response
        enhanced_content = response_text.strip()

    # Only clean the code if it's not just imports
    if not all(
        line.strip().startswith("import") or line.strip().startswith("from")
        for line in enhanced_content.splitlines()
    ):
        enhanced_content = clean_streamlit_code(enhanced_content)

    return enhanced_content


class ModuleGenerator:
    def __init__(self, topic, module_number, initial_model="openai"):
        """
        initial_model: set to "openai" or "claude" to choose which LLM to use for initial generation.
        """
        self.topic = topic
        self.module_number = module_number
        self.module_path = f"modules/module_{module_number}"
        self.initial_model = initial_model.lower()

    def generate_completion(self, messages, default_model="gpt-4o"):
        """
        Helper method that sends the messages to the selected LLM.
        For OpenAI, it uses the OpenAI client; for Claude, it concatenates the messages into a prompt.
        """
        if self.initial_model == "openai":
            completion = openai_client.chat.completions.create(
                model=default_model, messages=messages
            )
            return completion.choices[0].message.content.strip()
        elif self.initial_model == "claude":
            # Concatenate messages into a single prompt for Claude.
            prompt = ""
            for msg in messages:
                role = msg.get("role", "")
                content = msg.get("content", "")
                if role == "system":
                    prompt += f"System: {content}\n"
                elif role == "user":
                    prompt += f"User: {content}\n"
                elif role == "assistant":
                    prompt += f"Assistant: {content}\n"
            response = claude_client.messages.create(
                model="claude-3-5-sonnet-20241022",
                max_tokens=2000,
                messages=[{"role": "user", "content": prompt}],
            )
            if hasattr(response.content, "text"):
                response_text = response.content.text
            elif isinstance(response.content, list) and len(response.content) > 0:
                response_text = response.content[0].text
            else:
                response_text = str(response.content)
            return response_text.strip()
        else:
            raise ValueError(f"Unsupported initial_model: {self.initial_model}")

    def create_module_structure(self):
        """Create the module directory and empty files."""
        os.makedirs(self.module_path, exist_ok=True)
        Path(f"{self.module_path}/module.json").touch()
        Path(f"{self.module_path}/quiz.py").touch()

    def generate_content(self, subject, learning_style):
        """Generate and enhance content for all module files."""
        # Generate module metadata
        module_data = self.generate_module_metadata(subject, learning_style)
        with open(f"{self.module_path}/module.json", "w") as f:
            json.dump(module_data, f, indent=2)

        # Generate and enhance articles in parallel
        article_titles = module_data["articles"]
        with concurrent.futures.ThreadPoolExecutor() as executor:
            future_to_article = {
                executor.submit(
                    self.generate_enhanced_article, subject, learning_style, title
                ): article_num
                for article_num, title in article_titles.items()
            }
            for future in concurrent.futures.as_completed(future_to_article):
                article_num = future_to_article[future]
                article_content = future.result()
                with open(f"{self.module_path}/article_{article_num}.py", "w") as f:
                    f.write(article_content)

        # Generate and enhance quiz content
        quiz_content = self.generate_enhanced_assessment(
            subject, learning_style, article_content
        )
        with open(f"{self.module_path}/quiz.py", "w") as f:
            f.write("import modules.utils as utils\n")
            f.write("params = st.params = st.query_params\n")
            f.write("module_number = int(params.get(\"module\", [0])[0]) if \"module\" in params else None\n")
            f.write(quiz_content)

    def generate_module_metadata(self, subject, learning_style):
        """Generate module metadata using the selected LLM."""
        overview = self.generate_overview(subject, learning_style)
        article_titles = self.generate_article_titles(subject, learning_style)
        return {
            "module_number": self.module_number,
            "module_name": f"Module {self.module_number}: Introduction to {self.topic}",
            "overview": overview,
            "learning_objectives": [
                f"Understand the fundamentals of {self.topic}",
                f"Explore advanced concepts in {self.topic}",
                f"Apply practical examples related to {self.topic}",
            ],
            "articles": article_titles,
            "progress": {"current_article": 1, "quiz_passed": False},
        }

    def generate_overview(self, subject, learning_style):
        """Generate a brief module overview using the selected LLM."""
        messages = [
            {
                "role": "system",
                "content": "You are a helpful tutor who creates engaging module overviews for a subject. Return a short overview in plain text.",
            },
            {
                "role": "user",
                "content": f"Generate a brief overview for a module teaching {subject} in a way that fits this learning style: {learning_style}.",
            },
        ]
        return self.generate_completion(messages, default_model="gpt-4o")

    def generate_article_titles(self, subject, learning_style):
        """Generate article titles using the selected LLM."""
        num_articles = 1
        messages = [
            {
                "role": "system",
                "content": "You are a creative tutor generating article titles for an educational module. Return only a numbered list of titles, one per line.",
            },
            {
                "role": "user",
                "content": f"Generate {num_articles} article titles for a module on {subject} that fits this learning style: {learning_style}.",
            },
        ]
        titles_text = self.generate_completion(messages, default_model="gpt-4o")
        article_titles = {}
        for line in titles_text.splitlines():
            if "." in line:
                try:
                    num, title = line.split(".", 1)
                    article_titles[str(num.strip())] = title.strip()
                except Exception:
                    continue
        return article_titles

    def generate_enhanced_article(self, subject, learning_style, article_title):
        """Generate and enhance an article using both the selected LLM and Claude for enhancement."""
        # First generate base content with the selected LLM
        initial_content = self.generate_teaching_article(
            subject, learning_style, article_title
        )
        # Then enhance it with Claude
        purpose = f"Educational article about {subject} titled '{article_title}' for {learning_style} learning style"
        enhanced_content = enhance_teaching_with_claude(initial_content, purpose)
        return enhanced_content

    def generate_teaching_article(self, subject, learning_style, article_title):
        """Generate initial article content using the selected LLM."""
        messages = [
            {
                "role": "system",
                "content": "You are a creative tutor who designs innovative and visually engaging educational content using Streamlit code. Return only the Streamlit code that can be executed directly.",
            },
            {
                "role": "system",
                "content": f"The student's learning style is: {learning_style}. Emphasize interactive components and creative visualizations.",
            },
            {
                "role": "user",
                "content": f"Generate a short, creative article titled '{article_title}' about {subject}. Include interactive elements and visualizations. Return only Streamlit code.",
            },
        ]
        content = self.generate_completion(messages, default_model="gpt-4o")
        return clean_streamlit_code(content)

    def generate_enhanced_assessment(self, subject, learning_style, previous_module):
        """Generate and enhance assessment using both the selected LLM and Claude for enhancement."""
        # Generate initial assessment with the selected LLM
        initial_content = self.generate_assessment(
            subject, learning_style, previous_module
        )
        # Enhance with Claude
        purpose = f"Assessment quiz for {subject} module, tailored to {learning_style} learning style"
        enhanced_content = enhance_assessment_with_claude(initial_content, purpose, previous_module)
        return enhanced_content

    def generate_assessment(self, subject, learning_style, previous_module):
        """Generate a short assessment based on the module overview using AI chat completions."""
        completion = openai_client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful tutor who is going to assess if a student understood certain subject material. You will do this by returning Streamlit code that will fit in individual Python files/pages. Focus on returning creative UI components, like tables, interactive graphs, games, or anything else you can think of that will surprise the student that will help the student learn. Only return Streamlit code, nothing else that would not work directly as Streamlit code, no not return any backticks."},
            {"role": "system", "content": f"Here is the module the student tried to learn from as Streamlit code:{previous_module}"},
            {"role": "system", "content": f"Once a user gets all the answers correct on the quiz, be certain to call a function called exactly this:'utils.quiz_passed(module_number). Never include 'import utils' in the code."},

            {
                "role": "user",
                "content": f"Generate some short, concise method of assessing the student to test their understanding of {subject} based on the module they tried to learn the material from. Only inlcude information they could have learned from the module and one question, and only return Streamlit code, no not return any backticks."
            }
        ]
    )
        assessment_content = f"{completion.choices[0].message.content}\n"
        print(assessment_content)
        return assessment_content
