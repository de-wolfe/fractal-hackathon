import streamlit as st
import pandas as pd
import plotly.express as px
import random
from PIL import Image
import numpy as np

# Title with custom styling
st.markdown("""
    <h1 style='text-align: center; color: #1E88E5;'>
        🎭 Mocking Around: A Comedy of Test Doubles and Jest-ers
    </h1>
    """, unsafe_allow_html=True)

st.markdown("""
<div style='background-color: #f0f2f6; padding: 20px; border-radius: 10px;'>
    <h2 style='text-align: center;'>🤡 Welcome to the Unit Testing Comedy Club!</h2>
    <p style='text-align: center; font-style: italic;'>Where the jokes are tested, but the tests are a joke! <em>ba dum tss</em></p>
</div>
""", unsafe_allow_html=True)

# Create two columns for layout
col1, col2 = st.columns([2, 1])

# Interactive joke section with improved styling
with col1:
    if st.button("😂 Generate Test-Related Dad Joke", key='joke_button'):
        jokes = [
            "Why did the mock object go to therapy? It had identity issues!",
            "What's a unit tester's favorite dance? The test-two step!",
            "Why did the stub feel lonely? Because it was just a dummy!",
            "What do you call a fake test double? A mock-ery!",
            "Why did the test fail? Because it couldn't handle the mock pressure!"
        ]
        st.success(random.choice(jokes))

# Interactive Test Double Types with improved visuals
st.markdown("## 🎭 The Cast of Test Doubles")

test_doubles = {
    "Dummy": ["Just fills space (like my ex's Instagram posts)", "🤖"],
    "Stub": ["Returns fixed values (as reliable as pizza delivery times)", "🎯"],
    "Spy": ["Records method calls (stalker much?)", "🕵️"],
    "Mock": ["Verifies behavior (like your mom checking your room)", "🎭"],
    "Fake": ["Working implementation (but not as fake as reality TV)", "🎪"]
}

selected_double = st.selectbox("Select your favorite test double:", list(test_doubles.keys()))
st.markdown(f"""
    <div style='background-color: #e3f2fd; padding: 15px; border-radius: 5px;'>
        <h3>{test_doubles[selected_double][1]} {selected_double}</h3>
        <p>{test_doubles[selected_double][0]}</p>
    </div>
""", unsafe_allow_html=True)

# Enhanced visualization of test coverage
st.markdown("## 📊 The 'Coverage' Comedy Show")

coverage_data = pd.DataFrame({
    'Component': ['Unit Tests', 'Integration Tests', 'End-to-End Tests', 'Dad Jokes'],
    'Coverage': [80, 60, 40, 100],
    'Difficulty': [2, 3, 4, 1]
})

fig = px.scatter(coverage_data, x='Difficulty', y='Coverage',
                size='Coverage', color='Component',
                title='Test Coverage vs Difficulty (Warning: May Contain Traces of Humor)')
fig.update_layout(
    plot_bgcolor='rgba(240,242,246,0.8)',
    paper_bgcolor='rgba(240,242,246,0.8)',
)
st.plotly_chart(fig, use_container_width=True)

# Enhanced interactive testing quiz
st.markdown("## 🎯 The 'Mock' Quiz")

with st.form("quiz_form"):
    question = st.radio(
        "What's the main purpose of mocking in unit tests?",
        [
            "To make fun of other developers' code",
            "To isolate the code being tested",
            "To waste time in meetings",
            "To increase coffee consumption"
        ]
    )
    submit_button = st.form_submit_button("Submit Answer")
    
    if submit_button:
        if question == "To isolate the code being tested":
            st.balloons()
            st.success("🎉 Correct! You're officially a Jest-er! 🎭")
        else:
            st.error("❌ Wrong! But hey, at least you're funny! 😄")

# Enhanced testing wisdom generator
st.markdown("## 🎮 Testing Wisdom Generator")

if st.button("Generate Testing Wisdom", key='wisdom_button'):
    wisdoms = [
        "Remember: If at first you don't succeed, call it a 'known issue'",
        "The best kind of test is the one that passes... eventually",
        "Unit tests are like jokes - if you have to explain them, they're bad",
        "Debug like nobody's watching, test like everybody's watching",
        "Keep calm and blame the test environment"
    ]
    st.info(random.choice(wisdoms))

st.markdown("""
---
<div style='text-align: center; font-style: italic; color: #666;'>
    Remember: In unit testing, as in comedy, timing is everything! ⏰
</div>
""", unsafe_allow_html=True)