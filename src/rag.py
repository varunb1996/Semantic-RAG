import json
from embed import embed
from vectordb import VectorDB

class SemanticRAG:
    def __init__(self, path):
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)

        texts = [d["text"] for d in data]

        if len(texts) == 0:
            raise ValueError("No data found. Run scraper and preprocess first.")

        metadata = [{"category": d["category"]} for d in data]

        embeddings = embed(texts)

        self.db = VectorDB(len(embeddings[0]))
        self.db.add(embeddings, texts, metadata)

    def retrieve(self, query, category=None):
        query_embedding = embed([query])[0]
        results = self.db.search(query_embedding, filter_category=category)
        return "\n".join(results)