import os
from dotenv import load_dotenv
import google.generativeai as genai
load_dotenv()

prompt = """
Classify the sentiment.

Text: I love this phone.
Sentiment: Positive

Text: This app is terrible.
Sentiment: Negative

Text: The movie was okay.
Sentiment:
"""
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")


genai.configure(api_key = GOOGLE_API_KEY)
gemini_model = genai.GenerativeModel("gemini-2.5-flash")
gemini_response = gemini_model.generate_content(prompt)
print(gemini_response.text)
