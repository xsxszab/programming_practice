#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 14:31:09 2018

@author: xsxsz
"""

import re
string1='''
<html><body><h1>hello world<h1></body></html>
'''
p1='<html>'
print(re.search(pattern=p1,string=string1))
print('-----------')
string2 = "javapythonhtmlvhdl"
p2='python'
pattern2=re.compile(p2)
print(re.search(pattern2,string2))
print('-----------')
