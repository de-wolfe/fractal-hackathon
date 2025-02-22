import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from PIL import Image
import numpy as np
import plotly.express as px

st.title("🎯 Inside the Reactor: Color-Coded Guide to Nuclear Power Plant Components")

# Enhanced styling with custom CSS
st.markdown("""
    <style>
    .highlight {
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0;
    }
    </style>
""", unsafe_allow_html=True)

# Interactive sidebar with enhanced styling
st.sidebar.title("Navigation 🧭")
section = st.sidebar.radio("Go to:", 
    ["Reactor Overview", "Key Components", "Interactive Diagram"],
    key="nav_radio")

if section == "Reactor Overview":
    st.write("""
    ## How Nuclear Power Works 🔋
    Nuclear power plants harness the energy released during nuclear fission to generate electricity.
    Let's explore the key components through an interactive color-coded guide!
    """)
    
    col1, col2 = st.columns(2)
    with col1:
        with st.expander("What is Nuclear Fission? 💥", expanded=True):
            st.write("""
            Nuclear fission occurs when uranium atoms split, releasing energy in the form of heat.
            This heat is used to create steam, which drives turbines to generate electricity.
            """)
    
    with col2:
        with st.expander("Safety Measures ⚡", expanded=True):
            st.write("""
            Multiple safety systems and barriers ensure safe operation:
            - Multiple containment layers
            - Emergency cooling systems
            - Redundant safety controls
            """)

elif section == "Key Components":
    components_df = pd.DataFrame({
        'Component': ['Reactor Core', 'Control Rods', 'Steam Generator', 'Containment Building'],
        'Function': ['Houses nuclear fuel and reaction', 'Controls reaction rate', 'Converts water to steam', 'Safety barrier'],
        'Color Code': ['🔴 Red', '🟣 Purple', '🔵 Blue', '⚪ Gray'],
        'Safety Level': [3, 4, 2, 5]
    })
    
    # Enhanced table visualization
    st.plotly_chart(px.bar(components_df, x='Component', y='Safety Level',
                          color='Component', title='Component Safety Levels'))
    
    st.dataframe(components_df.style.highlight_max(subset=['Safety Level']))
    
    selected_component = st.selectbox(
        "Select a component to learn more:",
        components_df['Component']
    )
    
    component_info = {
        "Reactor Core": {"color": "red", "message": "The reactor core is where nuclear fission takes place. It contains fuel rods arranged in a specific pattern."},
        "Control Rods": {"color": "purple", "message": "Control rods absorb neutrons to regulate the nuclear reaction. They can be inserted or withdrawn to control power output."},
        "Steam Generator": {"color": "blue", "message": "The steam generator transfers heat from the reactor coolant to create steam for electricity generation."},
        "Containment Building": {"color": "gray", "message": "The containment building is a reinforced structure that prevents radiation release and protects the reactor."}
    }
    
    st.markdown(f"""
        <div style='background-color: {component_info[selected_component]["color"]}22; 
                    padding: 20px; border-radius: 10px; border: 2px solid {component_info[selected_component]["color"]}'>
        {component_info[selected_component]["message"]}
        </div>
    """, unsafe_allow_html=True)

elif section == "Interactive Diagram":
    fig = go.Figure()
    
    # Enhanced reactor diagram
    components = [
        {"name": "Containment Building", "radius": 1, "color": "gray"},
        {"name": "Steam Generator", "radius": 0.8, "color": "blue"},
        {"name": "Control Rods", "radius": 0.7, "color": "purple"},
        {"name": "Reactor Core", "radius": 0.6, "color": "red"}
    ]
    
    for comp in components:
        fig.add_shape(type="circle",
            xref="x", yref="y",
            x0=-comp["radius"], y0=-comp["radius"], 
            x1=comp["radius"], y1=comp["radius"],
            line_color=comp["color"],
            fillcolor=f"rgba({','.join(map(str, [*px.colors.hex_to_rgb(px.colors.named[comp['color']]), 0.3])))}",
            name=comp["name"]
        )
        
        fig.add_annotation(x=0, y=comp["radius"]+0.1,
            text=comp["name"],
            showarrow=False,
            font=dict(size=12, color=comp["color"])
        )
    
    fig.update_layout(
        title="Interactive Nuclear Reactor Components",
        showlegend=False,
        width=700,
        height=700,
        xaxis=dict(showgrid=False, zeroline=False, visible=False),
        yaxis=dict(showgrid=False, zeroline=False, visible=False)
    )
    
    zoom = st.slider("Zoom level", 0.5, 2.0, 1.0, step=0.1)
    fig.update_layout(
        xaxis=dict(range=[-zoom, zoom]),
        yaxis=dict(range=[-zoom, zoom])
    )
    st.plotly_chart(fig)

st.markdown("---")
st.markdown("Created for educational purposes | Interactive Nuclear Reactor Guide 🔬")