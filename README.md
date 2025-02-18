
## TRIX-BOT


### Project Structure

```

trix-bot/
├── app/
│   ├── core/
│   │   ├── config.py
│   │   └── security.py
│   ├── db/
│   │   ├── supabase.py
│   │   └── models.py
│   ├── routes/
│   │   ├── chat.py
│   │   ├── agent.py
│   │   └── health.py
│   ├── services/
│   │   ├── chat/
│   │   │   ├── modelfiles/
│   │   │   ├── llm_handler.py
│   │   │   └── rag.py
│   │   └── agent/
│   │       ├── modelfiles/
│   │       ├── function_map.py
│   │       └── agent_handler.py
│   ├── main.py
│   └── utils.py
├── tests/
│   ├── test_chat.py
│   └── test_agent.py
├── frontend/
│   └── index.html
├── docker/
│   └── nginx/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .github/
│   └── workflows/
│       ├── ci.yml
│       └── cd.yml
├── .dockerignore
├── .gitignore
└── README.md

```