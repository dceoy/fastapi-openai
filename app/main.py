#!/usr/bin/env python

import openai
from fastapi import Depends, FastAPI
from typing_extensions import Annotated

from .config import Settings, read_settings

app = FastAPI()


@app.get('/')
def root():
    return {'message': 'Hello World'}


@app.post('/')
def generate_animal_names(
        animal: str, settings: Annotated[Settings, Depends(read_settings)]
):
    return openai.Completion.create(
        model='text-davinci-003', prompt=_generate_prompt(animal),
        temperature=0.6
    )


def _generate_prompt(animal):
    return f'''Suggest three names for an animal that is a superhero.

Animal: Cat
Names: Captain Sharpclaw, Agent Fluffball, The Incredible Feline
Animal: Dog
Names: Ruff the Protector, Wonder Canine, Sir Barks-a-Lot
Animal: {animal.capitalize()}
Names:'''
