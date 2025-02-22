import streamlit as st
import plotly.graph_objects as go
import numpy as np
from PIL import Image
import plotly.express as px

st.title("Nuclear Reactions in Motion: A Visual Journey Through Fission and Fusion")

# Add an engaging introduction
st.markdown("""
<div style='background-color: #f0f2f6; padding: 20px; border-radius: 10px;'>
    <h4>Welcome to the Interactive Nuclear Physics Lab! 🔬</h4>
    Explore the fascinating world of nuclear reactions through interactive visualizations.
    Adjust parameters and watch how atoms split and fuse in real-time!
</div>
""", unsafe_allow_html=True)

# Interactive tabs with custom styling
tab1, tab2 = st.tabs(["💥 Nuclear Fission", "🌟 Nuclear Fusion"])

with tab1:
    st.header("Nuclear Fission: Splitting Atoms")
    
    col1, col2 = st.columns([2, 1])
    with col1:
        time = st.slider("Animate Fission Process", 0, 100, 50, 
                        help="Move the slider to see the atom split!")
    with col2:
        energy_released = time * 2  # Simplified energy calculation
        st.metric("Energy Released (MeV)", f"{energy_released:.1f}")
    
    t = np.linspace(0, 2*np.pi, 100)
    nucleus_x = np.cos(t)
    nucleus_y = np.sin(t)
    split_factor = time/100
    
    fig_fission = go.Figure()
    
    # Enhanced visualization with more particles
    fig_fission.add_trace(go.Scatter(
        x=nucleus_x*split_factor + 1,
        y=nucleus_y,
        mode='markers',
        name='Fragment 1',
        marker=dict(size=10, color='red', symbol='circle')
    ))
    
    fig_fission.add_trace(go.Scatter(
        x=nucleus_x*split_factor - 1,
        y=nucleus_y,
        mode='markers',
        name='Fragment 2',
        marker=dict(size=10, color='blue', symbol='circle')
    ))
    
    # Add neutrons
    if time > 50:
        for i in range(3):
            angle = np.random.random() * 2 * np.pi
            fig_fission.add_trace(go.Scatter(
                x=[0, 2*np.cos(angle)],
                y=[0, 2*np.sin(angle)],
                mode='lines+markers',
                name='Neutron',
                line=dict(color='green', width=1),
                marker=dict(size=6, color='green')
            ))
    
    fig_fission.update_layout(
        title="Nuclear Fission Process",
        xaxis_range=[-3, 3],
        yaxis_range=[-2, 2],
        height=400,
        plot_bgcolor='rgba(240,242,246,0.8)',
        showlegend=True
    )
    
    st.plotly_chart(fig_fission, use_container_width=True)

with tab2:
    st.header("Nuclear Fusion: Joining Atoms")
    
    col1, col2 = st.columns([2, 1])
    with col1:
        temp = st.slider("Temperature (Million °C)", 0, 150, 100,
                        help="Increase temperature to overcome nuclear forces!")
    with col2:
        fusion_efficiency = min(100, temp/1.5)
        st.metric("Fusion Efficiency", f"{fusion_efficiency:.1f}%")
    
    distance = max(2 - (temp/50), 0.5)
    t = np.linspace(0, 2*np.pi, 100)
    
    fig_fusion = go.Figure()
    
    # Enhanced fusion visualization
    fig_fusion.add_trace(go.Scatter(
        x=np.cos(t)*0.5 - distance,
        y=np.sin(t)*0.5,
        mode='markers',
        name='Deuterium',
        marker=dict(size=8, color='orange', symbol='circle')
    ))
    
    fig_fusion.add_trace(go.Scatter(
        x=np.cos(t)*0.5 + distance,
        y=np.sin(t)*0.5,
        mode='markers',
        name='Tritium',
        marker=dict(size=8, color='purple', symbol='circle')
    ))
    
    # Add plasma effect when temperature is high
    if temp > 100:
        fig_fusion.add_trace(go.Scatter(
            x=np.cos(t)*2,
            y=np.sin(t)*2,
            mode='markers',
            name='Plasma',
            marker=dict(size=2, color='yellow'),
            opacity=0.3
        ))
    
    fig_fusion.update_layout(
        title=f"Fusion Process at {temp} Million °C",
        xaxis_range=[-3, 3],
        yaxis_range=[-2, 2],
        height=400,
        plot_bgcolor='rgba(240,242,246,0.8)',
        showlegend=True
    )
    
    st.plotly_chart(fig_fusion, use_container_width=True)

# Enhanced energy comparison
st.header("Energy Output Comparison")
reaction_type = st.selectbox("Select Reaction Type", ["Fission", "Fusion"])

energy_data = {
    "Fission": {"energy": 200, "color": "red", "icon": "💥"},
    "Fusion": {"energy": 17.6, "color": "blue", "icon": "🌟"}
}

fig_energy = go.Figure(go.Bar(
    x=[f"{reaction_type} {energy_data[reaction_type]['icon']}"],
    y=[energy_data[reaction_type]["energy"]],
    marker_color=[energy_data[reaction_type]["color"]]
))

fig_energy.update_layout(
    title=f"Energy Output of {reaction_type} (MeV)",
    yaxis_title="Energy (MeV)",
    height=400,
    plot_bgcolor='rgba(240,242,246,0.8)'
)

st.plotly_chart(fig_energy, use_container_width=True)

# Enhanced fact display
facts = [
    "🌞 The Sun fuses 620 million metric tons of hydrogen every second!",
    "⚡ One uranium fission event releases 200 MeV of energy!",
    "🔥 Nuclear fusion requires temperatures hotter than the Sun's core!",
    "🏸 The first nuclear reactor was built under a squash court in Chicago!"
]

st.sidebar.title("Did You Know? 🤔")
st.sidebar.info(np.random.choice(facts))