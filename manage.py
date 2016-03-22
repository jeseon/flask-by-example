#!/usr/bin/env python
# coding: utf-8
from flask_script import Manager
from example import create_app

app = create_app()
manager = Manager(app)

if __name__ == '__main__':
    manager.run()
