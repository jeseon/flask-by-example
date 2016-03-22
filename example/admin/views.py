#!/usr/bin/env python
# coding: utf-8
from flask_admin.contrib.sqla import ModelView


class CeoNoticeView(ModelView):
    can_delete = False
    can_view_details = True
    form_excluded_columns = ['created_at', 'updated_at']
