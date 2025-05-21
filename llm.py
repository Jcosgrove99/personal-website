# LLMs to use: Gemini, Groq

from google import genai
import os

client = genai.Client(api_key=os.getenv('gemini_api_key'))

response = client.models.generate_content(
    model="gemini-2.0-flash", contents="Explain how AI works in a few words"
)
print(response.text)