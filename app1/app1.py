from flask import Flask, render_template

app = Flask(__name__)


@app.route('/hello')
def hello_world():
    return render_template('index.html', source_app='app1')


if __name__ == '__main__':
   # BUG FIX #8: Исправлен порт приложения для соответствия nginx upstream: 8080 -> 81
   app.run(debug=True, host='0.0.0.0', port=81)
