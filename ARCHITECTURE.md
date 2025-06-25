# 🧠 RAG Architecture — How This Chatbot Works

This chatbot is built using the **Retrieval-Augmented Generation (RAG)** framework. Instead of relying solely on the language model's memory, it **retrieves relevant chunks from your own documents** and feeds them into the local LLM to answer your question.

---

## 🏗️ Overall Architecture Flow

[User Query]
↓
[Embed Query]
↓
[ChromaDB] ←→ [Pre-embedded Chunks from Docs]
↓
[Top-K Matches]
↓
[LLM Prompt: Query + Retrieved Chunks]
↓
[Local Answer Generated]

---

## 🔧 Main Components

### 1. **Document Ingestion Pipeline (`ingest.py`)**

When you run `ingest.py`, the following steps happen:

| Step | Description |
|------|-------------|
| 🔍 Read Files | Loads `.pdf`, `.docx`, `.pptx`, `.txt` from `data/` folder |
| 📃 Text Splitting | Breaks large text into small chunks (with context overlap) |
| 🔤 Embedding | Converts each chunk into a vector using `sentence-transformers` |
| 💾 ChromaDB | Stores all vectors and metadata into a local persistent DB |

---

### 2. **Query Handling Pipeline (`chatbot.py`)**

When the user asks a question:

| Step | Description |
|------|-------------|
| 🧠 Embed Query | Converts user question into a vector |
| 📡 Vector Search | Finds the most relevant chunks from ChromaDB |
| 🧩 Construct Prompt | Concatenates: system prompt + top-k chunks + user question |
| 🦙 LLM Response | Local LLM (Mistral-7B) generates the final answer |

---

## 🤖 Why Use RAG?

- LLMs (even GPT-4) **don’t know your documents**
- RAG makes them “appear smart” by **feeding them real context**
- You get **custom answers without fine-tuning or retraining**

---

## 🧠 Local LLM: `llama-cpp-python`

- Model format: `.gguf` (Quantized Mistral-7B Instruct)
- Run via: `llama_cpp.Llama` class
- Benefits:
  - 100% offline
  - Runs on CPU (AVX2+)
  - Fast inference with quantized model (Q4_0)

---

## 📦 Vector Store: ChromaDB

- Light, fast, and local
- Uses DuckDB under the hood
- Persists embeddings in `./chromadb/` folder

---

## 🔡 Embeddings: `sentence-transformers`

- Model: `all-MiniLM-L6-v2`
- Fast and small (384 or 768 dims)
- Converts all text into numerical vectors for comparison

---

## 🧪 Prompt Format Example

```text
System: You are a VLSI design assistant. Use only the provided context to answer.
---
Context:
1. "A decap cell is used to provide local capacitance and reduce IR drop..."
2. "Tie-high and tie-low cells help avoid floating nodes in digital logic..."
---
Question: What is the function of tie-low cells?
