import requests


OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL = "llama2:latest"


def ask_ollama(messages):

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "messages": messages,
            "stream": False
        },
        timeout=120
    )

    response.raise_for_status()

    data = response.json()

    return data["message"]["content"]