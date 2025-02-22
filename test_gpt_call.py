from openai import OpenAI
client = OpenAI()

def ask_openai_teaching(subject, crazy_level):
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful tutor who is going to teach someone a subject they request in an engaging, concise way. You will do this by returning Streamlit code that will fit in individual Python files/pages. Only return Streamlit code, nothing else that would not work directly as Streamlit code, no not return any backticks. "},
            {
                "role": "user",
                "content": f"Start teaching them by generating a short article, quiz, or some crazy component to teach them  about {subject}. The amount of information contained should be no more than a paragraph or 2. How crazy the component or method of teaching will be delineated by a Crazy Level. This user wants a crazy level of {crazy_level}. Return the article Streamlit code that can render it."
            }
        ]
    )
    with open("app.py", "a") as f:
        print(completion.choices[0].message.content)
        new_content = f"{completion.choices[0].message.content}\n"
        f.write(new_content)
    ask_openai_assessing(subject, crazy_level, new_content)

def ask_openai_assessing(subject, crazy_level, previous_module):
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful tutor who is going to assess if a student understood certain subject material. You will do this by returning Streamlit code that will fit in individual Python files/pages. Only return Streamlit code, nothing else that would not work directly as Streamlit code, no not return any backticks."},
            {"role": "system", "content": f"Here is the module the student tried to learn from as Streamlit code:{previous_module}"},
            {
                "role": "user",
                "content": f"Generate some short, concise method of assessing the student like a quiz, text input, or something else, to test their understanding of {subject} based on the module they tried to learn the material from. Make this way of testing them be about 1 or 2 questions long. How crazy the component or method of teaching will be delineated by a Crazy Level. This user wants a crazy level of {crazy_level}. Only inlcude information they could have learned from the module, and only return Streamlit code, no not return any backticks."
            }
        ]
    )
    with open("app.py", "a") as f:
        print(completion.choices[0].message.content)
        new_content_assessment = f"{completion.choices[0].message.content}\n"
        f.write(new_content_assessment)