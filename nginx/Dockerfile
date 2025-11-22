FROM nginx:alpine
RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d/default.conf

RUN mkdir -p /etc/nginx/ssl
COPY www.example.com.crt /etc/nginx/ssl/www.example.com.crt
COPY www.example.com.key /etc/nginx/ssl/www.example.com.key
