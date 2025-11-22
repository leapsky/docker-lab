from flask import Flask, render_template

# Подключаем общий каталог шаблонов ../storage
app = Flask(__name__, template_folder='../storage')


# Обрабатываем запрос по /
@app.route('/')
@app.route('/hello')
def hello_world():
    # Передаём source_app в шаблон, чтобы на странице было видно имя сервиса
    return render_template('index.html', source_app='app2')


if __name__ == '__main__':
   # Используем порт >1024, чтобы non-root пользователь www мог привязаться
   app.run(debug=True, host='0.0.0.0', port=8081)
