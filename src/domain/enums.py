from enum import StrEnum, auto


class SystemComponent(StrEnum):
    """System component type.."""

    POSTGRES = auto()


class Gender(StrEnum):
    """User gender type."""

    MALE = auto()
    FEMALE = auto()
