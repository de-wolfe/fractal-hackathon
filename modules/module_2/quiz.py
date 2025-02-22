import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

# Custom styling
st.markdown("""
    <style>
    .question-text {
        font-size: 20px;
        color: #2c3e50;
        padding: 10px;
        background-color: #f7f9fc;
        border-radius: 5px;
        margin: 10px 0;
    }
    </style>
""", unsafe_allow_html=True)

# Header with engaging title
st.title("🌌 Quantum Mysteries: Interactive Quiz")
st.markdown("### Explore the fascinating world of quantum mechanics!")

# Progress tracking
progress = 0
total_questions = 2

# Create columns for layout
col1, col2 = st.columns([2, 1])

with col1:
    # Question 1 with visual enhancement
    st.markdown('<p class="question-text">Question 1: The Quantum Dance</p>', unsafe_allow_html=True)
    q1 = st.radio(
        "A quantum particle exists in multiple states simultaneously until measured. This phenomenon is known as:",
        ('Wave function collapse', 'Quantum superposition', 'Quantum entanglement', 'Wave-particle duality'),
        help="Think about the fundamental nature of quantum particles before measurement!"
    )

    # Question 2 with visual enhancement
    st.markdown('<p class="question-text">Question 2: Schrödinger\'s Famous Feline</p>', unsafe_allow_html=True)
    q2 = st.text_area(
        "Explain Schrödinger's Cat thought experiment in your own words and what it demonstrates about quantum mechanics:",
        height=150,
        help="Remember to include key elements: cat, container, and measurement concept"
    )

with col2:
    # Visual representation of quantum superposition
    fig, ax = plt.subplots(figsize=(4, 4))
    x = np.linspace(-2, 2, 1000)
    y1 = np.exp(-x**2) * np.cos(5*x)
    y2 = np.exp(-x**2) * np.sin(5*x)
    ax.plot(x, y1, 'b-', alpha=0.5, label='State 1')
    ax.plot(x, y2, 'r-', alpha=0.5, label='State 2')
    ax.set_title('Quantum Wave Function')
    ax.legend()
    st.pyplot(fig)

# Submit button with animation
if st.button("🔍 Evaluate My Understanding", help="Click to see your results!"):
    score = 0
    feedback = ""
    
    # Grade Q1
    if q1 == "Quantum superposition":
        score += 1
        feedback += "✨ Q1: Brilliant! Quantum superposition is indeed the correct answer.\n\n"
    else:
        feedback += "📚 Q1: Not quite. Quantum superposition describes the ability of particles to exist in multiple states simultaneously.\n\n"
    
    # Grade Q2
    if len(q2) > 0:
        key_terms = ["cat", "box", "container", "measurement", "observe", "state"]
        matches = sum(1 for term in key_terms if term in q2.lower())
        if matches >= 3:
            score += 1
            feedback += "✨ Q2: Excellent explanation! You've captured the essence of the thought experiment.\n\n"
        else:
            feedback += "📚 Q2: Your explanation could include more key elements of the thought experiment.\n\n"
    
    # Display results with visual enhancement
    st.markdown(f"### Your Quantum Score: {score}/{total_questions}")
    st.progress(score/total_questions)
    st.info(feedback)
    
    if score == total_questions:
        st.balloons()
        st.success("🎉 Congratulations! You've mastered these quantum concepts!")
    elif score > 0:
        st.warning("Keep exploring! You're on the right track.")
    else:
        st.error("Don't worry! Quantum mechanics is complex. Try reviewing the concepts and attempt again.")

st.markdown("---")
st.markdown("*Remember: In quantum mechanics, the act of observation affects the outcome!*")