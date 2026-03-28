from typing import Any, Literal

from pydantic import model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Main project settings."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="allow",
        case_sensitive=True,
    )

    # .env core
    ENVIRONMENT: Literal["dev", "prod"]
    DEBUG: bool

    # FastAPI
    FASTAPI_TITLE: str = "Flashcards"
    FASTAPI_VERSION: str = "0.0.1"
    FASTAPI_DESCRIPTION: str = (
        "The system of language flashcards for learning foreign words"
    )
    FASTAPI_DOCS_URL: str = "/docs"
    FASTAPI_REDOC_URL: str = "/redoc"
    FASTAPI_OPENAPI_URL: str | None = "/openapi"

    # .env database
    DB_USER: str | None = None
    DB_PASSWORD: str | None = None
    DB_HOST: str | None = None
    DB_PORT: str | None = None
    DB_NAME: str | None = None

    @classmethod
    @model_validator(mode="before")
    def check_env(cls, values: Any) -> Any:
        if values.get("ENVIRONMENT") == "prod":
            # FastAPI
            values["FASTAPI_OPENAPI_URL"] = None

        return values
