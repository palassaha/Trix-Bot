
import ollama
from app.services.chat.rag import retrieve_event_info

# Load the chatbot model (Trix-Bot-Chat)
MODEL_NAME = "Trix-Bot-Chat"

def handle_chat_query(query: str):
    event_info = retrieve_event_info(query)
    
    system_prompt = (
    "You are Trix-Bot, the official AI assistant for TechTrix, our college tech fest. "
    "Your role is to provide accurate and concise details about TechTrix events based on user queries. "
    "If the required information is unavailable, respond with one of the following fallback messages:\n"
    "- 'I don't have enough information about that. Can you ask something specific about TechTrix?'\n"
    "- 'I'm focused on TechTrix. Would you like to know about the schedule, workshops, or competitions?'\n"
    "- 'Could you rephrase your question to relate to the event?'\n\n"
    "Context: {event_info}\n\n"
    "User Question: {query}\n\n"
    "Previous Conversation: {chat_history}\n\n"
    "Answer:"
)

    response = ollama.chat(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": system_prompt}]
    )
    
    return response["message"]["content"]

