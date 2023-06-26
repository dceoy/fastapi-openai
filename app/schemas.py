#!/usr/bin/env python

from pydantic import BaseModel


class CompletionBase(BaseModel):
    completion_model: str
    completion_prompt: str
    completion_temperature: float
    completion_result: dict


class CompletionCreate(CompletionBase):
    pass


class Completion(CompletionBase):
    id: int

    class Config:
        orm_mode = True
