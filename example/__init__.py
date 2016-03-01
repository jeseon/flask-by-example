#!/usr/bin/env python
# coding: utf-8
from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy
import os
import config

current_dir = os.path.abspath(os.path.dirname(__file__))
template_folder = os.path.join(current_dir, 'templates')

app = Flask(__name__, template_folder=template_folder)
config.init_app(app)
db = SQLAlchemy(app)

from admin import admin
from models import CeoNotice

@app.route('/')
def index():
    return render_template('example/index.html', hello='Hello')

@app.route('/notice/<int:id>')
def notice(id):
    return 'Title: ' + CeoNotice.query.filter_by(id=id).first().title


if __name__ == '__main__':
    app.run()
