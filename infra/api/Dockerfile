FROM python:3.8.7-buster

RUN mkdir app

WORKDIR /app

ADD ./requirements.txt /app

RUN pip install --upgrade pip setuptools && \
pip install -r requirements.txt