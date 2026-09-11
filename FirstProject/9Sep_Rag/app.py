import streamlit as st
from rag import ask_gpt

st.write("Ask questions about the company documents")


question = st.text_input("Enter your question:")

if st.button("Ask"):
    if question:
        answer = ask_gpt(question)
        st.subheader("Answer")
        st.write(answer)

    else:
        st.warning("Please enter a question before asking.")