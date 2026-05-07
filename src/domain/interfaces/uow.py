from typing import Protocol

from src.domain.interfaces.repositories.user import IUserRepository


class IUnitOfWork(Protocol):
    """Unit of Work interface."""

    users: IUserRepository

    async def __aenter__(self) -> "IUnitOfWork": ...

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None: ...

    async def commit(self) -> None: ...

    async def rollback(self) -> None: ...
