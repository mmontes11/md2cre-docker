FROM python:3.9-slim

WORKDIR /usr/src/app

COPY convert.py /usr/src/app/convert.py

ENTRYPOINT ["python3", "/usr/src/app/convert.py"]
