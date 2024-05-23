FROM python:3.11.2
ENV PYTHONUNBUFFERED 1
RUN mkdir /app

WORKDIR /app
# Install system dependencies
RUN apt-get update \
    && apt-get install -y default-libmysqlclient-dev gcc \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/

# Install Python dependencies
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt
COPY . /app/
RUN python -m pip install psycopg2
