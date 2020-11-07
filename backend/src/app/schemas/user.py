import datetime

from typing import Optional

from pydantic import BaseModel, EmailStr, Field

# Shared properties
class UserBase(BaseModel):
    email: Optional[EmailStr] = None
    name : str = Field(..., min_length=1, max_length=50)
    surname : str = Field(..., min_length=1, max_length=100)
    
# Properties to receive via API on creation
class UserCreate(UserBase):
    email: EmailStr
    password: str 
    username: str = Field(..., min_length=3, max_length=50)

# Properties to receive via API on update
class UserUpdate(UserBase):
    password: Optional[str] = None

class UserInDBBase(UserBase):
    user_id: Optional[int] = None
    is_active: bool
    username: str = Field(..., min_length=3, max_length=50)
    created_date: datetime.datetime
    class Config:
        orm_mode = True

# Additional properties to return via API
class User(UserInDBBase):
    pass

# Additional properties stored in DB
class UserInDB(UserInDBBase):
    hashed_password: str

# check if email o is used
class UserDataExists(BaseModel):
    exists: bool