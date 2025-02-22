import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image
import random
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

st.title("🐔 Why Did the Unit Test Cross the Road?")
st.subheader("To Assert Its Independence! 🤣")

# Fun animation effect with custom styling
st.markdown("""
    <style>
    .main-content {
        padding: 2rem;
        border-radius: 10px;
        background-color: #f8f9fa;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
## The Comedy Club of Testing 🎭

Once upon a time, in a codebase far, far away...
""")

# Enhanced interactive joke section with animation
col1, col2 = st.columns([3, 1])
with col1:
    if st.button("Tell me a testing joke! 😄", key="joke_button"):
        jokes = [
            "What's a unit test's favorite drink? Mock-a Cola! 🥤",
            "Why do unit tests make terrible comedians? They always expect something! 🎭",
            "What did the unit test say to the bug? I've got my assertions on you! 👀",
            "Why was the test suite feeling lonely? It had no class! 📚",
            "What's a QA tester's favorite dessert? Bug pudding! 🍮"
        ]
        st.success(random.choice(jokes))

# Enhanced knowledge check with progress bar
st.markdown("### 🎯 Test Your Testing Knowledge!")
progress = st.progress(0)
answer = st.radio(
    "What's the main purpose of unit testing?",
    [
        "To make developers cry 😢",
        "To test individual components in isolation ✅",
        "To waste company time ⌛",
        "To make the code run slower 🐌"
    ]
)

if answer == "To test individual components in isolation ✅":
    progress.progress(100)
    st.success("🎉 Correct! You're a testing superhero!")
else:
    progress.progress(30)
    st.error("Try again! Don't let the bugs win! 🐛")

# Enhanced visual representation with more engaging data
test_data = {
    'Testing Type': ['Unit Tests', 'Integration Tests', 'End-to-End Tests'],
    'Time to Run': [1, 5, 10],
    'Bug Detection': [70, 20, 10],
    'Complexity': [1, 3, 5]
}

df = pd.DataFrame(test_data)

# Interactive chart with more options
chart_type = st.selectbox(
    "Choose your visualization:",
    ["Bar", "Pie", "Scatter"]
)

if chart_type == "Bar":
    fig = px.bar(df, x='Testing Type', y='Bug Detection',
                 title='Bug Detection by Test Type',
                 color='Testing Type',
                 labels={'Bug Detection': 'Bug Detection %'},
                 template="plotly_dark")
elif chart_type == "Pie":
    fig = px.pie(df, values='Bug Detection', names='Testing Type',
                 title='Bug Detection Distribution',
                 hole=0.3)
else:
    fig = px.scatter(df, x='Time to Run', y='Bug Detection',
                    size='Complexity',
                    color='Testing Type',
                    title='Testing Metrics Correlation')

st.plotly_chart(fig, use_container_width=True)

# Enhanced interactive testing simulator
st.markdown("### 🎮 Test Your Code!")
code_input = st.text_area("Write a simple function to test:", 
                         "def add(a, b):\n    return a + b",
                         height=100)

if st.button("Run Mock Test", key="test_button"):
    with st.spinner("Running tests..."):
        st.code("""
def test_add():
    assert add(2, 2) == 4  # Basic addition
    assert add(0, 0) == 0  # Zero case
    assert add(-1, 1) == 0 # Negative numbers
    print("All tests passed! 🎉")
    """)
        st.success("Tests passed successfully! You're now a testing ninja! 🥷")

# Enhanced fun fact section
with st.expander("🎈 Fun Testing Facts"):
    cols = st.columns(2)
    with cols[0]:
        st.markdown("""
        - The term 'bug' came from an actual moth found in a computer in 1947!
        - The average developer spends 35-50% of their time testing code
        """)
    with cols[1]:
        st.markdown("""
        - Unit tests can reduce bug detection costs by up to 90%
        - Some developers write tests before writing actual code (TDD)
        """)

# Enhanced footer
st.markdown("---")
st.markdown("""
<div style='text-align: center'>
    <h4>Remember: A test in time saves nine! ⏰</h4>
    <p>Keep calm and write test cases 🧪</p>
</div>
""", unsafe_allow_html=True)