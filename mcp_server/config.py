import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    WIKIJS_URL = os.getenv("WIKIJS_URL")
    WIKIJS_API_KEY = os.getenv("WIKIJS_API_KEY")
    OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434")
    OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3")
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
