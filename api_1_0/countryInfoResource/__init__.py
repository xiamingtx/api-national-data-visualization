#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Blueprint

countryinfo_blueprint = Blueprint('countryInfo', __name__)

from . import urls
