from collections.abc import Iterable

from dishka import Provider, Scope, provide

from src.application.use_cases.health.health_check import HealthCheckUseCase
from src.application.use_cases.user.user_create import UserCreateUseCase
from src.domain.interfaces.health_checker import IComponentHealthChecker
from src.domain.interfaces.repositories.user import IUserRepository


class UseCasesProvider(Provider):
    """DI provider of usecases."""

    scope = Scope.REQUEST

    # Health

    @provide
    def get_health_use_case(
        self, checkers: Iterable[IComponentHealthChecker]
    ) -> HealthCheckUseCase:
        return HealthCheckUseCase(checkers)

    # User

    @provide
    def get_user_create_use_case(
        self, repo: IUserRepository
    ) -> UserCreateUseCase:
        return UserCreateUseCase(repo=repo)
