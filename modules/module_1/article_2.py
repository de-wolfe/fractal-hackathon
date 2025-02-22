import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Matrix Mastery", layout="wide")

st.title("Matrix Mastery: Using Visual Tools to Simplify Complex Concepts in Linear Algebra")

st.markdown("""
Linear algebra—often perceived as a tangled web of numbers and operations—can become an exhilarating puzzle when visual tools are brought into play. 
Visualizations can transform abstract equations into tangible concepts, making learning both intuitive and irresistibly engaging. Explore how matrices can be more than just grids of numbers!
""")

# Create a matrix
matrix = np.array([[2, 3], [1, 4]])

st.subheader("Matrix Visualization")

st.markdown("""
Let's start with a simple matrix:
""")

st.code("""
[[2, 3],
 [1, 4]]
""")

st.markdown("""
A matrix can be thought of as a transformation. Imagine it like a mini squish-and-stretch operation applied to space. 
To visualize this, adjust the sliders and see how the points in space move when transformed by our matrix.
""")

angle = st.slider("Rotate Space by Degrees", 0, 360, 45)
magnitude = st.slider("Scale the Transformation", 0.5, 2.0, 1.0)

# Create a grid of points
x, y = np.meshgrid(np.linspace(-5, 5, 10), np.linspace(-5, 5, 10))
rotated_x = magnitude * (x * np.cos(np.radians(angle)) - y * np.sin(np.radians(angle)))
rotated_y = magnitude * (x * np.sin(np.radians(angle)) + y * np.cos(np.radians(angle)))

fig, ax = plt.subplots()
ax.quiver(x, y, rotated_x-x, rotated_y-y, angles='xy', scale_units='xy', scale=1, color='blue')
ax.set_xlim([-10, 10])
ax.set_ylim([-10, 10])
ax.set_title("2D Space Transformation by Matrix")

st.pyplot(fig)

st.subheader("Eigenvectors and Eigenvalues")

st.markdown("""
Discover the magic of eigenvectors and eigenvalues! They play a crucial role in simplifying matrix operations by providing insight into the directions and scales of transformation.
Below, see how a matrix can be represented with its eigenvectors:
""")

eigenvalues, eigenvectors = np.linalg.eig(matrix)

st.markdown("Eigenvalues:")
st.write(eigenvalues)

st.markdown("Eigenvectors:")
st.write(eigenvectors)

fig, ax = plt.subplots()
ax.quiver([0, 0], [0, 0], eigenvectors[:,0], eigenvectors[:,1], angles='xy', scale_units='xy', scale=1, color=['red', 'green'])
ax.set_xlim([-2, 2])
ax.set_ylim([-2, 2])
ax.grid()
ax.set_title("Eigenvectors of the Matrix")

st.pyplot(fig)

st.markdown("""
By interacting with these visualizations, complex topics in linear algebra like transformation matrices, eigenvectors, and eigenvalues 
become more than theory—they become a vibrant part of intuitive understanding. Ready to dive deeper into the matrix?
""")