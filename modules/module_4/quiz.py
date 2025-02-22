import modules.utils as utils
params = st.experimental_get_query_params()
module_number = int(params.get("module", [0])[0]) if "module" in params else None
```python
import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.title("📐 Interactive Linear Algebra Quiz")

# Custom CSS for better styling
st.markdown("""
    <style>
    .quiz-container {
        padding: 20px;
        border-radius: 10px;
        background-color: #f0f2f6;
        margin: 10px 0;
    }
    </style>
    """, unsafe_allow_html=True)

# Question 1 with visualization
st.markdown("<div class='quiz-container'>", unsafe_allow_html=True)
st.write("### Question 1: Vector Operations 🔢")
st.write("Given vectors v = [2,3] and w = [1,4], calculate v + w")

# Create visual representation of vectors
fig = go.Figure()
# Add vectors
fig.add_trace(go.Scatter(x=[0, 2], y=[0, 3], mode='lines+markers', name='v = [2,3]', 
                        line=dict(color='blue', width=2)))
fig.add_trace(go.Scatter(x=[0, 1], y=[0, 4], mode='lines+markers', name='w = [1,4]', 
                        line=dict(color='red', width=2)))
fig.update_layout(title='Vector Visualization', showlegend=True)
st.plotly_chart(fig)

user_answer1 = st.text_input("Enter your answer as two comma-separated numbers (e.g., 3,7):")

if st.button("Check Answer 1 ✓"):
    try:
        user_vector = [float(x) for x in user_answer1.split(",")]
        correct_answer = [3,7]
        if np.array_equal(user_vector, correct_answer):
            st.success("🎉 Correct! v + w = [3,7]")
            # Show resulting vector
            fig.add_trace(go.Scatter(x=[0, 3], y=[0, 7], mode='lines+markers', 
                         name='v + w = [3,7]', line=dict(color='green', width=3)))
            st.plotly_chart(fig)
        else:
            st.error("Not quite. Try adding the corresponding components again.")
    except:
        st.error("Please enter your answer in the correct format (e.g., 3,7)")
st.markdown("</div>", unsafe_allow_html=True)

# Question 2 with interactive visualization
st.markdown("<div class='quiz-container'>", unsafe_allow_html=True)
st.write("### Question 2: Matrix Transformation 🔄")
st.write("""Consider the matrix A = [[2,0], [0,2]]. 
What type of transformation does this matrix represent?""")

# Create grid visualization
x = np.linspace(-2, 2, 5)
y = np.linspace(-2, 2, 5)
X, Y = np.meshgrid(x, y)

fig2 = go.Figure()
# Original grid
fig2.add_trace(go.Scatter(x=X.flatten(), y=Y.flatten(), mode='markers',
                         name='Original Grid', marker=dict(color='blue')))
# Transformed grid
fig2.add_trace(go.Scatter(x=2*X.flatten(), y=2*Y.flatten(), mode='markers',
                         name='Transformed Grid', marker=dict(color='red')))
fig2.update_layout(title='Grid Transformation Visualization')
st.plotly_chart(fig2)

options = ["Rotation", "Scaling", "Shear", "Reflection"]
user_answer2 = st.radio("Select your answer:", options)

if st.button("Check Answer 2 ✓"):
    if user_answer2 == "Scaling":
        st.success("🎉 Correct! This matrix scales all vectors by a factor of 2.")
        st.write("Notice how the grid points move away from the origin by a factor of 2.")
    else:
        st.error("Not quite. Observe how the points move in the visualization above.")
st.markdown("</div>", unsafe_allow_html=True)

# Add a progress indicator
progress = st.progress(0)
for i in range(100):
    progress.progress(i + 1)
```