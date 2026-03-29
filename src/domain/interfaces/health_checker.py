from dataclasses import dataclass
from typing import Protocol

from src.domain.enums import SystemComponent


@dataclass
class ComponentHealthStatus:
    component_name: SystemComponent
    is_healthy: bool
    error_msg: str | None = None


class IComponentHealthChecker(Protocol):
    async def check(self) -> ComponentHealthStatus:
        """Checking the status of a system component."""
        ...
