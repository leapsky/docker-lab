FROM python:3.12-alpine

COPY ./requirements.txt /requirements.txt

# BUG FIX #13: Изменена рабочая директория на /app
# Было: WORKDIR /
# Стало: WORKDIR /app (соответствует монтированию templates в /app/templates)
WORKDIR /app

RUN pip install -r /requirements.txt

COPY . /app

RUN adduser -S www

USER www

ENTRYPOINT [ "python3" ]

# BUG FIX #11: Исправлено имя исполняемого файла
# Было: CMD [ "app1.py" ] (неверное имя файла для app2)
# Стало: CMD [ "app2.py" ] (правильное имя файла)
CMD [ "app2.py" ]
