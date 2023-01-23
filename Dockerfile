FROM python:3.11.0-alpine

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk del build-deps

WORKDIR /app

ADD Pipfile Pipfile.lock /app/

RUN pip install --upgrade pip
RUN pip install -U pip pipenv

RUN pipenv install --system --deploy

COPY . /app/