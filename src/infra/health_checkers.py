from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from src.domain.enums import SystemComponent
from src.domain.interfaces.health_checker import ComponentHealthStatus


class PostgresHealthChecker:
    def __init__(self, session: AsyncSession):
        self._session = session

    async def check(self) -> ComponentHealthStatus:
        """Checking the PostgreSQL status."""
        try:
            await self._session.execute(text("SELECT 1"))
            return ComponentHealthStatus(
                component_name=SystemComponent.POSTGRES, is_healthy=True
            )
        except Exception as e:
            return ComponentHealthStatus(
                component_name=SystemComponent.POSTGRES,
                is_healthy=False,
                error_msg=str(e),
            )
