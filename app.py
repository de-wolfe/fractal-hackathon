import streamlit as st
import writer
import test_gpt_call
import random
import numpy as np
import matplotlib.pyplot as plt

    

# Streamlit UI setup
st.title("Interactive Quiz App")
subject = st.text_input("What do you want to learn about?")
crazy_level = st.slider("Crazy Level")
if st.button("Click me"):
    test_gpt_call.ask_openai_teaching(subject, crazy_level)

import streamlit as st

st.title("Introduction to Basic Thermodynamics")

st.write("""
Thermodynamics is the branch of physics that deals with the relationships between heat and other forms of energy. At the heart of thermodynamics are the four fundamental laws: the zeroth, first, second, and third laws. 

- **Zeroth Law**: Establishes the concept of temperature. If two thermodynamic systems are each in thermal equilibrium with a third one, they are also in thermal equilibrium with each other.
- **First Law**: Known as the Law of Energy Conservation, it states that energy cannot be created or destroyed in an isolated system.
- **Second Law**: Introduces the concept of entropy, indicating that the total entropy of an isolated system can never decrease over time.
- **Third Law**: As a system approaches absolute zero, the entropy of the system approaches a constant minimum.

These principles are essential for understanding how energy is transferred and transformed, which is foundational to engineering, chemistry, and many natural phenomena. Thermodynamics provides the framework for analyzing the efficiency of engines, refrigerators, and even biological processes.
""")
import streamlit as st

st.title("Basic Thermodynamics Quiz")

st.write("Test your understanding of basic thermodynamics concepts introduced in the module.")

question1 = st.radio(
    "Which law of thermodynamics introduces the concept of entropy?",
    ("Zeroth Law", "First Law", "Second Law", "Third Law")
)

if question1:
    if question1 == "Second Law":
        st.write("Correct! The Second Law of Thermodynamics introduces the concept of entropy.")
    else:
        st.write("Incorrect. The Second Law of Thermodynamics introduces the concept of entropy.")

question2 = st.text_input("What does the First Law of Thermodynamics state?")

if question2:
    correct_answer2 = "energy cannot be created or destroyed in an isolated system"
    if correct_answer2 in question2.lower():
        st.write("Correct! The First Law of Thermodynamics states that energy cannot be created or destroyed in an isolated system.")
    else:
        st.write("Incorrect. The First Law of Thermodynamics states that energy cannot be created or destroyed in an isolated system.")
