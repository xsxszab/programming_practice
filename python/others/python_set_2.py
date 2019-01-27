#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 22:32:29 2019

@author: xsxsz
"""

s = set(('a', 'cc', 'f'))
s1 = {'a', 'f', 1, 'ww'}
print(s)
print('---------------')
print(s1)
print('---------------')
print(s-s1)
print('---------------')
print(s1-s)
print('---------------')
print(s&s1)
print('---------------')
print(s|s1)
print('---------------')
print(s^s1)
print('---------------')
print(s.issubset(s1))
print('---------------')
print(s1.issubset(s))
print('---------------')
print(s.issuperset(s1))
print('---------------')
print(s1.issuperset(s))
print('---------------')