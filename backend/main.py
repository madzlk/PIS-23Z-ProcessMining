from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from backend import crud, models, database, schemas

database.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

# Dependency to get the database session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create a user
@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)

# Get all users
@app.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_users(db, skip=skip, limit=limit)

# Get a specific user by user_uid
@app.get("/users/{user_uid}", response_model=schemas.User)
def read_user(user_uid: str, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_uid=user_uid)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
