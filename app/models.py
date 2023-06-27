#!/usr/bin/env python

from sqlalchemy import JSON, Column, DateTime, Float, Integer, String, func

from .database import DbBase


class Completion(DbBase):
    __tablename__ = 'completion'

    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime(timezone=True), default=func.now())
    completion_model = Column(String)
    completion_prompt = Column(String)
    completion_temperature = Column(Float)
    completion_result = Column(JSON)
