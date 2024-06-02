from typing import List

from sqlalchemy import delete, select

from database import new_session
from github.users.models import User


class UserRepository:
    @classmethod
    async def add_user(cls, data: User) -> int:
        async with new_session() as session:
            user_dict = data.model_dump()
            user = User(**user_dict)
            session.add(user)
            await session.flush()
            await session.commit()
            return user.user_id

    @classmethod
    async def get_users(cls) -> List[User]:
        async with new_session() as session:
            query = select(User)
            result = await session.execute(query)
            user_models = result.scalars().all()
            return user_models

    @classmethod
    async def get_user_by_id(cls, user_id: int) -> User:
        async with new_session() as session:
            query = select(User).where(User.user_id == user_id)
            result = await session.execute(query)
            user_models = result.scalars().all()
            return user_models

    @classmethod
    async def delete_user_by_id(cls, user_id: int) -> int:
        async with new_session() as session:
            query = delete(User).where(User.user_id == user_id)
            result = await session.execute(query)
            num_deleted_rows = result.rowcount
            await session.flush()
            await session.commit()
            return num_deleted_rows

