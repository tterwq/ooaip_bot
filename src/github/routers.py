from src.github.service import GetUserCommitsService, GetCommitMetricsService
from src.config import settings
from src.database import async_session

router = Router()

@router.message(Navigation.users, types.ContentType.TEXT)
async def create_user(user_id: types.Message, state: FSMContext):
    async with async_session() as s:
        user_service = GetUserCommitsService(s)
        response = await user_service.get_user_commits(user_id.text)
        if response:
            await state.set_state(Navigation.user_commits)

@router.message(Navigation.user_commits, types.ContentType.TEXT)
async def create_commit(commit_id: types.Message, state: FSMContext):
    async with async_session() as s:
        commit_service = GetCommitMetricsService(s)
        response = await commit_service.get_commit_metrics(commit_id.text)
        if response:
            await state.set_state(Navigation.commit_metrics)
