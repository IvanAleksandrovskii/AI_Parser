import os
from pydantic_settings import BaseSettings


class ChromeConfig:
    path: str = os.path.abspath("/usr/local/bin/chromedriver")  # Updated path


class Settings(BaseSettings):
    chrome: ChromeConfig = ChromeConfig()


settings = Settings()
