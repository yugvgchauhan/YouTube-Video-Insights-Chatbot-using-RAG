"""
Configuration management for YouTube RAG Chatbot
"""
import os
from dotenv import load_dotenv

try:
    import streamlit as st
except ImportError:  # pragma: no cover - only used in Streamlit runtime
    st = None

# Load environment variables
load_dotenv()

# Prefer Streamlit secrets when available (e.g., Streamlit Cloud deploys)
if st and "HUGGINGFACE_API_TOKEN" in st.secrets:
    os.environ.setdefault("HUGGINGFACE_API_TOKEN", st.secrets["HUGGINGFACE_API_TOKEN"])

# HuggingFace Configuration
HUGGINGFACE_API_TOKEN = os.getenv("HUGGINGFACE_API_TOKEN", "")
HUGGINGFACE_LLM_MODEL = "meta-llama/Llama-3.1-8B-Instruct"
HUGGINGFACE_EMBEDDING_MODEL = "intfloat/e5-small-v2"

# OpenAI Configuration (optional)
if st and "OPENAI_API_KEY" in st.secrets:
    os.environ.setdefault("OPENAI_API_KEY", st.secrets["OPENAI_API_KEY"])
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")

# ChromaDB Configuration
CHROMA_PERSIST_DIRECTORY = "./chroma_db"
CHROMA_COLLECTION_NAME = "youtube_transcripts"

# Text Splitting Configuration
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200

# RAG Configuration
RETRIEVAL_K = 4  # Number of documents to retrieve
LLM_TEMPERATURE = 0.2
LLM_MAX_NEW_TOKENS = 512

# Streamlit Configuration
PAGE_TITLE = "YouTube Video Chatbot"
PAGE_ICON = "🎥"

