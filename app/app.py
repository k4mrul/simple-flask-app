from flask import Flask

app = Flask(__name__)


@app.route('/', methods=['GET'])
def get():
    return 'Hello from flask'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9999, debug=True)