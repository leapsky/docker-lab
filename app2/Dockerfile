FROM python:3.12-alpine

COPY ./requirements.txt /requirements.txt

WORKDIR /

RUN pip install -r requirements.txt

COPY . /

RUN adduser -S www

USER www

ENTRYPOINT [ "python3" ]

CMD [ "app2.py" ]
