from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings


class DbConfig(BaseModel):
    name: str = Field(alias="DUROV_DB_NAME")
    user: str = Field(alias="DUROV_DB_USER")
    password: str = Field(alias="DUROV_DB_PASS")


class Config(BaseSettings):
    db: DbConfig
