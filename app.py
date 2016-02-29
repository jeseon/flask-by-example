from flask import Flask
import os
import config


app = Flask(__name__)
config.init_app(app)

@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/<name>')
def hello_name(name):
    return 'Hello {}!'.format(name)


if __name__ == '__main__':
	app.run()

