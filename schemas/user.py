
from pydantic import BaseModel, EmailStr, Field, ConfigDict


# Input schema for user registration
class UserCreate(BaseModel):
    username: str = Field(min_length=3, max_length=100)
    email: EmailStr
    password: str = Field(min_length=8, max_length=128)


# Response schema
class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    role: str
    is_active: bool

    model_config = ConfigDict(from_attributes=True)


# Input schema for login
class UserLogin(BaseModel):
    email: EmailStr
    password: str


# Schema for JWT token response
class Token(BaseModel):
    access_token: str
    token_type: str
