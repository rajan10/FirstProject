"""
app.py
Streamlit frontend for the Student GEN-AI Chatbot.
Architecture:
Streamlit
    |
    v
LangChain
    |
    +---- MySQL
    |
    +---- RAG
    |
    v
Ollama
    |
    v
Answer
"""
import streamlit as st
from db_manager import create_courses_table
from lang_chain import ask_student
# --------------------------------------------------
# Page configuration
# --------------------------------------------------
st.set_page_config(
    page_title="Student GEN-AI Chatbot",
    page_icon="🎓",
    layout="centered"
)
# --------------------------------------------------
# Initialize database
# --------------------------------------------------
create_courses_table()
# --------------------------------------------------
# Page title
# --------------------------------------------------
st.title("🎓 Student GEN-AI Chatbot")
st.write(
    "Ask questions about courses, fees, duration, "
    "and institute policies."
)
st.divider()
# --------------------------------------------------
# Chat history
# --------------------------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []
# --------------------------------------------------
# Display previous messages
# --------------------------------------------------
for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])
# --------------------------------------------------
# Student question
# --------------------------------------------------
question = st.chat_input(
    "Ask your question..."
)
# --------------------------------------------------
# Process question
# --------------------------------------------------
if question:
    # Display student question
    with st.chat_message("user"):

        st.markdown(question)

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )
    # Generate answer
    with st.chat_message("assistant"):
        with st.spinner("Thinking... 🤔"):
            try:
                answer = ask_student(question)
                st.markdown(answer)
            except Exception as error:
                answer = (
                    "Sorry, something went wrong.\n\n"
                    f"Error: `{error}`"
                )
                st.error(answer)
    # Save assistant response
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )