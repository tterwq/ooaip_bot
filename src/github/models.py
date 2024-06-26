from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey
from datetime import time

from models import BaseModel


class User(BaseModel):
    __tablename__ = 'users'

    user_id: Mapped[int] = mapped_column(primary_key=True)


class UserCommits(BaseModel):
    __tablename__ = 'user_commits'

    commit_id: Mapped[int] = mapped_column(primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.user_id", ondelete="CASCADE"))


class CommitMetrics(BaseModel):
    __tablename__ = 'commit_metrics'

    commit_id: Mapped[int] = mapped_column(ForeignKey("user_commits.commit_id", ondelete="CASCADE"), primary_key=True)
    execution_time: Mapped[time]
    allocated_memory: Mapped[int]
