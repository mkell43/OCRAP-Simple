FROM python:3.8.2-alpine

COPY . .

RUN ["pip", "install", "-r", "requirements.txt"]

ENTRYPOINT [ "python", "ocrap-simple.py" ]