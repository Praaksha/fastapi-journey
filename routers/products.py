from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)

class Product(BaseModel):
    product_id:str
    product_name:str

@router.get("/")
def get_all_products():
    return {"message": "Get All products"}

@router.get("/{product_id}")
def get_product(product_id:str):
    return {"message": f"Get product with product_id: {product_id}"}

@router.post("/")
def create_product(product:Product):
    return product