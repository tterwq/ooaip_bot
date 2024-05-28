from typing import List, Dict, Any

from fastapi import APIRouter, Depends

from github.models import User, UserCommits, CommitMetrics
from github.service import UserService, UserCommitsService, CommitMetricsService


users_router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@users_router.post("/add_user")
async def add_user(user: User = Depends(User)) -> Dict[str, Any]:
    user_id = await UserService.add_user(user)
    return {"ok": True, "user_id": user_id}

@users_router.get("")
async def get_all_users() -> List[User]:
    users = await UserService.get_users()
    return users

@users_router.get("/{user_id}")
async def get_user_by_id(user_id: int) -> User:
    user = await UserService.get_user_by_id(user_id)
    return user

@users_router.delete("/{user_id}")
async def delete_user_by_id(user_id: int) -> Dict[str, Any]:
    num_deleted_rows = await UserService.delete_user_by_id(user_id)
    return {"ok": True, "num_deleted_rows": num_deleted_rows}


commits_router = APIRouter(
    prefix="/commits",
    tags=["Commits"]
)

@commits_router.post("/add_commit")
async def add_commit(commit: UserCommits = Depends(UserCommits)) -> Dict[str, Any]:
    commit_id = await UserCommitsService.add_commit(commit)
    return {"ok": True, "commit_id": commit_id}

@commits_router.get("/user/{user_id}")
async def get_commits_by_user_id(user_id: int) -> List[UserCommits]:
    commits = await UserCommitsService.get_commits_by_user_id(user_id)
    return commits

@commits_router.delete("/{commit_id}")
async def delete_commit_by_id(commit_id: int) -> Dict[str, Any]:
    num_deleted_rows = await UserCommitsService.delete_commit_by_id(commit_id)
    return {"ok": True, "num_deleted_rows": num_deleted_rows}


metrics_router = APIRouter(
    prefix="/metrics",
    tags=["Metrics"]
)

@metrics_router.post("/add_metric")
async def add_commit_metric(metric: CommitMetrics = Depends(CommitMetrics)) -> Dict[str, Any]:
    metric_id = await CommitMetricsService.add_commit_metric(metric)
    return {"ok": True, "metric_id": metric_id}

@metrics_router.get("/commit/{commit_id}")
async def get_metrics_by_commit_id(commit_id: int) -> CommitMetrics:
    metrics = await CommitMetricsService.get_metrics_by_commit_id(commit_id)
    return metrics

@metrics_router.delete("/{commit_id}")
async def delete_metric_by_commit_id(commit_id: int) -> Dict[str, Any]:
    num_deleted_rows = await CommitMetricsService.delete_metric_by_commit_id(commit_id)
    return {"ok": True, "num_deleted_rows": num_deleted_rows}
