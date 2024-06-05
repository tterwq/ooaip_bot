from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import delete, select
from database import get_db
from .models import UserCommits
from typing import List

async def add_commit(data: UserCommits, db: AsyncSession = Depends(get_db)) -> int:
    commit_dict = data.model_dump()
    commit = UserCommits(**commit_dict)
    db.add(commit)
    await db.flush()
    await db.commit()
    return commit.commit_id

async def get_commits_by_user_id(user_id: int, db: AsyncSession = Depends(get_db)) -> List[UserCommits]:
    query = select(UserCommits).where(UserCommits.user_id == user_id)
    result = await db.execute(query)
    commit_models = result.scalars().all()
    return commit_models

async def delete_commit_by_id(commit_id: int, db: AsyncSession = Depends(get_db)) -> int:
    query = delete(UserCommits).where(UserCommits.commit_id == commit_id)
    result = await db.execute(query)
    num_deleted_rows = result.rowcount
    await db.flush()
    await db.commit()
    return num_deleted_rows

