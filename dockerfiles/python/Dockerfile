# syntax=docker/dockerfile:1
FROM python:3.11-alpine

WORKDIR /app

COPY requirements.txt requirements.txt

RUN set -eux \
    && apk add --no-cache build-base \
    && apk add --no-cache postgresql-libs \
    && apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev \
    && pip install --no-cache-dir --upgrade -r requirements.txt \
    && apk del build-base
    
EXPOSE 5000

COPY . ./app
