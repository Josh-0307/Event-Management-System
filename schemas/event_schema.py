from pydantic import BaseModel, Field
from datetime import datetime


class EventCreate(BaseModel):
    venue_id: int = Field(..., gt=0)
    name: str = Field(..., min_length=2, max_length=150)
    description: str | None = None
    event_date: datetime
    capacity: int = Field(..., gt=0)


class EventResponse(BaseModel):
    id: int
    venue_id: int
    name: str
    description: str | None
    event_date: datetime
    capacity: int

    model_config = {"from_attributes": True}

class EventUpdate(BaseModel):
    venue_id: int = Field(..., gt=0)
    name: str = Field(..., min_length=2, max_length=150)
    description: str | None = None
    event_date: datetime
    capacity: int = Field(..., gt=0)