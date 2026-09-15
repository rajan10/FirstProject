"""
lang_chain.py
This file connects:
DB CALL
   +
RAG CALL
   +
PROMPT
   +
OLLAMA
नेपाली:
सबै components लाई एउटै LangChain pipeline मा जोड्छ।
"""
from db_manager import (
    get_courses_context
)
from rag_service import (
    rag_call
)
from prompt import (
    prompt
)
from llm_provider import (
    get_llm
)
# ---------------------------------------------------------
# DB CALL
# ---------------------------------------------------------
def db_call(question: str):
    """
    Get course data from MySQL.
    नेपाली:
    Student को question पाएपछि MySQL बाट
    course information ल्याउँछ।

    Question यहाँ आवश्यक नभए पनि
    LangChain pipeline सँग मिलाउन argument राखिएको हो।
    """
    return get_courses_context()
# ---------------------------------------------------------
# Build LangChain
# ---------------------------------------------------------
def build_chain():
    chain = (
        {
            # MySQL data
            "course_data":
                db_call,
            # RAG data
            "policy_data":
                rag_call,
            # Original student question
            "question":
                lambda question: question
        }
        # Send all data to prompt
        | prompt
        # Send prompt to Ollama
        | get_llm()
    )
    return chain
# ---------------------------------------------------------
# Create chain
# ---------------------------------------------------------
chain = build_chain()
# ---------------------------------------------------------
# Ask student
# ---------------------------------------------------------
def ask_student(question: str):
    """
    Send question through complete pipeline.
    नेपाली:
    Student question लाई DB + RAG + Prompt + Ollama
    बाट process गर्छ।
    """
    answer = chain.invoke(
        question
    )
    return answer.content