FROM python:3.9.0-alpine

RUN mkdir app

WORKDIR /app

ADD app/requirements.txt /app


RUN pip install --upgrade pip setuptools && \
pip install -r requirements.txt