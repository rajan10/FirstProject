
#open the cupboard(.env file) and bring the configuration to the applicaiton; env loader
from dotenv import load_dotenv
import os  #interacting with the os including accessing the environment variables


load_dotenv()  

DB_NAME = os.getenv("DATABASE_NAME")

OLLAMA_MODEL = os.getenv("OLLAMA_MODEL")

OLLAMA_TEMPERATURE = os.getenv("OLLAMA_TEMPERATURE")

EXTERNAL_API_URL = os.getenv("EXTERNAL_API_URL")

"""
          .env
        ┌─────────────────────┐
        │ OLLAMA_MODEL=llama3.2
        │ OLLAMA_TEMPERATURE=0
        │ DATABASE_NAME=students.db
        │ EXTERNAL_API_URL=...
        └──────────┬──────────┘
                   │
                   │ load_dotenv()
                   ▼
             settings.py
        ┌─────────────────────┐
        │ os.getenv(...)      │
        │                     │
        │ OLLAMA_MODEL        │
        │ OLLAMA_TEMPERATURE  │
        │ DB_NAME             │
        │ EXTERNAL_API_URL    │
        └──────────┬──────────┘
                   │
                   ▼
             Your application
        ┌─────────────────────┐
        │ app.py              │
        │ database.py         │
        │ ollama_service.py   │
        │ api_service.py      │
        └─────────────────────┘

.env = STORE
settings.py = READ
app.py = USE

.env stores → settings.py reads → application uses

"""