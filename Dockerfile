FROM python:3.11-slim

# Install system dependencies required by mysqlclient and other build tools
RUN apt-get update && apt-get install -y \
    build-essential \
    default-libmysqlclient-dev \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

COPY . /app/

CMD ["gunicorn", "carproject.wsgi:application", "--bind", "0.0.0.0:8000"]
