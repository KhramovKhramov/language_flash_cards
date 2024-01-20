from pydantic import PostgresDsn
from pydantic_settings import BaseSettings

from src.exceptions import db_connect_data_exception


class Settings(BaseSettings):
    DATABASE_USER: str | None = None
    DATABASE_PASSWORD: str | None = None
    DATABASE_HOST: str | None = None
    DATABASE_PORT: str | None = None
    DATABASE_NAME: str | None = None
    DATABASE_DSN: PostgresDsn | None = None

    @property
    def database_url(self) -> str:
        if self.DATABASE_DSN:
            return str(self.DATABASE_DSN)

        if not all(
            (
                self.DATABASE_USER,
                self.DATABASE_PASSWORD,
                self.DATABASE_HOST,
                self.DATABASE_PORT,
                self.DATABASE_NAME,
            ),
        ):
            raise db_connect_data_exception
        return (
            f'postgresql+asyncpg://'
            f'{self.DATABASE_USER}:{self.DATABASE_PASSWORD}@'
            f'{self.DATABASE_HOST}:{self.DATABASE_PORT}/{self.DATABASE_NAME}'
        )


settings = Settings(
    _env_file='.env',
    _env_file_encoding='utf-8',
)
