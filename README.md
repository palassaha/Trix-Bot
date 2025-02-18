
## Trix-Bot


### Project Structure

```
trix-bot/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py (FastAPI server)
│   │   ├── database.py (Supabase connection)
│   │   ├── models/ (Pydantic models for database tables)
│   │   ├── routes/ (API routes)
│   │   │   ├── chat.py (Chatbot routes)
│   │   │   └── agent.py (AI agent routes)
│   │   ├── services/ (Business logic)
│   │   │   ├── chat_service.py (Chatbot logic)
│   │   │   └── agent_service.py (AI agent logic)
│   │   ├── utils/ (Helper functions)
│   │   └── tests/ (Unit tests)
├── frontend/ (Optional for testing)
├── modelfiles/ (Ollama modelfiles)
├── data/ (PDFs for fine-tuning)
├── Dockerfile
├── requirements.txt
├── .github/workflows/ (CI/CD pipeline)
└── README.md

```