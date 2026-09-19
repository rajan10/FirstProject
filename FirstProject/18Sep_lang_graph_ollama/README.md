# Student Support Chatbot

An Agentic AI student-support chatbot built with Python, LangGraph, Ollama, RAG, FAISS, and Streamlit.

## Features

- Local LLM using Ollama
- LangGraph-based AI workflow
- Retrieval-Augmented Generation (RAG)
- Ollama embeddings
- FAISS vector store
- SQLite database
- Streamlit web interface
- Course information retrieval
- Student-support chatbot workflow

## Technologies

- Python
- Streamlit
- LangGraph
- LangChain
- Ollama
- FAISS
- SQLite

## Project Structure

18Sep_lang_graph_ollama/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── graph/
│   └── student_support_graph.py
│
├── nodes/
│   ├── database_node.py
│   └── rag_node.py
│
├── state/
│   └── chat_state.py
│
├── knowledge/
│   └── course_knowledge.py
│
└── database/
    └── ...
Setup
1. Clone the repository
git clone <your-github-repository-url>
cd 18Sep_lang_graph_ollama
2. Create a virtual environment
python -m venv .venv
3. Activate the virtual environment

Windows PowerShell:

.\.venv\Scripts\Activate.ps1
4. Install dependencies
pip install -r requirements.txt
5. Install Ollama

Make sure Ollama is installed and running.

Check available models:

ollama list

Pull the required models if they are not already installed:

ollama pull llama3.2:latest
ollama pull embeddinggemma:latest
Run the Application

Start the Streamlit application:

streamlit run app.py

The application will open in your browser.

RAG Workflow
Course Knowledge
       ↓
   Documents
       ↓
 Text Chunking
       ↓
Ollama Embeddings
       ↓
      FAISS
       ↓
 Student Question
       ↓
Similarity Search
       ↓
Relevant Context
       ↓
   LangGraph
       ↓
     Ollama
       ↓
    Response

Purpose

This project is designed as a learning project for understanding:

Agentic AI
LangGraph
RAG
Vector databases
Embeddings
Local LLMs
AI application development
Streamlit