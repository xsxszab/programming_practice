# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 15:54:12 2018

@author: Administrator
"""

def gen():
    yield 1

def value():
    return 1

ret=gen()
print ret,type(ret)
print'---------'
def gen_example():
    print 'a'
    yield 'first'
    print 'b'
    yield 'second'
    print 'c'
    
g=gen_example()
print id(g)
print'---------'
print g.next()
print'---------'
print g.next()
print'---------'
print id(g)

