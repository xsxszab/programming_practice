#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 14:39:45 2018

@author: xsxsz
"""

import re

key1 = "<h1>hello world<h1>"
p1 = "<h1>.+<h1>"
pattern1 = re.compile(p1)
print(pattern1.findall(key1))
print('-----------')
key2='1238927458@abcd.com.cn'
p2='1238927458@abcd\.com\.cn'
pattern2=re.compile(p2)
print(pattern2.findall(key2))
print('-----------')
