# coding: utf-8
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()



class Country(db.Model):
    __tablename__ = 'country'

    CountryID = db.Column(db.Integer, primary_key=True)
    CountryName = db.Column(db.String(64, 'utf8mb4_0900_ai_ci'))
    isDeleted = db.Column(db.Integer, server_default=db.FetchedValue())
    CreatedTime = db.Column(db.DateTime, server_default=db.FetchedValue())
    UpdatedTime = db.Column(db.DateTime, server_default=db.FetchedValue())
