import contextlib
from collections.abc import AsyncGenerator
from typing import Annotated

import sqlalchemy.orm
from fastapi import Depends
from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import (
    async_sessionmaker,
    AsyncAttrs,
    AsyncSession,
    create_async_engine,
)

from src.config import settings


class Base(AsyncAttrs, sqlalchemy.orm.DeclarativeBase):
    """Base model"""

    metadata = MetaData(
        naming_convention={
            "ix": "ix_%(column_0_label)s",
            "uq": "uq_%(table_name)s_%(column_0_name)s",
            "ck": "ck_%(table_name)s_`%(constraint_name)s`",
            "fk": (
                "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s"
            ),
            "pk": "pk_%(table_name)s",
        },
    )

    def __repr__(self):
        """
        Печать орм-объектов с отображением атрибутов
        """

        fmt = '{}.{}({})'
        package = self.__class__.__module__
        class_ = self.__class__.__name__
        attrs = sorted(
            (k, getattr(self, k)) for k in self.__mapper__.columns.keys()
        )
        sattrs = ', '.join('{}={!r}'.format(*x) for x in attrs)
        return fmt.format(package, class_, sattrs)


engine = create_async_engine(settings.database_url)
async_session = async_sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:  # type: AsyncSession
        try:
            yield session
        except Exception as exc:
            await session.rollback()
            raise exc
        else:
            await session.commit()


session_context_manager = contextlib.asynccontextmanager(get_session)

SessionDep = Annotated[AsyncSession, Depends(get_session)]
