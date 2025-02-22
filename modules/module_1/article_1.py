import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
from PIL import Image

st.title("🧪 Color-Changing Reactions: A Visual Guide to Chemical Transformations")

# Add custom CSS for better styling
st.markdown("""
    <style>
    .reaction-box {
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0;
        background-color: #f0f2f6;
    }
    .highlight-text {
        color: #1f618d;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
## The Magic of Chemical Color Changes ✨

Discover how molecules transform and create stunning visual displays in these fascinating chemical reactions!
""")

# Enhanced interactive color reaction simulator
st.subheader("🎨 Interactive Color Change Simulator")

col1, col2 = st.columns(2)

with col1:
    reagent1 = st.selectbox(
        "Select first reagent:",
        ["Copper Sulfate", "Potassium Permanganate", "Sodium Hydroxide"],
        help="Choose your first chemical reagent"
    )
    
with col2:
    reagent2 = st.selectbox(
        "Select second reagent:",
        ["Ammonia", "Hydrogen Peroxide", "Hydrochloric Acid"],
        help="Choose your second chemical reagent"
    )

# Enhanced color map with descriptions
color_reactions = {
    ("Copper Sulfate", "Ammonia"): {
        "colors": ["#1E90FF", "#00BFFF"],
        "description": "Forms a deep blue copper-ammonia complex"
    },
    ("Potassium Permanganate", "Hydrogen Peroxide"): {
        "colors": ["#800080", "#FFC0CB"],
        "description": "Reduction of purple permanganate to pink"
    },
    ("Sodium Hydroxide", "Hydrochloric Acid"): {
        "colors": ["#FFFFFF", "#FFB6C1"],
        "description": "Neutralization reaction with pH indicator"
    }
}

if (reagent1, reagent2) in color_reactions:
    st.markdown("### Reaction Result")
    col3, col4 = st.columns(2)
    reaction_info = color_reactions[(reagent1, reagent2)]
    
    with col3:
        st.markdown(f"""
        <div style='background-color: {reaction_info["colors"][0]}; 
                    height: 120px; 
                    border-radius: 10px;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    color: white;
                    font-weight: bold;'>
            Initial State
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown(f"""
        <div style='background-color: {reaction_info["colors"][1]}; 
                    height: 120px; 
                    border-radius: 10px;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    color: white;
                    font-weight: bold;'>
            Final State
        </div>
        """, unsafe_allow_html=True)
    
    st.info(f"**Reaction Description:** {reaction_info['description']}")

# Enhanced pH color chart
st.subheader("📊 Interactive pH Scale")

ph_values = np.arange(0, 15, 1)
colors = ['#FF0000', '#FF4500', '#FFA500', '#FFD700', '#FFFF00', 
          '#9ACD32', '#00FF00', '#00FA9A', '#00FFFF', '#1E90FF',
          '#0000FF', '#4B0082', '#8B008B', '#800080', '#4B0082']

selected_ph = st.slider("Select pH value", 0, 14, 7)
st.markdown(f"""
<div style='background-color: {colors[selected_ph]}; 
            padding: 20px; 
            border-radius: 10px; 
            text-align: center; 
            color: black; 
            font-weight: bold;'>
    pH {selected_ph}: {['Strongly Acidic', 'Acidic', 'Neutral', 'Basic', 'Strongly Basic'][min(4, selected_ph//3)]}
</div>
""", unsafe_allow_html=True)

# Enhanced expandable sections
st.subheader("💡 Color Chemistry Facts")

with st.expander("🍁 Why do leaves change color in fall?", expanded=False):
    st.markdown("""
    ### Seasonal Color Changes
    - 🟢 **Chlorophyll** (green) breaks down
    - 🟡 **Carotenoids** reveal yellow and orange
    - 🔴 **Anthocyanins** produce red and purple
    """)

with st.expander("🎆 The Chemistry of Fireworks Colors", expanded=False):
    st.markdown("""
    ### Metal Salts Create Colors
    - 🔴 **Strontium** → Red
    - 🔵 **Copper** → Blue
    - 🟢 **Barium** → Green
    - 🟡 **Sodium** → Yellow
    """)

# Enhanced interactive quiz
st.subheader("🎯 Test Your Knowledge")

questions = {
    "What causes the blue color in Copper Sulfate solutions?": {
        "options": ["The Cu²⁺ ion", "The SO₄²⁻ ion", "Water molecules", "Temperature"],
        "correct": "The Cu²⁺ ion",
        "explanation": "The Cu²⁺ ion gives Copper Sulfate its characteristic blue color due to d-orbital electron transitions."
    }
}

for question, data in questions.items():
    user_answer = st.radio(question, data["options"])
    
    if st.button("Check Answer 🎲"):
        if user_answer == data["correct"]:
            st.success("🎉 Correct! " + data["explanation"])
        else:
            st.error("Try again! Think about the metallic components of the compound.")