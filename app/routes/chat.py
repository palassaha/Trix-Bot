
from fastapi import APIRouter, Depends
from app.services.chat.llm_handler import handle_chat_query

router = APIRouter()

@router.post("/query")
async def query(query: str):
    return {"response": handle_chat_query(query)}