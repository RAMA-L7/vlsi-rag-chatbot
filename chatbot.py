from llama_cpp import Llama
import chromadb
from sentence_transformers import SentenceTransformer
import gradio as gr

# Load embedding model
print("🔠 Loading embedding model...")
embedder = SentenceTransformer("all-MiniLM-L6-v2")

# ✅ FIXED: Load Chroma with new syntax
print("📦 Loading Chroma DB...")
chroma_client = chromadb.PersistentClient(path="./chromadb")
collection = chroma_client.get_or_create_collection("vlsi_docs")

# Load local model
print("🤖 Loading LLaMA model...")
llm = Llama(
    model_path="./models/mistral-7b.Q4_0.gguf",
    n_ctx=2048,
    n_threads=6
)

# RAG query handler
def ask_rag(query):
    query_vec = embedder.encode(query).tolist()
    results = collection.query(query_embeddings=[query_vec], n_results=3)
    context = "\n\n".join(results["documents"][0])

    prompt = f"""
[Context:]
{context}

[Question:]
{query}

[Answer:]
"""
    output = llm(prompt, max_tokens=300, stop=["[End]"])
    return output["choices"][0]["text"].strip()

print("🧪 Pre-warming model with dummy prompt...")
llm("The following is a test prompt to warm up the model. [End]")

iface = gr.Interface(fn=ask_rag, inputs="text", outputs="text", title="🧠 VLSI Chatbot", description="Ask me about VLSI Physical Design.")
iface.launch()
