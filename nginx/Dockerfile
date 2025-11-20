FROM nginx:alpine
RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Добавлено копирование SSL сертификатов в контейнер
RUN mkdir -p /etc/nginx/certs
COPY www.example.com.crt /etc/nginx/certs/www.example.com.crt
COPY www.example.com.key /etc/nginx/certs/www.example.com.key
