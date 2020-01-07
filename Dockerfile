FROM python:3.7
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create a group and user to run our app
ARG APP_USER=appuser
RUN groupadd -r ${APP_USER} && useradd --no-log-init -r -g ${APP_USER} ${APP_USER}

# Run initial contain installation commands
RUN apt-get update && \
    apt-get install -y && \
    apt-get install -y apt-utils

# Install uwsgi to serve django
RUN pip3 install uwsgi

# Install postgres build dependencies
RUN set -ex \
    && BUILD_DEPS=" \
    build-essential \
    libpcre3-dev \
    libpq-dev \
    " \
    && apt-get update && apt-get install -y --no-install-recommends $BUILD_DEPS

# Install postgres specific packages
RUN pip3 install psycopg2

# Install pipenv
RUN pip install pipenv

# Copy installation files to working directory
COPY Pipfile* /app/

# Build project
RUN pipenv install --deploy --system

# Copy the remaining project files into the container
COPY . .

# Generate static files
RUN DATABASE_URL='' python manage.py collectstatic --noinput

# Change to a non-root user
USER ${APP_USER}:${APP_USER}

# Run server
EXPOSE 8000
CMD /bin/bash -c '\
        python3 manage.py migrate && \
        uwsgi --ini uwsgi.ini --show-config \
    '