FROM python:3.12-alpine

COPY ./requirements.txt /requirements.txt

# Изменена рабочая директория на /app для соответствия структуре проекта
WORKDIR /app

RUN pip install -r requirements.txt

COPY . /

RUN adduser -S www

USER www

ENTRYPOINT [ "python3" ]

CMD [ "app1.py" ]
