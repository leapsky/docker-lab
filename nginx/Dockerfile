FROM nginx:alpine
RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Отсутствует работа с SSL сертификатами
RUN mkdir -p /etc/nginx/certificates
COPY www.example.com.crt /etc/nginx/certificates/www.example.com.crt
COPY www.example.com.key /etc/nginx/certificates/www.example.com.key