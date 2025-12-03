from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASSWORD: str
    DB_NAME: str

    model_config = SettingsConfigDict(env_file=".env")


config = Config()


