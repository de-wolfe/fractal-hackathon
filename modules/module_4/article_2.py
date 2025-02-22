```python
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from PIL import Image
import plotly.express as px

st.title("🌈 Colorful Eigenvalues: Understanding Linear Systems Through Geometric Patterns")

# Add a visually appealing header image using a gradient
def create_gradient_background():
    fig = go.Figure(go.Heatmap(
        z=[[1, 2, 3], [1, 2, 3]],
        colorscale='Viridis',
        showscale=False
    ))
    fig.update_layout(height=100, margin=dict(t=0,b=0,l=0,r=0))
    return fig

st.plotly_chart(create_gradient_background(), use_container_width=True)

st.markdown("""
## 🎨 Explore the Beauty of Linear Transformations
Discover how matrices transform space and learn about eigenvalues through interactive visualizations!
""")

# Enhanced Interactive Matrix Input with better styling
st.sidebar.markdown("### 🎮 Control Panel")
st.sidebar.markdown("Adjust the matrix elements to see the transformation in action!")

matrix_container = st.sidebar.container()
with matrix_container:
    a11 = st.slider("Element [1,1] 📍", -3.0, 3.0, 1.0, step=0.1)
    a12 = st.slider("Element [1,2] 📍", -3.0, 3.0, 0.0, step=0.1)
    a21 = st.slider("Element [2,1] 📍", -3.0, 3.0, 0.0, step=0.1)
    a22 = st.slider("Element [2,2] 📍", -3.0, 3.0, 1.0, step=0.1)

# Create matrix and compute eigenvalues
A = np.array([[a11, a12], [a21, a22]])
eigenvalues, eigenvectors = np.linalg.eig(A)

# Create enhanced grid of points
x = np.linspace(-2, 2, 20)
y = np.linspace(-2, 2, 20)
X, Y = np.meshgrid(x, y)
points = np.column_stack((X.flatten(), Y.flatten()))
transformed_points = points @ A.T

# Enhanced visualization with better styling
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 📐 Original Space")
    fig1 = go.Figure()
    fig1.add_trace(go.Scatter(x=points[:,0], y=points[:,1], 
                             mode='markers',
                             marker=dict(color='blue', size=5, symbol='circle')))
    fig1.update_layout(
        width=400, height=400,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(240,240,240,0.95)',
        showlegend=False
    )
    st.plotly_chart(fig1)

with col2:
    st.markdown("### ✨ Transformed Space")
    fig2 = go.Figure()
    fig2.add_trace(go.Scatter(x=transformed_points[:,0], y=transformed_points[:,1], 
                             mode='markers',
                             marker=dict(color='red', size=5, symbol='circle')))
    fig2.update_layout(
        width=400, height=400,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(240,240,240,0.95)',
        showlegend=False
    )
    st.plotly_chart(fig2)

# Enhanced matrix properties display
st.markdown("### 📊 Matrix Analysis")
col3, col4 = st.columns(2)

with col3:
    st.markdown("#### Your Matrix:")
    st.write(pd.DataFrame(A, columns=['Column 1', 'Column 2']))

with col4:
    st.markdown("#### Eigenvalues:")
    eigenval_df = pd.DataFrame({
        'Eigenvalue': eigenvalues,
        'Magnitude': np.abs(eigenvalues)
    })
    st.write(eigenval_df)

# Enhanced eigenvector visualization
if st.button("🎯 Visualize Eigenvectors"):
    fig3 = plt.figure(figsize=(8, 8))
    plt.quiver(0, 0, eigenvectors[0,0], eigenvectors[1,0], 
               color='green', angles='xy', scale_units='xy', scale=1, label='Eigenvector 1')
    plt.quiver(0, 0, eigenvectors[0,1], eigenvectors[1,1], 
               color='purple', angles='xy', scale_units='xy', scale=1, label='Eigenvector 2')
    plt.grid(True)
    plt.xlim(-2, 2)
    plt.ylim(-2, 2)
    plt.legend()
    st.pyplot(fig3)

# Enhanced interactive quiz
st.markdown("### 🎯 Knowledge Check!")
quiz_answer = st.radio(
    "What special property do eigenvectors have under linear transformation?",
    ["🔄 They change direction completely",
     "📏 They maintain their direction but may be scaled",
     "❌ They disappear",
     "📝 They always stay the same length"])

if quiz_answer == "📏 They maintain their direction but may be scaled":
    st.success("🎉 Correct! Eigenvectors keep their direction but get scaled by their corresponding eigenvalue.")
else:
    st.error("❌ Not quite right! Think about what makes eigenvectors special.")

# Add an interactive exploration section
st.markdown("""
### 🔍 Try This!
1. Set all values to 0 except [1,1]. What happens?
2. Make the matrix symmetric. How does it affect the transformation?
3. Try to create a rotation by setting [1,2] = -1 and [2,1] = 1
""")
```