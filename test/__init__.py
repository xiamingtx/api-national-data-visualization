#!/usr/bin/env python
# -*- coding:utf-8 -*-

from app import create_app

app = create_app("develop")
app.app_context().push()
