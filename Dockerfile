# syntax=docker/dockerfile:1

FROM python:3.13-slim

WORKDIR /KDS-Consulting

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 5000

CMD [ "python3", "main.py"]