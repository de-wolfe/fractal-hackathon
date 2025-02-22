import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import plotly.graph_objects as go
import plotly.express as px

st.title("🐱 Schrödinger's Riddle: When is a Cat Both Dead and Alive? 🤔")

# Add a fun animated introduction
st.markdown("""
<div style='background-color: #f0f2f6; padding: 20px; border-radius: 10px;'>
## A Quantum Mystery in Riddle Form

*Riddle me this:*
> In a box that none can see,  
> Lives (or doesn't) a mystery.  
> Both alive and dead it stays,  
> Until someone lifts the haze.  
> What am I?
</div>
""", unsafe_allow_html=True)

# Interactive box with improved visualization
col1, col2 = st.columns(2)
with col1:
    if st.button("🎁 Open the Mystery Box", key='box'):
        st.snow()
        st.markdown("### You've collapsed the wave function!")
        st.write("The cat is now either alive 😺 or dead 💀 - but not both!")

# Improved probability visualization
st.markdown("### 🎲 Quantum Probability Explorer")
probability = st.slider("What's the chance of finding the cat alive?", 0.0, 1.0, 0.5)

# Create an interactive plotly visualization
x = np.linspace(0, 10, 100)
wave = np.sin(x) * np.exp(-x/5)

fig = go.Figure()
fig.add_trace(go.Scatter(
    x=x, y=wave,
    fill='tonexty',
    fillcolor='rgba(128, 0, 128, 0.3)',
    line=dict(color='purple', width=2),
    name='Quantum State'
))
fig.update_layout(
    title='Interactive Quantum Superposition Wave',
    xaxis_title='Space',
    yaxis_title='Probability Amplitude',
    hovermode='x'
)
st.plotly_chart(fig)

# Enhanced interactive quiz
st.markdown("### 🧩 Quantum Challenge")
with st.form("quantum_quiz"):
    answer = st.text_input("What happens when you observe a quantum system?")
    submitted = st.form_submit_button("Check Answer")
    if submitted:
        if "collapse" in answer.lower() or "measurement" in answer.lower():
            st.success("🌟 Brilliant! The wave function collapses upon observation!")
            st.balloons()
        else:
            st.error("Not quite! Hint: Think about what happens to the quantum superposition...")

# Improved tabs with more engaging content
st.markdown("### 🔍 Quantum Concepts")
tab1, tab2, tab3 = st.tabs(["🤔 The Paradox", "🔬 The Science", "💡 The Resolution"])

with tab1:
    st.markdown("""
    ### The Famous Cat Paradox
    - 📦 Cat in a sealed box
    - ⚛️ Quantum trigger mechanism
    - 🤯 Superposition of states
    """)

with tab2:
    st.markdown("""
    ### The Quantum Science
    - 🌊 Wave function describes the system
    - 🎲 Probability governs outcomes
    - 👁️ Observation affects reality
    """)

with tab3:
    st.markdown("""
    ### The Resolution
    - 📊 Measurement collapses possibilities
    - 🎯 One definite outcome emerges
    - 🤓 Copenhagen interpretation
    """)

# Enhanced quantum state generator
st.markdown("### 🎮 Quantum State Simulator")
if st.button("Generate Random Quantum State", key='generator'):
    state = np.random.choice(["😺 ALIVE", "💀 DEAD"], p=[probability, 1-probability])
    st.balloons()
    st.markdown(f"<h1 style='text-align: center; color: purple;'>{state}</h1>", unsafe_allow_html=True)

st.markdown("""
---
<div style='background-color: #e6e6fa; padding: 15px; border-radius: 10px;'>
> *"The more precisely the position is determined, the less precisely the momentum is known in this instant, and vice versa."* - Werner Heisenberg
</div>
""", unsafe_allow_html=True)