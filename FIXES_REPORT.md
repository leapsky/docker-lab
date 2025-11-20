### 1. **docker-compose.yml**
- **Исправление**: Изменен порт на `"443:443"`

### 2. **app1/app1.py**
- **Исправление**: Изменен маршрут на `@app.route('/')`
- **Исправление**: Изменен порт на `port=80`
- **Исправление**: Добавлен `template_folder='/storage'`

### 3. **app2/app2.py**
- **Исправление**: Изменен маршрут на `@app.route('/')`
- **Исправление**: Добавлен параметр `source_app='app2'`
- **Исправление**: Добавлен `template_folder='/storage'`

### 4. **app2/Dockerfile**
- **Исправление**: Изменен на `CMD [ "app2.py" ]`

### 5. **nginx/nginx.conf**
- **Исправление**: Изменен `proxy_pass http://loadbalancer`
- **Исправление**: Изменены порты на `server app1:80` и `server app2:80`
- **Исправление**: Добавлены полные пути `/etc/ssl/certs/` и `/etc/ssl/private/`

### 6. **SSL сертификаты**
- **Исправление**: Созданы самоподписанные сертификаты для localhost
- **Исправление**: Обновлен Dockerfile nginx для копирования сертификатов

### 7. **storage/index.html**
- **Исправление**: Исправлен HTML тег на `<h1>Hello World from {{ source_app }}!</h1>`

## Команды для запуска системы:

```bash
copy your certs to ./nginx/www.example.com.crt and ./nginx/www.example.com.key
```

```bash
docker-compose up --build
```

Система будет доступна по адресу: **https://localhost**
