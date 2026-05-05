# from pydantic import Field
# from pydantic_settings import BaseSettings, SettingsConfigDict


# class Settings(BaseSettings):
#     model_config = SettingsConfigDict(
#         env_file=".env",
#         env_file_encoding="utf-8",
#         extra="ignore",
#     )

#     app_env: str = Field(default="development", alias="APP_ENV")
#     openai_api_key: str | None = Field(default=None, alias="OPENAI_API_KEY")
#     openai_model: str = Field(default="gpt-4o-mini", alias="OPENAI_MODEL")
#     database_url: str | None = Field(default=None, alias="DATABASE_URL")
#     redis_url: str | None = Field(default=None, alias="REDIS_URL")

#     request_timeout_seconds: float = 12.0
#     stream_ping_seconds: int = 15


# settings = Settings()












import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    openai_api_key: str | None = os.getenv("OPENAI_API_KEY")
    openai_model: str = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
    app_env: str = os.getenv("APP_ENV", "development")
    database_url: str | None = os.getenv("DATABASE_URL")
    pgvector_database_url: str | None = os.getenv("PGVECTOR_DATABASE_URL")
    redis_url: str | None = os.getenv("REDIS_URL")


settings = Settings()