FROM python:3.7

ADD entrypoint.sh /entrypoint.sh
ADD requirements.txt /requirements.txt

RUN pip install -r requirements.txt

RUN mkdir api

WORKDIR /api

RUN pip install --upgrade pip setuptools