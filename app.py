# app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, DUniya!"

@app.route('/add/<int:a>/<int:b>')
def add(a, b):
    return str(a + b)

if __name__ == '__main__':
    app.run()
