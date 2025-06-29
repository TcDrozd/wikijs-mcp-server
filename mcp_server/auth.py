from .config import Config

def check_wikijs_api_key():
    if not Config.WIKIJS_API_KEY:
        raise Exception("Wiki.js API key is not set. Please check your .env file.")
