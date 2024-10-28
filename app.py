from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, World!"

@app.route('/add/<int:a>/<int:b>')
def add(a, b):
    return str(a + b)

if __name__ == '__main__':
    # Use host='0.0.0.0' to make it accessible externally (e.g., on EC2)
    # Adjust the port as needed; 5000 is a common choice
    app.run(host='0.0.0.0', port=5000)
