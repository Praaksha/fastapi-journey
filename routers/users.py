from fastapi import FastAPI, APIRouter
from pydantic import BaseModel

class User(BaseModel):
    user_id:int
    user_name:str

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.get("/")
def get_all_users():
    return {"message": "Get all users"}

@router.get("/{user_id}")
def get_user(user_id: int):
    return {"message": f"Get user with User ID: {user_id}"}

@router.post("/")
def create_user(user:User):
    return user