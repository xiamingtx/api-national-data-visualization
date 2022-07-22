#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Blueprint

country_blueprint = Blueprint('country', __name__)

from . import urls
