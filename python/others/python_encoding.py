#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 07:43:38 2018

@author: xsxsz
"""

string1='文件'
print(string1)
print('----------')
string2=string1.encode('utf-8')
print(type(string2))
print('----------')
print(string2)
print('----------')
print(string2.decode('utf-8'))
print('----------')
try:
    print(string2.decode('ascii'))
except UnicodeDecodeError:
    print('decoding error')

