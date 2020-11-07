from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.db.init_db import init_db
from app.db.session import SessionLocal

from app.api.api_v1.api import api_router
from app.config import settings

def init() -> None:
    db = SessionLocal()
    init_db(db)

init()

app = FastAPI(
    title=settings.PROJECT_NAME,
    description="This is the API for the Smartbin App",
    version="0.1.0"
)

origins = settings.BACKEND_CORS_ORIGINS

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix=settings.API_V1_STR)