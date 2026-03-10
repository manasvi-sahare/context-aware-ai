from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from backend.response_strategy import generate_response_llm
from backend.memory_manager import init_db, get_history_by_date

app = FastAPI()
init_db()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    message = data["message"]

    reply = generate_response_llm(message)
    return {"reply": reply}

@app.get("/history-by-date")
async def history_by_date():
    return get_history_by_date()
