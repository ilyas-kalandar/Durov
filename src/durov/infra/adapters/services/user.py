from durov.app.dto.user import UserRegisterParamsDTO, UserCreationParamsDTO
from durov.app.models.user import User
from durov.app.repos.user import UserRepoInterface
from durov.app.services.user import UserServiceInterface


class UserService(UserServiceInterface):
    """Implementation of `UserServiceInterface`"""

    def __init__(self, user_repo: UserRepoInterface):
        self._user_repo = user_repo

    async def register_user(self, params: UserRegisterParamsDTO):
        """
        Registers user
        :param params: A parameters
        :return: `
        """

        data = UserCreationParamsDTO(
            last_name=params.last_name,
            first_name=params.first_name,
            nickname=params.nickname,
        )

        return await self._user_repo.create(
            data,
        )

    async def get_user_by_nickname(self, nickname: str) -> User:
        """
        Returns user by its nickname
        :param nickname: A nickname
        :return: `User` object
        """

        return await self._user_repo.get_by_nickname(
            nickname,
        )
