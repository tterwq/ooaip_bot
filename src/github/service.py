from sqlalchemy.orm import Session
from .models import UserCommits, CommitMetrics

class GetUserCommitsService:
    def __init__(self, session: Session):
        self.session = session

    async def get_user_commits(self, user_id: int):
        user_commits = self.session.query(UserCommits).filter(UserCommits.user_id == user_id).all()
        return user_commits
    from .models import CommitMetrics

class GetCommitMetricsService:
    def __init__(self, session: Session):
        self.session = session

    async def get_commit_metrics(self, commit_id: int):
        commit_metrics = self.session.query(CommitMetrics).filter(CommitMetrics.commit_id == commit_id).first()
        return commit_metrics