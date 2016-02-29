#!/usr/bin/env python
# coding: utf-8
from flask import Flask
from flask_admin import Admin
from flask.ext.sqlalchemy import SQLAlchemy
from views import CeoNoticeView
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

admin = Admin(app, name='Flask-Admin', template_mode='bootstrap3')
admin.add_view(CeoNoticeView(CeoNotice, db.session, category='공지사항', name='점주 공지사항'))

if __name__ == '__main__':
	app.run()
