from abc import ABC, abstractmethod

from durov.app.models.user import User


class UserServiceInterface(ABC):
    """Contract for UserService"""

    @abstractmethod
    async def register_user(self):
        raise NotImplementedError

    @abstractmethod
    async def get_user_by_nickname(self, nickname: str) -> User:
        raise NotImplementedError
