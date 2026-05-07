from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from src.domain.interfaces.uow import IUnitOfWork
from src.infra.repositories.sqlalchemy.user import SQLAlchemyUserRepository


class SQLAlchemyUnitOfWork(IUnitOfWork):
    def __init__(self, session_factory: async_sessionmaker[AsyncSession]):
        self._session_factory = session_factory
        self._session: AsyncSession | None = None

    async def __aenter__(self) -> "SQLAlchemyUnitOfWork":
        self._session = self._session_factory()

        # Repositories inject
        self.users = SQLAlchemyUserRepository(session=self._session)

        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        if exc_type is not None:
            await self.rollback()

        if self._session:
            await self._session.close()

    async def commit(self) -> None:
        if self._session:
            await self._session.commit()

    async def rollback(self) -> None:
        if self._session:
            await self._session.rollback()
