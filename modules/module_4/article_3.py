```python
import streamlit as st
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import matplotlib.pyplot as plt

# Page Title with custom styling
st.markdown("""
    <style>
    .title {
        text-align: center;
        color: #1f77b4;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    .subheader {
        color: #2c3e50;
        border-bottom: 2px solid #eee;
        padding-bottom: 10px;
    }
    </style>
    <h1 class='title'>The Art of Linear Transformations</h1>
    """, unsafe_allow_html=True)

st.markdown("<h3 class='subheader'>Explore how vectors and shapes transform in 2D space!</h3>", unsafe_allow_html=True)

# Create tabs for different visualizations
tab1, tab2 = st.tabs(["Vector Transformation", "Unit Circle Transformation"])

with tab1:
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("### Input Vector")
        x = st.slider('X component', -5.0, 5.0, 1.0, key='x1')
        y = st.slider('Y component', -5.0, 5.0, 1.0, key='y1')
        
        st.markdown("### Transformation Matrix")
        col_a, col_b = st.columns(2)
        with col_a:
            a11 = st.number_input('A₁₁', -2.0, 2.0, 1.0, step=0.1, key='a11')
            a21 = st.number_input('A₂₁', -2.0, 2.0, 0.0, step=0.1, key='a21')
        with col_b:
            a12 = st.number_input('A₁₂', -2.0, 2.0, 0.0, step=0.1, key='a12')
            a22 = st.number_input('A₂₂', -2.0, 2.0, 1.0, step=0.1, key='a22')

    # Create transformation matrix and transform vector
    A = np.array([[a11, a12], [a21, a22]])
    v = np.array([x, y])
    v_transformed = A @ v

    with col2:
        # Enhanced interactive plot
        fig = go.Figure()
        
        # Add grid lines
        for i in range(-5, 6):
            fig.add_shape(type="line", x0=-5, y0=i, x1=5, y1=i,
                         line=dict(color="lightgray", width=1))
            fig.add_shape(type="line", x0=i, y0=-5, x1=i, y1=5,
                         line=dict(color="lightgray", width=1))

        # Plot original vector
        fig.add_trace(go.Scatter(x=[0, x], y=[0, y],
                                mode='lines+markers',
                                name='Original Vector',
                                line=dict(color='#1f77b4', width=3)))

        # Plot transformed vector
        fig.add_trace(go.Scatter(x=[0, v_transformed[0]], y=[0, v_transformed[1]],
                                mode='lines+markers',
                                name='Transformed Vector',
                                line=dict(color='#ff7f0e', width=3)))

        fig.update_layout(
            title="Vector Transformation Visualization",
            xaxis=dict(range=[-5, 5], zeroline=True),
            yaxis=dict(range=[-5, 5], zeroline=True),
            showlegend=True,
            width=600,
            height=600,
            plot_bgcolor='white'
        )

        st.plotly_chart(fig)

with tab2:
    st.markdown("### Unit Circle Transformation")
    if st.button("Transform Unit Circle", key='transform_circle'):
        # Create points for unit circle
        theta = np.linspace(0, 2*np.pi, 100)
        circle_x = np.cos(theta)
        circle_y = np.sin(theta)
        
        # Transform all points
        transformed_points = A @ np.vstack((circle_x, circle_y))
        
        # Enhanced circle plot
        fig2 = go.Figure()
        
        # Add grid lines
        for i in range(-5, 6):
            fig2.add_shape(type="line", x0=-5, y0=i, x1=5, y1=i,
                          line=dict(color="lightgray", width=1))
            fig2.add_shape(type="line", x0=i, y0=-5, x1=i, y1=5,
                          line=dict(color="lightgray", width=1))
        
        # Original circle
        fig2.add_trace(go.Scatter(x=circle_x, y=circle_y,
                                 mode='lines',
                                 name='Original Circle',
                                 line=dict(color='#1f77b4', width=3)))
        
        # Transformed circle
        fig2.add_trace(go.Scatter(x=transformed_points[0], y=transformed_points[1],
                                 mode='lines',
                                 name='Transformed Shape',
                                 line=dict(color='#ff7f0e', width=3)))
        
        fig2.update_layout(
            title="Unit Circle Transformation",
            xaxis=dict(range=[-5, 5], zeroline=True),
            yaxis=dict(range=[-5, 5], zeroline=True),
            showlegend=True,
            width=600,
            height=600,
            plot_bgcolor='white'
        )
        
        st.plotly_chart(fig2)

# Educational content with enhanced styling
st.markdown("""
    <style>
    .concept-box {
        background-color: #f8f9fa;
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("""
    <div class='concept-box'>
    <h2>Understanding Linear Transformations</h2>
    <p>A linear transformation is a special type of function that preserves two key properties:</p>
    <ol>
        <li>Vector addition: T(v + w) = T(v) + T(w)</li>
        <li>Scalar multiplication: T(cv) = cT(v)</li>
    </ol>
    <h3>Key Takeaways:</h3>
    <ul>
        <li>The blue vector/circle represents the original shape</li>
        <li>The orange vector/circle shows the transformed shape</li>
        <li>The transformation matrix completely determines how vectors are transformed</li>
        <li>Try different matrix values to see how they affect the transformation!</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
```