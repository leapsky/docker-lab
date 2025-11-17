FROM python:3.12-alpine

COPY ./requirements.txt /requirements.txt

# BUG FIX #13: Изменена рабочая директория на /app
WORKDIR /app

RUN pip install -r /requirements.txt

COPY . /app

RUN adduser -S www

USER www

ENTRYPOINT [ "python3" ]

CMD [ "app1.py" ]
