import streamlit as st
import random
import numpy as np

st.title("✨ Chemistry Visual Concepts Explorer")

# Create a custom container with better styling
st.markdown("""
    <style>
    .question-container {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0;
    }
    </style>
""", unsafe_allow_html=True)

# Introduction
st.markdown("### Let's explore some fascinating chemistry concepts! 🔬")
st.write("Test your knowledge about atomic behavior and chemical bonding.")

# Question 1 with interactive visualization
st.markdown('<div class="question-container">', unsafe_allow_html=True)
st.subheader("📊 Electron Energy Transitions")

# Simple animation effect using alternating colors
energy_levels = np.linspace(1, 5, 5)
if 'color_index' not in st.session_state:
    st.session_state.color_index = 0

colors = ['#FF9999', '#99FF99', '#9999FF']
current_color = colors[st.session_state.color_index % len(colors)]
st.session_state.color_index += 1

# Create simple visualization
for level in energy_levels:
    st.markdown(f'<div style="background-color: {current_color}; height: 10px; width: {level*20}%;"></div>', 
                unsafe_allow_html=True)

q1 = st.radio(
    "When electrons move between energy levels in an atom, what happens?",
    ["Emit light of specific wavelengths",
     "Always remain neutral",
     "Only move to lower energy levels",
     "Change atomic number"]
)

if q1:
    if q1 == "Emit light of specific wavelengths":
        st.success("🎉 Correct! When electrons move between energy levels, they can emit or absorb light of specific wavelengths.")
        st.markdown("*Fun fact: This is why fireworks have different colors!*")
    else:
        st.error("Try again! Think about how electrons interact with light.")
st.markdown('</div>', unsafe_allow_html=True)

# Question 2 with interactive elements
st.markdown('<div class="question-container">', unsafe_allow_html=True)
st.subheader("🔗 Chemical Bonding Analysis")

# Display image with enhanced styling
st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/7/78/Chemical_bond.svg/320px-Chemical_bond.svg.png", 
         caption="Chemical Bonding Visualization",
         use_column_width=True)

q2 = st.selectbox(
    "What type of chemical bonding is shown in the diagram above?",
    ["Select your answer...", "Ionic bonding", "Covalent bonding", "Metallic bonding", "Hydrogen bonding"]
)

if q2 != "Select your answer...":
    if q2 == "Covalent bonding":
        st.success("🌟 Excellent! The sharing of electrons between atoms shows covalent bonding.")
        st.markdown("*Tip: Covalent bonds are crucial in organic chemistry!*")
    else:
        st.error("Not quite! Look at how the electrons are being shared between atoms.")
st.markdown('</div>', unsafe_allow_html=True)

# Interactive score calculation
if st.button("📊 Show My Results"):
    score = 0
    if q1 == "Emit light of specific wavelengths":
        score += 1
    if q2 == "Covalent bonding":
        score += 1
    
    # Create an engaging score display
    st.balloons()
    st.markdown(f"""
        <div style='background-color: #e6f3ff; padding: 20px; border-radius: 10px;'>
            <h3>Your Score: {score}/2 ({score/2*100}%)</h3>
            <p>{'🌟 ' * score + '⭐ ' * (2-score)}</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Provide encouraging feedback
    if score == 2:
        st.markdown("### 🎉 Perfect Score! You're a chemistry master!")
    elif score == 1:
        st.markdown("### 👍 Good effort! Review the concepts and try again!")
    else:
        st.markdown("### 📚 Keep learning! Every attempt helps you improve!")