import asyncio
import logging
from collections import defaultdict
from asyncio import Future
from random import randint
from typing import Dict

from sqlalchemy import select

from durov.app.dto.user import UserCreationParamsDTO
from durov.app.exceptions.user import UserNotFound
from durov.app.models.user import User
from durov.app.repos.user import UserRepoInterface
from durov.infra.adapters.repos.base import BaseSQLAlchemyRepo
from durov.infra.db import models

# Mock-cache
CACHE: Dict[str, User] = {}

# For futures
FUTURES: Dict[str, Future[User]] = {}
REFS: Dict[str, int] = defaultdict(int)

# Locker
lock = asyncio.Lock()


class UserRepo(BaseSQLAlchemyRepo, UserRepoInterface):
    """Impl of `UserRepoInterface`"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._logger = logging.getLogger("user-repo")

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

    async def _get_from_db(self, nickname: str) -> User:
        # Very slow method

        await asyncio.sleep(10)  # 10 seconds delay

        results = await self._session.execute(
            select(models.User).where(models.User.nickname == nickname).limit(1)
        )

        first_one = results.scalars().first()

        if first_one is None:
            raise UserNotFound("User not found")

        # Generate random identifier
        random_id = randint(1, 20)

        return User(
            id=random_id,
            nickname=first_one.nickname,
            last_name=first_one.last_name,
            first_name=first_one.first_name,
        )

    async def _get_from_cache(self, nickname: str) -> User:
        # Slow method too

        await asyncio.sleep(3)

        if nickname not in CACHE:
            CACHE[nickname] = await self._get_from_db(nickname)

        return CACHE[nickname]

    async def get_by_nickname(self, nickname: str) -> User:
        """
        Returns user by its nickname
        :param nickname: A nickname (ex: durov)
        :return: `User` object if found
        """

        async with lock:
            self._logger.info("Added ref for nickname: %s", nickname)
            REFS[nickname] += 1

            if nickname not in FUTURES:
                self._logger.info("Added future for nickname: %s", nickname)
                loop = asyncio.get_event_loop()
                FUTURES[nickname] = loop.create_future()
                user = await self._get_from_cache(nickname)

                FUTURES[nickname].set_result(user)

        self._logger.info("Waiting for future for %s", nickname)
        result = await FUTURES[nickname]

        async with lock:
            REFS[nickname] -= 1
            if REFS[nickname] == 0:
                del REFS[nickname]
                del FUTURES[nickname]

        return result
