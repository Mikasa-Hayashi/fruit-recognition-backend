from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABAE_URL: str
    MODEL_PATH: str

    class Config:
        env_file = '.env'
        

settings = Settings()