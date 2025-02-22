import matplotlib.pyplot as plt
import numpy as np
import random
def write_to_target():    
    with open("app.py", "a") as f:
        # Content to add to target.py
        new_content  = """\n
m = random.randint(-5, 5)  # Random slope
b = random.randint(-10, 10)  # Random y-intercept

# Function to plot the graph
def plot_function():
    x = np.linspace(-10, 10, 100)
    y = m * x + b

    fig, ax = plt.subplots()
    ax.plot(x, y, label=f"y = {m}x + {b}")
    ax.axhline(0, color='black', linewidth=1)  # X-axis
    ax.axvline(0, color='black', linewidth=1)  # Y-axis
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.legend()
    
    st.pyplot(fig)

# Streamlit UI setup
st.title("Guess the Slope! 🧠📈")

st.write("A random linear function is plotted below. Can you guess its slope?")

# Show the graph
plot_function()

# User input
user_slope = st.number_input("Enter the slope (m):", step=0.1, format="%.1f")

# Check answer
if st.button("Check Answer"):
    if user_slope == m:
        st.success("✅ Correct! The slope is indeed " + str(m))
    else:
        st.error(f"❌ Incorrect. The correct slope is {m}")
"""
        
        # Write to the file
        f.write(new_content)

    print("Content successfully added to app.py")
