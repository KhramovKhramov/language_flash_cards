from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database import Base


class IdMixin:
    id: Mapped[int] = mapped_column('id', primary_key=True, autoincrement=True)


class Card(Base, IdMixin):
    __tablename__ = 'cards'

    front_side: Mapped[str] = mapped_column(String(64))
    back_side: Mapped[str] = mapped_column(String(64))
    pack_id: Mapped[int] = mapped_column(ForeignKey('packs.id'))
    pack: Mapped['Pack'] = relationship(back_populates='cards')


class Pack(Base, IdMixin):
    __tablename__ = 'packs'

    title: Mapped[str] = mapped_column(String(32))
    description: Mapped[str] = mapped_column(String(256), nullable=True)
    cards: Mapped[list['Card']] = relationship(back_populates='pack')
