🎓 Student GEN-AI Chatbot

A local Generative AI Student Chatbot built with Streamlit, LangChain, MySQL, RAG, FAISS, Ollama, and local embedding models.

The chatbot allows students to ask questions about:

📚 Available courses
💰 Course fees
⏱️ Course duration
📖 Course descriptions
📜 Institute policies
🎓 Academic rules

The application uses MySQL for structured course information and RAG/FAISS for institute policy information, while Ollama provides the local LLM.

🚀 Project Overview
                     🎓 STUDENT
                          │
                          │ Question
                          ▼
                ┌─────────────────────┐
                │     STREAMLIT       │
                │       app.py        │
                │    Web Interface    │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │      LANGCHAIN      │
                │    lang_chain.py    │
                └──────────┬──────────┘
                           │
             ┌─────────────┴─────────────┐
             │                           │
             ▼                           ▼
      🗄️ MYSQL DATABASE             📚 RAG SYSTEM
       courses_info                 policy.txt
             │                           │
             │                           ▼
             │                    Text Splitting
             │                           │
             │                           ▼
             │                    Ollama Embeddings
             │                  embeddinggemma:latest
             │                           │
             │                           ▼
             │                         FAISS
             │                           │
             └──────────────┬────────────┘
                            │
                            ▼
                     📝 PROMPT
                     prompt.py
                            │
                            ▼
                     🦙 OLLAMA LLM
                     llama3.2:latest
                            │
                            ▼
                       🤖 ANSWER
                            │
                            ▼
                     STREAMLIT UI
🧠 How the Chatbot Works

The application follows this basic sequence:

Student Question
       │
       ▼
   Streamlit
       │
       ▼
   LangChain
       │
       ├──────────────► MySQL
       │                    │
       │                    ▼
       │              Course Information
       │
       └──────────────► RAG / FAISS
                            │
                            ▼
                       Policy Information
                            │
                            ▼
                         Prompt
                            │
                            ▼
                    Ollama llama3.2
                            │
                            ▼
                         Answer
                            │
                            ▼
                       Student

✨ Features
📚 Course Information

Course information is stored in MySQL.

Current sample courses:

Code	Course	Duration	Fee
CS101	Python Programming	3 months	$750
CS102	Java Programming	2 months	$850
CS103	JavaScript Programming	3 months	$950
CS104	GenAI Programming	4 months	$1,000

The chatbot can answer questions such as:

What courses are available?

What is the fee for Python Programming?

How long is the GenAI Programming course?

Tell me about Java Programming.
📖 RAG-Based Policy Questions

Institute policies are stored in:

Documents/policy.txt

The RAG pipeline processes this document using:

policy.txt
     │
     ▼
Document Loader
     │
     ▼
Text Splitter
     │
     ▼
Ollama Embeddings
embeddinggemma:latest
     │
     ▼
FAISS Vector Store

Students can ask:

What is the withdrawal policy?

What is the attendance requirement?

Can I submit an assignment late?

What happens if I cheat?

What is the plagiarism policy?
🧩 Technology Stack
Technology	Purpose
🐍 Python	Main programming language
🎨 Streamlit	Web user interface
🔗 LangChain	LLM orchestration
🗄️ MySQL	Course information
🔎 FAISS	Vector similarity search
🧠 Ollama	Local LLM and embeddings
🦙 llama3.2	Chat/LLM model
🔤 embeddinggemma	Embedding model
📝 python-dotenv	Environment configuration
🐼 SQLAlchemy	Database connection
🔌 PyMySQL	MySQL driver
📁 Project Structure
14Sep_ollama_langchain/
│
├── 📄 README.md
├── 📄 .env
├── 📄 .env.example
├── 📄 requirements.txt
│
├── 🎨 app.py
│
├── 🗄️ db_manager.py
├── 📥 data_ingest.py
│
├── 📚 rag_service.py
├── 📝 prompt.py
├── 🦙 llm_provider.py
├── 🔗 lang_chain.py
│
├── 🧪 test.py
│
└── 📂 Documents/
    └── 📄 policy.txt
📄 File Responsibilities
app.py

The Streamlit frontend.

Responsible for:

Displaying the chatbot
Accepting student questions
Displaying chat history
Calling ask_student()
Showing the generated answer
Student
   ↓
Streamlit
   ↓
ask_student()
db_manager.py

Handles MySQL operations.

Responsible for:

Creating courses_info
Connecting to MySQL
Retrieving courses
Formatting course information

Main functions:

