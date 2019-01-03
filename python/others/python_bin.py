#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  8 16:10:25 2018

@author: xsxsz
"""

a=10
b=0.23
string='abcd'

print(bin(a))
print('-----------')

try:
    print(bin(b))
    print('-----------')
except TypeError:
    print('TypeError')
    print('-----------')

try:
    print(bin(string))
    print('-----------')
except TypeError:
    print('TypeError')
    print('-----------')

