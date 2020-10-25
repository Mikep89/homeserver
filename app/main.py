from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from typing import Optional

app = FastAPI()

@app.get('/')
async def read_root():
    return jsonable_encoder({"hello": "world"})

@app.get('/item/{item_id}')
async def read_item(item_id: int, q: Optional[str] = None):
    return jsonable_encoder({"item_id": item_id, 'q':q})