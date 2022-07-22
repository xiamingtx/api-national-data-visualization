#!/usr/bin/env python
# -*- coding:utf-8 -*-

import pytest
from utils.response_code import RET
from .datas import add_datas,get_datas,delete_datas,update_datas,addlist_datas
from controller.countryInfoController import CountryInfoController


@pytest.mark.controller
def test_add():
    for data in add_datas:
        result = CountryInfoController.add(**data)
        assert result['code'] == RET.OK


@pytest.mark.controller
def test_get():
    for data in get_datas:
        result = CountryInfoController.get(**data)
        assert result['code'] == RET.OK


@pytest.mark.controller
def test_delete():
    for data in delete_datas:
        result = CountryInfoController.delete(**data)
        assert result['code'] == RET.OK


@pytest.mark.controller
def test_update():
    for data in update_datas:
        result = CountryInfoController.update(**data)
        assert result['code'] == RET.OK


@pytest.mark.controller
def test_addlist():
    for data in addlist_datas:
        result = CountryInfoController.add_list(**data)
        assert result['code'] == RET.OK