from fastapi import Depends
from sqlalchemy.orm import Session, delete, select
from database import get_db
from models import User
from typing import List

async def add_user(data: User, db: Session = Depends(get_db)) -> int:
    user_dict = data.model_dump()
    user = User(**user_dict)
    db.add(user)
    await db.flush()
    await db.commit()
    return user.user_id

async def get_users(db: Session = Depends(get_db)) -> List[User]:
    query = select(User)
    result = await db.execute(query)
    user_models = result.scalars().all()
    return user_models

async def get_user_by_id(user_id: int, db: Session = Depends(get_db)) -> User:
    query = select(User).where(User.user_id == user_id)
    result = await db.execute(query)
    user_models = result.scalars().all()
    return user_models

async def delete_user_by_id(user_id: int, db: Session = Depends(get_db)) -> int:
    query = delete(User).where(User.user_id == user_id)
    result = await db.execute(query)
    num_deleted_rows = result.rowcount
    await db.flush()
    await db.commit()
    return num_deleted_rows
