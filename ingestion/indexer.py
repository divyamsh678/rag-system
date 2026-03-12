import faiss
import numpy as np
import pickle

class VectorIndexer:

    def __init__(self, dimension=384):
        self.index = faiss.IndexFlatL2(dimension)
        self.chunks = []

    def add_embeddings(self, chunks, embeddings):
        embeddings = np.array(embeddings).astype("float32")

        self.index.add(embeddings)

        self.chunks.extend(chunks)

    def search(self, query_embedding, top_k=5):
        query_embedding = np.array([query_embedding]).astype("float32")
        distances, indices = self.index.search(query_embedding, top_k)
        results = [self.chunks[i] for i in indices[0]]

        return results

    def save(self, index_path="faiss.index", chunk_path="chunks.pkl"):
        faiss.write_index(self.index, index_path)
        with open(chunk_path, "wb") as f:
            pickle.dump(self.chunks, f)

    def load(self, index_path="faiss.index", chunk_path="chunks.pkl"):
        self.index = faiss.read_index(index_path)
        with open(chunk_path, "rb") as f:
            self.chunks = pickle.load(f)
