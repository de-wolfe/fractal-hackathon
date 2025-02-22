import streamlit as st
import plotly.graph_objects as go
import numpy as np
from PIL import Image
import plotly.express as px

st.title("🌌 Entanglement's Enigma: How Do Particles Dance Together Miles Apart? 🕺💃")

# Custom CSS for better styling
st.markdown("""
    <style>
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 10px;
        padding: 10px 20px;
    }
    .stMarkdown {
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

# Enhanced riddle introduction with animation
st.write("""
## A Quantum Riddle for You...

*Two dancers never met, yet move as one,*  
*Miles apart, their cosmic dance has begun.*  
*When one spins up, the other spins down,*  
*What quantum mystery wears this crown?*
""")

# Interactive answer reveal with enhanced feedback
if st.button("🎭 Reveal the Answer!", key="reveal"):
    st.success("**Quantum Entanglement!** When particles become entangled, they behave like these mysterious dancers!")
    st.write("Let's explore this fascinating phenomenon!")

# Enhanced interactive particle simulation
st.subheader("🎲 Play with Entangled Particles!")

col1, col2 = st.columns(2)
with col1:
    distance = st.slider("Distance between particles (light years)", 0.0, 100.0, 10.0)
with col2:
    particle_color = st.color_picker("Choose particle color", "#1f77b4")

# Create enhanced visualization
t = np.linspace(0, 2*np.pi, 100)
fig = go.Figure()

# Add particles with enhanced styling
fig.add_trace(go.Scatter(
    x=[0], y=[0],
    mode='markers+text',
    name='Particle 1',
    marker=dict(size=20, color=particle_color, symbol='circle'),
    text=['P1'],
    textposition='top center'
))

fig.add_trace(go.Scatter(
    x=[distance], y=[0],
    mode='markers+text',
    name='Particle 2',
    marker=dict(size=20, color=particle_color, symbol='circle'),
    text=['P2'],
    textposition='top center'
))

# Add connecting line to show entanglement
fig.add_trace(go.Scatter(
    x=[0, distance], y=[0, 0],
    mode='lines',
    line=dict(color='rgba(128, 128, 128, 0.5)', dash='dot'),
    showlegend=False
))

fig.update_layout(
    title=dict(
        text=f"Entangled Particles {distance} Light Years Apart",
        x=0.5,
        xanchor='center'
    ),
    xaxis_title="Distance (Light Years)",
    yaxis_title="State",
    height=400,
    template="plotly_dark",
    hovermode='closest'
)

st.plotly_chart(fig, use_container_width=True)

# Enhanced state measurement interface
st.subheader("🔄 Quantum Measurement Experiment")
col1, col2 = st.columns(2)

with col1:
    if st.button("Measure Particle 1", key="measure"):
        result = np.random.choice(['UP ⬆️', 'DOWN ⬇️'])
        st.write(f"Particle 1 measured: {result}")
        with col2:
            st.write(f"Particle 2 instantly becomes: {'DOWN ⬇️' if result == 'UP ⬆️' else 'UP ⬆️'}")
            st.markdown("*Instantaneous quantum correlation!*")

# Enhanced fact display
facts = [
    "Entanglement is what Einstein called 'spooky action at a distance'! 👻",
    "Quantum computers use entanglement to perform calculations! 🖥️",
    "Entangled particles can be used for ultra-secure communication! 🔐",
    "Scientists have entangled particles over 1,200 kilometers apart! 🌍"
]

st.subheader("🎲 Quantum Facts")
if st.button("Reveal Random Quantum Fact!", key="fact"):
    st.info(np.random.choice(facts))

# Enhanced final riddle
st.markdown("""
---
## 🤔 One Last Riddle...
*I'm faster than light, yet carry no mass,*  
*Through entanglement's dance, all distance I pass.*  
*What am I?*
""")

options = ['Information', 'Quantum Correlation', 'Light', 'Energy']
answer = st.selectbox('Select your answer:', options)

if answer == 'Quantum Correlation':
    st.balloons()
    st.success("🎉 Correct! Quantum correlations appear to act instantaneously across any distance!")
elif answer:
    st.error("Not quite! Think about what connects entangled particles...")

st.markdown("""
---
*Remember: The quantum world is strange, but that's what makes it beautiful!* ✨
""")