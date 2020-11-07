from sqlalchemy.orm import Session
from app.security import get_password_hash, verify_password

from app import models
from app.schemas import user
from app.models import User

def get_user_by_email(db_session: Session, email: str):
    return db_session.query(models.User).filter(models.User.email == email).first()

def get_user_by_username(db_session: Session, username: str):
    return db_session.query(models.User).filter(models.User.username == username).first()

def create_user(db_session: Session, user: user.UserCreate):
    password_hash = get_password_hash(user.password)
    db_user = models.User(email=user.email, 
                            password_hash=password_hash,
                            name=user.name,
                            surname=user.surname,
                            username=user.username
                            )
    db_session.add(db_user)
    db_session.commit()
    db_session.refresh(db_user)
    return db_user

def is_active(user: user.User) -> bool:
    return user.is_active

def authenticate_user(db_session: Session, username: str, password: str):
    user = get_user_by_username(db_session, username)
    if not user:
        return False
    if not verify_password(password, user.password_hash):
        return False
    return user