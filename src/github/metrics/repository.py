from sqlalchemy import delete, select

from database import new_session
from github.metrics.models import CommitMetrics


class CommitMetricsRepository:
    @classmethod
    async def add_commit_metric(cls, data: CommitMetrics) -> int:
        async with new_session() as session:
            metric_dict = data.model_dump()
            metric = CommitMetrics(**metric_dict)
            session.add(metric)
            await session.flush()
            await session.commit()
            return metric.commit_id

    @classmethod
    async def get_metrics_by_commit_id(cls, commit_id: int) -> CommitMetrics:
        async with new_session() as session:
            query = select(CommitMetrics).where(CommitMetrics.commit_id == commit_id)
            result = await session.execute(query)
            metric_models = result.scalars().all()
            return metric_models

    @classmethod
    async def delete_metric_by_commit_id(cls, commit_id: int) -> int:
        async with new_session() as session:
            query = delete(CommitMetrics).where(CommitMetrics.commit_id == commit_id)
            result = await session.execute(query)
            num_deleted_rows = result.rowcount
            await session.flush()
            await session.commit()
            return num_deleted_rows