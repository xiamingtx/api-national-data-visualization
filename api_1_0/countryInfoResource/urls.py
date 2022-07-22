#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask_restful import Api

from . import countryinfo_blueprint
from api_1_0.countryInfoResource.countryInfoResource import CountryInfoResource
from api_1_0.countryInfoResource.countryInfoOtherResource import CountryInfoOtherResource

api = Api(countryinfo_blueprint)

api.add_resource(CountryInfoResource, '/countryInfo/<CountryInfoID>', '/countryInfo', endpoint='CountryInfo')

