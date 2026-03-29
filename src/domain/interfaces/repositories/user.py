from typing import Protocol

from src.domain.entities.user import User


class IUserRepository(Protocol):
    """User repository interface."""

    async def add(self, data: User) -> User: ...
