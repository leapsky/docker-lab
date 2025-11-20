FROM python:3.12-alpine

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

RUN adduser -S www

USER www

ENTRYPOINT [ "python3" ]

CMD [ "app2.py" ]
