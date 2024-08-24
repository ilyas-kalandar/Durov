from contextlib import asynccontextmanager

from fastapi import FastAPI

from durov.infra.settings import Settings, load_settings
from durov.presentation.api.boot import (
    init_logging,
    destroy_engine,
    get_engine,
    get_session_maker,
)
from durov.presentation.api.routers import user


def build_lifespan(configuration: Settings):
    @asynccontextmanager
    async def lifespan(app: FastAPI):
        init_logging(configuration)
        engine = await get_engine(configuration)

        session_maker = await get_session_maker(configuration)

        app.state.settings = configuration
        app.state.session_maker = session_maker
        app.state.db_engine = engine

        yield
        await destroy_engine(engine)

    return lifespan


def build_fastapi_app():
    """Builds & returns `FastAPI`"""
    settings = load_settings()

    lifespan = build_lifespan(
        settings,
    )
    app = FastAPI(
        title="Durov",
        version="0.1",
        description="A test task",
        lifespan=lifespan,
    )

    # TODO(Ilyas): Will be better, if we override deps.

    app.include_router(
        user.router,
    )

    return app
