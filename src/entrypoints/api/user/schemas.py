from datetime import date, datetime

from pydantic import (
    BaseModel,
    ConfigDict,
    EmailStr,
    Field,
)

from src.domain.enums import Gender


class UserBaseSchema(BaseModel):
    """Base user data schema."""

    first_name: str = Field(description="Имя", max_length=50)
    last_name: str | None = Field(
        default=None, description="Фамилия", max_length=50
    )
    date_of_birth: date = Field(description="Дата рождения")
    gender: Gender = Field(description="Пол")
    email: EmailStr = Field(description="Email", max_length=50)


class UserCreateRequestSchema(UserBaseSchema):
    """User's create request schema."""


class UserResponseSchema(UserBaseSchema):
    """User's base response schema."""

    model_config = ConfigDict(from_attributes=True)

    id: int = Field(
        description="Идентификатор",
        examples=[1],
    )
    is_active: bool = Field(description="Активен", examples=[True, False])
    join_time: datetime = Field(description="Дата регистрации")
