# pull official base image
FROM python:3.8-slim-buster

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN apt-get update 
RUN pip install --upgrade pip setuptools wheel

# copy requirements file
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r /usr/src/app/requirements.txt \
    && rm -rf /root/.cache/pip

# copy requirements file
COPY ./requirements_prod.txt /usr/src/app/requirements_prod.txt
RUN pip install -r /usr/src/app/requirements_prod.txt \
    && rm -rf /root/.cache/pip

# copy project
COPY . /usr/src/app/



