import re
from typing import Dict, Any, List
from app.db.supabase import sb

def extract_intent(state):

    prompt = state.prompt
    register_keywords = ["register me for", "sign me up for", "i want to register for", "participate in"]

    for keyword in register_keywords:
        if keyword in prompt:
            state.intent = "register_for_event"
            break

    if state.intent == "register_for_event":
        match = re.search(r"for\s(.+)", prompt)
        if match:
            event_name = match.group(1).strip()
            response = sb.get_client().table("events").select("id, is_team, registration_fees").eq("name", event_name).execute()
            if response.data:
                event_data = response.data[0]
                state.event_id = event_data["id"]
                state.is_team_event = event_data["is_team"]
                state.team_members = extract_team_members(prompt, state.user)
            else:
                state.response = f"Couldn't find an event named '{event_name}'. Please check the event name."
    
    if not state.intent:
        state.intent = "unknown"
        state.response = "Sorry, I couldn't understand your request. Please try again with a valid event name."
    
    return state

def extract_team_members(prompt, user):

    members = []
    match = re.search(r"with (.+)", prompt)
    
    if match:
        raw_members = match.group(1).split(",")
        for member in raw_members:
            parts = member.strip().split()
            if len(parts) >= 2:
                email = parts[-1] if "@" in parts[-1] else ""
                name = " ".join(parts[:-1]) if email else " ".join(parts)
                members.append({"name": name, "email": email})
    
    members.insert(0, {"name": user["name"], "email": user["email"]})
    return members

def register_for_event(state):

    if not state.event_id:
        state.response = "I couldn't find the event you're trying to register for. Please check the event name."
        return state

    user_email = state.user.get("email")
    if not user_email:
        state.response = "I need your email to complete the registration. Please provide it."
        return state

    # Check if the user exists in the SWC table
    swc_response = sb.get_client().table("SWC").select("id").eq("email", user_email).execute()
    user_in_swc = bool(swc_response.data)

    if state.is_team_event:
        response = sb.get_client().table("teams").insert({
            "event_id": state.event_id,
            "team_lead_email": user_email,
            "is_team": True,
            "team_members": state.team_members
        }).execute()
    else:
        response = sb.get_client().table("participants").insert({
            "event_id": state.event_id,
            "email": user_email
        }).execute()
    
    if response.data:
        if not user_in_swc:
            payment_url = f"https://payment.techtix.com/pay?event={state.event_id}"
            state.response = f"Successfully registered! Here is the payment link: {payment_url}"
        else:
            state.response = "Successfully registered! Since you are an SWC member, no payment is required."
    else:
        state.response = "There was an issue with registration. Please try again later."
    
    return state

# Define allowed functions the AI agent can call
allowed_functions = {
    "extract_intent": extract_intent,
    "extract_team_members": extract_team_members,
    "register_for_event": register_for_event
}
