from flask import Flask
import os

app = Flask(__name__)


@app.route('/')
def start():
    return "<h1>Миссия Колонизация Марса</h1>"


@app.route('/index')
def index():
    return "<h2>И на Марсе будут яблони цвести!<h2>"


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)