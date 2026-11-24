from pydantic import BaseModel, Field
from datetime import datetime


class RegistrationCreate(BaseModel):
    event_id: int = Field(..., gt=0)
    attendee_id: int = Field(..., gt=0)
    status: str = "registered"


class RegistrationResponse(BaseModel):
    id: int
    event_id: int
    attendee_id: int
    registration_date: datetime
    status: str

    model_config = {"from_attributes": True}


class RegistrationUpdate(BaseModel):
    event_id: int = Field(..., gt=0)
    attendee_id: int = Field(..., gt=0)
    status: str = Field(..., min_length=1, max_length=20)