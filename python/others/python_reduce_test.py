# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 10:28:46 2018

@author: Administrator
"""

def add(a,b):
    return a+b
def multiply(a,b):
    return a*b
list=[1,2,3,2,2,4,5,6,5,3,2,3,6]
print reduce(add,list)
print'-------------'
print reduce(multiply,list)
print'-------------'
print sum(list)
print'-------------'
