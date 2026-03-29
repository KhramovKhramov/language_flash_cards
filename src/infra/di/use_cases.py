from collections.abc import Iterable

from dishka import Provider, Scope, provide

from src.application.use_cases.health.health_check import HealthCheckUseCase
from src.domain.interfaces.health_checker import IComponentHealthChecker


class UseCasesProvider(Provider):
    """Провайдер юзкейсов приложения."""

    scope = Scope.REQUEST

    # Health

    @provide
    def get_health_use_case(
        self, checkers: Iterable[IComponentHealthChecker]
    ) -> HealthCheckUseCase:
        return HealthCheckUseCase(checkers)
