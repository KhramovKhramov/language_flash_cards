from dishka import Provider, Scope, provide
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from src.domain.interfaces.uow import IUnitOfWork
from src.infra.uow import SQLAlchemyUnitOfWork


class UoWProvider(Provider):
    """DI provider of Unit of Work pattern."""

    scope = Scope.REQUEST

    @provide
    def get_uow(
        self, sessionmaker: async_sessionmaker[AsyncSession]
    ) -> IUnitOfWork:
        return SQLAlchemyUnitOfWork(session_factory=sessionmaker)
