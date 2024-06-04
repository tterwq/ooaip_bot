from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey

from models import BaseModel


class UserCommits(BaseModel):
    __tablename__ = 'user_commits'

    commit_id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.user_id", ondelete="CASCADE"))