from state.chat_state import ChatState
from knowledge.course_knowledge import COURSE_KNOWLEDGE

from langchain_core.documents import Document
from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter


EMBED_MODEL = "embeddinggemma:latest"


def create_vector_store():
    document = Document(
        page_content=COURSE_KNOWLEDGE,
        metadata={
            "source": "course_knowledge.py"
        }
    )

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    chunks = splitter.split_documents(
        [document]
    )

    embeddings = OllamaEmbeddings(
        model=EMBED_MODEL
    )

    vector_store = FAISS.from_documents(
        chunks,
        embeddings
    )

    return vector_store


vector_store = create_vector_store()


def rag_node(state: ChatState) -> dict:
    print("Executing rag node")

    question = state.get("question", "")

    if not question:
        return {
            "context": ""
        }

    documents = vector_store.similarity_search(
        question,
        k=2
    )

    if not documents:
        return {
            "context": ""
        }

    context = "\n\n".join(
        document.page_content
        for document in documents
    )

    return {
        "context": context
    }
