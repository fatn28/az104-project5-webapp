from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return 'Hello from AZ-104 Projekt 5 - STAGING Version!'


if __name__ == '__main__':
    app.run()
