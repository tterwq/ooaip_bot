from typing import Dict, Any

from fastapi import APIRouter, Depends

from github.metrics.models import CommitMetrics
from github.metrics.repository import CommitMetricsRepository


metrics_router = APIRouter(
    prefix="/metrics",
    tags=["Metrics"]
)

@metrics_router.post("/add_metric")
async def add_commit_metric(metric: CommitMetrics = Depends(CommitMetrics)) -> Dict[str, Any]:
    metric_id = await CommitMetricsRepository.add_commit_metric(metric)
    return {"ok": True, "metric_id": metric_id}

@metrics_router.get("/commit/{commit_id}")
async def get_metrics_by_commit_id(commit_id: int) -> CommitMetrics:
    metrics = await CommitMetricsRepository.get_metrics_by_commit_id(commit_id)
    return metrics

@metrics_router.delete("/{commit_id}")
async def delete_metric_by_commit_id(commit_id: int) -> Dict[str, Any]:
    num_deleted_rows = await CommitMetricsRepository.delete_metric_by_commit_id(commit_id)
    return {"ok": True, "num_deleted_rows": num_deleted_rows}
