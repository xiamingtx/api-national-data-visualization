#!/usr/bin/env python
# -*- coding:utf-8 -*-

from .apiVersionResource import apiversion_blueprint
from .countryResource import country_blueprint
from .countryInfoResource import countryinfo_blueprint


def init_router(app):
    from api_1_0.apiVersionResource import apiversion_blueprint
    app.register_blueprint(apiversion_blueprint, url_prefix="/api_1_0")

    # country blueprint register
    from api_1_0.countryResource import country_blueprint
    app.register_blueprint(country_blueprint, url_prefix="/api_1_0")
    
    # countryInfo blueprint register
    from api_1_0.countryInfoResource import countryinfo_blueprint
    app.register_blueprint(countryinfo_blueprint, url_prefix="/api_1_0")
    
