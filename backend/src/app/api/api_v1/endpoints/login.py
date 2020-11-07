from datetime import timedelta

from fastapi import APIRouter, Body, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.config import settings
from app import schemas, security, models
from app.crud import crud_user
from app.api import deps
from app.schemas.token import TokenLoginResponse

router = APIRouter()


@router.post("/login/access-token", response_model=TokenLoginResponse)
def login_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(deps.get_db)):
    """
    OAuth2 compatible token login, get an access token for future requests
    """
    user = crud_user.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    elif not crud_user.is_active(user):
        raise HTTPException(status_code=400, detail="Inactive user")
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = security.create_access_token(data={"sub": user.username}, expires_delta=access_token_expires)
    return {"access_token": access_token, "token_type": "bearer", "expiresIn": settings.ACCESS_TOKEN_EXPIRE_MINUTES}


@router.post("/login/test-token", response_model=schemas.user.User)
def test_token(current_user: models.User = Depends(deps.get_current_user)):
    """
    Test access token
    """
    return current_user