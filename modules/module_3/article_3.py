import streamlit as st
import pandas as pd
import plotly.express as px
from random import choice
import numpy as np
import plotly.graph_objects as go
import seaborn as sns
import matplotlib.pyplot as plt

st.title("🐛 Debug Walks into a Bar: The Hilarious Side of Test-Driven Development")

# Add custom CSS for better styling
st.markdown("""
    <style>
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 10px;
        padding: 10px 20px;
    }
    .highlight {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# Enhanced joke generator with animation
testing_jokes = [
    "Why do programmers prefer dark mode? Because light attracts bugs! 🐛",
    "What's a unit test's favorite drink? Mock-tail! 🍹",
    "How do you know your tests are working? They keep failing! 😅",
    "What's a developer's favorite party game? Debug the bottle! 🍾",
    "Why did the test fail? It was ex-spec-ting something else! 📝",
    "What's a QA engineer's favorite dessert? Bug pudding! 🍮",
    "Why did the testing framework go to therapy? Too many dependencies! 🛋️"
]

col1, col2 = st.columns([2, 1])
with col1:
    if st.button("Tell me a testing joke! 🎭"):
        st.markdown(f"### {choice(testing_jokes)}")
        st.balloons()

# Enhanced TDD Rules visualization
st.markdown("""
## 🎭 The TDD Comedy Club Rules
""")

rules = {
    "Act 1: Red 🔴": "Write a test that fails (like a bad joke)",
    "Act 2: Green 💚": "Write code that passes (the punchline)",
    "Act 3: Refactor 🔄": "Polish your routine (make it shine)"
}

for rule, desc in rules.items():
    st.markdown(f"### {rule}")
    st.markdown(f"*{desc}*")

# Enhanced TDD Cycle Visualization
tdd_cycle = pd.DataFrame({
    'Stage': ['Red', 'Green', 'Refactor'],
    'Time': [20, 40, 40],
    'Description': ['Write failing test', 'Make it pass', 'Make it better']
})

fig = px.pie(tdd_cycle, values='Time', names='Stage', title='The TDD Comedy Cycle',
             color_discrete_sequence=['#ff6b6b', '#51cf66', '#339af0'])
fig.update_traces(textposition='inside', textinfo='percent+label')
st.plotly_chart(fig)

# Enhanced Interactive Quiz
st.markdown("## 🎯 Quick Comedy Quiz!")
with st.form("quiz_form"):
    question = st.radio(
        "What comes first in TDD?",
        ["The chicken 🐔", "The egg 🥚", "The test ✅", "The code 💻"]
    )
    submit_button = st.form_submit_button("Check Answer!")
    
    if submit_button:
        if question == "The test ✅":
            st.success("🎉 Correct! You're a TDD natural! Here's your virtual trophy 🏆")
        else:
            st.error("Almost! Remember: In TDD, we always start with the test - it's like writing the punchline first! 😉")

# Enhanced Test Status Simulator
st.markdown("### 🔧 Test Status Simulator")
cols = st.columns(3)

test_counts = {'passed': 0, 'failed': 0, 'refactored': 0}

with cols[0]:
    if st.button("Run Test 🏃"):
        test_counts['passed'] += 1
        st.metric("Tests Passed", f"{test_counts['passed']}", "+1")
        
with cols[1]:
    if st.button("Break Code 💔"):
        test_counts['failed'] += 1
        st.metric("Tests Failed", f"{test_counts['failed']}", "+1")
        
with cols[2]:
    if st.button("Refactor 🔄"):
        test_counts['refactored'] += 1
        st.metric("Code Improved", f"{test_counts['refactored']}", "+1")
        st.balloons()

# Fun progress tracker
if st.button("Debug Progress 🐛"):
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    for i in range(100):
        progress_bar.progress(i + 1)
        if i < 30:
            status_text.text("🔍 Searching for bugs...")
        elif i < 60:
            status_text.text("🐛 Catching bugs...")
        elif i < 90:
            status_text.text("🔨 Squashing bugs...")
        else:
            status_text.text("✨ Polishing code...")
    
    st.success("🎉 Bug successfully debugged! Time for a coffee break! ☕")

st.info("""
💡 **Pro Tip**: TDD is like stand-up comedy:
- You write your material (tests) first
- Practice makes perfect
- Sometimes you bomb, but you learn from it
- The audience (your code) will tell you if it works!
""")