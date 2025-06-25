# 📄 Document Ingestion — Turning PDFs into AI Memory

The `ingest.py` file is the first step in making your documents searchable by the chatbot. It loads files from the `data/` folder, breaks them into chunks, and stores vector embeddings into ChromaDB.

> _Think of this step like uploading your brain into a searchable library._

---

## 📁 Supported File Types

You can place any of the following into the `/data` folder:

- `.pdf` — Floorplanning specs, reports, etc.
- `.docx` — Design notes or project logs
- `.pptx` — Slide decks or onboarding material
- `.txt` — Clean text references

---

## 🔄 Ingestion Pipeline Flow

[Document File]
↓
[Text Extraction]
↓
[Chunking (with overlap)]
↓
[Text Embeddings]
↓
[Store in ChromaDB]


---

## 🛠️ Step-by-Step Breakdown

### 1. **Load Files from `/data` Folder**

Using `PyMuPDF`, `python-docx`, and `python-pptx`, the script extracts raw text from supported file types.

```python
documents = SimpleDirectoryReader("data").load_data()

2. Split Text into Chunks
Large documents are broken down into smaller overlapping chunks using the RecursiveCharacterTextSplitter:

chunk_size = 500

chunk_overlap = 50

Why? Because LLMs have input limits, and smaller chunks improve retrieval accuracy.

3. Embed the Text Chunks
Each chunk is converted to a vector embedding using a SentenceTransformer model:
model = SentenceTransformer("all-MiniLM-L6-v2")
Each vector is a list of 384–768 float values representing the semantic meaning of the text.

4. Store in ChromaDB (Vector DB)
The resulting embeddings and metadata (file name, chunk ID, etc.) are stored in a local ChromaDB database:

chroma_client = chromadb.PersistentClient(path="./chromadb")
collection = chroma_client.get_or_create_collection("vlsi_docs")

This creates the memory layer that the chatbot later queries.

🧪 Example Output Chunk

{
  "id": "chunk-1042",
  "text": "Tap cells are placed regularly to prevent latch-up...",
  "source": "data/floorplan_basics.pdf"
}

❓ FAQs
❌ What happens if the file is over 100MB?
You should not place large files directly. Either:

Compress or split the PDF, or

Extract only the useful pages

🔄 Can I update the data later?
Yes! Just add new files to data/, then rerun:

python ingest.py

It will embed and store the new content.