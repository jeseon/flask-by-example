#!/usr/bin/env python
# coding: utf-8
from flask import Flask
from example.admin import admin
from example.models import db
import config
import os


def create_app():
    """
    :return: flask application

    flask application generator
    """
    current_dir = os.path.abspath(os.path.dirname(__file__))
    template_folder = os.path.join(current_dir, 'templates')

    app = Flask(__name__, template_folder=template_folder)
    config.init_app(app)
    db.init_app(app)
    admin.init_app(app)
    
    """ application blueprints """
    from example.main import main as main_blueprint

    app.register_blueprint(main_blueprint)

    return app
