from ingestion.url_loader import extract_text
from ingestion.chunking import chunk_text
from ingestion.embedding import Embedder
from ingestion.indexer import VectorIndexer
from retrieval.retriever import Retriever
from generation.prompt import build_prompt
from generation.llm import LLM
from ingestion.pdf_loader import extract_text as extract_pdf_text

def build_index(url):
    text=extract_text(url)
    chunks=chunk_text(text)
    embedder=Embedder()
    embeddings=embedder.embed_chunks(chunks)
    indexer=VectorIndexer()
    indexer.add_embeddings(chunks,embeddings)
    return indexer

if __name__=="__main__":
    choice = input("pdf or url")
    if choice == "pdf":
        file_path=input("Enter PDF path: ")
        text=extract_pdf_text(file_path)
        chunks=chunk_text(text)
        embedder=Embedder()
        embeddings=embedder.embed_chunks(chunks)
        indexer=VectorIndexer()
        indexer.add_embeddings(chunks,embeddings)
        retriever=Retriever(indexer)
        llm=LLM()
        while True:
            question=input("\nAsk a question (exit to quit): ")
            if question=="exit":
                break
            contexts=retriever.retrieve(question)
            prompt=build_prompt(question,contexts)
            answer=llm.generate(prompt)
            print("\nAnswer:\n",answer)
    else:
        url="https://en.wikipedia.org/wiki/IPhone"
        indexer=build_index(url)
        retriever=Retriever(indexer)
        llm=LLM()
        while True:
            question=input("\nAsk a question (exit to quit): ")
            if question=="exit":
                break
            contexts=retriever.retrieve(question)
            prompt=build_prompt(question,contexts)
            answer=llm.generate(prompt)
            print("\nAnswer:\n",answer)