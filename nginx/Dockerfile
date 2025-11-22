FROM nginx:alpine

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Копируем сертификат и ключ в /etc/nginx, откуда их читает nginx.conf
COPY www.example.com.crt www.example.com.key /etc/nginx/
