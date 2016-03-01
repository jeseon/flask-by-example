#!/usr/bin/env python
# coding: utf-8
from flask.ext.script import Manager
from example import create_app

app = create_app()
manager = Manager(app)

if __name__ == '__main__':
    manager.run()
