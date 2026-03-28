from fastapi import FastAPI

from src.core.config import Settings


def create_app(settings: Settings) -> FastAPI:
    """FastAPI app registration."""

    return FastAPI(
        title=settings.FASTAPI_TITLE,
        version=settings.FASTAPI_VERSION,
        description=settings.FASTAPI_DESCRIPTION,
        docs_url=settings.FASTAPI_DOCS_URL,
        redoc_url=settings.FASTAPI_REDOC_URL,
        openapi_url=settings.FASTAPI_OPENAPI_URL,
    )
