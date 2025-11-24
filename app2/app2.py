from flask import Flask, render_template

app = Flask(__name__, template_folder='/storage')


@app.route('/hello')
@app.route('/')
def hello_world():
    return render_template('index.html', source_app='app2')


if __name__ == '__main__':
    # use port, which is greater than 1024
    app.run(debug=True, host='0.0.0.0', port=8081)
