from datetime import date, datetime

from sqlalchemy import Boolean, Date, DateTime, Enum, String, true
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql.functions import now

from src.domain.enums import Gender
from src.infra.postgres.models.base import Base


class UserORM(Base):
    """User SQLAlchemy DB model."""

    __tablename__ = "users"

    # User data
    first_name: Mapped[str] = mapped_column(
        String(50), comment="User's first name"
    )
    last_name: Mapped[str | None] = mapped_column(
        String(50), comment="User's last name"
    )
    date_of_birth: Mapped[date] = mapped_column(
        Date(), comment="User's date of birth"
    )
    gender: Mapped[Gender] = mapped_column(
        Enum(Gender), comment="User's gender type"
    )

    # Contacts
    email: Mapped[str] = mapped_column(
        String(50), unique=True, index=True, comment="Email"
    )

    # Core data
    is_active: Mapped[bool] = mapped_column(
        Boolean(), server_default=true(), comment="User's activity status"
    )
    join_time: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=now(),
        comment="Registration date and time",
    )
