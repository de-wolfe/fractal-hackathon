import os
import json
from pathlib import Path
from openai import OpenAI
import streamlit as st

api_key = st.secrets["OPENAI_API_KEY"]

# Instantiate the OpenAI client
client = OpenAI(api_key=api_key)


def clean_streamlit_code(code):
    """
    Remove markdown code fences (e.g. lines starting with triple backticks)
    from the provided code so that only pure Streamlit code remains.
    """
    lines = code.splitlines()
    cleaned_lines = []
    for line in lines:
        if line.strip().startswith("```"):
            continue
        cleaned_lines.append(line)
    return "\n".join(cleaned_lines)


class ModuleGenerator:
    def __init__(self, topic, module_number):
        self.topic = topic
        self.module_number = module_number
        self.module_path = f"modules/module_{module_number}"

    def create_module_structure(self):
        """Create the module directory and empty files."""
        os.makedirs(self.module_path, exist_ok=True)
        # Create empty metadata and quiz files; article files will be created after generating titles.
        Path(f"{self.module_path}/module.json").touch()
        Path(f"{self.module_path}/quiz.py").touch()

    def generate_content(self, subject, learning_style):
        """Generate content for all module files using OpenAI."""
        # Generate module metadata (overview and article titles)
        module_data = self.generate_module_metadata(subject, learning_style)
        with open(f"{self.module_path}/module.json", "w") as f:
            json.dump(module_data, f, indent=2)

        # For each article title, generate the article content and save it.
        for article_num, title in module_data["articles"].items():
            article_content = self.generate_teaching_article(
                subject, learning_style, title
            )
            with open(f"{self.module_path}/article_{article_num}.py", "w") as f:
                f.write(article_content)

        # Generate and save quiz content
        quiz_content = self.generate_assessment(
            subject, learning_style, module_data.get("overview", "")
        )
        with open(f"{self.module_path}/quiz.py", "w") as f:
            f.write("import modules.utils as utils\n")
            f.write("params = st.experimental_get_query_params()\n")
            f.write("module_number = int(params.get(\"module\", [0])[0]) if \"module\" in params else None\n")
            f.write(quiz_content)

    def generate_module_metadata(self, subject, learning_style):
        """Generate module metadata including overview, article titles, and progress tracking."""
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
            # Dictionary mapping article numbers to titles
            "articles": article_titles,
            # Progress tracking for articles and quiz
            "progress": {"current_article": 1, "quiz_passed": False},
        }

    def generate_overview(self, subject, learning_style):
        """Generate a brief module overview using AI."""
        completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful tutor who is going to teach someone a subject they request in an engaging, concise way. You will do this by returning Streamlit code that will fit in individual Python files/pages. Start by teaching the student about the topic, and make sure to include creative interactive components to help them learn. Only return Streamlit code, nothing else that would not work directly as Streamlit code, no not return any backticks. "},
            {"role": "system", "content": f"Here is some information on the learning style of this particular student, or things that make it easier for them to learn:{learning_style}. When making Streamlit components, prioritize making content in this style."},

            {
                "role": "user",
                "content": f"Start teaching about {subject}. The amount of information contained should be no more than a paragraph or 2. Return Streamlit code."
            }
        ]
    )
        teaching_content = f"{completion.choices[0].message.content}\n"
        print(teaching_content)
        return teaching_content

    def generate_assessment(self, subject, learning_style, previous_module):
        """Generate a short assessment based on the module overview using AI chat completions."""
        completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful tutor who is going to assess if a student understood certain subject material. You will do this by returning Streamlit code that will fit in individual Python files/pages. Focus on returning creative UI components, like tables, interactive graphs, games, or anything else you can think of that will surprise the student that will help the student learn. Only return Streamlit code, nothing else that would not work directly as Streamlit code, no not return any backticks."},
            {"role": "system", "content": f"Here is the module the student tried to learn from as Streamlit code:{previous_module}"},
            {"role": "system", "content": f"Once a user gets all the answers correct on the quiz, be certain to call a function called 'utils.quiz_passed(module_number)"},

            {
                "role": "user",
                "content": f"Generate some short, concise method of assessing the student to test their understanding of {subject} based on the module they tried to learn the material from. Only inlcude information they could have learned from the module, and only return Streamlit code, no not return any backticks."
            }
        ]
    )
        assessment_content = f"{completion.choices[0].message.content}\n"
        print(assessment_content)
        return assessment_content
