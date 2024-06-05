from pydantic import BaseModel
from datetime import time


class CommitMetricsSchema(BaseModel):

    commit_id: int
    execution_time: time
    allocated_memory: int