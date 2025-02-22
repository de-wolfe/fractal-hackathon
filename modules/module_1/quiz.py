import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Custom styling
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stRadio > label {
        background-color: #f0f2f6;
        padding: 10px;
        border-radius: 5px;
        margin: 5px 0;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("⚛️ Nuclear Energy Assessment")

# Introduction with visual explanation
st.markdown("""
    Welcome to the Nuclear Energy Assessment! Test your knowledge about nuclear power 
    and how it works. Each correct answer will help build your understanding of this 
    important energy source.
""")

# Progress tracking
progress = st.progress(0)

# Question 1 with visual enhancement
st.subheader("🔄 Question 1: Nuclear Fission Process")
st.write("In nuclear fission, what happens to the atomic nucleus?")

q1 = st.radio(
    "Select the best answer:",
    [
        "The nucleus combines with another nucleus",
        "The nucleus splits into smaller nuclei, releasing energy",
        "The nucleus remains unchanged",
        "The nucleus loses electrons only"
    ],
    help="Think about the meaning of 'fission' - splitting or breaking apart"
)

# Question 2 with interactive layout
st.subheader("🏭 Question 2: Nuclear Power Plant Components")
st.write("Match each component to its function in a nuclear power plant:")

# Create two columns with better visual separation
col1, col2 = st.columns([1, 2])

with col1:
    st.markdown("""
    **Components:**
    - 🔴 Reactor Core
    - 🔵 Cooling Tower
    - 🟡 Turbine
    """)

with col2:
    q2_1 = st.selectbox(
        "What component contains the nuclear fuel and controls the fission reaction?",
        ["Select", "Reactor Core", "Cooling Tower", "Turbine"]
    )
    
    q2_2 = st.selectbox(
        "What component removes excess heat from the system?",
        ["Select", "Reactor Core", "Cooling Tower", "Turbine"]
    )

# Interactive scoring system
if st.button("📝 Check My Answers", help="Click to see how well you did!"):
    score = 0
    
    # Question 1 evaluation
    if q1 == "The nucleus splits into smaller nuclei, releasing energy":
        score += 1
        st.success("✅ Question 1: Excellent! Nuclear fission involves splitting the nucleus.")
    else:
        st.error("❌ Question 1: Not quite. Remember, fission means splitting.")
        
    # Question 2 evaluation
    if q2_1 == "Reactor Core" and q2_2 == "Cooling Tower":
        score += 1
        st.success("✅ Question 2: Perfect! You understand the plant components.")
    else:
        st.error("❌ Question 2: Review the function of each component.")
    
    # Final score display with visual feedback
    progress.progress(score/2)
    st.balloons() if score == 2 else None
    
    col1, col2 = st.columns([1, 2])
    with col1:
        st.metric("Final Score", f"{score}/2")
    with col2:
        if score == 2:
            st.markdown("🌟 **Excellent work! You're a nuclear energy expert!**")
        elif score == 1:
            st.markdown("📚 **Good start! Review the material and try again.**")
        else:
            st.markdown("💡 **Keep learning! The concepts will become clearer with practice.**")

# Additional resources
with st.expander("📚 Want to Learn More?"):
    st.markdown("""
    - Nuclear fission is the process of splitting atomic nuclei
    - Nuclear power plants use this process to generate electricity
    - Safety systems like cooling towers are crucial for operation
    """)