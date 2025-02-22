import streamlit as st
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Main title with custom styling
st.title("🔄 Mapping Matrix Transformations")
st.markdown("### A Visual Journey Through Vector Spaces")

# Create two columns for better layout
col1, col2 = st.columns([1, 3])

with col1:
    st.markdown("### Matrix Controls")
    # Enhanced matrix controls with better descriptions
    a11 = st.slider("Scale X ➡️ [1,1]", -2.0, 2.0, 1.0, 0.1)
    a12 = st.slider("Shear X ↗️ [1,2]", -2.0, 2.0, 0.0, 0.1)
    a21 = st.slider("Shear Y ↗️ [2,1]", -2.0, 2.0, 0.0, 0.1)
    a22 = st.slider("Scale Y ⬆️ [2,2]", -2.0, 2.0, 1.0, 0.1)

    # Matrix visualization
    st.latex(
        r"""
    \text{Transform Matrix} = \begin{bmatrix} 
    """
        + f"{a11} & {a12}"
        + r""" \\
    """
        + f"{a21} & {a22}"
        + r"""
    \end{bmatrix}
    """
    )

# Create transformation matrix
transformation_matrix = np.array([[a11, a12], [a21, a22]])

# Create grid of points with more density for smoother visualization
x = np.linspace(-2, 2, 25)
y = np.linspace(-2, 2, 25)
X, Y = np.meshgrid(x, y)

# Transform the grid
points = np.column_stack((X.flatten(), Y.flatten()))
transformed_points = points @ transformation_matrix.T
X_transformed = transformed_points[:, 0].reshape(X.shape)
Y_transformed = transformed_points[:, 1].reshape(Y.shape)

# Enhanced visualization
fig = make_subplots(
    rows=1, cols=2, subplot_titles=("Original Space 📐", "Transformed Space ✨")
)

# Original grid with improved styling
fig.add_trace(
    go.Scatter(
        x=X.flatten(),
        y=Y.flatten(),
        mode="markers",
        name="Original Points",
        marker=dict(size=4, color="rgba(65, 105, 225, 0.7)"),
    ),
    row=1,
    col=1,
)

# Transformed grid with improved styling
fig.add_trace(
    go.Scatter(
        x=X_transformed.flatten(),
        y=Y_transformed.flatten(),
        mode="markers",
        name="Transformed Points",
        marker=dict(size=4, color="rgba(220, 20, 60, 0.7)"),
    ),
    row=1,
    col=2,
)

# Enhanced layout
fig.update_layout(
    height=600,
    showlegend=True,
    title_text="Interactive Matrix Transformation Visualization",
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(240,240,240,0.5)",
)

# Update axes with grid lines
for i in [1, 2]:
    fig.update_xaxes(
        range=[-3, 3],
        row=1,
        col=i,
        gridcolor="lightgray",
        zeroline=True,
        zerolinecolor="black",
    )
    fig.update_yaxes(
        range=[-3, 3],
        row=1,
        col=i,
        gridcolor="lightgray",
        zeroline=True,
        zerolinecolor="black",
    )

st.plotly_chart(fig, use_container_width=True)

# Interactive explanations
st.markdown("### 🎯 Understanding Matrix Transformations")

# Calculate determinant
det = np.linalg.det(transformation_matrix)

# Create columns for explanation and effects
exp_col1, exp_col2 = st.columns(2)

with exp_col1:
    st.markdown("""
    **What you're seeing:**
    - 🔵 Blue points show the original coordinate grid
    - 🔴 Red points show where each point moves after transformation
    - The grid helps visualize how space is transformed
    """)

with exp_col2:
    st.markdown("""
    **Matrix Properties:**
    - Determinant shows scaling and orientation changes
    - When det = 0, space collapses to lower dimensions
    - Negative determinant indicates reflection
    """)

# Enhanced determinant display with interpretations
st.markdown("### 📊 Transformation Analysis")
st.write(f"**Determinant:** {det:.2f}")

if abs(det) < 0.01:
    st.warning(
        "⚠️ SINGULAR MATRIX: This transformation collapses space into a line or point!"
    )
elif det < 0:
    st.info(
        "🔄 REFLECTION: This transformation includes a reflection (flips orientation)"
    )
elif det > 1:
    st.success(
        "↗️ EXPANSION: This transformation increases area by a factor of {:.2f}".format(
            abs(det)
        )
    )
elif det < 1:
    st.info(
        "↙️ CONTRACTION: This transformation decreases area by a factor of {:.2f}".format(
            abs(det)
        )
    )
else:
    st.success("✓ AREA PRESERVING: This transformation maintains area")
