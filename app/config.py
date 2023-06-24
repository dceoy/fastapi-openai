#!/usr/bin/env python

from functools import lru_cache

import openai
from pydantic import BaseSettings


class Settings(BaseSettings):
    openai_api_key: str

    class Config:
        env_file = '.env'


@lru_cache()
def read_settings():
    settings = Settings()
    openai.api_key = settings.openai_api_key
    return settings
