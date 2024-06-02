from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey
from datetime import time

from models import BaseModel


class CommitMetrics(BaseModel):
    __tablename__ = 'commit_metrics'

    commit_id: Mapped[int] = mapped_column(ForeignKey("user_commits.commit_id", ondelete="CASCADE"), primary_key=True)
    execution_time: Mapped[time]
    allocated_memory: Mapped[int]
