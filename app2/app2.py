from flask import Flask, render_template

app = Flask(__name__)


@app.route('/hello')
def hello_world():
    # Не указан параметр source_app
    return render_template('index.html', source_app='app2')


if __name__ == '__main__':
    # Неверный порт под nginx
   app.run(debug=True, host='0.0.0.0', port=81)
