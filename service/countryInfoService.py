#!/usr/bin/env python
# -*- coding:utf-8 -*-
import math
import time

from sqlalchemy import func

from app import db
from models.countryInfoModel import CountryInfo
from models.countryModel import Country
from utils import commons
from utils.loggings import loggings
from utils.response_code import RET, error_map_EN


class CountryInfoService(CountryInfo):

    # 返回最近一年的各国概览统计表  国家名 GDP(亿元)  人口(万人)   人均GDP(万元)
    @classmethod
    def get_general_info(cls, **kwargs):
        filter_list = [cls.IsDeleted == 0]
        try:
            info = db.session.query(
                cls.CountryID,
                Country.CountryName,
                cls.GDP,
                cls.Population,
                cls.AvgGDP
            ).outerjoin(Country, Country.CountryID == cls.CountryID).filter(*filter_list).order_by(
                cls.InfoYear.desc()).group_by(cls.CountryID)

            count = info.count()

            results = commons.query_to_dict(info.all())

            return {'code': RET.OK, 'message': error_map_EN[RET.OK], 'totalCount': count, 'data': results}
        except Exception as e:
            loggings.exception(1, e)
            return {'code': RET.DBERR, 'message': error_map_EN[RET.DBERR], 'data': {'error': str(e)}}
        finally:
            db.session.close()

    @classmethod
    def get_details_by_country_id(cls, **kwargs):
        filter_list = [cls.IsDeleted == 0, cls.CountryID == kwargs.get('CountryID')]
        try:
            detail = db.session.query(cls.CountryID, cls.CountryInfoID, cls.GDP, cls.Population, cls.InfoYear,
                                      cls.AvgGDP, cls.PrimaryIndustry, cls.SecondaryIndustry, cls.TertiaryIndustry,
                                      cls.FarmingIndustry, cls.Industry, cls.ConstructionIndustry,
                                      cls.WholesaleAndRetail, cls.TransportationAndStorage, cls.AccommodationAndCatering,
                                      cls.FinancialBusiness, cls.RealtyBusiness, cls.Others, Country.CountryName) \
                .outerjoin(Country, Country.CountryID == kwargs.get('CountryID')) \
                .filter(*filter_list).order_by(cls.InfoYear.desc())

            count = detail.count()

            results = commons.query_to_dict(detail.all())

            return {'code': RET.OK, 'message': error_map_EN[RET.OK], 'totalCount': count, 'data': results}
        except Exception as e:
            loggings.exception(1, e)
            return {'code': RET.DBERR, 'message': error_map_EN[RET.DBERR], 'data': {'error': str(e)}}
        finally:
            db.session.close()

    @classmethod
    def get_all_details(cls):
        filter_list = [cls.IsDeleted == 0]
        try:
            detail = db.session.query(cls.CountryID, cls.CountryInfoID, cls.GDP, cls.Population, cls.InfoYear,
                                      cls.AvgGDP, cls.PrimaryIndustry, cls.SecondaryIndustry, cls.TertiaryIndustry,
                                      cls.FarmingIndustry, cls.Industry, cls.ConstructionIndustry,
                                      cls.WholesaleAndRetail, cls.TransportationAndStorage, cls.AccommodationAndCatering,
                                      cls.FinancialBusiness, cls.RealtyBusiness, cls.Others, Country.CountryName) \
                .outerjoin(Country, Country.CountryID == cls.CountryID) \
                .filter(*filter_list).order_by(cls.InfoYear.desc())

            count = detail.count()

            results = commons.query_to_dict(detail.all())

            return {'code': RET.OK, 'message': error_map_EN[RET.OK], 'totalCount': count, 'data': results}
        except Exception as e:
            loggings.exception(1, e)
            return {'code': RET.DBERR, 'message': error_map_EN[RET.DBERR], 'data': {'error': str(e)}}
        finally:
            db.session.close()
