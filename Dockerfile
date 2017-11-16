FROM python:2

RUN apt-get -y update && \
    apt-get -y install python3-setuptools && \
	apt-get -y clean

RUN pip install coverage
