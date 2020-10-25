from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from typing import Optional
from sqlalchemy.orm.session import Session


from app.schema import *
from app.model import Base,User,engine


session = Session(bind=engine)


app = FastAPI()

@app.get('/')
async def read_root():
    return jsonable_encoder({"hello": "world"})

@app.get('/userlist')
async def get_users():
    from app.model import Base,User,engine
    from sqlalchemy.orm.session import Session

    session = Session(bind=engine)
    return jsonable_encoder(session.query(User).all())

@app.get('/user/{user_id}')
async def get_user(user_id:int):
    return jsonable_encoder(session.query(User).filter(User.id == user_id).first())

@app.post("/user/add")
async def create_user(db:session, user = schema.UserCreate):
    hash = 
    
    return user


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=5000)