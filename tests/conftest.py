import pytest

from fastapi.testclient import TestClient

from durov.infra.settings import load_settings
from durov.presentation.api.app_builder import build_fastapi_app


@pytest.fixture
def configuration():
    return load_settings()


@pytest.fixture
def client(configuration) -> TestClient:
    """Provides `fastapi.TestClient` object (basically `httpx.TestClient`)"""

    fastapi_application = build_fastapi_app()

    with TestClient(
        app=fastapi_application,
        base_url=f"http://{configuration.serving_host}:{configuration.serving_port}",
    ) as client:
        yield client
