from fastapi import FastAPI, APIRouter
from pydantic import BaseModel
import psycopg2
from psycopg2.extras import RealDictCursor
import json
from database import db_connection


class User(BaseModel):
    user_name:str
    email:str

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

@router.post("/")
def create_user(user:User):
    conn = db_connection()
    curr = conn.cursor()
    curr.execute(f"Insert into users (user_name, email) values ('{user.user_name}', '{user.email}') RETURNING *")
    new_user = curr.fetchone()
    curr.close()
    conn.commit()
    conn.close()
    return new_user

@router.put("/{user_id}")
def update_user(user_id:int, user:User):
    conn = db_connection()
    curr = conn.cursor()
    curr.execute(f"Update users set user_name='{user.user_name}', email='{user.email}' where user_id={user_id} RETURNING *")
    updated_user = curr.fetchone()
    curr.close()
    conn.commit()
    conn.close()
    return updated_user

@router.delete("/{user_id}")
def delete_user(user_id):
    conn = db_connection()
    curr = conn.cursor()
    curr.execute(f"Delete from users where user_id={user_id} RETURNING *")
    deleted_user = curr.fetchone()
    curr.close()
    conn.commit()
    conn.close()
    return deleted_user