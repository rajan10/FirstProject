
from openai import OpenAI
import os
from dotenv import load_dotenv


from urllib import response


# Loading env variables from .env file
load_dotenv()

# Read OpenAI API key from environment variable
api_key = os.getenv("OPEN_API_KEY")

# Create OpenAI client with the API key
client = OpenAI(api_key=api_key)

# Function to call GPT Model
def ask_gpt(input):
    response = client.responses.create(
        model="gpt-5-mini",
        input=input
    )
    return response.output_text
