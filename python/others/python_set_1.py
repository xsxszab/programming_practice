#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 22:27:43 2019

@author: xsxsz
"""

s=set()
for i in range(10):
    s.add(i)
print(s)
print('-------------')
print(type(s))
print('-------------')
s.add(7)
print(s)
print('-------------')
s.add('7')
print(s)
print('-------------')
arr=(11,12,13,14)
s.update(arr)
print(s)
print('-------------')
s.remove('7')
print(s)
print('-------------')
s.pop()
print(s)
print('-------------')
s.clear()
print(s)
print('-------------')
