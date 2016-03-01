#!/usr/bin/env python
# coding: utf-8
from flask.ext.admin import Admin
from example.models import db, CeoNotice
from example.admin.views import CeoNoticeView


admin = Admin(name='Flask-Admin', template_mode='bootstrap3')
admin.add_view(CeoNoticeView(CeoNotice, db.session, category='공지사항', name='점주 공지사항'))
