#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 14:48:54 2018

@author: xsxsz
"""

import re

key1='http://sdhahguighvsg.com.cn and https://sdgrwewegelboie.io'
p1='https*://'
pattern1=re.compile(p1)
print(pattern1.findall(key1))
print('---------------')

key2='12435209358djsoklgj@ndvs.com'
p2='\w+@+\w+\.com'
pattern2=re.compile(p2)
print(pattern2.findall(key2))
print('---------------')

key3='3982759827r9dsg@abcd.ogjo.com'
p3='\w+'
pattern3=re.compile(p3)
print(pattern3.findall(key3))
print('---------------')

key4='color colour'
p4='colou?r'
pattern4=re.compile(p4)
print(pattern4.findall(key4))
print('---------------')

