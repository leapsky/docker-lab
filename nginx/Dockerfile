FROM nginx:alpine
RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d/default.conf
# copy TLS certs and key into the image
COPY www.example.com.crt /etc/nginx/www.example.com.crt
COPY www.example.com.key /etc/nginx/www.example.com.key
