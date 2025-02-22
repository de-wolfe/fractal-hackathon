import os
import json
from pathlib import Path
from openai import OpenAI
import streamlit as st

api_key = st.secrets["OPENAI_KEY"]

# Instantiate the OpenAI client
client = OpenAI(api_key=api_key)


class ModuleGenerator:
    def __init__(self, topic, module_number):
        self.topic = topic
        self.module_number = module_number
        self.module_path = f"modules/module_{module_number}"

    def create_module_structure(self):
        """Create the module directory and empty files."""
        os.makedirs(self.module_path, exist_ok=True)

        # Create empty files for metadata, article, and quiz
        Path(f"{self.module_path}/module.py").touch()
        Path(f"{self.module_path}/article_1.py").touch()
        Path(f"{self.module_path}/quiz.py").touch()

    def generate_content(self):
        """Generate content for all module files using OpenAI."""
        # Generate and save module metadata (including progress tracking)
        module_data = self.generate_module_metadata()
        with open(f"{self.module_path}/module.py", "w") as f:
            f.write(json.dumps(module_data, indent=2))

        # Generate and save article content
        article_content = self.generate_article()
        with open(f"{self.module_path}/article_1.py", "w") as f:
            f.write(article_content)

        # Generate and save quiz content
        quiz_content = self.generate_quiz()
        with open(f"{self.module_path}/quiz.py", "w") as f:
            f.write(quiz_content)

    def generate_module_metadata(self):
        """Generate module metadata including progress tracking."""
        return {
            "module_number": self.module_number,
            "module_name": f"Module {self.module_number}: Introduction to {self.topic}",
            "learning_objectives": [
                f"Understand the fundamentals of {self.topic}",
                f"Explore advanced concepts in {self.topic}",
                f"Apply practical examples related to {self.topic}",
            ],
            # Progress tracking for articles and quiz
            "progress": {"current_article": 1, "quiz_passed": False},
        }

    def generate_article(self):
        """Generate an article about the topic using OpenAI chat completions."""
        prompt = (
            f"Write an engaging and informative educational article about {self.topic}. "
            "Explain its key concepts, background, and practical applications in a clear and concise manner."
        )
        try:
            completion = client.chat.completions.create(
                model="gpt-4o",
                store=True,
                messages=[{"role": "user", "content": prompt}],
            )
            article_text = completion.choices[0].message.content.strip()
        except Exception as e:
            article_text = f"Error generating article content: {e}"

        return f"""
import streamlit as st

st.header("Introduction to {self.topic}")
st.write({json.dumps(article_text)})
"""

    def generate_quiz(self):
        """Generate a multiple-choice quiz question about the topic using OpenAI chat completions."""
        prompt = (
            f"Generate a multiple-choice quiz question that tests understanding of {self.topic}. "
            "Include one question with 4 answer options, and mark the correct option in a comment."
        )
        try:
            completion = client.chat.completions.create(
                model="gpt-4o",
                store=True,
                messages=[{"role": "user", "content": prompt}],
            )
            quiz_text = completion.choices[0].message.content.strip()
        except Exception as e:
            quiz_text = f"Error generating quiz content: {e}"

        return f"""
import streamlit as st

st.header("Quiz on {self.topic}")
st.write({json.dumps(quiz_text)})
"""
