from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str
    MODEL_PATH: str
    TRUSTED_TOKEN: str

    class Config:
        env_file = '.env'


settings = Settings()