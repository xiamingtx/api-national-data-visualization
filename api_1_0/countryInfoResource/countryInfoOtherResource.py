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
		parser.add_argument('Page', location='args', required=False, help='Page参数类型不正确或缺失')
		parser.add_argument('Size', location='args', required=False, help='Size参数类型不正确或缺失')

		kwargs = parser.parse_args()
		kwargs = commons.put_remove_none(**kwargs)

		res = CountryInfoService.get_general_info(**kwargs)
		if res['code'] == RET.OK:
			return jsonify(code=res['code'], message=res['message'], data=res['data'], totalPage=res['totalPage'],
						   totalCount=res['totalCount'])
		else:
			return jsonify(code=res['code'], message=res['message'], data=res['data'])

