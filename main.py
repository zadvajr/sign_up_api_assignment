from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


class User(BaseModel):
    """Model for User"""
    first_name: str
    last_name: str
    age: int
    email: str
    height: float

users = []

app = FastAPI()

@app.get("/")
def home():
    return {"HOME": "Welcome to Sign Up API Home Page"}

@app.post("/signup")
def signup(user: User):
    """Signup a new user"""
    users.append(user)
    return {"User Added Successfully!\n": user}  

@app.get("/users")
def get_users():
    """Get all users"""
    return users