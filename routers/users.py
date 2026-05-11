from fastapi import FastAPI, APIRouter
from pydantic import BaseModel
import psycopg2
from psycopg2.extras import RealDictCursor
import json
from database import db_connection


# class User(BaseModel):
#     user_id:int
#     user_name:str

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.get("/")
def get_all_users():
    conn = db_connection()
    curr = conn.cursor()
    curr.execute("SELECT * FROM users")
    res = curr.fetchall()
    curr.close()
    conn.close()
    return res

@router.get("/{user_id}")
def get_user(user_id: int):
    conn = db_connection()
    curr = conn.cursor()
    curr.execute(f"SELECT * FROM users where user_id={user_id}")
    res = curr.fetchall()
    curr.close()
    conn.close()
    return res

# @router.post("/")
# def create_user(user:User):
#     return user