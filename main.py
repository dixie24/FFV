from typing import Union
from pydantic import BaseModel
from fastapi import FastAPI
from api.users import user_rourter
from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi import FastAPI, BackgroundTasks
import time
from fastapi import File, UploadFile, Header, HTTPException, Depends
from enum import Enum


app = FastAPI()
app.include_router(user_rourter)


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




class PowerLevel(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"
    god = "god"

@app.get("/hero/power/{level}")
async def get_hero_by_power(level: PowerLevel):
    if level == PowerLevel.god:
        return {"message": "Это уровень Супермена!"}
    return {"message": f"Уровень силы: {level.value}"}

@app.get("/headers/")
async def read_headers(user_agent: Union[str, None] = Header(default=None)):
    if user_agent:
        return {"User-Agent": user_agent}
    else:
        raise HTTPException(status_code=400, detail="User-Agent header is missing")

@app.post("/upload-map/")
async def upload_secret_map(file: UploadFile = File(...)):
    # file.filename - имя файла
    # file.file - сам объект файла для чтения
    contents = await file.read() 
    return {
        "filename": file.filename, 
        "size": len(contents),
        "content_type": file.content_type
    }



@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request) # Передаем запрос дальше
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    print(f"Запрос обработан за: {process_time:.4f} сек")
    return response

def write_log(message: str):
    with open("log.txt", "a") as log_file:
        log_file.write(f"{time.ctime()}: {message}\n")  



@app.post("/process/")
async def process_data(background_tasks: BackgroundTasks, data: str):
    background_tasks.add_task(write_log, f"Обработка данных: {data}")
    return {"message": "Данные обрабатываются в фоновом режиме"}
