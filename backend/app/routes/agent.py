
from fastapi import APIRouter, HTTPException
from app.services.agent_service import AgentService

router = APIRouter()
agent_service = AgentService()

@router.post("/register")
async def register_for_event(team_data: dict):
    try:
        response = agent_service.register_for_event(team_data)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))