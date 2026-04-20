from fastapi import FastAPI, Depends
from pydantic import BaseModel
import asyncio
import functools

app = FastAPI()


# -------------------------
# Custom Decorator
# -------------------------
def log_request(func):
    @functools.wraps(func)
    async def wrapper(*args, **kwargs):
        print("Request received")
        result = await func(*args, **kwargs)
        print("Request completed")
        return result
    return wrapper


# -------------------------
# Request Model
# -------------------------
class User(BaseModel):
    name: str
    age: int


# -------------------------
# Response Model
# -------------------------
class UserResponse(BaseModel):
    name: str


# -------------------------
# Dependency Function
# -------------------------
async def auth_dependency():
    await asyncio.sleep(0.1)
    return {"auth": "verified"}


# -------------------------
# Simulated DB Call
# -------------------------
async def fake_db_call():
    await asyncio.sleep(1)
    return {"name": "John", "age": 28}


# -------------------------
# Routes with Custom Decorator
# -------------------------
@app.get("/users/{user_id}")
@log_request
async def get_user(user_id: int):
    return {"user_id": user_id}


@app.get("/profile", response_model=UserResponse)
@log_request
async def profile():
    data = await fake_db_call()
    return data


@app.post("/users")
@log_request
async def create_user(user: User):
    return user


@app.get("/secure")
@log_request
async def secure_route(dep=Depends(auth_dependency)):
    return dep