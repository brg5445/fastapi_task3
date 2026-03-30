from pydantic import BaseModel, Field
from datetime import datetime as dati
from typing import Annotated, Optional


class CommentUpdate(BaseModel):
    text: Annotated[Optional[str], Field(default=None, min_length=1, max_length=1000)]


class CommentCreate(CommentUpdate):
    post_id: Annotated[int, Field(ge=1)]
    author_id: Annotated[int, Field(ge=1)]


class CommentOut(CommentCreate):
    id: Annotated[int, Field(ge=1)]
    created_at: dati

    class Config:
        from_attributes = True