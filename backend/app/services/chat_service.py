
import ollama


class ChatService:
    def __init__(self, model_name: str = "Trix-Bot-Chat"):
        self.model_name = model_name
        
    def get_response(self, prompt: str) -> str:
        response = ollama.generate(self.model_name, prompt=prompt)
        return response["response"]