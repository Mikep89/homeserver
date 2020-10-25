from typing import List, Optional
from pydantic import BaseModel
import datetime

class UserBase(BaseModel):
    name: str
    email: str
    dateCreated: datetime.datetime

class UserCreate(UserBase):
    password:str

class RenewApiKey(UserBase):
    apiKey: str
    apiExpiry: datetime.datetime

    class Config:
        orm_mode= True

class User(UserBase):
    id: int
    apiKey: str
    apiExpiry: datetime.datetime

    class Config:
        orm_mode= True
    