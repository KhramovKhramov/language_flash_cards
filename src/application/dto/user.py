from dataclasses import dataclass
from datetime import date

from src.domain.enums import Gender


@dataclass
class UserCreateCommand:
    first_name: str
    date_of_birth: date
    gender: Gender
    email: str

    last_name: str | None = None
