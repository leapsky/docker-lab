FROM nginx:alpine
RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d/default.conf

COPY www.example.com.crt /etc/nginx/
COPY www.example.com.key /etc/nginx/
