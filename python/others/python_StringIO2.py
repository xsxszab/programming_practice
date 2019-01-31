#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 15:44:20 2019

@author: xsxsz
"""

from io import StringIO

f=StringIO('abcd\nefgh\nijkl\n')
print(f.getvalue())
print('------------')
while True:
    s=f.readline()
    if s=='':
        break
    print(s.strip())
print('------------')
