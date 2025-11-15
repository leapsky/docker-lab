FROM nginx:alpine
RUN rm /etc/nginx/conf.d/default.conf
COPY www.example.com.crt /etc/nginx/www.example.com.crt
COPY www.example.com.key /etc/nginx/www.example.com.key
COPY nginx.conf /etc/nginx/conf.d/default.conf
