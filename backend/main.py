from fastapi import FastAPI, Depends, HTTPException, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from bson import ObjectId
from gridfs import GridFS

from sqlalchemy.orm import Session
import crud, models, database, schemas, stats
import mongodb_conn



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

def get_mongo_db():
    client = mongodb_conn.get_new_mongo_client()
    yield client[mongodb_conn.mongo_db]
    client.close()


#default
@app.get("/")
async def home():
    return {"message": "First FastAPI app"}

# Create a user
@app.post("/users/", response_model=schemas.User)
async def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)

# Get all users
@app.get("/users/", response_model=list[schemas.User])
async def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users

# Get a specific user by user_uid
@app.get("/users/{user_uid}", response_model=schemas.User)
async def read_user(user_uid: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_uid=user_uid)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

# Delete a user by user_uid
@app.delete("/users/{user_uid}", response_model=schemas.User)
async def delete_user(user_uid: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_uid=user_uid)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return crud.delete_user(db=db, user=db_user)

@app.post("/files/{user_uid}")
async def upload_file(user_uid: int, file: UploadFile = File(...), db = Depends(get_mongo_db)):
    fs = GridFS(db, collection=f"user_files_{user_uid}")
    with fs.new_file(filename=file.filename) as f:
        f.write(file.file.read())
    return {"filename": file.filename}

# Get all files descriptors from a specific user
@app.get("/files/{user_uid}", response_model=list[schemas.UserFile])
async def read_files_of_a_user(user_uid: int, db: Session = Depends(get_mongo_db)):
    collection_name = f"user_files_{user_uid}.files"
    collection = db[collection_name]

    user_files = []
    for file in collection.find():
        user_files.append(schemas.UserFile(**file)) # ** just unpacks file dict into UserFile constructor

    if not user_files:
        raise HTTPException(status_code=404, detail=f"No files found for user {user_uid}")

    return user_files

@app.get("/files/{user_uid}/{file_id}/statistics")
async def get_file_statistics(user_uid: int, file_uid: str, db: Session = Depends(get_mongo_db)):
    fs = GridFS(db, collection=f"user_files_{user_uid}")

    file_object = fs.find_one({'_id': ObjectId(file_uid)})
    if file_object:
        statistics = stats.create_stats_json_string_from_(file_object)
        return statistics
    else:
        raise HTTPException(status_code=404, detail=f"File not found")


