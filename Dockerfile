FROM python:3.7
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install pipenv
RUN pip install pipenv

# Copy installation files to working directory
COPY Pipfile* /app/

# Build project
RUN pipenv install --deploy --system

# Copy the remaining project files into the container
COPY . .

# Run server
CMD python manage.py runserver