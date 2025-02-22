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

    def generate_content(self, subject, learning_style):
        """Generate content for all module files using OpenAI."""
        # Generate and save module metadata (including progress tracking)
        module_data = self.generate_module_metadata()
        with open(f"{self.module_path}/module.py", "w") as f:
            f.write(json.dumps(module_data, indent=2))

        # Generate and save article content
        article_content = self.generate_teaching(subject, learning_style)
        with open(f"{self.module_path}/article_1.py", "w") as f:
            f.write(article_content)

        # Generate and save quiz content
        quiz_content = self.generate_assessment(subject, learning_style, article_content)
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

    def generate_teaching(self, subject, learning_style):
        """Generate an article about the topic using OpenAI chat completions."""
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
        """Generate a multiple-choice quiz question about the topic using OpenAI chat completions."""
        completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful tutor who is going to assess if a student understood certain subject material. You will do this by returning Streamlit code that will fit in individual Python files/pages. Focus on returning creative UI components, like tables, interactive graphs, games, or anything else you can think of that will surprise the student that will help the student learn. Only return Streamlit code, nothing else that would not work directly as Streamlit code, no not return any backticks."},
            {"role": "system", "content": f"Here is the module the student tried to learn from as Streamlit code:{previous_module}"},
            {
                "role": "user",
                "content": f"Generate some short, concise method of assessing the student to test their understanding of {subject} based on the module they tried to learn the material from. Only inlcude information they could have learned from the module, and only return Streamlit code, no not return any backticks."
            }
        ]
    )
        assessment_content = f"{completion.choices[0].message.content}\n"
        print(assessment_content)
        return assessment_content
