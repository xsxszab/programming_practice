# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 16:22:56 2018

@author: Administrator
"""

def dec(func):
    print 'This is a function'
    return func

@dec
def add(a,b):
    return a+b
print'----------'

def dec1(func):
    print'111111111'
    def one():
        print'22222222'
        func()
        print '333333333'
    return one

def dec2(func):
    print'aaaaaaaaaaa'
    def two():
        print'bbbbbbb'
        func()
        print'cccccccccc'
    return two

@dec1
@dec2
def test():
    print 'test'

test()