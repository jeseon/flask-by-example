#!/usr/bin/env python
# coding: utf-8
from example import db
from datetime import datetime


class CeoNotice(db.Model):
    __tablename__ = 'ceo_notices'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Unicode(255), nullable=False)
    is_scheduled = db.Column(db.Boolean, nullable=False, default=False)
    scheduled_at = db.Column(db.DateTime, nullable=True, default=datetime.now)
    image_path = db.Column(db.Unicode(255), nullable=True, default=u'')
    action = db.Column(db.Unicode(100), nullable=True, default=u'')
    content = db.Column(db.UnicodeText, default=u'')
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)
