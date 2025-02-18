
from app.db.supabase import sb

allowed_functions = {
    "register_for_event": lambda user, event_id: sb.get_client().table("teams").insert({
        "event_id": event_id,
        "team_lead_email": user["email"]
    }).execute()
}