#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 16:36:41 2018

@author: xsxsz
"""

import chardet
print(chardet.detect(b'hello world'))
print('-----------')
data = '光怪陆离'.encode('gbk')
print(chardet.detect(data))
print('-----------')
data1 = '编码'.encode('utf-8')
print(chardet.detect(data1))
print('-----------')
