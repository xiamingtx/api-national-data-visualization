#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask_restful import Api

from . import country_blueprint
from api_1_0.countryResource.countryResource import CountryResource
from api_1_0.countryResource.countryOtherResource import CountryOtherResource

api = Api(country_blueprint)

api.add_resource(CountryResource, '/<CountryID>', endpoint='Country')


# 获取国家列表
@country_blueprint.route('/countries', methods=['GET'], endpoint='countries')
def get_countries():
    return CountryOtherResource.get_countries()
