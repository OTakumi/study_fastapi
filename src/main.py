from typing import Union
from fastapi import FastAPI
import sqlalchemy

import datetime
from dotenv import load_dotenv

app = FastAPI()
load_dotenv()
engine = sqlalchemy.create_engine("postgresql://" \
        + 'POSTGRES_USER' \
        + ":" \
        + 'POSTGRES_PASSWORD' \
        + "@localhost/db")

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

@app.get("/info")
def read_info():
    sqlalchemy_version = sqlalchemy.__version__

    return {"sqlalchemy": sqlalchemy_version}
