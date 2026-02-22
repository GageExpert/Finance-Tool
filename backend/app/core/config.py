from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Axium API"
    database_url: str = "postgresql+psycopg2://axium:axium@localhost:5432/axium"
    redis_url: str = "redis://localhost:6379/0"
    secret_key: str = "change-me"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 60
    sec_user_agent: str = "AxiumResearch/0.1 (contact: dev@axium.local)"
    demo_mode: bool = True

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()
