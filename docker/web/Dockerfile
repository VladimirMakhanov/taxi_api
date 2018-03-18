FROM python:3.6.3

RUN apt-get update -qq

RUN apt-get -y install python3-dev libpq-dev
COPY requirements.txt .
RUN pip3 install -r requirements.txt
