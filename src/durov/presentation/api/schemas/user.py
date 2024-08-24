from pydantic import Field

from durov.app.dto.user import UserRegisterParamsDTO
from durov.presentation.api.schemas.base import BaseModel


class UserRegisteringRequest(BaseModel):
    first_name: str = Field(
        title="First name", description="Name of user", examples=["Pavel"]
    )
    last_name: str = Field(
        title="Last name", description="Last name of user", examples=["Durov"]
    )
    nickname: str = Field(
        title="Nick",
        description="Nick",
        examples=["durov"],
    )

    def to_dto(self) -> UserRegisterParamsDTO:
        return UserRegisterParamsDTO(
            first_name=self.first_name,
            last_name=self.last_name,
            nickname=self.nickname,
        )


class User(BaseModel):
    id: int = Field(
        title="ID",
        description="Id of user",
        examples=[1],
    )
    first_name: str = Field(
        title="First name", description="Name of user", examples=["Pavel"]
    )
    last_name: str = Field(
        title="Last name", description="Last name of user", examples=["Durov"]
    )
    nickname: str = Field(
        title="Nick",
        description="Nick",
        examples=["durov"],
    )
