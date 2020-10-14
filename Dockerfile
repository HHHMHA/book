# Pull base image
FROM python:3.8

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Project Env
ENV DJANGO_PROJECT_NAME "Book Store"
ENV DJANGO_PROJECT_ROOT /code
ENV DJANGO_LOGSTASH_HOST localhost
ENV DJANGO_LOGSTASH_PORT 8001
ENV DJANGO_ADMIN_URL kiddos
ENV DJANGO_SECRET_KEY My_SUPER_555_DEV_SECRETE_KEY
ENV ENABLE_APM 0

# Set work directory
WORKDIR /code/book

# Install dependencies
COPY Pipfile Pipfile.lock /code/
RUN pip install pipenv && pipenv install --system

# Copy project
COPY . /code/