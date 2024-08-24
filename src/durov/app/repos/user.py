from abc import ABC, abstractmethod

from durov.app.dto.user import UserCreationParamsDTO
from durov.app.models.user import User


class UserRepoInterface(ABC):
    """Contract for user-repo"""

    @abstractmethod
    async def create(self, params: UserCreationParamsDTO):
        """
        Creates a user
        :param params: Creation params
        :return: Created user
        """
        raise NotImplementedError

    @abstractmethod
    async def get_by_nickname(self, nickname: str) -> User:
        """
        Returns user by its nickname
        :param nickname: A nickname (ex: durov)
        :return: `User` object if found
        """
        raise NotImplementedError
