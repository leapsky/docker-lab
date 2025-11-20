from flask import Flask, render_template

# ИСПРАВЛЕНО: Добавлен template_folder='/storage' для корректного поиска HTML шаблонов  
app = Flask(__name__, template_folder='/storage')


# ИСПРАВЛЕНО: Изменен маршрут с '/hello' на '/' для корректной работы с nginx
@app.route('/')
def hello_world():
    # ИСПРАВЛЕНО: Добавлен параметр source_app='app2' для демонстрации балансировки
    return render_template('index.html', source_app='app2')


if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0', port=80)
