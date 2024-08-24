import logging

import uvicorn
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine, async_sessionmaker

from durov.infra.settings import Settings
from durov.infra.db.models import BaseModel


def init_logging(conf: Settings):
    """Initializes logging"""

    logging.getLogger("uvicorn").handlers.clear()

    logging.basicConfig(
        level=conf.logging_level, format=conf.logging_format, force=True
    )


async def get_engine(conf: Settings) -> AsyncEngine:
    """
    Initializes & returns SQLAlchemy's engine
    """

    logging.debug("Creating db's engine.")

    engine = create_async_engine(
        url=conf.db_url,
    )

    async with engine.begin() as conn:
        await conn.run_sync(BaseModel.metadata.create_all)

    return engine


async def get_session_maker(conf: Settings) -> async_sessionmaker:
    """
    Builds & returns session-maker
    :return: Initialized session-maker
    """
    engine = await get_engine(conf)
    return async_sessionmaker(engine, autoflush=True, expire_on_commit=False)


def get_uvicorn_logging_conf(conf: Settings):
    log_config = uvicorn.config.LOGGING_CONFIG
    log_config["formatters"]["access"]["fmt"] = conf.logging_format
    log_config["formatters"]["default"]["fmt"] = conf.logging_format

    return log_config


async def destroy_engine(engine: AsyncEngine):
    """Destroys engine"""
    await engine.dispose()
