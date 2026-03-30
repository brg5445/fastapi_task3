from pydantic import BaseModel, Field
from datetime import datetime as dati
from typing import List, Annotated, Optional

from .users import UserOut
from .categories import CategoryOut
from .locations import LocationOut
from .comments import CommentOut


class PostUpdate(BaseModel):
    title: Annotated[Optional[str], Field(default=None, min_length=1, max_length=200)]
    text: Annotated[Optional[str], Field(default=None, min_length=1)]
    pub_date: Annotated[Optional[dati], Field(default=None)]
    is_published: Annotated[Optional[bool], Field(default=None)]
    image: Annotated[Optional[str], Field(default=None, max_length=500)]
    location_id: Annotated[Optional[int], Field(default=None, ge=1)]
    category_id: Annotated[Optional[int], Field(default=None, ge=1)]


class PostCreate(PostUpdate):
    author_id: Annotated[Optional[int], Field(default=None, ge=1)]


class PostOut(PostCreate):
    id: Annotated[int, Field(ge=1)]
    created_at: dati

    class Config:
        from_attributes = True


class PostDetail(PostOut):
    author: UserOut
    category: Annotated[Optional[CategoryOut], Field(default=None)]
    location: Annotated[Optional[LocationOut], Field(default=None)]
    comments: Annotated[List["CommentOut"], Field(default_factory=list)]

    class Config:
        from_attributes = True