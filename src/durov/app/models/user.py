from dataclasses import dataclass

from durov.app.models.base import BaseModel


@dataclass
class User(BaseModel):
    id: int
    first_name: str
    last_name: str
