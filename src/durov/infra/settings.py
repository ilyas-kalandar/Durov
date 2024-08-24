from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Database settings
    db_url: str = Field(alias="DB_URL")

    # Logging settings
    logging_level: str = Field(alias="LOGGING_LVL")
    logging_format: str = Field(alias="LOGGING_FORMAT")

    # Serving settings
    serving_host: str = Field(env="SERVING_HOST")
    serving_port: int = Field(env="SERVING_PORT")

    model_config = SettingsConfigDict(env_file=".env", env_prefix="DUROV_")


def load_settings() -> Settings:
    """Loads configuration from .env | os.getenv"""
    return Settings()
