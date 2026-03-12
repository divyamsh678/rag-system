import numpy as np
from ingestion.embedding import Embedder

class Retriever:
    def __init__(self,indexer):
        self.indexer=indexer
        self.embedder=Embedder()
    def retrieve(self,query,top_k=5):
        query_embedding=self.embedder.embed_text(query)
        query_embedding=np.array([query_embedding]).astype("float32")
        distances,indices=self.indexer.index.search(query_embedding,top_k)
        results=[self.indexer.chunks[i] for i in indices[0]]
        return results