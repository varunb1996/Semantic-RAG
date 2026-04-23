# 🚀 Advanced Semantic RAG (Retrieval-Augmented Generation)

An end-to-end Semantic RAG pipeline that scrapes real-world data, processes it into embeddings, stores it in a vector database, and enables intelligent question answering using LLMs via OpenRouter.

---

## 🔧 Features

- Web scraping from real sources (Wikipedia / tech docs)
- Text cleaning + chunking
- Embedding generation (Sentence Transformers)
- Vector database for semantic search
- Metadata-aware retrieval
- LLM integration (OpenRouter - Nemotron)
- FastAPI backend for inference
- Streamlit UI for interaction

---

## 📁 Project Structure

advanced-semantic-rag/ │ ├── data/ │   ├── raw/                # scraped data │   └── processed/          # chunked documents │ ├── src/ │   ├── scraper.py          # scrape data │   ├── preprocess.py       # chunk + clean text │   ├── embed.py            # generate embeddings │   ├── vectordb.py         # vector storage │   ├── rag.py              # retrieval + generation │   ├── main.py             # core logic │   └── api.py              # FastAPI endpoints │ ├── ui/ │   └── app.py              # Streamlit UI │ ├── .env                    # API keys ├── requirements.txt └── README.md

---

## ⚙️ Setup Instructions

### 1. Clone Repo
```bash
git clone https://github.com/varunb1996/Semantic-RAG.git
cd advanced-semantic-rag

Create virtual environment 

python -m venv venv
venv\Scripts\activate

Install Dependencies

pip install -r requirements.txt

Create a .env file in root:

OPENROUTER_API_KEY=your_api_key_here

Run Pipeline 
Step 1: Scrape Data
cd src
python scraper.py

Step 2: Preprocess + Chunk
python preprocess.py

Step 3: Generate Embeddings
python embed.py

Run Backend API
python -m uvicorn api:app --reload
Open: http://127.0.0.1:8000/docs⁠�

Run UI

Open a new terminal:
cd ui
python -m streamlit run app.py

Example Query
docker vs kubernetes
what is kafka used for
explain microservices architecture

Tech Stack
Python
Sentence Transformers
FastAPI
Streamlit
OpenRouter (LLM)
Custom Vector DB

Notes
Uses fully free tools (no paid APIs required)
Scalable to large datasets via chunking
Easily extendable with other domains

Future Improvements
Hybrid search (BM25 + vector)
Reranking models
Persistent vector DB (FAISS / Chroma)
Docker deployment
