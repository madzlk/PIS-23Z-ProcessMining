from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import crud, models, database, schemas
from fastapi.middleware.cors import CORSMiddleware
database.Base.metadata.create_all(bind=database.engine)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with the specific origin of your frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency to get the database session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

#default
@app.get("/")
def home():
    return {"message": "First FastAPI app"}

# Create a user
@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)

# Get all users
@app.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users

# Get a specific user by user_uid
@app.get("/users/{user_uid}", response_model=schemas.User)
def read_user(user_uid: str, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_uid=user_uid)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

# Delete a user by user_uid
@app.delete("/users/{user_uid}", response_model=schemas.User)
def delete_user(user_uid: str, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_uid=user_uid)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return crud.delete_user(db=db, user=db_user)
