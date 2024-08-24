from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from durov.app.repos.user import UserRepoInterface
from durov.app.services.user import UserServiceInterface
from durov.infra.adapters.repos.user import UserRepo
from durov.infra.adapters.services.user import UserService
from durov.presentation.api.dependencies.common import get_session


def get_user_repo(session: AsyncSession = Depends(get_session)) -> UserRepoInterface:
    return UserRepo(session)


def get_user_service(
    repo: UserRepoInterface = Depends(get_user_repo),
) -> UserServiceInterface:
    service = UserService(
        repo,
    )

    return service
