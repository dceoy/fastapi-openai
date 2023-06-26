#!/usr/bin/env python

from sqlalchemy.orm import Session

from .models import Completion
from .schemas import CompletionCreate


def create_completion(db_session: Session, completion: CompletionCreate):
    completion = Completion(**completion.dict())
    db_session.add(completion)
    db_session.commit()
    db_session.refresh(completion)
    return completion


def get_completions(db_session: Session, skip: int = 0, limit: int = 100):
    return db_session.query(Completion).offset(skip).limit(limit).all()
