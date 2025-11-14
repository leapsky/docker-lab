FROM python:3.12-alpine

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

RUN adduser -S www

USER www

ENTRYPOINT [ "python3" ]

CMD [ "/app/app.py" ]
