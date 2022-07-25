#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:myQueue.py
# author:xm
# datetime:2022/7/25 20:23
# software: PyCharm

"""
this is function  description 
"""


# import module your need
class Queue(object):

    def __init__(self, max_size=10):
        self.max_size = max_size
        self.arr = [0 for _ in range(self.max_size)]  # 存储数据的数组
        self.hh = 0  # 队首
        self.tt = -1  # 队尾

    def push(self, val):
        if self.full():
            print('队列已满!')
            return False
        self.tt = self.tt + 1
        self.arr[self.tt] = val
        return True

    def front(self):
        if self.empty():
            print('队列为空')
            return False
        return self.arr[self.hh]

    def pop(self):
        if self.empty():
            print('队列为空')
        val = self.front()
        self.hh = self.hh + 1
        return val

    def empty(self):
        return not self.not_empty()

    def not_empty(self):
        return self.hh <= self.tt

    def full(self):
        return self.tt == self.max_size - 1

