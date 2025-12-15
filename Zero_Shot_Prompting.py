import os
from dotenv import load_dotenv
import google.generativeai as genai
load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key = GOOGLE_API_KEY)
gemini_model = genai.GenerativeModel("gemini-2.5-flash")
gemini_response = gemini_model.generate_content("Summarize the article in one sentence about quantum computing in simple terms.")

print("Gemini Output:\n", gemini_response.text)
