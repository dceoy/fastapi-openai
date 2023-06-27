#!/usr/bin/env python

from datetime import datetime

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
    timestamp: datetime

    class Config:
        orm_mode = True
