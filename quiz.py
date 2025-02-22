import streamlit as st


def initialize_quiz_state():
    """Initialize quiz session state variables if they don't exist"""
    if "current_question" not in st.session_state:
        st.session_state.current_question = 0
    if "score" not in st.session_state:
        st.session_state.score = 0
    if "quiz_complete" not in st.session_state:
        st.session_state.quiz_complete = False


def get_questions(topic):
    """Generate questions based on the topic"""
    return [
        {
            "question": f"What is {topic}?",
            "options": [
                f"A framework for building {topic} applications",
                f"A programming language for {topic}",
                f"A methodology for understanding {topic}",
                f"A tool for analyzing {topic}",
            ],
            "correct_answer": f"A methodology for understanding {topic}",
        },
        {
            "question": f"Which of the following is a key concept in {topic}?",
            "options": [
                f"{topic} Architecture",
                f"{topic} Implementation",
                f"{topic} Design",
                "All of the above",
            ],
            "correct_answer": "All of the above",
        },
        {
            "question": f"What is the primary benefit of using {topic}?",
            "options": [
                "Increased efficiency",
                "Better organization",
                "Improved understanding",
                "Enhanced productivity",
            ],
            "correct_answer": "Improved understanding",
        },
    ]


def check_answer(selected_answer, correct_answer):
    """Check if the selected answer is correct and update score"""
    if selected_answer == correct_answer:
        st.session_state.score += 1
        st.success("Correct! 🎉")
    else:
        st.error(f"Wrong! The correct answer is {correct_answer}")

    # Move to next question
    st.session_state.current_question += 1
    if st.session_state.current_question >= len(st.session_state.questions):
        st.session_state.quiz_complete = True


def show_quiz(topic):
    """Main quiz component that can be called from other Streamlit pages"""
    # Initialize state
    initialize_quiz_state()

    # Initialize questions if not already done
    if "questions" not in st.session_state:
        st.session_state.questions = get_questions(topic)

    st.title(f"📚 Quiz: {topic}")
    st.write("Test your knowledge with this quick quiz!")

    # Display progress
    questions = st.session_state.questions
    progress = st.progress(st.session_state.current_question / len(questions))
    st.write(f"Question {st.session_state.current_question + 1} of {len(questions)}")

    # Quiz logic
    if not st.session_state.quiz_complete:
        current_q = questions[st.session_state.current_question]
        st.subheader(current_q["question"])

        # Create radio buttons for options
        answer = st.radio(
            "Choose your answer:",
            current_q["options"],
            key=f"question_{st.session_state.current_question}",
        )

        # Check answer button
        if st.button("Submit Answer"):
            check_answer(answer, current_q["correct_answer"])
            st.rerun()

    # Quiz completion
    if st.session_state.quiz_complete:
        st.balloons()
        st.success(
            f"Quiz completed! Your score: {st.session_state.score}/{len(questions)}"
        )

        # Calculate percentage
        percentage = (st.session_state.score / len(questions)) * 100
        st.write(f"You got {percentage:.1f}% correct!")

        # Provide feedback based on score
        if percentage == 100:
            st.write("Perfect score! You're a genius! 🌟")
        elif percentage >= 80:
            st.write("Great job! You really know your stuff! 🎉")
        elif percentage >= 60:
            st.write("Good effort! Keep learning! 📚")
        else:
            st.write("Keep practicing! You can do better next time! 💪")

        # Restart button
        if st.button("Restart Quiz"):
            st.session_state.current_question = 0
            st.session_state.score = 0
            st.session_state.quiz_complete = False
            st.session_state.questions = get_questions(topic)
            st.rerun()


if __name__ == "__main__":
    show_quiz("Sample Topic")  # For testing the component independently
