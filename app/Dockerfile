FROM python:3.12-alpine AS builder

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt -t /opt/venv

FROM python:3.12-alpine

RUN adduser -S www
USER www

WORKDIR /app

COPY --from=builder /opt/venv /usr/local/lib/python3.12/site-packages

COPY . .

ENTRYPOINT ["python3"]
CMD ["/app/app.py"]