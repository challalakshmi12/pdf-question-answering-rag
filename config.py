import os
import google.generativeai as genai

from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer

# ===========================================
# Load Environment Variables
# ===========================================

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# ===========================================
# Configure Gemini
# ===========================================

genai.configure(api_key=GEMINI_API_KEY)

gemini_model = genai.GenerativeModel("gemini-2.5-flash")

# ===========================================
# Load Embedding Model
# ===========================================

print("\nLoading Embedding Model...")

embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

print("Embedding Model Loaded Successfully!")