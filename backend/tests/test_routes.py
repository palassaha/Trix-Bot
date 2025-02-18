
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_chat_query():
    response = client.get("/chat/query", json={"prompt": "Tell me about Tech Quiz"})
    assert response.status_code == 200
    assert "response" in response.json()
    
