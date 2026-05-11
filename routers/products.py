from fastapi import APIRouter
from pydantic import BaseModel
from database import db_connection

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)

# class Product(BaseModel):
#     product_id:str
#     product_name:str

@router.get("/")
def get_all_products():
    conn = db_connection()
    curr = conn.cursor()
    curr.execute("SELECT * FROM products")
    res = curr.fetchall()
    curr.close()
    conn.close()
    return res

@router.get("/{product_id}")
def get_product(product_id:str):
    conn = db_connection()
    curr = conn.cursor()
    curr.execute(f"SELECT * FROM products where product_id='{product_id}'")
    res = curr.fetchall()
    curr.close()
    conn.close()
    return res

# @router.post("/")
# def create_product(product:Product):
#     return product