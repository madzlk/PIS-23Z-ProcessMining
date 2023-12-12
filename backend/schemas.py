from pydantic import BaseModel

class UserData(BaseModel):
    username: str

class UserCreate(UserData):
    email: str

class User(UserCreate):
    user_uid: int

    class Config:
        orm_mode = True
