


import os
from urllib import response
import requests
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

chroma_client=chromadb.PersistentClient(path=CHROMA_PATH)  # Create a persistent ChromaDB client  as we want db to survive even after app stops
# a collection is similar to a table/container in a database, it holds the documents and their embeddings
collection=chroma_client.get_or_create_collection(name=COLLECTION_NAME)  # Get or create a collection named "company_knowledge"


with open(KNOWLEDGE_FILE, "r", encoding="utf-8" ) as file: # read  everything into the variable 
    document=file.read()

    chunks=document.split("\n\n")  # Split the document into chunks based on double newlines


#Large documents  -> chunks -> embeddings -> Vector DB ( store in ChromaDB )
for index, chunk in enumerate(chunks):  # chunk = Fortigate is a NGFW device.
    # Create an embedding for the chunk using Ollama's embedding model
    response=ollama.embed(
            model=EMBEDDING_MODEL,
            input=chunk,
        )

    #print("Response", response)

#the entire repsone from ollama.embed() is a list of list with keys: model, embeddings, and input. The embeddings key contains a list of
#  embeddings for the input text. Since we are embedding one chunk at a time, we access the first embedding in the list using
# response.embeddings[0]. This gives us the embedding vector for the chunk, which we can then store in ChromaDB along with the chunk itself.
    embedding = response.embeddings[0]  # Get the first embedding for the chunk  embedding=[10,20,30,40,50]  # This is a vector representation of the chunk
    
    collection.upsert(
        ids=[f"knowledge_chunk_{index}"],  # Use the same unique ID for the embedding eg "knowledge_chunk_0" for the first chunk, 
        # "knowledge_chunk_1" for the second chunk, and so on. This ensures that each chunk has a unique identifier in the collection.
        documents=[chunk],  # Add the chunk as a document to the collection eg Fortigate is a NGFW device.
        embeddings=[embedding]  # Add the embedding to the collection eg [10,20,30,40,50]  # This is a vector representation of the chunk
    )
    print(f"Document added to ChromaDB collection: {chunk}")  # Print a message indicating that the document has been added
    print(f"Total documents: {collection.count()}")