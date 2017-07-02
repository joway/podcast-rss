FROM python:3.6.1-slim

MAINTAINER joway wang <joway@gmail.com>
ENV TZ Asia/Shanghai

RUN apt update \
    && apt install -y build-essential \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir /code && mkdir /code/cache
WORKDIR /code

COPY ./requirementsx.txt /code/
RUN pip install -r ./requirementsx.txt

COPY . /code

EXPOSE 8000
VOLUME /code/cache

ENTRYPOINT ./entrypoint.sh
