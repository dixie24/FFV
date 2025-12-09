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


class Item(BaseModel):
    id: int
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
    
@app.post("/items/create/")
def create_item_with_model(item: Item):
    return item

@app.get("/items/model/{item_id}")
def read_item_with_model(item_id: int):
    return {"item_id": item_id, "name": "Sample Item", "price": 10.0}

@app.put("/items/model/{item_id}")
def update_item_with_model(item_id: int, item: Item):
    return {"item_id": item_id, "name": item.name, "price": item.price}

@app.delete("/items/model/{item_id}")
def delete_item_with_model(item_id: int):
    return {"item_id": item_id, "status": "deleted"}

@app.get("/search/")
def search_items(q: str):
    return {"results": f"Search results for query: {q}"}


@app.get("/categories/{category_id}/items/")
def read_category_items(category_id: int):
    return {"category_id": category_id, "items": ["item1", "item2", "item3"]}

@app.post("/categories/{category_id}/items/")
def create_category_item(category_id: int, item: Item): 
    return {"category_id": category_id, "item": item}  

@app.get("/reports/")
def get_reports():
    return {"reports": ["report1", "report2", "report3"]}   


@app.get("/metrics/")
def get_metrics():
    return {"metrics": {"uptime": "24h", "requests": 1000}}

@app.get("/config/")
def get_config():
    return {"config": {"setting1": True, "setting2": "value2"}}

@app.post("/config/")
def update_config(setting1: bool, setting2: str):
    return {"config": {"setting1": setting1, "setting2": setting2}}

@app.get("/logs/")
def get_logs():
    return {"logs": ["log1", "log2", "log3"]}

@app.post("/logs/")
def create_log(entry: str):
    return {"log_entry": entry, "status": "created"}