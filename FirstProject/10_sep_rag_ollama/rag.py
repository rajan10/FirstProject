
import chromadb
import ollama

# ==========================================
# Configuration
# ==========================================

KNOWLEDGE_FILE = "documents/knowledge.txt"

CHROMA_PATH = "./chroma_db"

COLLECTION_NAME = "company_knowledge"

OLLAMA_URL = "http://localhost:11434"

EMBEDDING_MODEL = "embeddinggemma"

LLM_MODEL = "llama3.2"

chroma_client=chromadb.PersistentClient(path=CHROMA_PATH)  # Create a persistent ChromaDB client with the specified path
collection=chroma_client.get_or_create_collection(name=COLLECTION_NAME)  # Get or create a collection named "company_knowledge" 

def ask_question(question):

    # create embedding for the question
    response = ollama.embed(
        model = EMBEDDING_MODEL,
        input = question
    )

    question_embedding = response.embeddings[0]

    # search chroma DB
    results = collection.query(
        query_embeddings = question_embedding,
        n_results = 3
    )
# Testing print result
    print("Results:", results)

    # Get Retrieved Documents
    documents = results["documents"][0]

    print("documents:", documents)

    #combine documents into context
    context = "\n\n".join(documents)

    print("Context:", context)

    # Create RAG Prompt
    prompt = f"""
    
    Answer the question using the context provided below. If not found in the context, say "I don't know". Do not make up an answer.
    
    Context : {context}
    
    Question : {question}

    """

    response = ollama.generate(
        model = LLM_MODEL,
        prompt = prompt
    )

  
    answer = response["response"]
    return answer


# simple test to run
if __name__ == "__main__":
    question = input("Ask a question:")
    answer = ask_question(question)
    print("\n==============================")
    print("ANSWER")
    print("==============================")
    print(answer)         
