from dataclasses import dataclass

from durov.app.dto.base import BaseDTO


@dataclass
class UserCreationParamsDTO(BaseDTO):
    first_name: str
    last_name: str
    nickname: str


@dataclass
class UserRegisterParamsDTO(BaseDTO):
    first_name: str
    last_name: str
    nickname: str
