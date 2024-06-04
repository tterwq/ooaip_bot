from typing import List, Dict, Any

from fastapi import APIRouter, Depends

from models import User
from repository import UserRepository

users_router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@users_router.post("/add_user")
async def add_user(user: User = Depends(User)) -> Dict[str, Any]:
    user_id = await UserRepository.add_user(user)
    return {"ok": True, "user_id": user_id}

@users_router.get("")
async def get_all_users() -> List[User]:
    users = await UserRepository.get_users()
    return users

@users_router.get("/{user_id}")
async def get_user_by_id(user_id: int) -> User:
    user = await UserRepository.get_user_by_id(user_id)
    return user

@users_router.delete("/{user_id}")
async def delete_user_by_id(user_id: int) -> Dict[str, Any]:
    num_deleted_rows = await UserRepository.delete_user_by_id(user_id)
    return {"ok": True, "num_deleted_rows": num_deleted_rows}

