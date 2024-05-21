"""from github import Github
from src.github.service import GetUserCommitsService, GetCommitMetricsService
from src.config import settings
from src.db import async_session

# Аутентификация с использованием вашего токена GitHub
g = Github(settings.GITHUB_TOKEN)

# Получение репозитория, на который вы хотите реагировать
repo = g.get_repo("username/repository")

def handle_push(payload):
    commit_id = payload['head_commit']['id']
    async with async_session() as s:
        commit_service = GetCommitMetricsService(s)
        metrics = await commit_service.get_commit_metrics(commit_id)
        print(metrics)

def handle_workflow_run(payload):
    if payload['action'] == 'completed':
        async with async_session() as s:
            user_service = GetUserCommitsService(s)
            user_commits = await user_service.get_user_commits(payload['sender']['login'])
            print(user_commits)

event_handlers = {
    'push': handle_push,
    'workflow_run': handle_workflow_run,
}

def handle_event(event, payload):
    handler = event_handlers.get(event)
    if handler is not None:
        handler(payload)

# Здесь вы можете добавить код для запуска вашего бота и прослушивания веб-хуков GitHub
"""