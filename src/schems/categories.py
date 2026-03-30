from pydantic import BaseModel, Field
from datetime import datetime as dati
from typing import Annotated, Optional


class CategoryUpdateAndCreate(BaseModel):
    slug: Annotated[Optional[str], Field(default=None, max_length=100)]
    title: Annotated[Optional[str], Field(default=None, min_length=1, max_length=200)]
    description: Annotated[Optional[str], Field(default=None, max_length=500)]
    is_published: Annotated[Optional[bool], Field(default=None)]


class CategoryOut(CategoryUpdateAndCreate):
    id: Annotated[int, Field(ge=1)]
    created_at: dati

    class Config:
        from_attributes = True