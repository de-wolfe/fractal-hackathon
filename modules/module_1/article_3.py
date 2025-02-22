import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title='Geometric Interpretations: Exploring Linear Transformations through Visual Aid', layout='wide')

st.title('Geometric Interpretations: Exploring Linear Transformations through Visual Aid')

st.write('''
Linear algebra is a cornerstone of both pure and applied mathematics, offering insights that can be beautifully translated into geometry. Today, we explore the magical world of linear transformations – the functions that map vectors to other vectors while preserving the operations of vector addition and scalar multiplication. We'll visualize and interact with these mappings to gain a deeper understanding of their geometric significance.
''')

st.write('''
To begin our visual journey, consider the simplest form of transformation: scaling. A scalar matrix transforms a vector by stretching or shrinking it. Below, you can adjust the scaling factor to see how vectors change their magnitude while maintaining their direction.
''')

# Slider for scaling factor
scale = st.slider("Scale Factor", min_value=0.1, max_value=3.0, value=1.0, step=0.1)

# Plot original and transformed vector
fig, ax = plt.subplots()
original_vector = np.array([1, 1])
transformed_vector = scale * original_vector

ax.quiver(0, 0, *original_vector, angles='xy', scale_units='xy', scale=1, color='r', label='Original Vector')
ax.quiver(0, 0, *transformed_vector, angles='xy', scale_units='xy', scale=1, color='b', label='Transformed Vector')

ax.set_xlim(-4, 4)
ax.set_ylim(-4, 4)
ax.axhline(0, color='grey', linewidth=0.8)
ax.axvline(0, color='grey', linewidth=0.8)
ax.set_aspect('equal')

plt.title('Scaling Transformation')
plt.legend()
st.pyplot(fig)

st.write('''
But linear transformations can be much more than simple scaling. Let us delve into rotation, where angles and orientation bring to life a dynamic aspect of linear algebra, demonstrating the preservation of lengths but alteration of directions. Adjust the angle below to see how vectors spin around the origin.
''')

# Slider for rotation angle
angle = st.slider("Rotation Angle (degrees)", min_value=0, max_value=360, value=0, step=5)

# Rotation matrix
theta = np.radians(angle)
rotation_matrix = np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])
rotated_vector = rotation_matrix @ original_vector

# Plot original and rotated vector
fig, ax = plt.subplots()

ax.quiver(0, 0, *original_vector, angles='xy', scale_units='xy', scale=1, color='r', label='Original Vector')
ax.quiver(0, 0, *rotated_vector, angles='xy', scale_units='xy', scale=1, color='g', label='Rotated Vector')

ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.axhline(0, color='grey', linewidth=0.8)
ax.axvline(0, color='grey', linewidth=0.8)
ax.set_aspect('equal')

plt.title('Rotation Transformation')
plt.legend()
st.pyplot(fig)

st.write('''
A more complex transformation involves shearing, where each point moves parallel to an axis by a specified amount related to its other coordinate. The visualization below lets you adjust the shear factor, demonstrating how such a transformation alters both the shape and orientation of an object, embedding linear algebra's profound influence on geometry.
''')

# Slider for shear factor
shear_x = st.slider("Shear Factor (X-axis)", min_value=-2.0, max_value=2.0, value=0.0, step=0.1)

# Shear matrix
shear_matrix = np.array([[1, shear_x], [0, 1]])
sheared_vector = shear_matrix @ original_vector

# Plot original and sheared vector
fig, ax = plt.subplots()

ax.quiver(0, 0, *original_vector, angles='xy', scale_units='xy', scale=1, color='r', label='Original Vector')
ax.quiver(0, 0, *sheared_vector, angles='xy', scale_units='xy', scale=1, color='purple', label='Sheared Vector')

ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)
ax.axhline(0, color='grey', linewidth=0.8)
ax.axvline(0, color='grey', linewidth=0.8)
ax.set_aspect('equal')

plt.title('Shear Transformation')
plt.legend()
st.pyplot(fig)

st.write('''
Through dynamic visualizations, we unveil how linear transformations act to twist, stretch, and embed intricate geometries. Such interpretations not only aid in understanding but inspire wonder at how these fundamental operations weave into the fabric of higher mathematics and everyday technologies.
''')