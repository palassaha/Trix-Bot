

from fastapi import FASTAPI
from app.routes import chat, agent


from dotenv import load_dotenv
load_dotenv()


app = FASTAPI()

app.include_router(chat.router, prefix="/chat")
app.include_router(agent.router, prefix="/agent")

@app.get("/")
def read_root():
    return {"message": "Trix-Bot welcomes you!"}