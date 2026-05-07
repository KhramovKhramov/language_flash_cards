from src.application.dto.user import UserCreateCommand
from src.domain.entities.user import User
from src.domain.interfaces.uow import IUnitOfWork


class UserCreateUseCase:
    """Creating new user."""

    def __init__(self, uow: IUnitOfWork) -> None:
        self._uow = uow

    async def execute(self, data: UserCreateCommand) -> User:
        user = User(
            first_name=data.first_name,
            last_name=data.last_name,
            date_of_birth=data.date_of_birth,
            gender=data.gender,
            email=data.email,
        )

        async with self._uow as uow:
            added_user = await uow.users.add(user)

            await uow.commit()

        return added_user
