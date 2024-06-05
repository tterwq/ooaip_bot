from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from commits.router import commits_router
from metrics.router import metrics_router
from users.router import users_router
from checker.router import checker_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(commits_router)
app.include_router(metrics_router)
app.include_router(users_router)
app.include_router(checker_router)
