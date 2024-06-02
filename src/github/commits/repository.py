from typing import List

from sqlalchemy import delete, select

from database import new_session
from github.commits.models import UserCommits


class UserCommitsRepository:
    @classmethod
    async def add_commit(cls, data: UserCommits) -> int:
        async with new_session() as session:
            commit_dict = data.model_dump()
            commit = UserCommits(**commit_dict)
            session.add(commit)
            await session.flush()
            await session.commit()
            return commit.commit_id

    @classmethod
    async def get_commits_by_user_id(cls, user_id: int) -> List[UserCommits]:
        async with new_session() as session:
            query = select(UserCommits).where(UserCommits.user_id == user_id)
            result = await session.execute(query)
            commit_models = result.scalars().all()
            return commit_models

    @classmethod
    async def delete_commit_by_id(cls, commit_id: int) -> int:
        async with new_session() as session:
            query = delete(UserCommits).where(UserCommits.commit_id == commit_id)
            result = await session.execute(query)
            num_deleted_rows = result.rowcount
            await session.flush()
            await session.commit()
            return num_deleted_rows
