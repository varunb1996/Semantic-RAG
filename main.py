import os
import requests
from dotenv import load_dotenv
from rag import SemanticRAG
import os
from dotenv import load_dotenv

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
env_path = os.path.join(BASE_DIR, ".env")

load_dotenv(env_path)
API_KEY = os.getenv("OPENROUTER_API_KEY")
print("API_KEY", API_KEY)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_path = os.path.join(BASE_DIR, "data", "processed", "documents.json")

rag = SemanticRAG(data_path)

def ask(query, category=None):
    context = rag.retrieve(query, category)

    prompt = f"""
You are an expert AI system designer.

Use the context below to answer clearly:

Context:
{context}

Question:
{query}

Answer:
"""

    res = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "nvidia/nemotron-3-super-120b-a12b:free",
            "messages": [{"role": "user", "content": prompt}]
        }
    )

    data = res.json()

    #Debug print (VERY IMPORTANT for now)
    print("\n===== OPENROUTER RESPONSE =====")
    print(data)
    print("================================\n")

    #Handle API errors safely
    if "choices" not in data:
        return f"❌ API Error: {data}"

    return data["choices"][0]["message"]["content"]

if __name__ == "__main__":
    q = input("Query: ")
    print(ask(q))