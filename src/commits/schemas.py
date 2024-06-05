from pydantic import BaseModel


class UserCommitsSchema(BaseModel):
    commit_id: int
    user_id: int