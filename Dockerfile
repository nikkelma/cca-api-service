FROM python:3.7
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install postgres build dependencies
RUN set -ex \
    && BUILD_DEPS=" \
    build-essential \
    libpcre3-dev \
    libpq-dev \
    " \
    && apt-get update && apt-get install -y --no-install-recommends $BUILD_DEPS

# Install pipenv
RUN pip install pipenv

# Copy installation files to working directory
COPY Pipfile* /app/

# Build project
RUN pipenv install --deploy --system

# Install postgres specific packages
RUN pipenv install --system psycopg2

# Copy the remaining project files into the container
COPY . .

# Run server
CMD python manage.py runserver