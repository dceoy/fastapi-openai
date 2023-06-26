#!/usr/bin/env python

from sqlalchemy import Column, Float, JSON, Integer, String

from .database import DbBase


class Completion(DbBase):
    __tablename__ = 'completion'

    id = Column(Integer, primary_key=True)
    completion_model = Column(String)
    completion_prompt = Column(String)
    completion_temperature = Column(Float)
    completion_result = Column(JSON)
