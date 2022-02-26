#ubuntu-python3
FROM ubuntu:latest
MAINTAINER Jiage "liujiage@yahoo.com"
#ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update \
  && apt-get install -y python3-pip python3-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip \
  && apt-get install -y sshpass \
  && apt-get install -y vim \
  && apt-get install -y sqlite3

WORKDIR /opt/services

#devops-web
FROM ubuntu-python3:latest
MAINTAINER Jiage "liujiage@yahoo.com"
#ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update
COPY ./requirements.txt /tmp/requirements.txt
RUN pip3 install -qr /tmp/requirements.txt

WORKDIR /opt/services
EXPOSE 5000
CMD ["flask", "run"]



RUN apt-get update
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y -q python-all python-pip
ADD ./webapp/requirements.txt /tmp/requirements.txt
RUN pip install -qr /tmp/requirements.txt
ADD ./webapp /opt/webapp/
WORKDIR /opt/webapp
EXPOSE 5000
CMD ["python", "app.py"]