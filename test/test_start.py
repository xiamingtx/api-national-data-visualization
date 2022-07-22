#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import webbrowser

import pytest
from flask import Flask, render_template
from flask_bootstrap import Bootstrap


# run all test
def start_test():
    # html report path
    dir_path = os.path.split(os.path.realpath(__file__))[0]
    html_report = r'{}\report\test_report.html'.format(dir_path)

    pytest.main(['-s', '-v', '--capture=sys', "--html={}".format(html_report)])


app = Flask(__name__, template_folder="./report", static_folder="./report/assets")
Bootstrap(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("test_report.html")


if __name__ == '__main__':
    start_test()
    webbrowser.open('http://127.0.0.1:8001')
    app.run(port=8001)
