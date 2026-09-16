"""
rag_service.py
============================================================
Purpose:
    This file implements the RAG (Retrieval-Augmented Generation)
    part of our Student GEN-AI Chatbot.

Architecture:
    policy.txt
        |
        v
    Load document
        |
        v
    Split into chunks
        |
        v
    Ollama Embeddings
    embeddinggemma:latest
        |
        v
    FAISS Vector Store
        |
        v
    Student Question
        |
        v
    Similarity Search
        |
        v
    Relevant Policy
        |
        v
    Send to Prompt / Ollama LLM

यो file को मुख्य काम institute को policy document बाट
student को question अनुसार relevant information खोज्नु हो।
Flow:
    policy.txt
        ↓
    document पढ्ने
        ↓
    chunks बनाउने
        ↓
    Ollama embedding बनाउने
        ↓
    FAISS मा vector राख्ने
        ↓
    Student question आउने
        ↓
    Similarity search गर्ने
        ↓
    Relevant policy निकाल्ने
"""
# ============================================================
# 1. IMPORT LIBRARIES
# ============================================================
import os
from pathlib import Path
from langchain_core.documents import Document
from langchain_community.vectorstores import FAISS  # FAISS is your vector database/search mechanism. 
# Facebook AI Similarity Search.FAISS लाई vector librarian जस्तो सम्झनुहोस्
# "Shelf number 7 मा withdrawal सम्बन्धी paragraph छ!
from langchain_ollama import OllamaEmbeddings
# An embedding isn't simply:
# "convert words into random numbers."
# It creates a numerical representation intended to capture semantic relationships.
from langchain_text_splitters import RecursiveCharacterTextSplitter
# RecursiveCharacterTextSplitter intelligently tries different separators when splitting text

# own mini .env loader.
def load_dotenv(dotenv_path=".env"):
    env_file = Path(dotenv_path)
    if not env_file.is_file():
        return

    for line in env_file.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))
# ============================================================
# 2. LOAD ENVIRONMENT VARIABLES
# ============================================================
"""
load_dotenv() reads the .env file.
For example:
OLLAMA_EMBED_MODEL=embeddinggemma:latest
load_dotenv() ले .env file पढ्छ।
त्यसबाट Ollama embedding model को नाम
हामीले लिन सक्छौं।
"""
load_dotenv()
# ============================================================
# 3. GET OLLAMA EMBEDDING MODEL
# ============================================================
"""
Read the embedding model name from .env.
If .env does not contain the value,
use embeddinggemma:latest as the default.
.env मा embedding model को नाम छ भने त्यो प्रयोग गर्छ।
नभए default रूपमा embeddinggemma:latest प्रयोग गर्छ।
"""
EMBED_MODEL = os.getenv(
    "OLLAMA_EMBED_MODEL",
    "embeddinggemma:latest"
)
# ============================================================
# 4. FIND POLICY FILE
# ============================================================
"""
Path to our policy document:
Documents/policy.txt
हाम्रो institute policy document को location
Documents/policy.txt हो।
"""
POLICY_FILE = (   # __file__ implies current file which is rag_service.py
    Path(__file__).parent  # get the dir containing rag_service.py 14Sep_ollama_langchain\Documents
    / "Documents"
    / "policy.txt"
)
# ============================================================
# 5. LOAD POLICY DOCUMENT
# ============================================================
def load_policy_documents():
    """
    Read policy.txt and convert it into a LangChain Document.
    policy.txt पढेर LangChain Document बनाउँछ।
    """
    # --------------------------------------------------------
    # Read policy.txt
    # --------------------------------------------------------
    policy_text = POLICY_FILE.read_text(
        encoding="utf-8"
    )
    # --------------------------------------------------------
    # Create LangChain Document
    # --------------------------------------------------------
    document = Document(  # convert raw text into a LangChain Document
        # Actual policy content
        page_content=policy_text,
        # Meta data
        metadata={
            "source": "Documents/policy.txt"
        }
    )
    # Return a list because LangChain works with a collection of documents later staring today with just 1 Document
    return [document] 
# ============================================================
# 6. CREATE VECTOR STORE
# ============================================================
def build_vector_store():
    """
    Build our FAISS vector database.
    Steps:
        1. Load policy
        2. Split policy into chunks
        3. Create Ollama embeddings
        4. Store embeddings in FAISS
    """
    # ========================================================
    # STEP 1: LOAD DOCUMENT
    # ========================================================
    documents = load_policy_documents() # documents= [document1, document1, document3, ..]
    # ========================================================
    # STEP 2: SPLIT DOCUMENT INTO CHUNKS
    # ========================================================
    """
    Large documents are split into smaller pieces.
    chunk_size = 500
        Maximum approximate size of each chunk.
    chunk_overlap = 50
        Some text is repeated between chunks.
    ठूलो document लाई सानो-सानो भागमा विभाजन गर्छ।
    chunk_size = 500
        लगभग 500 characters सम्मको chunk।
    chunk_overlap = 50
        अर्को chunk मा अघिल्लो chunk को केही text
        repeat हुन्छ।
    Example
      Chunk 1:
        "Students can withdraw ... official deadline..."
        Chunk 2:
        "... official deadline ... academic office..."
    यसले context हराउन नदिने मद्दत गर्छ।
    """
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )
    # Actually split the document
    chunks = splitter.split_documents(documents)
    # ========================================================
    # STEP 3: CREATE OLLAMA EMBEDDINGS
    # ========================================================
    """
    Ollama converts each text chunk into a numerical vector.
    Model:
        embeddinggemma:latest
    Ollama ले text लाई numerical vector मा convert गर्छ।
    Example:
        "withdrawal policy"
                ↓
        [0.12, -0.44, 0.83, ...]
    Similar meanings produce similar vectors.
    """
    embeddings = OllamaEmbeddings(model=EMBED_MODEL)
    # ========================================================
    # STEP 4: CREATE FAISS VECTOR STORE
    # ========================================================
    """
    FAISS stores the vectors and allows fast similarity search.
    FAISS ले vectors store गर्छ र question सँग
    सबैभन्दा मिल्ने document खोज्न मद्दत गर्छ।
    """
    vector_store = FAISS.from_documents(chunks,embeddings)
    # Return the completed vector store
    return vector_store
# ============================================================
# 7. BUILD VECTOR STORE
# ============================================================
"""
Build the vector store when this module is loaded.
यो module load हुँदा policy को vector store तयार हुन्छ।
"""
vector_store = build_vector_store()
# ============================================================
# 8. RAG CALL
# ============================================================
def rag_call(question: str):
    """
    Search the policy document for information relevant
    to the student's question.
    Student को question अनुसार policy document बाट
    relevant information खोज्छ।
    """
    # --------------------------------------------------------
    # Similarity search
    # --------------------------------------------------------
    documents = vector_store.similarity_search(
        question,
        # Return top 2 relevant chunks
        k=2
    )
    # --------------------------------------------------------
    # Check whether anything was found
    # --------------------------------------------------------
    if not documents:
        return (
            "No relevant policy was found."
        )
    # --------------------------------------------------------
    # Extract text from retrieved documents
    # --------------------------------------------------------
    policy_text = [] # This creates an empty list.
    for document in documents:
        policy_text.append(document.page_content)
    # --------------------------------------------------------
    # Combine retrieved chunks
    # --------------------------------------------------------
    return "\n\n".join(
        policy_text
    )