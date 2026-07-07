from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return 'Hello from AZ-104 Projekt 5 - App Service Deployment & Scaling!'


if __name__ == '__main__':
    app.run()
