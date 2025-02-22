import streamlit as st
import numpy as np
import plotly.graph_objects as go
import pandas as pd
import plotly.express as px
import seaborn as sns

st.title("🌈 The Rainbow of Radiation: Visualizing Nuclear Energy Wavelengths")

# Add custom CSS for better visual appeal
st.markdown("""
    <style>
    .stMarkdown {
        font-size: 18px;
        line-height: 1.6;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
Embark on an exciting journey through the electromagnetic spectrum! 
Discover how different types of radiation interact with our world, from the powerful gamma rays 
to the gentle infrared waves. 🚀
""")

# Create two columns for better layout
col1, col2 = st.columns([2, 1])

# Create wavelength slider with better formatting
with col1:
    wavelength = st.slider(
        "🔍 Adjust wavelength (picometers)", 
        0.0001, 1000.0, 100.0,
        help="Drag the slider to see how wavelength affects radiation properties"
    )
    energy = 1240 / wavelength  # E = hc/λ simplified

# Enhanced radiation type selector
with col2:
    radiation_type = st.selectbox(
        "📊 Select radiation type:",
        ["Gamma Rays", "X-Rays", "Ultraviolet", "Visible Light", "Infrared"]
    )

# Updated information dictionary with enhanced visuals
radiation_info = {
    "Gamma Rays": {
        "wavelength": "< 0.01 picometers",
        "energy": "> 100 keV",
        "description": "🔥 Highest energy radiation, produced in nuclear reactions",
        "color": "rgba(128, 0, 128, 0.6)"
    },
    "X-Rays": {
        "wavelength": "0.01 - 10 picometers",
        "energy": "0.1 - 100 keV",
        "description": "🏥 Used in medical imaging and astronomy",
        "color": "rgba(0, 0, 255, 0.6)"
    },
    "Ultraviolet": {
        "wavelength": "10 - 380 picometers",
        "energy": "3.3 - 124 eV",
        "description": "☀️ Causes sunburns, used in sterilization",
        "color": "rgba(238, 130, 238, 0.6)"
    },
    "Visible Light": {
        "wavelength": "380 - 700 picometers",
        "energy": "1.7 - 3.3 eV",
        "description": "👁️ The light we can see with our eyes",
        "color": "rgba(0, 255, 0, 0.6)"
    },
    "Infrared": {
        "wavelength": "> 700 picometers",
        "energy": "< 1.7 eV",
        "description": "🌡️ Felt as heat, used in thermal imaging",
        "color": "rgba(255, 0, 0, 0.6)"
    }
}

# Enhanced information card
st.markdown(f"""
### ⚡ {radiation_type}
""")
col3, col4 = st.columns(2)
with col3:
    st.markdown(f"""
    - **Wavelength:** {radiation_info[radiation_type]['wavelength']}
    - **Energy:** {radiation_info[radiation_type]['energy']}
    """)
with col4:
    st.markdown(f"""
    - **Key Feature:** {radiation_info[radiation_type]['description']}
    """)

# Enhanced spectrum visualization
x = np.linspace(0, 1000, 100)
y = np.exp(-((x - wavelength)**2)/(2*50**2))

fig = go.Figure()
fig.add_trace(go.Scatter(
    x=x, 
    y=y,
    fill='tozeroy',
    fillcolor=radiation_info[radiation_type]['color'],
    line_color=radiation_info[radiation_type]['color']
))

fig.update_layout(
    title="Interactive Radiation Spectrum",
    xaxis_title="Wavelength (picometers)",
    yaxis_title="Relative Intensity",
    showlegend=False,
    plot_bgcolor='rgba(240,240,240,0.5)',
    paper_bgcolor='rgba(0,0,0,0)'
)

st.plotly_chart(fig, use_container_width=True)

# Enhanced energy calculator
st.markdown("### ⚛️ Energy Calculator")
col5, col6 = st.columns([2, 1])
with col5:
    user_wavelength = st.number_input(
        "Enter wavelength (picometers):", 
        0.0001, 1000.0, 100.0,
        format="%.4f"
    )
with col6:
    calculated_energy = 1240 / user_wavelength
    st.metric("Energy (eV)", f"{calculated_energy:.2f}")

# Enhanced fact generator
facts = [
    "💡 Nuclear power plants use controlled nuclear reactions to generate electricity!",
    "🧪 Marie Curie won Nobel Prizes in both Physics and Chemistry for her work on radioactivity!",
    "☀️ The sun is powered by nuclear fusion reactions!",
    "🏥 Nuclear medicine uses radiation to diagnose and treat diseases!",
    "🔍 Some smoke detectors contain small amounts of radioactive material!"
]

if st.button("🎲 Generate Random Nuclear Fact!"):
    st.info(np.random.choice(facts))