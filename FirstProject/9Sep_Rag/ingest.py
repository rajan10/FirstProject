import chromadb
import os
from dotenv import load_dotenv
from openai import OpenAI




load_dotenv()  # Load environment variables from .env file
api_key = os.getenv("OPENAI_API_KEY")  # Get the API key from environment variables
client = OpenAI(api_key=api_key)  # Initialize the OpenAI client with the API key   

#create persistent ChromaDB client
chroma_client = chromadb.PersistentClient(path="./chroma_db")  # Create a persistent ChromaDB client with the specified path

collection=chroma_client.get_or_create_collection(name="company_documents")  # Get or create a collection named "company_documents"  

#read document from file
with open("documents/company_documents.txt", "r", encoding="utf-8") as file:
    document = file.read()  # Read the contents of the file into a list of lines

chunks = document.split("\n\n")  # Split the document into chunks based on double newlines

for index, chunk in enumerate(chunks):
    response=client.embeddings.create(
        model="text-embedding-3-small",  # Specify the embedding model to use
        input=chunk
    )

    embedding=response.data[0].embedding  # Extract the embedding from the response
    collection.add(
        ids=[f"chunk-{index}"],  # Create a unique ID for each chunk
        documents=[chunk],
        embeddings=embedding
        
    )

print("Document successfully stored in ChromaDB.")  # Print a success message after storing the document