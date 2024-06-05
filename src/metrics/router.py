from typing import Dict, Any

from fastapi import APIRouter, Depends

from datetime import datetime
from httpx import AsyncClient

from models import CommitMetrics
from repository import (
    add_commit_metric,
    get_metrics_by_commit_id,
    delete_metric_by_commit_id
)

metrics_router = APIRouter(
    prefix="/metrics",
    tags=["Metrics"]
)

@metrics_router.get("/get_execution_time")
async def get_execution_time(owner: str, repo: str, job_id: int):
    async with AsyncClient() as client:
        response = await client.get(f"https://api.github.com/repos/{owner}/{repo}/actions/jobs/{job_id}").json()
    job_start_time = datetime.fromisoformat(response["started_at"][:-1] + '+00:00')
    job_end_time = datetime.fromisoformat(response["completed_at"][:-1] + '+00:00')
    execution_time = job_end_time - job_start_time
    return execution_time

@metrics_router.get("/get_allocated_memory")
async def get_allocated_memory(owner: str, repo: str, run_id: int):
    async with AsyncClient() as client:
        response = await client.get(f"https://api.github.com/repos/{owner}/{repo}/actions/runs/{run_id}/artifacts").json()
    size_b = []
    for number in response["artifacts"]:
        size_b.append(number["size_in_bytes"])
    return sum(size_b)


@metrics_router.post("/add_metric")
async def add_commit_metric(metric: CommitMetrics = Depends(CommitMetrics)) -> Dict[str, Any]:
    metric_id = await add_commit_metric(metric)
    return {"ok": True, "metric_id": metric_id}

@metrics_router.get("/commit/{commit_id}")
async def get_metrics_by_commit_id(commit_id: int) -> CommitMetrics:
    metrics = await get_metrics_by_commit_id(commit_id)
    return metrics

@metrics_router.delete("/{commit_id}")
async def delete_metric_by_commit_id(commit_id: int) -> Dict[str, Any]:
    num_deleted_rows = await delete_metric_by_commit_id(commit_id)
    return {"ok": True, "num_deleted_rows": num_deleted_rows}
