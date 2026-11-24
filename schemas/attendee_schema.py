from pydantic import BaseModel, Field, EmailStr


class AttendeeCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=150)
    email: EmailStr
    phone: str | None = None


class AttendeeResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    phone: str | None

    model_config = {"from_attributes": True}

class AttendeeUpdate(BaseModel):
    name: str = Field(..., min_length=2, max_length=150)
    email: EmailStr
    phone: str | None = None