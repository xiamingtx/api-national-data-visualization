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
        page = int(kwargs.get('Page', 1))
        size = int(kwargs.get('Size', 10))
        try:
            detail = db.session.query(
                cls.CountryID,
                Country.CountryName,
                cls.GDP,
                cls.Population,
                cls.AvgGDP
            ).outerjoin(Country, Country.CountryID == cls.CountryID).filter(*filter_list).order_by(cls.InfoYear.desc()).group_by(cls.CountryID)

            count = detail.count()
            pages = math.ceil(count / size)
            detail = detail.limit(size).offset((page - 1) * size).all()

            results = commons.query_to_dict(detail)

            return {'code': RET.OK, 'message': error_map_EN[RET.OK], 'totalCount': count, 'totalPage': pages, 'data': results}
        except Exception as e:
            loggings.exception(1, e)
            return {'code': RET.DBERR, 'message': error_map_EN[RET.DBERR], 'data': {'error': str(e)}}
        finally:
            db.session.close()
