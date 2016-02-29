#!/usr/bin/env python
# coding: utf-8
from flask_admin.contrib.sqla import ModelView


class CeoNoticeView(ModelView):
    can_delete = False
