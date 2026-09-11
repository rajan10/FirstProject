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

def ask_question(question):
    # Create an embedding for the question
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=question
    )

    question_embedding = response.data[0].embedding

    # Query the ChromaDB collection for relevant documents based on the question embedding
    results = collection.query(
        query_embeddings=[question_embedding],
        n_results=3  # Retrieve the top 3 relevant documents
    )

    # Extract the retrieved documents from the results
    retrieved_docs = results['documents'][0] 
                

    # Combine the retrieved documents into a single context string
    context = "\n\n".join(retrieved_docs)

    # Create a prompt for GPT-5 Mini using the question and context
    prompt = f"""
    Answer the  question using only the 
     context provided below.
      Context : {context} 
      Question : {question}
      """
    

    # Use the OpenAI client to get a response from GPT-5 Mini
    response = client.responses.create(
        model="gpt-5.6"
       input =prompt
    )

    # Extract and return the content of the response
    return response.choices[0].message.content

def ask_gpt(question):
    # Call the ask_question function with the user's input and return the response
    return ask_question(question)

if __name__ == "__main__":
    # Example usage of the ask_gpt function
    user_question = "What is the company's mission statement?"
    answer = ask_gpt(user_question)
    print("Answer:", answer)