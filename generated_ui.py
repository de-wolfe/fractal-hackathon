
import streamlit as st
import quiz  # Import the quiz module

def show_generated_steps(topic):
    st.markdown("## Navigation Steps")
    st.markdown("- [Home](#home)")
    st.markdown("- [Syllabus](#syllabus)")
    st.markdown("- [Articles](#articles)")
    st.markdown("- [Quiz](#quiz)")
    st.markdown("- [Return to Generator](#return-to-generator)")

def show_home(topic):
    st.markdown("### Home")
    st.title(f"Learning Materials for {topic}")
    st.write("Welcome to the generated UI! Use the links above to navigate.")

def show_syllabus(topic):
    st.markdown("### Syllabus")
    st.write("1. Introduction to " + topic)
    st.write("2. Key Concepts in " + topic)
    st.write("3. Advanced Topics in " + topic)

def show_articles(topic):
    st.markdown("### Articles")
    st.write("- https://example.com/" + topic + "-basics")
    st.write("- https://example.com/" + topic + "-advanced")
    st.write("- https://example.com/" + topic + "-case-studies")

def show_quiz(topic):
    st.markdown("### Quiz")
    # Use the quiz component from our quiz module
    quiz.show_quiz(topic)

def show_back():
    st.markdown("### Return to Generator")
    st.write("Click the button below to go back to the generator.")
    if st.button("Go Back"):
        st.set_query_params(page="generator")


def main():
    topic = "Example Topic"
    st.markdown("# Generated UI")
    show_generated_steps(topic)
    st.markdown("---")
    show_home(topic)
    st.markdown("---")
    show_syllabus(topic)
    st.markdown("---")
    show_articles(topic)
    st.markdown("---")
    show_quiz(topic)
    st.markdown("---")
    show_back()

if __name__ == "__main__":
    main()
