#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : testdemo.py
# @Author: pyeye
# @Date  : 2019/6/28
# @Desc  :

def foo():
    print("starting......")
    while True:
        res = yield 4
        print("res:", res)


if __name__ == '__main__':
    g = foo()
    print(next(g))
    print("*" * 20)
    print(next(g))



