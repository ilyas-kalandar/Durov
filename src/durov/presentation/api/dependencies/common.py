from fastapi import Request

from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession


async def get_session(request: Request) -> AsyncSession:
    """Returns `sqlalchemy.ext.asyncio.AsyncSession` object"""
    maker: async_sessionmaker = request.app.state.session_maker
    se = maker()
    yield se
    await se.close()
