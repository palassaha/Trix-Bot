
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.db.supabase import sb
from app.core.config import settings

import httpx

router = APIRouter()

@router.get("/health")
async def health():
    try:
        db_response = sb.get_client().table("users").select("count", count='exact').execute()
        
        async with httpx.AsyncClient() as client:
            ollama_resp = await client.get(f"{settings.OLLAMA_HOST}/")
            
        
        return JSONResponse(
            status_code=200,
            content={
                "status": "healty",
                "database": "connected",
                "version": "0.0.1",
                "sevices": {
                    "database": True,
                    "ollama": True
                }           
            }
        )
        
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={
                "status": "healty",
                "database": "disconnected",
                "version": "0.0.1",
                "sevices": {
                    "database": False,
                    "ollama": False
                }           
            }
        )
        
        
