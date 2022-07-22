#!/usr/bin/env python
# -*- coding:utf-8 -*- 

from flask_restful import Resource, reqparse
from flask import jsonify

from controller.countryInfoController import CountryInfoController
from utils import commons
from utils.response_code import RET


class CountryInfoResource(Resource):

    # get
    @classmethod
    def get(cls, CountryInfoID=None):
        if CountryInfoID:
            kwargs = {
                'CountryInfoID': CountryInfoID
            }

            res = CountryInfoController.get(**kwargs)
            if res['code'] == RET.OK:
                return jsonify(code=res['code'], message=res['message'], data=res['data'])
            else:
                return jsonify(code=res['code'], message=res['message'], data=res['data'])

        parser = reqparse.RequestParser()
        parser.add_argument('CountryID', location='args', required=False, help='CountryID参数类型不正确或缺失')
        parser.add_argument('GDP', location='args', required=False, help='GDP参数类型不正确或缺失')
        parser.add_argument('PrimaryIndustry', location='args', required=False, help='PrimaryIndustry参数类型不正确或缺失')
        parser.add_argument('SecondaryIndustry', location='args', required=False, help='SecondaryIndustry参数类型不正确或缺失')
        parser.add_argument('TertiaryIndustry', location='args', required=False, help='TertiaryIndustry参数类型不正确或缺失')
        parser.add_argument('FarmingIndustry', location='args', required=False, help='FarmingIndustry参数类型不正确或缺失')
        parser.add_argument('Industry', location='args', required=False, help='Industry参数类型不正确或缺失')
        parser.add_argument(' ConstructionIndustry', location='args', required=False, help=' ConstructionIndustry参数类型不正确或缺失')
        parser.add_argument('WholesaleAndRetail', location='args', required=False, help='WholesaleAndRetail参数类型不正确或缺失')
        parser.add_argument('TransportationAndStorage', location='args', required=False, help='TransportationAndStorage参数类型不正确或缺失')
        parser.add_argument('AccommodationAndCatering', location='args', required=False, help='AccommodationAndCatering参数类型不正确或缺失')
        parser.add_argument('FinancialBusiness', location='args', required=False, help='FinancialBusiness参数类型不正确或缺失')
        parser.add_argument('RealtyBusiness', location='args', required=False, help='RealtyBusiness参数类型不正确或缺失')
        parser.add_argument('Others', location='args', required=False, help='Others参数类型不正确或缺失')
        parser.add_argument('InfoYear', location='args', required=False, help='InfoYear参数类型不正确或缺失')
        parser.add_argument('CreatedTime', location='args', required=False, help='CreatedTime参数类型不正确或缺失')
        parser.add_argument('DeletedTime', location='args', required=False, help='DeletedTime参数类型不正确或缺失')
        
        parser.add_argument('Page', location='args', required=False, help='Page参数类型不正确或缺失')
        parser.add_argument('Size', location='args', required=False, help='Size参数类型不正确或缺失')

        kwargs = parser.parse_args()
        kwargs = commons.put_remove_none(**kwargs)

        res = CountryInfoController.get(**kwargs)
        if res['code'] == RET.OK:
            return jsonify(code=res['code'], message=res['message'], data=res['data'], totalPage=res['totalPage'], totalCount=res['totalCount'])
        else:
            return jsonify(code=res['code'], message=res['message'], data=res['data']) 

    # delete
    @classmethod
    def delete(cls, CountryInfoID=None):
        if CountryInfoID:
            kwargs = {
                'CountryInfoID': CountryInfoID
            }

        else:
            parser = reqparse.RequestParser()
            parser.add_argument('CountryID', location='form', required=False, help='CountryID参数类型不正确或缺失')
            parser.add_argument('GDP', location='form', required=False, help='GDP参数类型不正确或缺失')
            parser.add_argument('PrimaryIndustry', location='form', required=False, help='PrimaryIndustry参数类型不正确或缺失')
            parser.add_argument('SecondaryIndustry', location='form', required=False, help='SecondaryIndustry参数类型不正确或缺失')
            parser.add_argument('TertiaryIndustry', location='form', required=False, help='TertiaryIndustry参数类型不正确或缺失')
            parser.add_argument('FarmingIndustry', location='form', required=False, help='FarmingIndustry参数类型不正确或缺失')
            parser.add_argument('Industry', location='form', required=False, help='Industry参数类型不正确或缺失')
            parser.add_argument(' ConstructionIndustry', location='form', required=False, help=' ConstructionIndustry参数类型不正确或缺失')
            parser.add_argument('WholesaleAndRetail', location='form', required=False, help='WholesaleAndRetail参数类型不正确或缺失')
            parser.add_argument('TransportationAndStorage', location='form', required=False, help='TransportationAndStorage参数类型不正确或缺失')
            parser.add_argument('AccommodationAndCatering', location='form', required=False, help='AccommodationAndCatering参数类型不正确或缺失')
            parser.add_argument('FinancialBusiness', location='form', required=False, help='FinancialBusiness参数类型不正确或缺失')
            parser.add_argument('RealtyBusiness', location='form', required=False, help='RealtyBusiness参数类型不正确或缺失')
            parser.add_argument('Others', location='form', required=False, help='Others参数类型不正确或缺失')
            parser.add_argument('InfoYear', location='form', required=False, help='InfoYear参数类型不正确或缺失')
            parser.add_argument('CreatedTime', location='form', required=False, help='CreatedTime参数类型不正确或缺失')
            parser.add_argument('DeletedTime', location='form', required=False, help='DeletedTime参数类型不正确或缺失')
            
            # Pass in the ID list for multiple deletions
            parser.add_argument('CountryInfoID', type=str, location='form', required=False, help='CountryInfoID参数类型不正确或缺失')

            kwargs = parser.parse_args()
            kwargs = commons.put_remove_none(**kwargs)

        res = CountryInfoController.delete(**kwargs)

        return jsonify(code=res['code'], message=res['message'], data=res['data'])

    # put
    @classmethod
    def put(cls, CountryInfoID):
        if not CountryInfoID:
            return jsonify(code=RET.NODATA, message='primary key missed', error='primary key missed')

        parser = reqparse.RequestParser()
        parser.add_argument('CountryID', location='form', required=False, help='CountryID参数类型不正确或缺失')
        parser.add_argument('GDP', location='form', required=False, help='GDP参数类型不正确或缺失')
        parser.add_argument('PrimaryIndustry', location='form', required=False, help='PrimaryIndustry参数类型不正确或缺失')
        parser.add_argument('SecondaryIndustry', location='form', required=False, help='SecondaryIndustry参数类型不正确或缺失')
        parser.add_argument('TertiaryIndustry', location='form', required=False, help='TertiaryIndustry参数类型不正确或缺失')
        parser.add_argument('FarmingIndustry', location='form', required=False, help='FarmingIndustry参数类型不正确或缺失')
        parser.add_argument('Industry', location='form', required=False, help='Industry参数类型不正确或缺失')
        parser.add_argument(' ConstructionIndustry', location='form', required=False, help=' ConstructionIndustry参数类型不正确或缺失')
        parser.add_argument('WholesaleAndRetail', location='form', required=False, help='WholesaleAndRetail参数类型不正确或缺失')
        parser.add_argument('TransportationAndStorage', location='form', required=False, help='TransportationAndStorage参数类型不正确或缺失')
        parser.add_argument('AccommodationAndCatering', location='form', required=False, help='AccommodationAndCatering参数类型不正确或缺失')
        parser.add_argument('FinancialBusiness', location='form', required=False, help='FinancialBusiness参数类型不正确或缺失')
        parser.add_argument('RealtyBusiness', location='form', required=False, help='RealtyBusiness参数类型不正确或缺失')
        parser.add_argument('Others', location='form', required=False, help='Others参数类型不正确或缺失')
        parser.add_argument('InfoYear', location='form', required=False, help='InfoYear参数类型不正确或缺失')
        parser.add_argument('CreatedTime', location='form', required=False, help='CreatedTime参数类型不正确或缺失')
        parser.add_argument('DeletedTime', location='form', required=False, help='DeletedTime参数类型不正确或缺失')
        
        kwargs = parser.parse_args()
        kwargs = commons.put_remove_none(**kwargs)
        kwargs['CountryInfoID'] = CountryInfoID

        res = CountryInfoController.update(**kwargs)

        return jsonify(code=res['code'], message=res['message'], data=res['data'])

    # add
    @classmethod
    def post(cls):
        '''
        CountryInfoList: Pass in values in JSON format to batch add
        eg.[{k1:v1,k2:v2,...},...]
        '''
        parser = reqparse.RequestParser()
        parser.add_argument('CountryInfoList', type=str, location='form', required=False, help='CountryInfoList参数类型不正确或缺失')

        kwargs = parser.parse_args()
        kwargs = commons.put_remove_none(**kwargs)

        if kwargs.get('CountryInfoList'):
            res = CountryInfoController.add_list(**kwargs)

        else:
            parser.add_argument('CountryID', location='form', required=True, help='CountryID参数类型不正确或缺失')
            parser.add_argument('GDP', location='form', required=False, help='GDP参数类型不正确或缺失')
            parser.add_argument('PrimaryIndustry', location='form', required=False, help='PrimaryIndustry参数类型不正确或缺失')
            parser.add_argument('SecondaryIndustry', location='form', required=False, help='SecondaryIndustry参数类型不正确或缺失')
            parser.add_argument('TertiaryIndustry', location='form', required=False, help='TertiaryIndustry参数类型不正确或缺失')
            parser.add_argument('FarmingIndustry', location='form', required=False, help='FarmingIndustry参数类型不正确或缺失')
            parser.add_argument('Industry', location='form', required=False, help='Industry参数类型不正确或缺失')
            parser.add_argument(' ConstructionIndustry', location='form', required=False, help=' ConstructionIndustry参数类型不正确或缺失')
            parser.add_argument('WholesaleAndRetail', location='form', required=False, help='WholesaleAndRetail参数类型不正确或缺失')
            parser.add_argument('TransportationAndStorage', location='form', required=False, help='TransportationAndStorage参数类型不正确或缺失')
            parser.add_argument('AccommodationAndCatering', location='form', required=False, help='AccommodationAndCatering参数类型不正确或缺失')
            parser.add_argument('FinancialBusiness', location='form', required=False, help='FinancialBusiness参数类型不正确或缺失')
            parser.add_argument('RealtyBusiness', location='form', required=False, help='RealtyBusiness参数类型不正确或缺失')
            parser.add_argument('Others', location='form', required=False, help='Others参数类型不正确或缺失')
            parser.add_argument('InfoYear', location='form', required=False, help='InfoYear参数类型不正确或缺失')
            parser.add_argument('CreatedTime', location='form', required=False, help='CreatedTime参数类型不正确或缺失')
            parser.add_argument('DeletedTime', location='form', required=False, help='DeletedTime参数类型不正确或缺失')
            
            kwargs = parser.parse_args()
            kwargs = commons.put_remove_none(**kwargs)

            res = CountryInfoController.add(**kwargs)

        return jsonify(code=res['code'], message=res['message'], data=res['data'])
