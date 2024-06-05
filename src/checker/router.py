from .utils import check_similary
from metrics.schemas import CommitMetricsSchema

from typing import List, Dict, Any

from fastapi import APIRouter, Depends
from httpx import AsyncClient


checker_router = APIRouter(
    prefix="/checker",
    tags=["Checer"]
)

@checker_router.get("/check_jobs")
async def get_commits_id(metrics: Dict[str, CommitMetricsSchema]):
    return check_similary(metrics["metrics_1"].__dict__, metrics["metrics_2"].__dict__)
