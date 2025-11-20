FROM nginx:alpine
RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d/default.conf
# ИСПРАВЛЕНО: Установка openssl (не включен в nginx:alpine по умолчанию)
RUN apk add --no-cache openssl
# ИСПРАВЛЕНО: Добавлена генерация самоподписанного SSL сертификата
RUN mkdir -p /etc/nginx/ssl && \
    openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
    -keyout /etc/nginx/ssl/www.example.com.key \
    -out /etc/nginx/ssl/www.example.com.crt \
    -subj "/C=RU/ST=State/L=City/O=Organization/CN=www.example.com"
