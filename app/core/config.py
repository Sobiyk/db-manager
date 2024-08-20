from pydantic import ConfigDict
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    model_config = ConfigDict(env_file='.env')

    tnt_host: str = '0.0.0.0'
    tnt_port: str = '1234'


settings = Settings()
