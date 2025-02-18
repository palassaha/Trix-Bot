
from fastapi import APIRouter, Depends
from app.services.agent.agent_handler import execute_agent_action

router = APIRouter()

@router.post("/agent")
async def agent_endpoint(prompt: str, user:dict):
    return {'result': await execute_agent_action(prompt, user)}