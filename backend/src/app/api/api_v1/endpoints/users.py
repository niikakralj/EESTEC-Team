from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, Body
from fastapi.encoders import jsonable_encoder
from pydantic.networks import EmailStr

from app import schemas, models
from app.api import deps
from app.crud import crud_user


router = APIRouter()


@router.post("/", response_model=schemas.user.User, status_code=201)
def create_user(*, user_in: schemas.user.UserCreate, db: Session = Depends(deps.get_db)):
    """
    Create new user.
    """
    user_by_email = crud_user.get_user_by_email(db, email=user_in.email)
    if user_by_email:
        raise HTTPException(status_code=400, detail="The user with this email already exists in the system.")
    user_by_username = crud_user.get_user_by_username(db, username=user_in.username)
    if user_by_username:
        raise HTTPException(status_code=400, detail="The user with this username already exists in the system.")
    user = crud_user.create_user(db, user=user_in)
    return user


@router.get("/me/", response_model=schemas.user.User)
def read_users_me(current_user: schemas.user.User = Depends(deps.get_current_active_user)):
    """
    Get current user.
    """
    return current_user


@router.get("/emailexist", response_model=schemas.user.UserDataExists)
def check_if_email_exists(email: str, db: Session = Depends(deps.get_db)):
    user_by_email = crud_user.get_user_by_email(db, email=email)
    if user_by_email:
        return {"exists": True}
    else:
        return {"exists": False}


@router.get("/usernameexist", response_model=schemas.user.UserDataExists)
def check_if_username_exists(username: str, db: Session = Depends(deps.get_db)):
    user_by_username = crud_user.get_user_by_username(db, username=username)
    if user_by_username:
        return {"exists": True}
    else:
        return {"exists": False}