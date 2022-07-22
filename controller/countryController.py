#!/usr/bin/env python
# -*- coding:utf-8 -*-

import datetime
import math
import json

from sqlalchemy import or_

from app import db
from models.countryModel import Country
from utils import commons
from utils.response_code import RET, error_map_EN
from utils.loggings import loggings


class CountryController(Country):

    # add
    @classmethod
    def add(cls, **kwargs):
        from utils.generate_id import GenerateID
        CountryID = GenerateID.create_random_id()
        
        try:
            model = Country(
                CountryID=CountryID,
                CountryName=kwargs.get('CountryName'),
                CreatedTime=kwargs.get('CreatedTime'),
                UpdatedTime=kwargs.get('UpdatedTime'),
                
            )
            db.session.add(model)
            db.session.commit()
            results = {
                'add_time': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'CountryID': model.CountryID,
                
            }
            return {'code': RET.OK, 'message': error_map_EN[RET.OK], 'data': results}
            
        except Exception as e:
            db.session.rollback()
            loggings.exception(1, e)
            return {'code': RET.DBERR, 'message': error_map_EN[RET.DBERR], 'data': {'error': str(e)}}
        finally:
            db.session.close()

    # get
    @classmethod
    def get(cls, **kwargs):
        try:
            filter_list = [cls.isDeleted == 0]
            if kwargs.get('CountryID'):
                filter_list.append(cls.CountryID == kwargs['CountryID'])
            else:
                if kwargs.get('CountryName'):
                    filter_list.append(cls.CountryName == kwargs.get('CountryName'))
                if kwargs.get('CreatedTime'):
                    filter_list.append(cls.CreatedTime == kwargs.get('CreatedTime'))
                if kwargs.get('UpdatedTime'):
                    filter_list.append(cls.UpdatedTime == kwargs.get('UpdatedTime'))
                

            page = int(kwargs.get('Page', 1))
            size = int(kwargs.get('Size', 10))
            
            country_info = db.session.query(cls).filter(*filter_list)
            
            count = country_info.count()
            pages = math.ceil(count / size)
            country_info = country_info.limit(size).offset((page - 1) * size).all()
   
            results = commons.query_to_dict(country_info)
            return {'code': RET.OK, 'message': error_map_EN[RET.OK], 'totalCount': count, 'totalPage': pages, 'data': results}
            
        except Exception as e:
            loggings.exception(1, e)
            return {'code': RET.DBERR, 'message': error_map_EN[RET.DBERR], 'data': {'error': str(e)}}
        finally:
            db.session.close()

    # delete
    @classmethod
    def delete(cls, **kwargs):
        try:
            filter_list = [cls.isDeleted == 0]
            if kwargs.get('CountryID'):
                primary_key_list = []
                for primary_key in str(kwargs.get('CountryID')).replace(' ', '').split(','):
                    primary_key_list.append(cls.CountryID == primary_key)
                filter_list.append(or_(*primary_key_list))
                
            else:
                if kwargs.get('CountryName'):
                    filter_list.append(cls.CountryName == kwargs.get('CountryName'))
                if kwargs.get('CreatedTime'):
                    filter_list.append(cls.CreatedTime == kwargs.get('CreatedTime'))
                if kwargs.get('UpdatedTime'):
                    filter_list.append(cls.UpdatedTime == kwargs.get('UpdatedTime'))
                
            res = db.session.query(cls).filter(*filter_list).with_for_update()

            results = {
                'delete_time': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'CountryID': []
            }
            for query_model in res.all():
                results['CountryID'].append(query_model.CountryID)

            res.update({'isDeleted': 1})
            db.session.commit()

            return {'code': RET.OK, 'message': error_map_EN[RET.OK], 'data': results}

        except Exception as e:
            db.session.rollback()
            loggings.exception(1, e)
            return {'code': RET.DBERR, 'message': error_map_EN[RET.DBERR], 'data': {'error': str(e)}}
        finally:
            db.session.close()
    
    # update
    @classmethod
    def update(cls, **kwargs):
        try:
            
            
            filter_list = [cls.isDeleted == 0]
            filter_list.append(cls.CountryID == kwargs.get('CountryID'))
            
            res = db.session.query(cls).filter(*filter_list).with_for_update()

            results = {
                'update_time': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'CountryID': res.first().CountryID,
                
            }
            
            res.update(kwargs)
            db.session.commit()

            return {'code': RET.OK, 'message': error_map_EN[RET.OK], 'data': results}

        except Exception as e:
            db.session.rollback()
            loggings.exception(1, e)
            return {'code': RET.DBERR, 'message': error_map_EN[RET.DBERR], 'data': {'error': str(e)}}
        finally:
            db.session.close()

    # batch add
    @classmethod
    def add_list(cls, **kwargs):
        param_list = json.loads(kwargs.get('CountryList'))
        model_list = []
        for param_dict in param_list:
            from utils.generate_id import GenerateID
            CountryID = GenerateID.create_random_id()
            
            model = Country(
                CountryID=CountryID,
                CountryName=param_dict.get('CountryName'),
                CreatedTime=param_dict.get('CreatedTime'),
                UpdatedTime=param_dict.get('UpdatedTime'),
                
            )
            model_list.append(model)
        
        try:
            db.session.add_all(model_list)
            db.session.commit()
            results = {
                'added_records': [],
                'add_time': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            for model in model_list:
                added_record = {}
                added_record['CountryID'] = model.CountryID
                
                results['added_records'].append(added_record)
                
            return {'code': RET.OK, 'message': error_map_EN[RET.OK], 'data': results}
            
        except Exception as e:
            db.session.rollback()
            loggings.exception(1, e)
            return {'code': RET.DBERR, 'message': error_map_EN[RET.DBERR], 'data': {'error': str(e)}}
        finally:
            db.session.close()
