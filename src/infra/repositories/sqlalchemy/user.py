from sqlalchemy.ext.asyncio import AsyncSession

from src.domain.entities.user import User
from src.domain.interfaces.repositories.user import IUserRepository
from src.infra.postgres.models import UserORM


class SQLAlchemyUserRepository(IUserRepository):
    def __init__(self, session: AsyncSession):
        self._session = session

    async def add(self, data: User) -> User:
        """Saving User to database."""

        new_user: UserORM = UserORM(
            first_name=data.first_name,
            last_name=data.last_name,
            date_of_birth=data.date_of_birth,
            gender=data.gender,
            email=data.email,
            is_active=data.is_active,
            join_time=data.join_time,
        )

        self._session.add(new_user)
        await self._session.flush()

        return User(
            id=new_user.id,
            first_name=new_user.first_name,
            last_name=new_user.last_name,
            date_of_birth=new_user.date_of_birth,
            gender=new_user.gender,
            email=new_user.email,
            is_active=new_user.is_active,
            join_time=new_user.join_time,
        )
