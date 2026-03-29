from pydantic import BaseModel, ConfigDict, Field

from src.domain.enums import SystemComponent


class ComponentStatus(BaseModel):
    """System component status schema."""

    component_name: SystemComponent = Field(
        description="System component name"
    )
    is_healthy: bool = Field(description="System component health status")
    error_msg: str | None = Field(
        default=None, description="Error description message"
    )


class HealthCheckResponseSchema(BaseModel):
    """Healthcheck response schema."""

    model_config = ConfigDict(from_attributes=True)

    is_healthy: bool = Field(description="System health status")
    components_statuses: list[ComponentStatus]
