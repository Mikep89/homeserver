from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from typing import Optional

app = FastAPI()

@app.get('/')
async def read_root():
    return jsonable_encoder({"hello": "world"})

@app.get('/users')
async def get_users():
    from app.model import Base,User,engine
    from sqlalchemy.orm.session import Session

    session = Session(bind=engine)
    return jsonable_encoder(session.query(User).all())



if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=5000)