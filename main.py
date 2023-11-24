from fastapi import FastAPI
from pydantic import BaseModel

from enum import Enum


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


class ModelNames(str, Enum):
    ALEXNET = "alexnet"
    RESNET = "resnet"
    LENET = "lenet"


app = FastAPI()


@app.post("items/")
async def create_item(item: Item):
    return item


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}


@app.get("/models/{model_name}")
async def get_model(model_name:  ModelNames):
    if model_name is ModelNames.ALEXNET:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have som e residuals"}



fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/users/{user_id}/items/{item_id}")
async def read_item(user_id: int, item_id: str, q: str | None = None, short: bool = False):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update({
            "description": "This is an amazing item that has a long description"
        })
    return item


@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}



@app.get("/items/{item_id}")
async def read_user_item(item_id: str, needy: str):
    item = {"item_id": item_id, "needy": needy}
    return item

