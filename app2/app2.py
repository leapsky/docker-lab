from flask import Flask, render_template

app = Flask(__name__)


@app.route('/hello')
def hello_world():
    # Добавлен параметр source_app для корректного отображения
    return render_template('index.html', source_app='app2')


if __name__ == '__main__':
    # Исправлен порт  80 -> 81
   app.run(debug=True, host='0.0.0.0', port=81)
