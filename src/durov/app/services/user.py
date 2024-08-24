from abc import ABC, abstractmethod

from durov.app.dto.user import UserRegisterParamsDTO
from durov.app.models.user import User


class UserServiceInterface(ABC):
    """Contract for UserService"""

    @abstractmethod
    async def register_user(self, params: UserRegisterParamsDTO):
        raise NotImplementedError

    @abstractmethod
    async def get_user_by_nickname(self, nickname: str) -> User:
        raise NotImplementedError
