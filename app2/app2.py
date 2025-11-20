from flask import Flask, render_template

app = Flask(__name__)


# ИСПРАВЛЕНО: Изменен маршрут с '/hello' на '/' для обработки корневого пути
@app.route('/')
def hello_world():
    # ИСПРАВЛЕНО: Добавлен параметр source_app='app2' для идентификации приложения
    return render_template('index.html', source_app='app2')


if __name__ == '__main__':
   # ИСПРАВЛЕНО: Изменен порт с 80 на 8080, так как пользователь www не может слушать порты <1024
   app.run(debug=True, host='0.0.0.0', port=8080)
