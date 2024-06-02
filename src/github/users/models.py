from sqlalchemy.orm import Mapped, mapped_column

from models import BaseModel


class User(BaseModel):
    __tablename__ = 'users'

    user_id: Mapped[int] = mapped_column(primary_key=True)