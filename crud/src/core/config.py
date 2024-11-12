import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Edulibre Project"
    PROJECT_VERSION: str = "0.0.1"
    DATABASE_URL: str
    SECRET_KEY: str = os.getenv("SECRET_KEY", "fallback_secret_key")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30 

    class Config:
        env_file = ".env" 

settings = Settings()
