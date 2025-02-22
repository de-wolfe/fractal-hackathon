
import streamlit as st

st.header("Quiz on Python programming")
st.write("**Question:**  \nWhat will be the output of the following Python code snippet?\n\n```python\ndef foo(*args, **kwargs):\n    print(\"Args:\", args)\n    print(\"Kwargs:\", kwargs)\n\nfoo(1, 2, 3, a=4, b=5)\n```\n\nA)  \n```\nArgs: (1, 2, 3)\nKwargs: {'a': 4, 'b': 5}\n```\n\nB)  \n```\nArgs: [1, 2, 3]\nKwargs: {'a': 4, 'b': 5}\n```\n\nC)  \n```\nArgs: (1, 2, 3)\nKwargs: 4, 5\n```\n\nD)  \n```\nArgs: [1, 2, 3]\nKwargs: [4, 5]\n```\n\n*Correct Answer: A*")
