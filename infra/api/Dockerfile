FROM python:3.7

ADD entrypoint.sh /entrypoint.sh
ADD requirements.txt /requirements.txt
RUN apt-get update
RUN apt-get -y install ansible
RUN pip install --upgrade pip setuptools
RUN pip install -r requirements.txt

RUN mkdir api

WORKDIR /api

