from flask import Flask, render_template
import socket

app = Flask(__name__, template_folder='/app/storage')
hostname = socket.gethostname()


@app.route('/hello')
def hello_world():
    return render_template('index.html', source_app=hostname)


if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0', port=81)
