from sqlalchemy.orm import Session

from app import crud, schemas
from app.db import base  # noqa: F401
from app.db.session import engine


def init_db(db: Session) -> None:
    base.Base.metadata.create_all(bind=engine)