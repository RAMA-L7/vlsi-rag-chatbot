# 🗂 Folder Structure — What Each File and Folder Does

This project is structured to separate code, data, embeddings, and models clearly. Below is a breakdown of each major component.

---

## 📁 Root Directory

vlsi-rag-chatbot/
├── chatbot.py
├── ingest.py
├── requirements.txt
├── .gitignore
├── chromadb/
├── data/
├── models/
├── .venv/
├── *.md (documentation files)


---

## 🔹 `chatbot.py`

The **main app** that runs your RAG chatbot using Gradio UI.

- Loads the local GGUF model (e.g., Mistral-7B)
- Queries ChromaDB with user questions
- Builds a prompt and generates answers

---

## 🔹 `ingest.py`

This is the **data preprocessing script**. It:

- Loads and cleans files from `/data`
- Splits documents into manageable chunks
- Embeds each chunk using `sentence-transformers`
- Stores everything into `ChromaDB`

You run this **every time you update your documents.**

---

## 📁 `/data`

Put your `.pdf`, `.pptx`, `.docx`, or `.txt` files here.

| Type | Example |
|------|---------|
| PDF  | Floorplanning specs, IR drop analysis |
| PPTX | Onboarding decks, design flows |
| DOCX | Timing closure SOP, RTL notes |
| TXT  | Clean summaries or extracted rules |

> _Tip: Avoid files over 100 MB — split or summarize instead._

---

## 📁 `/models`

Put your **quantized `.gguf` model file** here.

Example:  
mistral-7b-instruct-v0.1.Q4_0.gguf

This is what powers the LLM locally using `llama-cpp-python`.

---

## 📁 `/chromadb`

This is the **local vector database** created automatically by ChromaDB.

It stores:
- All document embeddings
- Metadata like file name, chunk number
- Persistent storage between runs

---

## 📁 `/.venv`

Optional: This folder is created when you set up your Python virtual environment.

> _Do not commit this to Git — it’s local-only and should be in `.gitignore`._

---

## 📄 `requirements.txt`

Contains all Python packages needed to run the project:

- `llama-cpp-python`
- `chromadb`
- `sentence-transformers`
- `gradio`
- `PyMuPDF`, `python-docx`, `python-pptx`

> Run: `pip install -r requirements.txt` to install them.

---

## 📄 `.gitignore`

Specifies which files/folders Git should **not track**.

Includes:
- `.venv/`
- `/chromadb/`
- Any large files like `.pdf`, `.pptx` if added

---

## 📝 `.md` Files (Docs)

All project documentation lives here. Includes:

- `README.md`
- `ARCHITECTURE.md`
- `INGESTION.md`
- `SETUP_GUIDE.md`
- `FOLDER_STRUCTURE.md`
- `FUTURE_PLANS.md`

---

## ✅ Summary

Your project is cleanly organized for:

- Local document-based QA
- Easy debugging and updates
- GitHub portfolio visibility

> _You now have a real, working AI chatbot — but designed for your own chip design world._

---

