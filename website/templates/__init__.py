from flask import Flask
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hello i am shreya'

    return app

