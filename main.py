"""FastAPI application with Middleware"""
from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, EmailStr
import time

class User(BaseModel):
    """Model for User"""
    first_name: str
    last_name: str
    age: int
    email: EmailStr
    height: float

#Users in memory database
users = []

app = FastAPI()

#CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#Logger Middleware
@app.middleware("http")
async def log_requests_time(request: Request, call_next):
    """Middleware to log requests time"""
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    print(f"Request: {request.method} {request.url} completed in {process_time:.1f} seconds")
    return response


@app.post("/users", status_code=201)
def create_user(user: User):
    """Signup a new user"""
    for i, j in enumerate(users):
        if user == users[i]:
            raise HTTPException(status_code=400, detail="User already exists")
    users.append(user)
    return {"User Added Successfully!\n": user}  

@app.get("/users")
def get_users():
    """Get all users"""
    return users