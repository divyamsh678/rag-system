# Retrieval-Augmented Generation (RAG) System

A simple end-to-end **Retrieval-Augmented Generation (RAG)** system that can ingest documents (PDF or URLs), index them using embeddings, and answer questions based on the retrieved context.

This project demonstrates how modern AI systems combine **vector search + LLM reasoning** to answer questions grounded in external knowledge.

---

## Features

* Ingest **PDF documents**
* Ingest **web pages (URLs)**
* Automatic **text extraction**
* **Chunking with overlap** for better retrieval
* **Embedding generation**
* **FAISS vector database** for similarity search
* **Retriever → Prompt → LLM pipeline**
* Uses **Hugging Face Router API** for LLM inference
* Simple **Streamlit UI** for interaction

---

## System Architecture

Document → Text Extraction → Chunking → Embeddings → Vector Index (FAISS) → Retrieval → Prompt Construction → LLM → Answer

---

## Project Structure

```
rag-system/

ingestion/
    pdf_loader.py
    url_loader.py
    chunking.py
    embeddings.py
    indexer.py

retrieval/
    retriever.py

generation/
    prompt.py
    llm.py

app.py
main.py

requirements.txt
.env.example
README.md
```

---

## Installation

Clone the repository:

```
git clone https://github.com/YOUR_USERNAME/rag-system.git
cd rag-system
```

Install dependencies:

```
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file and add the below line with your Hugging face token

Example:

```
HF_TOKEN=your_huggingface_token
```

This token is used to access models through the Hugging Face Router API.

---

## Running the CLI Version

```
python main.py
```

You can choose:

```
pdf
url
```

Then ask questions about the indexed document.

---

## Running the Web Interface

```
streamlit run app.py
```

This launches a simple UI where you can:

* Upload PDFs
* Provide URLs
* Ask questions about the indexed content

---

## Technologies Used

* Python
* FAISS (vector search)
* Sentence Transformers (embeddings)
* Hugging Face Router API (LLM inference)
* BeautifulSoup (web scraping)
* pdfplumber / pytesseract (PDF extraction)

---

## Example Use Case

Index a Wikipedia article:

```
https://en.wikipedia.org/wiki/IPhone
```

Ask questions such as:

```
Who introduced the first iPhone?
When was it released?
```

The system retrieves relevant document chunks and generates an answer using the LLM.

---

## Future Improvements

* Reranking retrieved chunks
* Multi-query retrieval
* Source citations in answers
* Hybrid search (keyword + vector)
* Multi-document indexing
* Better UI for document management