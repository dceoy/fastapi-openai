#!/usr/bin/env python

from functools import lru_cache

import openai
from pydantic import BaseSettings


class Settings(BaseSettings):
    openai_api_key: str
    openai_completion_model_id: str
    openai_completion_temperature: float = 0.7
    postgres_host: str = 'localhost'
    postgres_port: int = 5432
    postgres_db: str = 'openai'
    postgres_user: str
    postgres_password: str

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


@lru_cache()
def read_settings():
    settings = Settings()
    openai.api_key = settings.openai_api_key
    return settings
