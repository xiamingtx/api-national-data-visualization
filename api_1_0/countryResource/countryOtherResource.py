#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import jsonify
from flask_restful import Resource, reqparse
from controller.countryController import CountryController
from utils import commons
from utils.response_code import RET


class CountryOtherResource(Resource):

    # 获取国家列表
    @classmethod
    def get_countries(cls):
        parser = reqparse.RequestParser()

        parser.add_argument('Page', location='args', required=False, help='Page参数类型不正确或缺失')
        parser.add_argument('Size', location='args', required=False, help='Size参数类型不正确或缺失')

        kwargs = parser.parse_args()
        kwargs = commons.put_remove_none(**kwargs)

        res = CountryController.get(**kwargs)
        if res['code'] == RET.OK:
            return jsonify(code=res['code'], message=res['message'], data=res['data'], totalPage=res['totalPage'],
                           totalCount=res['totalCount'])
        else:
            return jsonify(code=res['code'], message=res['message'], data=res['data'])
