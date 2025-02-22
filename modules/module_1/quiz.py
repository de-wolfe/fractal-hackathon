import streamlit as st

st.title("Linear Algebra Module Assessment")

st.write("Please answer the following questions to demonstrate your understanding of the key concepts taught in the module.")

st.header("Question 1")
st.write("1. **Vector Operations**: Which of the following best describes scalar multiplication?")
options1 = [
    "A transformation that rotates a vector in space.",
    "An operation that adds two vectors to produce a third vector.",
    "A method of stretching or shrinking a vector by a scalar factor."
]
answer1 = st.radio("Choose the correct option:", options1)

st.header("Question 2")
st.write("2. **Matrices and Transformations**: How does a matrix transformation affect vectors in a vector space?")
options2 = [
    "It only changes the length of vectors.",
    "It reflects vectors through the origin.",
    "It can rotate, scale, or translate vectors depending on the matrix entries."
]
answer2 = st.radio("Choose the correct option:", options2)

if st.button("Submit Answers"):
    if answer1 == "A method of stretching or shrinking a vector by a scalar factor.":
        st.success("Question 1: Correct!")
    else:
        st.error("Question 1: Incorrect. The correct answer is: A method of stretching or shrinking a vector by a scalar factor.")
    
    if answer2 == "It can rotate, scale, or translate vectors depending on the matrix entries.":
        st.success("Question 2: Correct!")
    else:
        st.error("Question 2: Incorrect. The correct answer is: It can rotate, scale, or translate vectors depending on the matrix entries.")