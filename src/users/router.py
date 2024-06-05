from typing import List, Dict, Any

from fastapi import APIRouter, Depends

from .models import User
from .schemas import UserSchema
from .repository import (
    add_user,
    get_users,
    get_user_by_id,
    delete_user_by_id
)

users_router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@users_router.post("/add_user")
async def add_user(user: User = Depends(User)) -> Dict[str, Any]:
    user_id = await add_user(user)
    return {"ok": True, "user_id": user_id}

@users_router.get("")
async def get_all_users() -> List[UserSchema]:
    users = await get_users()
    res = [UserSchema.model_validate(obj) for obj in users]
    return res

@users_router.get("/{user_id}")
async def get_user_by_id(user_id: int) -> UserSchema:
    user = await get_user_by_id(user_id)
    res = UserSchema.model_validate(user)
    return res

@users_router.delete("/{user_id}")
async def delete_user_by_id(user_id: int) -> Dict[str, Any]:
    num_deleted_rows = await delete_user_by_id(user_id)
    return {"ok": True, "num_deleted_rows": num_deleted_rows}
