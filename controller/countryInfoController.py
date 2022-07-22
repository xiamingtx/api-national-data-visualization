#!/usr/bin/env python
# -*- coding:utf-8 -*-

import datetime
import math
import json

from sqlalchemy import or_

from app import db
from models.countryInfoModel import CountryInfo
from utils import commons
from utils.response_code import RET, error_map_EN
from utils.loggings import loggings


class CountryInfoController(CountryInfo):

    # add
    @classmethod
    def add(cls, **kwargs):
        from utils.generate_id import GenerateID
        CountryInfoID = GenerateID.create_random_id()
        
        try:
            model = CountryInfo(
                CountryInfoID=CountryInfoID,
                CountryID=kwargs.get('CountryID'),
                GDP=kwargs.get('GDP'),
                PrimaryIndustry=kwargs.get('PrimaryIndustry'),
                SecondaryIndustry=kwargs.get('SecondaryIndustry'),
                TertiaryIndustry=kwargs.get('TertiaryIndustry'),
                FarmingIndustry=kwargs.get('FarmingIndustry'),
                Industry=kwargs.get('Industry'),
                 ConstructionIndustry=kwargs.get(' ConstructionIndustry'),
                WholesaleAndRetail=kwargs.get('WholesaleAndRetail'),
                TransportationAndStorage=kwargs.get('TransportationAndStorage'),
                AccommodationAndCatering=kwargs.get('AccommodationAndCatering'),
                FinancialBusiness=kwargs.get('FinancialBusiness'),
                RealtyBusiness=kwargs.get('RealtyBusiness'),
                Others=kwargs.get('Others'),
                InfoYear=kwargs.get('InfoYear'),
                CreatedTime=kwargs.get('CreatedTime'),
                DeletedTime=kwargs.get('DeletedTime'),
                
            )
            db.session.add(model)
            db.session.commit()
            results = {
                'add_time': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'CountryInfoID': model.CountryInfoID,
                
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
            filter_list = [cls.IsDeleted == 0]
            if kwargs.get('CountryInfoID'):
                filter_list.append(cls.CountryInfoID == kwargs['CountryInfoID'])
            else:
                if kwargs.get('CountryID') is not None:
                    filter_list.append(cls.CountryID == kwargs.get('CountryID'))
                if kwargs.get('GDP') is not None:
                    filter_list.append(cls.GDP == kwargs.get('GDP'))
                if kwargs.get('PrimaryIndustry') is not None:
                    filter_list.append(cls.PrimaryIndustry == kwargs.get('PrimaryIndustry'))
                if kwargs.get('SecondaryIndustry') is not None:
                    filter_list.append(cls.SecondaryIndustry == kwargs.get('SecondaryIndustry'))
                if kwargs.get('TertiaryIndustry') is not None:
                    filter_list.append(cls.TertiaryIndustry == kwargs.get('TertiaryIndustry'))
                if kwargs.get('FarmingIndustry') is not None:
                    filter_list.append(cls.FarmingIndustry == kwargs.get('FarmingIndustry'))
                if kwargs.get('Industry') is not None:
                    filter_list.append(cls.Industry == kwargs.get('Industry'))
                if kwargs.get(' ConstructionIndustry') is not None:
                    filter_list.append(cls. ConstructionIndustry == kwargs.get(' ConstructionIndustry'))
                if kwargs.get('WholesaleAndRetail') is not None:
                    filter_list.append(cls.WholesaleAndRetail == kwargs.get('WholesaleAndRetail'))
                if kwargs.get('TransportationAndStorage') is not None:
                    filter_list.append(cls.TransportationAndStorage == kwargs.get('TransportationAndStorage'))
                if kwargs.get('AccommodationAndCatering') is not None:
                    filter_list.append(cls.AccommodationAndCatering == kwargs.get('AccommodationAndCatering'))
                if kwargs.get('FinancialBusiness') is not None:
                    filter_list.append(cls.FinancialBusiness == kwargs.get('FinancialBusiness'))
                if kwargs.get('RealtyBusiness') is not None:
                    filter_list.append(cls.RealtyBusiness == kwargs.get('RealtyBusiness'))
                if kwargs.get('Others') is not None:
                    filter_list.append(cls.Others == kwargs.get('Others'))
                if kwargs.get('InfoYear') is not None:
                    filter_list.append(cls.InfoYear == kwargs.get('InfoYear'))
                if kwargs.get('CreatedTime'):
                    filter_list.append(cls.CreatedTime == kwargs.get('CreatedTime'))
                if kwargs.get('DeletedTime'):
                    filter_list.append(cls.DeletedTime == kwargs.get('DeletedTime'))
                

            page = int(kwargs.get('Page', 1))
            size = int(kwargs.get('Size', 10))
            
            country_info_info = db.session.query(cls).filter(*filter_list)
            
            count = country_info_info.count()
            pages = math.ceil(count / size)
            country_info_info = country_info_info.limit(size).offset((page - 1) * size).all()
   
            results = commons.query_to_dict(country_info_info)
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
            filter_list = [cls.IsDeleted == 0]
            if kwargs.get('CountryInfoID'):
                primary_key_list = []
                for primary_key in str(kwargs.get('CountryInfoID')).replace(' ', '').split(','):
                    primary_key_list.append(cls.CountryInfoID == primary_key)
                filter_list.append(or_(*primary_key_list))
                
            else:
                if kwargs.get('CountryID') is not None:
                    filter_list.append(cls.CountryID == kwargs.get('CountryID'))
                if kwargs.get('GDP') is not None:
                    filter_list.append(cls.GDP == kwargs.get('GDP'))
                if kwargs.get('PrimaryIndustry') is not None:
                    filter_list.append(cls.PrimaryIndustry == kwargs.get('PrimaryIndustry'))
                if kwargs.get('SecondaryIndustry') is not None:
                    filter_list.append(cls.SecondaryIndustry == kwargs.get('SecondaryIndustry'))
                if kwargs.get('TertiaryIndustry') is not None:
                    filter_list.append(cls.TertiaryIndustry == kwargs.get('TertiaryIndustry'))
                if kwargs.get('FarmingIndustry') is not None:
                    filter_list.append(cls.FarmingIndustry == kwargs.get('FarmingIndustry'))
                if kwargs.get('Industry') is not None:
                    filter_list.append(cls.Industry == kwargs.get('Industry'))
                if kwargs.get(' ConstructionIndustry') is not None:
                    filter_list.append(cls. ConstructionIndustry == kwargs.get(' ConstructionIndustry'))
                if kwargs.get('WholesaleAndRetail') is not None:
                    filter_list.append(cls.WholesaleAndRetail == kwargs.get('WholesaleAndRetail'))
                if kwargs.get('TransportationAndStorage') is not None:
                    filter_list.append(cls.TransportationAndStorage == kwargs.get('TransportationAndStorage'))
                if kwargs.get('AccommodationAndCatering') is not None:
                    filter_list.append(cls.AccommodationAndCatering == kwargs.get('AccommodationAndCatering'))
                if kwargs.get('FinancialBusiness') is not None:
                    filter_list.append(cls.FinancialBusiness == kwargs.get('FinancialBusiness'))
                if kwargs.get('RealtyBusiness') is not None:
                    filter_list.append(cls.RealtyBusiness == kwargs.get('RealtyBusiness'))
                if kwargs.get('Others') is not None:
                    filter_list.append(cls.Others == kwargs.get('Others'))
                if kwargs.get('InfoYear') is not None:
                    filter_list.append(cls.InfoYear == kwargs.get('InfoYear'))
                if kwargs.get('CreatedTime'):
                    filter_list.append(cls.CreatedTime == kwargs.get('CreatedTime'))
                if kwargs.get('DeletedTime'):
                    filter_list.append(cls.DeletedTime == kwargs.get('DeletedTime'))
                
            res = db.session.query(cls).filter(*filter_list).with_for_update()

            results = {
                'delete_time': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'CountryInfoID': []
            }
            for query_model in res.all():
                results['CountryInfoID'].append(query_model.CountryInfoID)

            res.update({'IsDeleted': 1})
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
            
            
            filter_list = [cls.IsDeleted == 0]
            filter_list.append(cls.CountryInfoID == kwargs.get('CountryInfoID'))
            
            res = db.session.query(cls).filter(*filter_list).with_for_update()

            results = {
                'update_time': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'CountryInfoID': res.first().CountryInfoID,
                
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
        param_list = json.loads(kwargs.get('CountryInfoList'))
        model_list = []
        for param_dict in param_list:
            from utils.generate_id import GenerateID
            CountryInfoID = GenerateID.create_random_id()
            
            model = CountryInfo(
                CountryInfoID=CountryInfoID,
                CountryID=param_dict.get('CountryID'),
                GDP=param_dict.get('GDP'),
                PrimaryIndustry=param_dict.get('PrimaryIndustry'),
                SecondaryIndustry=param_dict.get('SecondaryIndustry'),
                TertiaryIndustry=param_dict.get('TertiaryIndustry'),
                FarmingIndustry=param_dict.get('FarmingIndustry'),
                Industry=param_dict.get('Industry'),
                 ConstructionIndustry=param_dict.get(' ConstructionIndustry'),
                WholesaleAndRetail=param_dict.get('WholesaleAndRetail'),
                TransportationAndStorage=param_dict.get('TransportationAndStorage'),
                AccommodationAndCatering=param_dict.get('AccommodationAndCatering'),
                FinancialBusiness=param_dict.get('FinancialBusiness'),
                RealtyBusiness=param_dict.get('RealtyBusiness'),
                Others=param_dict.get('Others'),
                InfoYear=param_dict.get('InfoYear'),
                CreatedTime=param_dict.get('CreatedTime'),
                DeletedTime=param_dict.get('DeletedTime'),
                
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
                added_record['CountryInfoID'] = model.CountryInfoID
                
                results['added_records'].append(added_record)
                
            return {'code': RET.OK, 'message': error_map_EN[RET.OK], 'data': results}
            
        except Exception as e:
            db.session.rollback()
            loggings.exception(1, e)
            return {'code': RET.DBERR, 'message': error_map_EN[RET.DBERR], 'data': {'error': str(e)}}
        finally:
            db.session.close()
