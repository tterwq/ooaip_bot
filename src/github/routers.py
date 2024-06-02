from fastapi import APIRouter, Depends
from datetime import datetime
import requests


github_router = APIRouter(
    prefix="/github",
    tags=["Github"]
)
@github_router.get("/get_commits_id")
def get_commits_id(owner: str, repo: str):
    response = requests.get(f"https://api.github.com/repos/{owner}/{repo}commits").json()
    commits_id = []
    for number in response:
        commits_id.append(number["sha"])
    return commits_id


@github_router.get("/get_execution_time")
def get_execution_time(owner: str, repo: str, job_id: int):
    response = requests.get(f"https://api.github.com/repos/{owner}/{repo}/actions/jobs/{job_id}").json()
    job_start_time = datetime.fromisoformat(response["started_at"][:-1] + '+00:00')
    job_end_time = datetime.fromisoformat(response["completed_at"][:-1] + '+00:00')
    execution_time = job_end_time - job_start_time
    return execution_time

@github_router.get("/get_allocated_memory")
def get_allocated_memory(owner: str, repo: str, run_id: int):
    response = requests.get(f"https://api.github.com/repos/{owner}/{repo}/actions/runs/{run_id}/artifacts").json()
    size_b = []
    for number in response["artifacts"]:
        size_b.append(number["size_in_bytes"])
    return sum(size_b)

