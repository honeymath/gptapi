import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    path = os.getenv('PATH')
    return f'PATH: {path}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

