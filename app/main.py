from typing import Union
from fastapi import FastAPI
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String

import datetime
from api import api_router

app = FastAPI()

# DBの情報は環境変数から取得する
engine = create_engine("postgresql://" \
        + 'POSTGRES_USER' \
        + ":" \
        + 'POSTGRES_PASSWORD' \
        + "@localhost/db")

Base = declarative_base()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/now")
def read_datetime_now():
    dt_now = datetime.datetime.now()
    return {"data": dt_now}

@app.get("/info")
def read_info():
    sqlalchemy_version = sqlalchemy.__version__

    return {"sqlalchemy": sqlalchemy_version}
