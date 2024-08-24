import uvicorn
import click

from durov.infra.settings import load_settings
from durov.presentation.api.boot import get_uvicorn_logging_conf


@click.command("run")
@click.option("--hot-reload", is_flag=True, help="Enable hot reload")
def main(
    hot_reload: bool = False,
):
    """Entrypoint"""

    settings = load_settings()
    logging_conf = get_uvicorn_logging_conf(settings)

    uvicorn.run(
        "durov.presentation.api.app_builder:build_fastapi_app",
        host=settings.serving_host,
        port=settings.serving_port,
        log_config=logging_conf,
        factory=True,
        lifespan="on",
        loop="uvloop",
        reload=hot_reload,
    )


main()
