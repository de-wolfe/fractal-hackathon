import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import seaborn as sns

st.title("Visualizing Vectors: A Graphical Approach to Understanding Linear Algebra")

st.markdown("""
Linear algebra is the backbone of many fields in science and engineering. Vectors and matrices form the crux of this subject. Rather than getting lost in theoretical definitions, let's explore their beauty through rich visualizations.
""")

st.header("Vectors in 2D and 3D")

st.markdown("""
Visualizing vectors often starts in two dimensions. Let's interactively explore how these vectors look. In 2D, a vector is represented as an arrow with both direction and magnitude.
""")

# Slider for vector coordinates
x = st.slider('2D Vector X component', -10.0, 10.0, 1.0)
y = st.slider('2D Vector Y component', -10.0, 10.0, 2.0)

# Plot 2D vector
fig, ax = plt.subplots()
ax.quiver(0, 0, x, y, angles='xy', scale_units='xy', scale=1, color=sns.color_palette()[0])
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_aspect('equal')
st.pyplot(fig)

st.markdown("""
Moving into 3D introduces a new dimension, adding more complexity and beauty. Below is an interactive 3D vector.
""")

# Slider for 3D vector coordinates
x3 = st.slider('3D Vector X component', -10.0, 10.0, 1.0)
y3 = st.slider('3D Vector Y component', -10.0, 10.0, 2.0)
z3 = st.slider('3D Vector Z component', -10.0, 10.0, 3.0)

# Plot 3D vector
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.quiver(0, 0, 0, x3, y3, z3, arrow_length_ratio=0.1, color=sns.color_palette()[1])
ax.set_xlim([-10, 10])
ax.set_ylim([-10, 10])
ax.set_zlim([-10, 10])
ax.set_box_aspect([1, 1, 1])
st.pyplot(fig)

st.header("Matrix Transformations")

st.markdown("""
Matrices can be thought of as transformations applied to vectors. Let's consider a simple scaling matrix and visualize its effect on a vector.
""")

# Define a scaling matrix
scale_factor = st.slider('Scale Factor', 0.1, 5.0, 1.0)
matrix = np.array([[scale_factor, 0], [0, scale_factor]])

# Calculate transformed vector
transformed_vector = matrix @ np.array([x, y])

# Plot original and transformed vectors
fig, ax = plt.subplots()
ax.quiver(0, 0, x, y, angles='xy', scale_units='xy', scale=1, color=sns.color_palette()[0], label='Original')
ax.quiver(0, 0, transformed_vector[0], transformed_vector[1],
          angles='xy', scale_units='xy', scale=1, color=sns.color_palette()[2], label='Transformed')
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_aspect('equal')
ax.legend()
st.pyplot(fig)

st.markdown("""
Matrix transformations extend far beyond scaling. Try imagining how transformations like rotation and shear would reshape our vector space, opening new frontiers in graphics, machine learning, and beyond.
""")