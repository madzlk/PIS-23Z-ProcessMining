from sqlalchemy.orm import Session
from datetime import datetime
import models, schemas


""" USERS """

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User( username=user.username,
        email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db: Session, user_uid: str):
    return db.query(models.User).filter(models.User.user_uid == user_uid).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

def delete_user(db: Session, user: models.User):
    db.delete(user)
    db.commit()
    return user