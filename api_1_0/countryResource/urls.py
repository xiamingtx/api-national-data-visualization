#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask_restful import Api

from . import country_blueprint
from api_1_0.countryResource.countryResource import CountryResource
from api_1_0.countryResource.countryOtherResource import CountryOtherResource

api = Api(country_blueprint)

api.add_resource(CountryResource, '/country/<CountryID>', '/country', endpoint='Country')

