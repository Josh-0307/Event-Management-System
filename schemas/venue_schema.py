
from pydantic import BaseModel, Field


class VenueCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=150)
    address: str = Field(..., min_length=3, max_length=255)
    city: str = Field(..., min_length=2, max_length=100)
    capacity: int = Field(..., gt=0)


class VenueResponse(BaseModel):
    id: int
    name: str
    address: str
    city: str
    capacity: int

    model_config = {"from_attributes": True}
class VenueUpdate(BaseModel):
    name: str = Field(..., min_length=2, max_length=150)
    address: str = Field(..., min_length=3, max_length=255)
    city: str = Field(..., min_length=2, max_length=100)
    capacity: int = Field(..., gt=0)