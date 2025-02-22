import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
from PIL import Image
import time
import random

st.title("🌈 From Crystal Formation to Flame Tests: The Rainbow World of Chemical Reactions")

# Custom CSS for better visual appeal
st.markdown("""
    <style>
    .stProgress .st-bo {
        background-color: #f0f2f6;
    }
    .success-text {
        color: #28a745;
        font-size: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# Interactive Tabs with emoji icons
tab1, tab2, tab3 = st.tabs(["✨ Crystal Magic", "🔥 Flame Test Colors", "🤔 Quiz Time"])

with tab1:
    st.header("Crystal Formation in Solutions")
    
    # Enhanced Crystal Growth Animation
    if st.button("✨ Grow Crystals"):
        crystal_progress = st.progress(0)
        status_text = st.empty()
        stages = ['Nucleation', 'Growth', 'Formation']
        for i in range(100):
            crystal_progress.progress(i + 1)
            status_text.text(f"Stage: {stages[i//34]}")
            time.sleep(0.05)
        st.balloons()
    
    col1, col2 = st.columns(2)
    with col1:
        temperature = st.slider("Temperature (°C)", 0, 100, 25)
    with col2:
        concentration = st.slider("Solution Concentration (%)", 0, 100, 50)
    
    # Enhanced visualization
    size = temperature * concentration / 100
    crystal_display = '💎' * int(size/20)
    st.markdown(f"### Your Crystal Size:\n{crystal_display}")

with tab2:
    st.header("Flame Test Colors")
    
    flame_data = {
        'Element': ['Sodium', 'Potassium', 'Calcium', 'Copper', 'Lithium', 'Barium'],
        'Color': ['Yellow', 'Purple', 'Red-Orange', 'Green', 'Red', 'Green'],
        'Wavelength (nm)': [589, 768, 622, 520, 670, 554],
        'Symbol': ['Na', 'K', 'Ca', 'Cu', 'Li', 'Ba']
    }
    df = pd.DataFrame(flame_data)
    
    col1, col2 = st.columns([2, 1])
    with col1:
        selected_element = st.selectbox("Select Element", df['Element'])
        element_info = df[df['Element'] == selected_element]
        st.markdown(f"""
        ### {selected_element} ({element_info['Symbol'].iloc[0]})
        **Flame Color**: {element_info['Color'].iloc[0]}
        **Wavelength**: {element_info['Wavelength (nm)'].iloc[0]} nm
        """)
    
    fig = px.bar(df, x='Element', y='Wavelength (nm)', 
                 color='Color', title='Emission Spectrum Wavelengths',
                 hover_data=['Symbol'])
    fig.update_layout(height=400)
    st.plotly_chart(fig, use_container_width=True)

with tab3:
    st.header("Interactive Chemistry Quiz")
    
    questions = {
        "What causes the different colors in flame tests?": {
            "options": ["Heat of the flame", "Electronic transitions", "Chemical decomposition", "Random chance"],
            "correct": "Electronic transitions"
        },
        "Which element produces a yellow flame?": {
            "options": ["Potassium", "Sodium", "Calcium", "Lithium"],
            "correct": "Sodium"
        }
    }
    
    score = 0
    for q, data in questions.items():
        answer = st.radio(q, data["options"])
        if st.button(f"Check Answer for '{q[:20]}...'"):
            if answer == data["correct"]:
                st.success("🎉 Correct!")
                score += 1
            else:
                st.error("Try again! 💪")

# Enhanced sidebar
with st.sidebar:
    st.title("💡 Chemistry Fun Facts")
    facts = [
        "Crystals can form in zero gravity! 🚀",
        "Some reactions produce bioluminescence! ✨",
        "Diamond is pure carbon in crystalline form! 💎",
        "Gold can be hammered into sheets one atom thick! 🌟"
    ]
    if st.button("🎲 Generate Random Fact"):
        st.info(random.choice(facts))

st.markdown("---")
st.markdown("*Making chemistry colorful and fun! Created for visual learners* 🧪")