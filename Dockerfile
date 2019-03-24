FROM python:3.7-alpine3.8

RUN mkdir /app
WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

ENTRYPOINT gunicorn -w 4 -b:8000 --access-logfile - app:app
