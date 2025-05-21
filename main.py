from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from llm import LLM

llm = LLM()
app = FastAPI()

# Allow frontend to call this from browser
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # for dev only; restrict in prod
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/greet")
def greet():
    response = llm.ask("is the api call working?")

    return {
        "message": response
        }

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)