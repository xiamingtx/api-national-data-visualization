#!/usr/bin/env python
# -*- coding:utf-8 -*- 

from flask_restful import Resource, reqparse
from flask import jsonify

from controller.countryController import CountryController
from utils import commons
from utils.response_code import RET


class CountryResource(Resource):

    # get
    @classmethod
    def get(cls, CountryID=None):
        if CountryID:
            kwargs = {
                'CountryID': CountryID
            }

            res = CountryController.get(**kwargs)
            if res['code'] == RET.OK:
                return jsonify(code=res['code'], message=res['message'], data=res['data'])
            else:
                return jsonify(code=res['code'], message=res['message'], data=res['data'])

        parser = reqparse.RequestParser()
        parser.add_argument('CountryName', location='args', required=False, help='CountryName参数类型不正确或缺失')
        parser.add_argument('CreatedTime', location='args', required=False, help='CreatedTime参数类型不正确或缺失')
        parser.add_argument('UpdatedTime', location='args', required=False, help='UpdatedTime参数类型不正确或缺失')
        
        parser.add_argument('Page', location='args', required=False, help='Page参数类型不正确或缺失')
        parser.add_argument('Size', location='args', required=False, help='Size参数类型不正确或缺失')

        kwargs = parser.parse_args()
        kwargs = commons.put_remove_none(**kwargs)

        res = CountryController.get(**kwargs)
        if res['code'] == RET.OK:
            return jsonify(code=res['code'], message=res['message'], data=res['data'], totalPage=res['totalPage'], totalCount=res['totalCount'])
        else:
            return jsonify(code=res['code'], message=res['message'], data=res['data']) 

    # delete
    @classmethod
    def delete(cls, CountryID=None):
        if CountryID:
            kwargs = {
                'CountryID': CountryID
            }

        else:
            parser = reqparse.RequestParser()
            parser.add_argument('CountryName', location='form', required=False, help='CountryName参数类型不正确或缺失')
            parser.add_argument('CreatedTime', location='form', required=False, help='CreatedTime参数类型不正确或缺失')
            parser.add_argument('UpdatedTime', location='form', required=False, help='UpdatedTime参数类型不正确或缺失')
            
            # Pass in the ID list for multiple deletions
            parser.add_argument('CountryID', type=str, location='form', required=False, help='CountryID参数类型不正确或缺失')

            kwargs = parser.parse_args()
            kwargs = commons.put_remove_none(**kwargs)

        res = CountryController.delete(**kwargs)

        return jsonify(code=res['code'], message=res['message'], data=res['data'])

    # put
    @classmethod
    def put(cls, CountryID):
        if not CountryID:
            return jsonify(code=RET.NODATA, message='primary key missed', error='primary key missed')

        parser = reqparse.RequestParser()
        parser.add_argument('CountryName', location='form', required=False, help='CountryName参数类型不正确或缺失')
        parser.add_argument('CreatedTime', location='form', required=False, help='CreatedTime参数类型不正确或缺失')
        parser.add_argument('UpdatedTime', location='form', required=False, help='UpdatedTime参数类型不正确或缺失')
        
        kwargs = parser.parse_args()
        kwargs = commons.put_remove_none(**kwargs)
        kwargs['CountryID'] = CountryID

        res = CountryController.update(**kwargs)

        return jsonify(code=res['code'], message=res['message'], data=res['data'])

    # add
    @classmethod
    def post(cls):
        '''
        CountryList: Pass in values in JSON format to batch add
        eg.[{k1:v1,k2:v2,...},...]
        '''
        parser = reqparse.RequestParser()
        parser.add_argument('CountryList', type=str, location='form', required=False, help='CountryList参数类型不正确或缺失')

        kwargs = parser.parse_args()
        kwargs = commons.put_remove_none(**kwargs)

        if kwargs.get('CountryList'):
            res = CountryController.add_list(**kwargs)

        else:
            parser.add_argument('CountryName', location='form', required=False, help='CountryName参数类型不正确或缺失')
            parser.add_argument('CreatedTime', location='form', required=False, help='CreatedTime参数类型不正确或缺失')
            parser.add_argument('UpdatedTime', location='form', required=False, help='UpdatedTime参数类型不正确或缺失')
            
            kwargs = parser.parse_args()
            kwargs = commons.put_remove_none(**kwargs)

            res = CountryController.add(**kwargs)

        return jsonify(code=res['code'], message=res['message'], data=res['data'])
