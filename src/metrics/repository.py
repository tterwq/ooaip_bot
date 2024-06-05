from fastapi import Depends
from sqlalchemy.orm import Session
from sqlalchemy import delete, select
from database import get_db
from .models import CommitMetrics

async def add_commit_metric(data: CommitMetrics, db: Session = Depends(get_db)) -> int:
    metric_dict = data.model_dump()
    metric = CommitMetrics(**metric_dict)
    db.add(metric)
    await db.flush()
    await db.commit()
    return metric.commit_id

async def get_metrics_by_commit_id(commit_id: int, db: Session = Depends(get_db)) -> CommitMetrics:
    query = select(CommitMetrics).where(CommitMetrics.commit_id == commit_id)
    result = await db.execute(query)
    metric_models = result.scalars().all()
    return metric_models

async def delete_metric_by_commit_id(commit_id: int, db: Session = Depends(get_db)) -> int:
    query = delete(CommitMetrics).where(CommitMetrics.commit_id == commit_id)
    result = await db.execute(query)
    num_deleted_rows = result.rowcount
    await db.flush()
    await db.commit()
    return num_deleted_rows
