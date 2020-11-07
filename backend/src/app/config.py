import secrets
from typing import List

from pydantic import BaseSettings, AnyHttpUrl

class Settings(BaseSettings):
    PROJECT_NAME: str = "Smartbin API"
    API_V1_STR: str = "/smartbin/api/v1"
    SECRET_KEY: str = secrets.token_urlsafe(32)
    # 60 minutes * 24 hours * 8 days = 8 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    BACKEND_CORS_ORIGINS = ["*"]
    
    class Config:
        case_sensitive = True

settings = Settings()   