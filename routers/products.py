from fastapi import APIRouter
from pydantic import BaseModel
from database import db_connection

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)

class Product(BaseModel):
    product_id:str
    product_name:str

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

@router.post("/")
def create_product(product:Product):
    conn = db_connection()
    curr = conn.cursor()
    curr.execute(f"Insert into products (product_id, product_name) values ('{product.product_id}', '{product.product_name}') RETURNING *")
    new_product = curr.fetchone()
    curr.close()
    conn.commit()
    conn.close()
    return new_product

@router.put("/{product_id}")
def update_product(product_id:str, product:Product):
    conn = db_connection()
    curr = conn.cursor()
    curr.execute(f"Update products set product_id='{product.product_id}', product_name='{product.product_name}' where product_id='{product_id}' RETURNING *")
    updated_user = curr.fetchone()
    curr.close()
    conn.commit()
    conn.close()
    return updated_user

@router.delete("/{product_id}")
def delete_user(product_id):
    conn = db_connection()
    curr = conn.cursor()
    curr.execute(f"Delete from products where product_id='{product_id}' RETURNING *")
    deleted_product = curr.fetchone()
    curr.close()
    conn.commit()
    conn.close()
    return deleted_product