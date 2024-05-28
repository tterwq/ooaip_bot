from typing import List

from sqlalchemy import delete, select

from database import new_session
from models import User, UserCommits, CommitMetrics


class UserService:
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


class UserCommitsService:
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


class CommitMetricsService:
    @classmethod
    async def add_commit_metric(cls, data: CommitMetrics) -> int:
        async with new_session() as session:
            metric_dict = data.model_dump()
            metric = CommitMetrics(**metric_dict)
            session.add(metric)
            await session.flush()
            await session.commit()
            return metric.commit_id

    @classmethod
    async def get_metrics_by_commit_id(cls, commit_id: int) -> CommitMetrics:
        async with new_session() as session:
            query = select(CommitMetrics).where(CommitMetrics.commit_id == commit_id)
            result = await session.execute(query)
            metric_models = result.scalars().all()
            return metric_models

    @classmethod
    async def delete_metric_by_commit_id(cls, commit_id: int) -> int:
        async with new_session() as session:
            query = delete(CommitMetrics).where(CommitMetrics.commit_id == commit_id)
            result = await session.execute(query)
            num_deleted_rows = result.rowcount
            await session.flush()
            await session.commit()
            return num_deleted_rows