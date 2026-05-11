import psycopg2
import json
from psycopg2.extras import RealDictCursor
import os
from dotenv import load_dotenv

load_dotenv()

def db_connection():
    conn = psycopg2.connect(
        host = os.getenv("DB_HOST"),
        database = os.getenv("DB_DATABASE"),
        user = os.getenv("DB_USER"),
        password = os.getenv("DB_PASS"),
        port = os.getenv("DB_PORT"),
        cursor_factory = RealDictCursor
    )
    print("Connected to DB successfully")
    return conn