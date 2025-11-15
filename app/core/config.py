from functools import lru_cache

from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    """Application configuration values loaded from environment variables."""

    app_name: str = "Tableros API"
    environment: str = Field(default="development", alias="ENVIRONMENT")
    database_url: str = Field(default="sqlite:///./tableros.db", alias="DATABASE_URL")
    echo_sql: bool = Field(default=False, alias="ECHO_SQL")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False


@lru_cache
def get_settings() -> Settings:
    """Return a cached Settings instance to avoid repeated environment parsing."""

    return Settings()


settings = get_settings()
