"""User Model"""
from pydantic import BaseModel, EmailStr

class User(BaseModel):
    """Model for User"""
    first_name: str
    last_name: str
    age: int
    email: EmailStr
    height: float
