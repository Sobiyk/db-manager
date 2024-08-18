from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    tnt_host: str = '0.0.0.0'
    tnt_port: str = '1234'

    class Config:
        env_file = '.env'


settings = Settings()
