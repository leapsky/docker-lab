FROM python:3.12-alpine

COPY ./requirements.txt /requirements.txt

# Неверная рабочая директория
WORKDIR /app

# Неверное указание на файл
RUN pip install -r /requirements.txt

# Неверная рабочая директория
COPY . /app

RUN adduser -S www

USER www

ENTRYPOINT [ "python3" ]

# Неверное указание на py файл
CMD [ "app2.py" ]
