from dishka import make_async_container
from dishka.integrations.fastapi import setup_dishka
from fastapi import FastAPI

from src.core.config import Settings
from src.infra.di.postgres import PostgresProvider
from src.infra.di.settings import SettingsProvider


def create_app(settings: Settings) -> FastAPI:
    """FastAPI app registration."""

    app = FastAPI(
        title=settings.FASTAPI_TITLE,
        version=settings.FASTAPI_VERSION,
        description=settings.FASTAPI_DESCRIPTION,
        docs_url=settings.FASTAPI_DOCS_URL,
        redoc_url=settings.FASTAPI_REDOC_URL,
        openapi_url=settings.FASTAPI_OPENAPI_URL,
    )

    # DI inject
    container = make_async_container(
        SettingsProvider(settings=settings),
        PostgresProvider(),
    )
    setup_dishka(container, app)

    return app
