FROM debian:stable-slim

RUN apt update
RUN apt install -y python3

COPY main.py main.py
COPY books/ books/
CMD ["python3", "main.py"]