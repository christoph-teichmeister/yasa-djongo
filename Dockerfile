FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get -y upgrade

WORKDIR /app

ADD Pipfile Pipfile.lock /app/

RUN pip install --upgrade pip
RUN pip install -U pip pipenv

RUN pipenv install --system --deploy

COPY ./ /app/