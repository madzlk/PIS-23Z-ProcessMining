from sqlalchemy.orm import Session
from datetime import datetime

from . import models, schemas


""" USERS """


def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(
        user_uid=user.user_uid, username=user.username,
        email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()