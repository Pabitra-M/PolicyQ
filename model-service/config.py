import os
from dotenv import load_dotenv

load_dotenv()

WEAVIATE_URL = os.getenv("WEAVIATE_URL")
WEAVIATE_API_KEY = os.getenv("WEAVIATE_API_KEY")

print("DEBUG:", WEAVIATE_URL, WEAVIATE_API_KEY)  # 🔍 temporary check
