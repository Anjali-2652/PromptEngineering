from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=OPENAI_API_KEY)
response = client.chat.completions.create(
    model = "gpt-4o-mini",
    messages = [
        {
            "role": "system", 
            "content": "You are a helpful assistant that summarizes about tourist places."
        },
        {
            "role": "user", 
            "content": "Summarize the tourist places of janakpur and also where is janakpur ."
        }
    ]
)

print("OpenAI Output:\n", response.choices[0].message.content)