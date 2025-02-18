

from fastapi import APIRouter, HTTPException
from app.services.chat_service import ChatService

router = APIRouter()
chat_service = ChatService()

@router.post("/query")
async def chat_query(prompt: str):
    try:
        response = chat_service.get_response(prompt)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))