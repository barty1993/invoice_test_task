from pydantic import PostgresDsn
from pydantic_settings import BaseSettings


class Config(BaseSettings):
    class Config:
        env_file = ".env"

    POSTGRES_DSN = PostgresDsn
