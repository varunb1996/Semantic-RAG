import faiss
import numpy as np

class VectorDB:
    def __init__(self, dim):
        self.index = faiss.IndexFlatL2(dim)
        self.texts = []
        self.meta = []

    def add(self, embeddings, texts, metadata):
        self.index.add(np.array(embeddings))
        self.texts.extend(texts)
        self.meta.extend(metadata)

    def search(self, query_embedding, top_k=5, filter_category=None):
        D, I = self.index.search(np.array([query_embedding]), top_k * 2)

        results = []

        for idx in I[0]:
            if filter_category:
                if self.meta[idx]["category"] != filter_category:
                    continue

            results.append(self.texts[idx])

            if len(results) == top_k:
                break

        return results