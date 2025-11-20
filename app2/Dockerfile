FROM python:3.12-alpine

COPY ./requirements.txt /requirements.txt

WORKDIR /

RUN pip install -r requirements.txt

COPY . /

RUN adduser -S www

USER www

ENTRYPOINT [ "python3" ]

# ИСПРАВЛЕНО: Изменено имя файла с "app1.py" на "app2.py"
CMD [ "app2.py" ]
