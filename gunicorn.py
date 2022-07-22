#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
    gunicorn启动文件
"""

import os
import sys


def start():
    cmd = 'source /deploy/app/venv/bin/activate;' \
          'cd /deploy/your project;' \
          'gunicorn -c deploy/gunicorn.conf manage:app -D'
    os.system(cmd)


def stop():
    cmd = "ps -ef | grep 'api_national_data_visualization/bin/gunicorn' | grep -v grep | awk '{print $2}' | xargs kill -9"
    os.system(cmd)


def restart():
    stop()
    start()


if sys.argv[1] == 'start':
    start()
elif sys.argv[1] == 'restart':
    restart()
elif sys.argv[1] == 'stop':
    stop()
else:
    print('params error!')
