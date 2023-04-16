FROM python:3.9-buster

# package
RUN apt update -y && \
    apt upgrade -y && \
    apt install -y git 
RUN pip install --upgrade pip && \
    pip install poetry

# poetry
# COPY ./start.sh ./start.sh
# RUN sh start.sh

WORKDIR /src
