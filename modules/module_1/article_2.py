import streamlit as st
import py3Dmol
import pandas as pd
import plotly.express as px
from stmol import showmol
import plotly.graph_objects as go

st.title("🔬 Molecular Models in 3D: Understanding Chemical Structures Through Visual Patterns")

# Add custom CSS for better styling
st.markdown("""
    <style>
    .stSelectbox {
        background-color: #f0f2f6;
        border-radius: 5px;
        padding: 5px;
    }
    .stButton button {
        background-color: #4CAF50;
        color: white;
        border-radius: 5px;
    }
    </style>
    """, unsafe_allow_html=True)

# Introduction with animation
st.markdown("""
## 🎯 Explore the fascinating world of molecular structures!
Let's dive into the microscopic world of molecules and discover their unique properties!
""")

# Create two columns with better spacing
col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("""
    ### 🔄 Interactive 3D Molecule Viewer
    Select a molecule to view its 3D structure:
    - 🖱️ Rotate: Click and drag
    - 🔍 Zoom: Scroll wheel
    - 🎨 Style: Use selector below
    """)
    
    molecule_options = {
        "Water": "O",
        "Carbon Dioxide": "O=C=O",
        "Methane": "C",
        "Ammonia": "N"
    }
    
    selected_molecule = st.selectbox("Choose a molecule:", list(molecule_options.keys()))
    style = st.selectbox("Select display style:", ["stick", "sphere", "line", "cartoon"])
    
    def render_mol(xyz):
        xyzview = py3Dmol.view(width=400, height=400)
        xyzview.addModel(xyz, "sdf")
        xyzview.setStyle({style:{}})
        xyzview.zoomTo()
        showmol(xyzview, height=400, width=400)
    
    render_mol(molecule_options[selected_molecule])

with col2:
    st.markdown("### 📊 Molecular Properties Visualization")
    
    data = {
        'Molecule': ['Water', 'Carbon Dioxide', 'Methane', 'Ammonia'],
        'Molecular Weight': [18, 44, 16, 17],
        'Boiling Point (°C)': [100, -78, -161, -33],
        'Number of Atoms': [3, 3, 5, 4]
    }
    
    df = pd.DataFrame(data)
    
    property_to_plot = st.selectbox("Select property to visualize:", 
                                  ['Molecular Weight', 'Boiling Point (°C)', 'Number of Atoms'])
    
    fig = px.bar(df, x='Molecule', y=property_to_plot,
                 color='Molecule',
                 title=f'{property_to_plot} Comparison',
                 template="plotly_white",
                 height=400)
    
    fig.update_layout(
        showlegend=False,
        plot_bgcolor='rgba(0,0,0,0)'
    )
    
    st.plotly_chart(fig, use_container_width=True)

st.markdown("""
### 💡 Visualization Styles Guide
""")
styles_df = pd.DataFrame({
    'Style': ['Stick', 'Sphere', 'Line', 'Cartoon'],
    'Best Used For': ['Viewing bonds clearly', 'Understanding atomic size', 'Simplifying complex structures', 'Large biomolecules'],
    'Common Applications': ['Small molecules', 'Atomic interactions', 'Quick structure review', 'Proteins and DNA']
})

st.table(styles_df)

# Enhanced interactive quiz
st.markdown("### 🎯 Knowledge Challenge!")
with st.form("quiz_form"):
    quiz_question = st.radio(
        "Which molecule has the highest boiling point among the options shown?",
        ["Water", "Carbon Dioxide", "Methane", "Ammonia"]
    )
    
    submit_button = st.form_submit_button("Check Answer!")
    
    if submit_button:
        if quiz_question == "Water":
            st.success("🎉 Correct! Water's high boiling point (100°C) is due to hydrogen bonding between molecules.")
            st.balloons()
        else:
            st.error("❌ Not quite! Remember that hydrogen bonding in water makes it special.")

st.markdown("---")
st.markdown("### 👩‍🔬 Want to learn more?")
if st.button("Show Fun Fact"):
    st.info("Did you know? Water's unique properties, including its high boiling point, make it essential for life on Earth! 🌍")