create_courses_table()
get_courses()
get_courses_context()
data_ingest.py

Loads sample course data into MySQL.

Example:

CS101 → Python Programming
CS102 → Java Programming
CS103 → JavaScript Programming
CS104 → GenAI Programming

Run:

python data_ingest.py
rag_service.py

Implements the RAG pipeline.

policy.txt
    ↓
Document
    ↓
Chunking
    ↓
embeddinggemma
    ↓
FAISS
    ↓
Similarity Search

Main function:

rag_call(question)
prompt.py

Contains the instructions sent to the LLM.

The prompt combines:

Course Data
     +
Policy Data
     +
Student Question

into one prompt.

llm_provider.py

Connects LangChain to Ollama.

Current model:

llama3.2:latest
lang_chain.py

The orchestration layer.

It connects:

MySQL
   +
RAG
   +
Prompt
   +
Ollama

Main function:

ask_student(question)

🔄 Detailed Execution Flow
1️⃣ Application Startup

Run:

streamlit run app.py

Streamlit loads:

app.py
   │
   ▼
lang_chain.py
   │
   ├── db_manager.py
   ├── rag_service.py
   ├── prompt.py
   └── llm_provider.py
2️⃣ RAG Initialization

During startup:

Documents/policy.txt
        │
        ▼
   Load Document
        │
        ▼
   Split into Chunks
        │
        ▼
embeddinggemma:latest
        │
        ▼
     Embeddings
        │
        ▼
       FAISS

FAISS is now ready to search for relevant policy information.

3️⃣ Student Asks a Question

Example:

What courses are available?

Streamlit calls:

ask_student(question)
4️⃣ LangChain Calls Data Sources

The current chain calls:

                    Question
                        │
                        ▼
                   LangChain
                  /          \
                 /            \
                ▼              ▼
             MySQL             RAG
                │               │
                ▼               ▼
          Course Data      Policy Data
5️⃣ MySQL Returns Course Data

MySQL returns:

CS101 - Python Programming
CS102 - Java Programming
CS103 - JavaScript Programming
CS104 - GenAI Programming
6️⃣ RAG Searches Policy

The student's question is converted into an embedding and compared against FAISS vectors.

Student Question
       │
       ▼
Embedding
       │
       ▼
FAISS Similarity Search
       │
       ▼
Relevant Policy Chunks
7️⃣ Prompt Construction

LangChain combines everything:

┌──────────────────────────────────────┐
│              PROMPT                  │
│                                      │
│ Course Data:                         │
│ CS101 Python                         │
│ CS102 Java                           │
│ CS103 JavaScript                     │
│ CS104 GenAI                          │
│                                      │
│ Policy Data:                         │
│ Relevant policy chunks...            │
│                                      │
│ Student Question:                    │
│ What courses are available?          │
└──────────────────┬───────────────────┘
                   │
                   ▼
8️⃣ Ollama Generates the Answer
Prompt
  │
  ▼
Ollama
  │
  ▼
llama3.2:latest
  │
  ▼
Generated Answer
9️⃣ Streamlit Displays the Answer

The answer returns to:

st.markdown(answer)

and appears in the browser.

🛠️ Installation
1. Clone or create the project
mkdir 14Sep_ollama_langchain
cd 14Sep_ollama_langchain
2. Create virtual environment
python -m venv .ollama_langchain

Activate:

.\.ollama_langchain\Scripts\Activate.ps1

You should see:

(.ollama_langchain)
3. Install dependencies
python -m pip install -r requirements.txt

Or:

python -m pip install `
langchain `
langchain-core `
langchain-community `
langchain-ollama `
langchain-text-splitters `
faiss-cpu `
SQLAlchemy `
PyMySQL `
python-dotenv `
streamlit
🦙 Ollama Setup

Make sure Ollama is installed and running.

Check:

ollama --version

Check installed models:

ollama list

The project expects:

llama3.2:latest
embeddinggemma:latest

If they are not installed:

ollama pull llama3.2:latest
ollama pull embeddinggemma:latest
🗄️ MySQL Setup

Create the database:

CREATE DATABASE student_db;

The application uses the:

courses_info

table.

You can populate the sample courses using:

python data_ingest.py
🔐 Environment Variables

Create:

.env

Example:

MYSQL_URI=mysql+pymysql://root:YOUR_PASSWORD@localhost:3306/student_db

OLLAMA_CHAT_MODEL=llama3.2:latest

OLLAMA_EMBED_MODEL=embeddinggemma:latest