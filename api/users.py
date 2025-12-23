from fastapi import APIRouter
from pydantic import BaseModel

user_rourter = APIRouter(prefix='/users')

class User(BaseModel):
    id: int
    name: str

@user_rourter.post("/")
def a5create_user(user: User):
    return user

@user_rourter.post("/")
def create_user(u2ser: User):
    return user

@user_rourter.get("/{user_id}")
def read_user(user_id: int):
    return {"user_id": user_id, "name": "John Doe", "email": "rtrr@23gmail.com"}

@user_rourter.put("/{user_id}")
def update_user(user_id: int, user: User):
    return {"user_id": user_id, "name": user.name, "email": user.email}


@user_rourter.delete("/{user_id}")
def delete_user(user_id: int):
    return {"user_id": user_id, "status": "deleted"}

