from pydantic import BaseModel, Field, EmailStr
from datetime import datetime as dati
from typing import Annotated, Optional


class UserUpdate(BaseModel):
    first_name: Annotated[str, Field(min_length=1, max_length=50)]
    last_name: Annotated[str, Field(min_length=1, max_length=50)]
    bio_info: Annotated[str, Field(max_length=500)]
    email: Annotated[EmailStr, Field(max_length=100)]


class UserCreate(UserUpdate):
    nickname: Annotated[str, Field(min_length=3, max_length=50, pattern=r"^[a-zA-Z0-9_]+$")]
    password: Annotated[str, Field(min_length=6)]


class UserOut(UserUpdate):
    id: Annotated[int, Field(ge=1)]
    nickname: Annotated[str, Field(min_length=3, max_length=50)]
    active: bool
    date_joined: dati

    class Config:
        from_attributes = True