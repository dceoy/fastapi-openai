#!/usr/bin/env python

from sqlalchemy.orm import Session

from .models import Completion
from .schemas import CompletionCreate


def create_completion(db_session: Session, completion: CompletionCreate):
    db_session_completion = Completion(**completion.dict())
    db_session.add(db_session_completion)
    db_session.commit()
    db_session.refresh(db_session_completion)
    return db_session_completion
