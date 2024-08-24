from sqlalchemy import select

from durov.app.dto.user import UserCreationParamsDTO
from durov.app.exceptions.user import UserNotFound
from durov.app.models.user import User
from durov.app.repos.user import UserRepoInterface
from durov.infra.adapters.repos.base import BaseSQLAlchemyRepo
from durov.infra.db import models


class UserRepo(BaseSQLAlchemyRepo, UserRepoInterface):
    """Impl of `UserRepoInterface`"""

    async def create(self, params: UserCreationParamsDTO):
        """
        Creates a user
        :param params: Creation params
        :return: Created user
        """

        # TODO(Ilyas): Some validations needed, ex: User.nickname

        obj = models.User(
            first_name=params.first_name,
            last_name=params.last_name,
            nickname=params.nickname,
        )

        self._session.add(obj)
        await self._session.flush()
        await self._session.commit()
        await self._session.refresh(obj)

        return obj.to_domain()

    async def get_by_nickname(self, nickname: str) -> User:
        """
        Returns user by its nickname
        :param nickname: A nickname (ex: durov)
        :return: `User` object if found
        """

        results = await self._session.execute(
            select(models.User).where(models.User.nickname == nickname).limit(1)
        )

        first_one = results.scalars().first()

        if first_one is None:
            raise UserNotFound("User not found")

        return first_one.to_domain()
