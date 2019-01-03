#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 15:05:35 2018

@author: xsxsz
"""

import re

#--------<*>-----------
key1='sdhgawfwghhhhhhhhhhhhhh'
p1='gh*'
pattern1=re.compile(p1)
print(pattern1.findall(key1))
print('-------------')

#--------<?>-----------
key2='sdhgawfwghhhhhhhhhhhhhh'
p2='gh?'
pattern2=re.compile(p2)
print(pattern2.findall(key2))
print('-------------')

#--------<+>-----------
key3='sdhgawfwghhhhhhhhhhhhhh'
p3='gh+'
pattern3=re.compile(p3)
print(pattern3.findall(key3))
print('-------------')

#--------<{n}>-----------
key4='sdhgawfwghhhhhhhhhhhhhh'
p4='gh{3}'
pattern4=re.compile(p4)
print(pattern4.findall(key4))
print('-------------')

