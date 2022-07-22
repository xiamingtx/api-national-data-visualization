#!/usr/bin/env python
# -*- coding:utf-8 -*-

import json
import requests
import pytest
from .datas import get_data ,delete_data,put_data ,post_data ,get_query_data,joint_query_data
from ..utils import printResponse
from utils.response_code import RET


@pytest.mark.resource
def test_get_countryInfoResource():
    api_url = "http://xxxxxx"
    for data in get_data:
        response = requests.get(
            api_url,
            params=data,
        )
        response.encoding = 'utf8'
        printResponse(response)
        assert json.loads(response.text)['code'] == RET.OK


@pytest.mark.resource
def test_delete_countryInfoResource():
    for data in delete_data:
        api_url = ""
        response = requests.delete(
            api_url,
            data=data,
        )
        response.encoding = 'utf8'
        printResponse(response)
        assert json.loads(response.text)['code'] == RET.OK


@pytest.mark.resource
def test_put_countryInfoResource():
    for data in put_data:
        api_url = ""
        response = requests.put(
            api_url,
            data=data,
        )
        response.encoding = 'utf8'
        printResponse(response)
        assert json.loads(response.text)['code'] == RET.OK


@pytest.mark.resource
def test_post_countryInfoResource():
    for data in post_data:
        api_url = ""
        response = requests.post(
            api_url,
            data=data,
        )
        response.encoding = 'utf8'
        printResponse(response)
        assert json.loads(response.text)['code'] == RET.OK


@pytest.mark.resource
def test_get_query_countryInfoResource():
    for data in get_query_data:
        api_url = ""
        response = requests.get(
            api_url,
            params=data,
        )
        response.encoding = 'utf8'
        printResponse(response)
        assert json.loads(response.text)['code'] == RET.OK


@pytest.mark.resource
def test_joint_query_countryInfoResource():
    for data in joint_query_data:
        api_url = ""
        response = requests.get(
            api_url,
            params=data,
        )
        response.encoding = 'utf8'
        printResponse(response)
        assert json.loads(response.text)['code'] == RET.OK
