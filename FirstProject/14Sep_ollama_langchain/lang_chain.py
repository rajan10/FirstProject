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

सबै components लाई एउटै LangChain pipeline मा जोड्छ।
"""
from db_manager import get_courses_context
from rag_service import rag_call
from prompt import prompt
from llm_provider import get_llm
# ---------------------------------------------------------
# DB CALL
# ---------------------------------------------------------
def db_call(question: str):
    """
    Get course data from MySQL.
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
            "question":  # lambda is a small anonymous function
                lambda question: question # whatever question you give me, return the same question
        }
        # Send all data to prompt
        | prompt  # pipeline means pass the output of 1 component to the next component 
        # Send prompt to Ollama
        | get_llm()  # db_call -> rag_call -> question -> prompt -> get_llm()
    )
    return chain
# ---------------------------------------------------------
# Create chain
# ---------------------------------------------------------
chain = build_chain() #create the machine/pipeline
# ---------------------------------------------------------
# Ask student
# ---------------------------------------------------------
def ask_student(question: str): # ask_student is like front desk reception counter
    """
    Send question through complete pipeline.
    Student ask in the front_desk(ask_student) "What is the Python course fee?"
    """
    answer = chain.invoke(question) #run the chain/pipeline and get the answer box
    return answer.content # from answer box, retrieve the contents

"""
"What is the Python course fee?"
                │
                ▼
       ┌─────────────────┐
       │     DB CALL     │
       └─────────────────┘
                │
                ▼
          course_data
                │

"What is the Python course fee?"
                │
                ▼
       ┌─────────────────┐
       │    RAG CALL     │
       └─────────────────┘
                │
                ▼
          policy_data
                │

                ▼
       ┌─────────────────┐
       │      PROMPT     │
       └─────────────────┘
                │
                ▼
       ┌─────────────────┐
       │     OLLAMA      │
       └─────────────────┘
                │
                ▼
             answer
"""
