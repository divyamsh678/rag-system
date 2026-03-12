from sentence_transformers import SentenceTransformer


class Embedder:
    def __init__(self, model_name="all-MiniLM-L6-v2"):
        """
        Initialize embedding model
        """
        self.model = SentenceTransformer(model_name)

    def embed_text(self, text: str):
        """
        Generate embedding for a single text
        """
        embedding = self.model.encode(text)
        return embedding

    def embed_chunks(self, chunks: list):
        """
        Generate embeddings for list of chunks
        """
        embeddings = self.model.encode(chunks)
        return embeddings
