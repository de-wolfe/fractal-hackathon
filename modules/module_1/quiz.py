import streamlit as st

st.title("Spanish Greetings Quiz")

st.header("Test Your Knowledge")

st.write("Translate the following English phrases into Spanish:")

# First question
st.subheader("1) Hello")

answer1 = st.text_input("Your answer for 'Hello':")

if answer1.lower() == "hola":
    st.success("Correct! 'Hello' in Spanish is 'Hola'.")
elif answer1:
    st.error("Incorrect. Try again.")

# Second question
st.subheader("2) How are you?")

answer2 = st.text_input("Your answer for 'How are you?':")

if answer2.lower() == "¿cómo estás?" or answer2.lower() == "como estas":
    st.success("Correct! 'How are you?' in Spanish is '¿Cómo estás?'.")
elif answer2:
    st.error("Incorrect. Try again.")
