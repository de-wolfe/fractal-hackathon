import streamlit as st
import os


def generate_streamlit_code(topic):
    """
    Simulate an LLM generating Streamlit UI code with navigation.
    This code creates a sidebar for navigation between different pages.
    """
    code = f"""
import streamlit as st

def show_home(topic):
    st.title(f"Learning Materials for {{topic}}")
    st.write("Welcome! Use the navigation on the left to explore the learning materials.")

def show_syllabus(topic):
    st.title(f"Syllabus for {{topic}}")
    st.write("1. Introduction to {{topic}}")
    st.write("2. Key Concepts in {{topic}}")
    st.write("3. Advanced Topics in {{topic}}")

def show_articles(topic):
    st.title(f"Learning Articles for {{topic}}")
    st.write("- https://example.com/{{topic}}-basics")
    st.write("- https://example.com/{{topic}}-advanced")
    st.write("- https://example.com/{{topic}}-case-studies")

def show_quiz(topic):
    st.title(f"Quiz on {{topic}}")
    st.write("1. What is {{topic}}?")
    st.write("2. Name one application of {{topic}}.")
    st.write("3. Describe a challenge related to {{topic}}.")

def main():
    topic = "{topic}"
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", ["Home", "Syllabus", "Articles", "Quiz"])
    
    if selection == "Home":
        show_home(topic)
    elif selection == "Syllabus":
        show_syllabus(topic)
    elif selection == "Articles":
        show_articles(topic)
    elif selection == "Quiz":
        show_quiz(topic)

if __name__ == "__main__":
    main()
"""
    return code


def update_ui_file(new_code, filename="generated_ui.py"):
    # Backup the original file if needed
    if os.path.exists(filename):
        os.rename(filename, filename + ".bak")

    with open(filename, "w") as f:
        f.write(new_code)
    st.success(f"Updated {filename} with new UI code!")


def main():
    st.title("Dynamic UI Code Generator")
    topic = st.text_input("Enter a topic:", value="Example Topic")

    if st.button("Generate New UI Code with Navigation"):
        if topic.strip():
            # Generate new code based on the topic
            new_code = generate_streamlit_code(topic)
            update_ui_file(new_code)

            # Inform the user they might need to refresh or restart the app.
            st.info(
                "The UI code has been updated in 'generated_ui.py'. Please refresh your browser or restart the app to see changes."
            )
        else:
            st.warning("Please enter a valid topic.")


if __name__ == "__main__":
    main()
