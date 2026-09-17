"""Application configuration loaded from environment variables."""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Runtime settings shared by the API and security dependencies."""

    app_name: str = "RepoMind Fixture API"
    api_key: str = "local-development-key"
    debug: bool = False
    order_tax_rate: float = 0.10

    model_config = SettingsConfigDict(env_prefix="", extra="ignore")


settings = Settings()
