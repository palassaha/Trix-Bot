
from langchain.document_loaders import PyPDFLoader
from langchain.embeddings import OllamaEmbeddings
from langchain.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os

# Path to event PDF files
DATA_DIR = "data\TechFest2025-EventDetails.pdf"
PDF_FILE = os.path.join(DATA_DIR, "events.pdf")

def retrieve_event_info(query: str):
    # Load event PDF
    loader = PyPDFLoader(PDF_FILE)
    documents = loader.load()

    # Split text into manageable chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=512, chunk_overlap=512)
    docs = text_splitter.split_documents(documents)

    # Create a vector database for semantic search
    embeddings = OllamaEmbeddings(model="Trix-Bot-Chat")
    vector_db = FAISS.from_documents(docs, embeddings)

    # Perform similarity search
    results = vector_db.similarity_search(query, k=2)
    
    # Return relevant content or a default response
    return " ".join([doc.page_content for doc in results]) if results else "No relevant event details found."
