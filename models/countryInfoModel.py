# coding: utf-8
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()



class CountryInfo(db.Model):
    __tablename__ = 'country_info'

    CountryInfoID = db.Column(db.Integer, primary_key=True)
    CountryID = db.Column(db.Integer, nullable=False)
    GDP = db.Column(db.Float(precision="20, 1"), info='国内生产总值(亿元)')
    GDPIncRate = db.Column(db.Float(precision="10, 1"), info='GDP增长率')
    AvgGDP = db.Column(db.Integer, info='人均GDP(万元)')
    PrimaryIndustry = db.Column(db.Float(precision="3, 1"), info='第一产业贡献率')
    SecondaryIndustry = db.Column(db.Float(precision="3, 1"), info='第二产业贡献率')
    TertiaryIndustry = db.Column(db.Float(precision="3, 1"), info='第三产业贡献率')
    FarmingIndustry = db.Column(db.Float(precision="20, 1"), info='农林渔业增加值(亿元)')
    Industry = db.Column(db.Float(precision="20, 1"), info='工业增加值(亿元)')
    ConstructionIndustry = db.Column(db.Float(precision="20, 1"), info='建筑业增加值(亿元)')
    WholesaleAndRetail = db.Column(db.Float(precision="20, 1"), info='批发和零售业增加值(亿元)')
    TransportationAndStorage = db.Column(db.Float(precision="20, 1"), info='交通运输、仓储和邮政业(亿元)')
    AccommodationAndCatering = db.Column(db.Float(precision="20, 1"), info='住宿和餐饮业增加值(亿元)')
    FinancialBusiness = db.Column(db.Float(precision="20, 1"), info='金融业增加值(亿元)')
    RealtyBusiness = db.Column(db.Float(precision="20, 1"), info='房地产业增加值(亿元)')
    Population = db.Column(db.BigInteger, info='人口数量(万人)')
    Others = db.Column(db.Float(precision="20, 1"), info='其他产业增加值(亿元)')
    InfoYear = db.Column(db.Integer)
    IsDeleted = db.Column(db.Integer, server_default=db.FetchedValue())
    CreatedTime = db.Column(db.DateTime, server_default=db.FetchedValue())
    DeletedTime = db.Column(db.DateTime, server_default=db.FetchedValue())
