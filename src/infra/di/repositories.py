from dishka import Provider, Scope, provide
from sqlalchemy.ext.asyncio import AsyncSession

from src.domain.interfaces.repositories.user import IUserRepository
from src.infra.repositories.sqlalchemy.user import SQLAlchemyUserRepository


class RepositoriesProvider(Provider):
    """DI provider of repositories."""

    scope = Scope.REQUEST

    @provide
    def get_user_repo(self, session: AsyncSession) -> IUserRepository:
        return SQLAlchemyUserRepository(session=session)
