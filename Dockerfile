FROM python:3.9-slim

WORKDIR /app

COPY src/main.py .

RUN pip install flask

ENV APP_VERSION=v1

CMD ["python", "main.py"]
