FROM python:3.9.2
COPY . /app
WORKDIR /app

CMD python ./main.py