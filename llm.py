# LLMs to use: Gemini, Groq
from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv('GEMINI_API_KEY')
client = genai.Client(api_key=api_key)

# LLM class
class LLM:
    def __init__(self):
        self.client = genai.Client(api_key=api_key)

    def ask(self, prompt):
        response = self.client.models.generate_content(
            model="gemini-2.0-flash", contents=prompt
        )
        return response.text

