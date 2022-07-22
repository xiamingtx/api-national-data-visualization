#!/usr/bin/env python
# -*- coding:utf-8 -*-

import json
import requests


def printResponse(response):
    print('\n\n------------------------------------------')
    print(response.status_code)

    for k, v in response.headers.items():
        print(f'{k}: {v}')

    print('')

    print(response.content.decode('utf8'))
    print('------------------------------------------\n\n')


# 模拟登录,获取token
def get_token(api_url, request_data):
    response = requests.post(
        api_url,
        data=request_data
    )

    response_data_dict = json.loads(response.text)
    token = response_data_dict['data']['Token']
    # printResponse(response)
    print('token:', token)
    return token
    