
import streamlit as st

def display_quiz():
    st.header("Module Quiz")
    score = 0
    total_questions = 3

    # Question 1
    q1 = st.radio(
        "Question 1: Sample question here?",
        ["Option 1", "Option 2", "Option 3", "Option 4"]
    )
    if q1 == "Option 2":  # Correct answer
        score += 1

    # Display results
    if st.button("Submit Quiz"):
        st.write(f"Your score: {score}/{total_questions}")

display_quiz()
