FROM nginx:alpine
RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d/default.conf

# BUG FIX #7: Добавлено копирование SSL сертификатов в контейнер
# Создаем директорию для сертификатов и копируем их
RUN mkdir -p /etc/nginx/certs
COPY www.example.com.crt /etc/nginx/certs/www.example.com.crt
COPY www.example.com.key /etc/nginx/certs/www.example.com.key
