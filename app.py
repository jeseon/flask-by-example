from flask import Flask
import os

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTING'])


@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/<name>')
def hello_name(name):
    return 'Hello {}!'.format(name)


if __name__ == '__main__':
	app.run()

