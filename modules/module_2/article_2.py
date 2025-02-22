import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import plotly.graph_objects as go
import plotly.express as px

# Title and styling
st.markdown("""
<style>
.big-font {
    font-size:30px !important;
    color: #1E88E5;
    font-weight: bold;
    margin-bottom: 30px;
}
.riddle {
    padding: 20px;
    background-color: #f0f8ff;
    border-radius: 10px;
    margin: 20px 0;
    box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
}
.hint {
    font-style: italic;
    color: #666;
    font-size: 0.9em;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="big-font">🌟 The Quantum Puzzle: Why Does Light Play Hide and Seek?</p>', unsafe_allow_html=True)

# Interactive tabs
tab1, tab2, tab3 = st.tabs(["Quantum Riddles", "Wave-Particle Magic", "Quantum Quiz"])

with tab1:
    st.markdown("""
    <div class='riddle'>
        🤔 Riddle me this:
        <br>I am here and there, wave and dot
        <br>Look at me close, and I'm maybe not
        <br>What am I?
    </div>
    """, unsafe_allow_html=True)

with tab2:
    st.subheader("🌊 Wave or Particle? You Decide!")
    wave_particle = st.slider("Adjust the quantum behavior", 0.0, 1.0, 0.5)
    
    # Create interactive plotly visualization
    x = np.linspace(0, 10, 1000)
    wave = np.sin(x) * np.exp(-x/10)
    particles_x = np.linspace(0, 10, 50)
    particles_y = np.random.normal(size=50)

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=wave * wave_particle,
                            mode='lines',
                            name='Wave',
                            line=dict(color='blue', width=2)))
    fig.add_trace(go.Scatter(x=particles_x, y=particles_y * (1-wave_particle),
                            mode='markers',
                            name='Particles',
                            marker=dict(color='red', size=8)))
    
    fig.update_layout(title='Wave-Particle Duality Visualization',
                     height=400,
                     showlegend=True)
    st.plotly_chart(fig)

with tab3:
    st.subheader("🎯 Quantum Challenge")
    
    col1, col2 = st.columns(2)
    
    with col1:
        riddle_answer = st.text_input("What particle is both a wave and a particle, and helps you see?")
        if riddle_answer.lower() == "photon":
            st.success("🎉 Brilliant! The photon is indeed the quantum of light!")
        elif riddle_answer:
            st.error("Not quite! Hint: I'm the smallest unit of light.")
    
    with col2:
        quiz_question = st.radio(
            "What happens to a quantum particle when we observe it?",
            ["It disappears", "It collapses into a definite state", "It multiplies", "Nothing changes"]
        )
        if quiz_question == "It collapses into a definite state":
            st.success("🎯 Correct! This is the wave function collapse.")
        elif quiz_question:
            st.error("Think about the observer effect in quantum mechanics!")

# Interactive fact explorer
st.markdown("### 🤯 Quantum Facts Explorer")
facts = {
    "Wave-Particle Duality": "Light can behave as both a wave and a particle",
    "Quantum Superposition": "Quantum particles can be in multiple states at once",
    "Quantum Entanglement": "Particles can be instantly connected regardless of distance",
    "Observer Effect": "The act of observation affects quantum systems"
}

selected_fact = st.selectbox("Choose a quantum concept to explore:", list(facts.keys()))
st.info(facts[selected_fact])

# Easter egg
if st.button("🎁 Discover a Quantum Secret"):
    st.balloons()
    st.markdown("*The universe is stranger than we can imagine, but not stranger than we can explore!*")