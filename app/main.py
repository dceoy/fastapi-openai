#!/usr/bin/env python

from fastapi import Depends, FastAPI
from typing_extensions import Annotated

from .config import Settings, read_settings

app = FastAPI()


@app.get('/')
async def root():
    return {'message': 'Hello World'}


# @app.get('/info')
# async def info(settings: Annotated[Settings, Depends(read_settings)]):
#     return {'openai_api_key': settings.openai_api_key}
