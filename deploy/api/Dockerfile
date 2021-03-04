FROM python:3.7

ADD entrypoint.sh /entrypoint.sh
ADD requirements.txt /requirements.txt
ADD .aws /.aws
ADD src /api
RUN apt-get update
RUN apt-get -y install ansible
RUN pip install --upgrade pip setuptools
RUN pip install -r requirements.txt

WORKDIR /api

CMD /entrypoint.sh
