# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 16:01:40 2018

@author: Administrator
"""

def generator():
    yield 1
    yield 2

for i in generator():
    print i
print'---------'
def fib():
    a,b=1,1
    while True:
        yield a
        a,b=b,a+b
a=fib()
for j in range(10):
    print a.next()