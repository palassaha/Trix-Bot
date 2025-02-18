
from fastapi import FastAPI
from app.routes import chat, agent, health

app = FastAPI(title="TRIX-BOT")

app.include_router(health.router)
app.include_router(chat.router, prefix="/chat")
app.include_router(agent.router, prefix="/agent")


