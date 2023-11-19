from pydantic import BaseModel


class UserData(BaseModel):
    username: str


class UserCreate(UserData):
    user_uid: str
    email: str

class User(UserCreate):

    class Config:
        orm_mode = True
