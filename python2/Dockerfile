FROM python:3.13-alpine

WORKDIR /app

LABEL MAINTAINER="sksupremeboss"

COPY app.py/ app/
COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD [" python", "app.py"]
