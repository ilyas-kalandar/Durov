from sqlalchemy.ext.asyncio import AsyncSession


class BaseSQLAlchemyRepo:
    """Base for all alchemy-repos"""

    def __init__(self, session: AsyncSession):
        """
        Initializes self
        :param session: An async-session object
        """
        self._session = session
