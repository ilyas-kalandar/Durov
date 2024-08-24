from datetime import datetime
from typing import List, Self

from sqlalchemy import (
    Column,
    Connection,
    DateTime,
    Enum,
    Integer,
    String,
    Text,
    Boolean,
    ForeignKey,
    Float,
    event,
)
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped


class BaseModel(DeclarativeBase):
    """Base for all models"""

    id: Mapped[int] = mapped_column(
        Integer,
        autoincrement=True,
        primary_key=True,
    )

    first_name: Mapped[str] = mapped_column(
        String(length=255),
        nullable=False,
    )
    last_name: Mapped[str] = mapped_column(
        String(length=255),
        nullable=False,
    )
    nickname: Mapped[str] = mapped_column(
        String(length=25),
        nullable=False,
    )
