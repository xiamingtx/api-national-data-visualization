#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import jsonify
from flask_restful import Resource, reqparse

from utils import commons
from service.countryInfoService import CountryInfoService
from utils.response_code import RET


class CountryInfoOtherResource(Resource):

	# 返回最近一年的各国概览统计表  国家名 GDP(亿元)  人口(万人)   人均GDP(万元)
	@classmethod
	def get_general_info(cls):
		parser = reqparse.RequestParser()

		kwargs = parser.parse_args()
		kwargs = commons.put_remove_none(**kwargs)

		res = CountryInfoService.get_general_info(**kwargs)
		if res['code'] == RET.OK:
			return jsonify(code=res['code'], message=res['message'], data=res['data'], totalCount=res['totalCount'])
		else:
			return jsonify(code=res['code'], message=res['message'], data=res['data'])

	@classmethod
	def get_details_by_country_id(cls, country_id):

		if country_id:
			kwargs = {
				'CountryID': country_id
			}
		else:
			return jsonify(code=RET.PARAMERR, message='缺少参数country_id')

		res = CountryInfoService.get_details_by_country_id(**kwargs)
		if res['code'] == RET.OK:
			return jsonify(code=res['code'], message=res['message'], data=res['data'], totalCount=res['totalCount'])
		else:
			return jsonify(code=res['code'], message=res['message'], data=res['data'])

	@classmethod
	def get_all_details(cls):
		res = CountryInfoService.get_all_details()
		if res['code'] == RET.OK:
			return jsonify(code=res['code'], message=res['message'], data=res['data'], totalCount=res['totalCount'])
		else:
			return jsonify(code=res['code'], message=res['message'], data=res['data'])