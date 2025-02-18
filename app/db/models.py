
from pydantic import BaseModel
from typing import Optional

class TeamCreate(BaseModel):
    team_name: str
    event_id: str
    team_lead_email: str
    