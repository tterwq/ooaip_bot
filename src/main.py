from fastapi import FastAPI
from commits.router import commits_router
from metrics.router import metrics_router
from users.router import users_router

app = FastAPI()

app.include_router(commits_router)
app.include_router(metrics_router)
app.include_router(users_router)
