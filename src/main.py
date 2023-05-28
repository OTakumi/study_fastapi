from typing import Union
from fastapi import FastAPI

import datetime

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/now")
def read_datetime_now():
    dt_now = datetime.datetime.now()
    return {"data": dt_now}
