from src.application.dto.user import UserCreateCommand
from src.domain.entities.user import User
from src.domain.interfaces.repositories.user import IUserRepository


class UserCreateUseCase:
    """Creating new user."""

    def __init__(self, repo: IUserRepository) -> None:
        self._repo = repo

    async def execute(self, data: UserCreateCommand) -> User:
        user = User(
            first_name=data.first_name,
            last_name=data.last_name,
            date_of_birth=data.date_of_birth,
            gender=data.gender,
            email=data.email,
        )

        return await self._repo.add(user)
