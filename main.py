from typing import Union
from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.post("/items/")
def create_item(name: str, price: float):
    return {"name": name, "price": price}


@app.put("/items/{item_id}")
def update_item(item_id: int, name: str, price: float):
    return {"item_id": item_id, "name": name, "price": price}   

@app.delete("/items/{item_id}")
def delete_item(item_id: int):  
    return {"item_id": item_id, "status": "deleted"}

@app.get("/users/{user_id}/items/{item_id}")
def read_user_item(user_id: int, item_id: int, q: Union[str, None] = None):
    return {"user_id": user_id, "item_id": item_id, "q": q} 


@app.get("/status/")
def get_status():
    return {"status": "ok"} 


@app.get("/health/")
def get_health():
    return {"health": "good"}


class User(BaseModel):
    id: int
    name: str
    email: str
    
@app.post("/users/")
def create_user(user: User):
    return user

@app.get("/users/{user_id}")
def read_user(user_id: int):
    return {"user_id": user_id, "name": "John Doe", "email": "rtrr@23gmail.com"}

@app.put("/users/{user_id}")
def update_user(user_id: int, user: User):
    return {"user_id": user_id, "name": user.name, "email": user.email}


@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    return {"user_id": user_id, "status": "deleted"}