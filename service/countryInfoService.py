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
from queue import Queue


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

    # 根据国家的country_id查询该国所有数据
    @classmethod
    def get_details_by_country_id(cls, **kwargs):
        filter_list = [cls.IsDeleted == 0, cls.CountryID == kwargs.get('CountryID')]
        if kwargs.get('Year'):
            filter_list.append(cls.InfoYear == kwargs.get('Year'))
        try:
            detail = db.session.query(cls.CountryID, cls.CountryInfoID, cls.GDP, cls.Population, cls.InfoYear,
                                      cls.AvgGDP, cls.PrimaryIndustry, cls.SecondaryIndustry, cls.TertiaryIndustry,
                                      cls.FarmingIndustry, cls.Industry, cls.ConstructionIndustry, cls.GDPIncRate,
                                      cls.WholesaleAndRetail, cls.TransportationAndStorage,
                                      cls.AccommodationAndCatering,
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

    # 根据国家的country_id查询该国最近一年数据
    @classmethod
    def get_recent_by_country_id(cls, country_id):
        filter_list = [cls.IsDeleted == 0, cls.CountryID == country_id]
        try:
            detail = db.session.query(cls.CountryID, cls.CountryInfoID, cls.GDP, cls.Population, cls.InfoYear,
                                      cls.AvgGDP, cls.PrimaryIndustry, cls.SecondaryIndustry, cls.TertiaryIndustry,
                                      cls.FarmingIndustry, cls.Industry, cls.ConstructionIndustry, cls.GDPIncRate,
                                      cls.WholesaleAndRetail, cls.TransportationAndStorage,
                                      cls.AccommodationAndCatering,
                                      cls.FinancialBusiness, cls.RealtyBusiness, cls.Others, Country.CountryName) \
                .outerjoin(Country, Country.CountryID == country_id) \
                .filter(*filter_list).order_by(cls.InfoYear.desc())

            results = commons.query_to_dict(detail.first())

            return {'code': RET.OK, 'message': error_map_EN[RET.OK], 'data': results}
        except Exception as e:
            loggings.exception(1, e)
            return {'code': RET.DBERR, 'message': error_map_EN[RET.DBERR], 'data': {'error': str(e)}}
        finally:
            db.session.close()

    # 查询所有国家的详情数据
    @classmethod
    def get_all_details(cls):
        filter_list = [cls.IsDeleted == 0]
        try:
            detail = db.session.query(cls.CountryID, cls.CountryInfoID, cls.GDP, cls.Population, cls.InfoYear,
                                      cls.AvgGDP, cls.PrimaryIndustry, cls.SecondaryIndustry, cls.TertiaryIndustry,
                                      cls.FarmingIndustry, cls.Industry, cls.ConstructionIndustry, cls.GDPIncRate,
                                      cls.WholesaleAndRetail, cls.TransportationAndStorage,
                                      cls.AccommodationAndCatering,
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

    # 预测
    @classmethod
    def forecast(cls, country_id):
        filter_list = [cls.IsDeleted == 0, cls.CountryID == country_id]
        try:
            info = db.session.query(cls.GDP, cls.GDPIncRate, cls.InfoYear).filter(*filter_list).order_by(cls.InfoYear.desc()).all()
            results = commons.query_to_dict(info)[:5]
            inc_queue = Queue()
            inc_sum = 0
            for i in range(len(results)):
                idx = len(results) - i - 1
                inc_queue.put(results[idx]['GDPIncRate'])
                inc_sum = inc_sum + results[idx]['GDPIncRate']

            inc_avg = inc_sum / len(results)
            rawData = results[0]['GDP']
            start_year = results[0]['InfoYear'] + 1
            data = []
            for i in range(len(results)):
                data.append({
                    'GDP': round(rawData * (1 + inc_avg / 100), 1),
                    'GDPIncRate': round(inc_avg, 1),
                    'InfoYear': start_year
                })
                start_year = start_year + 1
                inc_sum = inc_sum - inc_queue.get()  # 取出队首并删除
                inc_sum = inc_sum + inc_avg  # 总和加入最新一年的增长率
                inc_avg = inc_sum / len(results)
                rawData = rawData * (1 + inc_avg / 100)
                inc_queue.put(inc_avg)  # 将最新一年增长率放入队列中

            return {'code': RET.OK, 'message': error_map_EN[RET.OK], 'data': data}
        except Exception as e:
            loggings.exception(1, e)
            return {'code': RET.DBERR, 'message': error_map_EN[RET.DBERR], 'data': {'error': str(e)}}
        finally:
            db.session.close()
