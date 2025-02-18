
import re
from typing import Dict, Any, List
from langgraph.graph import StateGraph, END
from app.db.supabase import sb
from agent.function_map import extract_intent, extract_team_members, register_for_event

class AgentState:

    def __init__(self, prompt: str, user: Dict[str, Any]):
        self.prompt = prompt.lower()  # Normalize prompt for easier processing
        self.user = user
        self.intent = None
        self.event_id = None
        self.is_team_event = False
        self.team_members = extract_team_members(self.prompt, self.user)
        self.response = None

graph = StateGraph(AgentState)

graph.add_node("extract_intent", extract_intent)
graph.add_node("register_for_event", register_for_event)

graph.set_entry_point("extract_intent")
graph.add_edge("extract_intent", "register_for_event", condition=lambda state: state.intent == "register_for_event")
graph.add_edge("extract_intent", END, condition=lambda state: state.intent == "unknown")
graph.add_edge("register_for_event", END)

agent_executor = graph.compile()

async def execute_agent_action(prompt: str, user: Dict[str, Any]) -> Dict[str, Any]:

    initial_state = AgentState(prompt, user)
    final_state = await agent_executor.ainvoke(initial_state)
    return {"response": final_state.response}
