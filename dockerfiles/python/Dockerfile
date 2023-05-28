# syntax=docker/dockerfile:1
FROM python:3.11-alpine

WORKDIR /code

COPY requirements.txt requirements.txt

RUN set -eux \
    && apk add --no-cache build-base \
    && pip install --upgrade pip setuptools wheel \
    && pip install --no-cache-dir --upgrade -r requirements.txt \
    && pip install uvicorn[standard] \
    && apk del build-base
    
EXPOSE 5000

COPY . ./code
