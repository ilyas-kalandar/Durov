from sqlalchemy import (
    Integer,
    String,
)
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped

from durov.app.models.user import User as UserModel


class BaseModel(DeclarativeBase):
    """Base for all models"""


class User(BaseModel):
    """User's model"""

    __tablename__ = "users"

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
        unique=True,
    )

    def to_domain(self) -> UserModel:
        return UserModel(
            id=self.id,
            nickname=self.nickname,
            first_name=self.first_name,
            last_name=self.last_name,
        )
