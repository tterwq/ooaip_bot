from typing import List, Dict, Any

from fastapi import APIRouter, Depends
import requests

from models import UserCommits
from repository import UserCommitsRepository


commits_router = APIRouter(
    prefix="/commits",
    tags=["Commits"]
)

@commits_router.get("/get_commits_id")
def get_commits_id(owner: str, repo: str):
    response = requests.get(f"https://api.github.com/repos/{owner}/{repo}commits").json()
    commits_id = []
    for number in response:
        commits_id.append(number["sha"])
    return commits_id

@commits_router.post("/add_commit")
async def add_commit(commit: UserCommits = Depends(UserCommits)) -> Dict[str, Any]:
    commit_id = await UserCommitsRepository.add_commit(commit)
    return {"ok": True, "commit_id": commit_id}

@commits_router.get("/user/{user_id}")
async def get_commits_by_user_id(user_id: int) -> List[UserCommits]:
    commits = await UserCommitsRepository.get_commits_by_user_id(user_id)
    return commits

@commits_router.delete("/{commit_id}")
async def delete_commit_by_id(commit_id: int) -> Dict[str, Any]:
    num_deleted_rows = await UserCommitsRepository.delete_commit_by_id(commit_id)
    return {"ok": True, "num_deleted_rows": num_deleted_rows}

