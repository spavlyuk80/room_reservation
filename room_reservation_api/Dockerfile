FROM python:3.8.3-alpine

WORKDIR /usr/src/app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . .
RUN pip install pipenv
RUN pipenv install --system
