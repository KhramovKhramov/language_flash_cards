from dataclasses import dataclass, field
from datetime import UTC, date, datetime

from src.domain.enums import Gender


@dataclass
class User:
    first_name: str
    date_of_birth: date
    gender: Gender
    email: str
    is_active: bool = True
    join_time: datetime = field(default_factory=lambda: datetime.now(UTC))

    id: int | None = None
    last_name: str | None = None
