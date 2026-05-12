from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from src.domain.enums import SystemComponent
from src.domain.interfaces.health_checker import ComponentHealthStatus


class PostgresHealthChecker:
    def __init__(self, session_factory: async_sessionmaker[AsyncSession]):
        self._session_factory = session_factory

    async def check(self) -> ComponentHealthStatus:
        """Checking the PostgreSQL status."""
        try:
            async with self._session_factory() as session:
                await session.execute(text("SELECT 1"))
            return ComponentHealthStatus(
                component_name=SystemComponent.POSTGRES, is_healthy=True
            )
        except Exception as e:
            return ComponentHealthStatus(
                component_name=SystemComponent.POSTGRES,
                is_healthy=False,
                error_msg=str(e),
            )
