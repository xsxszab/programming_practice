# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 18:24:29 2018

@author: Administrator
"""

from numpy import *
a=mat('9 4 3;2 1 8;2 5,6')
print a
print'-------'
a=a.T
print a
print'-------'
a=a.H
print a
print'-------'
a=a.I
print a
print'-------'
b=mat(ones((3,3)))
print dot(a,b)
print'-------'
c=linspace(1,10,10,dtype=int)
d=linspace(1,20,10,dtype=int)
print c
print'-------'
print d
print'-------'
d=d.T
print d
print'-------'