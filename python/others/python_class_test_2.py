# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 08:05:39 2018

@author: Administrator
"""

class test(object):
    def __init__(itself,a,b):
        itself.a=a
        itself.b=b
    def function1(self):
        return ([self.a,self.b])
    def __str__(self):
        return 'What are you looking for?'

a=test(1,2)
print a.function1()
print a.__str__()
