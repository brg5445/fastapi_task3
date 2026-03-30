from pydantic import BaseModel, Field
from datetime import datetime as dati
from typing import Annotated, Optional


class LocationUpdateAndCreate(BaseModel):
    name: Annotated[Optional[str], Field(default=None, min_length=1, max_length=256)]
    is_published: Annotated[Optional[bool], Field(default=None)]


class LocationOut(LocationUpdateAndCreate):
    id: Annotated[int, Field(ge=1)]
    created_at: dati

    class Config:
        from_attributes = True