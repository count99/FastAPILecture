from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello1(name: str):
    return {"message": f"Hello {name}"}

@app.get("/item/")
async def get_item(name: str, price: float):
    return {"message": f"{name} is {price}"}
