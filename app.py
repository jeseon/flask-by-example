#!/usr/bin/env python
# coding: utf-8
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import os
import config


app = Flask(__name__)
config.init_app(app)
db = SQLAlchemy(app)

from models import CeoNotice

@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/notice/<int:id>')
def notice(id):
    return 'Title: ' + CeoNotice.query.filter_by(id=id).first().title


if __name__ == '__main__':
	app.run()
