from flask import Flask, render_template

# Добавили путь до папки
app = Flask(__name__, template_folder='/storage')


@app.route('/hello')
def hello_world():
    # Указали параметр шаблона
    return render_template('index.html', source_app='app1')


if __name__ == '__main__':
    # Будем слушать на 8080
   app.run(debug=True, host='0.0.0.0', port=8080)
