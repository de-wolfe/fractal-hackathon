import streamlit as st
import random

st.title("🎯 Unit Testing Quiz Adventure ✅")

# Add some styling
st.markdown("""
    <style>
    .main {
        background-color: #f5f5f5;
    }
    .stRadio > label {
        padding: 10px;
        background-color: #ffffff;
        border-radius: 5px;
        margin: 5px 0;
    }
    </style>
    """, unsafe_allow_html=True)

# Introduction with fun context
st.markdown("""
### Welcome to the Unit Testing Challenge! 🚀
Test your knowledge and become a testing superhero! Each correct answer brings you closer to 
becoming a Unit Testing Master.
""")

# Question 1 with enhanced presentation
st.markdown("### 🤔 Question 1:")
q1 = st.radio(
    "What's the main purpose of unit testing?",
    [
        "To make the code run faster 🏃‍♂️",
        "To test individual components/units of code in isolation 🔍",
        "To check if the UI looks good 🎨",
        "To deploy code to production 🚀"
    ]
)

# Question 2 with better visualization
st.markdown("### 🎯 Question 2:")
st.markdown("The famous AAA pattern is crucial in unit testing. Can you identify its components?")
q2 = st.multiselect(
    "Select the parts of the AAA pattern:",
    [
        "Analyze 📊",
        "Arrange 🔧",
        "Act 🎭",
        "Assert ✅",
        "Authenticate 🔑"
    ]
)

# Fun encouragement messages
encouragement_messages = [
    "You're doing great! 🌟",
    "Keep going, testing champion! 💪",
    "You've got this! 🎯",
    "Almost there! 🚀"
]

if st.button("📝 Check My Answers!", help="Click to see how well you did!"):
    score = 0
    feedback = ""
    
    # Check Q1 with detailed explanation
    if q1 == "To test individual components/units of code in isolation 🔍":
        score += 1
        feedback += """
        ✅ **Question 1: Excellent!**
        - You understand that unit testing is about isolating and testing individual components
        - This helps catch bugs early in the development process
        \n\n"""
    else:
        feedback += """
        ❌ **Question 1: Not quite right**
        - Unit testing is specifically about testing individual code components in isolation
        - This helps us identify issues at the smallest possible level
        \n\n"""
    
    # Check Q2 with detailed feedback
    correct_aaa = {"Arrange 🔧", "Act 🎭", "Assert ✅"}
    if set(q2) == correct_aaa:
        score += 1
        feedback += """
        ✅ **Question 2: Perfect!**
        - You've mastered the AAA pattern:
          * Arrange: Set up your test conditions
          * Act: Execute the code being tested
          * Assert: Verify the results
        \n\n"""
    else:
        feedback += """
        ❌ **Question 2: Let's review**
        - The AAA pattern consists of:
          * Arrange: Prepare your test environment
          * Act: Run the code you're testing
          * Assert: Check if the results match expectations
        \n\n"""
    
    # Display results with enhanced styling
    st.balloons()
    st.markdown(f"### Your Score: {score}/2 {'🌟' * score}")
    st.markdown(feedback)
    st.markdown(f"_{random.choice(encouragement_messages)}_")

# Additional resources
with st.expander("📚 Want to Learn More About Unit Testing?"):
    st.markdown("""
    * Write tests that focus on one thing at a time
    * Keep your tests simple and readable
    * Follow the AAA pattern consistently
    * Test both valid and invalid scenarios
    * Keep your tests independent of each other
    """)