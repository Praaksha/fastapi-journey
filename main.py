from fastapi import FastAPI
from pydantic import BaseModel
from routers import users, products

app = FastAPI()

app.include_router(users.router)
app.include_router(products.router)
# class User(BaseModel):
#     name:str
#     age:int

@app.get("/")
def home():
    return {"message":"Home Page"}

@app.get("/about")
def about():
    return {"message": "About Page"}

# @app.get("/user/{name}")
# def user(name):
#     return {"user": name}

# @app.get("/products")
# def products(limit:int):
#     return {"limit": limit}

# @app.post("/create-user")
# def create_user(user:User):
#     return{
#         "name":user.name,
#         "age":user.age
#     }