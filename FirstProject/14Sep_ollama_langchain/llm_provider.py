"""
llm_provider.py
This file creates our Ollama LLM.
IMPORTANT:
We are NOT using OpenAI.

नेपाली:
यो file ले LangChain लाई local Ollama model सँग जोड्छ।
"""
import os
from dotenv import load_dotenv
from langchain_ollama import ChatOllama
# ---------------------------------------------------------
# Load .env
# ---------------------------------------------------------
load_dotenv()
# ---------------------------------------------------------
# Read Ollama model name
# ---------------------------------------------------------
MODEL = os.getenv(
    "OLLAMA_CHAT_MODEL",
    "llama3.2:3b"
)
# ---------------------------------------------------------
# Create LLM
# ---------------------------------------------------------
def get_llm():

    llm = ChatOllama(

        model=MODEL,

        # Lower temperature =
        # more focused answers
        temperature=0.2
    )

    return llm