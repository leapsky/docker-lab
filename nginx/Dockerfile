FROM nginx:alpine
RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d/default.conf

# ИСПРАВЛЕНО: Добавлены команды для копирования SSL сертификатов
COPY www.example.com.crt /etc/ssl/certs/www.example.com.crt
COPY www.example.com.key /etc/ssl/private/www.example.com.key
