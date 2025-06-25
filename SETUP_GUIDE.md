# ⚙️ Setup Guide — Run the VLSI RAG Chatbot Locally

This guide shows you how to install, configure, and run the chatbot completely offline using your own documents.

You’ll need:
- A laptop with **Windows**, **16GB RAM**, and **VS Code**
- No OpenAI keys or paid services
- Just Python, Git, and a little curiosity

---

## ✅ 1. Clone the Project

```bash
git clone https://github.com/RAMA-L7/vlsi-rag-chatbot.git
cd vlsi-rag-chatbot
🧪 2. Create a Virtual Environment (Recommended)

python -m venv .venv
.venv\Scripts\activate  # On Windows
This keeps all dependencies isolated to this project.

📦 3. Install Dependencies

pip install -r requirements.txt
If you hit any errors with llama-cpp-python, make sure:

You have Visual Studio Build Tools installed

You selected “Desktop Development with C++”

📁 4. Add Your Documents
Place your .pdf, .docx, .pptx, or .txt files inside the /data folder:


vlsi-rag-chatbot/
├── data/
│   ├── floorplan_timing.pdf
│   ├── timing_eco_notes.docx
│   └── design_rules.pptx

🧠 5. Download LLM Model (Mistral-7B)
⚠️ You need a .gguf quantized model that works with llama-cpp-python

Go to TheBloke on HuggingFace
Download this version:
mistral-7b-instruct-v0.1.Q4_0.gguf

Place it into the /models folder:

vlsi-rag-chatbot/
└── models/
    └── mistral-7b-instruct-v0.1.Q4_0.gguf

6. Embed Your Documents
Run:
python ingest.py

This will:

Read files from data/
Split them into text chunks
Embed them using sentence-transformers
Save them into ./chromadb/ vector DB

7. Start the Chatbot
Run:
python chatbot.py

You’ll see:
Running on local URL: http://127.0.0.1:7860
Open it in your browser and ask questions!


