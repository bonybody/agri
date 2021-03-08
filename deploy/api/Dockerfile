FROM python:3.7

ADD entrypoint.sh /entrypoint.sh
ADD .aws /root/.aws
ADD src /api
WORKDIR /api
RUN apt-get update
RUN apt-get -y install ansible
ADD requirements.txt /requirements.txt
RUN pip install --upgrade pip setuptools
RUN pip install -r /requirements.txt
CMD /entrypoint.sh
