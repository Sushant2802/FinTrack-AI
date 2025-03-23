import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('COHERE_API_KEY')
if not api_key:
    print("❗ COHERE_API_KEY not found. Please check your .env file.")
else:
    print("✅ API Key loaded successfully")
