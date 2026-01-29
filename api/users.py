from fastapi import APIRouter, HTTPException, Query, Path
from pydantic import BaseModel
from typing import List, Optional

# Создаем роутер с префиксом и тегами для документации Swagger
user_router = APIRouter(prefix="/users", tags=["Users"])

# Модель данных пользователя
class UserProfile(BaseModel):
    id: int
    username: str
    email: str
    is_superhero: bool = False

# Имитация базы данных
fake_users_db = [
    {"id": 1, "username": "clark_kent", "email": "clark@dailyplanet.com", "is_superhero": True},
    {"id": 2, "username": "bruce_wayne", "email": "bruce@wayne.corp", "is_superhero": False},
]

@user_router.get("/", response_model=List[UserProfile])
async def get_all_users():
    """Получить список всех жителей Метрополиса"""
    return fake_users_db

@user_router.get("/{user_id}", response_model=UserProfile)
async def get_user_by_id(user_id: int = Path(..., title="ID пользователя", ge=1)):
    """Поиск пользователя по его уникальному ID"""
    user = next((u for u in fake_users_db if u["id"] == user_id), None)
    if not user:
        raise HTTPException(status_code=404, detail="Герой не найден в базе")
    return user

@user_router.post("/create", status_code=201)
async def create_new_user(user: UserProfile):
    """Регистрация нового пользователя в системе"""
    fake_users_db.append(user.dict())
    return {"status": "success", "message": f"Пользователь {user.username} добавлен"}