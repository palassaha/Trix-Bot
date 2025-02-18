

from app.database import supabase

class AgentService:
    def register_for_event(self, team_data: dict) -> dict:
        try:
            response = supabase.table("teams").insert(team_data).execute()
            return {"message": "Registration successful!", "data": response.data}
        except Exception as e:
            raise Exception(f"Registration failed: {str(e)}")