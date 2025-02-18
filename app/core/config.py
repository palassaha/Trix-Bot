
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    SUPABASE_URL: str
    SUPABASE_KEY: str 
    OLLAMA_HOST: str = 'http://localhost:11434'
    
    
    class Config:
        env_file = ".env"
        
        
settings = Settings()