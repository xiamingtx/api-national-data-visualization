#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask_restful import Api

from . import countryinfo_blueprint
from api_1_0.countryInfoResource.countryInfoResource import CountryInfoResource
from api_1_0.countryInfoResource.countryInfoOtherResource import CountryInfoOtherResource

api = Api(countryinfo_blueprint)

api.add_resource(CountryInfoResource, '/<CountryInfoID>', endpoint='CountryInfo')


# 返回最近一年的各国概览统计表  国家名 GDP(亿元)  人口(万人)   人均GDP(万元)
@countryinfo_blueprint.route('/general_info', methods=['GET'], endpoint='general_info')
def get_general_info():
    return CountryInfoOtherResource.get_general_info()


@countryinfo_blueprint.route('/details/<country_id>', methods=['GET'], endpoint='details')
def get_details_by_country_id(country_id):
    return CountryInfoOtherResource.get_details_by_country_id(country_id)


@countryinfo_blueprint.route('/all', methods=['GET'], endpoint='all')
def get_all_details():
    return CountryInfoOtherResource.get_all_details()